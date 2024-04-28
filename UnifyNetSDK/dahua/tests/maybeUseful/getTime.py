# from pathlib import Path
# sys.path.append(str(Path(__file__).resolve().parent.parent))
from ctypes import *
from pathlib import Path

from _ctypes import sizeof

import UnifyNetSDK.dahua.dh_netsdk_wrapper as DH
from UnifyNetSDK import DaHuaNetSDK
from UnifyNetSDK.dahua.dh_netsdk import DaHuaNetSDK
from UnifyNetSDK.dahua.dh_netsdk_exception import DHNetSDKException
from UnifyNetSDK.parameter import UnifyLoginArg
from tests._testLoginConfig import getTestUserConfig

testUserConfig = getTestUserConfig("dahua")


def main():
    dahuaClient = DaHuaNetSDK()
    dahuaClient.init()
    absLogPath = Path(__file__).absolute().parent
    absLogPath = absLogPath.joinpath("dh_netsdk_log/netsdk1.log")
    dahuaClient.logopen(str(absLogPath))

    easy_login_info = UnifyLoginArg()
    easy_login_info.userName = testUserConfig.devUserName
    easy_login_info.userPassword = testUserConfig.devPassword
    easy_login_info.devicePort = testUserConfig.devPort
    easy_login_info.deviceAddress = testUserConfig.devIP

    userID, device_info = dahuaClient.login(easy_login_info)
    print("硬盘数量", device_info.stuDeviceInfo.nDiskNum)

    # ################ 业务代码

    dahuaClient.netDll.CLIENT_GetDevConfig.restype = c_bool

    lChannel = 0
    dwOutBufferSize = sizeof(DH.NET_TIME)
    lpOutBuffer = DH.NET_TIME()
    lpBytesReturned = c_ulong()
    waittime = 500

    try:
        result = dahuaClient.netDll.CLIENT_GetDevConfig(userID, DH.DH_DEV_TIMECFG, lChannel, byref(lpOutBuffer), dwOutBufferSize, byref(lpBytesReturned), waittime)
    except DHNetSDKException as e:
        print(str(e))
    else:
        if result:
            print("获取时间成功")
            print(lpOutBuffer.dwYear, lpOutBuffer.dwMonth, lpOutBuffer.dwDay, lpOutBuffer.dwHour, lpOutBuffer.dwMinute, lpOutBuffer.dwSecond)
        else:
            print("获取时间失败")
    finally:
        dahuaClient.logout(userID)
        dahuaClient.logclose()
        dahuaClient.cleanup()

    # BOOL; CLIENT_GetDevConfig(LLONG; lLoginID, DWORD; dwCommand, LONG; lChannel, LPVOID; lpOutBuffer, DWORD; dwOutBufferSize, LPDWORD; lpBytesReturned, int; waittime = 500);
    # if _libs["Libs/win64/dhnetsdk.dll"].has("CLIENT_GetDevConfig", "cdecl"):
    #     CLIENT_GetDevConfig = _libs["Libs/win64/dhnetsdk.dll"].get("CLIENT_GetDevConfig", "cdecl")
    #     CLIENT_GetDevConfig.argtypes = [c_longlong, c_uint, c_int, POINTER(None), c_uint, POINTER(c_uint), c_int]
    #     CLIENT_GetDevConfig.restype = c_int


    # ################ 业务代码


if __name__ == '__main__':
    main()
