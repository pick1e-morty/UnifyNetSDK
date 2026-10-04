# -*- coding: utf-8 -*-
"""大华 NVR 模拟器的启动胶水。

原来这段逻辑内嵌在 test_login_callback.py 的一个三引号字符串字面量里：改端口/账号
要在字符串里翻找，IDE 跳不过去，报错行号也指向那个测试文件。TODO 0.2 里写了
"模拟器胶水从字符串字面量挪成真文件"，这里是兑现。

用法：由 test_login_callback.py 以子进程方式启动，模拟器仓库根路径走 argv[1]：

    python server.py [Dahua_NVR_Simulator 仓库根]

为什么路径从命令行拿而不是自己推导：本文件在 native/tests/e2e/simulator/，
到项目根要往上数 5 层；模拟器又不在项目内（独立 clone，与 UnifyNetSDK 同级）。
数层数的地方一多就一定会错，而调用方那边有现成的锚点查找（_paths.SIMULATOR），
传进来最省事。
"""
import os
import sys
import time

if len(sys.argv) < 2:
    sys.exit("usage: python server.py [Dahua_NVR_Simulator 仓库根]")

SIM_ROOT = sys.argv[1]
sys.path.insert(0, os.path.join(SIM_ROOT, "src"))

from config import DeviceConfig                                          # noqa: E402
from dahua_netsdk import DahuaNetSDKServer                              # noqa: E402

cfg = DeviceConfig()
cfg.ip = "127.0.0.1"
cfg.dahua_port = 37778
cfg.username = "admin"
cfg.password = "admin123"
cfg.set_channel_count(3)

srv = DahuaNetSDKServer(
    lambda: cfg,
    log_cb=lambda s, level="INFO": print("  [srv]", s, flush=True))
srv.start()
time.sleep(3)
print("[srv] active disconnect all ...", flush=True)
srv.stop()
time.sleep(3)
