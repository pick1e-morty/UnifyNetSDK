import typing
from ctypes import *
from pathlib import Path

from loguru import logger

import UnifyNetSDK.haikang.hk_playsdk_wrapper as playsdk_wrapper
from UnifyNetSDK.define import AbsPlaySDK
from UnifyNetSDK.haikang.hk_playsdk_exception import HKPlaySDKExceptionDict


class HaikangPlaySDK(AbsPlaySDK):
    playDll = playsdk_wrapper

    def __init__(self):
        pass

    @classmethod
    def getFreePort(cls):
        nPort = c_long(0)
        result = cls.playDll.PlayM4_GetPort(byref(nPort))
        cls.getLastError(nPort, "PlayM4_GetPort", bool(result))
        return nPort

    @classmethod
    def releasePort(cls, nPort: int):
        result = cls.playDll.PlayM4_FreePort(nPort)
        cls.getLastError(nPort, "PlayM4_FreePort", bool(result))
        return result

    @classmethod
    def openFile(cls, nPort: int, videoFilePath: [str, Path]):
        filePath = create_string_buffer(str(videoFilePath).encode("gbk"))
        openResult = cls.playDll.PlayM4_OpenFile(nPort, filePath)
        cls.getLastError(nPort, "PlayM4_OpenFile", bool(openResult))
        return openResult

    @classmethod
    def play(cls, nPort: int, hwnd=None):
        playResult = cls.playDll.PlayM4_Play(nPort, hwnd)
        cls.getLastError(nPort, "PlayM4_Play", bool(playResult))
        return playResult

    @classmethod
    def catchPic(cls, nPort: int, absPicName: str, quality=None):
        """
        如果quality参数是None，则抓图质量为，jpg格式，压缩70%
        大华那边限制了jpeg压缩质量为，10，30，50，70，100
        那海康这边也需要同步一下，只能有这四种选项
        """
        quality = 70 if quality is None else quality
        qualityDict = {100: 100, 70: 70, 50: 50, 30: 30, 10: 10}
        quality = qualityDict[quality]

        setResult = cls.playDll.PlayM4_SetJpegQuality(quality)  # 设置jpeg压缩质量
        cls.getLastError(nPort, "PlayM4_SetJpegQuality", bool(setResult))

        dwWidth = c_long(0)
        dwHeight = c_long(0)  # 获得码流中原始图像的大小
        getResult = cls.playDll.PlayM4_GetPictureSize(nPort, byref(dwWidth), byref(dwHeight))
        cls.getLastError(getResult, "PlayM4_GetPictureSize", bool(getResult))

        dwSize = dwWidth.value * dwHeight.value * 5  # 预计大小，4500kb
        exPicBuf = (c_ubyte * dwSize)()  # m_pCapBuf 是一个 c_ubyte 数组的实例，而不是一个指针。你可以直接传递 m_pCapBuf，因为 ctypes 会自动将数组转换为指针。
        dwCapSize = c_ulong(0)  # [out] 获取到的实际JPEG图像数据大小

        catchResult = cls.playDll.PlayM4_GetJPEG(nPort, exPicBuf, dwSize, byref(dwCapSize))
        cls.getLastError(nPort, "PlayM4_GetJPEG", bool(catchResult))  # 抓图

        acPicBuf = (c_ubyte * dwCapSize.value)()  # 真正需要用到的内存空间
        memmove(acPicBuf, exPicBuf, sizeof(acPicBuf))  # 大数组内容移动到小数组中,去除多余的空白数据

        with open(absPicName, "wb") as f:  # 源数据就是一帧jpeg，直接以二进制写入就能用图像查看器打开了
            f.write(acPicBuf)

        return catchResult

    @classmethod
    def stop(cls, nPort: int):
        stopResult = cls.playDll.PlayM4_Stop(nPort)
        cls.getLastError(nPort, "PlayM4_Stop", bool(stopResult))
        return stopResult

    @classmethod
    def close(cls, nPort: int):
        closeResult = cls.playDll.PlayM4_CloseFile(nPort)
        cls.getLastError(nPort, "PlayM4_CloseFile", bool(closeResult))
        return closeResult

    @classmethod
    def getLastError(cls, nPort: int, methodName: str, methodResult: typing.Union[int, bool]):
        logger.debug(f"{methodName}执行结果为 {type(methodResult)} {methodResult}")
        if methodResult == -1 or methodResult is False:
            cls._getLastError(nPort)

    @classmethod
    def _getLastError(cls, nPort: int):
        errorIndex = cls.playDll.PlayM4_GetLastError(nPort)
        try:
            exception = HKPlaySDKExceptionDict[errorIndex]
        except IndexError:
            logger.error(f"{errorIndex} 未知错误")
            raise Exception("未知错误")
        logger.error(f"{errorIndex} {exception}")
        raise exception
