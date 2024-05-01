import typing
from ctypes import *
from pathlib import Path
from time import sleep

from loguru import logger

import UnifyNetSDK.haikang.hk_netsdk_wrapper as HK
from UnifyNetSDK.define import *
from UnifyNetSDK.haikang.hk_netsdk_exception import HKNetSDKExceptionDict
from UnifyNetSDK.parameter import *

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


class HaikangNetSDK(AbsNetSDK):
    netDll = None
    # 目前调用dll的函数都是cls.netdll.func的形式调用
    # 需要变量引用，Enum或者结构体之类的用了DH直接引用
    # 海康跟大华又不相同了，海康还必须做一个NET_DVR_SetSDKInitCfg，
    # 所以 如果_loadLibrary执行失败那所有的classmethod都会(报错?)
    playDll = None

    def __init__(self):
        self._loadLibrary()

    @classmethod
    def init(cls) -> bool:
        initResult = cls.netDll.NET_DVR_Init()
        logger.info(f"SDK初始化已执行")
        cls.getLastError("NET_DVR_Init", bool(initResult))
        return bool(initResult)

    @classmethod
    def _loadLibrary(cls):
        try:
            curPyPath = Path(__file__).parent
            libPath = curPyPath / "lib/win"
            # cls.netDll = CDLL(str(libPath / "HCNetSDK.dll"))  # 加载网络库
            cls.netDll = HK  # hcnetsdk.dll由ctypesgen中间层加载
            # cls.playctrlDll = CDLL(str(libPath / 'PlayCtrl.dll'))  # 加载播放库。其他库需要再制作头文件的

            sdk_ComPath = HK.NET_DVR_LOCAL_SDK_PATH()
            sdk_ComPath.sPath = str(libPath).encode("gbk")
            setResult = cls.netDll.NET_DVR_SetSDKInitCfg(2, byref(sdk_ComPath))
            cls.getLastError("NET_DVR_SetSDKInitCfg", bool(setResult))
            libcryptoPath = str(libPath / "libcrypto-1_1-x64.dll").encode("gbk")
            setResult = cls.netDll.NET_DVR_SetSDKInitCfg(3, create_string_buffer(libcryptoPath))
            cls.getLastError("NET_DVR_SetSDKInitCfg", bool(setResult))
            libsslPath = str(libPath / "libssl-1_1-x64.dll").encode("gbk")
            setResult = cls.netDll.NET_DVR_SetSDKInitCfg(4, create_string_buffer(libsslPath))
            cls.getLastError("NET_DVR_SetSDKInitCfg", bool(setResult))

        except OSError as e:
            logger.error(f"动态库加载失败,原错误信息:{e}")
            # logger.exception(e)

    @classmethod
    def getTime_CFG(cls, userID: int) -> datetime:
        lChannel = 0
        dwOutBufferSize = sizeof(HK.NET_DVR_TIME)
        lpOutBuffer = HK.NET_DVR_TIME()
        lpBytesReturned = c_ulong()

        result = cls.netDll.NET_DVR_GetDVRConfig(userID, HK.NET_DVR_GET_TIMECFG, lChannel, byref(lpOutBuffer), dwOutBufferSize, byref(lpBytesReturned))
        cls.getLastError("NET_DVR_GetDVRConfig__NET_DVR_GET_TIMECFG", bool(result))
        pyTime = cls.DVR_Struct_Time2Datetime(lpOutBuffer)
        return pyTime

    @classmethod
    def setTime_CFG(cls, userID: int, pyTime: datetime) -> bool:
        lChannel = 0
        dwOutBufferSize = sizeof(HK.NET_DVR_TIME)
        lpOutBuffer = cls.datetime2DVR_Struct_TIME(pyTime)
        result = cls.netDll.NET_DVR_SetDVRConfig(userID, HK.NET_DVR_SET_TIMECFG, lChannel, byref(lpOutBuffer), dwOutBufferSize)
        cls.getLastError("NET_DVR_SetDVRConfig__NET_DVR_SET_TIMECFG", bool(result))
        return bool(result)

    @classmethod
    def getNTP_CFG(cls, userID: int) -> UninfyNTPArg:
        lChannel = 0
        dwOutBufferSize = sizeof(HK.NET_DVR_NTPPARA)
        lpOutBuffer = HK.NET_DVR_NTPPARA()
        lpBytesReturned = c_ulong()

        result = cls.netDll.NET_DVR_GetDVRConfig(userID, HK.NET_DVR_GET_NTPCFG, lChannel, byref(lpOutBuffer), dwOutBufferSize, byref(lpBytesReturned))
        cls.getLastError("NET_DVR_GetDVRConfig__NET_DVR_GET_NTPCFG", bool(result))

        ntpArg = UninfyNTPArg()
        ntpArg.enable = bool(lpOutBuffer.byEnableNTP)

        server_bytes = bytes(lpOutBuffer.sNTPServer)
        server_text = server_bytes.decode('utf-8').rstrip('\x00')

        ntpArg.domainOrIP = server_text
        ntpArg.port = lpOutBuffer.wNtpPort
        ntpArg.updateInterval = lpOutBuffer.wInterval
        difference_h = int.from_bytes(lpOutBuffer.cTimeDifferenceH, byteorder='big', signed=True)
        sign = '+' if difference_h >= 0 else '-'  # 确定符号
        difference_m = int.from_bytes(lpOutBuffer.cTimeDifferenceM, byteorder='big', signed=True)
        ntpArg.timeZone = f"GMT{sign}{abs(difference_h):02d}:{difference_m:0>2d}"  # # 数字补零 (填充左边, 宽度为2)
        return ntpArg

    @classmethod
    def setNTP_CFG(cls, userID: int, ntpArg: UninfyNTPArg) -> bool:
        # 注意，如果想修改时区为非默认东八区，ntpArg.timeZone被处理为一个列表，第一元素为小时，第二元素为分钟。元素类型为int
        lChannel = 0
        dwOutBufferSize = sizeof(HK.NET_DVR_NTPPARA)
        lpOutBuffer = HK.NET_DVR_NTPPARA()
        lpOutBuffer.byEnableNTP = ntpArg.enable

        ba = bytearray(ntpArg.domainOrIP.encode('utf-8'))
        lpOutBuffer.sNTPServer = (c_ubyte * 64)(*ba)

        lpOutBuffer.wNtpPort = ntpArg.port
        lpOutBuffer.wInterval = ntpArg.updateInterval

        lpOutBuffer.cTimeDifferenceH = (8).to_bytes(1, byteorder='big')  # 默认 东八区，正八
        lpOutBuffer.cTimeDifferenceM = (0).to_bytes(1, byteorder='big')  # b'\x08' b'\x00' 十六进制的

        if ntpArg.timeZone is not None:
            lpOutBuffer.cTimeDifferenceH = ntpArg.timeZone[0].to_bytes(1, byteorder='big')
            lpOutBuffer.cTimeDifferenceM = ntpArg.timeZone[1].to_bytes(1, byteorder='big')

        result = cls.netDll.NET_DVR_SetDVRConfig(userID, HK.NET_DVR_SET_NTPCFG, lChannel, byref(lpOutBuffer), dwOutBufferSize)
        cls.getLastError("NET_DVR_SetDVRConfig__NET_DVR_SET_NTPCFG", bool(result))
        return bool(result)

    @classmethod
    def login(cls, loginArg: UnifyLoginArg) -> (int, HK.NET_DVR_USER_LOGIN_INFO):
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
        userID = cls.netDll.NET_DVR_Login_V40(loginInfo, byref(deviceInfo))
        cls.getLastError("NET_DVR_Login_V40", int(userID))
        return userID, deviceInfo

    @classmethod
    def stopFindFileTimer(cls, findHandle: int) -> int:

        lpFindData = HK.NET_DVR_FINDDATA_V50()  # 这是一个out参数，用来接收文件查找结果信息的
        findResult = cls.netDll.NET_DVR_FindNextFile_V50(findHandle, byref(lpFindData))
        cls.getLastError("NET_DVR_FindNextFile_V50", int(findResult))

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
            stopFindResult = cls.netDll.NET_DVR_FindClose_V30(findHandle)
            cls.getLastError("NET_DVR_FindClose_V30", bool(stopFindResult))
            return True
        elif findResult in findStateList:
            logger.error(f"查找ID {findHandle},查找状态异常代码 {findResult},{findStateList[findResult]}")
            stopFindResult = cls.netDll.NET_DVR_FindClose_V30(findHandle)
            cls.getLastError("NET_DVR_FindClose_V30", bool(stopFindResult))
        return findResult

    @classmethod
    def syncFindFileByTime(cls, userID: int, findFileArg: UnifyFindFileByTimeArg) -> bool:
        """
        成功返回True
        失败返回False
        """
        findHandle = cls.__findFileByTime(userID, findFileArg)
        while True:
            findResult = cls.stopFindFileTimer(findHandle)
            if findResult != HK.NET_DVR_ISFINDING:  #
                if findResult is True:  # 大华和海康这部分功能的实现真是花开两朵各表一枝啊
                    return True  # 我统一了一下
                else:  # 找到了就True，没找到我底层这边打印个错误代码就行
                    return False
            sleep(0.5)

    @classmethod
    def asyncFindFileByTime(cls, userID: int, findFileArg: UnifyFindFileByTimeArg) -> int:
        findHandle = cls.__findFileByTime(userID, findFileArg)
        return findHandle

    @classmethod
    def __findFileByTime(cls, userID: int, findFileArg: UnifyFindFileByTimeArg) -> int:
        # 准备参数
        struStreamID = HK.NET_DVR_STREAM_INFO()
        struStreamID.dwSize = sizeof(HK.NET_DVR_STREAM_INFO)
        struStreamID.dwChannel = findFileArg.channel

        pFindCond = HK.NET_DVR_FILECOND_V50()
        pFindCond.struStreamID = struStreamID
        pFindCond.struStartTime = cls.datetime2NET_DVR_TIME_SEARCH_COND(findFileArg.startTime)
        pFindCond.struStopTime = cls.datetime2NET_DVR_TIME_SEARCH_COND(findFileArg.stopTime)

        # 开始查询
        findHandle = cls.netDll.NET_DVR_FindFile_V50(userID, pFindCond)
        cls.getLastError("NET_DVR_FindFile_V50", int(findHandle))

        return findHandle

    @classmethod
    def stopDownLoadTimer(cls, downLoadHandle: int) -> int:
        downLoadPos = c_int()
        lpOutLen = c_ulong(0)
        controlResult = cls.netDll.NET_DVR_PlayBackControl_V40(downLoadHandle, HK.NET_DVR_PLAYGETPOS, c_void_p(), 0, byref(downLoadPos), byref(lpOutLen))
        cls.getLastError("NET_DVR_PlayBackControl_V40", bool(controlResult))

        logger.trace(f"下载ID {downLoadHandle},下载状态 {downLoadPos.value}")
        if downLoadPos.value == 100:
            logger.success(f"下载ID {downLoadHandle} 下载成功")
            stopGetFileResult = cls.netDll.NET_DVR_StopGetFile(downLoadHandle)
            cls.getLastError("NET_DVR_StopGetFile", bool(stopGetFileResult))
        elif downLoadPos.value == 200:
            logger.error(f"下载ID {downLoadHandle} 下载异常")
            stopGetFileResult = cls.netDll.NET_DVR_StopGetFile(downLoadHandle)
            cls.getLastError("NET_DVR_StopGetFile", bool(stopGetFileResult))
        return downLoadPos.value

    @classmethod
    def syncDownLoadByTime(cls, userID: int, downLoadArg: UnifyDownLoadByTimeArg) -> bool:
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
    def asyncDownLoadByTime(cls, userID: int, downLoadArg: UnifyDownLoadByTimeArg):
        downLoadHandle = cls.__downLoadByTime(userID, downLoadArg)
        return downLoadHandle

    @classmethod
    def __downLoadByTime(cls, userID: int, downLoadArg: UnifyDownLoadByTimeArg) -> int:
        # 准备参数
        logger.info(f"下载文件路径为{downLoadArg.saveFilePath}")
        sSavedFileName = create_string_buffer(str(downLoadArg.saveFilePath).encode("gbk"))
        pDownloadCond = HK.NET_DVR_PLAYCOND()
        pDownloadCond.dwChannel = downLoadArg.channel
        pDownloadCond.struStartTime = cls.datetime2DVR_Struct_TIME(downLoadArg.startTime)
        pDownloadCond.struStopTime = cls.datetime2DVR_Struct_TIME(downLoadArg.stopTime)
        # 开始下载
        downLoadHandle = cls.netDll.NET_DVR_GetFileByTime_V40(userID, sSavedFileName, byref(pDownloadCond))
        cls.getLastError("NET_DVR_GetFileByTime_V40", int(downLoadHandle))

        controlResult = cls.netDll.NET_DVR_PlayBackControl_V40(downLoadHandle, HK.NET_DVR_PLAYSTART, c_void_p(), 0, c_void_p(), byref(c_ulong(0)))
        cls.getLastError("NET_DVR_PlayBackControl_V40", bool(controlResult))

        return downLoadHandle

    @classmethod  # 目前认为海康把两种状态作为方法执行错位的标识，-1和False，其他的都是正常值，不过我怕它整个新花样，如果能在这个方法中指定错误值，哦。。。那就需要白名单和黑名单了。。。。。。。。。。
    def getLastError(cls, methodName: str, methodResult: typing.Union[int, bool]) -> None:  # todo 如果这种写法能用的话记得加到define里
        logger.debug(f"{methodName}执行结果为 {type(methodResult)} {methodResult}")
        if methodResult == -1 or methodResult is False:
            cls.__getLastError()

    @classmethod
    def __getLastError(cls) -> None:
        errorIndex = cls.netDll.NET_DVR_GetLastError()
        try:
            exception = HKNetSDKExceptionDict[errorIndex]
        except IndexError:
            logger.error(f"{errorIndex} 未知错误")
            raise Exception("未知错误")
        logger.error(f"{errorIndex} {exception}")
        raise exception

    @classmethod
    def logout(cls, userID: int) -> bool:
        logoutResult = cls.netDll.NET_DVR_Logout(userID)
        logger.info(f"用户ID：{userID} 已登出")
        cls.getLastError("NET_DVR_Logout", bool(logoutResult))
        return bool(logoutResult)

    @classmethod
    def cleanup(cls) -> bool:
        cleanupResult = cls.netDll.NET_DVR_Cleanup()
        logger.info("SDK资源已释放")
        cls.getLastError("NET_DVR_Cleanup", bool(cleanupResult))
        return bool(cleanupResult)

    @classmethod
    def logopen(cls, absLogPath: str) -> bool:
        """
        打开日志功能
        """

        # 设置log数量仅保留一个，手册没说默认大小是多少，希望也是10240kb吧

        log_cfg = HK.NET_DVR_LOCAL_LOG_CFG()
        log_cfg.wSDKLogNum = 1
        setCFGResult = cls.netDll.NET_DVR_SetSDKLocalCfg(HK.NET_DVR_LOCAL_CFG_TYPE_LOG, byref(log_cfg))
        cls.getLastError("NET_DVR_SetSDKLocalCfg", bool(setCFGResult))

        logFilePath = str(absLogPath).encode('gbk')
        setFileResult = cls.netDll.NET_DVR_SetLogToFile(3, logFilePath, True)
        # 日志的等级 日志文件的路径 是否删除超出的文件数
        cls.getLastError("NET_DVR_SetLogToFile", bool(setFileResult))
        if setCFGResult and setFileResult:
            return True
        else:
            return False

    @classmethod
    def logclose(cls) -> bool:
        """
        关闭日志功能
        """
        return True
        # 海康不需要关闭日志，这是为了用户层调用对齐

    @staticmethod
    def datetime2DVR_Struct_TIME(timeArg: datetime) -> HK.NET_DVR_TIME:
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
    def datetime2NET_DVR_TIME_SEARCH_COND(timeArg: datetime) -> HK.NET_DVR_TIME_SEARCH_COND:
        # 省事的时间类型转换,查询录像用的时间类型
        net_dvr_time_search_cond = HK.NET_DVR_TIME_SEARCH_COND()
        net_dvr_time_search_cond.wYear = timeArg.year
        net_dvr_time_search_cond.byMonth = timeArg.month
        net_dvr_time_search_cond.byDay = timeArg.day
        net_dvr_time_search_cond.byHour = timeArg.hour
        net_dvr_time_search_cond.byMinute = timeArg.minute
        net_dvr_time_search_cond.bySecond = timeArg.second
        return net_dvr_time_search_cond

    @staticmethod
    def DVR_Struct_Time2Datetime(timeArg: HK.NET_DVR_TIME) -> datetime:
        pyTime = datetime(timeArg.dwYear, timeArg.dwMonth, timeArg.dwDay, timeArg.dwHour, timeArg.dwMinute, timeArg.dwSecond)
        return pyTime


if __name__ == "__main__":
    pass
