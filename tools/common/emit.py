# -*- coding: utf-8 -*-
"""通用 nanobind 代码生成：把 parse.py 产出的 IR 切成 TU 并写出 .cpp 分片。

同样**不含厂商特定逻辑**。厂商差异（头文件路径、模块名、include 指令、
文件名前缀、函数正则、未导出函数名单）全部来自 config/*.py 传入的 cfg。

**踩过的坑见 docs/implementation-notes.md** —— 本文件里几处"看起来可以简化"的
写法是刻意为之，注释里标了原因，别合并/删除：
  - `make_includes` 与 `make_cb_includes` 必须分开（第七节：12 分钟 vs 7 秒）
  - `gen_callback_binding` 用 `m.attr` 而不是 `m.def`（第一节 1.1）
  - `write_if_changed` 的 ASCII 断言（第三节 3.3）

生成物结构（cfg['file_prefix'] 决定文件名前缀）：

    {prefix}.h              分片函数声明
    {prefix}_enumsNNN.cpp   枚举分片
    {prefix}_partNNN.cpp    结构体分片
    {prefix}_funcsNNN.cpp   函数分片
    {prefix}_main.cpp       NB_MODULE + 按序调用各分片
"""
import collections
import os
import re

from common import dhcb, parse


# ------------------------------------------------------------ 字段代码生成

def gen_fields(struct_name, fields, with_dwsize, union_names, ptr_aliases=frozenset(),
               indent='        '):
    """返回结构体的字段绑定行（不含开头的 nb::class_ 注册）。"""
    alias_keys = set(ptr_aliases)
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
        # 指针别名（LPNET_X）必须和裸指针同等对待：类型名里没有 '*'，若按标量
        # 走 def_rw 会对指针成员报 C2440。
        is_ptr = '*' in base or type_name in alias_keys
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
        elif is_ptr:
            # 裸指针 / 指针别名：只暴露地址，不解引用。
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


def gen_callback(name, ret, params, kinds):
    """生成单个回调的 thunk + 注册语句。

    thunk 是交给 SDK 的 C 函数指针，签名与 typedef 逐字一致；内部把每个参数
    转换成 nanobind 能转的形态后再交给 Python 回调。注册侧只占两行。
    """
    if params:
        sig = ', '.join('%s a%d' % (p['type'], i) for i, p in enumerate(params))
        args = []
        for i, (kind, j) in enumerate(kinds):
            if kind == 'value':
                # 必须 nb::cast(...) 显式转：宏里 `nb::object _dh_args[] = {a0, ...}`
                # 要求元素已是 nb::object，而 int/long long 没有隐式转换
                # （直接传 a0 会 C2440）。
                args.append('nb::cast(a%d)' % i)
            elif kind == 'cstr':
                # NULL 安全：SDK 偶尔给空串指针，不能让 nanobind 去解引用。
                args.append('(a%d ? nb::cast(a%d) : nb::object())' % (i, i))
            elif kind == 'bytes':
                args.append('nb::bytes(reinterpret_cast<const char *>(a%d), '
                            'static_cast<std::size_t>(a%d))' % (i, j))
            elif kind == 'array':
                args.append('dhcb::as_list(a%d, static_cast<long long>(a%d))' % (i, j))
            elif kind == 'obj':
                args.append('dhcb::view(a%d)' % i)
            else:
                args.append('nb::cast(reinterpret_cast<std::uintptr_t>(a%d))' % i)
        call = ', '.join(args)
    else:
        sig, call = 'void', ''

    lines = []
    if ret and ret != 'void':
        # 有返回值（一般是 int 状态码）：未订阅 / 抛异常时一律回 0。
        lines.append('static int dh_thunk_%s(%s) {\n' % (name, sig))
        if call:
            lines.append('    return DH_CB_RET("%s", 0, %s);\n' % (name, call))
        else:
            lines.append('    return DH_CB_RET("%s", 0);\n' % name)
    else:
        lines.append('static void dh_thunk_%s(%s) {\n' % (name, sig))
        if call:
            lines.append('    DH_CB_VOID("%s", %s);\n' % (name, call))
        else:
            # 零参数回调：零长度数组不是合法 C++，用专门的 0 参数宏。
            lines.append('    DH_CB_VOID0("%s");\n' % name)
    lines.append('}\n')
    return lines


# 自测钩子能安全构造的标量类型（其余 value 参数多为传值结构体，放弃钩子）
_SELFTEST_SCALARS = frozenset("""
    void BOOL bool char short int long float double
    BYTE WORD DWORD LONG LDWORD LLONG UINT ULONGLONG
    unsigned signed
""".split())


def gen_selftest(name, params, kinds):
    """生成自测钩子：从**真正的 C++ 线程**调用该 thunk。

    为什么需要：ctypes 的 CFUNCTYPE 无法验证 GIL 路径。ctypes 回调会自己
    swap 一个 thread state 进去（gilstate_counter == 0，且 PyThreadState_
    GetUnchecked() 读不到它），于是判据"当前线程是否已附着"会误判成
    "未附着" -> 再次 attach -> Fatal Python error。真实 SDK 工作线程不会这样，
    所以只能用一个裸 std::thread 才能复现真实路径。

    自测钩子按签名自动填好固定参数，所以每个回调都能被独立验证：
        unify_dh_gen._selftest_fDataCallBack(b"\\x01\\x02")
    默认不生成（--emit-selftest 开启），避免污染交付产物。
    """
    if not params:
        return []
    call = []
    for i, (kind, j) in enumerate(kinds):
        t = params[i]['type']
        if kind == 'value':
            # 传值结构体没法用常量构造（static_cast<T>(0x1234) 编译不过），
            # 这类参数直接放弃整个钩子。
            core = re.sub(r'\b(const|struct|enum)\b', ' ', t).strip()
            if core not in _SELFTEST_SCALARS:
                return []
            call.append('static_cast<%s>(0x1234)' % t)
        elif kind == 'cstr':
            call.append('static_cast<%s>("probe")' % t)
        elif kind == 'bytes':
            call.append('reinterpret_cast<%s>(probe_bytes)' % t)
        elif kind in ('array', 'obj'):
            call.append('reinterpret_cast<%s>(probe_objs)' % t)
        else:
            call.append('static_cast<%s>(0)' % t)
    # 紧邻的字节长度 / 元素个数参数
    for i, (kind, j) in enumerate(kinds):
        if j is not None:
            n = 2 if kind == 'array' else 4
            call[j] = 'static_cast<%s>(%d)' % (params[j]['type'], n)
    return [
        '    m.attr("_selftest_%s") = nb::cpp_function([](nb::bytes payload) {\n' % name,
        '        BYTE probe_bytes[4] = {1, 2, 3, 4};\n',
        '        static char probe_objs[65536];\n',
        '        std::memset(probe_objs, 0, sizeof(probe_objs));\n',
        '        {\n',
        '            // Stage 1: bare thread + GIL round trip.\n',
        '            std::thread _probe([]() { nb::gil_scoped_acquire _g; });\n',
        '            nb::gil_scoped_release _rel0;\n',
        '            _probe.join();\n',
        '        }\n',
        '        if (payload.size() == 0)\n',
        '            return;   // stage-1-only mode, for bisecting crashes\n',
        '        std::thread _t([&]() { dh_thunk_%s(%s); });\n' % (name, ', '.join(call)),
        '        {\n',
        '            // Release the GIL before join: the thunk runs on the worker\n',
        '            // thread and must acquire it, so joining while this thread\n',
        '            // still holds it deadlocks (observed: CPU 0%, 3 threads stuck).\n',
        '            // A real SDK caller never hits this -- it returns right after\n',
        '            // registering, which drops the GIL -- so simulate that here.\n',
        '            nb::gil_scoped_release _rel;\n',
        '            _t.join();\n',
        '        }\n',
        '    });\n',
    ]


def gen_callback_binding(name):
    """注册侧：三个入口，Python 侧都是普通函数调用。

      set_fXxx(cb)    只订阅
      unbind_fXxx()   退订（不传 None：nb::object / nb::handle 都不接受 None）
      bind_fXxx(cb)   订阅并返回 C 函数指针，可直接交给 CLIENT_xxx

    必须用 `m.attr(name) = ...` 而不是 `m.def(name, ...)`：m.def 走
    analyze_method 去提取 lambda 的签名，而这里绑定的是**已经构造好的
    类型擦除 callable**（nb::object），没有签名可提取，会触发
    "analyze_method 使用类模板需要模板参数列表"。Python 侧调用形式完全一样。
    """
    return [
        '    m.attr("set_%s") = dhcb::setter("%s");\n' % (name, name),
        '    m.attr("unbind_%s") = dhcb::unbinder("%s");\n' % (name, name),
        '    m.attr("bind_%s") = dhcb::binder("%s",\n'
        '        reinterpret_cast<void *>(&dh_thunk_%s));\n' % (name, name, name),
    ]


def write_if_changed(path, text):
    """内容不变就不写文件，避免 mtime 变化导致 ninja 无谓重编整个分片。

    同时强制 ASCII：生成物是给 MSVC 读的，非 ASCII 会触发 C4819；而
    `open(..., 'w', encoding='ascii')` 是写到第一个非 ASCII 字符时才抛
    UnicodeEncodeError，报错里完全看不出是哪句注释写的。
    """
    try:
        text.encode('ascii')
    except UnicodeEncodeError as e:
        bad = text[max(0, e.start - 60):e.start + 60]
        raise ValueError(
            '生成内容含非 ASCII 字符（写入 %s 会因此崩溃）。\n'
            '  位置: %r\n  上下文: ...%s...\n'
            '  生成代码里的注释必须用 ASCII；中文说明请留在 Python 侧 docstring。'
            % (os.path.basename(path), e.start, bad.replace('\n', '\\n')))
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


def make_cb_includes(cfg):
    """回调分片额外需要的运行时头。

    刻意与 make_includes 分开：回调运行时头只被 *_cbsNNN.cpp 需要，若混进
    公共 include，dh_bind_cb.h 一改就会把 146 个结构体/枚举/函数分片全部拖去
    重编（实测 612s vs 6.9s）。
    """
    return ('#include "%s_cb.h"\n\n' % cfg['file_prefix']
            + '#include <thread>\n\n')


# ------------------------------------------------------------------ 主流程

def generate(cfg, args):
    header = cfg['header']
    prefix = cfg['file_prefix']

    if not os.path.isfile(header):
        print('找不到头文件:', header)
        return 1

    print('解析[%s]:' % cfg['name'], header)
    (enums, enum_names, structs, struct_names, fp_types, stats,
     typedef_names, union_names, ptr_aliases) = parse.parse_header(header)
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

    deps = parse.build_deps(structs, struct_names, ptr_aliases)
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

    # ---- 回调：解析 + 参数分类 ----
    # 分类规则全在 parse.classify_cb_params 里（靠参数名而非位置判断数量），
    # 这里只负责统计和分片。
    callbacks = parse.parse_callbacks(text)
    cb_stat = collections.Counter()
    bindable_cbs = []
    for cname, cret, cparams in callbacks:
        kinds = parse.classify_cb_params(cparams, struct_names, enum_names, ptr_aliases)
        for k, _ in kinds:
            cb_stat[k] += 1
        bindable_cbs.append((cname, cret, cparams, kinds))
    print('  回调      : %d 个（共 %d 个参数）'
          % (len(bindable_cbs), sum(cb_stat.values())))
    print('    参数分类: value %d / obj %d / uintptr %d / cstr %d / bytes %d / array %d'
          % (cb_stat['value'], cb_stat['obj'], cb_stat['uintptr'],
             cb_stat['cstr'], cb_stat['bytes'], cb_stat['array']))

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
    CB_INCLUDES = make_cb_includes(cfg)

    # ---- 枚举分片 ----
    # 1873 个枚举挤在一个 TU 里是约 150 秒的死疙瘩，且 /Od 救不了它
    # （瓶颈是 nb::enum_ 的模板实例化次数本身，不是优化器）。拆片才能并行。
    enum_shards = [enums[i:i + args.enums_per_tu]
                   for i in range(0, len(enums), args.enums_per_tu)] or [[]]
    func_shards = [bindable_funcs[i:i + args.funcs_per_tu]
                   for i in range(0, len(bindable_funcs), args.funcs_per_tu)] or [[]]

    cb_shards = [bindable_cbs[i:i + args.cbs_per_tu]
                 for i in range(0, len(bindable_cbs), args.cbs_per_tu)] or [[]]

    # ---- {prefix}.h ----
    lines = [BANNER, '#pragma once\n', '#include <nanobind/nanobind.h>\n\n']
    for i in range(len(enum_shards)):
        lines.append('void init_enums%03d(nanobind::module_ &m);\n' % i)
    for i in range(len(shards)):
        lines.append('void init_part%03d(nanobind::module_ &m);\n' % i)
    for i in range(len(func_shards)):
        lines.append('void init_funcs%03d(nanobind::module_ &m);\n' % i)
    for i in range(len(cb_shards)):
        lines.append('void init_cbs%03d(nanobind::module_ &m);\n' % i)
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
            lines += gen_fields(name, fields, has_dwsize, union_names, ptr_aliases)
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

    # ---- 回调运行时支持（槽位注册表 + GIL/异常隔离宏）----
    cb_header_name = '%s_cb.h' % prefix
    keep.add(cb_header_name)
    write_if_changed(os.path.join(out_dir, cb_header_name), dhcb.HEADER)

    # ---- 回调 thunk + 注册 ----
    for i, chunk in enumerate(cb_shards):
        lines = [BANNER, INCLUDES, CB_INCLUDES]
        # thunk 必须定义在**文件作用域**：C++ 不允许在函数体内定义函数
        # （MSVC C2601 "本地函数定义是非法的"）。init 里只放注册语句。
        for cname, cret, cparams, kinds in chunk:
            lines += gen_callback(cname, cret, cparams, kinds)
        lines.append('\nvoid init_cbs%03d(nb::module_ &m) {\n' % i)
        for cname, cret, cparams, kinds in chunk:
            lines += gen_callback_binding(cname)
            if args.emit_selftest:
                lines += gen_selftest(cname, cparams, kinds)
        lines.append('}\n')
        fname = '%s_cbs%03d.cpp' % (prefix, i)
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
    for i in range(len(cb_shards)):
        lines.append('    init_cbs%03d(m);\n' % i)
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
