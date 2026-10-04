# -*- coding: utf-8 -*-
"""通用 C 头文件解析：把厂商 SDK 头文件解析成 IR（枚举 / 结构体 / 字段 / 函数）。

这里**不含任何厂商特定的 if/else**。厂商差异（api 宏、调用约定、函数前缀、
头文件路径等）通过 config/*.py 以数据 + hook 传入：

  - 数据：`make_func_re(api_macro, callconv, func_prefix)` 由 config 提供的
    三个字段拼出函数正则；`parse_funcs(text, func_re)` 接受它作为参数。
  - 扩展点：解析被拆成细粒度函数（_collect_enums / _collect_structs /
    _collect_unions / _extract_fields / _split_decl_names ...）。若某家头文件
    出现真怪癖，覆盖对应函数即可。当前两家都落在「通用 C 语法」上，无需
    覆盖——实测标量别名大华用 #define、海康用 typedef，但双收集已统一覆盖。

IR 结构（元组，保持与旧 gen_dh_bind.py 完全一致）：

  enums        [(name, [(item_name, value_expr_or_None), ...]), ...]
  structs      [(name, [(ftype, fname, arr_or_None), ...]), ...]
  funcs        [(name, ret, [param_dict, ...]), ...]
  callbacks    [(name, ret, [param_dict, ...]), ...]

  **踩过的坑见 docs/implementation-notes.md**。本文件里几处"看起来可以简化"的
  判定全是踩出来的，注释标了原因，别"优化"掉：
  - 回调参数分类靠**参数名**而非位置，且数量关键词 `$` 锚定（第四节 4.2/4.4）
  - `ptr_aliases`：厂商用 `LPNET_X` 写指针，类型名里没有 `*`（第四节 4.1）
  - 生成代码必须纯 ASCII，否则 MSVC 报 C4819（第三节 3.3）
  """
import collections
import re


# ------------------------------------------------------------------ 正则

# typedef struct [tag] { ... } Name;     体内可能含嵌套 union/struct，必须用
# 平衡花括号匹配（_find_typedef_structs），不能再靠 [^{}]* 扁平正则——那会让
# 含匿名 union 的结构体（如 NET_DEVICEINFO）整个漏掉。
# 注意结尾不能只吃一个名字：厂商 SDK 大量写成
#     } NET_TIME, *LPNET_TIME;
#     } DH_POINT, *LPDH_POINT, NET_POINT, *LPNET_POINT;
# 只抓一个名字会让整个结构体漏掉，其字段随之被判为未知类型。
STRUCT_HEAD_RE = re.compile(r'typedef\s+struct\s*(?:\w+\s*)?\{')

# typedef enum [tag] { ... } Name;
ENUM_RE = re.compile(r'typedef\s+enum\s*(?:\w+\s*)?\{([^{}]*)\}\s*(\w+)\s*;', re.S)

# typedef union [tag] { ... } Name;   体内同样不含嵌套花括号。
# union 成员共享一块内存，字段按 bytes 暴露（见 emit.gen_fields），
# 类型名只需进白名单，不必注册 nb::class_。
UNION_RE = re.compile(r'typedef\s+union\s*(?:\w+\s*)?\{([^{}]*)\}\s*([^;]+);', re.S)

# 匹配单个字段声明（不含分号）。数组部分吃多个维度：[4][32] 这类二维也认。
FIELD_RE = re.compile(
    r'^\s*(?:(?:const|volatile|static)\s+)*'
    r'((?:unsigned\s+|signed\s+)*(?:long\s+)?(?:int|char|short|long|float|double)?'
    r'[A-Za-z_]\w*(?:\s*\*)*)'
    r'\s+([A-Za-z_]\w*)\s*((?:\[[^\]]*\])*)')

# typedef int (CALLBACK *fXxx)(...);
# 调用约定在头文件里常常是宏（CALLBACK / CALL_METHOD ...），写死列表必然漏。
# 漏了 CALL_METHOD 就会让 fNotifyXxx 这类字段被当成普通类型去 def_rw，触发 C2440。
FP_RE = re.compile(r'typedef\s+[^(;]*\(\s*(?:[A-Za-z_]\w*\s+)?\*\s*(\w+)\s*\)\s*\(')

# typedef 出来的普通类型别名（DWORD / LLONG / BYTE ...），用于字段白名单
TYPEDEF_NAME_RE = re.compile(r'typedef\s+(?!struct\b|union\b|enum\b)[^;{()]*?([A-Za-z_]\w*)\s*;')

# 类型别名的两种写法，两家各占一种，都要收进白名单：
#   大华：标量别名是宏    #define DWORD unsigned int / #define BYTE unsigned char
#   海康：标量别名是 typedef  typedef unsigned char BYTE;  （仅 BOOL 仍是 #define）
# 解析文本时 #define 与 typedef 必须都收集，否则对应字段被判未知类型。
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

def _brace_match(text, open_pos):
    """从 open_pos（指向 '{'）找到匹配的 '}' 下标。"""
    depth = 0
    i = open_pos
    while i < len(text):
        c = text[i]
        if c == '{':
            depth += 1
        elif c == '}':
            depth -= 1
            if depth == 0:
                return i
        i += 1
    return len(text) - 1


def _find_typedef_structs(text):
    """用平衡花括号匹配找出所有 typedef struct {...} Name;，含嵌套的。

    返回 [(body, decl), ...]。body 是花括号内完整文本（含嵌套 union/struct），
    decl 是 } 到 ; 之间的名字列表文本。
    """
    found = []
    for m in STRUCT_HEAD_RE.finditer(text):
        open_pos = m.end() - 1          # '{' 的位置
        close_pos = _brace_match(text, open_pos)
        body = text[m.end():close_pos]
        after = text[close_pos + 1:]
        semi = after.find(';')
        decl = after[:semi] if semi != -1 else ''
        found.append((body, decl))
    return found


def _normalize(ftype):
    """剥离 unsigned/signed 修饰符和指针，返回基础类型名。"""
    base = ftype.replace('unsigned', ' ').replace('signed', ' ').strip()
    return base.rstrip('*').strip()


def _split_decl_names(decl):
    """拆分 typedef 结尾的名字列表：'NET_TIME, *LPNET_TIME'。

    返回 (类型名列表, 指针别名字典 {别名: 目标类型})。

    指针别名（*LPNET_TIME）不构成新类型，不能注册 nb::class_，但**必须单独
    收集起来**：厂商头文件写回调签名和结构体字段时都经常直接用别名而不带
    星号，例如
        fQueryRecordFileCallBack(LLONG, LPNET_RECORDFILE_INFO pFileinfos, int nFileNum, ...)
        typedef struct { ... LPNET_TIME pTime; } NET_RECORD;
    只看 "类型里有没有 *" 会把它误判成非指针的传值结构体，从而丢掉数组语义、
    生成 static_cast<T>(0x1234) 这类编译不过的代码，或把字段判成未知类型。
    存成字典是为了让 build_deps 能据此排出正确的注册拓扑序（指针别名指向的
    结构体必须先注册）。
    """
    names, ptr_aliases = [], {}
    for part in decl.split(','):
        part = part.strip()
        if not part:
            continue
        if part.startswith('*'):
            mm = re.match(r'\*\s*([A-Za-z_]\w*)', part)
            if mm and names:
                ptr_aliases[mm.group(1)] = names[0]
            continue
        mm = re.match(r'([A-Za-z_]\w*)', part)
        if mm:
            names.append(mm.group(1))
    return names, ptr_aliases


def _collect_type_names(text):
    """收集类型名来源：函数指针 typedef / 普通 typedef 别名 / #define 名。"""
    fp_types = set(FP_RE.findall(text))
    typedef_names = set(TYPEDEF_NAME_RE.findall(text)) - fp_types
    define_names = set(DEFINE_NAME_RE.findall(text))
    return fp_types, typedef_names, define_names


def _collect_enums(text):
    """收集枚举。返回 (enums, enum_names)。"""
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
    return enums, enum_names


def _collect_structs(text):
    """收集结构体。先收全部名字再回头提字段：白名单需要完整名字集合。

    返回 (raw_structs, struct_names, struct_aliases, ptr_aliases)，
    其中 ptr_aliases 是 {LPNET_X: NET_X} 映射（供 build_deps 排注册顺序）。"""
    raw_structs = []
    struct_names = set()
    struct_aliases = set()
    ptr_aliases = {}
    for body, decl in _find_typedef_structs(text):
        names, ptrs = _split_decl_names(decl)
        if not names:
            continue
        name = names[0]
        struct_aliases.update(names[1:])
        ptr_aliases.update(ptrs)
        if name in struct_names:
            continue
        struct_names.add(name)
        raw_structs.append((name, body))
    return raw_structs, struct_names, struct_aliases, ptr_aliases


def _collect_unions(text):
    """收集有名 union 类型名（typedef union {...} NAME;）。只进白名单，字段由 emit 按 bytes 暴露。"""
    union_names = set()
    union_ptr_aliases = {}
    for m in UNION_RE.finditer(text):
        _ubody, decl = m.group(1), m.group(2)
        names, ptrs = _split_decl_names(decl)
        union_names.update(names)
        union_ptr_aliases.update(ptrs)
    return union_names, union_ptr_aliases


def _scan_body(body, bindable, fp_types, stats):
    """扫描一段 body（结构体或匿名 union 体内），返回字段列表。

    处理嵌套：
      - 匿名 union {...}; → 成员递归提升为字段（C 语义里匿名 union 成员
        直接进入外层命名空间）
      - 有名 union/struct {...} name; → name 按 bytes 暴露（匿名类型无法注册
        nb::class_），ftype 记为 __union__/__struct__ 标记
      - 普通字段 → FIELD_RE
    """
    fields = []
    i, n = 0, len(body)
    while i < n:
        c = body[i]
        if c in ' \t\r\n':
            i += 1
            continue
        m = re.match(r'(union|struct)\s*\{', body[i:])
        if m:
            kind = m.group(1)
            open_pos = body.find('{', i)
            close_pos = _brace_match(body, open_pos)
            block_body = body[open_pos + 1:close_pos]
            after = body[close_pos + 1:]
            m2 = re.match(r'\s*([A-Za-z_]\w*)\s*;', after)
            block_name = m2.group(1) if m2 else None
            if block_name:
                fields.append(('__%s__' % kind, block_name, None))
                stats['nested_bytes'] += 1
            else:
                fields.extend(_scan_body(block_body, bindable, fp_types, stats))
            i = close_pos + 1 + (m2.end() if m2 else 0)
            continue
        semi = body.find(';', i)
        if semi == -1:
            break
        decl = body[i:semi]
        fm = FIELD_RE.match(decl)
        if fm:
            ftype = fm.group(1).strip()
            fname = fm.group(2)
            arr = fm.group(3) or None
            # 位字段：名字后跟 ':' 和宽度（BYTE byImageQlty:7），不能取地址，
            # nanobind 绑不了，跳过。
            if decl[fm.end():].lstrip().startswith(':'):
                stats['skip_bitfield'] += 1
            elif fname in RESERVED_WORDS:
                stats['skip_reserved'] += 1
            elif '(' in ftype or ftype in fp_types:
                stats['skip_funcptr'] += 1
            else:
                base = _normalize(ftype)
                if '*' not in ftype and base not in bindable:
                    # 既不是基本类型，也不是已知 typedef / 结构体 / 枚举。
                    # 极可能是漏网的函数指针或外部类型，硬绑必然编译失败（C2440）。
                    stats['skip_unknown'] += 1
                    stats['unknown_' + base] += 1
                else:
                    fields.append((ftype, fname, arr))
        i = semi + 1
    return fields


def _extract_fields(raw_structs, bindable, fp_types):
    """从结构体 body 提字段（递归处理嵌套 union/struct）。返回 (structs, stats)。"""
    structs = []         # (name, [(ftype, fname, arr_or_None), ...])
    stats = collections.Counter()
    for name, body in raw_structs:
        fields = _scan_body(body, bindable, fp_types, stats)
        if not fields:
            continue
        structs.append((name, fields))
    return structs, stats


def parse_header(path):
    raw = open(path, encoding='latin-1', errors='replace').read()
    text = strip_comments(raw)

    fp_types, typedef_names, define_names = _collect_type_names(text)
    enums, enum_names = _collect_enums(text)
    raw_structs, struct_names, struct_aliases, struct_ptr_aliases = _collect_structs(text)
    union_names, union_ptr_aliases = _collect_unions(text)
    ptr_aliases = dict(struct_ptr_aliases)
    ptr_aliases.update(union_ptr_aliases)

    # 指针别名（LPNET_XXX）必须进白名单：厂商头文件里字段也这么写
    # （`LPNET_RECORDFILE_INFO pRecord;`），不进白名单会被判"未知类型"跳过。
    # 见 docs/implementation-notes.md 4.1 —— 这个疏漏曾让 6 个字段在指针别名
    # 已修之后仍留在 unknown 里。
    bindable = (struct_names | struct_aliases | enum_names | union_names
                | typedef_names | define_names | BASE_TYPES | set(ptr_aliases))

    structs, stats = _extract_fields(raw_structs, bindable, fp_types)

    return (enums, enum_names, structs, struct_names, fp_types, stats,
            typedef_names, union_names, ptr_aliases | union_ptr_aliases)


# ------------------------------------------------------------------ 函数

def parse_param(part):
    """解析单个参数文本：'const char *pName' / 'LLONG lLoginID' / 'unsigned char'。

    返回 dict(type/name/has_default)，type 是完整类型（含 const/unsigned/指针），
    name 可能为 None（有些函数只有类型没有参数名）。

    必须先归一化**后置 const**：海康写 `char const *sServerIP`，大华写
    `const char *pBuffer`。两者语义相同，但下面的正则只认前置形式，直接解析
    后置写法会把 `const` 当成参数名、把 `*sServerIP` 整个丢掉，生成出
    `char const` 这种非法代码（实测 C2059 + C2660 连环报）。
    这是标准 C++ 语法而非厂商方言，所以归一化放在 common/ 而不是 config/。
    """
    has_default = '=' in part
    part = re.sub(r'\s*=\s*.+$', '', part).strip()
    if not part:
        return None
    # 'char const *p' -> 'const char *p'（只改前两个记号，不碰指针部分）
    part = re.sub(r'\b([A-Za-z_]\w*)\s+const\b(?=\s*[\*\w])', r'const \1', part)
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

def build_deps(structs, struct_names, ptr_aliases=None):
    """deps[A] = {B, ...} 表示 A 的字段里出现了类型 B（需要 B 先注册）。

    ptr_aliases 是 {LPNET_X: NET_X} 映射：`LPNET_X pField;` 这种字段会让 A 依赖
    NET_X，不排进拓扑序的话 nb::class_<NET_X> 可能还没注册就 def_rw 指针成员，
    运行时找不到类型。
    """
    ptr_aliases = ptr_aliases or {}
    deps = {}
    for name, fields in structs:
        d = set()
        for ftype, _fname, _arr in fields:
            base = ftype.replace('unsigned', ' ').replace('signed', ' ').strip()
            base = base.rstrip('*').strip()
            target = ptr_aliases.get(base, base)
            if target in struct_names and target != name:
                d.add(target)
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


# ------------------------------------------------------------------ 回调
#
# 本节只回答"这个回调 typedef 长什么样"——纯 C 语法，各厂商同构。
# **不回答"这个整型参数是数量还是错误码"**——那是厂商语义，由 config/<sdk>.py
# 以 qty_pred / count_pred 钩子提供。见 classify_cb_params 的参数说明。

# typedef ret (CALLBACK *fXxx)(params);
# 调用约定在头文件里是宏（CALLBACK / CALL_METHOD / CALL_METHOD_WITH_RESULT ...），
# 不能写死列表，漏一个就会让整个回调漏绑。
CB_RE = re.compile(
    r'typedef\s+([^(;]*?)\s*\(\s*(?:[A-Za-z_]\w*\s+)?\*\s*(\w+)\s*\)\s*\(([^)]*)\)\s*;')


def parse_callbacks(text):
    """提取全部回调签名。返回 [(name, ret, [param_dict, ...]), ...]"""
    out, seen = [], set()
    for m in CB_RE.finditer(text):
        ret, name, args_s = m.group(1).strip(), m.group(2), m.group(3).strip()
        if name in seen:
            continue
        seen.add(name)
        params = []
        bad = False
        if args_s and args_s not in ('void', 'VOID'):
            for part in args_s.split(','):
                p = parse_param(part)
                if p is None:
                    bad = True
                    break
                params.append(p)
        if not bad:
            out.append((name, ret, params))
    return out


def _find_qty_index(params, start, qty_pred=None):
    """从 start 起（最多看 2 个位置）找第一个『数量/长度』语义的整型参数下标。

    qty_pred 由厂商 config 提供（见 classify_cb_params）。**None = 保守退化**：
    认为没有任何整型参数是数量，于是 BYTE* 不取长度（只给地址）、结构体指针
    一律给单对象。宁可少给，绝不给错。
    """
    if qty_pred is None:
        return None
    for j in range(start, min(start + 2, len(params))):
        p = params[j]
        if '*' in p['type']:
            continue
        nm = p['name'] or ''
        if nm and qty_pred(nm):
            return j
    return None


def classify_cb_params(params, struct_names, enum_names, ptr_aliases=frozenset(),
                       qty_pred=None, count_pred=None):
    """把回调参数逐个分类，返回 [(kind, qty_index), ...]。

    kind 语义（决定 Python 侧看到什么）：
      value   标量/枚举，原样转发（枚举在生成模块里是 nb::enum_）
      cstr    const char* -> str（NULL 转空串，不解引用空指针）
      bytes   BYTE*/unsigned char* + 紧邻长度 -> bytes
      array   结构体指针 + 紧邻**元素个数** -> list of 借用视图
      obj     结构体指针 -> 单个借用视图
      uintptr 其他指针（void*/HANDLE/int*...） -> 整数地址

    ptr_aliases 是"名字里没有星号的指针别名"集合或 {别名: 目标} 映射。厂商
    头文件大量这么写回调签名，漏掉它会把指针当成传值结构体 —— 详见
    docs/implementation-notes.md 4.1（实测 value 824→820、array 5→7）。

    qty_pred(name) -> bool：**厂商钩子**。判断一个整型参数名是否表示
    「数量/长度」。决定 BYTE* 能不能取紧邻整数当缓冲区长度。

    count_pred(name) -> bool：**厂商钩子**。判断一个整型参数名是否表示
    「元素个数」（而非字节长度）。决定结构体指针给 list 还是给单对象。

    两个钩子都是**可选**的，缺省 None = 保守退化：BYTE* 只给地址、结构体
    指针只给单对象。这样未适配的厂商不会静默拿到错误的 list —— 少给可接受，
    给错无法排查。各厂商的经验规则写在 config/<sdk>.py，不在这里。
    """
    alias_keys = set(ptr_aliases)
    kinds = []
    for i, p in enumerate(params):
        core = re.sub(r'^const\s+', '', p['type']).strip()
        base = core.replace('*', '').strip()
        # 注意是 `in alias_keys` 而不是只看 '*'：LPNET_X 展开后没有星号
        ptr = '*' in core or base in alias_keys

        if not ptr:
            kinds.append(('value', None))
            continue
        if base in OPAQUE_PTR or base == 'void':
            kinds.append(('uintptr', None))
            continue
        if base == 'char':
            kinds.append(('cstr', None))
            continue
        j = _find_qty_index(params, i + 1, qty_pred)
        if base in ('BYTE', 'unsigned char'):
            kinds.append(('bytes', j) if j is not None else ('uintptr', None))
            continue
        if base in enum_names:
            # 枚举没有 nb::class_，view() 会失败；一律按地址暴露。
            kinds.append(('uintptr', None))
            continue
        if base in struct_names or base in alias_keys:
            nm = (params[j]['name'] or '') if j is not None else ''
            is_count = (j is not None and count_pred is not None
                        and count_pred(nm))
            kinds.append(('array', j) if is_count else ('obj', None))
            continue
        kinds.append(('uintptr', None))
    return kinds
