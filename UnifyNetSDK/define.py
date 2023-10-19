from abc import ABC, abstractmethod
from typing import List


class UnifyLoginArg(object):
    # 基础的登录参数
    def __init__(self, device_address: str = None, device_port: int = None, user_name: str = None,
                 user_password: str = None):
        self.device_address = device_address
        self.device_port = device_port
        self.user_name = user_name
        self.user_password = user_password


class AbsNetSDK(ABC):

    @abstractmethod
    def init(cls):
        pass

    @abstractmethod
    def _loadLibrary(cls):
        pass

    @abstractmethod
    def login(cls, login_arg: UnifyLoginArg):
        pass

    @abstractmethod
    def realPlay(cls):
        pass

    @abstractmethod
    def logout(cls,userID):
        pass

    @abstractmethod
    def cleanup(cls):
        pass