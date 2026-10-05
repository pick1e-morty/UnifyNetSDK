# -*- coding: utf-8 -*-
"""Phase 2：逐个结构体冒烟（TODO 1.2 Phase 2）。

覆盖大华 10557 + 海康 2668 个结构体，**不抽样** —— nanobind 的 `def_rw` 是模板
胶水，一个能跑不代表另一个能跑（未知类型归零那次就一下找出 6 个漏网的指针别名）。

每个结构体做三件事：

1. 类存在且能构造（`cls()` 不抛）；
2. 带 `dwSize` 的，`__init__` 已按 `sizeof` 填好，且与 `baseline_sizes.json` 的
   golden 值一致（换 SDK 后布局变了当场红，不必等接设备才发现）；
3. 每个字段「读 -> 原样写回 -> 再读」往返一致。这条对 `str` / `bytes` / 指针 /
   数组 / 内嵌结构体 / 枚举全都成立，所以测试不必按类型分支。

**数据源是生成器的 `gen_manifest.json`**（名字 -> 字段列表），不是头文件：manifest
与 pyd 出自同一次生成，测试期再解析一遍 C 语法只会引入第二套口径。manifest 或 pyd
缺失都 skip（生成物不入库）。

**已知读不出来的字段**记在 `baseline_sizes.json` 的 `unreadable` 里，只减不增：

- memset 归零后读枚举，`0` 不是合法枚举项（nanobind 的固有行为，不是绑定缺陷）；
- `_DHDEVTIME` 之类类型未注册（真实缺口，见 docs/binding-tech-debt.md）。

新出现的读失败当场红；数量只降不升。基线文件缺失时全量扫一遍重新生成
（首次落地 / 换 SDK 后刷新基线，见 docs/testing-plan.md 已定决策 2）。
"""
import json
import os
import warnings

import pytest

from _manifest import SDKS, load as load_manifest, project_root

#: committed golden：结构体 `dwSize` 实测值 + 已知不可读字段清单。
BASELINE_NAME = "baseline_sizes.json"


def pytest_generate_tests(metafunc):
    """把 (sdk, 结构体名) 展开成逐项测试；清单缺失的厂商给个哨兵项去 skip。

    清单在 collection 期就要读，拿不到 fixture，所以走本 hook 而不是
    `@pytest.mark.parametrize`。
    """
    if "sdk" not in metafunc.fixturenames or "struct_name" not in metafunc.fixturenames:
        return
    cases, ids = [], []
    for sdk in SDKS:
        data = load_manifest(sdk)
        if data is None:
            cases.append((sdk, None))
            ids.append("%s-<清单缺失>" % sdk)
            continue
        for name in sorted(data["structs"]):
            cases.append((sdk, name))
            ids.append("%s-%s" % (sdk, name))
    metafunc.parametrize("sdk,struct_name", cases, ids=ids)


def _probe(cls, fields):
    """构造一个结构体，逐字段做往返。返回 `(dwSize|None, [(字段, 异常)], [(字段, 说明)])`。

    刻意不 assert：调用方各自决定怎么处理 —— 生成基线时"读不出来"是**要记录的数据**，
    测试期它才是失败。
    """
    obj = cls()                       # 构造失败直接抛：那是真 bug，不该被吞
    size = obj.dwSize if "dwSize" in fields else None
    unreadable, bad = [], []
    for f in fields:
        try:
            v = getattr(obj, f)
        except Exception as exc:      # 枚举 0 非法 / 类型未注册 —— 读这一步就失败
            unreadable.append((f, exc))
            continue
        try:
            setattr(obj, f, v)
            got = getattr(obj, f)
        except Exception as exc:      # noqa: BLE001
            bad.append((f, exc))
            continue
        if got != v:
            bad.append((f, "往返不一致：写回 %r 读回 %r" % (v, got)))
    return size, unreadable, bad


def _scan(g, structs):
    """全量扫一遍，产出基线的那两个字段（sizes / unreadable）。"""
    sizes, unreadable = {}, []
    for name, fields in structs.items():
        size, unreadable_fields, bad = _probe(getattr(g, name), fields)
        assert not bad, "%s 往返失败：%r" % (name, bad)     # 生成基线时不该有往返失败
        if size is not None:
            sizes[name] = size
        unreadable.extend("%s.%s" % (name, f) for f, _ in unreadable_fields)
    return {"sizes": sizes, "unreadable": sorted(unreadable)}


@pytest.fixture(scope="session")
def baseline(pyd):
    """committed golden 的加载器；文件缺失时全量扫一遍生成，并提醒复核后提交。"""
    path = os.path.join(project_root(), "native", "tests", BASELINE_NAME)
    if os.path.isfile(path):
        with open(path, encoding="ascii") as f:
            return json.load(f)

    data = {}
    for sdk in SDKS:
        man = load_manifest(sdk)
        if man is not None:
            data[sdk] = _scan(pyd(sdk), man["structs"])
    with open(path, "w", encoding="ascii", newline="\n") as f:
        json.dump(data, f, indent=1, sort_keys=True)
    warnings.warn(
        "%s 不存在，已按当前 pyd 全量扫描生成（%s）。复核后提交进库 —— "
        "其中的 dwSize 与 unreadable 是 Phase 2 的 golden 基线。"
        % (path, ", ".join("%s %d 结构体" % (s, len(d["sizes"])) for s, d in data.items())))
    return data


def test_struct_smoke(pyd, sdk, struct_name, baseline):
    """构造 -> dwSize -> 逐字段往返。见模块 docstring。"""
    if struct_name is None:
        pytest.skip("gen_manifest.json 缺失：先跑 `python native/codegen/gen_bind.py --sdk %s`"
                    % sdk)
    fields = load_manifest(sdk)["structs"][struct_name]
    g = pyd(sdk)

    size, unreadable, bad = _probe(getattr(g, struct_name), fields)

    assert not bad, "[%s] %s 字段往返失败：\n%s" % (
        sdk, struct_name, "\n".join("  .%s：%r" % (f, e) for f, e in bad))

    known = set(baseline[sdk]["unreadable"])
    fresh = [f for f, _ in unreadable if "%s.%s" % (struct_name, f) not in known]
    assert not fresh, (
        "[%s] %s 出现新的读不出来的字段：%s\n"
        "若确属「memset 归零后读枚举」「类型未注册」这类已知类别，确认后写进 "
        "baseline_sizes.json 的 unreadable；否则是绑定回归。"
        % (sdk, struct_name, ", ".join(fresh)))

    if size is not None:
        assert size > 0, "[%s] %s.dwSize == 0：__init__ 没填 sizeof" % (sdk, struct_name)
        exp = baseline[sdk]["sizes"].get(struct_name)
        assert exp is not None, (
            "[%s] %s 有 dwSize 但不在 baseline_sizes.json：基线过期了，"
            "删掉该文件重跑以重新生成" % (sdk, struct_name))
        assert size == exp, (
            "[%s] %s.dwSize %d != 基线 %d：结构体布局变了（换过 SDK？）"
            % (sdk, struct_name, size, exp))


# --------------------------------------------------------------------------
# 类型通道：这些是「字段以什么 Python 类型暴露」的显式断言。逐项往返测不出通道
# 差异（str 与 bytes 都能自往返），所以单独钉住 —— 承接原 test_runtime_roundtrip.py。
# --------------------------------------------------------------------------

def test_dahua_byte_array_is_bytes(pyd):
    """`BYTE[N]` 应是 bytes（序列号本就是字节数组，不是 str）。"""
    g = pyd("dahua")
    obj = g.NET_DEVICEINFO()
    obj.sSerialNumber = b"SN-abc-123"
    assert bytes(obj.sSerialNumber).rstrip(b"\x00") == b"SN-abc-123", \
        repr(bytes(obj.sSerialNumber)[:16])


def test_dahua_char_array_is_str(pyd):
    """`char[N]` 应自动走 str 通道。

    NET_DEVICEINFO 只有 `BYTE[48]` 的 sSerialNumber（那是 bytes 通道），所以探针
    落在真有 `char[N]` 的结构体上：把每个公开字段依次写成 str，第一个不抛的就是。
    """
    g = pyd("dahua")

    def find_str_field(obj):
        for attr in dir(obj):
            if attr.startswith("_"):
                continue
            try:
                setattr(obj, attr, "probe")
            except Exception:         # noqa: BLE001
                continue
            return attr
        return None

    for sname in ("NET_IN_LOGIN_WITH_HIGHLEVEL_SECURITY", "NET_LOG_INFO"):
        fname = find_str_field(getattr(g, sname)())
        if not fname:
            continue
        obj = getattr(g, sname)()
        setattr(obj, fname, "hello")
        assert getattr(obj, fname) == "hello", "%s.%s 不是 str 往返" % (sname, fname)
        return
    pytest.fail("NET_IN_LOGIN_WITH_HIGHLEVEL_SECURITY / NET_LOG_INFO 都没有 str 通道字段")


@pytest.mark.parametrize("sdk,enum_name", [
    ("dahua", "NET_DEVICE_TYPE"),
    ("dahua", "EM_LOGIN_SPAC_CAP_TYPE"),
    ("haikang", "GET_STREAM_TYPE"),
    ("haikang", "VIDEO_STANDARD"),
])
def test_enums_registered(pyd, sdk, enum_name):
    """枚举类型确实注册进了模块（逐项结构体冒烟只覆盖结构体，不覆盖枚举）。"""
    import enum

    mod = pyd(sdk)
    obj = getattr(mod, enum_name, None)
    assert isinstance(obj, type) and issubclass(obj, enum.IntEnum), \
        "[%s] 枚举 %s 未按 IntEnum 注册：%r" % (sdk, enum_name, obj)