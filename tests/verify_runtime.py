# -*- coding: utf-8 -*-
"""两个厂商 .pyd 的运行时读写验证。

编译通过 + import 成功只证明类型注册没崩。真正会出错的是：
  - 字段偏移算错（结构体布局不对）-> 读写拿到错乱的值
  - char[N] 当 str 处理但字段被填满无 NUL 结尾
  - 数组维度算错
  - 枚举值不对
所以这里做**写进去再读回来**的往返测试，值对不上就说明绑定有问题。

DLL 目录从 tools/config/<sdk>.py 读（不硬编码中文路径），加载方式照抄
native/smoke_test.py：os.add_dll_directory + sys.path.insert。
"""
import io
import os
import sys

ROOT = r"C:\Users\Hast\Documents\CodeProjects\UnifyNetSDK"
BUILD = os.path.join(ROOT, "native", "build")
sys.path.insert(0, os.path.join(ROOT, "tools"))
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

from config import get_config

fails = []

# 两个厂商的 DLL 目录**都要先 add**，再 import 任意一个：
# Windows 上 import 一个 pyd 会连带解析它的依赖 DLL，而 add_dll_directory
# 是进程级的、但只对**调用之后**的加载有效。先只 add 大华再去 import 海康，
# 会报 "DLL load failed: 找不到指定的模块"（依赖链里缺 HCNetSDK.dll）。
for _sdk in ("dahua", "haikang"):
    os.add_dll_directory(os.path.dirname(get_config(_sdk)["dll"]))
sys.path.insert(0, BUILD)


def ck(label, cond, extra=""):
    print("  [%s] %s%s" % ("OK  " if cond else "FAIL", label,
                           ("  " + extra) if extra else ""))
    if not cond:
        fails.append(label)


def load(sdk, modname):
    return __import__(modname)


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
        G = load(sdk, modname)
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
