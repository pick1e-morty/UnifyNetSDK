from datetime import datetime, timedelta
from pathlib import Path

from UnifyNetSDK.define import UnifyLoginArg, UnifyDownLoadByTimeArg
from UnifyNetSDK.haikang.haikangsdk import HaiKangSDK


def test_login():
    easy_login_info = UnifyLoginArg()
    easy_login_info.user_name = "admin"
    easy_login_info.user_password = "zzfb450000"
    easy_login_info.device_port = 8000
    easy_login_info.device_address = "10.200.15.41"

    hk_client = HaiKangSDK()
    hk_client.init()
    userID = hk_client.login(easy_login_info)
    print(userID)

    downArg = UnifyDownLoadByTimeArg()
    downArg.channel = 1
    downArg.saveFilePath = Path.cwd() / "test.mp4"

    downArg.startTime = datetime.now() - timedelta(seconds=60)
    downArg.stopTime = datetime.now() - timedelta(seconds=30)

    hk_client.downLoadByTime(userID, downArg)

    hk_client.logout(userID)

    hk_client.cleanup()


def test_loadLibrary():
    hk_client = HaiKangSDK()
    hk_client.init()

    hk_client.cleanup()


if __name__ == "__main__":
    test_login()
