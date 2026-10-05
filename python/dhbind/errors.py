# -*- coding: utf-8 -*-
"""dhbind 异常类型。

完整的"错误码 -> 异常"体系是独立任务（TODO 第 3 节：从 dhnetsdk.h 自动生成
错误码表），这里只定义骨架：code 随异常携带，调用方可以 `except DhLoginError
as e: e.code` 拿裸数字对照厂商手册。
"""


class DhError(Exception):
    """dhbind 异常基类。code 是 SDK 裸错误码（0 表示无错误）。"""

    def __init__(self, message, code=0):
        super().__init__(message)
        self.code = code


class DhLoginError(DhError):
    """登录失败。code 取 NET_OUT_LOGIN_WITH_HIGHLEVEL_SECURITY.nError。"""

    def __init__(self, code, sdk_last_error=0):
        super().__init__(
            "login failed: nError=%d (CLIENT_GetLastError=%d)" % (code, sdk_last_error),
            code=code)
        self.sdk_last_error = sdk_last_error
