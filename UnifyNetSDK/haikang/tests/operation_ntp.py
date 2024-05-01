# from pathlib import Path
# sys.path.append(str(Path(__file__).resolve().parent.parent))
from pathlib import Path

from UnifyNetSDK.haikang.hk_netsdk import HaikangNetSDK
from UnifyNetSDK.haikang.hk_netsdk_exception import HKNetSDKException
from UnifyNetSDK.parameter import UnifyLoginArg, UninfyNTPArg
from tests._testLoginConfig import getTestUserConfig

testUserConfig = getTestUserConfig("haikang")


def main():
    initResult = False
    releaseResult = False

    logOpenResult = False
    logCloseResult = False

    loginResult = False
    logoutResult = False

    haikangClient = None
    userID = None

    try:
        haikangClient = HaikangNetSDK()
        initResult = haikangClient.init()
        absLogPath = Path(__file__).absolute().parent
        absLogPath = absLogPath.joinpath("hk_netsdk_log")
        haikangClient.logopen(str(absLogPath))

        easy_login_info = UnifyLoginArg()
        easy_login_info.userName = testUserConfig.devUserName
        easy_login_info.userPassword = testUserConfig.devPassword
        easy_login_info.devicePort = testUserConfig.devPort
        easy_login_info.deviceAddress = testUserConfig.devIP

        userID, device_info = haikangClient.login(easy_login_info)
        print("硬盘数量", device_info.struDeviceV30.byDiskNum)

        # ntparg = haikangClient.getNTP_CFG(userID)
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

        result = haikangClient.setNTP_CFG(userID, new_ntparg)
        print(result)

        logoutResult = haikangClient.logout(userID)
        logCloseResult = haikangClient.logclose()
        releaseResult = haikangClient.cleanup()
    except HKNetSDKException as e:
        print(e)
        if haikangClient:
            if userID and loginResult and not logoutResult:
                haikangClient.logout(userID)
            if logOpenResult and not logCloseResult:
                haikangClient.logclose()
            if initResult and not releaseResult:
                haikangClient.cleanup()

    print(initResult)
    print(releaseResult)
    print(logOpenResult)
    print(logCloseResult)
    print(loginResult)
    print(logoutResult)
    print(haikangClient)
    print(userID)


if __name__ == '__main__':
    main()
