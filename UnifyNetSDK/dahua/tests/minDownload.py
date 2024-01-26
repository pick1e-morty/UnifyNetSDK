import sys
from pathlib import Path
# sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
from datetime import timedelta, datetime
from UnifyNetSDK import DaHuaSDK
from UnifyNetSDK.parameter import UnifyLoginArg, UnifyDownLoadByTimeArg, UnifyPlayBackByTimeArg, UnifyFindFileByTimeArg

# TODO 首先下载进度可以传给窗体，
# 取一帧有两种方式
# 1. playsdk解码，速度快，工具本身和输出体积都很小
#    # 我认为自解码依旧是异步的，想要精准控制只截取第一帧也是不可能的。
#    # fileWatchDog，有新文件就开一次，这个程序可以打包为一个dll，但返回值怎么办？
#         # 监控归监控，执行转换的步骤是同步的，不用dll，就内部多线程就够了，返回值的问题解决。
# 2. 依旧是ffmpeg

# TODO 海康窗体test还没做出来
# 窗体不用做了，直接异步下载，然后开timer，500ms
# 用户层面上两者都是相同的操作步骤，

# TODO NET_DVR_SET_TRANS_TYPE参数，一个 4 字节整型的转码类型：1-PS, 2-TS，3-RTP，5-MP4
# 或许海康能直接拿到MP4不过还是需要转图片


# 主进程开两个线程，分别是大华和海康的视频转图片
# 这个playctrl估计不好搞
# 然后是进程池，开八个


dahuaClient = DaHuaSDK()
dahuaClient.init()
dahuaClient.logopen()

easy_login_info = UnifyLoginArg()
easy_login_info.userName = "admin"
easy_login_info.userPassword = "admin"
easy_login_info.devicePort = 80
easy_login_info.deviceAddress = "10.10.10.10"

userID, device_info = dahuaClient.login(easy_login_info)
print("硬盘数量", device_info.stuDeviceInfo.nDiskNum)

十月二十六号 = datetime(2023, 10, 26, 6, 0, 0)
十月二十六号2 = datetime(2023, 10, 26, 6, 0, 1)

两分钟前 = 十月二十六号
一分钟前 = 十月二十六号2

# 两分钟前 = datetime.now() - timedelta(seconds=360)
# 一分钟前 = datetime.now() - timedelta(seconds=359)

findArg = UnifyFindFileByTimeArg()
findArg.channel = 31
findArg.startTime = 两分钟前
findArg.stopTime = 一分钟前
findResult = dahuaClient.syncFindFileByTime(userID, findArg)
print(f"查找到的文件数量为{findResult}")  # 0说明没找到

if findResult >= 1:
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
