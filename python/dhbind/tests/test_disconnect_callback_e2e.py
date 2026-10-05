# -*- coding: utf-8 -*-
"""e2e：真实 SDK 工作线程 -> thunk -> GIL -> Python。

**2026-10-05 从 native/tests/e2e/test_login_callback.py 搬到这里并转成 pytest**：
e2e 属于 python 层（wheel）而不是 native 层（pyd）—— 两层产物本质同构，但"连
模拟器"这件事归 dhbind 更合适，native 只留绑定层测试（本包收走模拟器胶水后，
native/tests/e2e/ 整目录已删）。

这是 selftest 钩子（`_selftest_fXxx`）之外的另一条验证：selftest 只能证明"从裸
std::thread 调 thunk"不崩，这里证明的是真实链路。

覆盖：
  1. bind_fDisConnect 返回的地址能直接喂给 CLIENT_Init
  2. Gen2 登录成功（nError == 0）
  3. 模拟器主动断开时，绑定层注册的回调真的被调用，且参数正确

被 pytest.ini 默认排除（-m "not e2e"），用 `pytest -m e2e` 实跑。
"""
import time

import pytest

from dhbind import _native

PORT = 37778
#: CLIENT_Init 的第二个参数：SDK 会在回调里原样回传，用来确认是我们这次注册的
MAGIC = 0x1234


@pytest.fixture
def sdk_with_disconnect_cb():
    """把进程级 SDK 重装成"带断线回调"的形态，收尾还原成 dhbind 的默认形态。

    CLIENT_Init 是进程级的，`import dhbind` 时 _native 已经 ``CLIENT_Init(0, 0)``
    （没有回调）。要装回调只能 Cleanup 后重 Init，所以这里必须还原，否则同进程
    后面的 e2e（test_client_e2e.py 的 Client 登录）会跑到我们的 Init 上。
    """
    g = _native.gen()
    calls = []

    def on_disconnect(login_id, ip, port, user):
        calls.append((login_id, ip, port, user))

    g.CLIENT_Cleanup()
    cb_ptr = g.bind_fDisConnect(on_disconnect)
    assert cb_ptr != 0, "bind_fDisConnect 返回了空指针"
    g.CLIENT_Init(cb_ptr, MAGIC)
    g.CLIENT_SetConnectTime(5000, 3)
    yield g, calls
    g.CLIENT_Cleanup()
    g.CLIENT_Init(0, 0)          # 还原 _native 的默认形态
    g.CLIENT_SetConnectTime(5000, 3)


@pytest.mark.e2e
def test_disconnect_callback_fires(sim_server, sdk_with_disconnect_cb):
    g, calls = sdk_with_disconnect_cb

    in_param = g.NET_IN_LOGIN_WITH_HIGHLEVEL_SECURITY()
    in_param.szIP = "127.0.0.1"
    in_param.nPort = PORT
    in_param.szUserName = "admin"
    in_param.szPassword = "admin123"
    out = g.NET_OUT_LOGIN_WITH_HIGHLEVEL_SECURITY()
    handle = g.CLIENT_LoginWithHighLevelSecurity(in_param, out)
    assert out.nError == 0, "登录失败：nError=%d" % out.nError
    assert handle != 0

    # 模拟器 server.py：服务 3 秒后主动断开所有连接 —— 回调应在那一刻触发
    deadline = time.time() + 20
    while not calls and time.time() < deadline:
        time.sleep(0.3)

    assert len(calls) == 1, "断线回调触发 %d 次（期望 1）" % len(calls)
    login_id, ip, port, user = calls[0]
    assert login_id == handle
    assert ip == "127.0.0.1"
    assert port == PORT
    assert user == MAGIC

    g.CLIENT_Logout(handle)