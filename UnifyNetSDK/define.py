from abc import ABC, abstractmethod
from datetime import datetime
from pathlib import Path
from typing import List
from time import time, struct_time


# TODO 这几个统一参数都要用单例

class UnifyLoginArg(object):
    # 基础的登录参数
    def __init__(self, device_address: str = None, device_port: int = None, user_name: str = None,
                 user_password: str = None):
        self.device_address = device_address
        self.device_port = device_port
        self.user_name = user_name
        self.user_password = user_password


class UnifyDownLoadByTimeArg(object):
    # 基础的按时间下载回放参数定义，注意大华的downloadbytime不支持选择码流
    def __init__(self, channel: int = None, saveFilePath: Path = None, startTime: datetime = None,
                 stopTime: datetime = None):
        self.channel = channel
        self.saveFilePath = saveFilePath  # Path(saveFilePath).absolute()
        self.startTime = startTime
        self.stopTime = stopTime


class AbsNetSDK(ABC):

    @abstractmethod
    def init(cls):
        pass

    @abstractmethod
    def _loadLibrary(cls):
        pass

    @abstractmethod
    def login(cls, loginArg: UnifyLoginArg):
        pass

    @abstractmethod
    def realPlay(cls):
        pass

    @abstractmethod
    def playBackByTime(cls):
        pass

    @abstractmethod
    def downLoadByTime(cls, userID, downLoadArg: UnifyDownLoadByTimeArg):
        pass

    @abstractmethod
    def customDownLoadFromPlayBackByTime(cls):
        # 有时候会下载失败，sdk却没有显示报错
        # 我怀疑是他们自己封装的download有问题
        # 我想回放应该是不受他们内部干扰的
        # 所以自己写一个回调用来保存录像
        # 也就是，只要回放能成功，下载就一定也是成功的

        pass

    @abstractmethod
    def logout(cls, userID):
        pass

    @abstractmethod
    def cleanup(cls):
        pass

    @staticmethod
    @abstractmethod
    def datetime2NET_DVR_TIME(timeArg: datetime):
        net_dvr_time = None
        return net_dvr_time
