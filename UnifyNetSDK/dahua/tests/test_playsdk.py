import time
from pathlib import Path

from UnifyNetSDK.dahua.dh_playsdk import DaHuaPlaySDK
from UnifyNetSDK.dahua.dh_playsdk_exception import DHPlaySDKException

playClient = DaHuaPlaySDK()
nPort = playClient.getFreePort()
videoPath = "test.mp4"
playClient.openFile(nPort, videoPath)
playClient.play(nPort)

time.sleep(0.1)

absPath = Path(__file__).absolute()
absPicName = absPath.with_name("test.jpg")
try:
    playClient.catchPic(nPort, absPicName)
# except PLAY_NO_FRAME as e:
#     print(e)
except DHPlaySDKException as e:
    print(e)

playClient.stop(nPort)
playClient.close(nPort)
playClient.releasePort(nPort)
