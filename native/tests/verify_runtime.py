# -*- coding: utf-8 -*-
"""两个厂商 .pyd 的运行时读写验证。

编译通过 + import 成功只证明类型注册没崩。真正会出错的是：
  - 字段偏移算错（结构体布局不对）-> 读写拿到错乱的值
  - char[N] 当 str 处理但字段被填满无 NUL 结尾
  - 数组维度算错
  - 枚举值不对
所以这里做**写进去再读回来**的往返测试，值对不上就说明绑定有问题。

========================================================================
【退役约定 —— Phase 2 落地后必须删掉本文件，不要忘】

本文件是 TODO 1.2 Phase 2 的**手工预演版**：只覆盖 3-6 个结构体，而 Phase 2
要求逐个跑完全部 10557 个（TODO 里的 native/tests/test_structs.py）。

触发退役的条件：**native/tests/test_structs.py 落地并跑通**。届时本文件的
全部价值都已转移：
  - 两个厂商的 DLL 目录都要先 add 再 import 任意 pyd
    -> _paths.add_sdk_dll_dirs（转 pytest 后进 conftest.py 的 fixture）
  - 结构体字段往返 -> test_structs.py 的 test_struct_roundtrip

在那之前**不要删**：海康 pyd 还没编译通过（TODO 第 2 节），本文件是目前唯一
能同时验证两个厂商 .pyd 可 import + 字段可读写的跨厂商回归工具。删早了就没有
替代品了。

退役动作：删本文件；若届时 _paths.py 已无其他使用者，一并删掉。
========================================================================
"""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

import _paths  # noqa: E402

ROOT = _paths.PROJECT
BUILD = _paths.BUILD

fails = []

# 两个厂商的 DLL 目录都要先 add 再 import 任意一个 pyd，原因见
# _paths.add_sdk_dll_dirs 的 docstring。
_paths.add_sdk_dll_dirs()


def ck(label, cond, extra=""):
    print("  [%s] %s%s" % ("OK  " if cond else "FAIL", label,
                           ("  " + extra) if extra else ""))
    if not cond:
        fails.append(label)


def roundtrip(G, sname, fields):
    """fields: [(字段名, 写入值, 期望读回)] —— 写进去再读回来。"""
    obj = getattr(G, sname)()
    for fname, wval, _ in fields:
        setattr(obj, fname, wval)
    for fname, wval, rval in fields:
        got = getattr(obj, fname)
        ok = abs(got - rval) < 1e-6 if isinstance(got, float) else got == rval
        ck("%s.%s 往返" % (sname, fname), ok,
           "写入=%r 读回=%r" % (wval, got))
    return obj


def survey(G, modname, sdk):
    print("=" * 68)
    print("[%s] %s" % (sdk, modname))
    print("=" * 68)
    pyd = os.path.join(BUILD, modname + ".cp313-win_amd64.pyd")
    ck("pyd 存在", os.path.isfile(pyd),
       "%.1f MB" % (os.path.getsize(pyd) / 1048576.0))
    try:
        G = _paths.import_pyd(modname)
    except Exception as e:
        ck("import", False, "%s: %s" % (type(e).__name__, e))
        return None
    ck("import", True, (G.__doc__ or "")[:44])
    names = dir(G)
    cb3 = [n for n in names if n.startswith(("set_", "bind_", "unbind_"))]
    # SDK 函数名全是全大写（CLIENT_xxx / NET_DVR_xxx），不能按首字母大小写分类
    upper = sum(1 for n in names if n.isupper() or (n[:1].isupper() and n.isupper()))
    print("  导出 %d 个：全大写符号 %d / 回调三件套 %d (= %d 个回调)"
          % (len(names), upper, len(cb3), len(cb3) // 3))
    return G


# ---------------- 大华 ----------------
G = survey("dahua", "unify_dh_gen", "dahua")
if G:
    print()
    print("--- 结构体读写往返（标量字段）---")
    roundtrip(G, "NET_DEVICEINFO", [
        ("byChanNum", 16, 16),
        ("byDVRType", 0, 0),
        ("byDiskNum", 4, 4),
    ])
    print()
    print("--- BYTE[N] 应是 bytes（序列号本就是字节数组，不是 str）---")
    _o = G.NET_DEVICEINFO()
    _o.sSerialNumber = b"SN-abc-123"
    ck("NET_DEVICEINFO.sSerialNumber bytes 往返",
       bytes(_o.sSerialNumber).rstrip(b"\x00") == b"SN-abc-123",
       repr(bytes(_o.sSerialNumber)[:16]))
    print()
    print("--- char[N] 应自动走 str 通道 ---")

    def _find_str_field(obj):
        for _a in dir(obj):
            if _a.startswith("_"):
                continue
            try:
                setattr(obj, _a, "probe")
            except Exception:
                continue
            return _a
        return None

    _fs = _find_str_field(G.NET_DEVICEINFO())
    print("  NET_DEVICEINFO 里绑定成 str 的字段: %s" % (_fs or "(无)"))
    if _fs:
        roundtrip(G, "NET_DEVICEINFO", [(_fs, "hello", "hello")])
    print()
    print("--- 枚举 ---")
    for en in ("NET_DEVICE_STATE", "EM_LOGIN_ERROR"):
        print("  %-22s 存在=%s" % (en, hasattr(G, en)))
    print()
    print("--- 不依赖设备的安全函数 ---")
    for fn in ("CLIENT_GetSDKVersion", "CLIENT_GetLastError"):
        if not hasattr(G, fn):
            ck("%s() 存在" % fn, False)
            continue
        try:
            ck("%s()" % fn, True, "返回 %r" % (getattr(G, fn)(),))
        except Exception as e:
            ck("%s()" % fn, False, "%s: %s" % (type(e).__name__, e))
    print()

# ---------------- 海康 ----------------
H = survey("haikang", "unify_hk_gen", "haikang")
if H:
    print()
    print("--- 结构体读写往返（真实字段：NET_DVR_TIME.dwYear 等）---")
    roundtrip(H, "NET_DVR_TIME", [
        ("dwYear", 2026, 2026), ("dwMonth", 10, 10), ("dwDay", 4, 4),
        ("dwHour", 23, 23), ("dwMinute", 59, 59), ("dwSecond", 58, 58),
    ])
    print()
    print("--- 不依赖设备的安全函数 ---")
    for fn in ("NET_DVR_GetSDKVersion", "NET_DVR_GetLastError"):
        if not hasattr(H, fn):
            ck("%s() 存在" % fn, False)
            continue
        try:
            ck("%s()" % fn, True, "返回 %r" % (getattr(H, fn)(),))
        except Exception as e:
            ck("%s()" % fn, False, "%s: %s" % (type(e).__name__, e))
    print()

print("=" * 68)
print("失败 %d 项" % len(fails))
for f in fails:
    print("   - %s" % f)
