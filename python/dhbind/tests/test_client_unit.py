# -*- coding: utf-8 -*-
"""不需要模拟器的 Client 单测（但 import dhbind 要求 _binding 已填充）。"""
import dhbind
from dhbind import DhError, DhLoginError, LoginArgs


def test_version():
    assert dhbind.__version__ == "1.0.0"


def test_login_args_defaults():
    args = LoginArgs(host="192.168.1.108")
    assert args.host == "192.168.1.108"
    assert args.user == "admin"
    assert args.password == ""
    assert args.port == 37777


def test_error_carries_code():
    err = DhLoginError(5, sdk_last_error=7)
    assert err.code == 5
    assert err.sdk_last_error == 7
    assert isinstance(err, DhError)
    assert "nError=5" in str(err)


def test_client_starts_logged_out():
    client = dhbind.Client()
    assert client.handle == 0
    assert client.device is None
    assert client.logout() is False
