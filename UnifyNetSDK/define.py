from abc import ABC, abstractmethod
from datetime import datetime
from pathlib import Path
from typing import List


# TODO 这几个统一参数都要用单例

class UnifyLoginArg(object):
    # 基础的登录参数
    def __init__(self, deviceAddress: str = None, devicePort: int = None, userName: str = None,
                 userPassword: str = None):
        self.deviceAddress = deviceAddress
        self.devicePort = devicePort
        self.userName = userName
        self.userPassword = userPassword


class UnifyDownLoadByTimeArg(object):
    # 基础的按时间下载回放参数定义，注意大华的downloadbytime不支持选择码流
    def __init__(self, channel: int = None, saveFilePath: Path = None, startTime: datetime = None, stopTime: datetime = None):
        self.channel = channel
        self.saveFilePath = saveFilePath  # Path(saveFilePath).absolute()
        self.startTime = startTime
        self.stopTime = stopTime


class UnifyFindFileByTimeArg(object):
    # 基础的按时间搜索回放参数定义，做这个数据保存类是由于海康的搜索回放函数中的时间参数是不同于下载回放函数中的时间参数的，这很奇怪。
    def __init__(self, channel: int = None, startTime: datetime = None, stopTime: datetime = None):
        self.channel = channel
        self.startTime = startTime
        self.stopTime = stopTime


class AbsNetSDK(ABC):

    @abstractmethod
    def init(cls):
        pass

    # @abstractmethod
    # def _loadLibrary(cls):
    #     pass

    @abstractmethod
    def login(cls, loginArg: UnifyLoginArg):
        pass

    # @abstractmethod
    # def downLoadByTime(cls, userID, downLoadArg: UnifyDownLoadByTimeArg):
    #     pass

    # @abstractmethod
    # def realPlay(cls):
    #     pass
    #
    # @abstractmethod
    # def playBackByTime(cls):
    #     pass
    #
    #
    #
    # @abstractmethod
    # def customDownLoadFromPlayBackByTime(cls):
    #     # 有时候会下载失败，sdk却没有显示报错
    #     # 我怀疑是他们自己封装的download有问题
    #     # 我想回放应该是不受他们内部干扰的
    #     # 所以自己写一个回调用来保存录像
    #     # 也就是，只要回放能成功，下载就一定也是成功的
    #     pass

    @abstractmethod
    def logout(cls, userID):
        pass

    @abstractmethod
    def cleanup(cls):
        pass

    # @staticmethod
    # @abstractmethod
    # def datetime2NET_DVR_TIME(timeArg: datetime):
    #     net_dvr_time = None
    #     return net_dvr_time
