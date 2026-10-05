# -*- coding: utf-8 -*-
"""大华 NVR 模拟器的启动胶水。

原来这段逻辑内嵌在测试文件的一个三引号字符串字面量里：改端口/账号要在字符串里
翻找，IDE 跳不过去，报错行号也指向那个测试文件。TODO 0.2 里写了"模拟器胶水从
字符串字面量挪成真文件"，这里是兑现。

**2026-10-05 从 native/tests/e2e/simulator/ 搬到这里**：e2e 属于 python 层
（wheel）而不是 native 层（pyd）；而且 dhbind 的 conftest 本来就一直在跨层引用
这个文件，搬过来正好把那层引用收干净。

用法：由本包 conftest.py 的 `sim_server` fixture 以子进程方式启动，模拟器仓库根
路径走 argv[1]：

    python server.py [Dahua_NVR_Simulator 仓库根]

为什么路径从命令行拿而不是自己推导：模拟器不在项目内（独立 clone，与 UnifyNetSDK
同级），数层数的地方一多就一定会错，调用方那边有现成的锚点查找，传进来最省事。

启动后的行为：服务 3 秒 -> **主动断开所有连接**（用来触发断线回调）-> 停服 ->
3 秒后进程退出。所以拿它做 e2e 时，客户端要在前 3 秒内登录上。
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
