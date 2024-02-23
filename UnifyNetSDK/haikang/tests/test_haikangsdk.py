from datetime import datetime, timedelta
from pathlib import Path

from UnifyNetSDK.parameter import UnifyLoginArg, UnifyDownLoadByTimeArg, UnifyFindFileByTimeArg
from UnifyNetSDK.haikang.hk_netsdk import HaikangNetSDK
from tests._testLoginConfig import getTestUserConfig
testUserConfig = getTestUserConfig("haikang")

def test_login():
    easy_login_info = UnifyLoginArg()
    easy_login_info.userName = testUserConfig.devUserName
    easy_login_info.userPassword = testUserConfig.devPassword
    easy_login_info.devicePort = testUserConfig.devPort
    easy_login_info.deviceAddress = testUserConfig.devIP

    hkClient = HaiKangNetSDK()
    hkClient.init()
    userID, device_info = hkClient.login(easy_login_info)
    print("硬盘数量", device_info.struDeviceV30.byDiskNum)

    两分钟前 = datetime.now() - timedelta(seconds=120)
    一分钟前 = datetime.now() - timedelta(seconds=60)

    findArg = UnifyFindFileByTimeArg()
    findArg.channel = 1
    findArg.startTime = 两分钟前
    findArg.stopTime = 一分钟前
    findResult = hkClient.syncFindFileByTime(userID, findArg)
    print(f"查找结果{findResult}")

    downArg = UnifyDownLoadByTimeArg()
    downArg.channel = 1
    downArg.saveFilePath = Path.cwd() / "test.mp4"

    downArg.startTime = 两分钟前
    downArg.stopTime = 一分钟前

    downLoadResult = hkClient.syncDownLoadByTime(userID, downArg)
    print(f"下载结果{downLoadResult}")

    hkClient.logout(userID)

    hkClient.cleanup()


def test_loadLibrary():
    hk_client = HaiKangNetSDK()
    hk_client.init()

    hk_client.cleanup()


if __name__ == "__main__":
    test_login()
