# -*- coding: utf-8 -*-
"""端到端：用**生成版** unify_dh_gen 登录模拟器，验证回调在真实 SDK 线程上触发。

这是 --emit-selftest 的替代验证：selftest 只能证明"从裸 std::thread 调 thunk"
不崩，而这里证明的是真实链路 —— SDK 自己的工作线程 -> thunk -> GIL -> Python。

覆盖：
  1. bind_fDisConnect 返回的地址能直接喂给 CLIENT_Init
  2. Gen2 登录成功（nError == 0）
  3. server 断开时，绑定层注册的回调真的被调用，且参数正确
"""
import io
import os
import subprocess
import sys
import time

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

UNIFY = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SIM = os.path.join(os.path.dirname(UNIFY), "Dahua_NVR_Simulator")

server_script = r'''
import sys, time
sys.path.insert(0, r"%s\\src")
from config import DeviceConfig
from dahua_netsdk import DahuaNetSDKServer
cfg = DeviceConfig()
cfg.ip = "127.0.0.1"
cfg.dahua_port = 37778
cfg.username = "admin"
cfg.password = "admin123"
cfg.set_channel_count(3)
srv = DahuaNetSDKServer(lambda: cfg, log_cb=lambda s, level="INFO": print("  [srv]", s, flush=True))
srv.start()
time.sleep(3)
print("[srv] 主动断开所有连接...", flush=True)
srv.stop()
time.sleep(3)
''' % SIM

proc = subprocess.Popen([sys.executable, "-c", server_script])
time.sleep(1.5)

os.add_dll_directory(os.path.join(UNIFY, "dahua", "C_Win64", "Bin"))
sys.path.insert(0, os.path.join(UNIFY, "native", "build"))
import unify_dh_gen as g  # noqa: E402

_t0 = time.time()
fails = []


def mark(m):
    print("[%6.2fs] %s" % (time.time() - _t0, m), flush=True)


def check(label, got, want):
    ok = got == want
    print("  [%s] %-24s got=%r want=%r" % ("OK" if ok else "FAIL", label, got, want))
    if not ok:
        fails.append(label)


# ---- 1. 订阅断线回调 ----
DISCONNECTED = []


def on_disconnect(login_id, ip, port, user):
    print(">>> [回调] 断线触发! loginID=%d ip=%r port=%d user=%d"
          % (login_id, ip, port, user), flush=True)
    DISCONNECTED.append((login_id, ip, port, user))


mark("bind_fDisConnect")
cb_ptr = g.bind_fDisConnect(on_disconnect)
mark("cb_ptr = %#x" % cb_ptr)
check("cb_ptr non-zero", cb_ptr != 0, True)

# ---- 2. 初始化 + 登录 ----
mark("CLIENT_Init")
g.CLIENT_Init(cb_ptr, 0x1234)
g.CLIENT_SetConnectTime(5000, 3)

mark("登录中...")
in_param = g.NET_IN_LOGIN_WITH_HIGHLEVEL_SECURITY()
in_param.szIP = "127.0.0.1"
in_param.nPort = 37778
in_param.szUserName = "admin"
in_param.szPassword = "admin123"
out = g.NET_OUT_LOGIN_WITH_HIGHLEVEL_SECURITY()
handle = g.CLIENT_LoginWithHighLevelSecurity(in_param, out)
mark("登录返回 handle=%s nError=%d" % (handle, out.nError))
check("login nError", out.nError, 0)
check("login handle", handle != 0, True)

# ---- 3. 等 server 主动断开，回调应触发 ----
mark("等断线回调...")
deadline = time.time() + 20
while not DISCONNECTED and time.time() < deadline:
    time.sleep(0.3)

check("回调触发次数", len(DISCONNECTED), 1)
if DISCONNECTED:
    lid, ip, port, user = DISCONNECTED[0]
    check("callback loginID", lid, handle)
    check("callback ip", ip, "127.0.0.1")
    check("callback port", port, 37778)
    check("callback user", user, 0x1234)

g.CLIENT_Logout(handle)
g.CLIENT_Cleanup()
# 显式释放：否则 nanobind 会对未回收的 nb::class_ 实例/类型报 leaked，
# 在 stderr 里留一堆噪音，掩盖真正的错误。
del in_param, out
mark("cleanup done")

try:
    proc.wait(timeout=10)
except subprocess.TimeoutExpired:
    proc.kill()

print()
print("RESULT:", "ALL PASS" if not fails else "FAILED: %s" % fails)
