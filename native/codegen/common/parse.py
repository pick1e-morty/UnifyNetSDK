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

# typedef union [tag] { ... } Name;   体内**可以**嵌套花括号（海康
# NET_DVR_PLAYITEM_INFO 等的 union 体内嵌 struct/union 定义），所以收集时
# 必须用平衡花括号匹配，不能用 [^{}]* 的单层正则。
# union 成员共享一块内存，字段按 bytes 暴露（见 emit.gen_fields），
# 类型名只需进白名单，不必注册 nb::class_。
UNION_HEAD_RE = re.compile(r'typedef\s+union\s*(?:\w+\s*)?\{')

# 匹配单个字段声明（不含分号）。数组部分吃多个维度：[4][32] 这类二维也认。
#
# 类型与名字之间的分隔是 `[\s*]+`（空格/星号混合，**至少 1 个字符**），星号
# 归分隔组、由调用方拼回 ftype。两个坑都踩过：
#   - 用 `\s+`：`unsigned char *in_buf`（* 紧贴字段名，海康/大华都这么写）
#     匹配不上，回退成 type='unsigned'、name='char'，字段名错、类型成空。
#   - 用 `\s*`：贪婪回退会把名字劈开 —— `long bToScreen` 匹配成
#     type='long bToScree' + name='n'。分隔组要求至少 1 个字符即可杜绝：
#     合法 C 里类型和名字之间必有空格或 *。
FIELD_RE = re.compile(
    r'^\s*(?:(?:const|volatile|static)\s+)*'
    r'((?:unsigned\s+|signed\s+)*(?:long\s+)?(?:int|char|short|long|float|double)?'
    r'[A-Za-z_]\w*)'           # 1: 类型 core（不含 *）
    r'([\s*]+)'                # 2: 类型与名字之间的分隔（空格 / * 混合）
    r'([A-Za-z_]\w*)'          # 3: 字段名
    r'\s*((?:\[[^\]]*\])*)')   # 4: 数组维度

# typedef int (CALLBACK *fXxx)(...);
# 调用约定在头文件里常常是宏（CALLBACK / CALL_METHOD ...），写死列表必然漏。
# 漏了 CALL_METHOD 就会让 fNotifyXxx 这类字段被当成普通类型去 def_rw，触发 C2440。
# 宏与 * 之间的空格不能要求：大华写 `typedef void (CALLBACK* fXxx)(...)`
#（无空格），要求 \s+ 会漏掉整整一族 fNotifyXxx typedef。
FP_RE = re.compile(r'typedef\s+[^(;]*\(\s*(?:[A-Za-z_]\w*\s*)?\*\s*(\w+)\s*\)\s*\(')

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
    # Windows SDK 的整数别名，**来自 windows.h 而非厂商头文件**。
    #
    # 为什么必须列在这里：白名单里"哪些类型算已知"有一部分是靠扫厂商头文件的
    # typedef 得到的，而海康头文件把这些别名放在了 Linux 分支：
    #     #if   (defined(_WIN32))
    #         typedef unsigned __int64  UINT64;      // Windows 分支只补这两个
    #     #elif defined(__linux__) || defined(__APPLE__)
    #         typedef unsigned int      DWORD;      // 基础类型全在 Linux 分支
    #         typedef unsigned char     BYTE;
    #     #endif
    # 一旦裁掉非活动分支（parse.strip_inactive_branches），DWORD / BYTE 这类
    # typedef 就消失了，白名单随之断裂 —— 所有 DWORD 字段被判"未知类型"，
    # 结构体因提不出字段被整体跳过，海康字段数从 18635 掉到 3225（-82.7%）。
    #
    # 裁剪本身没错（Windows 下这些类型确实由 windows.h 提供，生成的 C++
    # 也确实 #include 了它），错的是白名单依赖了"头文件里写了什么 typedef"。
    # 把平台自带的别名显式列出来，白名单就不再受裁剪影响。
    'BOOL', 'BYTE', 'WORD', 'DWORD', 'LONG', 'ULONG', 'SHORT', 'USHORT',
    'INT', 'UINT', 'INT8', 'UINT8', 'INT16', 'UINT16', 'INT32', 'UINT32',
    'INT64', 'UINT64', 'DWORD64', 'LONGLONG', 'ULONGLONG', 'CHAR', 'UCHAR',
}

# Windows 句柄 / 不透明指针：本质是 void* 的 typedef，参数里看不到 *，
# 但必须当指针暴露成 uintptr_t，否则 nanobind 找不到 caster。
OPAQUE_PTR = {
    'HWND', 'HDC', 'HANDLE', 'HMODULE', 'HINSTANCE', 'LPVOID',
    'LPARAM', 'WPARAM', 'HGLRC', 'HICON', 'HCURSOR', 'HBRUSH', 'HFONT', 'HPEN',
}


def strip_comments(text):
    """去掉块注释和行注释，避免注释里的分号/花括号干扰正则。

    必须**单趟交替匹配**，不能"先块后行"两趟：C 语义里行注释到行末为止，
    行注释里的 `/*` 不是块注释开头。两趟式先删块注释会把 `//.../*...` 行里的
    `/*` 误当块注释起点，一路吞到文件里下一个 `*/`，中间的**真代码整段消失**。
    海康 HCNetSDK.h 的 `///////////*网络参数配置_V50/////////////` 就是这种写法，
    曾把 NET_DVR_ALARMHOST_NETPARAM_V50 的 typedef 头吞掉，结构体收集不到，
    引用它的字段全部被判未知类型。
    """
    text = re.sub(r'/\*.*?\*/|//[^\n]*', ' ', text, flags=re.S)
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
    """收集有名 union 类型名（typedef union {...} NAME;）。只进白名单，字段由 emit 按 bytes 暴露。

    body 用平衡花括号找（同 _find_typedef_structs）：海康的 union 体内嵌
    struct/union 定义，单层 [^{}]* 正则抓不到，整个类型会从白名单里消失，
    引用它的字段全部被判未知类型。
    """
    union_names = set()
    union_ptr_aliases = {}
    for m in UNION_HEAD_RE.finditer(text):
        open_pos = m.end() - 1          # '{' 的位置
        close_pos = _brace_match(text, open_pos)
        after = text[close_pos + 1:]
        semi = after.find(';')
        decl = after[:semi] if semi != -1 else ''
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
            m2 = re.match(r'\s*([A-Za-z_]\w*)\s*((?:\[[^\]]*\])*)\s*;', after)
            block_name = m2.group(1) if m2 else None
            block_arr = (m2.group(2) or '') if m2 else ''
            if block_name:
                # 有名（含数组维度，如 `}struReceiver[3];`）——整体按 bytes 暴露。
                # 数组维度必须一起吃掉：早先正则只认 `}name;`，于是
                # `}struReceiver[3];` 匹配不上、被误判成匿名 struct，内部字段
                # `sName` / `sAddress` 被提升到外层 class_，编译报
                # C2039 "sName 不是 NET_DVR_EMAILCFG_V30 的成员"。
                fields.append(('__%s__' % kind, block_name,
                               block_arr or None))
                stats['nested_bytes'] += 1
            else:
                # 真正的匿名 union：C 语义下成员直接进入外层命名空间，故提升。
                fields.extend(_scan_body(block_body, bindable, fp_types, stats))
            i = close_pos + 1 + (m2.end() if m2 else 0)
            continue
        semi = body.find(';', i)
        if semi == -1:
            break
        decl = body[i:semi]
        fm = FIELD_RE.match(decl)
        if fm:
            # 星号在分隔组（group 2）里，拼回类型；见 FIELD_RE 处的注释
            ftype = (fm.group(1) + fm.group(2)).strip()
            fname = fm.group(3)
            arr = fm.group(4) or None
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


# ------------------------------------------------------------------ 条件编译
#
# 厂商头文件里大量类型被平台条件包着，只在别的平台存在：
#     #if defined(__linux__)
#     typedef struct __DC { void *surface; HWND hWnd; }DC;
#     #endif
# 生成器若不裁剪就会绑定 DC，MSVC 报 C2653 "'DC' 不是类或命名空间名称"，
# 一轮 121 处编译错误里大半是这个。
#
# 不调用真预处理器（cl /EP）而自己做条件求值，理由：先把两个 SDK 头文件全量
# 统计过一遍 —— 24（大华）/ 47（海康）个条件**全部**只由 defined / 宏名 /
# && || ! ! 组成，没有一处需要真正的宏展开或函数调用（实测 0 个）。既然如此，
# 引入 cl /EP 只会带来一个新的失败模式（中文路径 + 输出格式），而求值器
# 30 行就能覆盖全部实际用例。
#
# 语义上**裁掉非活动分支**而非"排除类型名"：后者治不了下一个 Linux-only 类型。

# 平台预定义宏。我们只支持 Windows x64 + MSVC + C++，两个厂商 SDK 都是
# Windows 版，所以这份集合对两者通用，不属于任何厂商的知识。
#
# **只放编译器命令行上就有的宏**，一个都不能多。踩过的坑：`_WINDOWS_` 曾被列在
# 这里，而它其实是 windows.h 的 include guard —— 只有 windows.h 被包含之后才
# 存在。海康头文件开头正是
#     #ifndef _WINDOWS_
#     #if (defined(_WIN32) || defined(_WIN64))
#     #include <windows.h>
#     #endif
#     #endif
# 把它当成已定义会让整个 Windows 块判为假，#include 被裁、其后大量内容跟着
# 被裁：海康字段从 18647 掉到 3237（-83%），而**编译错误数反而会下降**，
# 看起来像修好了。所以这份名单只能加"编译器命令行必有"的宏。
PLATFORM_DEFINES = frozenset({
    '_WIN32', '_WIN64', '_M_X64', '_M_IX86', '_MSC_VER', '_MSC_FULL_VER',
    '__cplusplus', '_WIN64_', '__WIN32__', '__WIN64__', '__x86_64__',
})


def collect_defined(text):
    """收集头文件里 #define 过的宏名，作为条件求值的"已定义"集合。

    必须连函数宏一起收：`#define IS_X(x) ...` 也会让 `#if defined(IS_X)` 为真。
    同时并入 PLATFORM_DEFINES（平台事实，非厂商知识）。
    """
    names = set(re.findall(r'^\s*#\s*define\s+([A-Za-z_]\w*)', text, re.M))
    names |= PLATFORM_DEFINES
    return names


# 交给 eval 之前的最后一道闸：此时表达式已把 defined/宏名全换成数字，
# 只允许数字、C 运算符和空白 —— 没有字母（不会解析成名字或函数调用），
# 没有 . [ ] ' " （没有属性访问/下标/字符串）。
_SAFE_EXPR = re.compile(r'^[0-9\s()!<>=&|+\-*/%^~?:]*$')


def eval_cond(expr, defined):
    """求值一条 #if 条件。返回 True / False / None（求不了）。

    只看宏**是否被定义**，不展开宏的值 —— 实测两个头文件的条件里没有一处
    需要值（都是 defined(X) 形式），展开值反而会引入 "OS_WINDOWS64 是 1 还是
    空" 这类分支差异。

    求不了时返回 None，调用方按"保守保留"处理：宁可多留一个 Linux-only 类型
    让它编译报错，也不能漏掉一个 Windows 真正有的类型 —— 后者是静默功能缺失。
    """
    if expr is None:
        return None
    e = expr.strip()
    if not e:
        return None
    # defined(X) / defined X -> 1 / 0
    e = re.sub(r'defined\s*\(\s*([A-Za-z_]\w*)\s*\)',
               lambda m: '1' if m.group(1) in defined else '0', e)
    e = re.sub(r'defined\s+([A-Za-z_]\w*)',
               lambda m: '1' if m.group(1) in defined else '0', e)
    # 剩下的裸标识符：查 defined（C 里未定义标识符就是 0）。
    # 平台宏（__cplusplus / _WIN64 等）也在这里生效：#if __cplusplus 是常见写法。
    e = re.sub(r'\b[A-Za-z_]\w*\b',
               lambda m: '1' if m.group(0) in defined else '0', e)
    # 十六进制字面量按"非零"处理
    e = re.sub(r'\b0[xX][0-9a-fA-F]+\b', '1', e)
    # 安全检查必须在**运算符转换之前**：此时表达式里只有数字和 C 运算符，
    # 没有字母、没有调用/下标/属性访问。转换是固定替换，本身不会引入风险。
    if not _SAFE_EXPR.match(e):
        return None
    # C 的逻辑运算符换成 Python 的，否则 eval 报 SyntaxError：
    # "1 || 1" 在 Python 里不是合法表达式（Python 用 or / and / not）。
    # 顺序要紧：先换双字符的 || 和 &&，再换单个 !，且 ! 不能吃掉 !=。
    e = e.replace('||', ' or ').replace('&&', ' and ')
    e = re.sub(r'!(?!=)', ' not ', e)
    try:
        return bool(eval(e, {'__builtins__': {}}, {}))
    except Exception:
        return None


def strip_inactive_branches(text, defined=None):
    """按条件编译裁掉非活动分支的内容，保留 #if/#endif 结构行本身。

    逐行状态机，每个栈帧记 [是否有分支已被取用, 当前是否活跃, 是否已进 else]。
    求不了条件的块（eval_cond 返回 None）按**活跃**处理，且视为"已取用"，
    于是其后的 #elif/#else 会被裁掉 —— 与 C 预处理器的行为一致。

    **#define 必须边走边加，不能预先全量收集。** 头文件的标准写法是
        #ifndef _HC_NET_SDK_H_
        #define _HC_NET_SDK_H_
        ... 全文 ...
        #endif
    预收集会把末尾那句 #define 也算进"已定义"，于是 #ifndef 判为假、**整个文件
    被裁掉**（实测海康 51581 行裁到 129 行，NET_DVR_TIME 这类 Windows 核心类型
    一并消失）。预扫描只用于给调用方一个粗略的宏集合参考。
    """
    defined = set(PLATFORM_DEFINES if defined is None else defined)
    out = []
    stack = []          # [any_taken, active, seen_else]
    for line in text.splitlines(keepends=True):
        s = line.strip()
        # #define 先入集合，再看当前是否活跃（顺序即语义）
        md = re.match(r'#\s*define\s+([A-Za-z_]\w*)', s)
        if md:
            defined.add(md.group(1))
            if all(f[1] for f in stack):
                out.append(line)
            continue
        m = re.match(r'#\s*(ifdef|ifndef|if|elif|else|endif)\b\s*(.*?)\s*$', s)
        if not m:
            # 普通行：所有外层都活跃才保留
            if all(f[1] for f in stack):
                out.append(line)
            continue
        kw, rest = m.group(1), m.group(2)
        if kw in ('if', 'ifdef', 'ifndef'):
            if kw == 'if':
                v = eval_cond(rest, defined)
            elif kw == 'ifdef':
                v = (rest in defined) if rest else None
            else:
                v = (rest not in defined) if rest else None
            if v is None:
                v = True               # 保守保留
            stack.append([bool(v), bool(v), False])
            out.append(line)
        elif kw == 'elif':
            if not stack:
                out.append(line)
                continue
            fr = stack[-1]
            if fr[2] or fr[0]:         # 已进 else，或已有分支被取用
                fr[1] = False
            else:
                v = eval_cond(rest, defined)
                if v is None:
                    v = True
                fr[1] = bool(v)
                fr[0] = fr[0] or bool(v)
            out.append(line)
        elif kw == 'else':
            if not stack:
                out.append(line)
                continue
            fr = stack[-1]
            if fr[2]:
                fr[1] = False
            else:
                fr[1] = not fr[0]
                fr[0] = True
                fr[2] = True
            out.append(line)
        else:  # endif
            if stack:
                stack.pop()
            out.append(line)
    return ''.join(out)


def load_header(path, filters=None):
    """读头文件并返回可解析文本：去注释 + 依次应用 filters。

    这是唯一的读入口。调用方不要再自己 open() + strip_comments() ——
    emit.py 曾经另外读了一遍喂给 parse_funcs/parse_callbacks，一旦只改
    parse_header 就会漏掉，两边看到的头文件不一致。

    **filters 是厂商钩子**，默认 None（什么都不做）。存在的理由：一个解析步骤
    对某个厂商必要、对另一个厂商却有害时，必须能按厂商开关，而不是无差别
    应用于所有人。真实教训见 _verify_no_overcut 的 docstring —— 条件编译裁剪
    就是这么把大华的字段砍掉 32% 的。

    调用方应把 cfg['text_filters'] 传进来，不要硬编码。
    """
    text = strip_comments(open(path, encoding='latin-1', errors='replace').read())
    for fn in (filters or []):
        text = fn(text)
    return text


# 裁剪后可提取字段数的最大跌幅（%）。实测：正常裁剪掉 0.2%（海康 18635 ->
# 18599，消掉的是 Linux-only 的 DC / INITINFO）；误裁时掉 82.7%。10% 足够
# 区分两者。
FIELD_DROP_LIMIT = 10.0


def _extract_scale(text):
    """跑一遍完整提取，返回 (结构体数, 字段总数)。给自检用。"""
    rs, rsn, rsa, rspa = _collect_structs(text)
    un, unp = _collect_unions(text)
    fp, td, dn = _collect_type_names(text)
    bindable = (rsn | rsa | un | td | dn | BASE_TYPES | OPAQUE_PTR
                | set(rspa) | set(unp))
    st, _ = _extract_fields(rs, bindable, fp)
    return len(st), sum(len(f) for _, f in st)


def _verify_no_overcut(path, filters, before_text, after_text):
    """裁剪前后比对：**可提取字段数跌幅超阈值就中止**。

    为什么必须有这道闸：条件编译裁剪过头时，**编译错误数是会下降的**（类型被
    裁掉了，编译器自然没话可说），看起来像"修好了"。实测海康裁剪过度时字段从
    18635 掉到 3225（-82.7%），而 NET_DVR_ACCELERATIONCFG / NET_DVR_ACS_CFG
    这类核心类型一起消失 —— 只看错误数完全发现不了。

    判据用**字段数**而不是"消失的类型名"。早先试过按名字判（名字不含
    linux/posix 就算误裁），误报严重：海康的 DC / INITINFO 确实该被裁（它们
    就住在 `#if defined(__linux__)` 里），大华的 RECT 也确实该消失（windows.h
    的 windef.h 会提供），只是名字里没有平台字样。

    数量判据足够灵敏：误裁 82.7% vs 正常裁剪 0.2%，差 400 倍，10% 的阈值
    绰绰有余。类型名只作为**报错信息**附在后面，帮助定位，不作判据。
    """
    if not filters:
        return
    before = _collect_structs(before_text)[1]
    after = _collect_structs(after_text)[1]
    lost = sorted(before - after)

    n_struct_b, n_field_b = _extract_scale(before_text)
    n_struct_a, n_field_a = _extract_scale(after_text)
    drop = 0.0 if n_field_b == 0 else 100.0 * (n_field_b - n_field_a) / n_field_b

    if drop <= FIELD_DROP_LIMIT:
        print('  条件编译裁剪: 去掉 %d 个平台专属类型，字段 %d -> %d (-%.1f%%)'
              % (len(lost), n_field_b, n_field_a, drop))
        return
    raise ValueError(
        'text_filters 裁剪过度，已中止（生成残缺的绑定比构建失败更糟）:\n'
        '  字段总数 %d -> %d (-%.1f%%，阈值 %.0f%%)\n'
        '  消失的类型 %d 个，前 15 个: %s'
        % (n_field_b, n_field_a, drop, FIELD_DROP_LIMIT,
           len(lost), ', '.join(lost[:15])))


def parse_header(path, filters=None, verify=True):
    raw = open(path, encoding='latin-1', errors='replace').read()
    before_text = strip_comments(raw)
    text = before_text
    for fn in (filters or []):
        text = fn(text)
    if verify:
        _verify_no_overcut(path, filters, before_text, text)

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
    #
    # OPAQUE_PTR（HWND/HANDLE 等）同理：它们是 void* 的 typedef，来自
    # windows.h 而非厂商头文件。海康头文件里 HWND 的 typedef 住在被
    # text_filters 裁掉的 Linux 分支里，不进白名单的话 gen_bind 管线会把
    # 7 个 HWND 字段判未知（check_coverage 不裁剪所以看不见这个差）。
    # emit.gen_fields 对这些类型按指针字段同款处理（uintptr 地址读写）。
    bindable = (struct_names | struct_aliases | enum_names | union_names
                | typedef_names | define_names | BASE_TYPES | OPAQUE_PTR
                | set(ptr_aliases))

    structs, stats = _extract_fields(raw_structs, bindable, fp_types)

    return (enums, enum_names, structs, struct_names, fp_types, stats,
            typedef_names, union_names, ptr_aliases | union_ptr_aliases)


# ------------------------------------------------------------------ 函数

def parse_param(part):
    """解析单个参数文本，返回 dict(type/name/has_default)。

    必须先归一化**后置 const**：海康写 `char const *sServerIP` 与
    `void* const pBuf`，大华写 `const char *pBuffer`。语义相同，但下面第一个
    正则只认前置形式，直接解析后置写法会把 `const` 当成参数名、把指针整个
    丢掉，生成 `char const` 这种非法代码（实测 C2059 + C2660 连环报）。
    这是标准 C++ 语法而非厂商方言，所以归一化放在 common/ 而不是 config/。
    """
    has_default = '=' in part
    part = re.sub(r'\s*=\s*.+$', '', part).strip()
    if not part:
        return None
    # 后置 const -> 前置。两种形态都要覆盖：
    #   'char const *p'   标识符 + 空格 + const
    #   'void* const p'   指针 + 空格 + const
    part = re.sub(r'\b([A-Za-z_]\w*\s*\*?)\s+const\b(?=\s*[\*\w])',
                  r'const \1', part)
    m = re.match(
        r'((?:const\s+)?(?:unsigned\s+|signed\s+|long\s+|short\s+)?'
        r'[A-Za-z_]\w*\s*\**)\s*([A-Za-z_]\w*)?', part)
    if not m or not m.group(1):
        return None
    ftype, fname = m.group(1).strip(), m.group(2)
    # 引用参数：`const int& nCount` / `int &n` / `NET_X &info`。
    #
    # 不处理会生成 `const arg3` 这种非法代码（C4430 缺少类型说明符）—— 正则只认
    # 指针（\s*\**），遇到 & 就把类型截断成 `const`、变量名丢失。
    # 实证：fSubLogDataCallBack(..., const int& nCount, ...) 整个大华编译失败。
    #
    # 语义上引用参数在 Python 侧无法直接表达（nanobind 只能传值），按指针处理是
    # 对的：Python 给地址，C++ 写入后 Python 读回 —— 与既有 outptr 一致。
    # `T&&`（右值引用，SDK 参数里不会出现）不转换，避免和 `&&` 运算符混淆。
    if '&' in part and not re.search(r'&&\s*\w*$', part):
        part = part.replace('&', '*', 1)
        m = re.match(
            r'((?:const\s+)?(?:unsigned\s+|signed\s+|long\s+|short\s+)?'
            r'[A-Za-z_]\w*\s*\**)\s*([A-Za-z_]\w*)?', part)
        if not m or not m.group(1):
            return None
        ftype, fname = m.group(1).strip(), m.group(2)
    else:
        # `long x` / `unsigned short y`：修饰符本身是完整类型（long == long int），
        # 后面那个标识符才是变量名。剥修饰符后若只剩一个标识符就是这种情况。
        mods, rest = ftype, None
        while True:
            m2 = re.match(r'(const|unsigned|signed|long|short)\s+(.*)$', mods)
            if not m2:
                break
            rest = m2.group(2)
            mods = m2.group(1)
        if rest and re.fullmatch(r'[A-Za-z_]\w*', rest) and not fname:
            ftype, fname = mods, rest
    # 摘掉数组后缀（可能多维，如 strIP[16][16]、iBuf[256]）。只处理紧跟在
    # 变量名后面的；指针上的维度（`int (*p)[16]`）是另一种形态，不在这里处理。
    #
    # 用朴素的字符串切分而不是正则。曾用
    #     re.match(r'%s((?:\[[^\]]*\])+)\s*$' % re.escape(fname), part)
    # 反复匹配不上，改用 find 定位更直白，也省掉正则转义的麻烦。
    arr = None
    if fname:
        body = part.rstrip()
        pos = body.find(fname)
        # 从 fname 之后一路扫到末尾，必须全是 [..] 组，否则不是数组参数
        if pos >= 0:
            tail = body[pos + len(fname):].strip()
            if tail.startswith('[') and tail.count('[') == tail.count(']'):
                arr = tail
    return {'type': ftype, 'name': fname or None, 'arr': arr,
            'has_default': has_default}


def classify_param(p, struct_names, enum_names, fp_types):
    """参数分类。返回 'skip'/'callback' 表示该函数不能直接绑。"""
    t = p['type']
    core = re.sub(r'^const\s+', '', t)
    ptr = '*' in core
    base = core.replace('*', '').strip()
    # 数组参数（char strIP[16][16]）在函数签名里等价于指针，按指针处理。
    # 不做这一步的话，生成侧会把维度丢掉、只传 char 进去，报 C2664
    # "无法将参数从 char 转换为 char [][16]"（实测 NET_DVR_GetLocalIP）。
    if p.get('arr'):
        return 'uintptr'
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
            # 不透明指针 / 回调 / 输出指针 / 数组参数：一律暴露成地址，可传 0
            cpp_args.append('std::uintptr_t %s' % n)
            if p.get('arr'):
                # 数组参数退化成"指向数组的指针"，**只有第一维变成指针**：
                #   char strIP[16][16]  作为形参的真实类型是 char (*)[16]
                # 我曾把所有维度都塞进 pointed-to，生成 char (*)[16][16]，报
                # C2664 "无法将参数从 char (*)[16][16] 转换为 char [][16]"
                # （MSVC 诊断里会把 char(*)[16] 显示成 char [][16]）。
                base = t.replace('*', '').strip()
                dims = re.findall(r'\[([^\]]*)\]', p['arr'])
                rest = ''.join('[%s]' % d for d in dims[1:])
                call_args.append('reinterpret_cast<%s (*)%s>(%s)'
                                 % (base, rest, n))
            else:
                # 去掉顶层 const：`void* const p` 的参数类型是"const 指针"，
                # 而非"指向 const 的指针"，reinterpret_cast<const void*> 回去
                # 时类型不匹配（const 限定的是指针本身，赋值要求显式转换）。
                t_cast = re.sub(r'^const\s+', '', t) if t.startswith('const ') else t
                t_cast = t_cast.replace('* const', '*')
                call_args.append('reinterpret_cast<%s>(%s)' % (t_cast, n))
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
    # 无条件释放 GIL，与 ctypes.CDLL 语义等比：每次外部调用都不持 GIL。
    # 参数转换与返回值构造仍在外层 lambda 里持 GIL（call_guard 包在裸调用外层），
    # 线程安全/并发假设一律由 Python 上层负责，native 不掺和。
    extra = list(nb_args)
    extra.append('nb::call_guard<nb::gil_scoped_release>()')
    tail = ', ' + ', '.join(extra)
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
