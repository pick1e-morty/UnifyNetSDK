import time
from ctypes import create_string_buffer
from pathlib import Path

from UnifyNetSDK.dahua.dh_playsdk import DaHuaPlaySDK

playClient = DaHuaPlaySDK()
nPort = playClient.getFreePort()
videoPath = "test.mp4"
playClient.openFile(nPort, videoPath)
playClient.play(nPort)

time.sleep(0.1)

absPath = Path(__file__).absolute()
absPicName = absPath.with_name("test.jpg")
playClient.catchPic(nPort, absPicName)
playClient.stop(nPort)
playClient.close(nPort)
playClient.releasePort(nPort)
