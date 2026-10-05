# -*- coding: utf-8 -*-
"""把 pyd 与厂商 DLL 填进 dhbind/hkbind 的 _binding/（wheel 打包的前置步骤）。

对应 TODO 0.2 构建流程图的第 2 步：
    native/build/*.pyd + vendor/<厂商>/sdk_win64/bin/*.dll  ->  python/<包>/_binding/

用法：
    python tools/fill_binding.py --sdk dahua
    python tools/fill_binding.py --sdk haikang   （DLL 集合待真机验证，见下）

DLL 清单是**白名单**而不是整目录拷贝：vendor bin 里有几十个 MB 级 DLL
（play.dll / StreamConvertor.dll / RenderEngine.dll ...），登录链路用不到
它们，整拷会把 wheel 撑到无谓的体积。缺什么由 import/登录失败信息驱动补。
"""
import argparse
import os
import shutil
import sys

PROJECT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD = os.path.join(PROJECT, "native", "build")

# pyd（带 ABI 标签，按前缀在 native/build 里找）
PYDS = {
    "dahua": ["unify_dh_gen.cp313-win_amd64.pyd"],
    "haikang": ["unify_hk_gen.cp313-win_amd64.pyd"],
}

# 厂商运行库白名单（登录链路的最小集；缺了会在 import/登录时暴露，按报错补）
DLLS = {
    "dahua": ["dhnetsdk.dll", "libeay32.dll", "ssleay32.dll"],
    # 海康：HCNetSDK.dll 的依赖链（HCCore 等）尚未在无设备环境验证过，
    # 先不给名单——等真机/模拟器跑通登录后按实际依赖回填（testing-plan 选项 A/B）。
    "haikang": [],
}

PKG_DIRS = {
    "dahua": os.path.join(PROJECT, "python", "dhbind"),
    "haikang": os.path.join(PROJECT, "python", "hkbind"),
}


def fill(sdk):
    pyds = PYDS[sdk]
    dlls = DLLS[sdk]
    target = os.path.join(PKG_DIRS[sdk], "_binding")
    os.makedirs(target, exist_ok=True)

    copied = 0
    for f in pyds:
        src = os.path.join(BUILD, f)
        if not os.path.isfile(src):
            sys.exit("缺 pyd: %s（先跑 native/build.ps1）" % src)
        shutil.copy2(src, os.path.join(target, f))
        copied += 1
    for f in dlls:
        src = os.path.join(PROJECT, "vendor", sdk, "sdk_win64", "bin", f)
        if not os.path.isfile(src):
            sys.exit("缺 DLL: %s" % src)
        shutil.copy2(src, os.path.join(target, f))
        copied += 1
    print("[%s] %d 个文件 -> %s" % (sdk, copied, target))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--sdk", choices=["dahua", "haikang", "all"], default="dahua")
    args = ap.parse_args()
    for sdk in (["dahua", "haikang"] if args.sdk == "all" else [args.sdk]):
        if sdk == "haikang" and not DLLS["haikang"]:
            print("[haikang] 跳过：DLL 白名单未定（等海康登录在真机/模拟器上跑通，"
                  "见 docs/testing-plan.md），pyd 可先单独填充")
            fill_pyd_only = PYDS["haikang"]
            target = os.path.join(PKG_DIRS["haikang"], "_binding")
            os.makedirs(target, exist_ok=True)
            for f in fill_pyd_only:
                src = os.path.join(BUILD, f)
                if os.path.isfile(src):
                    shutil.copy2(src, os.path.join(target, f))
            continue
        fill(sdk)


if __name__ == "__main__":
    main()
