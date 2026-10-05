# -*- coding: utf-8 -*-
"""头文件 -> pyd 的覆盖边界：哪些完全对上、哪些跳过、哪些降级。

厂商无关：头文件路径、函数正则、回调参数语义钩子全部来自 config/<sdk>.py，
统计口径是通用的。**厂商差异只该出现在 config/ 里，不该出现在本脚本里。**

    python native/codegen/check_coverage.py --sdk dahua
    python native/codegen/check_coverage.py --sdk haikang

本模块只有一个纯函数 `collect(sdk)` 负责算数字，`main()` 只负责排版打印。
分开的原因是 `native/tests/test_coverage_regression.py` 要直接复用同一批数字
做断言 —— 断言和打印必须是**同一个数据源**，否则两边的口径迟早会漂。
"""
import argparse
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from common import parse
from config import CONFIGS, get_config


def collect(sdk):
    """算出某厂商的全部覆盖边界数字（无打印、无全局副作用，可在测试里直接调）。

    返回 dict 的键就是 main() 打印时用到的全部量；键名尽量与打印文案对应。
    """
    cfg = get_config(sdk)
    hdr = cfg['header']

    # filters 必须传：厂商 filter（海康的"条件编译裁剪"）会改文本，生成器用的是
    # 裁剪后的文本。不传的话这里的数字描述的是一个**并不存在的产物** —— 海康实测
    # 差 2 个结构体 / 29 个字段（2670/18821 vs 实际 2668/18792）。
    filters = cfg.get('text_filters')
    (enums, enum_names, structs, struct_names, _fp_types, stats,
     _typedef_names, _union_names, ptr_aliases) = parse.parse_header(
         hdr, filters=filters)

    # 与 emit.generate 读同一份文本（load_header = 去注释 + 厂商 filter）
    text = parse.load_header(hdr, filters)
    funcs = parse.parse_funcs(text, cfg['func_re'])
    cbs = parse.parse_callbacks(text)

    n_fields = sum(len(f) for _, f in structs)

    # 数组字段细分：char[N] 是 str（无损），其余是 bytes（降级）
    arr_char = arr_other = 0
    for _s, flds in structs:
        for ftype, _fn, arr in flds:
            if not arr:
                continue
            if ftype.replace(" ", "") == "char" and arr.count("[") == 1:
                arr_char += 1
            else:
                arr_other += 1

    skipped = {
        'funcptr': stats["skip_funcptr"],      # 结构体成员里的函数指针，完全未绑
        'bitfield': stats["skip_bitfield"],    # C 不允许对位域取地址，nanobind 绑不了
        'unknown': stats["skip_unknown"],      # 漏网函数指针 / 空类型
        'reserved': stats["skip_reserved"],
    }
    skipped_total = sum(skipped.values())

    # ---- 回调参数分类 ----
    # 这一节直接反映厂商钩子的有无，是"解耦是否到位"的体检表：
    # 若 count_pred 缺失，array 必然是 0、bytes 会退化成 uintptr。
    stat = {}
    for _n, _r, p in cbs:
        for kind, _j in parse.classify_cb_params(
                p, struct_names, enum_names, ptr_aliases,
                qty_pred=cfg.get('cb_qty_pred'),
                count_pred=cfg.get('cb_count_pred')):
            stat[kind] = stat.get(kind, 0) + 1

    return {
        'cfg': cfg,
        'header': hdr,
        'enums': len(enums),
        'structs': len(structs),
        'funcs': len(funcs),
        'callbacks': len(cbs),
        'fields_total': n_fields,
        'fields_bound': n_fields - skipped_total,
        'arr_char': arr_char,
        'arr_other': arr_other,
        'skipped': skipped,
        'skipped_total': skipped_total,
        # unknown_* 明细（键是 stats 里的 unknown_<类型>）
        'unknown_detail': sorted(
            ((k[8:], v) for k, v in stats.items() if k.startswith("unknown_")),
            key=lambda kv: -kv[1]),
        'cb_kinds': stat,
        'cb_params_total': sum(stat.values()),
    }


def report(c):
    """把 collect() 的结果排版打印。文案与拆分前逐字一致。"""
    cfg = c['cfg']
    print("=" * 68)
    print("[%s] %s  ->  %s 覆盖边界"
          % (cfg['name'], os.path.basename(c['header']), cfg['module']))
    print("=" * 68)
    print()
    print("[完全对上]")
    print("  枚举          %5d / %5d" % (c['enums'], c['enums']))
    print("  结构体        %5d / %5d" % (c['structs'], c['structs']))
    print("  函数          %5d / %5d    (DLL 未导出 %d 个，见 cfg['skip_funcs'])"
          % (c['funcs'], c['funcs'], len(cfg['skip_funcs'])))
    print("  回调 typedef  %5d / %5d" % (c['callbacks'], c['callbacks']))
    print()
    print("[字段 绑定 %d / 共 %d = %.2f%%]"
          % (c['fields_bound'], c['fields_total'],
             100.0 * c['fields_bound'] / c['fields_total']))
    print("   char[N] 文本数组   %5d  -> str    无损" % c['arr_char'])
    print("   其余数组           %5d  -> bytes   降级" % c['arr_other'])
    print()
    print("[跳过 %d 个字段]" % c['skipped_total'])
    print("   结构体成员里的函数指针 %4d    完全未绑" % c['skipped']['funcptr'])
    print("   位字段                %4d    C 不允许对位域取地址，nanobind 绑不了"
          % c['skipped']['bitfield'])
    print("   未知类型              %4d    漏网函数指针 / 空类型" % c['skipped']['unknown'])
    print("   保留字                %4d" % c['skipped']['reserved'])
    print("     明细: %s" % ", ".join("%s x%d" % kv for kv in c['unknown_detail']))
    print()
    print("[降级：绑了但只能看]")
    print("   非 char 数组 / 多维数组  %4d  拿到 bytes，需自己 struct.unpack" % c['arr_other'])
    print("   内嵌 struct/union 字段        按 bytes 暴露")
    print("   outptr 输出指针               暴露为 int 地址，调用后需自己读回")
    print("   错误码裸数字                  厂商错误码无符号名，待错误码表")
    print()

    stat = c['cb_kinds']
    print("[回调参数分类：Python 侧实际会看到什么]")
    print("  value %d（标量/枚举，原样转发） / cstr %d（char* -> str）"
          % (stat.get('value', 0), stat.get('cstr', 0)))
    print("  obj %d（结构体指针 -> 单个借用视图） / uintptr %d（其他指针 -> int 地址）"
          % (stat.get('obj', 0), stat.get('uintptr', 0)))
    print("  bytes %d（BYTE* + 长度 -> bytes） / array %d（结构体数组 -> list）"
          % (stat.get('bytes', 0), stat.get('array', 0)))
    print()
    if cfg.get('cb_count_pred'):
        print("  厂商钩子：已启用（cfg['cb_qty_pred'] / cfg['cb_count_pred']）")
    else:
        print("  厂商钩子：**未启用** —— 本厂商没有数量/长度语义规则，")
        print("  于是 array 恒为 0、BYTE* 只能给 int 地址（少给而非给错）。")
        print("  这是有意的保守退化：要写规则请照该厂商的实际回调行为，别照抄别家。")
    if c['cb_params_total']:
        print("  （共 %d 个参数，%d 个回调）" % (c['cb_params_total'], c['callbacks']))


def main():
    # 只在作为脚本运行时换 stdout：import 本模块（测试会这么干）不该动全局流。
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--sdk', default='dahua', choices=sorted(CONFIGS),
                    help='要检查的厂商（默认 dahua）')
    args = ap.parse_args()
    report(collect(args.sdk))


if __name__ == "__main__":
    main()