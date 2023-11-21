from datetime import datetime
from pathlib import Path
from threading import RLock


class UnifyLoginArg:
    # 基础的登录参数
    def __init__(self):
        self.deviceAddress = None
        self.devicePort = None
        self.userName = None
        self.userPassword = None


class UnifyDownLoadByTimeArg:
    # 基础的按时间下载回放参数定义，注意大华的downloadbytime不支持选择码流
    def __init__(self):
        self.channel = None
        self.saveFilePath = None  # Path(saveFilePath).absolute()
        self.startTime = None
        self.stopTime = None


class UnifyFindFileByTimeArg:
    # 基础的按时间搜索回放参数定义，做这个数据保存类是由于海康的搜索回放函数中的时间参数是不同于下载回放函数中的时间参数的，这很奇怪。
    def __init__(self):
        self.channel = None
        self.startTime = None
        self.stopTime = None


class UnifyPlayBackByTimeArg:
    # 基础的按时间回放参数定义，高度相同
    def __init__(self):
        self.channel = None
        self.startTime = None
        self.stopTime = None
        self.hwnd = None
        self.dataCallBack = None
        self.dwPosUser = None
        self.downLoadPosCallBack = None
        self.dwDataUser = None
