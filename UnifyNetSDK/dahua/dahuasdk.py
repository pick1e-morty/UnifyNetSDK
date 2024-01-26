import os
from time import sleep
from ctypes import *
import sys

from UnifyNetSDK.define import *
from UnifyNetSDK.dahua.dh_exception import ErrorCode, DHException
import UnifyNetSDK.dahua.ctypes_headfile as DH
from UnifyNetSDK.parameter import *
from loguru import logger

logger.remove()
logger.add(sys.stdout, level="TRACE")


@Singleton
class DaHuaSDK(AbsNetSDK):
    sdkDll = DH  # netsdk.dll由ctypesgen中间层加载
    configDll = None
    playDll = None
    renderDll = None
    infraDll = None

    def __init__(self):
        pass
        # self._loadLibrary()
        # self.setArgTypes_ResType()

    def setArgTypes_ResType(self):
        # 有时候ctypesgen把握不住，就需要手动设置函数的形参类型和返回值类型，目前是弃用的
        self.sdkDll.CLIENT_LoginWithHighLevelSecurity.argtypes = [POINTER(DH.NET_IN_LOGIN_WITH_HIGHLEVEL_SECURITY), POINTER(DH.NET_OUT_LOGIN_WITH_HIGHLEVEL_SECURITY)]
        self.sdkDll.CLIENT_LoginWithHighLevelSecurity.restype = c_longlong
        self.sdkDll.CLIENT_QueryRecordFile.argtypes = [c_longlong, c_int, c_int, DH.LPNET_TIME, DH.LPNET_TIME, DH.String, DH.LPNET_RECORDFILE_INFO, c_int, POINTER(c_int), c_int, c_int]
        self.sdkDll.CLIENT_QueryRecordFile.restype = c_int
        self.sdkDll.CLIENT_DownloadByTimeEx.argtypes = [c_longlong, c_int, c_int, DH.LPNET_TIME, DH.LPNET_TIME, DH.String, DH.fTimeDownLoadPosCallBack, c_long, DH.fDataCallBack, c_long, POINTER(None)]
        self.sdkDll.CLIENT_DownloadByTimeEx.restype = c_longlong
        self.sdkDll.CLIENT_Logout.argtypes = [c_longlong]
        self.sdkDll.CLIENT_Logout.restype = c_int
        self.sdkDll.CLIENT_GetDownloadPos.argtypes = [c_longlong, POINTER(c_int), POINTER(c_int)]
        self.sdkDll.CLIENT_GetDownloadPos.restype = c_int
        self.sdkDll.CLIENT_StopDownload.argtypes = [c_longlong]
        self.sdkDll.CLIENT_StopDownload.restype = c_int
        self.sdkDll.CLIENT_RealPlayEx.argtypes = [c_longlong, c_int, POINTER(None), DH.DH_RealPlayType]
        self.sdkDll.CLIENT_RealPlayEx.restype = c_longlong
        self.sdkDll.CLIENT_PlayBackByTimeEx.argtypes = [c_longlong, c_int, DH.LPNET_TIME, DH.LPNET_TIME, POINTER(None), DH.fDownLoadPosCallBack, c_long, DH.fDataCallBack, c_long]
        self.sdkDll.CLIENT_PlayBackByTimeEx.restype = c_longlong

    @classmethod
    def init(cls):
        initResult = cls.sdkDll.CLIENT_InitEx(DH.fDisConnect(0), 0, DH.NETSDK_INIT_PARAM())
        logger.info(f"SDK初始化已执行")
        cls.getLastError("CLIENT_InitEx", bool(initResult))

    @classmethod
    def _loadLibrary(cls):  # 未使用
        try:
            curPyPath = Path(__file__).parent
            libPath = curPyPath / "Libs/win64"
            cls.sdkDll = windll.LoadLibrary(str(libPath / "dhnetsdk.dll"))
            cls.configDll = windll.LoadLibrary(str(libPath / "dhconfigsdk.dll"))
            cls.renderDll = windll.LoadLibrary(str(libPath / "RenderEngine.dll"))
            cls.infraDll = windll.LoadLibrary(str(libPath / "Infra.dll"))
            cls.playDll = windll.LoadLibrary(str(libPath / "dhplay.dll"))
        except OSError as e:
            logger.error(f"动态库加载失败,原错误信息:{e}")
            # logger.exception(e)

    @classmethod
    def realPlay(cls, userID, channel, hwnd):
        """
        hwnd只需要从QtWidgets.QWidget.winId()获取即可,转换均有sdk这边来做
        """
        valid_hwnd = cast(c_void_p(int(hwnd)), c_void_p)
        # realPlayHandle = cls.sdkDll.CLIENT_RealPlayEx(userID, channel, valid_hwnd, DH.DH_RType_Realplay)
        realPlayHandle = cls.sdkDll.CLIENT_RealPlayEx(userID, channel, valid_hwnd, DH.DH_RType_Multiplay_4)
        cls.getLastError("CLIENT_RealPlayEx", bool(realPlayHandle))
        return realPlayHandle

    @classmethod
    def stopRealPlay(cls, realPlayHandle):
        stopRealPlayResult = cls.sdkDll.CLIENT_StopRealPlay(realPlayHandle)
        cls.getLastError("CLIENT_StopRealPlayEx", bool(stopRealPlayResult))
        return stopRealPlayResult

    @classmethod
    def playBackByTime(cls, userID, playBackArg: UnifyPlayBackByTimeArg):
        channel = playBackArg.channel
        startDateTime = cls.datetime2DVR_Struct_TIME(playBackArg.startTime)
        endDateTime = cls.datetime2DVR_Struct_TIME(playBackArg.stopTime)
        valid_hwnd = cast(c_void_p(int(playBackArg.hwnd)), c_void_p)
        downloadPosCallBack = DH.fDownLoadPosCallBack(0) if playBackArg.downLoadPosCallBack is None else playBackArg.downLoadPosCallBack
        dwPosUser = 0 if playBackArg.dwPosUser is None else playBackArg.dwPosUser
        dataCallBack = DH.fDataCallBack(0) if playBackArg.dataCallBack is None else playBackArg.dataCallBack
        dwDataUser = 0 if playBackArg.dwDataUser is None else playBackArg.dwDataUser
        playBackHandle = cls.sdkDll.CLIENT_PlayBackByTimeEx(userID, channel, byref(startDateTime), byref(endDateTime), valid_hwnd, downloadPosCallBack, dwPosUser, dataCallBack, dwDataUser)
        cls.getLastError("CLIENT_PlayBackByTimeEx", bool(playBackHandle))
        return playBackHandle

    @classmethod
    def stopPlayBack(cls, playBackHandle):
        stopPlayBackResult = cls.sdkDll.CLIENT_StopPlayBack(playBackHandle)
        cls.getLastError("CLIENT_StopPlayBack", bool(stopPlayBackResult))
        return stopPlayBackResult

    @classmethod
    def catchPicture(cls, lPlayHandle, savedFileName):
        # 抓图，可以是实时预览或是回放函数的返回的句柄，
        # 重中之重的是这两个函数的hwnd必须是有效的
        catchResult = cls.sdkDll.CLIENT_CapturePictureEx(lPlayHandle, savedFileName, DH.NET_CAPTURE_JPEG_70)
        cls.getLastError("CLIENT_CapturePictureEx", bool(catchResult))
        return catchResult

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

        # 设备信息, 输出参数
        deviceInfo = DH.NET_OUT_LOGIN_WITH_HIGHLEVEL_SECURITY()
        deviceInfo.dwSize = sizeof(DH.NET_OUT_LOGIN_WITH_HIGHLEVEL_SECURITY)

        cls.sdkDll.CLIENT_LoginWithHighLevelSecurity.restype = c_longlong
        login_id = cls.sdkDll.CLIENT_LoginWithHighLevelSecurity(byref(loginInfo), byref(deviceInfo))
        cls.getLastError("CLIENT_LoginWithHighLevelSecurity", bool(login_id))
        return login_id, deviceInfo

    @classmethod
    def syncFindFileByTime(cls, userID, findFileArg: UnifyFindFileByTimeArg):  # 大华的sdk，能通过时间查询的就这一个方法，且没有返回给我查找句柄，所以大华这边只能有sync了
        return cls.__findFileByTime(userID, findFileArg)  # CLIENT_FindFileEx能返回句柄，但不能按照时间查询

    @classmethod
    def __findFileByTime(cls, userID, findFileArg: UnifyFindFileByTimeArg):
        """
        成功返回True
        失败返回False
        """
        # 准备参数
        nChannelId = findFileArg.channel
        nRecordFileType = DH.EM_RECORD_TYPE_ALL
        tmStart = cls.datetime2DVR_Struct_TIME(findFileArg.startTime)
        tmEnd = cls.datetime2DVR_Struct_TIME(findFileArg.stopTime)

        structArray = DH.NET_RECORDFILE_INFO * 100
        nriFileinfo = structArray()

        nriFileinfo_ptr = cast(pointer(nriFileinfo[0]), DH.LPNET_RECORDFILE_INFO)

        maxlen = sizeof(structArray)
        filecount = c_int(0)

        pchCardid = None  # char * 空指针  char *pchCardid
        waittime = 2000
        byTime = True
        findFileResult = cls.sdkDll.CLIENT_QueryRecordFile(userID, nChannelId, nRecordFileType, byref(tmStart), byref(tmEnd),
                                                           pchCardid, nriFileinfo_ptr, maxlen, byref(filecount), waittime, byTime)
        cls.getLastError("CLIENT_QueryRecordFile", bool(findFileResult))
        return bool(filecount.value)

    @classmethod
    def stopDownLoadTimer(cls, downLoadHandle):
        nTotalSize = c_int(0)  # 下载的总长度，单位:KB
        nDownLoadSize = c_int(0)  # 已下载的长度，单位:KB

        getDownLoadPosResult = cls.sdkDll.CLIENT_GetDownloadPos(downLoadHandle, byref(nTotalSize), byref(nDownLoadSize))
        cls.getLastError("CLIENT_GetDownloadPos", bool(getDownLoadPosResult))
        logger.trace(f"下载ID {downLoadHandle} ,下载总长度 {nTotalSize.value}KB ,已下载长度 {nDownLoadSize.value}KB ")
        if nTotalSize.value == nDownLoadSize.value:
            logger.success(f"下载ID {downLoadHandle} 下载完成")
            stopGetFileResult = cls.sdkDll.CLIENT_StopDownload(downLoadHandle)
            cls.getLastError("CLIENT_StopDownload", stopGetFileResult)
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

        startDateTime = cls.datetime2DVR_Struct_TIME(downLoadArg.startTime)
        endDateTime = cls.datetime2DVR_Struct_TIME(downLoadArg.stopTime)

        # 开始下载。虽然是和抽象接口对齐了，但真正原因是海康没提供下载函数回调接口，顺势而为无伤大雅。
        pReserved = pointer(c_int(0))
        downLoadHandle = cls.sdkDll.CLIENT_DownloadByTimeEx(userID, channel, DH.EM_RECORD_TYPE_ALL, startDateTime, endDateTime, savedFileName,
                                                            DH.fTimeDownLoadPosCallBack(0), 0, DH.fDataCallBack(0), 0, pReserved)

        cls.getLastError("CLIENT_DownloadByTimeEx", bool(downLoadHandle))
        return downLoadHandle

    @classmethod
    def getLastError(cls, methodName: str, methodResult):
        logger.debug(f"{methodName}执行结果为 {type(methodResult)} {methodResult}")
        if methodResult == -1 or methodResult is False:
            cls.__getLastError()

    @classmethod
    def __getLastError(cls):
        errorIndex = cls.sdkDll.CLIENT_GetLastError() & 0x7fffffff
        errorText = ErrorCode[errorIndex]
        logger.error(f"{errorIndex} {errorText}")
        raise DHException(errorIndex, errorText)

    @classmethod
    def logout(cls, userID):
        logoutResult = cls.sdkDll.CLIENT_Logout(userID)
        logger.info(f"用户ID：{userID} 已登出")
        cls.getLastError("CLIENT_Logout", bool(logoutResult))

    @classmethod
    def cleanup(cls):
        cls.sdkDll.CLIENT_Cleanup()
        logger.info("SDK资源已释放")

    @classmethod
    def logopen(cls):
        """
        打开日志功能
        """
        log_info = DH.LOG_SET_PRINT_INFO()
        log_info.dwSize = sizeof(DH.LOG_SET_PRINT_INFO)
        log_info.bSetFilePath = 1
        log_info.szLogFilePath = os.path.join(os.getcwd(), 'dahua_sdk.log').encode('gbk')
        # log_info.cbSDKLogCallBack = SDKLogCallBack

        log_info = pointer(log_info)
        logOpenResult = cls.sdkDll.CLIENT_LogOpen(log_info)
        cls.getLastError("CLIENT_LogOpen", bool(logOpenResult))
        return logOpenResult

    @classmethod
    def logclose(cls):
        """
        关闭日志功能
        """
        logCloseResult = cls.sdkDll.CLIENT_LogClose()
        cls.getLastError("CLIENT_LogClose", bool(logCloseResult))
        return logCloseResult

    @staticmethod
    def datetime2DVR_Struct_TIME(timeArg: datetime):
        # 省事的时间类型转换,下载录像用的时间类型
        netTime = DH.NET_TIME()
        netTime.dwYear = timeArg.year
        netTime.dwMonth = timeArg.month
        netTime.dwDay = timeArg.day
        netTime.dwHour = timeArg.hour
        netTime.dwMinute = timeArg.minute
        netTime.dwSecond = timeArg.second
        return netTime
