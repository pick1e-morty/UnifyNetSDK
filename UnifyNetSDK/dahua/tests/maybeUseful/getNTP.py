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
    dwOutBufferSize = sizeof(DH.DHDEV_NTP_CFG)
    lpOutBuffer = DH.DHDEV_NTP_CFG()
    lpBytesReturned = c_ulong()
    waittime = 500

    try:
        result = dahuaClient.netDll.CLIENT_GetDevConfig(userID, DH.DH_DEV_NTP_CFG, lChannel, byref(lpOutBuffer), dwOutBufferSize, byref(lpBytesReturned), waittime)
    except DHNetSDKException as e:
        print(str(e))
    else:
        if result:
            print("获取时间成功")
            print("是否启用 ", lpOutBuffer.bEnable)
            print("NTP服务器默认端口为123 ", lpOutBuffer.nHostPort)
            print(lpOutBuffer.szDomainName, type(lpOutBuffer.szDomainName))
            print("NTP服务器地址 ", lpOutBuffer.szHostIp)
            print("NTP服务器域名 ", lpOutBuffer.szDomainName)
            print("NTP服务器类型 ", lpOutBuffer.nType)
            print("更新时间(分钟)", lpOutBuffer.nUpdateInterval)
            print("NTP服务器时区 ", lpOutBuffer.nTimeZone)
        else:
            print("获取时间失败")
    finally:
        dahuaClient.logout(userID)
        dahuaClient.logclose()
        dahuaClient.cleanup()
        print("清理完成")

    # struct; DHDEV_NTP_CFG; {BOOL; bEnable;int; nHostPort;char; szHostIp[32];char; szDomainName[128];int; nType;int; nUpdateInterval;int; nTimeZone;char; reserved[128];};

    # ################ 业务代码


if __name__ == '__main__':
    main()
