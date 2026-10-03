# -*- coding: utf-8 -*-
"""通用 C 头文件解析：把厂商 SDK 头文件解析成 IR（枚举 / 结构体 / 字段 / 函数）。

这里**不含任何厂商特定的 if/else**。厂商差异（api 宏、调用约定、函数前缀、
头文件路径等）通过 config/*.py 以数据 + hook 传入：

  - 数据：`make_func_re(api_macro, callconv, func_prefix)` 由 config 提供的
    三个字段拼出函数正则；`parse_funcs(text, func_re)` 接受它作为参数。
  - hook：厂商特有的坑（比如大华的多别名 typedef、海康的嵌套 union）通过
    覆盖本模块里的默认函数实现。目前默认实现就是「大华验证过」的那套，
    海康要覆盖时再在 config 里挂 hook。

IR 结构（元组，保持与旧 gen_dh_bind.py 完全一致）：

  enums        [(name, [(item_name, value_expr_or_None), ...]), ...]
  structs      [(name, [(ftype, fname, arr_or_None), ...]), ...]
  funcs        [(name, ret, [param_dict, ...]), ...]
"""
import collections
import re


# ------------------------------------------------------------------ 正则

# typedef struct [tag] { ... } Name;     体内不含花括号（含 union/嵌套的会被跳过）
# 注意结尾不能只吃一个名字：大华大量写成
#     } NET_TIME, *LPNET_TIME;
#     } DH_POINT, *LPDH_POINT, NET_POINT, *LPNET_POINT;
# 只抓一个名字会让整个结构体漏掉，其字段随之被判为未知类型。
STRUCT_RE = re.compile(r'typedef\s+struct\s*(?:\w+\s*)?\{([^{}]*)\}\s*([^;]+);', re.S)

# typedef enum [tag] { ... } Name;
ENUM_RE = re.compile(r'typedef\s+enum\s*(?:\w+\s*)?\{([^{}]*)\}\s*(\w+)\s*;', re.S)

FIELD_RE = re.compile(
    r'^[ \t]*(?:(?:const|volatile|static)\s+)*'
    r'((?:unsigned\s+|signed\s+)*(?:long\s+)?(?:int|char|short|long|float|double)?'
    r'[A-Za-z_]\w*(?:\s*\*)*)'
    r'\s+([A-Za-z_]\w*)\s*(\[[^\]]*\])?\s*;',
    re.M)

# typedef int (CALLBACK *fXxx)(...);
# 调用约定在头文件里常常是宏（CALLBACK / CALL_METHOD ...），写死列表必然漏。
# 漏了 CALL_METHOD 就会让 fNotifyXxx 这类字段被当成普通类型去 def_rw，触发 C2440。
FP_RE = re.compile(r'typedef\s+[^(;]*\(\s*(?:[A-Za-z_]\w*\s+)?\*\s*(\w+)\s*\)\s*\(')

# typedef 出来的普通类型别名（DWORD / LLONG / BYTE ...），用于字段白名单
TYPEDEF_NAME_RE = re.compile(r'typedef\s+(?!struct\b|union\b|enum\b)[^;{()]*?([A-Za-z_]\w*)\s*;')

# 大华把一批类型别名写成宏：#define DWORD unsigned int / #define BYTE unsigned char
# 这些在 MSVC 下实际来自 windows.h，解析文本时只能靠 #define 认出来
DEFINE_NAME_RE = re.compile(r'^\s*#\s*define\s+([A-Za-z_]\w*)\b', re.M)

ENUM_ITEM_RE = re.compile(r'([A-Za-z_]\w*)\s*(?:=\s*([^,\n]+?))?\s*(?=,|\n|$)', re.M)

# C++ 关键字 / 无意义的"类型名"
RESERVED_WORDS = {'struct', 'union', 'enum', 'const', 'volatile', 'static', 'unsigned', 'signed'}

# 语言自带的标量类型
BASE_TYPES = {
    'void', 'bool', 'char', 'short', 'int', 'long', 'float', 'double',
    '__int8', '__int16', '__int32', '__int64', 'size_t', 'wchar_t',
}

# Windows 句柄 / 不透明指针：本质是 void* 的 typedef，参数里看不到 *，
# 但必须当指针暴露成 uintptr_t，否则 nanobind 找不到 caster。
OPAQUE_PTR = {
    'HWND', 'HDC', 'HANDLE', 'HMODULE', 'HINSTANCE', 'LPVOID',
    'LPARAM', 'WPARAM', 'HGLRC', 'HICON', 'HCURSOR', 'HBRUSH', 'HFONT', 'HPEN',
}


def strip_comments(text):
    """去掉块注释和行注释，避免注释里的分号/花括号干扰正则。"""
    text = re.sub(r'/\*.*?\*/', ' ', text, flags=re.S)
    text = re.sub(r'//[^\n]*', ' ', text)
    return text


def make_func_re(api_macro, callconv, func_prefix):
    """按厂商的 api 宏 / 调用约定 / 函数前缀拼出函数声明正则。

    callconv 是正则片段：大华传 'CALL_METHOD'，海康传
    '(?:__stdcall|CALLBACK|WINAPI)'（海康函数声明里三种调用约定混用）。
    """
    return re.compile(
        r'%s\s+([A-Za-z_][\w\s*]*?)\s+%s\s+(%s\w+)\s*\(([^)]*)\)\s*;'
        % (api_macro, callconv, func_prefix), re.S)


# ------------------------------------------------------------------ 结构体 / 枚举

def parse_header(path):
    raw = open(path, encoding='latin-1', errors='replace').read()
    text = strip_comments(raw)

    fp_types = set(FP_RE.findall(text))
    typedef_names = set(TYPEDEF_NAME_RE.findall(text)) - fp_types
    define_names = set(DEFINE_NAME_RE.findall(text))

    # ---- 枚举 ----
    enums = []           # (name, [(item_name, value_expr or None), ...])
    enum_names = set()
    for m in ENUM_RE.finditer(text):
        body, name = m.group(1), m.group(2)
        if name in enum_names:
            continue
        items = []
        for im in ENUM_ITEM_RE.finditer(body):
            iname, ival = im.group(1), im.group(2)
            if iname in RESERVED_WORDS:
                continue
            items.append((iname, (ival or '').strip() or None))
        if items:
            enum_names.add(name)
            enums.append((name, items))

    # ---- 结构体 ----
    # 先收集全部结构体名，再回头提字段：字段类型白名单需要完整的名字集合，
    # 否则引用「后面才定义」的结构体会被误判成未知类型。
    raw_structs = []
    struct_names = set()
    struct_aliases = set()
    for m in STRUCT_RE.finditer(text):
        body, decl = m.group(1), m.group(2)
        names = []
        for part in decl.split(','):
            part = part.strip()
            if not part or part.startswith('*'):
                continue            # *LPNET_TIME 这类指针别名，不构成新类型
            mm = re.match(r'([A-Za-z_]\w*)', part)
            if mm:
                names.append(mm.group(1))
        if not names:
            continue
        name = names[0]
        # 其余名字是同一 C++ 类型的别名：不能重复注册 nb::class_（否则报
        # already registered），但必须进白名单，否则用别名的字段会被当成
        # 未知类型整个跳过，功能静默缺失。
        struct_aliases.update(names[1:])
        if name in struct_names:
            continue
        struct_names.add(name)
        raw_structs.append((name, body))

    bindable = (struct_names | struct_aliases | enum_names
                | typedef_names | define_names | BASE_TYPES)

    structs = []         # (name, [(ftype, fname, arr_or_None), ...])
    stats = collections.Counter()
    for name, body in raw_structs:
        fields = []
        for fm in FIELD_RE.finditer(body):
            ftype, fname, arr = fm.group(1).strip(), fm.group(2), fm.group(3)
            if fname in RESERVED_WORDS:
                stats['skip_reserved'] += 1
                continue
            if '(' in ftype or ftype in fp_types:
                stats['skip_funcptr'] += 1
                continue
            base = ftype.replace('unsigned', ' ').replace('signed', ' ').strip()
            base = base.rstrip('*').strip()
            if '*' not in ftype and base not in bindable:
                # 既不是基本类型，也不是已知 typedef / 结构体 / 枚举。
                # 极可能是漏网的函数指针或外部类型，硬绑必然编译失败（C2440）。
                stats['skip_unknown'] += 1
                stats['unknown_' + base] += 1
                continue
            fields.append((ftype, fname, arr))
        if not fields:
            continue
        structs.append((name, fields))

    return enums, enum_names, structs, struct_names, fp_types, stats, typedef_names


# ------------------------------------------------------------------ 函数

def parse_param(part):
    """解析单个参数文本：'const char *pName' / 'LLONG lLoginID' / 'unsigned char'。

    返回 dict(type/name/has_default)，type 是完整类型（含 const/unsigned/指针），
    name 可能为 None（有些函数只有类型没有参数名）。"""
    has_default = '=' in part
    part = re.sub(r'\s*=\s*.+$', '', part).strip()
    if not part:
        return None
    m = re.match(
        r'((?:const\s+)?(?:unsigned\s+|signed\s+|long\s+|short\s+)?'
        r'[A-Za-z_]\w*\s*\**)\s*([A-Za-z_]\w*)?', part)
    if not m or not m.group(1):
        return None
    return {'type': m.group(1).strip(), 'name': m.group(2) or None,
            'has_default': has_default}


def classify_param(p, struct_names, enum_names, fp_types):
    """参数分类。返回 'skip'/'callback' 表示该函数不能直接绑。"""
    t = p['type']
    core = re.sub(r'^const\s+', '', t)
    ptr = '*' in core
    base = core.replace('*', '').strip()
    if base in fp_types:
        return 'funcptr'
    if base in OPAQUE_PTR:
        return 'uintptr'
    if ptr:
        if base in ('void', 'LPVOID', 'HWND', 'HDC'):
            return 'uintptr'
        if base == 'char' and t.startswith('const'):
            return 'cstr'
        if base in struct_names or base in enum_names:
            return 'objptr'
        # int* / DWORD* / char*（非 const）等：暴露为地址，Python 侧用
        # ctypes 预分配缓冲或传 0。输出指针不再整个跳过。
        return 'outptr'
    if base == 'void':
        return 'skip'
    return 'value'


def parse_funcs(text, func_re):
    """提取全部函数签名。返回 [(name, ret, [param_dict, ...]), ...]"""
    funcs = []
    seen = set()
    for m in func_re.finditer(text):
        ret = m.group(1).strip()
        name = m.group(2)
        if name in seen:
            continue
        seen.add(name)
        params = []
        bad = False
        args_s = m.group(3).strip()
        if args_s and args_s not in ('void', 'VOID'):
            for part in args_s.split(','):
                p = parse_param(part)
                if p is None:
                    bad = True
                    break
                params.append(p)
        if not bad:
            funcs.append((name, ret, params))
    return funcs


def gen_func(name, ret, params, struct_names, enum_names, fp_types):
    """生成单个函数的 m.def 代码；返回 (lines, None) 或 (None, 跳过原因)。"""
    cpp_args, nb_args, call_args = [], [], []
    for idx, p in enumerate(params):
        kind = classify_param(p, struct_names, enum_names, fp_types)
        if kind == 'skip':
            return None, kind
        t = p['type']
        n = p['name'] or ('arg%d' % idx)   # 无名参数补一个占位名
        if kind == 'value':
            cpp_args.append('%s %s' % (t, n))
            call_args.append(n)
        elif kind in ('uintptr', 'funcptr', 'outptr'):
            # 不透明指针 / 回调 / 输出指针：一律暴露成地址，可传 0
            cpp_args.append('std::uintptr_t %s' % n)
            call_args.append('reinterpret_cast<%s>(%s)' % (t, n))
        elif kind == 'cstr':
            cpp_args.append('const std::string &%s' % n)
            call_args.append('%s.c_str()' % n)
        elif kind == 'objptr':
            # const T* 会破坏 nanobind 的 type_caster<T*>，转成 T*（非 const
            # 指针可隐式转 const，不影响调用）
            t_clean = re.sub(r'^const\s+', '', t)
            cpp_args.append('%s %s' % (t_clean, n))
            call_args.append(n)
        if p.get('has_default'):
            nb_args.append('nb::arg("%s") = 0' % n)
        else:
            nb_args.append('nb::arg("%s")' % n)

    sig = ', '.join(cpp_args)
    call = ', '.join(call_args)
    ret_ann = '' if ret == 'void' else ' -> %s' % ret
    tail = (', ' + ', '.join(nb_args)) if nb_args else ''
    lines = [
        '    m.def("%s",' % name,
        '        [](%s)%s { return %s(%s); }%s)' % (sig, ret_ann, name, call, tail),
    ]
    return lines, None


# ------------------------------------------------------------------ 依赖与拓扑

def build_deps(structs, struct_names):
    """deps[A] = {B, ...} 表示 A 的字段里出现了类型 B（需要 B 先注册）。"""
    deps = {}
    for name, fields in structs:
        d = set()
        for ftype, _fname, _arr in fields:
            base = ftype.replace('unsigned', ' ').replace('signed', ' ').strip()
            base = base.rstrip('*').strip()
            if base in struct_names and base != name:
                d.add(base)
        deps[name] = d
    return deps


def topo_order(structs, deps):
    """返回结构体名的拓扑序：被依赖者在前。有环时把剩余部分附加到末尾。"""
    names = [n for n, _ in structs]
    indeg = {n: 0 for n in names}
    rdeps = collections.defaultdict(list)   # d -> [依赖 d 的类型]
    for n in names:
        for d in deps.get(n, ()):
            if d in indeg and d != n:
                indeg[n] += 1
                rdeps[d].append(n)

    # 稳定起见，按原出现顺序处理入度为 0 的节点
    queue = [n for n in names if indeg[n] == 0]
    order = []
    while queue:
        cur = queue.pop(0)
        order.append(cur)
        for m in rdeps[cur]:
            indeg[m] -= 1
            if indeg[m] == 0:
                queue.append(m)
    if len(order) < len(names):
        order += [n for n in names if n not in set(order)]
    return order
