import time
from time import sleep
from ctypes import *
import os
import sys

from threading import Timer

import schedule

from UnifyNetSDK.define import *
from UnifyNetSDK.haikang.HK_Exception import ErrorCode, HKException
import UnifyNetSDK.haikang.ctypegen.full_headfile as HK

# 结构体初始化会被赋值
# 默认应该都是0的形式，特别是bool
from loguru import logger

from glob_path import ProjectPath

logger.remove()
logger.add(sys.stdout, level="INFO")

# cleanup
# logout还有login都是有返回值的
# 这些估计都要用assert


# sdk函数要对变量本身数据进行修改时需要添加byref函数
# 貌似需要传结构体时都要加byref函数


# 海康sdk的login登录用户名再C语言那边定义为char数组
# python这边用create_string_buffer创建了一个<class 'ctypes.c_char_Array_6'>   也是数组

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


class HaiKangSDK(AbsNetSDK):
    objDll = None
    playctrlDll = None

    def __init__(self):
        self._loadLibrary()

    def init(cls):
        initResult = bool(cls.objDll.NET_DVR_Init())
        logger.info(f"SDK初始化已执行")
        cls.__getLastError("NET_DVR_Init", initResult)

    @classmethod
    def _loadLibrary(cls):
        WINDOWS_FLAG = True
        try:
            if WINDOWS_FLAG:
                libPath = ProjectPath / "UnifyNetSDK/haikang/lib/win"
                cls.objDll = CDLL(str(libPath / "HCNetSDK.dll"))  # 加载网络库
                cls.playctrlDll = CDLL(str(libPath / 'PlayCtrl.dll'))  # 加载播放库

                sdk_ComPath = HK.NET_DVR_LOCAL_SDK_PATH()
                sdk_ComPath.sPath = str(libPath).encode("gbk")
                setResult = bool(cls.objDll.NET_DVR_SetSDKInitCfg(2, byref(sdk_ComPath)))
                cls.__getLastError("NET_DVR_SetSDKInitCfg", setResult)
                libcryptoPath = str(libPath / "libcrypto-1_1-x64.dll").encode("gbk")
                setResult = bool(cls.objDll.NET_DVR_SetSDKInitCfg(3, create_string_buffer(libcryptoPath)))
                cls.__getLastError("NET_DVR_SetSDKInitCfg", setResult)
                libsslPath = str(libPath / "libssl-1_1-x64.dll").encode("gbk")
                setResult = bool(cls.objDll.NET_DVR_SetSDKInitCfg(4, create_string_buffer(libsslPath)))
                cls.__getLastError("NET_DVR_SetSDKInitCfg", setResult)

        except OSError as e:
            logger.error(f"动态库加载失败,原错误信息:{e}")
            # logger.exception(e)

    @classmethod
    def login(cls, loginArg: UnifyLoginArg):
        # 登录参数，包括设备地址、登录用户、密码等
        login_info = HK.NET_DVR_USER_LOGIN_INFO()
        login_info.bUseAsynLogin = 0  # 同步通讯登录
        login_info.sDeviceAddress = loginArg.device_address.encode()
        login_info.wPort = loginArg.device_port
        login_info.sUserName = loginArg.user_name.encode()
        login_info.sPassword = loginArg.user_password.encode()
        # 设备信息, 输出参数
        device_info = HK.NET_DVR_DEVICEINFO_V40()
        # 登录
        userID = cls.objDll.NET_DVR_Login_V40(login_info, byref(device_info))  # TODO 注意device_info是需要加byref才能正常显示的
        cls.__getLastError("NET_DVR_Login_V40", userID)
        print("硬盘数量", device_info.struDeviceV30.byDiskNum)
        return userID

    @classmethod
    def stopDownLoadTimer(cls, downLoadHandle: int):
        downLoadPos = c_int()
        cls.objDll.NET_DVR_PlayBackControl_V40(downLoadHandle, HK.NET_DVR_PLAYGETPOS, c_void_p(), 0, byref(downLoadPos), 1)
        logger.trace(f"下载ID {downLoadHandle},下载状态 {downLoadPos.value}")
        if downLoadPos.value == 100:
            logger.info(f"下载ID {downLoadHandle} 下载成功")
            stopGetFileResult = cls.objDll.NET_DVR_StopGetFile(downLoadHandle)
            cls.__getLastError("NET_DVR_StopGetFile", stopGetFileResult)
        elif downLoadPos.value == 200:
            logger.info(f"下载ID {downLoadHandle} 下载异常")
            stopGetFileResult = cls.objDll.NET_DVR_StopGetFile(downLoadHandle)
            cls.__getLastError("NET_DVR_StopGetFile", stopGetFileResult)
        return downLoadPos.value

    @classmethod
    def stopFindFileTimer(cls, findHandle):

        lpFindData = HK.NET_DVR_FINDDATA_V50()  # 这是一个out参数，用来接收文件查找结果信息的
        findResult = cls.objDll.NET_DVR_FindNextFile_V50(findHandle, byref(lpFindData))
        cls.__getLastError("NET_DVR_FindNextFile_V50", findResult)

        # if findResult ==

    @classmethod
    def syncFindFileByTime(cls, userID, findFileArg: UnifyFindFileByTimeArg):
        findHandle = cls.__findFileByTime(userID, findFileArg)
        while True:
            findResult = cls.stopFindFileTimer(findHandle)
            if findResult != HK.NET_DVR_ISFINDING:  #
                return findResult
            sleep(0.5)

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
        findHandle = cls.objDll.NET_DVR_FindFile_V50(userID, pFindCond)
        cls.__getLastError("NET_DVR_FindFile_V50", findHandle)

        return findHandle

    @classmethod
    def syncDownLoadByTime(cls, userID, downLoadArg: UnifyDownLoadByTimeArg):
        """
        hk说按照时间下载就只会有三个数值，0：正在下载，100：下载完成，200：下载异常
        其它报错都会直接被raise出来
        """
        downLoadHandle = cls.__downLoadByTime(userID, downLoadArg)
        while True:
            downLoadResult = cls.stopDownLoadTimer(downLoadHandle)  # 每0.5秒查一下有没有下载完成
            if downLoadResult != 0:
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
        pDownloadCond.struStartTime = cls.datetime2NET_DVR_TIME(downLoadArg.startTime)
        pDownloadCond.struStopTime = cls.datetime2NET_DVR_TIME(downLoadArg.stopTime)
        # 开始下载
        # TODO 如果成功了还要做一个先查找是否有录像的功能，因为如果没录象的话SDK并不会报错，而是直接下载文件大小为0kb
        downLoadHandle = cls.objDll.NET_DVR_GetFileByTime_V40(userID, sSavedFileName, byref(pDownloadCond))
        cls.__getLastError("NET_DVR_GetFileByTime_V40", downLoadHandle)

        controlResult = bool(cls.objDll.NET_DVR_PlayBackControl_V40(downLoadHandle, HK.NET_DVR_PLAYSTART, c_void_p(), 0, c_void_p(), 0))
        cls.__getLastError("NET_DVR_PlayBackControl_V40", controlResult)

        return downLoadHandle

    @classmethod  # 目前认为海康把两种状态作为方法执行错位的标识，-1和False，其他的都是正常值，不过我怕它整个新花样，如果能在这个方法中指定错误值，哦。。。那就需要白名单和黑名单了。。。。。。。。。。
    def __getLastError(cls, methodName, methodResult):  # todo 如果这种写法能用的话记得加到define里
        logger.debug(f"{methodName}执行结果为 {type(methodResult)} {methodResult}")
        if methodResult == -1 or methodResult is False:
            errorIndex = cls.objDll.NET_DVR_GetLastError()
            errorText = ErrorCode[errorIndex]
            logger.error(f"{errorIndex} {errorText}")
            raise HKException(errorIndex, errorText)

    # def getLastError(cls):
    #     errorIndex = cls.objDll.NET_DVR_GetLastError()
    #     try:
    #         errorText = ErrorCode[errorIndex]
    #         raise HKException(errorIndex, errorText)
    #     except KeyError:
    #         errorText = "未知错误代码,查手册"
    #         raise HKException(errorIndex, errorText)

    @classmethod
    def logout(cls, userID):
        logoutResult = bool(cls.objDll.NET_DVR_Logout(userID))
        logger.info(f"用户ID：{userID} 已登出")
        cls.__getLastError("NET_DVR_Logout", logoutResult)

    @classmethod
    def cleanup(cls):
        cleanupResult = bool(cls.objDll.NET_DVR_Cleanup())
        logger.info("SDK资源已释放")
        cls.__getLastError("NET_DVR_Cleanup", cleanupResult)

    @staticmethod
    def datetime2NET_DVR_TIME(timeArg: datetime):
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
