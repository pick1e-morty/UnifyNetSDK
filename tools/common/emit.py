# -*- coding: utf-8 -*-
"""通用 nanobind 代码生成：把 parse.py 产出的 IR 切成 TU 并写出 .cpp 分片。

同样**不含厂商特定逻辑**。厂商差异（头文件路径、模块名、include 指令、
文件名前缀、函数正则、未导出函数名单）全部来自 config/*.py 传入的 cfg。

生成物结构（cfg['file_prefix'] 决定文件名前缀）：

    {prefix}.h              分片函数声明
    {prefix}_enumsNNN.cpp   枚举分片
    {prefix}_partNNN.cpp    结构体分片
    {prefix}_funcsNNN.cpp   函数分片
    {prefix}_main.cpp       NB_MODULE + 按序调用各分片
"""
import collections
import os

from common import parse


# ------------------------------------------------------------ 字段代码生成

def gen_fields(struct_name, fields, with_dwsize, union_names, indent='        '):
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
        type_name = base.replace('unsigned', ' ').replace('signed', ' ').strip().rstrip('*').strip()
        if arr:
            n = arr.strip()
            # 多维数组（[4][32]）无论元素类型一律按 bytes：char[4][32] 不是
            # 单个 C 字符串，按 str 截断语义是错的。
            if base.replace(' ', '') == 'char' and arr.count('[') == 1:
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
        elif base in ('__struct__', '__union__'):
            # 内嵌有名 struct/union 字段：匿名类型无法注册 nb::class_，
            # 按 bytes 暴露原始内存（取地址用 &，字段是标量不会退化成指针）。
            lines += [
                indent + '.def_prop_rw("%s",' % fname,
                indent + '    [](const %s &s) {' % struct_name,
                indent + '        return nb::bytes(reinterpret_cast<const char *>(&s.%s), sizeof(s.%s));' % (fname, fname),
                indent + '    },',
                indent + '    [](%s &s, const nb::bytes &v) {' % struct_name,
                indent + '        std::size_t n = v.size() < sizeof(s.%s) ? v.size() : sizeof(s.%s);' % (fname, fname),
                indent + '        std::memcpy(&s.%s, v.data(), n);' % fname,
                indent + '    })',
            ]
        elif type_name in union_names:
            # union 字段：多个成员共享一块内存，按 bytes 暴露原始内存。
            # 取地址用 &（union 字段是标量，不像数组会退化成指针）。
            lines += [
                indent + '.def_prop_rw("%s",' % fname,
                indent + '    [](const %s &s) {' % struct_name,
                indent + '        return nb::bytes(reinterpret_cast<const char *>(&s.%s), sizeof(s.%s));' % (fname, fname),
                indent + '    },',
                indent + '    [](%s &s, const nb::bytes &v) {' % struct_name,
                indent + '        std::size_t n = v.size() < sizeof(s.%s) ? v.size() : sizeof(s.%s);' % (fname, fname),
                indent + '        std::memcpy(&s.%s, v.data(), n);' % fname,
                indent + '    })',
            ]
        else:
            # 标量 / typedef 别名 / 枚举 / 结构体，交给 nanobind 的 caster
            lines.append(indent + '.def_rw("%s", &%s::%s)' % (fname, struct_name, fname))
    # 每行自带换行符。外层用 ''.join 拼接，缺 \n 会把一个结构体的所有字段
    # 挤成一行（单行可达数万字符），MSVC 处理超长行会明显变慢。
    return [l + '\n' for l in lines]


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


def make_includes(cfg):
    return (
        '#define NOMINMAX\n'
        '#include <nanobind/nanobind.h>\n'
        '#include <nanobind/stl/string.h>\n'
        '#include <cstddef>\n'
        '#include <cstdint>\n'
        '#include <cstring>\n'
        '#include <string>\n'
        + cfg['include'] + '\n'
        + '#include "%s.h"\n\n' % cfg['file_prefix']
        + 'namespace nb = nanobind;\n\n'
    )


# ------------------------------------------------------------------ 主流程

def generate(cfg, args):
    header = cfg['header']
    prefix = cfg['file_prefix']

    if not os.path.isfile(header):
        print('找不到头文件:', header)
        return 1

    print('解析[%s]:' % cfg['name'], header)
    enums, enum_names, structs, struct_names, fp_types, stats, typedef_names, union_names = parse.parse_header(header)
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

    # ---- 函数：先分类，能安全绑的才生成 ----
    text = parse.strip_comments(open(header, encoding='latin-1', errors='replace').read())
    funcs = parse.parse_funcs(text, cfg['func_re'])
    func_stat = collections.Counter()
    bindable_funcs = []
    for fname, ret, params in funcs:
        if fname in cfg['skip_funcs']:
            func_stat['skip_undefined'] += 1
            continue
        flines, reason = parse.gen_func(fname, ret, params, struct_names, enum_names, fp_types)
        if flines is None:
            func_stat['skip_' + reason] += 1
        else:
            bindable_funcs.append((fname, flines))
            func_stat['bound'] += 1
    print('  函数      : %d 个（可绑 %d / 未导出跳过 %d / 其他跳过 %d）'
          % (len(funcs), func_stat['bound'],
             func_stat['skip_undefined'], func_stat['skip_skip']))

    deps = parse.build_deps(structs, struct_names)
    n_dep = sum(1 for v in deps.values() if v)
    print('  有类型依赖的结构体: %d 个' % n_dep)

    order = parse.topo_order(structs, deps)
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

    out_dir = args.out_dir or cfg['out_dir']
    os.makedirs(out_dir, exist_ok=True)
    # 本次生成会产出的文件集合：内容不变就不重写（保持 mtime 不变，让
    # ninja 跳过未变化的分片）；生成结束后清掉不在集合里的过期旧文件。
    keep = set()

    BANNER = '// AUTO-GENERATED by tools/gen_bind.py -- DO NOT EDIT\n'
    INCLUDES = make_includes(cfg)

    # ---- 枚举分片 ----
    # 1873 个枚举挤在一个 TU 里是约 150 秒的死疙瘩，且 /Od 救不了它
    # （瓶颈是 nb::enum_ 的模板实例化次数本身，不是优化器）。拆片才能并行。
    enum_shards = [enums[i:i + args.enums_per_tu]
                   for i in range(0, len(enums), args.enums_per_tu)] or [[]]
    func_shards = [bindable_funcs[i:i + args.funcs_per_tu]
                   for i in range(0, len(bindable_funcs), args.funcs_per_tu)] or [[]]

    # ---- {prefix}.h ----
    lines = [BANNER, '#pragma once\n', '#include <nanobind/nanobind.h>\n\n']
    for i in range(len(enum_shards)):
        lines.append('void init_enums%03d(nanobind::module_ &m);\n' % i)
    for i in range(len(shards)):
        lines.append('void init_part%03d(nanobind::module_ &m);\n' % i)
    for i in range(len(func_shards)):
        lines.append('void init_funcs%03d(nanobind::module_ &m);\n' % i)
    keep.add('%s.h' % prefix)
    write_if_changed(os.path.join(out_dir, '%s.h' % prefix), ''.join(lines))

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
        fname = '%s_enums%03d.cpp' % (prefix, i)
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
            lines += gen_fields(name, fields, has_dwsize, union_names)
            lines.append('        ;\n')
            for _t, _fn, a in fields:
                if a:
                    n_array += 1
                else:
                    n_scalar += 1
            n_ptr += sum(1 for t, _, _ in fields if '*' in t)
        lines.append('}\n')
        fname = '%s_part%03d.cpp' % (prefix, i)
        keep.add(fname)
        write_if_changed(os.path.join(out_dir, fname), ''.join(lines))

    # ---- 函数 ----
    for i, chunk in enumerate(func_shards):
        lines = [BANNER, INCLUDES, 'void init_funcs%03d(nb::module_ &m) {\n' % i]
        for _fname, flines in chunk:
            lines += flines
            lines.append('        ;\n')
        lines.append('}\n')
        fname = '%s_funcs%03d.cpp' % (prefix, i)
        keep.add(fname)
        write_if_changed(os.path.join(out_dir, fname), ''.join(lines))

    # ---- main ----
    lines = [BANNER, '#include "%s.h"\n\n' % prefix,
             'NB_MODULE(%s, m) {\n' % cfg['module'],
             '    m.doc() = "%s";\n' % cfg['doc']]
    for i in range(len(enum_shards)):
        lines.append('    init_enums%03d(m);\n' % i)
    for i in range(len(shards)):
        lines.append('    init_part%03d(m);\n' % i)
    for i in range(len(func_shards)):
        lines.append('    init_funcs%03d(m);\n' % i)
    lines.append('}\n')
    keep.add('%s_main.cpp' % prefix)
    write_if_changed(os.path.join(out_dir, '%s_main.cpp' % prefix), ''.join(lines))

    # ---- 清理过期分片（片数变少 / 改名后残留的旧文件）----
    removed = 0
    for fn in os.listdir(out_dir):
        if fn in keep:
            continue
        if (fn.startswith('%s_' % prefix) and fn.endswith('.cpp')) or fn == '%s.h' % prefix:
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
