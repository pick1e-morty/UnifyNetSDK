# from pathlib import Path
# sys.path.append(str(Path(__file__).resolve().parent.parent))
from pathlib import Path

from UnifyNetSDK.dahua.dh_netsdk import DaHuaNetSDK
from UnifyNetSDK.dahua.dh_netsdk_exception import DHNetSDKException
from UnifyNetSDK.parameter import UnifyLoginArg, UninfyNTPArg
from tests._testLoginConfig import getTestUserConfig

testUserConfig = getTestUserConfig("dahua")


def main():
    initResult = False
    releaseResult = False

    logOpenResult = False
    logCloseResult = False

    loginResult = False
    logoutResult = False

    dahuaClient = None
    userID = None

    try:
        dahuaClient = DaHuaNetSDK()
        initResult = dahuaClient.init()
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

        # ntparg = dahuaClient.getNTP_CFG(userID)
        # print("ntp功能是否启用", ntparg.enable)
        # print("ntp的地址", ntparg.domainOrIP)
        # print("ntp的端口", ntparg.port)
        # print("ntp的时区", ntparg.timeZone)
        # print("ntp的更新间隔", ntparg.updateInterval)

        new_ntparg = UninfyNTPArg()
        new_ntparg.enable = True
        new_ntparg.domainOrIP = "ntp.aliyun.com"
        new_ntparg.port = 123
        new_ntparg.updateInterval = 60

        result = dahuaClient.setNTP_CFG(userID, new_ntparg)
        print(result)

        logoutResult = dahuaClient.logout(userID)
        logCloseResult = dahuaClient.logclose()
        releaseResult = dahuaClient.cleanup()
    except DHNetSDKException as e:
        print(e)
        if dahuaClient:
            if userID and loginResult and not logoutResult:
                dahuaClient.logout(userID)
            if logOpenResult and not logCloseResult:
                dahuaClient.logclose()
            if initResult and not releaseResult:
                dahuaClient.cleanup()


if __name__ == '__main__':
    main()
