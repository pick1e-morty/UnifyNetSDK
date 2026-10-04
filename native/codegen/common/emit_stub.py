# -*- coding: utf-8 -*-
""".pyi stub 发射器：IR 的第二个消费者。

emit.py 把 IR 变成 C++ 分片，本模块把**同一份 IR** 变成 `{module}.pyi`，
给 IDE 补全 / 类型检查用。同样**不含厂商特定逻辑**：双厂商零特判，
cfg 只提供模块名、路径等数据。

**类型注解必须与运行时绑定逐字一致 —— stub 说谎比没有 stub 更糟。**
所以每条映射都对照 emit.gen_fields / parse.classify_param 的实际分支：

  字段（emit.gen_fields 的分支顺序）         运行时            stub
  char[N]（一维）                        -> str             str
  其余数组（BYTE[N]/多维/结构体[N]）     -> bytes           bytes
  裸指针 / LP 别名 / OPAQUE_PTR          -> int 地址         int
  有名内嵌 struct/union / union 类型     -> bytes           bytes
  枚举字段                               -> 枚举实例         枚举类名
  结构体标量字段                         -> 实例             结构体类名
  其余标量 / 整数别名（DWORD...）        -> int / float     int / float
  裸 char（无 unsigned/signed）          -> 单字符 str      str
    （unsigned char / BYTE 归一化后 core 同为 'char'，运行时是 int，
     必须看原始类型文本区分 —— 校验对拍实测逮到过这个 lie）

  函数参数（parse.classify_param）           stub
  cstr                                  -> str
  objptr（结构体/枚举指针）              -> 类名（借用视图）
  uintptr / funcptr / outptr / 数组      -> int（地址）
  value                                 -> 标量 / 类名

  函数返回值：void -> None；结构体指针别名（LPNET_X，注册过的类型指针）
  -> 目标类名；char* -> bytes；HWND 等句柄 -> int；其余按标量映射。

pyi 是**不执行的**：注解不求值，类型前向引用无需排序，IR 顺序直接输出。
枚举成员**不写值**（C 表达式无法在此安全求值，且 pyd 的 nb::enum_ 已携带
真值），只写 `成员: int`。`dwSize` 结构体的零初始化 __init__ 与默认
nb::init<>() 在 stub 里同为无参，统一注解为 `def __init__(self) -> None`。

C 标识符可能是 Python 关键字 / 非 Python 标识符，这类成员无法写进 pyi：
跳过并在生成时报告数量（运行时属性仍存在，只是没有注解）。

产物写两份：`cfg['out_dir']`（生成器管辖区）与 `cfg['build_dir']`（pyd
同目录，IDE 按模块名 `unify_xxx_gen.pyi` 自动识别，README 的
`sys.path.insert(native/build)` 用法开箱即得）。两份内容一致，
write_if_changed 保证 mtime 稳定。
"""
import keyword
import os

from common import parse
from common.writeout import write_if_changed


def _core_name(ftype):
    """剥 unsigned/signed/指针，返回基础类型名（与 emit.gen_fields 同口径）。"""
    return (ftype.strip().replace('unsigned', ' ').replace('signed', ' ')
            .strip().rstrip('*').strip())


def _field_anno(ftype, arr, union_names, alias_keys, struct_names, enum_names):
    """字段注解。分支顺序镜像 emit.gen_fields，改绑定不改这里（反之亦然）。"""
    base = ftype.strip()
    if arr:
        # 一维 char[N] 是 C 字符串 -> str；多维 char 不是单个字符串，其余
        # 数组一律原始内存 -> bytes（与 gen_fields 一致）。
        if base.replace(' ', '') == 'char' and arr.count('[') == 1:
            return 'str'
        return 'bytes'
    core = _core_name(base)
    if '*' in base or core in alias_keys or core in parse.OPAQUE_PTR:
        return 'int'
    if base in ('__struct__', '__union__'):
        return 'bytes'
    if core in union_names:
        return 'bytes'
    if core in enum_names or core in struct_names:
        return core
    if core == 'bool':
        return 'bool'
    # 裸 char（非数组、无 unsigned/signed）运行时是单字符 str；注意
    # unsigned char / BYTE 归一化后 core 也是 'char'，但运行时是 int ——
    # 必须看原始类型文本区分（校验对拍实测逮到过这个 lie）。
    if core == 'char' and 'unsigned' not in base and 'signed' not in base:
        return 'str'
    return 'float' if core in ('float', 'double') else 'int'


def _param_anno(p, fp_types, struct_names, enum_names, alias_keys):
    """函数参数注解：分类直接复用 parse.classify_param（与 gen_func 同源）。"""
    kind = parse.classify_param(p, struct_names, enum_names, fp_types)
    if kind == 'cstr':
        return 'str'
    if kind == 'objptr':
        core = p['type'].replace('*', '').strip()
        if core.startswith('const '):
            core = core[6:].strip()
        return core
    if kind == 'value':
        t = p['type']
        core = _core_name(t.replace('const', ' '))
        if core in struct_names or core in enum_names:
            return core
        if core == 'bool':
            return 'bool'
        if core == 'char' and 'unsigned' not in t and 'signed' not in t:
            return 'str'
        return 'float' if core in ('float', 'double') else 'int'
    # uintptr / funcptr / outptr（含数组参数，C 里等价指针）-> int 地址
    return 'int'


def _ret_anno(ret, struct_names, enum_names, alias_keys):
    """返回值注解。注意 LPNET_X 这类指针别名：运行时 nanobind 把
    "指向已注册类型的指针"转成实例（不是 int），所以按目标类名注解。"""
    t = ret.strip()
    if t == 'void':
        return 'None'
    core = _core_name(t.replace('const', ' '))
    if core in alias_keys:
        return alias_keys[core]
    if '*' in t or core in parse.OPAQUE_PTR:
        if core == 'char':
            return 'bytes'
        if core in struct_names or core in enum_names:
            return core
        return 'int'
    if core in struct_names or core in enum_names:
        return core
    if core == 'bool':
        return 'bool'
    if core == 'char' and 'unsigned' not in t and 'signed' not in t:
        return 'str'
    return 'float' if core in ('float', 'double') else 'int'


def _safe_ident(name):
    """C 标识符是否可直接作为 Python 属性名。"""
    return name.isidentifier() and not keyword.iskeyword(name)


def write(cfg, fp_types, enums, structs, struct_names, enum_names,
          union_names, ptr_aliases, funcs, cb_names, selftest_names):
    """生成 {module}.pyi。入参全部来自 emit.generate 的解析结果（同一份 IR）。"""
    prefix = cfg['file_prefix']
    alias_keys = set(ptr_aliases)
    skipped = 0            # 无法写进 pyi 的成员数（非 Python 标识符 / 关键字）
    lines = [
        '# AUTO-GENERATED by native/codegen/common/emit_stub.py -- DO NOT EDIT.\n'
        '# Regenerate: python native/codegen/gen_bind.py --sdk %s\n' % cfg['name'],
        '#\n'
        '# Types mirror the runtime bindings exactly:\n'
        '#   char[N] -> str | other arrays / nested unions -> bytes |\n'
        '#   pointers, LP aliases, HWND/HANDLE -> int (address) |\n'
        '#   enums -> enum.IntEnum (member values live at runtime)\n',
        'import enum as _enum\n',
        '\n',
        'from typing import Callable\n',
        '\n',
    ]

    # ---- 枚举 ----
    n_enum_members = 0
    for ename, items in enums:
        lines.append('class %s(_enum.IntEnum):\n' % ename)
        wrote = 0
        seen = set()
        for iname, _ival in items:
            if not _safe_ident(iname) or iname in seen:
                skipped += 1
                continue
            seen.add(iname)
            lines.append('    %s: int\n' % iname)
            n_enum_members += 1
            wrote += 1
        if not wrote:
            lines.append('    ...\n')
        lines.append('\n')

    # ---- 结构体 ----
    n_fields = 0
    for sname, fields in structs:
        lines.append('class %s:\n' % sname)
        for ftype, fname, arr in fields:
            if not _safe_ident(fname):
                skipped += 1
                continue
            anno = _field_anno(ftype, arr, union_names, alias_keys,
                               struct_names, enum_names)
            lines.append('    %s: %s\n' % (fname, anno))
            n_fields += 1
        lines.append('    def __init__(self) -> None: ...\n')
        lines.append('\n')

    # ---- 函数 ----
    n_funcs = 0
    for fname, ret, params in funcs:
        anns = []
        for i, p in enumerate(params):
            name = p['name'] or ('arg%d' % i)
            if not _safe_ident(name):
                name = 'arg%d' % i
            anns.append('%s: %s' % (name, _param_anno(
                p, fp_types, struct_names, enum_names, alias_keys)))
            if p.get('has_default'):
                anns[-1] += ' = ...'
        lines.append('def %s(%s) -> %s: ...\n' % (
            fname, ', '.join(anns),
            _ret_anno(ret, struct_names, enum_names, alias_keys)))
        n_funcs += 1
    lines.append('\n')

    # ---- 回调三件套 + 自测钩子 ----
    n_cbs = 0
    for cname in cb_names:
        lines.append('def bind_%s(cb: Callable[..., int | None]) -> int: ...\n'
                     % cname)
        lines.append('def set_%s(cb: Callable[..., int | None]) -> None: ...\n'
                     % cname)
        lines.append('def unbind_%s() -> None: ...\n' % cname)
        if cname in selftest_names:
            lines.append('def _selftest_%s(payload: bytes) -> None: ...\n'
                         % cname)
        n_cbs += 1
    lines.append('\n')

    text = ''.join(lines)
    targets = [os.path.join(cfg['out_dir'], '%s.pyi' % cfg['module'])]
    build_dir = cfg.get('build_dir')
    if build_dir and os.path.isdir(build_dir):
        # pyd 同目录放一份：IDE 按模块名识别，README 的用法开箱即得
        targets.append(os.path.join(build_dir, '%s.pyi' % cfg['module']))
    for path in targets:
        write_if_changed(path, text)
    print('  stub       : %s（枚举 %d / 结构体 %d / 函数 %d / 回调 %d；'
          '跳过非 Python 标识符 %d 项；%.1f MB x %d 份）'
          % (', '.join(os.path.basename(p) for p in targets),
             len(enums), len(structs), n_funcs, n_cbs,
             skipped, len(text.encode('ascii')) / 1048576.0, len(targets)))
