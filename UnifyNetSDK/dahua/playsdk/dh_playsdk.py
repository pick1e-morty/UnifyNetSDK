from pathlib import Path

from loguru import logger

from UnifyNetSDK.dahua.playsdk.dh_playsdk_exception import ErrorCode, DH_PlaySDK_Exception
from UnifyNetSDK.define import AbsPlaySDK
import UnifyNetSDK.dahua.playsdk.dh_playsdk_wrapper as playsdk_wrapper
from ctypes import *


class DaHuaPlaySDK(AbsPlaySDK):
    playDll = playsdk_wrapper

    def __init__(self):
        pass

    @classmethod
    def getFreePort(cls):
        nPort = c_long(0)
        result = cls.playDll.PLAY_GetFreePort(byref(nPort))
        cls.getLastError("PLAY_GetFreePort", bool(result))
        return nPort

    @classmethod
    def openFile(cls, nPort, videoFilePath: [str, Path]):
        filePath = create_string_buffer(str(videoFilePath).encode("gbk"))
        openResult = cls.playDll.PLAY_OpenFile(nPort, filePath)
        cls.getLastError("PLAY_OpenFile", bool(openResult))
        return openResult

    @classmethod
    def play(cls, nPort, hwnd=None):
        playResult = cls.playDll.PLAY_Play(nPort, hwnd)
        cls.getLastError("PLAY_Play", bool(playResult))
        return playResult

    @classmethod
    def catchPic(cls, nPort, absPicName, quality=None):
        """
        如果quality参数是None，则抓图质量为，jpg格式，压缩70%
        """
        quality = cls.playDll.PicFormat_JPEG_70 if quality is None else quality
        catchResult = cls.playDll.PLAY_CatchPicEx(nPort, absPicName, quality)
        cls.getLastError("PLAY_CatchPicEx", bool(catchResult))
        return catchResult

    @classmethod
    def stop(cls, nPort):
        stopResult = cls.playDll.PLAY_Stop(nPort)
        cls.getLastError("PLAY_Stop", bool(stopResult))
        return stopResult

    @classmethod
    def close(cls, nPort):
        closeResult = cls.playDll.PLAY_CloseFile(nPort)
        cls.getLastError("PLAY_CloseFile", bool(closeResult))
        return closeResult

    @classmethod
    def getLastError(cls, methodName: str, methodResult):
        logger.debug(f"{methodName}执行结果为 {type(methodResult)} {methodResult}")
        if methodResult == -1 or methodResult is False:
            cls._getLastError()

    @classmethod
    def _getLastError(cls):
        errorIndex = cls.playDll.PLAY_GetLastErrorEx()
        errorText = ErrorCode[errorIndex]
        logger.error(f"{errorIndex} {errorText}")
        raise DH_PlaySDK_Exception(errorIndex, errorText)
