# -*- coding: utf-8 -*-
"""e2e：dhbind.Client 连 Dahua_NVR_Simulator 的完整登录/登出链路。

被 pytest.ini 默认排除（-m "not e2e"），用 `pytest -m e2e` 实跑。
"""
import dhbind
from dhbind import DhError, DhLoginError, LoginArgs

import pytest


@pytest.mark.e2e
def test_login_logout(sim_server):
    client = dhbind.Client()
    try:
        handle = client.login(LoginArgs(host="127.0.0.1", user="admin",
                                        password="admin123", port=37778))
        assert handle != 0
        assert client.handle == handle
        # 模拟器 server.py 配置 3 个通道
        assert client.device.nChanNum == 3
        assert client.logout() is True
        assert client.handle == 0
    finally:
        client.logout()


@pytest.mark.e2e
def test_login_wrong_password(sim_server):
    client = dhbind.Client()
    with pytest.raises(DhLoginError) as exc:
        client.login(LoginArgs(host="127.0.0.1", user="admin",
                               password="wrong-password", port=37778))
    assert exc.value.code != 0


@pytest.mark.e2e
def test_login_twice_on_same_client(sim_server):
    client = dhbind.Client()
    try:
        client.login(LoginArgs(host="127.0.0.1", port=37778,
                               password="admin123"))
        with pytest.raises(DhError, match="already logged in"):
            client.login(LoginArgs(host="127.0.0.1", port=37778,
                                   password="admin123"))
    finally:
        client.logout()


@pytest.mark.e2e
def test_context_manager(sim_server):
    with dhbind.Client() as client:
        client.login(LoginArgs(host="127.0.0.1", port=37778,
                               password="admin123"))
        assert client.handle != 0
    assert client.handle == 0        # __exit__ 已登出
