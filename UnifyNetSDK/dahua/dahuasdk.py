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
    sdkDll = DH  # 目前只加载了UnifyNetSDK/dahua/Libs/win64/dhnetsdk.dll，并且是由！！！DH！！！那边加载的
    configDll = None
    playDll = None
    renderDll = None
    infraDll = None

    def __init__(self):
        pass

    @classmethod
    def init(cls):
        initResult = cls.sdkDll.CLIENT_InitEx(DH.fDisConnect(0), 0, DH.NETSDK_INIT_PARAM())
        logger.info(f"SDK初始化已执行")
        cls.__getLastError("CLIENT_InitEx", bool(initResult))

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

        login_id = cls.sdkDll.CLIENT_LoginWithHighLevelSecurity(byref(loginInfo), byref(deviceInfo))
        cls.__getLastError("CLIENT_LoginWithHighLevelSecurity", bool(login_id))
        return login_id, deviceInfo

    @classmethod
    def syncFindFileByTime(cls, userID, findFileArg: UnifyFindFileByTimeArg):  # 大华的sdk，能通过时间查询的就这一个方法，且没有返回给我查找句柄，所以大华这边只能有sync了
        return cls.__findFileByTime(userID, findFileArg)  # CLIENT_FindFileEx能返回句柄，但不能按照时间查询

    @classmethod
    def __findFileByTime(cls, userID, findFileArg: UnifyFindFileByTimeArg):
        # 准备参数
        nChannelId = findFileArg.channel
        nRecordFileType = DH.EM_RECORD_TYPE_ALL
        tmStart = cls.datetime2NET_TIME(findFileArg.startTime)
        tmEnd = cls.datetime2NET_TIME(findFileArg.stopTime)

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
        cls.__getLastError("CLIENT_QueryRecordFile", bool(findFileResult))
        return nriFileinfo, filecount.value

    @classmethod
    def stopDownLoadTimer(cls, downLoadHandle: int):
        nTotalSize = c_int(0)  # 下载的总长度，单位:KB
        nDownLoadSize = c_int(0)  # 已下载的长度，单位:KB

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
        pReserved = pointer(c_int(0))
        downLoadHandle = cls.sdkDll.CLIENT_DownloadByTimeEx(userID, channel, DH.EM_RECORD_TYPE_ALL, startDateTime, endDateTime, savedFileName,
                                                            DH.fTimeDownLoadPosCallBack(0), 0, DH.fDataCallBack(0), 0, pReserved)

        cls.__getLastError("CLIENT_DownloadByTimeEx", bool(downLoadHandle))
        return downLoadHandle

    @classmethod
    def __getLastError(cls, methodName: str, methodResult):  # todo 如果这种写法能用的话记得加到define里
        logger.debug(f"{methodName}执行结果为 {type(methodResult)} {methodResult}")
        if methodResult == -1 or methodResult is False:
            errorIndex = cls.sdkDll.CLIENT_GetLastError() & 0x7fffffff
            errorText = ErrorCode[errorIndex]
            logger.error(f"{errorIndex} {errorText}")
            raise DHException(errorIndex, errorText)

    @classmethod
    def logout(cls, userID):
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
