# from pathlib import Path
# sys.path.append(str(Path(__file__).resolve().parent.parent))
from ctypes import *
from pathlib import Path

import UnifyNetSDK.haikang.hk_netsdk_wrapper as HK
from UnifyNetSDK import HaikangNetSDK
from UnifyNetSDK.haikang.hk_netsdk_exception import HKNetSDKException
from UnifyNetSDK.parameter import UnifyLoginArg
from tests._testLoginConfig import getTestUserConfig

testUserConfig = getTestUserConfig("haikang")


def main():
    haikangClient = HaikangNetSDK()
    haikangClient.init()
    absLogPath = Path(__file__).absolute().with_name('hk_netsdk_log')
    haikangClient.logopen(absLogPath)

    easy_login_info = UnifyLoginArg()
    easy_login_info.userName = testUserConfig.devUserName
    easy_login_info.userPassword = testUserConfig.devPassword
    easy_login_info.devicePort = testUserConfig.devPort
    easy_login_info.deviceAddress = testUserConfig.devIP

    userID, device_info = haikangClient.login(easy_login_info)
    print("硬盘数量", device_info.struDeviceV30.byDiskNum)

    lChannel = 0
    dwOutBufferSize = sizeof(HK.NET_DVR_TIME)
    lpOutBuffer = HK.NET_DVR_TIME()
    lpBytesReturned = c_ulong()

    """
    BOOL NET_DVR_GetDVRConfig( LONG     lUserID, DWORD    dwCommand, LONG     lChannel, LPVOID   lpOutBuffer, DWORD    dwOutBufferSize, LPDWORD  lpBytesReturned );
    Parameters
    lUserID [in] NET_DVR_Login_V40等登录接口的返回值 
    dwCommand [in] 设备配置命令，详见“Remarks”说明 
    lChannel [in] 通道号，不同的命令对应不同的取值，如果该参数无效则置为0xFFFFFFFF即可，详见“Remarks”说明 
    lpOutBuffer [out] 接收数据的缓冲指针 
    dwOutBufferSize [in] 接收数据的缓冲长度(以字节为单位)，不能为0 
    lpBytesReturned [out] 实际收到的数据长度指针，不能为NULL 
    """
    try:
        result = haikangClient.netDll.NET_DVR_GetDVRConfig(userID, HK.NET_DVR_GET_TIMECFG, lChannel, byref(lpOutBuffer), dwOutBufferSize, byref(lpBytesReturned))
    except HKNetSDKException as e:
        print(str(e))
    else:
        if result:
            print("获取时间成功", lpOutBuffer)
            print(lpOutBuffer.dwYear, lpOutBuffer.dwMonth, lpOutBuffer.dwDay, lpOutBuffer.dwHour, lpOutBuffer.dwMinute, lpOutBuffer.dwSecond)

    finally:
        haikangClient.logout(userID)
        haikangClient.logclose()
        haikangClient.cleanup()
        print("清理完成")


if __name__ == "__main__":
    main()
"""
struct{  DWORD    dwYear;  DWORD    dwMonth;  DWORD    dwDay;  DWORD    dwHour;
  DWORD    dwMinute;  DWORD    dwSecond;}NET_DVR_TIME, *LPNET_DVR_TIME;
"""