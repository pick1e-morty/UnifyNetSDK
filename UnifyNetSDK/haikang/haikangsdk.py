import os
from pathlib import Path
from time import sleep
from ctypes import *
import sys
from UnifyNetSDK.define import *
from UnifyNetSDK.haikang.hk_exception import ErrorCode, HKException
from UnifyNetSDK.parameter import *
import UnifyNetSDK.haikang.ctypes_headfile as HK
from loguru import logger

logger.remove()
logger.add(sys.stdout, level="DEBUG")

"""
from ctypes import *
var1 = create_string_buffer(b"admin")   # 创建内容大小的c char数组，同时还被附加了byref函数同等属性，引用传递，可变数值

    

var2 = b"admin"     # 不能指定编码且不能使用非ascii字符
var3 = "你好".encode("gbk")
var4 = bytes('你好', encoding="utf-8") # 这是可指定编码的bytes创建方式
var5=b"a"   # 没有byte，只有bytes
var6 = bytearray(b'admin')      # bytes不可变（理解元组），这个bytearray就是可变的了


print(var1,type(var1))
print(var2,type(var2))
print(var3,type(var3))
print(var4,type(var4))
print(var5,type(var5))
print(var6,type(var6))

"""


# @Singleton
# 上面这个单例有问题，会影响类的类方法，python最终会认为这个类一个function
class HaiKangSDK(AbsNetSDK):
    sdkDll = None
    playctrlDll = None

    def __init__(self):
        self._loadLibrary()

    @classmethod
    def init(cls):
        initResult = bool(cls.sdkDll.NET_DVR_Init())
        logger.info(f"SDK初始化已执行")
        cls.getLastError("NET_DVR_Init", initResult)

    @classmethod
    def _loadLibrary(cls):
        try:
            curPyPath = Path(__file__).parent
            libPath = curPyPath / "lib/win"
            # cls.sdkDll = CDLL(str(libPath / "HCNetSDK.dll"))  # 加载网络库
            cls.sdkDll = HK  # hcnetsdk.dll由ctypesgen中间层加载
            # cls.playctrlDll = CDLL(str(libPath / 'PlayCtrl.dll'))  # 加载播放库

            sdk_ComPath = HK.NET_DVR_LOCAL_SDK_PATH()
            sdk_ComPath.sPath = str(libPath).encode("gbk")
            setResult = cls.sdkDll.NET_DVR_SetSDKInitCfg(2, byref(sdk_ComPath))
            cls.getLastError("NET_DVR_SetSDKInitCfg", bool(setResult))
            libcryptoPath = str(libPath / "libcrypto-1_1-x64.dll").encode("gbk")
            setResult = cls.sdkDll.NET_DVR_SetSDKInitCfg(3, create_string_buffer(libcryptoPath))
            cls.getLastError("NET_DVR_SetSDKInitCfg", bool(setResult))
            libsslPath = str(libPath / "libssl-1_1-x64.dll").encode("gbk")
            setResult = cls.sdkDll.NET_DVR_SetSDKInitCfg(4, create_string_buffer(libsslPath))
            cls.getLastError("NET_DVR_SetSDKInitCfg", bool(setResult))

        except OSError as e:
            logger.error(f"动态库加载失败,原错误信息:{e}")
            # logger.exception(e)

    @classmethod
    def login(cls, loginArg: UnifyLoginArg):
        # 登录参数，包括设备地址、登录用户、密码等
        loginInfo = HK.NET_DVR_USER_LOGIN_INFO()
        loginInfo.bUseAsynLogin = 0  # 同步通讯登录
        loginInfo.sDeviceAddress = loginArg.deviceAddress.encode()
        loginInfo.wPort = loginArg.devicePort
        loginInfo.sUserName = loginArg.userName.encode()
        loginInfo.sPassword = loginArg.userPassword.encode()
        # 设备信息, 输出参数
        deviceInfo = HK.NET_DVR_DEVICEINFO_V40()
        # 登录
        userID = cls.sdkDll.NET_DVR_Login_V40(loginInfo, byref(deviceInfo))
        cls.getLastError("NET_DVR_Login_V40", userID)
        return userID, deviceInfo

    @classmethod
    def stopFindFileTimer(cls, findHandle):

        lpFindData = HK.NET_DVR_FINDDATA_V50()  # 这是一个out参数，用来接收文件查找结果信息的
        findResult = cls.sdkDll.NET_DVR_FindNextFile_V50(findHandle, byref(lpFindData))
        cls.getLastError("NET_DVR_FindNextFile_V50", findResult)

        # findStateList = {1001: HK.NET_DVR_FILE_NOFIND,
        #                  1003: HK.NET_DVR_NOMOREFILE,
        #                  1004: HK.NET_DVR_FILE_EXCEPTION,
        #                  1005: HK.NET_DVR_FIND_TIMEOUT}

        findStateList = {1001: "未查找到文件",
                         1003: "没有更多的文件，查找结束",
                         1004: "查找文件时异常",
                         1005: "查找文件超时"}
        if findResult == HK.NET_DVR_ISFINDING:
            logger.trace(f"查找ID {findHandle},正在查找 {findResult}")
        elif findResult == HK.NET_DVR_FILE_SUCCESS:
            logger.success(f"查找ID {findHandle},查找成功")
            stopFindResult = cls.sdkDll.NET_DVR_FindClose_V30(findHandle)
            cls.getLastError("NET_DVR_FindClose_V30", stopFindResult)
            return True
        elif findResult in findStateList:
            logger.error(f"查找ID {findHandle},查找状态异常代码 {findResult},{findStateList[findResult]}")
            stopFindResult = cls.sdkDll.NET_DVR_FindClose_V30(findHandle)
            cls.getLastError("NET_DVR_FindClose_V30", bool(stopFindResult))
        return findResult

    @classmethod
    def syncFindFileByTime(cls, userID, findFileArg: UnifyFindFileByTimeArg):
        """
        成功返回True
        失败返回False
        """
        findHandle = cls.__findFileByTime(userID, findFileArg)
        while True:
            findResult = cls.stopFindFileTimer(findHandle)
            if findResult != HK.NET_DVR_ISFINDING:  #
                if findResult is True:      # 大华和海康这部分功能的实现真是花开一表各表自枝啊
                    return True             # 我统一了一下
                else:                       # 找到了就True，没找到我底层这边打印个错误代码就行
                    return False
            sleep(0.5)

    @classmethod
    def asyncFindFileByTime(cls, userID, findFileArg: UnifyFindFileByTimeArg):
        findHandle = cls.__findFileByTime(userID, findFileArg)
        return findHandle

    @classmethod
    def __findFileByTime(cls, userID, findFileArg: UnifyFindFileByTimeArg):
        # 准备参数
        struStreamID = HK.NET_DVR_STREAM_INFO()
        struStreamID.dwSize = sizeof(HK.NET_DVR_STREAM_INFO)
        struStreamID.dwChannel = findFileArg.channel

        pFindCond = HK.NET_DVR_FILECOND_V50()
        pFindCond.struStreamID = struStreamID
        pFindCond.struStartTime = cls.datetime2NET_DVR_TIME_SEARCH_COND(findFileArg.startTime)
        pFindCond.struStopTime = cls.datetime2NET_DVR_TIME_SEARCH_COND(findFileArg.stopTime)

        # 开始查询
        findHandle = cls.sdkDll.NET_DVR_FindFile_V50(userID, pFindCond)
        cls.getLastError("NET_DVR_FindFile_V50", findHandle)

        return findHandle

    @classmethod
    def stopDownLoadTimer(cls, downLoadHandle: int):
        downLoadPos = c_int()
        lpOutLen = c_ulong(0)
        cls.sdkDll.NET_DVR_PlayBackControl_V40(downLoadHandle, HK.NET_DVR_PLAYGETPOS, c_void_p(), 0, byref(downLoadPos), byref(lpOutLen))
        logger.trace(f"下载ID {downLoadHandle},下载状态 {downLoadPos.value}")
        if downLoadPos.value == 100:
            logger.success(f"下载ID {downLoadHandle} 下载成功")
            stopGetFileResult = cls.sdkDll.NET_DVR_StopGetFile(downLoadHandle)
            cls.getLastError("NET_DVR_StopGetFile", stopGetFileResult)
        elif downLoadPos.value == 200:
            logger.error(f"下载ID {downLoadHandle} 下载异常")
            stopGetFileResult = cls.sdkDll.NET_DVR_StopGetFile(downLoadHandle)
            cls.getLastError("NET_DVR_StopGetFile", stopGetFileResult)
        return downLoadPos.value

    @classmethod
    def syncDownLoadByTime(cls, userID, downLoadArg: UnifyDownLoadByTimeArg):
        """
        hk说按照时间下载就只会有三个数值，0：正在下载，100：下载完成，200：下载异常
        其它报错都会直接被raise出来
        """
        downLoadHandle = cls.__downLoadByTime(userID, downLoadArg)
        while True:
            downLoadResult = cls.stopDownLoadTimer(downLoadHandle)  # 每0.5秒查一下有没有下载完成
            if downLoadResult == 100 or downLoadResult == 200:
                return downLoadResult
            sleep(0.5)

    @classmethod
    def asyncDownLoadByTime(cls, userID, downLoadArg: UnifyDownLoadByTimeArg):
        downLoadHandle = cls.__downLoadByTime(userID, downLoadArg)
        return downLoadHandle

    @classmethod
    def __downLoadByTime(cls, userID, downLoadArg: UnifyDownLoadByTimeArg):
        # 准备参数
        logger.info(f"下载文件路径为{downLoadArg.saveFilePath}")
        sSavedFileName = create_string_buffer(str(downLoadArg.saveFilePath).encode("gbk"))
        pDownloadCond = HK.NET_DVR_PLAYCOND()
        pDownloadCond.dwChannel = downLoadArg.channel
        pDownloadCond.struStartTime = cls.datetime2DVR_Struct_TIME(downLoadArg.startTime)
        pDownloadCond.struStopTime = cls.datetime2DVR_Struct_TIME(downLoadArg.stopTime)
        # 开始下载
        downLoadHandle = cls.sdkDll.NET_DVR_GetFileByTime_V40(userID, sSavedFileName, byref(pDownloadCond))
        cls.getLastError("NET_DVR_GetFileByTime_V40", downLoadHandle)

        controlResult = cls.sdkDll.NET_DVR_PlayBackControl_V40(downLoadHandle, HK.NET_DVR_PLAYSTART, c_void_p(), 0, c_void_p(), byref(c_ulong(0)))
        cls.getLastError("NET_DVR_PlayBackControl_V40", bool(controlResult))

        return downLoadHandle

    @classmethod  # 目前认为海康把两种状态作为方法执行错位的标识，-1和False，其他的都是正常值，不过我怕它整个新花样，如果能在这个方法中指定错误值，哦。。。那就需要白名单和黑名单了。。。。。。。。。。
    def getLastError(cls, methodName, methodResult):  # todo 如果这种写法能用的话记得加到define里
        logger.debug(f"{methodName}执行结果为 {type(methodResult)} {methodResult}")
        if methodResult == -1 or methodResult is False:
            cls.__getLastError()

    @classmethod
    def __getLastError(cls):
        errorIndex = cls.sdkDll.NET_DVR_GetLastError()
        errorText = ErrorCode[errorIndex]
        logger.error(f"{errorIndex} {errorText}")
        raise HKException(errorIndex, errorText)

    @classmethod
    def logout(cls, userID):
        logoutResult = cls.sdkDll.NET_DVR_Logout(userID)
        logger.info(f"用户ID：{userID} 已登出")
        cls.getLastError("NET_DVR_Logout", bool(logoutResult))

    @classmethod
    def cleanup(cls):
        cleanupResult = cls.sdkDll.NET_DVR_Cleanup()
        logger.info("SDK资源已释放")
        cls.getLastError("NET_DVR_Cleanup", bool(cleanupResult))

    @classmethod
    def logopen(cls):
        """
        打开日志功能
        """
        logFilePath = os.path.join(os.getcwd(), 'haikang_sdk.log').encode('gbk')
        setResult = cls.sdkDll.NET_DVR_SetLogToFile(3, logFilePath, True)
        # 日志的等级 日志文件的路径 是否删除超出的文件数
        cls.getLastError("NET_DVR_SetLogToFile", bool(setResult))
        return setResult

    @classmethod
    def logclose(cls):
        """
        关闭日志功能
        """
        pass
        # 海康不需要关闭日志，这是为了用户层调用对齐

    @staticmethod
    def datetime2DVR_Struct_TIME(timeArg: datetime):
        # 省事的时间类型转换,下载录像用的时间类型
        net_dvr_time = HK.NET_DVR_TIME()
        net_dvr_time.dwYear = timeArg.year
        net_dvr_time.dwMonth = timeArg.month
        net_dvr_time.dwDay = timeArg.day
        net_dvr_time.dwHour = timeArg.hour
        net_dvr_time.dwMinute = timeArg.minute
        net_dvr_time.dwSecond = timeArg.second
        return net_dvr_time

    @staticmethod
    def datetime2NET_DVR_TIME_SEARCH_COND(timeArg: datetime):
        # 省事的时间类型转换,查询录像用的时间类型
        net_dvr_time_search_cond = HK.NET_DVR_TIME_SEARCH_COND()
        net_dvr_time_search_cond.wYear = timeArg.year
        net_dvr_time_search_cond.byMonth = timeArg.month
        net_dvr_time_search_cond.byDay = timeArg.day
        net_dvr_time_search_cond.byHour = timeArg.hour
        net_dvr_time_search_cond.byMinute = timeArg.minute
        net_dvr_time_search_cond.bySecond = timeArg.second
        return net_dvr_time_search_cond


if __name__ == "__main__":
    pass
