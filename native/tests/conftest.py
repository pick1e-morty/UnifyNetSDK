# -*- coding: utf-8 -*-
"""pytest 公共装置（fixture）。

**这个目录测的是第 1 层（native 产出的 .pyd）**，不是 python/ 下的三个包。
各包自己的测试放在包内（python/dhbind/tests/ 等），由各自的 conftest 负责加载 ——
conftest.py 是**逐层生效**的，所以"测试跟着被测对象走"不需要任何 if 分支去判断
"当前测的是哪一层"。

三个可独立交付对象各自的 tests 位置见 TODO 0.2 的目录树；pytest.ini 的 testpaths
必须与那棵树保持一致。

原 `_paths.py` 的内容已并入本文件（2026-10-05，该文件已删）。路径推导仍是
**向上找锚点**，不要改成"从本文件往上数 N 层"：这份装置搬过家（tests/ ->
native/tests/），数层数漏一次就是"路径指向不存在的位置"这种钝错误，症状是 DLL
加载失败或 pyd import 失败，跟真因隔着好几层。

e2e 不在这层：连模拟器那类测试归 python 层（python/dhbind/tests/），本目录只测
绑定层（pyd）本身。
"""
import os
import sys

import pytest


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

#: sdk 名 -> (pyd 模块名, 源文件相对 native/build 的路径)
PYDS = {
    "dahua": ("unify_dh_gen", "unify_dh_gen.cp313-win_amd64.pyd"),
    "haikang": ("unify_hk_gen", "unify_hk_gen.cp313-win_amd64.pyd"),
}


def _add_sdk_dll_dirs(sdks=("dahua", "haikang")):
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
    for sdk in sdks:
        os.add_dll_directory(os.path.dirname(get_config(sdk)["dll"]))


def _import_pyd(modname):
    """import native/build 下的 pyd，并确保 native/build 在 sys.path 里。"""
    if BUILD not in sys.path:
        sys.path.insert(0, BUILD)
    return __import__(modname)


@pytest.fixture(scope="session")
def project_root():
    return PROJECT


@pytest.fixture(scope="session")
def codegen_dir():
    """native/codegen 的路径，并确保它在 sys.path 里（导入 config / check_coverage 用）。"""
    if CODEGEN not in sys.path:
        sys.path.insert(0, CODEGEN)
    return CODEGEN


@pytest.fixture(scope="session")
def pyd():
    """按需 import 某个厂商的 pyd 的工厂：``pyd("dahua")``。

    没编译好的厂商**自动 skip** 而不是让整个 suite 挂掉 —— 海康还在编译推进中
    （TODO 第 2 节），测试不该因为它一个人编不过就全线飘红。
    """
    _add_sdk_dll_dirs()          # dahua + haikang 都加，理由见其 docstring
    loaded = {}

    def _get(sdk):
        if sdk not in PYDS:
            raise ValueError("unknown sdk %r (known: %s)" % (sdk, ", ".join(PYDS)))
        if sdk in loaded:
            return loaded[sdk]
        modname, filename = PYDS[sdk]
        path = os.path.join(BUILD, filename)
        if not os.path.isfile(path):
            pytest.skip("%s 未编译：%s 不存在，先跑 build.ps1 -Sdk %s" % (sdk, path, sdk))
        loaded[sdk] = _import_pyd(modname)
        return loaded[sdk]

    return _get