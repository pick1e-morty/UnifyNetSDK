import sys
from pathlib import Path
# sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
from datetime import timedelta, datetime
from UnifyNetSDK import DaHuaNetSDKs
from UnifyNetSDK.parameter import UnifyLoginArg, UnifyDownLoadByTimeArg, UnifyPlayBackByTimeArg, UnifyFindFileByTimeArg
from tests._testLoginConfig import getTestUserConfig
testUserConfig = getTestUserConfig("dahua")

dahuaClient = DaHuaNetSDKs()
dahuaClient.init()
dahuaClient.logopen()

easy_login_info = UnifyLoginArg()
easy_login_info.userName = testUserConfig.devUserName
easy_login_info.userPassword = testUserConfig.devPassword
easy_login_info.devicePort = testUserConfig.devPort
easy_login_info.deviceAddress = testUserConfig.devIP

userID, device_info = dahuaClient.login(easy_login_info)
print("硬盘数量", device_info.stuDeviceInfo.nDiskNum)

两分钟前 = datetime.now() - timedelta(seconds=360)
一分钟前 = datetime.now() - timedelta(seconds=359)

findArg = UnifyFindFileByTimeArg()
findArg.channel = 31
findArg.startTime = 两分钟前
findArg.stopTime = 一分钟前
findResult = dahuaClient.syncFindFileByTime(userID, findArg)
print(f"查找结果{findResult}")

if findResult is True:
    downloadArg = UnifyDownLoadByTimeArg()
    downloadArg.channel = 31
    downloadArg.saveFilePath = Path.cwd() / "test.mp4"
    downloadArg.startTime = 两分钟前
    downloadArg.stopTime = 一分钟前
    downLoadResult = dahuaClient.syncDownLoadByTime(userID, downloadArg)
    print(f"下载结果{downLoadResult}")

dahuaClient.logout(userID)
dahuaClient.logclose()
dahuaClient.cleanup()
