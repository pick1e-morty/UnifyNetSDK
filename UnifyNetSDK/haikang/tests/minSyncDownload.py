from datetime import datetime, timedelta
from pathlib import Path

from UnifyNetSDK.parameter import UnifyLoginArg, UnifyDownLoadByTimeArg, UnifyFindFileByTimeArg
from UnifyNetSDK.haikang.hk_netsdk import HaikangNetSDK
from tests._testLoginConfig import getTestUserConfig

testUserConfig = getTestUserConfig("haikang")

hkClient = HaikangNetSDK()
hkClient.init()
hkClient.logopen()

easy_login_info = UnifyLoginArg()
easy_login_info.userName = testUserConfig.devUserName
easy_login_info.userPassword = testUserConfig.devPassword
easy_login_info.devicePort = testUserConfig.devPort
easy_login_info.deviceAddress = testUserConfig.devIP

userID, device_info = hkClient.login(easy_login_info)
print("硬盘数量", device_info.struDeviceV30.byDiskNum)

两分钟前 = datetime.now() - timedelta(seconds=360)
一分钟前 = datetime.now() - timedelta(seconds=359)

findArg = UnifyFindFileByTimeArg()
findArg.channel = 31
findArg.startTime = 两分钟前
findArg.stopTime = 一分钟前
findResult = hkClient.syncFindFileByTime(userID, findArg)
print(f"查找结果{findResult}")

if findResult is True:
    downloadArg = UnifyDownLoadByTimeArg()
    downloadArg.channel = 31
    downloadArg.saveFilePath = Path.cwd() / "test.mp4"
    downloadArg.startTime = 两分钟前
    downloadArg.stopTime = 一分钟前
    downLoadResult = hkClient.syncDownLoadByTime(userID, downloadArg)
    print(f"下载结果{downLoadResult}")

hkClient.logout(userID)
hkClient.logclose()
hkClient.cleanup()
