# from datetime import datetime
# from pathlib import Path
# from threading import RLock


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

    def getSimpleReadMsg(self):
        text = f"通道 {self.channel}, 开始查询时间 {self.startTime}, 结束查询时间 {self.stopTime}\n 下载路径 {self.saveFilePath}"
        return text


class UnifyFindFileByTimeArg:
    # 基础的按时间搜索回放参数定义，做这个数据保存类是由于海康的搜索回放函数中的时间参数是不同于下载回放函数中的时间参数的，这很奇怪。
    def __init__(self):
        self.channel = None
        self.startTime = None
        self.stopTime = None

    def getSimpleReadMsg(self):
        text = f"通道 {self.channel}, 开始查询时间 {self.startTime}, 结束查询时间 {self.stopTime}"
        return text


class UnifyPlayBackByTimeArg:
    # 基础的按时间回放参数定义，高度相同
    def __init__(self):
        self.channel = None
        self.startTime = None
        self.stopTime = None
        self.hwnd = None
        self.dataCallBack = None        # 设备返回数据的回调函数
        self.dwDataUser = None          # 用户自定义参数
        self.downLoadPosCallBack = None # 设备返回下载进度的回调函数
        self.dwPosUser = None           # 用户自定义参数


class UninfyNTPArg:
    # 基础的NTP参数定义
    def __init__(self):
        self.enable = False  # 是否启用NTP
        self.domainOrIP = ""  # 域名或IP
        self.port = 0  # NTP 端口
        self.updateInterval = 0  # 更新时间间隔
        self.timeZone = None  # 时区,两家时区还不是用的同一套系统，一个24时区一个36时区，不管了，默认None，不传sdk那边就设置东八UTC+8

