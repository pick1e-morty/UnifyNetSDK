from datetime import datetime, timedelta
from pathlib import Path

from UnifyNetSDK.parameter import UnifyLoginArg, UnifyDownLoadByTimeArg, UnifyFindFileByTimeArg
from UnifyNetSDK.haikang.haikangsdk import HaiKangSDK


def test_login():
    easy_login_info = UnifyLoginArg()
    easy_login_info.userName = "admin"
    easy_login_info.userPassword = "zzfb450000"
    easy_login_info.devicePort = 8000
    easy_login_info.deviceAddress = "10.200.15.41"

    hkClient = HaiKangSDK()
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

    # 下载函数 在同步阻塞状态下，download是通过while不断startPending来保活的
    # 我作为最上层用户 我希望一个函数开过去就能得到视频文件，
    # 我想同时下载两个视频的话，就由我开启多线程
    # 下载函数内部，维护好自己的下载视频完成(stopgetfile)结束状态.

    # 异步非阻塞状态下
    # 下载函数只需要做一个微小的改变，把下载句柄交给我
    # 什么时候结束下载，由我来控制

    hkClient.logout(userID)

    hkClient.cleanup()


def test_loadLibrary():
    hk_client = HaiKangSDK()
    hk_client.init()

    hk_client.cleanup()


if __name__ == "__main__":
    test_login()
