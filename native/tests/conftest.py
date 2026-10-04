# -*- coding: utf-8 -*-
"""pytest 公共装置（fixture）。

**这个目录测的是第 1 层（native 产出的 .pyd）**，不是 python/ 下的三个包。
各包自己的测试放在包内（python/dhbind/tests/ 等），由各自的 conftest 负责加载 ——
conftest.py 是**逐层生效**的，所以"测试跟着被测对象走"不需要任何 if 分支去判断
"当前测的是哪一层"。

三个可独立交付对象各自的 tests 位置见 TODO 0.2 的目录树；pytest.ini 的 testpaths
必须与那棵树保持一致。

## 现状：三个脚本还没转成 pytest

native/tests/ 下目前是三个**脚本**（test_callbacks.py / verify_runtime.py /
e2e/test_login_callback.py），它们不是 pytest 测试（没有 def test_*），pytest 收
不到东西，只会在 collection 阶段 import 它们从而执行副作用。转正计划见 TODO 1.3。

转换时要做的事：
  1. 把 _paths.py 的内容并入本文件的 fixture，然后删掉 _paths.py
  2. 三个脚本的顶层代码拆成 def test_*，脚本的 print+自建 fails 列表换成 assert
  3. e2e/test_login_callback.py 加 @pytest.mark.e2e（否则默认收集就会启动模拟器
     并阻塞 20 秒 —— pytest.ini 里已用 addopts 默认排除）
  4. verify_runtime.py 在 test_structs.py 落地后退役，详见该文件 docstring 顶部
"""
import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import _paths  # noqa: E402

#: sdk 名 -> (pyd 模块名, 源文件相对 native/build 的路径)
PYDS = {
    "dahua": ("unify_dh_gen", "unify_dh_gen.cp313-win_amd64.pyd"),
    "haikang": ("unify_hk_gen", "unify_hk_gen.cp313-win_amd64.pyd"),
}


@pytest.fixture(scope="session")
def pyd():
    """按需 import 某个厂商的 pyd 的工厂：``pyd("dahua")``。

    没编译好的厂商**自动 skip** 而不是让整个 suite 挂掉 —— 海康还在编译推进中
    （TODO 第 2 节），测试不该因为它一个人编不过就全线飘红。
    """
    _paths.add_sdk_dll_dirs()          # dahua + haikang 都加，理由见其 docstring
    loaded = {}

    def _get(sdk):
        if sdk not in PYDS:
            raise ValueError("unknown sdk %r (known: %s)" % (sdk, ", ".join(PYDS)))
        if sdk in loaded:
            return loaded[sdk]
        modname, filename = PYDS[sdk]
        path = os.path.join(_paths.BUILD, filename)
        if not os.path.isfile(path):
            pytest.skip("%s 未编译：%s 不存在，先跑 build.ps1 -Sdk %s" % (sdk, path, sdk))
        loaded[sdk] = _paths.import_pyd(modname)
        return loaded[sdk]

    return _get
