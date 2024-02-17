import time
from ctypes import create_string_buffer
from pathlib import Path

from UnifyNetSDK.dahua.playsdk.dh_playsdk import DaHuaPlaySDK

playClient = DaHuaPlaySDK()
nPort = playClient.getFreePort()
videoPath = "hk1085062.mp4"
playClient.openFile(nPort, videoPath)
playClient.play(nPort)

time.sleep(0.1)

absPath = Path(__file__).absolute()
picName = absPath.with_name("123.jpg")
absPicName = create_string_buffer(str(picName).encode("gbk"))
playClient.catchPic(nPort, absPicName)

playClient.stop(nPort)
playClient.close(nPort)
