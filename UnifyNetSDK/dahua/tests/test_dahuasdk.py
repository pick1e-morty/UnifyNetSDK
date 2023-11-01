from datetime import datetime, timedelta
from pathlib import Path

from UnifyNetSDK.define import UnifyLoginArg, UnifyDownLoadByTimeArg, UnifyFindFileByTimeArg
from UnifyNetSDK.dahua.dahuasdk import DaHuaSDK

# cypesgen转换有误
# 暂不知和等原因导致CLIENT_DownloadByTimeEx没有被转换输出
# 这导致我上层需要手动指定restype和argtypes

# 注意 ctypesgen会自动指定restype和argtypes，那个init记得取消掉
# 还有 ctypesgen也没有输出一些结构体，这很严重


def test_login():
    easy_login_info = UnifyLoginArg()
    easy_login_info.userName = "admin"
    easy_login_info.userPassword = "ydfb450000"
    easy_login_info.devicePort = 80
    easy_login_info.deviceAddress = "10.30.15.215"

    dahuaClient = DaHuaSDK()
    dahuaClient.init()

    userID, device_info = dahuaClient.login(easy_login_info)
    print("硬盘数量", device_info.stuDeviceInfo.nDiskNum)

    两分钟前 = datetime.now() - timedelta(seconds=120)
    一分钟前 = datetime.now() - timedelta(seconds=60)

    # findArg = UnifyFindFileByTimeArg()
    # findArg.channel = 31
    # findArg.startTime = 两分钟前
    # findArg.stopTime = 一分钟前
    # findResult = dahuaClient.syncFindFileByTime(userID, findArg)
    # print(f"查找结果{findResult}")

    downArg = UnifyDownLoadByTimeArg()
    downArg.channel = 31
    downArg.saveFilePath = Path.cwd() / "test.mp4"

    downArg.startTime = 两分钟前
    downArg.stopTime = 一分钟前

    #  CLIENT_LoginWithHighLevelSecurity执行结果为 <class 'int'> -122444864
    # 句柄解析错了

    # try:
    downLoadResult = dahuaClient.syncDownLoadByTime(userID, downArg)
    print(f"下载结果{downLoadResult}")
    # except Exception as e:
    #     print(e)
    dahuaClient.logout(userID)
    dahuaClient.cleanup()


if __name__ == "__main__":
    test_login()
