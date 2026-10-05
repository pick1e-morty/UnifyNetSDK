# -*- coding: utf-8 -*-
"""两个厂商 .pyd 的运行时读写验证。

编译通过 + import 成功只证明类型注册没崩。真正会出错的是：
  - 字段偏移算错（结构体布局不对）-> 读写拿到错乱的值
  - char[N] 当 str 处理但字段被填满无 NUL 结尾
  - 数组维度算错
  - 枚举值不对
所以这里做**写进去再读回来**的往返测试，值对不上就说明绑定有问题。

（原名 verify_runtime.py，2026-10-05 转成 pytest 测试时改名：pytest 只收集
test_*.py，叫原名等于永远不被收集。）

========================================================================
【退役约定 —— Phase 2 落地后必须删掉本文件，不要忘】

本文件是 TODO 1.2 Phase 2 的**手工预演版**：只覆盖 3-6 个结构体，而 Phase 2
要求逐个跑完全部 10557 个（TODO 里的 native/tests/test_structs.py）。

触发退役的条件：**native/tests/test_structs.py 落地并跑通**。届时本文件的价值
已全部转移：
  - 两个厂商的 DLL 目录都要先 add 再 import 任意 pyd -> conftest.py 的 `pyd` fixture
  - 结构体字段往返 -> test_structs.py 的 test_struct_roundtrip

在那之前**不要删**：本文件是目前唯一能同时验证两个厂商 .pyd 可 import + 字段可
读写的跨厂商回归工具。删早了就没有替代品了。
========================================================================
"""
import pytest


def _roundtrip(obj, fields):
    """fields: [(字段名, 写入值, 期望读回)] —— 写进去再读回来。"""
    for fname, wval, _ in fields:
        setattr(obj, fname, wval)
    for fname, wval, rval in fields:
        got = getattr(obj, fname)
        ok = abs(got - rval) < 1e-6 if isinstance(got, float) else got == rval
        assert ok, "%s.%s 往返失败：写入 %r 读回 %r" % (
            type(obj).__name__, fname, wval, got)


def test_dahua_scalar_roundtrip(pyd):
    g = pyd("dahua")
    _roundtrip(g.NET_DEVICEINFO(), [
        ("byChanNum", 16, 16),
        ("byDVRType", 0, 0),
        ("byDiskNum", 4, 4),
    ])


def test_dahua_byte_array_is_bytes(pyd):
    """BYTE[N] 应是 bytes（序列号本就是字节数组，不是 str）。"""
    g = pyd("dahua")
    obj = g.NET_DEVICEINFO()
    obj.sSerialNumber = b"SN-abc-123"
    assert bytes(obj.sSerialNumber).rstrip(b"\x00") == b"SN-abc-123", \
        repr(bytes(obj.sSerialNumber)[:16])


def test_dahua_char_array_is_str(pyd):
    """char[N] 应自动走 str 通道。

    NET_DEVICEINFO 本身**没有** char[N] 字段（只有 BYTE[48] 的 sSerialNumber，那是
    bytes 通道），所以探针落在真有 char[N] 的结构体上。
    """
    g = pyd("dahua")

    def find_str_field(obj):
        """探针：把每个公开字段依次写成 str，第一个不抛的就是 str 通道字段。"""
        for attr in dir(obj):
            if attr.startswith("_"):
                continue
            try:
                setattr(obj, attr, "probe")
            except Exception:
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


def test_dahua_enums_and_safe_functions(pyd):
    """枚举已注册；不依赖设备的函数可调用。

    枚举名用确实存在的：原脚本只 print 了 NET_DEVICE_STATE / EM_LOGIN_ERROR 的
    存在性（都没进 fails），而这两个名字在当前头文件里并不存在，照抄就是恒假断言。
    """
    g = pyd("dahua")
    for en in ("NET_DEVICE_TYPE", "EM_LOGIN_SPAC_CAP_TYPE"):
        assert hasattr(g, en), "枚举 %s 不存在" % en
    for fn in ("CLIENT_GetSDKVersion", "CLIENT_GetLastError"):
        assert hasattr(g, fn), "函数 %s 不存在" % fn
        getattr(g, fn)()          # 只要不抛就算过


def test_haikang_time_roundtrip(pyd):
    h = pyd("haikang")
    _roundtrip(h.NET_DVR_TIME(), [
        ("dwYear", 2026, 2026), ("dwMonth", 10, 10), ("dwDay", 4, 4),
        ("dwHour", 23, 23), ("dwMinute", 59, 59), ("dwSecond", 58, 58),
    ])


def test_haikang_safe_functions(pyd):
    h = pyd("haikang")
    for fn in ("NET_DVR_GetSDKVersion", "NET_DVR_GetLastError"):
        assert hasattr(h, fn), "函数 %s 不存在" % fn
        getattr(h, fn)()