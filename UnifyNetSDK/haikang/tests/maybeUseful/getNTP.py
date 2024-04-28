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
    dwOutBufferSize = sizeof(HK.NET_DVR_NTPPARA)
    lpOutBuffer = HK.NET_DVR_NTPPARA()
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

    """
    struct{  BYTE           sNTPServer[64];  WORD           wInterval;
      BYTE           byEnableNTP;  signed char    cTimeDifferenceH;
      signed char    cTimeDifferenceM;  BYTE           res1;
      WORD           wNtpPort;  BYTE           res2[8];
    }NET_DVR_NTPPARA,*LPNET_DVR_NTPPARA;
    """

    try:
        result = haikangClient.netDll.NET_DVR_GetDVRConfig(userID, HK.NET_DVR_GET_NTPCFG, lChannel, byref(lpOutBuffer), dwOutBufferSize, byref(lpBytesReturned))
    except HKNetSDKException as e:
        print(str(e))
    else:
        if result:
            print("获取成功")

            print(type(lpOutBuffer.sNTPServer), lpOutBuffer.sNTPServer)

            server_bytes = bytes(lpOutBuffer.sNTPServer)
            server_text = server_bytes.decode('utf-8').rstrip('\x00')

            print("NTP校时是否启用", lpOutBuffer.byEnableNTP)
            print("NTP服务器域名或者IP地址", server_text)
            print("校时间隔时间", lpOutBuffer.wInterval)
            print("NTP服务器端口", lpOutBuffer.wNtpPort)

            print(lpOutBuffer.cTimeDifferenceH, lpOutBuffer.cTimeDifferenceM)

            difference_h = int.from_bytes(lpOutBuffer.cTimeDifferenceH, byteorder='big', signed=True)
            sign = '+' if difference_h >= 0 else '-'
            difference_h_text = f"{sign}{abs(difference_h):02d}"

            difference_m = int.from_bytes(lpOutBuffer.cTimeDifferenceM, byteorder='big', signed=True)
            print(f"GMT{difference_h_text}:{difference_m:0>2d}")

        else:
            print("获取失败")

    finally:
        haikangClient.logout(userID)
        haikangClient.logclose()
        haikangClient.cleanup()
        print("清理完成")


if __name__ == "__main__":
    main()

"""
sNTPServer 
NTP服务器域名或者IP地址 
wInterval 
校时间隔时间，以分钟或小时为单位（通过能力集NET_DVR_GetDeviceAbility获取，对应网络应用参数能力集：DEVICE_NETAPP_ABILITY） 
byEnableNTP 
NTP校时是否启用：0－否，1－是 
cTimeDifferenceH 
与国际标准时间的时差（小时），-12 ... +13 
cTimeDifferenceM 
与国际标准时间的时差（分钟），0, 30, 45 
res1 
保留，置为0 
wNtpPort 
NTP服务器端口，设备默认为123 
res2 
保留，置为0 
"""
