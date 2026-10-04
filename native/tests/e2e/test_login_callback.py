# -*- coding: utf-8 -*-
"""端到端：用**生成版** unify_dh_gen 登录模拟器，验证回调在真实 SDK 线程上触发。

这是 selftest 钩子（`_selftest_fXxx`）之外的另一条验证：selftest 只能证明
"从裸 std::thread 调 thunk"不崩，而这里证明的是真实链路 ——
SDK 自己的工作线程 -> thunk -> GIL -> Python。

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

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import _paths  # noqa: E402

SERVER = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                      "simulator", "server.py")

# 模拟器胶水已从字符串字面量挪成真文件（e2e/simulator/server.py）：改端口/账号
# 直接编辑那个文件，不用在测试脚本的字符串里翻找。模拟器仓库路径由 _paths 给出。
proc = subprocess.Popen([sys.executable, SERVER, _paths.SIMULATOR])
time.sleep(1.5)

_paths.add_sdk_dll_dirs("dahua")
g = _paths.import_pyd("unify_dh_gen")

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
