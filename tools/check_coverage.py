# -*- coding: utf-8 -*-
"""dhnetsdk.h -> pyd 的覆盖边界：哪些完全对上、哪些跳过、哪些降级。"""
import io
import sys

sys.path.insert(0, r"C:\Users\Hast\Documents\CodeProjects\UnifyNetSDK\tools")
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

from common import parse
from config import get_config

HDR = r"C:\Users\Hast\Documents\CodeProjects\UnifyNetSDK\dahua\C_Win64\Include\Common\dhnetsdk.h"
(enums, enum_names, structs, struct_names, fp_types, stats,
 typedef_names, union_names, ptr_aliases) = parse.parse_header(HDR)

text = parse.strip_comments(open(HDR, encoding="latin-1", errors="replace").read())
funcs = parse.parse_funcs(text, get_config("dahua")["func_re"])
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
print("大华 dhnetsdk.h  ->  unify_dh_gen / unify_dh  覆盖边界")
print("=" * 68)
print()
print("[完全对上]")
print("  枚举          %5d / %5d" % (len(enums), len(enums)))
print("  结构体        %5d / %5d" % (len(structs), len(structs)))
print("  函数          %5d / %5d    (头文件声明 2521，6 个 DLL 未导出)" % (len(funcs), len(funcs)))
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
