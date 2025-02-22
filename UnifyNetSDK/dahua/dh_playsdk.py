import typing
from ctypes import *
from pathlib import Path
from typing import NoReturn

from loguru import logger

import UnifyNetSDK.dahua.dh_playsdk_wrapper as playsdk_wrapper
from UnifyNetSDK.dahua.dh_playsdk_exception import DHPlaySDKExceptionDict
from UnifyNetSDK.define import AbsPlaySDK


# TODO playsdk的日志应该没必要开

class DaHuaPlaySDK(AbsPlaySDK):
    playDll = playsdk_wrapper

    def __init__(self):
        pass

    @classmethod
    def getFreePort(cls) -> c_long:
        # 获取一个可用的端口
        nPort = c_long(0)
        result = cls.playDll.PLAY_GetFreePort(byref(nPort))
        cls.getLastError("PLAY_GetFreePort", bool(result))
        return nPort

    @classmethod
    def releasePort(cls, nPort: int) -> bool:
        # 释放端口
        result = cls.playDll.PLAY_ReleasePort(nPort)
        cls.getLastError("PLAY_ReleasePort", bool(result))
        return bool(result)

    @classmethod
    def openFile(cls, nPort: int, videoFilePath: [str, Path]) -> bool:
        # 打开文件
        filePath = create_string_buffer(str(videoFilePath).encode("gbk"))
        openResult = cls.playDll.PLAY_OpenFile(nPort, filePath)
        cls.getLastError("PLAY_OpenFile", bool(openResult))
        return bool(openResult)

    @classmethod
    def play(cls, nPort: int, hwnd=None) -> bool:
        # 播放
        playResult = cls.playDll.PLAY_Play(nPort, hwnd)
        cls.getLastError("PLAY_Play", bool(playResult))
        return bool(playResult)

    @classmethod
    def catchPic(cls, nPort: int, absPicName: str, quality=None) -> bool:
        """
        如果quality参数是None，则抓图质量为，jpg格式，压缩70%
        大华这边限制了jpeg压缩质量为，10，30，50，70，100
        那海康那边也需要同步一下，只能有这四种选项
        """
        quality = 70 if quality is None else quality
        qualityDict = {100: cls.playDll.PicFormat_JPEG,
                       70: cls.playDll.PicFormat_JPEG_70,
                       50: cls.playDll.PicFormat_JPEG_50,
                       30: cls.playDll.PicFormat_JPEG_30,
                       10: cls.playDll.PicFormat_JPEG_10}
        quality = qualityDict[quality]

        absPicName = create_string_buffer(str(absPicName).encode("gbk"))
        catchResult = cls.playDll.PLAY_CatchPicEx(nPort, absPicName, quality)
        cls.getLastError("PLAY_CatchPicEx", bool(catchResult))
        return bool(catchResult)

    @classmethod
    def stop(cls, nPort: int) -> bool:
        # 停止播放
        stopResult = cls.playDll.PLAY_Stop(nPort)
        cls.getLastError("PLAY_Stop", bool(stopResult))
        return bool(stopResult)

    @classmethod
    def close(cls, nPort: int) -> bool:
        # 关闭文件
        closeResult = cls.playDll.PLAY_CloseFile(nPort)
        cls.getLastError("PLAY_CloseFile", bool(closeResult))
        return bool(closeResult)

    @classmethod
    def getLastError(cls, methodName: str, methodResult: typing.Union[int, bool]) -> NoReturn:
        # 获取错误码，就算没有错误也会被 raise NO_ERROR
        logger.debug(f"{methodName}执行结果为 {type(methodResult)} {methodResult}")
        if methodResult == -1 or methodResult is False:
            cls._getLastError()

    @classmethod
    def _getLastError(cls) -> NoReturn:
        # 获取错误码的底层实现
        errorIndex = cls.playDll.PLAY_GetLastErrorEx()
        try:
            exception = DHPlaySDKExceptionDict[errorIndex]
        except IndexError:
            logger.error(f"{errorIndex} 未知错误")
            raise Exception("未知错误")
        logger.error(f"{errorIndex} {exception}")
        raise exception
