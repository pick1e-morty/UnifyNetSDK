#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""从大华 dhnetsdk.h 生成 nanobind 绑定代码（枚举 + 结构体字段）。

产物（默认写到 native/src/gen/，不入库，可随时重建）:

    dh_bind.h            分片函数声明
    dh_bind_enums.cpp    所有枚举（最先注册）
    dh_bind_main.cpp     NB_MODULE + 按顺序调用各分片
    dh_bind_partNNN.cpp  结构体分片

为什么这样切分片
----------------
nanobind 有两条硬约束:

  1. 绑定某字段前，该字段类型必须已经注册为 nb::class_
     -> 同一个分片内：先注册本片所有类型，再统一绑字段（两阶段）

  2. 跨分片时，被引用的类型必须来自「更早执行」的分片
     -> 所以按【依赖拓扑序】切分，而不是按头文件里的出现顺序

结构体的值成员不可能成环（C 语言限制），所以拓扑排序总能成功。
指针字段不会产生依赖（我们只把指针暴露成整数，不解引用）。

用法
----
    python tools/gen_dh_bind.py                  # 默认 500 字段/片
    python tools/gen_dh_bind.py --fields-per-tu 800
    python tools/gen_dh_bind.py --dry-run        # 只统计，不写文件
    python tools/gen_dh_bind.py --limit 3000     # 只生成前 N 个字段（试编译用）
"""
import argparse
import collections
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PROJECT = os.path.dirname(HERE)
HEADER = os.path.join(PROJECT, 'dahua', 'C_Win64', 'Include', 'Common', 'dhnetsdk.h')
OUT_DIR = os.path.join(PROJECT, 'native', 'src', 'gen')

# ------------------------------------------------------------------ 解析

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


def strip_comments(text):
    """去掉块注释和行注释，避免注释里的分号/花括号干扰正则。"""
    text = re.sub(r'/\*.*?\*/', ' ', text, flags=re.S)
    text = re.sub(r'//[^\n]*', ' ', text)
    return text


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


# ------------------------------------------------------------ 依赖与拓扑

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


# ------------------------------------------------------------ 字段代码生成

def gen_fields(struct_name, fields, with_dwsize, indent='        '):
    """返回结构体的字段绑定行（不含开头的 nb::class_ 注册）。"""
    lines = []
    if with_dwsize:
        lines.append(indent + '.def("__init__", [](%s *self) {' % struct_name)
        lines.append(indent + '    std::memset(self, 0, sizeof(*self));')
        lines.append(indent + '    self->dwSize = sizeof(*self);')
        lines.append(indent + '})')
    else:
        lines.append(indent + '.def(nb::init<>())')

    for ftype, fname, arr in fields:
        base = ftype.strip()
        if arr:
            n = arr.strip()
            if base.replace(' ', '') == 'char':
                # char[N] <-> str，截断到 N-1 + NUL 防溢出
                lines += [
                    indent + '.def_prop_rw("%s",' % fname,
                    indent + '    [](const %s &s) {' % struct_name,
                    indent + '        std::size_t n = 0; while (n < sizeof(s.%s) && s.%s[n]) ++n;' % (fname, fname),
                    indent + '        return std::string(s.%s, n);' % fname,
                    indent + '    },',
                    indent + '    [](%s &s, const std::string &v) {' % struct_name,
                    indent + '        std::size_t n = v.size() < sizeof(s.%s) - 1 ? v.size() : sizeof(s.%s) - 1;' % (fname, fname),
                    indent + '        std::memcpy(s.%s, v.data(), n); std::memset(s.%s + n, 0, sizeof(s.%s) - n);' % (fname, fname, fname),
                    indent + '    })',
                ]
            else:
                # 其余数组（BYTE[N]/int[N]/结构体[N]）统一以 bytes 暴露原始内存
                lines += [
                    indent + '.def_prop_rw("%s",' % fname,
                    indent + '    [](const %s &s) {' % struct_name,
                    indent + '        return nb::bytes(reinterpret_cast<const char *>(s.%s), sizeof(s.%s));' % (fname, fname),
                    indent + '    },',
                    indent + '    [](%s &s, const nb::bytes &v) {' % struct_name,
                    indent + '        std::size_t n = v.size() < sizeof(s.%s) ? v.size() : sizeof(s.%s);' % (fname, fname),
                    indent + '        std::memcpy(s.%s, v.data(), n);' % fname,
                    indent + '    })',
                ]
        elif '*' in base:
            # 裸指针：只暴露地址，不解引用。
            # setter 必须转到字段自身的类型（int*/char*/NET_TIME* ...），
            # 直接转 void* 会被 MSVC 拒绝：C2440 void* -> T*
            lines += [
                indent + '.def_prop_rw("%s",' % fname,
                indent + '    [](const %s &s) { return reinterpret_cast<std::uintptr_t>(s.%s); },' % (struct_name, fname),
                indent + '    [](%s &s, std::uintptr_t v) { s.%s = reinterpret_cast<decltype(s.%s)>(v); })' % (struct_name, fname, fname),
            ]
        else:
            # 标量 / typedef 别名 / 枚举 / 结构体，交给 nanobind 的 caster
            lines.append(indent + '.def_rw("%s", &%s::%s)' % (fname, struct_name, fname))
    # 每行自带换行符。外层用 ''.join 拼接，缺 \n 会把一个结构体的所有字段
    # 挤成一行（单行可达数万字符），MSVC 处理超长行会明显变慢。
    return [l + '\n' for l in lines]


# ------------------------------------------------------------------ 主流程

def write_if_changed(path, text):
    """内容不变就不写文件，避免 mtime 变化导致 ninja 无谓重编整个分片。"""
    if os.path.isfile(path):
        try:
            with open(path, 'r', encoding='ascii', errors='replace') as f:
                if f.read() == text:
                    return False
        except OSError:
            pass
    with open(path, 'w', encoding='ascii') as f:
        f.write(text)
    return True


def main():
    ap = argparse.ArgumentParser(description='从 dhnetsdk.h 生成 nanobind 绑定代码')
    ap.add_argument('--fields-per-tu', type=int, default=500,
                    help='每个结构体分片的字段数上限（默认 500）')
    ap.add_argument('--enums-per-tu', type=int, default=250,
                    help='每个枚举分片的枚举数上限（默认 250）')
    ap.add_argument('--limit', type=int, default=0,
                    help='只生成前 N 个字段（试编译用，0=全量）')
    ap.add_argument('--out-dir', default=OUT_DIR)
    ap.add_argument('--dry-run', action='store_true', help='只统计，不写文件')
    args = ap.parse_args()

    if not os.path.isfile(HEADER):
        print('找不到头文件:', HEADER)
        return 1

    print('解析:', HEADER)
    enums, enum_names, structs, struct_names, fp_types, stats, typedef_names = parse_header(HEADER)
    total_fields = sum(len(f) for _, f in structs)
    n_arr = sum(1 for _, f in structs for _, _, a in f if a)
    print('  枚举      : %d 个' % len(enums))
    print('  结构体    : %d 个' % len(structs))
    print('  字段      : %d 个（其中数组 %d）' % (total_fields, n_arr))
    print('  跳过      : 函数指针字段 %d / 未知类型字段 %d / 保留字 %d'
          % (stats['skip_funcptr'], stats['skip_unknown'], stats['skip_reserved']))
    unknown = sorted(((k[8:], v) for k, v in stats.items() if k.startswith('unknown_')),
                     key=lambda kv: -kv[1])
    if unknown:
        print('  未知类型 TOP: %s' % ', '.join('%s x%d' % kv for kv in unknown[:8]))
    print('  函数指针类型 %d 个（不参与结构体字段）' % len(fp_types))

    deps = build_deps(structs, struct_names)
    n_dep = sum(1 for v in deps.values() if v)
    print('  有类型依赖的结构体: %d 个' % n_dep)

    order = topo_order(structs, deps)
    by_name = dict(structs)

    # ---- 按拓扑序切分片 ----
    shards, cur, cur_n = [], [], 0
    used_total = 0
    for name in order:
        fields = by_name[name]
        if args.limit and used_total >= args.limit:
            break
        cur.append(name)
        cur_n += len(fields)
        used_total += len(fields)
        if cur_n >= args.fields_per_tu:
            shards.append((cur, cur_n))
            cur, cur_n = [], 0
    if cur:
        shards.append((cur, cur_n))

    print('  分片      : %d 片，已覆盖 %d 个字段' % (len(shards), used_total))
    if shards:
        sizes = [n for _, n in shards]
        print('  每片字段  : min %d / max %d / avg %.0f'
              % (min(sizes), max(sizes), sum(sizes) / len(sizes)))

    if args.dry_run:
        print('\n--dry-run，未写文件。')
        return 0

    out_dir = args.out_dir
    os.makedirs(out_dir, exist_ok=True)
    # 本次生成会产出的文件集合：内容不变就不重写（保持 mtime 不变，让
    # ninja 跳过未变化的分片）；生成结束后清掉不在集合里的过期旧文件。
    keep = set()

    BANNER = '// AUTO-GENERATED by tools/gen_dh_bind.py -- DO NOT EDIT\n'
    INCLUDES = (
        '#define NOMINMAX\n'
        '#include <nanobind/nanobind.h>\n'
        '#include <nanobind/stl/string.h>\n'
        '#include <cstddef>\n'
        '#include <cstdint>\n'
        '#include <cstring>\n'
        '#include <string>\n'
        '#include <dhnetsdk.h>\n'
        '#include "dh_bind.h"\n\n'
        'namespace nb = nanobind;\n\n'
    )

    # ---- 枚举分片 ----
    # 1873 个枚举挤在一个 TU 里是约 150 秒的死疙瘩，且 /Od 救不了它
    # （瓶颈是 nb::enum_ 的模板实例化次数本身，不是优化器）。拆片才能并行。
    enum_shards = [enums[i:i + args.enums_per_tu]
                   for i in range(0, len(enums), args.enums_per_tu)] or [[]]

    # ---- dh_bind.h ----
    lines = [BANNER, '#pragma once\n', '#include <nanobind/nanobind.h>\n\n']
    for i in range(len(enum_shards)):
        lines.append('void init_enums%03d(nanobind::module_ &m);\n' % i)
    for i in range(len(shards)):
        lines.append('void init_part%03d(nanobind::module_ &m);\n' % i)
    keep.add('dh_bind.h')
    write_if_changed(os.path.join(out_dir, 'dh_bind.h'), ''.join(lines))

    # ---- 枚举 ----
    for i, chunk in enumerate(enum_shards):
        lines = [BANNER, INCLUDES, 'void init_enums%03d(nb::module_ &m) {\n' % i]
        for ename, items in chunk:
            lines.append('    nb::enum_<%s>(m, "%s", nb::is_arithmetic())\n' % (ename, ename))
            for iname, ival in items:
                # 值可能是整数字面量（= 0）或位或表达式，类型是 int 而非枚举自身，
                # 而 nanobind 的 value() 形参是 T，必须显式转换（C2664）
                expr = ival if ival else iname
                lines.append('        .value("%s", static_cast<%s>(%s))\n' % (iname, ename, expr))
            lines.append('        ;\n')
        lines.append('}\n')
        fname = 'dh_bind_enums%03d.cpp' % i
        keep.add(fname)
        write_if_changed(os.path.join(out_dir, fname), ''.join(lines))

    # ---- 分片 ----
    n_scalar = n_array = n_ptr = 0
    for i, (names, _n) in enumerate(shards):
        lines = [BANNER, INCLUDES, 'void init_part%03d(nb::module_ &m) {\n' % i]
        # 阶段一：注册本片全部类型
        lines.append('    // ---- stage 1: register types ----\n')
        for name in names:
            lines.append('    nb::class_<%s> c_%s(m, "%s");\n' % (name, name, name))
        # 阶段二：绑字段
        lines.append('\n    // ---- stage 2: bind fields ----\n')
        for name in names:
            fields = by_name[name]
            has_dwsize = any(f[1] == 'dwSize' for f in fields)
            lines.append('    c_%s\n' % name)
            lines += gen_fields(name, fields, has_dwsize)
            lines.append('        ;\n')
            for _t, _fn, a in fields:
                if a:
                    n_array += 1
                else:
                    n_scalar += 1
            n_ptr += sum(1 for t, _, _ in fields if '*' in t)
        lines.append('}\n')
        fname = 'dh_bind_part%03d.cpp' % i
        keep.add(fname)
        write_if_changed(os.path.join(out_dir, fname), ''.join(lines))

    # ---- main ----
    lines = [BANNER, '#include "dh_bind.h"\n\n',
             'NB_MODULE(unify_dh_gen, m) {\n',
             '    m.doc() = "auto-generated Dahua NetSDK binding (structs + enums)";\n']
    for i in range(len(enum_shards)):
        lines.append('    init_enums%03d(m);\n' % i)
    for i in range(len(shards)):
        lines.append('    init_part%03d(m);\n' % i)
    lines.append('}\n')
    keep.add('dh_bind_main.cpp')
    write_if_changed(os.path.join(out_dir, 'dh_bind_main.cpp'), ''.join(lines))

    # ---- 清理过期分片（片数变少 / 改名后残留的旧文件）----
    removed = 0
    for fn in os.listdir(out_dir):
        if fn in keep:
            continue
        if (fn.startswith('dh_bind_') and fn.endswith('.cpp')) or fn == 'dh_bind.h':
            os.remove(os.path.join(out_dir, fn))
            removed += 1

    # ---- 汇总 ----
    out_files = sorted(os.listdir(out_dir))
    total_kb = sum(os.path.getsize(os.path.join(out_dir, f)) for f in out_files) / 1024.0
    print()
    print('已写入 %s（未变化分片未重写，清理过期文件 %d 个）' % (out_dir, removed))
    print('  文件      : %d 个（1 头 + %d 枚举片 + 1 main + %d 分片）'
          % (len(out_files), len(enum_shards), len(shards)))
    print('  字段绑定  : 标量 %d / 数组 %d / 指针 %d' % (n_scalar, n_array, n_ptr))
    print('  产物大小  : %.0f KB' % total_kb)
    return 0


if __name__ == '__main__':
    sys.exit(main())
