from datetime import datetime
from pathlib import Path
from threading import RLock


class SingletonType(type):
    SingletonTypeLock = RLock()

    def __call__(cls, *args, **kwargs):  # 创建cls的对象时候调用
        with SingletonType.SingletonTypeLock:
            if not hasattr(cls, "_instance"):
                cls._instance = super(SingletonType, cls).__call__(*args, **kwargs)  # 创建cls的对象

        return cls._instance




class UnifyLoginArg(metaclass=SingletonType):
    # 基础的登录参数
    def __init__(self, deviceAddress: str = None, devicePort: int = None, userName: str = None,
                 userPassword: str = None):
        self.deviceAddress = deviceAddress
        self.devicePort = devicePort
        self.userName = userName
        self.userPassword = userPassword


class UnifyDownLoadByTimeArg(metaclass=SingletonType):
    # 基础的按时间下载回放参数定义，注意大华的downloadbytime不支持选择码流
    def __init__(self, channel: int = None, saveFilePath: Path = None, startTime: datetime = None, stopTime: datetime = None):
        self.channel = channel
        self.saveFilePath = saveFilePath  # Path(saveFilePath).absolute()
        self.startTime = startTime
        self.stopTime = stopTime


class UnifyFindFileByTimeArg(metaclass=SingletonType):
    # 基础的按时间搜索回放参数定义，做这个数据保存类是由于海康的搜索回放函数中的时间参数是不同于下载回放函数中的时间参数的，这很奇怪。
    def __init__(self, channel: int = None, startTime: datetime = None, stopTime: datetime = None):
        self.channel = channel
        self.startTime = startTime
        self.stopTime = stopTime
