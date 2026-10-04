"""验证 nanobind 适配器：fDisConnect 断线回调端到端。

流程：Python 函数 → set_disconnect_callback 拿 C 回调地址 → init 注册 →
登录模拟器 → server 主动断开 → 看 nanobind 适配器是否触发 Python 函数。
"""
import io
import os
import subprocess
import sys
import time

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

UNIFY = r"C:\Users\Hast\Documents\CodeProjects\UnifyNetSDK"

server_script = r'''
import sys, time
sys.path.insert(0, r"C:\Users\Hast\Documents\CodeProjects\Dahua_NVR_Simulator\src")
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
'''

proc = subprocess.Popen([sys.executable, "-c", server_script])
time.sleep(1.5)

os.add_dll_directory(os.path.join(UNIFY, "dahua", "C_Win64", "Bin"))
sys.path.insert(0, os.path.join(UNIFY, "native", "build"))
import unify_dh  # noqa: E402


def on_disconnect(lLoginID, pchDVRIP, nDVRPort, dwUser):
    print(">>> [回调] 断线触发! loginID=%d ip=%r port=%d user=%d" %
          (lLoginID, pchDVRIP, nDVRPort, dwUser), flush=True)


cb_addr = unify_dh.set_disconnect_callback(on_disconnect)
print("[client] 回调地址 = %#x" % cb_addr, flush=True)

unify_dh.init(cb_addr, 0x1234)
unify_dh.set_connect_time(5000, 3)

li = unify_dh.NET_IN_LOGIN_WITH_HIGHLEVEL_SECURITY()
li.szIP = "127.0.0.1"
li.nPort = 37778
li.szUserName = "admin"
li.szPassword = "admin123"
li.nClientType = 3

handle, res = unify_dh.login(li)
print("[client] 登录 handle=%d nError=%d" % (handle, res.nError), flush=True)

for i in range(8):
    time.sleep(1)

proc.wait(timeout=10)
print("Done.")
