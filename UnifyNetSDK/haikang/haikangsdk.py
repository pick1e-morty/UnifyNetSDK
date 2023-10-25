import time
from time import sleep
from ctypes import *
import os
import sys

from UnifyNetSDK.define import *
from UnifyNetSDK.haikang.ctypegen.full_headfile import *

# 结构体初始化会被赋值
# 默认应该都是0的形式，特别是bool
from loguru import logger

from glob_path import ProjectPath

logger.add(sys.stdout, level="DEBUG")

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
        cls.objDll.NET_DVR_Init()

    # 对着大华的python写初始化，注意，不是复制大华，而是python端的高层抽象
    # 所以不要有那么大的功能要求和压力

    @classmethod
    def _loadLibrary(cls):
        WINDOWS_FLAG = True
        try:
            if WINDOWS_FLAG:
                libPath = ProjectPath / "UnifyNetSDK/haikang/lib/win"
                cls.objDll = CDLL(str(libPath / "HCNetSDK.dll"))  # 加载网络库
                cls.playctrlDll = CDLL(str(libPath / 'PlayCtrl.dll'))  # 加载播放库

                sdk_ComPath = NET_DVR_LOCAL_SDK_PATH()
                sdk_ComPath.sPath = str(libPath).encode("gbk")
                cls.objDll.NET_DVR_SetSDKInitCfg(2, byref(sdk_ComPath))
                libcryptoPath = str(libPath / "libcrypto-1_1-x64.dll").encode("gbk")
                cls.objDll.NET_DVR_SetSDKInitCfg(3, create_string_buffer(libcryptoPath))
                libsslPath = str(libPath / "libssl-1_1-x64.dll").encode("gbk")
                cls.objDll.NET_DVR_SetSDKInitCfg(4, create_string_buffer(libsslPath))

        except OSError as e:
            logger.error(f"动态库加载失败,原错误信息:{e}")
            # logger.exception(e)

    @classmethod
    def login(cls, loginArg: UnifyLoginArg):
        # 登录参数，包括设备地址、登录用户、密码等
        login_info = NET_DVR_USER_LOGIN_INFO()
        login_info.bUseAsynLogin = 0  # 同步通讯登录
        login_info.sDeviceAddress = loginArg.device_address.encode()
        login_info.wPort = loginArg.device_port
        login_info.sUserName = loginArg.user_name.encode()
        login_info.sPassword = loginArg.user_password.encode()
        print(login_info.bUseAsynLogin)

        # 设备信息, 输出参数
        device_info = NET_DVR_DEVICEINFO_V40()

        # 登录，
        userID = cls.objDll.NET_DVR_Login_V40(login_info, byref(device_info))  # TODO 注意device_info是需要加byref才能正常显示的
        # TODO 注意检查设备信息是否被正确映射及正常打印
        print("登录后错误代码为", cls.objDll.NET_DVR_GetLastError())
        print("硬盘数量", device_info.struDeviceV30.byDiskNum)
        return userID

    @classmethod
    def realPlay(cls):
        print(123)
        pass

    @classmethod
    def downLoadByTime(cls, userID, downLoadArg: UnifyDownLoadByTimeArg):

        # 准备参数
        print("下载文件路径为", downLoadArg.saveFilePath)
        sSavedFileName = create_string_buffer(str(downLoadArg.saveFilePath).encode("gbk"))
        # sSavedFileName = str(downLoadArg.saveFilePath).encode("gbk")  # 看看两种写法是不是都能用？
        # sSavedFileName = bytes(bin(str(downLoadArg.saveFilePath)))  # 看看两种写法是不是都能用？

        #

        pDownloadCond = NET_DVR_PLAYCOND()
        pDownloadCond.dwChannel = downLoadArg.channel
        pDownloadCond.struStartTime = cls.datetime2NET_DVR_TIME(downLoadArg.startTime)
        pDownloadCond.struStopTime = cls.datetime2NET_DVR_TIME(downLoadArg.stopTime)


        # 开始下载
        # TODO 错误代码17，不知道参数哪里出错了 
        # TODO 如果成功了还要做一个先查找是否有录像的功能，因为如果没录象的话SDK并不会报错，而是直接下载文件大小为0kb
        downLoadHandle = cls.objDll.NET_DVR_GetFileByTime_V40(userID, sSavedFileName, byref(pDownloadCond))

        print("下载句柄为", downLoadHandle)
        print("获取下载句柄后错误代码为", cls.objDll.NET_DVR_GetLastError())  #

        cls.objDll.NET_DVR_PlayBackControl_V40(downLoadHandle, NET_DVR_PLAYSTART, c_void_p(), 0, c_void_p(), 0)
        print("开始下载状态为", downLoadHandle)
        print("开始下载后错误代码为", cls.objDll.NET_DVR_GetLastError())
        downLoadPos = c_int()
        for i in range(5):
            cls.objDll.NET_DVR_PlayBackControl_V40(downLoadHandle, NET_DVR_PLAYGETPOS, c_void_p(), 0, byref(downLoadPos),1)
            print("下载进度", downLoadPos)
            sleep(1)
        result = cls.objDll.NET_DVR_StopGetFile(userID)
        print("关闭下载为", result)
        print("关闭下载错误代码为", cls.objDll.NET_DVR_GetLastError())

    def customDownLoadFromPlayBackByTime(cls):
        pass

    def playBackByTime(cls):
        pass

    @classmethod
    def logout(cls, userID):
        cls.objDll.NET_DVR_Logout(userID)

    @classmethod
    def cleanup(cls):
        cls.objDll.NET_DVR_Cleanup()

    @staticmethod
    def datetime2NET_DVR_TIME(timeArg: datetime):
        # 省事的时间类型转换
        net_dvr_time = NET_DVR_TIME()
        net_dvr_time.dwYear = timeArg.year
        net_dvr_time.dwMonth = timeArg.month
        net_dvr_time.dwDay = timeArg.day
        net_dvr_time.dwHour = timeArg.hour
        net_dvr_time.dwMinute = timeArg.minute
        net_dvr_time.dwSecond = timeArg.second
        return net_dvr_time


if __name__ == "__main__":
    pass
