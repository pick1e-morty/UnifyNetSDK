# -*- coding: utf-8 -*-
"""Phase 1：把头文件 -> pyd 的覆盖边界钉成断言。

`native/codegen/check_coverage.py` 的打印是给人看的，运行一次看数字谁都会忘；
这里把**同一批数字**（同一个 `collect(sdk)`，不是重新解析一遍头文件）变成防线：
以后换 SDK 版本、改生成器、加厂商，漏了什么当场红，而不是靠人肉对照 README。

基线数字的含义：它们不是"目标"，是**当前实测值**，只允许往好的方向动 ——
漏绑只能减少，完全对上的只能增加。数字变差就说明这次改动真的丢了东西。

这些断言只解析头文件与生成物，不 import pyd，所以不需要 `pyd` fixture，
也不会被 SDK DLL 的加载问题牵连。
"""
import os
import re

import pytest

SDKS = ("dahua", "haikang")

#: 当前实测基线（2026-10-05）。见本文件顶部：只允许往好的方向变。
#: 字段总数/绑定数、跳过原因、回调参数分类的口径都来自 check_coverage.collect()。
BASELINE = {
    "dahua": {
        "enums": 1873,
        "structs": 10557,
        "funcs": 2521,
        "not_exported": 6,
        "callbacks": 289,
        "fields_total": 63353,
        "fields_bound": 63044,
        "skip_funcptr": 301,     # 结构体成员里的函数指针：缺口，只能减少
        "skip_bitfield": 8,      # C 语言限制，只能持平
        "skip_reserved": 0,
        "cb_params_total": 1146,
    },
    "haikang": {
        "enums": 264,
        "structs": 2668,
        "funcs": 789,
        "not_exported": 4,
        "callbacks": 26,
        "fields_total": 18792,
        "fields_bound": 18781,
        "skip_funcptr": 11,
        "skip_bitfield": 0,
        "skip_reserved": 0,
        "cb_params_total": 110,
    },
}


@pytest.fixture(scope="session")
def check_coverage(codegen_dir):
    """native/codegen/check_coverage.py 模块（目录由 conftest 的 codegen_dir 备好）。"""
    import check_coverage as mod
    return mod


@pytest.fixture(scope="session", params=SDKS)
def cov(request, check_coverage):
    """(sdk, collect(sdk)) —— session 级参数化，两个厂商各解析一次头文件。

    status quo 是 check_coverage.py 的打印口径，这里不另起炉灶：改口径要改
    check_coverage.collect()，两个消费方（人看的打印、机器看的断言）同时跟上。
    """
    sdk = request.param
    return sdk, check_coverage.collect(sdk)


def _generated_bind_count(out_dir):
    """生成物里注册了多少个 `bind_*`（回调订阅入口）。

    数的是生成源码而不是 pyd：pyd 可能还没编译，而"生成器漏了哪个回调"这件事
    在编译之前就该被发现。目录不存在返回 None（调用方决定 skip）。
    """
    if not os.path.isdir(out_dir):
        return None
    n = 0
    for name in sorted(os.listdir(out_dir)):
        if not name.endswith(".cpp"):
            continue
        with open(os.path.join(out_dir, name), encoding="utf-8", errors="replace") as f:
            n += len(re.findall(r'm\.attr\("bind_', f.read()))
    return n


def test_no_unknown_type_fields(cov):
    """未知类型字段必须是 0：它是"生成器没认出来的东西"，归零后不许再回来。"""
    sdk, c = cov
    assert c["skipped"]["unknown"] == 0, (
        "[%s] 出现 %d 个未知类型字段：%s\n"
        "这是生成器认不出的字段类型，说明 parse.py 需要补规则（不是可以放过的）"
        % (sdk, c["skipped"]["unknown"],
           ", ".join("%s x%d" % kv for kv in c["unknown_detail"]) or "(无明细)"))


def test_callback_count_matches(cov):
    """头文件里的回调 typedef 数 == 生成出来的 bind_* 数（大华 289、海康 26）。"""
    sdk, c = cov
    assert c["callbacks"] == BASELINE[sdk]["callbacks"], (
        "[%s] 头文件回调 typedef 从 %d 变成了 %d：SDK 换版本了？"
        "确认是有意变更后更新 BASELINE"
        % (sdk, BASELINE[sdk]["callbacks"], c["callbacks"]))

    n = _generated_bind_count(c["cfg"]["out_dir"])
    if n is None:
        pytest.skip("生成物不存在：%s（先跑 gen_bind.py --sdk %s）"
                    % (c["cfg"]["out_dir"], sdk))
    assert n == c["callbacks"], (
        "[%s] 头文件有 %d 个回调 typedef，生成物里只有 %d 个 bind_*："
        "生成器漏了 %d 个回调" % (sdk, c["callbacks"], n, c["callbacks"] - n))


def test_struct_field_total_not_shrinking(cov):
    """结构体/字段总量不许缩水：防某次改动一次漏绑一大批。"""
    sdk, c = cov
    b = BASELINE[sdk]
    assert c["structs"] >= b["structs"], (
        "[%s] 结构体从 %d 掉到 %d" % (sdk, b["structs"], c["structs"]))
    assert c["fields_total"] >= b["fields_total"], (
        "[%s] 字段总数从 %d 掉到 %d" % (sdk, b["fields_total"], c["fields_total"]))
    assert c["fields_bound"] >= b["fields_bound"], (
        "[%s] 绑定字段数从 %d 掉到 %d（新增的字段被跳过了？）"
        % (sdk, b["fields_bound"], c["fields_bound"]))
    assert c["enums"] >= b["enums"], (
        "[%s] 枚举从 %d 掉到 %d" % (sdk, b["enums"], c["enums"]))
    assert c["funcs"] >= b["funcs"], (
        "[%s] 函数从 %d 掉到 %d" % (sdk, b["funcs"], c["funcs"]))
    assert len(c["cfg"]["skip_funcs"]) == b["not_exported"], (
        "[%s] cfg['skip_funcs']（DLL 未导出的函数）从 %d 变成 %d："
        "check_exports.py 的结果要同步进来"
        % (sdk, b["not_exported"], len(c["cfg"]["skip_funcs"])))


def test_skipped_counts_stable(cov):
    """跳过的字段按原因分类守住：能变的只有"能变好"，不能变坏。"""
    sdk, c = cov
    b = BASELINE[sdk]
    s = c["skipped"]
    # 位字段是 C 语言限制（不能对位域取地址），nanobind 绑不了 —— 只能持平
    assert s["bitfield"] == b["skip_bitfield"], (
        "[%s] 位字段 %d -> %d：这个数只应持平，变大说明解析出错、变小说明有新办法了"
        % (sdk, b["skip_bitfield"], s["bitfield"]))
    # 结构体成员里的函数指针：目前完全未绑，是缺口，只能减少
    assert s["funcptr"] <= b["skip_funcptr"], (
        "[%s] 未绑的函数指针字段从 %d 涨到 %d" % (sdk, b["skip_funcptr"], s["funcptr"]))
    # 保留字命中说明 Python 侧命名撞了关键字，属于必须显式处理的异常
    assert s["reserved"] == 0, (
        "[%s] 出现 %d 个保留字字段" % (sdk, s["reserved"]))
    # 回调参数分类是"解耦是否到位"的体检：参数总数只应随回调数变化
    assert c["cb_params_total"] >= b["cb_params_total"], (
        "[%s] 回调参数总数从 %d 掉到 %d" % (sdk, b["cb_params_total"], c["cb_params_total"]))