# -*- coding: utf-8 -*-
"""把两个厂商 SDK 的编译/运行必需文件同步到统一的纯 ASCII 路径。

为什么做这件事：海康 SDK 的目录名是中文（"头文件" / "库文件"），而
MSVC / batch / dumpbin 等工具链对中文路径的处理并不可靠 —— 实测 CMake 的
message() 打印会乱码、bat 里传中文路径会让工具直接失败。大华的路径本来就是
纯 ASCII，但两边结构不一致会让后来的人猜"哪个是有意的"，所以两边一起统一：

    vendor/dahua/sdk_win64/{include,lib,bin}/
    vendor/haikang/sdk_win64/{include,lib,bin}/

vendor 原始目录保持不动，只作为复制源。

**不要靠依赖分析决定复制哪些 DLL。** 曾写过一个解析 PE import 表的脚本算依赖
闭包，结果它报告大华 dhnetsdk.dll "无本目录依赖" —— 因为 OpenSSL 那些库是
**延迟加载（delay-load）**的，静态 import 表里根本看不到，等运行时才会报"找不到
指定模块"。所以 bin/ 下的 .dll **全复制**，只按扩展名过滤（这也顺带排除了
639 MB 的 dhnetsdk.dll.i64 —— 那是 IDA 的数据库，不是 SDK 的一部分）。

用法：
    python tools/sync_sdk.py            # 全量同步
    python tools/sync_sdk.py --check    # 只校验，不复制；不一致时非零退出
    python tools/sync_sdk.py --sdk dahua
"""
import argparse
import filecmp
import io
import os
import shutil
import sys

# 厂商配置在 <root>/native/codegen/ 下（跟着 native 走 —— 它的产物就是 native
# 的绑定代码），而本文件留在 <root>/tools/，所以要跨目录把 codegen 挂进 sys.path。
# 别改回 os.path.dirname(__file__)：那会指向 tools/，config 不在那里。
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(_HERE), 'native', 'codegen'))
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

from config import get_config

# 目标子目录 -> 接受的扩展名。include 只收 .h；lib 收 .lib；bin 只收 .dll。
GROUPS = {
    "include": (".h",),
    "lib": (".lib",),
    "bin": (".dll",),
}


def needs_sync(src, dst):
    """目标缺失 / 大小不同 / 内容不同，都要同步。"""
    if not os.path.isfile(dst):
        return True
    try:
        if os.path.getsize(src) != os.path.getsize(dst):
            return True
        return not filecmp.cmp(src, dst, shallow=False)
    except OSError:
        return True


def sync_one(sdk, check_only):
    cfg = get_config(sdk)
    src_root = cfg["sdk_src"]
    dst_root = cfg["sdk_dir"]

    copied, uptodate, problems = [], [], []
    for group, exts in GROUPS.items():
        srcdir = src_root.get(group)
        dstdir = os.path.join(dst_root, group)
        if not srcdir or not os.path.isdir(srcdir):
            problems.append("源目录不存在: %s/%s" % (sdk, group))
            continue
        for fn in sorted(os.listdir(srcdir)):
            if not fn.lower().endswith(exts):
                continue
            src = os.path.join(srcdir, fn)
            dst = os.path.join(dstdir, fn)
            if not needs_sync(src, dst):
                uptodate.append("%s/%s" % (group, fn))
                continue
            if not check_only:
                os.makedirs(dstdir, exist_ok=True)
                shutil.copy2(src, dst)   # copy2 保留 mtime
            copied.append("%s/%s" % (group, fn))

    # 源里已删除、目标还留着的残留
    stale = []
    if os.path.isdir(dst_root):
        for group in GROUPS:
            dstdir = os.path.join(dst_root, group)
            srcdir = src_root.get(group) or ""
            if not os.path.isdir(dstdir) or not os.path.isdir(srcdir):
                continue
            for fn in os.listdir(dstdir):
                if not os.path.isfile(os.path.join(srcdir, fn)):
                    stale.append("%s/%s" % (group, fn))
    return copied, uptodate, stale, problems


def main():
    ap = argparse.ArgumentParser(description="同步厂商 SDK 到纯 ASCII 路径")
    ap.add_argument("--sdk", default="all", choices=["dahua", "haikang", "all"])
    ap.add_argument("--check", action="store_true",
                    help="只校验是否最新，不复制；不一致时非零退出")
    args = ap.parse_args()

    sdks = ["dahua", "haikang"] if args.sdk == "all" else [args.sdk]
    rc = 0
    for sdk in sdks:
        cfg = get_config(sdk)
        print("=== [%s] -> %s" % (sdk, cfg["sdk_dir"]))
        copied, uptodate, stale, problems = sync_one(sdk, args.check)
        for p in problems:
            print("  [缺失] %s" % p)
            rc = 1
        if copied:
            verb = "待同步" if args.check else "已同步"
            print("  %s %d 个: %s" % (verb, len(copied),
                                       ", ".join(copied[:8])
                                       + (" ..." if len(copied) > 8 else "")))
        if stale:
            print("  [残留] 源已删除但目标还留着 %d 个: %s"
                  % (len(stale), ", ".join(stale[:8])))
            rc = 1
        print("  已是最新 %d 个" % len(uptodate))
        total = 0
        if os.path.isdir(cfg["sdk_dir"]):
            for dp, _dn, fns in os.walk(cfg["sdk_dir"]):
                for f in fns:
                    total += os.path.getsize(os.path.join(dp, f))
        print("  目标目录合计 %.1f MB" % (total / 1048576.0))
        print()

    if args.check and rc == 0:
        print("--check 通过：两个厂商的 SDK 副本均与源同步。")
    return rc


if __name__ == "__main__":
    sys.exit(main())
