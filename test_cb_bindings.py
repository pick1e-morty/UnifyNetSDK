# -*- coding: utf-8 -*-
"""端到端验证 unify_dh_gen 的回调绑定（走自测钩子，真 C++ 线程）。

为什么不用 ctypes 调 thunk：ctypes 的 CFUNCTYPE 回调会自己 swap 一个 thread
state 进去，判据"当前线程是否已附着"在那种线程上恒为假（PyThreadState_
GetUnchecked() 读不到它），于是绑定会二次 attach 而 Fatal。真实 SDK 工作线程
不是那种情形，所以验证必须用生成出来的 _selftest_fXxx 钩子——它从裸
std::thread 调用 thunk，复现真实路径。

覆盖：
  1. 289 个 bind_/set_ 是否齐全
  2. bytes 分类：BYTE* + 长度 -> bytes
  3. obj 分类：结构体指针 -> 借用视图，且 dwUser 不被误判成数量
  4. array 分类：结构体指针 + 元素个数 -> list
  5. 退订、异常隔离
  6. 遍历全部 289 个自测钩子，确认没有一个会崩或抛未捕获异常
"""
import io
import os
import sys
import traceback

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

ROOT = r"C:\Users\Hast\Documents\CodeProjects\UnifyNetSDK"
os.add_dll_directory(os.path.join(ROOT, "dahua", "C_Win64", "Bin"))
sys.path.insert(0, os.path.join(ROOT, "native", "build"))

import unify_dh_gen as G

# 进度打点：native 线程/GIL 相关调用可能卡死或崩，必须能在日志里看到
# 停在哪一个 _selftest_ 之前（flush=True 是关键，否则卡住时缓冲区里啥都没有）。
import time

_t0 = time.time()


def mark(msg):
    print("[%7.3fs] %s" % (time.time() - _t0, msg), flush=True)


mark("module imported")

print("unify_dh_gen loaded")
binds = [n for n in dir(G) if n.startswith("bind_")]
setters = [n for n in dir(G) if n.startswith("set_")]
selftests = [n for n in dir(G) if n.startswith("_selftest_")]
print("  bind_* %d / set_* %d / _selftest_* %d" % (len(binds), len(setters), len(selftests)))
print()

fails = []


def check(label, got, want):
    ok = got == want
    print("  [%s] %-26s got=%r want=%r" % ("OK" if ok else "FAIL", label, got, want))
    if not ok:
        fails.append(label)


# ---- 1. bytes: fDataCallBack(LLONG, DWORD, BYTE*, DWORD, LDWORD) ----
print("=== bytes: fDataCallBack (真 C++ 线程) ===")
seen = []
G.bind_fDataCallBack(lambda h, dt, buf, sz, user: seen.append((h, dt, buf, sz, user)))
mark("calling _selftest_fDataCallBack")
# b"x" = 走完整 thunk；b"" 只做 Stage 1（线程+GIL 往返），用于二分定位
G._selftest_fDataCallBack(b"x")
mark("returned from _selftest_fDataCallBack")
check("call count", len(seen), 1)
if seen:
    check("handle", seen[0][0], 0x1234)
    check("buffer", seen[0][2], b"\x01\x02\x03\x04")
    check("bufsize", seen[0][3], 4)
print()

# ---- 2. obj: dwUser 不能被当成数量 ----
# 借用视图只在回调期间有效，所以按真实用法在回调里取走类型/字段，不留引用
# （留着会让 nanobind 在退出时报 leaked instance）。
print("=== obj: fVideoAnalyseState (dwUser 不应被当成数量) ===")
seen2 = []
G.bind_fVideoAnalyseState(
    lambda *a: seen2.append((type(a[1]).__name__, len(a), a[-2])))
G._selftest_fVideoAnalyseState(b"x")
check("call count", len(seen2), 1)
if seen2:
    name, nargs, dwuser = seen2[0]
    check("arg1 type", name, "NET_VIDEOANALYSE_STATE")
    check("arg count", nargs, 4)
    check("dwUser passthrough", dwuser, 0x1234)
print()

# ---- 3. array: 结构体指针 + 元素个数 -> list ----
print("=== array: fNotifyCarPassInfo ===")
seen3 = []
G.bind_fNotifyCarPassInfo(
    lambda *a: seen3.append((isinstance(a[1], list), len(a[1]),
                              type(a[1][0]).__name__)))
G._selftest_fNotifyCarPassInfo(b"x")
check("call count", len(seen3), 1)
if seen3:
    is_list, n, elem = seen3[0]
    check("is list", is_list, True)
    check("list len", n, 2)
    check("elem type", elem, "NET_CAR_PASS_INFO")
print()

# ---- 4. array: 指针别名写法（LPNET_XXX）也要成数组 ----
print("=== array via pointer alias: fQueryRecordFileCallBack ===")
seen4 = []
G.bind_fQueryRecordFileCallBack(
    lambda *a: seen4.append((isinstance(a[1], list), type(a[1][0]).__name__)))
G._selftest_fQueryRecordFileCallBack(b"x")
check("call count", len(seen4), 1)
if seen4:
    is_list, elem = seen4[0]
    check("is list", is_list, True)
    check("elem type", elem, "NET_RECORDFILE_INFO")
print()

# ---- 5. 退订 + 异常隔离 ----
print("=== unsubscribe / exception isolation ===")
G.unbind_fDataCallBack()
G._selftest_fDataCallBack(b"x")
check("no call after unsubscribe", len(seen), 1)


def boom(*a):
    raise ValueError("intentional test error")


G.bind_fDataCallBack(boom)
G._selftest_fDataCallBack(b"x")
print("  survived user exception, no crash")
print()

# ---- 6. 遍历全部自测钩子 ----
print("=== sweep all %d selftest hooks ===" % len(selftests))
crashed = []
for idx, n in enumerate(sorted(selftests)):
    mark("selftest %d/%d: %s" % (idx + 1, len(selftests), n))
    fn = getattr(G, n)
    try:
        fn(b"x")
    except Exception:
        crashed.append((n, traceback.format_exc(limit=1).strip().splitlines()[-1]))
mark("sweep done")
print("  hooks run     : %d" % len(selftests))
print("  raised/crashed: %d" % len(crashed))
for n, err in crashed[:10]:
    print("    %-46s %s" % (n, err))
if crashed:
    fails.append("selftest sweep")

print()
print("RESULT:", "ALL PASS" if not fails else "FAILED: %s" % fails)
