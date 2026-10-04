# -*- coding: utf-8 -*-
"""头文件 -> pyd 的覆盖边界：哪些完全对上、哪些跳过、哪些降级。

厂商无关：头文件路径、函数正则、回调参数语义钩子全部来自 config/<sdk>.py，
统计口径是通用的。**厂商差异只该出现在 config/ 里，不该出现在本脚本里。**

    python tools/check_coverage.py --sdk dahua
    python tools/check_coverage.py --sdk haikang
"""
import argparse
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

from common import parse
from config import CONFIGS, get_config

ap = argparse.ArgumentParser(description=__doc__)
ap.add_argument('--sdk', default='dahua', choices=sorted(CONFIGS),
                help='要检查的厂商（默认 dahua）')
args = ap.parse_args()
cfg = get_config(args.sdk)

HDR = cfg['header']
(enums, enum_names, structs, struct_names, fp_types, stats,
 typedef_names, union_names, ptr_aliases) = parse.parse_header(HDR)

text = parse.strip_comments(open(HDR, encoding="latin-1", errors="replace").read())
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

skipped = (stats["skip_funcptr"] + stats["skip_unknown"]
           + stats["skip_bitfield"] + stats["skip_reserved"])

print("=" * 68)
print("[%s] %s  ->  %s 覆盖边界"
      % (cfg['name'], os.path.basename(HDR), cfg['module']))
print("=" * 68)
print()
print("[完全对上]")
print("  枚举          %5d / %5d" % (len(enums), len(enums)))
print("  结构体        %5d / %5d" % (len(structs), len(structs)))
print("  函数          %5d / %5d    (DLL 未导出 %d 个，见 cfg['skip_funcs'])"
      % (len(funcs), len(funcs), len(cfg['skip_funcs'])))
print("  回调 typedef  %5d / %5d" % (len(cbs), len(cbs)))
print()
print("[字段 绑定 %d / 共 %d = %.2f%%]" % (n_fields - skipped, n_fields,
                                       100.0 * (n_fields - skipped) / n_fields))
print("   char[N] 文本数组   %5d  -> str    无损" % arr_char)
print("   其余数组           %5d  -> bytes   降级" % arr_other)
print()
print("[跳过 %d 个字段]" % skipped)
print("   结构体成员里的函数指针 %4d    完全未绑" % stats["skip_funcptr"])
print("   位字段                %4d    C 不允许对位域取地址，nanobind 绑不了" % stats["skip_bitfield"])
print("   未知类型              %4d    漏网函数指针 / 空类型" % stats["skip_unknown"])
print("   保留字                %4d" % stats["skip_reserved"])
unk = sorted(((k[8:], v) for k, v in stats.items() if k.startswith("unknown_")),
             key=lambda kv: -kv[1])
print("     明细: %s" % ", ".join("%s x%d" % kv for kv in unk))
print()
print("[降级：绑了但只能看]")
print("   非 char 数组 / 多维数组  %4d  拿到 bytes，需自己 struct.unpack" % arr_other)
print("   内嵌 struct/union 字段        按 bytes 暴露")
print("   outptr 输出指针               暴露为 int 地址，调用后需自己读回")
print("   无 .pyi stub                  IDE 无补全、错误码是裸数字")
print()

# ---- 回调参数分类 ----
# 这一节直接反映厂商钩子的有无，是"解耦是否到位"的体检表：
# 若 count_pred 缺失，array 必然是 0、bytes 会退化成 uintptr。
kinds = [parse.classify_cb_params(
    p, struct_names, enum_names, ptr_aliases,
    qty_pred=cfg.get('cb_qty_pred'),
    count_pred=cfg.get('cb_count_pred')) for _n, _r, p in cbs]
stat = {}
for k in kinds:
    for kind, _j in k:
        stat[kind] = stat.get(kind, 0) + 1
total_params = sum(stat.values())

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
if total_params:
    print("  （共 %d 个参数，%d 个回调）" % (total_params, len(cbs)))
