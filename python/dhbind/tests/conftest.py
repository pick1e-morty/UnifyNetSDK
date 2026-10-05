# -*- coding: utf-8 -*-
"""dhbind 测试装置。

e2e 需要 ../Dahua_NVR_Simulator（项目根的兄弟目录，独立 clone）。
server 胶水就在本包内：tests/simulator/server.py（2026-10-05 从
native/tests/e2e/simulator/ 搬来 —— e2e 归 python 层，之前跨层引用 native 的
测试文件本身就是放错层了）。
"""
import os
import subprocess
import sys
import time

import pytest

#: 本文件 = python/dhbind/tests/conftest.py。`import dhbind` 需要**包目录的
#: 父目录**（python/）在 sys.path 上 —— 与 wheel 装进 site-packages 同理。
PKG_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PKG_PARENT = os.path.dirname(PKG_ROOT)
if PKG_PARENT not in sys.path:
    sys.path.insert(0, PKG_PARENT)


def _project_root():
    d = PKG_ROOT
    while True:
        if os.path.isfile(os.path.join(d, "native", "CMakeLists.txt")):
            return d
        parent = os.path.dirname(d)
        if parent == d:
            raise RuntimeError("project root not found above %s" % PKG_ROOT)
        d = parent


PROJECT = _project_root()
SIMULATOR = os.path.join(os.path.dirname(PROJECT), "Dahua_NVR_Simulator")
SERVER_GLUE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "simulator", "server.py")

# 与 server.py 胶水内写死的端口/账号一致（改这里要连胶水一起改）
SIM = {"host": "127.0.0.1", "port": 37778, "user": "admin", "password": "admin123"}


@pytest.fixture(scope="module")
def sim_server():
    """拉起模拟器的 NetSDK 服务器（Gen2 登录 + 3 通道），测试结束停掉。"""
    if not os.path.isdir(SIMULATOR):
        pytest.skip("Dahua_NVR_Simulator 不在 %s（e2e 需要模拟器）" % SIMULATOR)
    proc = subprocess.Popen([sys.executable, SERVER_GLUE, SIMULATOR],
                            cwd=SIMULATOR,
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(3)          # server.py 自带 3s 启动等待
    yield proc
    proc.terminate()
    try:
        proc.wait(timeout=5)
    except subprocess.TimeoutExpired:
        proc.kill()
