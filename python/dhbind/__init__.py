# -*- coding: utf-8 -*-
"""dhbind —— 大华 NetSDK 厚封装 wheel（第 2 层）。

import 即加载 ``_binding/`` 里的 pyd 与厂商 DLL（布局见 ``_native.py``），
所以 ``import dhbind`` 本身就是"包是完整的"的证明。用法::

    import dhbind
    client = dhbind.Client()
    handle = client.login(dhbind.LoginArgs(host="192.168.1.108",
                                           user="admin", password="..."))
    ...
    client.logout()
"""
from dhbind._native import shutdown   # noqa: F401  进程级 CLIENT_Cleanup（测试收尾用）
from dhbind.client import Client, LoginArgs   # noqa: F401
from dhbind.errors import DhError, DhLoginError   # noqa: F401

__version__ = "1.0.0"

__all__ = ["Client", "LoginArgs", "DhError", "DhLoginError", "shutdown",
           "__version__"]
