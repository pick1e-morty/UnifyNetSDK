from datetime import datetime, timedelta
from pathlib import Path

from UnifyNetSDK.parameter import UnifyLoginArg, UnifyDownLoadByTimeArg, UnifyFindFileByTimeArg
from UnifyNetSDK.dahua.dahuasdk import DaHuaSDK


def test_login():
    easy_login_info = UnifyLoginArg()
    easy_login_info.userName = "admin"
    easy_login_info.userPassword = "admin"
    easy_login_info.devicePort = 37777
    easy_login_info.deviceAddress = "10.10.10.10"

    dahuaClient = DaHuaSDK()
    dahuaClient.init()

    userID, device_info = dahuaClient.login(easy_login_info)
    print("硬盘数量", device_info.stuDeviceInfo.nDiskNum)

    两分钟前 = datetime.now() - timedelta(seconds=120)
    一分钟前 = datetime.now() - timedelta(seconds=60)

    findArg = UnifyFindFileByTimeArg()
    findArg.channel = 31
    findArg.startTime = 两分钟前
    findArg.stopTime = 一分钟前
    findResult = dahuaClient.syncFindFileByTime(userID, findArg)
    print(f"查找结果{findResult}")

    downArg = UnifyDownLoadByTimeArg()
    downArg.channel = 31
    downArg.saveFilePath = Path.cwd() / "test.mp4"
    downArg.startTime = 两分钟前
    downArg.stopTime = 一分钟前

    try:
        downLoadResult = dahuaClient.syncDownLoadByTime(userID, downArg)
        print(f"下载结果{downLoadResult}")
    except Exception as e:
        print(e)
    dahuaClient.logout(userID)
    dahuaClient.cleanup()


if __name__ == "__main__":
    test_login()
