import time
from pathlib import Path

from UnifyNetSDK.dahua.playsdk.dh_playsdk_wrapper import *
import UnifyNetSDK.dahua.playsdk.dh_playsdk_wrapper as playDll

# 先在这个文件中测试一下，目标功能的实现
# 如果成功的话，那就恢复原来的项目结构
# playsdk直接在netsdk文件中一并导入。


nPort = c_long(0)
bFlag = bool(playDll.PLAY_GetFreePort(byref(nPort)))
if bFlag is False:
    print("PLAY_GetFreePort", playDll.PLAY_GetLastErrorEx())
    exit(1)

videoName = create_string_buffer("4002972.mp4".encode("gbk"))
bFlag = bool(playDll.PLAY_OpenFile(nPort, videoName))
if bFlag is False:
    print("PLAY_OpenFile", playDll.PLAY_GetLastErrorEx())
    exit(1)

# 开始播放文件
bFlag = bool(playDll.PLAY_Play(nPort, None))
if bFlag is False:
    print("PLAY_Play", playDll.PLAY_GetLastErrorEx())
    exit(1)
time.sleep(0.5)

absPath = Path(__file__).absolute()
picName = absPath.with_name("123.jpg")
abspicName = create_string_buffer(str(picName).encode("gbk"))

bFlag = bool(playDll.PLAY_CatchPicEx(nPort, abspicName, playDll.PicFormat_JPEG_70))
if bFlag is False:
    print("PLAY_CatchPic", playDll.PLAY_GetLastErrorEx())
    exit(1)

# 停止播放
bFlag = bool(playDll.PLAY_Stop(nPort))
if bFlag is False:
    print("PLAY_Stop", playDll.PLAY_GetLastErrorEx())
    exit(1)
# 关闭文件
bFlag = bool(playDll.PLAY_CloseFile(nPort))
if bFlag is False:
    print("PLAY_CloseFile", playDll.PLAY_GetLastErrorEx())
    exit(1)
