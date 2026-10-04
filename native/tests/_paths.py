# -*- coding: utf-8 -*-
"""测试脚本的路径推导与 SDK 加载（被 test_callbacks / verify_runtime / e2e 复用）。

**不要改成"从本文件往上数 N 层"。** 这份文件及其使用者搬过两次家
（tests/ -> native/tests/ -> native/tests/e2e/），每次数层数都要跟着改，
漏一次就是"路径指向不存在的位置"这种钝错误：症状是 DLL 加载失败或 pyd
import 失败，跟真因隔着好几层。向上找锚点则只要项目根还在就永远对。

将来这三个脚本转成 pytest 后，本文件的内容会并入 conftest.py 的 fixture，
届时本文件即可删除。
"""
import os
import sys


def _find_project_root():
    d = os.path.dirname(os.path.abspath(__file__))
    while True:
        if os.path.isfile(os.path.join(d, "native", "CMakeLists.txt")):
            return d
        parent = os.path.dirname(d)
        if parent == d:                      # 已到盘符根仍未命中
            raise RuntimeError(
                "project root not found: no native/CMakeLists.txt above %s" % d)
        d = parent


PROJECT = _find_project_root()
BUILD = os.path.join(PROJECT, "native", "build")
CODEGEN = os.path.join(PROJECT, "native", "codegen")

# 模拟器在项目外面（与 UnifyNetSDK 同级），是独立 clone 的仓库
SIMULATOR = os.path.join(os.path.dirname(PROJECT), "Dahua_NVR_Simulator")


def add_sdk_dll_dirs(*sdks):
    """把指定厂商的 DLL 目录加进 DLL 搜索路径。**必须在 import 任意 pyd 之前
    把所有要用的厂商都加完**。

    Windows 上 import 一个 pyd 会连带解析它的依赖 DLL，而 add_dll_directory
    是进程级的、但只对**调用之后**的加载有效。先只加大华就 import 海康，会报
    DLL load failed（依赖链里缺 HCNetSDK.dll）。

    路径从 native/codegen/config/<sdk>.py 读，不硬编码：海康原始包的目录名是
    中文（"头文件"/"库文件"），硬编码路径等于埋雷。
    """
    if CODEGEN not in sys.path:
        sys.path.insert(0, CODEGEN)
    from config import get_config
    for sdk in (sdks or ("dahua", "haikang")):
        os.add_dll_directory(os.path.dirname(get_config(sdk)["dll"]))


def import_pyd(modname):
    """import native/build 下的 pyd，并确保 native/build 在 sys.path 里。"""
    if BUILD not in sys.path:
        sys.path.insert(0, BUILD)
    return __import__(modname)
