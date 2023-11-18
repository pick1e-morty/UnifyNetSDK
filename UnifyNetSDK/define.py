from abc import ABC, abstractmethod
from threading import RLock

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

    @abstractmethod
    def init(cls):
        pass

    # @abstractmethod
    # def _loadLibrary(cls):
    #     pass

    @abstractmethod
    def login(cls, loginArg):
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
