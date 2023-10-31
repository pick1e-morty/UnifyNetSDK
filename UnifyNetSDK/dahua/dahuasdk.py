from time import sleep
from ctypes import *
import sys
from UnifyNetSDK.define import *
from UnifyNetSDK.dahua.dh_exception import ErrorCode, DHException
import UnifyNetSDK.dahua.ctypes_headfile as DH
from loguru import logger
from glob_path import ProjectPath

logger.remove()
logger.add(sys.stdout, level="TRACE")


class DaHuaSDK(AbsNetSDK):
    sdkDll = None
    configDll = None
    playDll = None
    renderDll = None
    infraDll = None

    def __init__(self):
        self._loadLibrary()

    @classmethod
    def _loadLibrary(cls):
        try:
            libPath = ProjectPath / "UnifyNetSDK/dahua/Libs/win64"
            cls.sdkDll = windll.LoadLibrary(str(libPath / "dhnetsdk.dll"))
            # cls.configDll = windll.LoadLibrary(str(libPath / "dhconfigsdk.dll"))
            # cls.playDll = windll.LoadLibrary(str(libPath / "dhplay.dll"))
            # cls.renderDll = windll.LoadLibrary(str(libPath / "RenderEngine.dll"))
            # cls.infraDll = windll.LoadLibrary(str(libPath / "Infra.dll"))
        except OSError as e:
            logger.error(f"动态库加载失败,原错误信息:{e}")
            # logger.exception(e)

    @classmethod
    def init(cls):
        initResult = cls.sdkDll.CLIENT_InitEx(None, 0)
        logger.info(f"SDK初始化已执行")
        cls.__getLastError("CLIENT_InitEx", bool(initResult))

        # 设置接口函数参数类型和函数返回值类型
        """
        cls.sdkDll.CLIENT_LoginWithHighLevelSecurity.restype = c_longlong  # 登录设备
        # cls.sdkDll.CLIENT_LoginWithHighLevelSecurity.argtypes = [DH.NET_IN_LOGIN_WITH_HIGHLEVEL_SECURITY, DH.NET_OUT_LOGIN_WITH_HIGHLEVEL_SECURITY]

        cls.sdkDll.CLIENT_GetDownloadPos.restype = c_bool  # 获取下载进度
        # cls.sdkDll.CLIENT_GetDownloadPos.argtypes = [c_longlong, POINTER(c_int), POINTER(c_int)]


        cls.sdkDll.CLIENT_DownloadByTimeEx.restype = c_longlong  # 按时间下载
        cls.sdkDll.CLIENT_DownloadByTimeEx.argtypes = [c_longlong, c_int, c_int, DH.NET_TIME, DH.NET_TIME, POINTER(c_char), DH.fTimeDownLoadPosCallBack, c_longlong, DH.fDataCallBack, c_longlong]

        cls.sdkDll.CLIENT_StopDownload.restype = c_bool  # 停止下载
        cls.sdkDll.CLIENT_StopDownload.argtypes = [c_longlong]

        # cls.sdkDll.CLIENT_GetLastError.restype = c_ulong  # 获取最新错误代码
        # cls.sdkDll.CLIENT_GetLastError.argtypes = []

        cls.sdkDll.CLIENT_Logout.restype = c_bool  # 登出设备
        cls.sdkDll.CLIENT_Logout.argtypes = [c_longlong]

        cls.sdkDll.CLIENT_Cleanup.restype = c_void_p  # 释放SDK资源
        cls.sdkDll.CLIENT_Cleanup.argtypes = []
        """

    @classmethod
    def login(cls, loginArg: UnifyLoginArg):
        # 登录参数，包括设备地址、登录用户、密码等
        loginInfo = DH.NET_IN_LOGIN_WITH_HIGHLEVEL_SECURITY()
        loginInfo.dwSize = sizeof(DH.NET_IN_LOGIN_WITH_HIGHLEVEL_SECURITY)
        loginInfo.szIP = loginArg.deviceAddress.encode()
        loginInfo.nPort = loginArg.devicePort
        loginInfo.szUserName = loginArg.userName.encode()
        loginInfo.szPassword = loginArg.userPassword.encode()
        # loginInfo.emSpecCap = DH.EM_LOGIN_SPAC_CAP_TYPE.TCP
        # loginInfo.pCapParam = None

        # 设备信息, 输出参数
        deviceInfo = DH.NET_OUT_LOGIN_WITH_HIGHLEVEL_SECURITY()
        deviceInfo.dwSize = sizeof(DH.NET_OUT_LOGIN_WITH_HIGHLEVEL_SECURITY)

        cls.sdkDll.CLIENT_LoginWithHighLevelSecurity.restype = c_longlong  # 登录设备
        login_id = cls.sdkDll.CLIENT_LoginWithHighLevelSecurity(byref(loginInfo), byref(deviceInfo))
        cls.__getLastError("CLIENT_LoginWithHighLevelSecurity", login_id)
        return login_id, deviceInfo

    @classmethod
    def stopDownLoadTimer(cls, downLoadHandle: int):
        nTotalSize = c_int(0)  # 下载的总长度，单位:KB
        nDownLoadSize = c_int(0)  # 已下载的长度，单位:KB

        downLoadHandle = c_longlong(downLoadHandle)
        getDownLoadPosResult = cls.sdkDll.CLIENT_GetDownloadPos(downLoadHandle, byref(nTotalSize), byref(nDownLoadSize))

        cls.__getLastError("CLIENT_GetDownloadPos", bool(getDownLoadPosResult))
        logger.trace(f"下载ID {downLoadHandle} ,下载总长度 {nTotalSize.value}KB ,已下载长度 {nDownLoadSize.value}KB ")
        if nTotalSize.value == nDownLoadSize.value:
            logger.success(f"下载ID {downLoadHandle} 下载完成")
            stopGetFileResult = cls.sdkDll.CLIENT_StopDownload(downLoadHandle)
            cls.__getLastError("CLIENT_StopDownload", stopGetFileResult)
            return True
        else:
            return False

    @classmethod
    def syncDownLoadByTime(cls, userID, downLoadArg: UnifyDownLoadByTimeArg):
        """
        本方法自己提供一个while用于阻塞判读视频是否下载完成
        其它报错会被raise出来
        """
        downLoadHandle = cls.__downLoadByTime(userID, downLoadArg)
        while True:
            downLoadResult = cls.stopDownLoadTimer(downLoadHandle)  # 每0.5秒查一下有没有下载完成
            if downLoadResult is True:
                return downLoadResult
            sleep(1)

    @classmethod
    def asyncDownLoadByTime(cls, userID, downLoadArg: UnifyDownLoadByTimeArg):
        downLoadHandle = cls.__downLoadByTime(userID, downLoadArg)
        return downLoadHandle

    @classmethod
    def __downLoadByTime(cls, userID, downLoadArg: UnifyDownLoadByTimeArg):
        # 准备参数
        logger.info(f"下载文件路径为{downLoadArg.saveFilePath}")
        savedFileName = create_string_buffer(str(downLoadArg.saveFilePath).encode("gbk"))
        channel = downLoadArg.channel

        startDateTime = cls.datetime2NET_TIME(downLoadArg.startTime)
        endDateTime = cls.datetime2NET_TIME(downLoadArg.stopTime)

        # 开始下载。虽然是和抽象接口对齐了，但真正原因是海康没提供下载函数回调接口，顺势而为无伤大雅。

        @DH.fTimeDownLoadPosCallBack
        def empty_fTimeDownLoadPosCallBack():
            pass

        @DH.fDataCallBack
        def empty_fDataCallBack():
            pass

        userID = c_longlong(userID)
        cls.sdkDll.CLIENT_DownloadByTimeEx.restype = c_longlong  # 按时间下载
        # downLoadHandle = cls.sdkDll.CLIENT_DownloadByTimeEx(userID, channel, DH.EM_RECORD_TYPE_ALL, startDateTime, endDateTime, savedFileName, empty_fTimeDownLoadPosCallBack, 0, empty_fDataCallBack, 0)
        downLoadHandle = cls.sdkDll.CLIENT_DownloadByTimeEx(userID, channel, DH.EM_RECORD_TYPE_ALL, startDateTime, endDateTime, savedFileName, None, 0, None, 0)
        cls.__getLastError("CLIENT_DownloadByTimeEx", bool(downLoadHandle))
        return downLoadHandle

    @classmethod
    def __getLastError(cls, methodName, methodResult):  # todo 如果这种写法能用的话记得加到define里
        logger.debug(f"{methodName}执行结果为 {type(methodResult)} {methodResult}")
        if methodResult == -1 or methodResult is False:
            errorIndex = cls.sdkDll.CLIENT_GetLastError() & 0x7fffffff
            errorText = ErrorCode[errorIndex]
            logger.error(f"{errorIndex} {errorText}")
            raise DHException(errorIndex, errorText)

    @classmethod
    def logout(cls, userID):
        userID = c_longlong(userID)
        logoutResult = cls.sdkDll.CLIENT_Logout(userID)
        logger.info(f"用户ID：{userID} 已登出")
        cls.__getLastError("CLIENT_Logout", bool(logoutResult))

    @classmethod
    def cleanup(cls):
        cls.sdkDll.CLIENT_Cleanup()
        logger.info("SDK资源已释放")

    @staticmethod
    def datetime2NET_TIME(timeArg: datetime):
        # 省事的时间类型转换,下载录像用的时间类型
        netTime = DH.NET_TIME()
        netTime.dwYear = timeArg.year
        netTime.dwMonth = timeArg.month
        netTime.dwDay = timeArg.day
        netTime.dwHour = timeArg.hour
        netTime.dwMinute = timeArg.minute
        netTime.dwSecond = timeArg.second
        return netTime
