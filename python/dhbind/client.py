# -*- coding: utf-8 -*-
"""大华 Client：把"构造结构体、填 dwSize、阻塞调用"包成 Python 方法。

TODO 0.6 的验证方式：先手工写一个 LoginArgs 确认形态，跑通后再讨论自动生成。
本文件就是那个"确认形态"的第一版 —— 只做登录/登出，预览/报警等 Client 能力
等这条链路在模拟器上全绿之后再逐个加。

底层统一走生成版 unify_dh_gen：所有函数绑定都带 gil_scoped_release，登录这类
阻塞调用不会饿死同进程其他线程（语义与 ctypes.CDLL 等比）；dwSize 也由结构体的
生成版 __init__ 自动填好，不需要手写模块。
"""
from dataclasses import dataclass

from . import _native
from .errors import DhError, DhLoginError


@dataclass
class LoginArgs:
    """登录参数。字段名对应 NET_IN_LOGIN_WITH_HIGHLEVEL_SECURITY 的常用子集，
    其余字段（emSpecCap 等）由底层给安全默认值（TCP）。"""

    host: str
    user: str = "admin"
    password: str = ""
    port: int = 37777


class Client:
    """一个大华设备的连接。一个实例一个会话，登录后用 :attr:`device` 看设备信息。

    用法::

        client = dhbind.Client()
        handle = client.login(LoginArgs(host="127.0.0.1", user="admin",
                                        password="admin123", port=37778))
        ...
        client.logout()
    """

    def __init__(self):
        self._handle = 0
        self._device = None

    def login(self, args: LoginArgs) -> int:
        """登录，返回 SDK 句柄（非零）。失败抛 :class:`DhLoginError`。"""
        if self._handle:
            raise DhError("already logged in (handle=%d); logout first" % self._handle)
        g = _native.gen()
        in_param = g.NET_IN_LOGIN_WITH_HIGHLEVEL_SECURITY()
        in_param.szIP = args.host
        in_param.nPort = args.port
        in_param.szUserName = args.user
        in_param.szPassword = args.password
        out = g.NET_OUT_LOGIN_WITH_HIGHLEVEL_SECURITY()
        handle = g.CLIENT_LoginWithHighLevelSecurity(in_param, out)
        if handle == 0 or out.nError != 0:
            raise DhLoginError(out.nError, g.CLIENT_GetLastError())
        self._handle = int(handle)
        self._device = out.stuDeviceInfo
        return self._handle

    @property
    def handle(self) -> int:
        """SDK 句柄；未登录时为 0。"""
        return self._handle

    @property
    def device(self):
        """登录成功后的 NET_DEVICEINFO_Ex（通道数、序列号等），未登录为 None。"""
        return self._device

    def logout(self) -> bool:
        """登出。未登录时返回 False。"""
        if not self._handle:
            return False
        ok = _native.gen().CLIENT_Logout(self._handle)
        self._handle = 0
        return bool(ok)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        self.logout()
