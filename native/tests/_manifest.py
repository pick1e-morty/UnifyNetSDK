# -*- coding: utf-8 -*-
"""生成物清单（`gen_manifest.json`）的读取器，Phase 2/3 测试共用。

清单由生成器产出（`native/codegen/common/emit.py` 的 `write_manifest`），是
「结构体 -> 字段列表」「函数表」的唯一权威来源：它和 pyd 出自同一次生成，测试期
再解析一遍 C 语法只会引入第二套口径（check_coverage 就因为没传 text_filters 而
量出过"并不存在的产物"）。

**不是 test_\*.py**：pytest 不收集，只当普通模块 import。放在 tests/ 下是因为它
只服务本层测试（e2e 归 python 层，见 TODO 1.0）。
"""
import functools
import json
import os

#: 有清单的厂商；新增厂商时这里与 pytest.ini / conftest 一起加。
SDKS = ("dahua", "haikang")


@functools.lru_cache(maxsize=None)
def project_root():
    """向上找锚点，别数层数：本目录搬过家（tests/ -> native/tests/），数层数
    漏一次就是"路径指向不存在的位置"这种钝错误。"""
    d = os.path.dirname(os.path.abspath(__file__))
    while True:
        if os.path.isfile(os.path.join(d, "native", "CMakeLists.txt")):
            return d
        parent = os.path.dirname(d)
        if parent == d:
            raise RuntimeError("project root not found above %s" % d)
        d = parent


@functools.lru_cache(maxsize=None)
def load(sdk):
    """读 `native/src/gen_*/gen_manifest.json`，按清单自带的 `sdk` 字段认领。

    不拿 config 推 out_dir：清单自带 `sdk`，扫一遍 src/ 就能对上，少一处硬编码。
    找不到返回 None（调用方决定 skip —— 生成物不入库，没生成过就没有）。

    lru_cache 是必需的：逐项参数化会调上万次，1.4 MB 的 JSON 每次重读会拖垮 collection。
    """
    src = os.path.join(project_root(), "native", "src")
    if not os.path.isdir(src):
        return None
    for entry in sorted(os.listdir(src)):
        path = os.path.join(src, entry, "gen_manifest.json")
        if not os.path.isfile(path):
            continue
        with open(path, encoding="ascii") as f:
            data = json.load(f)
        if data.get("sdk") == sdk:
            return data
    return None