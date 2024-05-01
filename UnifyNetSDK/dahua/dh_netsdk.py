import typing
from ctypes import *
from datetime import datetime
from pathlib import Path
from time import sleep

from loguru import logger

import UnifyNetSDK.dahua.dh_netsdk_wrapper as DH
from UnifyNetSDK.dahua.dh_netsdk_exception import DHNetSDKExceptionDict
from UnifyNetSDK.define import AbsNetSDK
from UnifyNetSDK.parameter import *


class DaHuaNetSDK(AbsNetSDK):
    netDll = DH  # netsdk.dll由ctypesgen中间层加载
    # 目前调用dll的函数都是cls.netdll.func的形式调用
    # 需要变量引用，Enum或者结构体之类的用了DH直接引用
    configDll = None
    playDll = None
    renderDll = None
    infraDll = None

    DH_TIME_ZONE = {
        DH.DH_TIME_ZONE_0: "GMT+00:00",
        DH.DH_TIME_ZONE_1: "GMT+01:00",
        DH.DH_TIME_ZONE_2: "GMT+02:00",
        DH.DH_TIME_ZONE_3: "GMT+03:00",
        DH.DH_TIME_ZONE_4: "GMT+03:30",
        DH.DH_TIME_ZONE_6: "GMT+04:00",
        DH.DH_TIME_ZONE_7: "GMT+05:00",
        DH.DH_TIME_ZONE_8: "GMT+05:30",
        DH.DH_TIME_ZONE_9: "GMT+05:45",
        DH.DH_TIME_ZONE_10: "GMT+06:00",
        DH.DH_TIME_ZONE_11: "GMT+06:30",
        DH.DH_TIME_ZONE_12: "GMT+07:00",
        DH.DH_TIME_ZONE_13: "GMT+08:00",
        DH.DH_TIME_ZONE_14: "GMT+09:00",
        DH.DH_TIME_ZONE_15: "GMT+09:30",
        DH.DH_TIME_ZONE_16: "GMT+10:00",
        DH.DH_TIME_ZONE_17: "GMT+11:00",
        DH.DH_TIME_ZONE_18: "GMT+12:00",
        DH.DH_TIME_ZONE_19: "GMT-13:00",
        DH.DH_TIME_ZONE_20: "GMT-01:00",
        DH.DH_TIME_ZONE_21: "GMT-02:00",
        DH.DH_TIME_ZONE_22: "GMT-03:00",
        DH.DH_TIME_ZONE_23: "GMT-03:30",
        DH.DH_TIME_ZONE_24: "GMT-04:00",
        DH.DH_TIME_ZONE_25: "GMT-05:00",
        DH.DH_TIME_ZONE_26: "GMT-06:00",
        DH.DH_TIME_ZONE_27: "GMT-07:00",
        DH.DH_TIME_ZONE_28: "GMT-08:00",
        DH.DH_TIME_ZONE_29: "GMT-09:00",
        DH.DH_TIME_ZONE_30: "GMT-10:00",
        DH.DH_TIME_ZONE_31: "GMT-11:00",
        DH.DH_TIME_ZONE_32: "GMT-12:00"

    }

    def __init__(self):
        pass
        # self._loadLibrary()
        # self.setArgTypes_ResType()

    def setArgTypes_ResType(self):
        # 有时候ctypesgen把握不住，就需要手动设置函数的形参类型和返回值类型，目前是弃用的
        self.netDll.CLIENT_LoginWithHighLevelSecurity.argtypes = [POINTER(DH.NET_IN_LOGIN_WITH_HIGHLEVEL_SECURITY), POINTER(DH.NET_OUT_LOGIN_WITH_HIGHLEVEL_SECURITY)]
        self.netDll.CLIENT_LoginWithHighLevelSecurity.restype = c_longlong
        self.netDll.CLIENT_QueryRecordFile.argtypes = [c_longlong, c_int, c_int, DH.LPNET_TIME, DH.LPNET_TIME, DH.String, DH.LPNET_RECORDFILE_INFO, c_int, POINTER(c_int), c_int, c_int]
        self.netDll.CLIENT_QueryRecordFile.restype = c_int
        self.netDll.CLIENT_DownloadByTimeEx.argtypes = [c_longlong, c_int, c_int, DH.LPNET_TIME, DH.LPNET_TIME, DH.String, DH.fTimeDownLoadPosCallBack, c_long, DH.fDataCallBack, c_long, POINTER(None)]
        self.netDll.CLIENT_DownloadByTimeEx.restype = c_longlong
        self.netDll.CLIENT_Logout.argtypes = [c_longlong]
        self.netDll.CLIENT_Logout.restype = c_int
        self.netDll.CLIENT_GetDownloadPos.argtypes = [c_longlong, POINTER(c_int), POINTER(c_int)]
        self.netDll.CLIENT_GetDownloadPos.restype = c_int
        self.netDll.CLIENT_StopDownload.argtypes = [c_longlong]
        self.netDll.CLIENT_StopDownload.restype = c_int
        self.netDll.CLIENT_RealPlayEx.argtypes = [c_longlong, c_int, POINTER(None), DH.DH_RealPlayType]
        self.netDll.CLIENT_RealPlayEx.restype = c_longlong
        self.netDll.CLIENT_PlayBackByTimeEx.argtypes = [c_longlong, c_int, DH.LPNET_TIME, DH.LPNET_TIME, POINTER(None), DH.fDownLoadPosCallBack, c_long, DH.fDataCallBack, c_long]
        self.netDll.CLIENT_PlayBackByTimeEx.restype = c_longlong

    @classmethod
    def init(cls) -> bool:
        initResult = cls.netDll.CLIENT_InitEx(DH.fDisConnect(0), 0, DH.NETSDK_INIT_PARAM())
        logger.info(f"SDK初始化已执行")
        cls.getLastError("CLIENT_InitEx", bool(initResult))
        return bool(initResult)

    @classmethod
    def _loadLibrary(cls):  # 未使用
        try:
            curPyPath = Path(__file__).parent
            libPath = curPyPath / "Libs/win64"
            cls.netDll = windll.LoadLibrary(str(libPath / "dhnetsdk.dll"))
            cls.configDll = windll.LoadLibrary(str(libPath / "dhconfigsdk.dll"))
            cls.renderDll = windll.LoadLibrary(str(libPath / "RenderEngine.dll"))
            cls.infraDll = windll.LoadLibrary(str(libPath / "Infra.dll"))
            cls.playDll = windll.LoadLibrary(str(libPath / "dhplay.dll"))
        except OSError as e:
            logger.error(f"动态库加载失败,原错误信息:{e}")
            # logger.exception(e)

    @classmethod
    def getTime_CFG(cls, userID: int) -> datetime:
        # 获取设备时间
        lChannel = 0
        dwOutBufferSize = sizeof(DH.NET_TIME)
        lpOutBuffer = DH.NET_TIME()
        lpBytesReturned = c_ulong()
        waittime = 1000
        result = cls.netDll.CLIENT_GetDevConfig(userID, DH.DH_DEV_TIMECFG, lChannel, byref(lpOutBuffer), dwOutBufferSize, byref(lpBytesReturned), waittime)
        cls.getLastError("CLIENT_GetDevConfig__DH_DEV_TIMECFG", bool(result))
        pyTime = cls.DVR_Struct_Time2Datetime(lpOutBuffer)
        return pyTime

    @classmethod
    def setTime_CFG(cls, userID: int, pyTime: datetime) -> bool:
        # 设置设备时间
        lChannel = 0
        dwOutBufferSize = sizeof(DH.NET_TIME)
        lpOutBuffer = cls.datetime2DVR_Struct_TIME(pyTime)
        waittime = 1000
        result = cls.netDll.CLIENT_SetDevConfig(userID, DH.DH_DEV_TIMECFG, lChannel, byref(lpOutBuffer), dwOutBufferSize, waittime)
        cls.getLastError("CLIENT_SetDevConfig__DH_DEV_TIMECFG", bool(result))
        return bool(result)

    @classmethod
    def getNTP_CFG(cls, userID: int) -> UninfyNTPArg:
        # 获取设备NTP配置
        lChannel = 0
        dwOutBufferSize = sizeof(DH.DHDEV_NTP_CFG)
        lpOutBuffer = DH.DHDEV_NTP_CFG()
        lpBytesReturned = c_ulong()
        waittime = 1000
        result = cls.netDll.CLIENT_GetDevConfig(userID, DH.DH_DEV_NTP_CFG, lChannel, byref(lpOutBuffer), dwOutBufferSize, byref(lpBytesReturned), waittime)
        cls.getLastError("CLIENT_GetDevConfig__DH_DEV_NTP_CFG", bool(result))

        ntpArg = UninfyNTPArg()
        ntpArg.enable = bool(lpOutBuffer.bEnable)

        t_szHostIp = bytes(lpOutBuffer.szHostIp).decode('utf-8')
        t_szDomainName = bytes(lpOutBuffer.szDomainName).decode('utf-8')
        if lpOutBuffer.nType == 0:
            ntpArg.domainOrIP = t_szHostIp  # 这个szHostIp可能零几年的遗留参数吧，现在没被用了
        elif lpOutBuffer.nType == 1:
            ntpArg.domainOrIP = t_szDomainName
        elif lpOutBuffer.nType == 2:
            ntpArg.domainOrIP = t_szHostIp + " 左IP右域名 " + t_szDomainName

        ntpArg.port = lpOutBuffer.nHostPort
        ntpArg.updateInterval = lpOutBuffer.nUpdateInterval
        ntpArg.timeZone = cls.DH_TIME_ZONE[lpOutBuffer.nTimeZone]

        return ntpArg

    @classmethod
    def setNTP_CFG(cls, userID: int, ntpArg: UninfyNTPArg) -> bool:
        # 设置设备NTP配置
        lChannel = 0
        dwOutBufferSize = sizeof(DH.DHDEV_NTP_CFG)
        lpInBuffer = DH.DHDEV_NTP_CFG()
        waittime = 1000
        lpInBuffer.bEnable = ntpArg.enable
        lpInBuffer.szDomainName = ntpArg.domainOrIP.encode('utf-8')
        # lpInBuffer.szHostIp 这个参数不起ip和域名分设的作用，文档说 主机IP
        lpInBuffer.nHostPort = ntpArg.port
        lpInBuffer.nUpdateInterval = ntpArg.updateInterval
        dongBaTimeZone = DH.DH_TIME_ZONE_13
        lpInBuffer.nTimeZone = dongBaTimeZone if ntpArg.timeZone is None else ntpArg.timeZone  # 用户不传时间区，默认东八区

        result = cls.netDll.CLIENT_SetDevConfig(userID, DH.DH_DEV_NTP_CFG, lChannel, byref(lpInBuffer), dwOutBufferSize, waittime)
        cls.getLastError("CLIENT_SetDevConfig__DH_DEV_NTP_CFG", bool(result))

        MustRuningResult = cls.getNTP_CFG(userID)
        logger.debug(f"设置NTP参数后，需要再次获取NTP参数才能在前端中看到结果，结果为{MustRuningResult}")
        cls.getLastError("CLIENT_GetDevConfig__DH_DEV_NTP_CFG", bool(MustRuningResult))
        if result and MustRuningResult:
            return True
        else:
            return False

    @classmethod
    def realPlay(cls, userID: int, channel: int, hwnd) -> int:
        """
        hwnd只需要从QtWidgets.QWidget.winId()获取即可,转换均有sdk这边来做
        """
        valid_hwnd = cast(c_void_p(int(hwnd)), c_void_p)
        # realPlayHandle = cls.sdkDll.CLIENT_RealPlayEx(userID, channel, valid_hwnd, DH.DH_RType_Realplay)
        realPlayHandle = cls.netDll.CLIENT_RealPlayEx(userID, channel, valid_hwnd, DH.DH_RType_Multiplay_4)
        cls.getLastError("CLIENT_RealPlayEx", bool(realPlayHandle))
        return realPlayHandle

    @classmethod
    def stopRealPlay(cls, realPlayHandle: int) -> bool:
        # 停止实时预览
        stopRealPlayResult = cls.netDll.CLIENT_StopRealPlay(realPlayHandle)
        cls.getLastError("CLIENT_StopRealPlayEx", bool(stopRealPlayResult))
        return bool(stopRealPlayResult)

    @classmethod
    def playBackByTime(cls, userID: int, playBackArg: UnifyPlayBackByTimeArg) -> int:
        # 按照时间参数进行回放
        channel = playBackArg.channel
        startDateTime = cls.datetime2DVR_Struct_TIME(playBackArg.startTime)
        endDateTime = cls.datetime2DVR_Struct_TIME(playBackArg.stopTime)
        valid_hwnd = cast(c_void_p(int(playBackArg.hwnd)), c_void_p)
        downloadPosCallBack = DH.fDownLoadPosCallBack(0) if playBackArg.downLoadPosCallBack is None else playBackArg.downLoadPosCallBack
        dwPosUser = 0 if playBackArg.dwPosUser is None else playBackArg.dwPosUser
        dataCallBack = DH.fDataCallBack(0) if playBackArg.dataCallBack is None else playBackArg.dataCallBack
        dwDataUser = 0 if playBackArg.dwDataUser is None else playBackArg.dwDataUser
        playBackHandle = cls.netDll.CLIENT_PlayBackByTimeEx(userID, channel, byref(startDateTime), byref(endDateTime), valid_hwnd, downloadPosCallBack, dwPosUser, dataCallBack, dwDataUser)
        cls.getLastError("CLIENT_PlayBackByTimeEx", bool(playBackHandle))
        return playBackHandle

    @classmethod
    def stopPlayBack(cls, playBackHandle: int) -> bool:
        # 停止回放
        stopPlayBackResult = cls.netDll.CLIENT_StopPlayBack(playBackHandle)
        cls.getLastError("CLIENT_StopPlayBack", bool(stopPlayBackResult))
        return bool(stopPlayBackResult)

    @classmethod
    def catchPicture(cls, lPlayHandle: int, savedFileName: str) -> bool:
        # 抓图，可以是实时预览或是回放函数的返回的句柄，
        # 重中之重的是这两个函数的hwnd必须是有效的
        catchResult = cls.netDll.CLIENT_CapturePictureEx(lPlayHandle, savedFileName, DH.NET_CAPTURE_JPEG_70)
        cls.getLastError("CLIENT_CapturePictureEx", bool(catchResult))
        return bool(catchResult)

    @classmethod
    def login(cls, loginArg: UnifyLoginArg) -> (int, DH.NET_OUT_LOGIN_WITH_HIGHLEVEL_SECURITY):
        # 登录参数，包括设备地址、登录用户、密码等
        loginInfo = DH.NET_IN_LOGIN_WITH_HIGHLEVEL_SECURITY()
        loginInfo.dwSize = sizeof(DH.NET_IN_LOGIN_WITH_HIGHLEVEL_SECURITY)
        loginInfo.szIP = loginArg.deviceAddress.encode()
        loginInfo.nPort = loginArg.devicePort
        loginInfo.szUserName = loginArg.userName.encode()
        loginInfo.szPassword = loginArg.userPassword.encode()
        loginInfo.emSpecCap = DH.EM_LOGIN_SPEC_CAP_TCP

        # 设备信息, 输出参数
        deviceInfo = DH.NET_OUT_LOGIN_WITH_HIGHLEVEL_SECURITY()
        deviceInfo.dwSize = sizeof(DH.NET_OUT_LOGIN_WITH_HIGHLEVEL_SECURITY)

        cls.netDll.CLIENT_LoginWithHighLevelSecurity.restype = c_longlong
        login_id = cls.netDll.CLIENT_LoginWithHighLevelSecurity(byref(loginInfo), byref(deviceInfo))
        cls.getLastError("CLIENT_LoginWithHighLevelSecurity", bool(login_id))
        return login_id, deviceInfo

    @classmethod
    def syncFindFileByTime(cls, userID: int, findFileArg: UnifyFindFileByTimeArg) -> bool:  # 大华的sdk，能通过时间查询的就这一个方法，且没有返回给我查找句柄，所以大华这边只能有sync了
        # 同步阻塞 按照时间查找录像文件是否存在
        return cls.__findFileByTime(userID, findFileArg)  # CLIENT_FindFileEx能返回句柄，但不能按照时间查询

    @classmethod
    def __findFileByTime(cls, userID: int, findFileArg: UnifyFindFileByTimeArg) -> bool:
        # 按照时间查找录像文件是否存在
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
        findFileResult = cls.netDll.CLIENT_QueryRecordFile(userID, nChannelId, nRecordFileType, byref(tmStart), byref(tmEnd), pchCardid, nriFileinfo_ptr, maxlen, byref(filecount), waittime, byTime)
        cls.getLastError("CLIENT_QueryRecordFile", bool(findFileResult))
        return bool(filecount.value)

    @classmethod
    def stopDownLoadTimer(cls, downLoadHandle: int) -> bool:
        # 内部实现的 关闭下载句柄 的类方法
        nTotalSize = c_int(0)  # 下载的总长度，单位:KB
        nDownLoadSize = c_int(0)  # 已下载的长度，单位:KB

        getDownLoadPosResult = cls.netDll.CLIENT_GetDownloadPos(downLoadHandle, byref(nTotalSize), byref(nDownLoadSize))
        cls.getLastError("CLIENT_GetDownloadPos", bool(getDownLoadPosResult))
        logger.trace(f"下载ID {downLoadHandle} ,下载总长度 {nTotalSize.value}KB ,已下载长度 {nDownLoadSize.value}KB ")
        if nTotalSize.value == nDownLoadSize.value:
            logger.success(f"下载ID {downLoadHandle} 下载完成")
            stopGetFileResult = cls.netDll.CLIENT_StopDownload(downLoadHandle)
            cls.getLastError("CLIENT_StopDownload", bool(stopGetFileResult))
            return True
        else:
            return False

    @classmethod
    def syncDownLoadByTime(cls, userID: int, downLoadArg: UnifyDownLoadByTimeArg) -> bool:
        # 同步阻塞，按照时间参数下载录像
        downLoadHandle = cls.__downLoadByTime(userID, downLoadArg)
        while True:
            downLoadResult = cls.stopDownLoadTimer(downLoadHandle)  # 每0.5秒查一下有没有下载完成
            if downLoadResult is True:
                return bool(downLoadResult)
            sleep(1)

    @classmethod
    def asyncDownLoadByTime(cls, userID: int, downLoadArg: UnifyDownLoadByTimeArg) -> int:
        # 异步，按照时间参数下载录像，句柄由用户关闭
        downLoadHandle = cls.__downLoadByTime(userID, downLoadArg)
        return downLoadHandle

    @classmethod
    def __downLoadByTime(cls, userID: int, downLoadArg: UnifyDownLoadByTimeArg) -> int:
        # 按照时间参数下载录像文件的底层方法
        logger.info(f"下载文件路径为{downLoadArg.saveFilePath}")
        savedFileName = create_string_buffer(str(downLoadArg.saveFilePath).encode("gbk"))
        channel = downLoadArg.channel

        startDateTime = cls.datetime2DVR_Struct_TIME(downLoadArg.startTime)
        endDateTime = cls.datetime2DVR_Struct_TIME(downLoadArg.stopTime)

        # 开始下载。虽然是和抽象接口对齐了，但真正原因是海康没提供下载函数回调接口，顺势而为无伤大雅。
        pReserved = pointer(c_int(0))
        downLoadHandle = cls.netDll.CLIENT_DownloadByTimeEx(userID, channel, DH.EM_RECORD_TYPE_ALL, startDateTime, endDateTime, savedFileName,
                                                            DH.fTimeDownLoadPosCallBack(0), 0, DH.fDataCallBack(0), 0, pReserved)

        cls.getLastError("CLIENT_DownloadByTimeEx", bool(downLoadHandle))
        return downLoadHandle

    @classmethod
    def getLastError(cls, methodName: str, methodResult: typing.Union[int, bool]) -> None:
        # 获取错误码，就算没有错误也会被 raise NO_ERROR
        logger.debug(f"{methodName}执行结果为 {type(methodResult)} {methodResult}")
        if methodResult == -1 or methodResult is False:
            cls._getLastError()

    @classmethod
    def _getLastError(cls) -> None:
        # 获取错误码的底层实现
        errorIndex = cls.netDll.CLIENT_GetLastError() & 0x7fffffff
        try:
            exception = DHNetSDKExceptionDict[errorIndex]
        except IndexError:
            logger.error(f"{errorIndex} 未知错误")
            raise Exception("未知错误")
        logger.error(f"{errorIndex} {exception}")
        raise exception

    @classmethod
    def logout(cls, userID: int) -> bool:
        # 登出
        logoutResult = cls.netDll.CLIENT_Logout(userID)
        logger.info(f"用户ID：{userID} 已登出")
        cls.getLastError("CLIENT_Logout", bool(logoutResult))
        return bool(logoutResult)

    @classmethod
    def cleanup(cls) -> bool:
        # 释放资源
        cls.netDll.CLIENT_Cleanup()  # 没有返回值
        logger.info("SDK资源已释放")
        return True  # 但是还是要做厂商SDK返回值对齐

    @classmethod
    def logopen(cls, absLogPath: str) -> bool:
        # 打开日志功能
        log_info = DH.LOG_SET_PRINT_INFO()
        log_info.dwSize = sizeof(DH.LOG_SET_PRINT_INFO)
        log_info.bSetFilePath = True
        log_info.szLogFilePath = str(absLogPath).encode('gbk')
        log_info.bSetFileNum = True  # 设置log数量仅保留一个，默认大小是10240kb
        log_info.nFileNum = 1
        # log_info.cbSDKLogCallBack = SDKLogCallBack

        log_info = pointer(log_info)
        logOpenResult = cls.netDll.CLIENT_LogOpen(log_info)
        cls.getLastError("CLIENT_LogOpen", bool(logOpenResult))
        return bool(logOpenResult)

    @classmethod
    def logclose(cls) -> bool:
        # 关闭日志功能
        logCloseResult = cls.netDll.CLIENT_LogClose()
        cls.getLastError("CLIENT_LogClose", bool(logCloseResult))
        return bool(logCloseResult)

    @staticmethod
    def datetime2DVR_Struct_TIME(timeArg: datetime) -> DH.NET_TIME:
        # 省事的时间类型转换,下载录像用的时间类型
        netTime = DH.NET_TIME()
        netTime.dwYear = timeArg.year
        netTime.dwMonth = timeArg.month
        netTime.dwDay = timeArg.day
        netTime.dwHour = timeArg.hour
        netTime.dwMinute = timeArg.minute
        netTime.dwSecond = timeArg.second
        return netTime

    @staticmethod
    def DVR_Struct_Time2Datetime(timeArg: DH.NET_TIME) -> datetime:
        # 大华时间类型转换成datetime类型
        pyTime = datetime(timeArg.dwYear, timeArg.dwMonth, timeArg.dwDay, timeArg.dwHour, timeArg.dwMinute, timeArg.dwSecond)
        return pyTime
