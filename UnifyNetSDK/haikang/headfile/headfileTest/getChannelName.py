# coding=utf-8

import os
import platform
import tkinter
from tkinter import *
from ctypesgenHeadFile import *
from PlayCtrl import *
from time import sleep

# 登录的设备信息
DEV_IP = create_string_buffer(b"10.200.15.41")
DEV_PORT = 8000
DEV_USER_NAME = create_string_buffer(b"admin")
DEV_PASSWORD = create_string_buffer(b"zzfb450000")


# 设置SDK初始化依赖库路径
def SetSDKInitCfg():
    # 设置HCNetSDKCom组件库和SSL库加载路径
    # print(os.getcwd())
    strPath = os.getcwd().encode("gbk")
    sdk_ComPath = NET_DVR_LOCAL_SDK_PATH()
    sdk_ComPath.sPath = strPath
    Objdll.NET_DVR_SetSDKInitCfg(2, byref(sdk_ComPath))
    Objdll.NET_DVR_SetSDKInitCfg(3, create_string_buffer(strPath + b"\libcrypto-1_1-x64.dll"))
    Objdll.NET_DVR_SetSDKInitCfg(4, create_string_buffer(strPath + b"\libssl-1_1-x64.dll"))


def LoginDev(Objdll):
    # 登录注册设备
    device_info = NET_DVR_DEVICEINFO_V30()
    lUserId = Objdll.NET_DVR_Login_V30(DEV_IP, DEV_PORT, DEV_USER_NAME, DEV_PASSWORD, byref(device_info))
    return (lUserId, device_info)


if __name__ == "__main__":
    os.chdir(r"../lib/win")  # 加载库,先加载依赖库
    Objdll = ctypes.CDLL(r"./HCNetSDK.dll")  # 加载网络库
    Playctrldll = ctypes.CDLL(r"./PlayCtrl.dll")  # 加载播放库
    SetSDKInitCfg()  # 设置组件库和SSL库加载路径
    Objdll.NET_DVR_Init()  # 初始化DLL
    Objdll.NET_DVR_SetLogToFile(3, bytes("./SdkLog_Python/", encoding="utf-8"), False)  # 启用SDK写日志

    # 登录设备
    (lUserId, device_info) = LoginDev(Objdll)
    if lUserId < 0:
        err = Objdll.NET_DVR_GetLastError()
        print("Login device fail, error code is: %d" % Objdll.NET_DVR_GetLastError())
        Objdll.NET_DVR_Cleanup()  # 释放资源
        exit()

    err = Objdll.NET_DVR_GetLastError()
    print(f"登录成功用户ID为{lUserId}")

    bytesReturned = c_ulong(0)
    ipcfg = NET_DVR_IPPARACFG_V40()
    ipcfg.dwSize = sizeof(NET_DVR_IPPARACFG_V40)
    resCode = Objdll.NET_DVR_GetDVRConfig(lUserId, NET_DVR_GET_IPPARACFG_V40, 0, byref(ipcfg),
                                          sizeof(NET_DVR_IPPARACFG_V40), byref(bytesReturned))
    if resCode == 0:
        print("NET_DVR_GET_IPPARACFG_V40 fail, error code is: %d" % Objdll.NET_DVR_GetLastError())
        Objdll.NET_DVR_Logout(lUserId)
        Objdll.NET_DVR_Cleanup()
        exit()

    起始模拟通道 = device_info.byStartChan
    设备模拟通道数量 = device_info.byChanNum
    for i in range(起始模拟通道,
                   设备模拟通道数量 + 1):  # ipcfg.byAnalogChanEnable 模拟通道数量在这个数组里，1表示有通道，0表示没有通道，不过我司用的应该都是32通道的
        bytesReturned = c_ulong(0)  # 如果未来还有数字通道的就直接开一个函数就行了
        channelInfo = NET_DVR_PICCFG_V30()
        channelInfo.dwSize = sizeof(NET_DVR_PICCFG_V30)
        channelNum = i
        resCode = Objdll.NET_DVR_GetDVRConfig(lUserId, NET_DVR_GET_PICCFG_V30, channelNum, byref(channelInfo),
                                              sizeof(NET_DVR_PICCFG_V30), byref(bytesReturned))
        if resCode == 1:
            Bbytes_Out = string_at(channelInfo.sChanName, NAME_LEN)
            strOutput = str(Bbytes_Out, 'gbk')
            print(f"通道号 {channelNum} 通道名称 {strOutput}")
        else:
            print("NET_DVR_GET_PICCFG_V30 fail, error code is: %d" % Objdll.NET_DVR_GetLastError())
            Objdll.NET_DVR_Logout(lUserId)
            Objdll.NET_DVR_Cleanup()
            exit()

    # 登出设备
    Objdll.NET_DVR_Logout(lUserId)
    # 释放资源
    Objdll.NET_DVR_Cleanup()
