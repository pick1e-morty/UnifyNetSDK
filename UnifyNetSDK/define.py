from abc import ABC, abstractmethod
from datetime import datetime
from threading import RLock

from UnifyNetSDK.parameter import UnifyDownLoadByTimeArg, UnifyFindFileByTimeArg

single_lock = RLock()


def Singleton(cls):
    instance = {}

    def _singleton_wrapper(*args, **kargs):
        with single_lock:
            if cls not in instance:
                instance[cls] = cls(*args, **kargs)
        return instance[cls]

    return _singleton_wrapper


class AbsNetSDK(ABC):

    @classmethod
    @abstractmethod
    def init(cls):
        pass

    @classmethod
    @abstractmethod
    def login(cls, loginArg):
        pass

    @classmethod
    @abstractmethod
    def syncFindFileByTime(cls, userID, findFileArg: UnifyFindFileByTimeArg):
        pass

    # @classmethod
    # @abstractmethod
    # def syncDownLoadByTime(cls, userID, downLoadArg: UnifyDownLoadByTimeArg):
    #     pass

    # @classmethod
    # @abstractmethod
    # def catchPictureFromPlayBackByTimeCallBack(cls, userID, downLoadArg: UnifyDownLoadByTimeArg):
    #     # 有时候会下载失败，sdk却没有显示报错
    #     # 我怀疑是他们自己封装的download有问题
    #     # 我想回放应该是不受他们内部干扰的
    #     # 所以自己写一个回调用来保存录像
    #     # 也就是，只要回放能成功，下载就一定也是成功的
    #     pass

    @classmethod
    @abstractmethod
    def logout(cls, userID):
        pass

    @classmethod
    @abstractmethod
    def cleanup(cls):
        pass

    @staticmethod
    @abstractmethod
    def datetime2DVR_Struct_TIME(timeArg: datetime):
        net_dvr_time = None
        return net_dvr_time
