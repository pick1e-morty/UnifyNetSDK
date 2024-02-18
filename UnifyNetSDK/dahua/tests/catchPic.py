import sys
from pathlib import Path
# sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
from ctypes import *
from datetime import timedelta

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QGridLayout
from UnifyNetSDK import DaHuaNetSDK
from UnifyNetSDK.parameter import UnifyLoginArg, UnifyPlayBackByTimeArg
import UnifyNetSDK.dahua.dh_playsdk_wrapper as DH
from UnifyNetSDK.dahua.tests._testLoginConfig import testUserConfig

global formObject

import random


# 一个函数，随即返回返回7个数字的字符串
def random7():
    return "".join([str(random.randint(0, 9)) for i in range(7)])


@DH.fDataCallBack
def downLoadDataCallBack(lPlayHandle, dwDataType, pBuffer, dwBufSize, dwUser):
    # print(lPlayHandle, dwDataType, pBuffer, dwBufSize, dwUser)
    return 1  # 回调函数要求返回值是整数类型的


@DH.fDownLoadPosCallBack
def downLoadPosCallBack(lPlayHandle, dwTotalSize, dwDownLoadSize, dwUser):
    # lPlayHandle = c_longlong(lPlayHandle)
    # dwTotalSize = c_ulong(dwTotalSize)
    # dwDownLoadSize = c_ulong(dwDownLoadSize)
    # dwUser = c_longlong(dwUser)
    # print(lPlayHandle.value, dwTotalSize.value, dwDownLoadSize.value, dwUser.value)
    print(lPlayHandle, dwTotalSize, dwDownLoadSize, dwUser)

    # 第三个参数那个最后 特别大的数字 是类型的负数
    # -1
    # 4294967295
    # 是那个类型的？

    num = random7()
    filePath = Path(__file__).with_name(str(num) + ".jpeg")
    savedFileName = create_string_buffer(str(filePath).encode("gbk"))
    if dwDownLoadSize >= dwTotalSize:
        formObject.dahuaClient.catchPicture(lPlayHandle, savedFileName)
        formObject.dahuaClient.stopPlayBack(lPlayHandle)


class CatchPic(QWidget):

    def __init__(self, catchArg):
        super().__init__()
        self.catchArg = catchArg
        self.initUI()

        self.resultDict = {}

    def initUI(self):
        self.label = QLabel(self)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.gridLayout = QGridLayout(self)
        self.gridLayout.addWidget(self.label, 0, 0)
        self.setLayout(self.gridLayout)
        self.resize(1280, 720)
        self.show()
        QApplication.processEvents()

    def initDaHuaClient(self):
        self.dahuaClient = DaHuaSDK()
        self.dahuaClient.init()
        self.dahuaClient.LogOpen()
        self.login()

        for channel, path_timeList in self.catchArg.downloadArg.items():
            index = 0
            for path_time in path_timeList:
                path = path_time.savePath
                time = path_time.downloadTime
                index += 1

                self.resultDict[index] = 0
                self.catch(channel, path, time, posUser=index)

    def login(self):
        easy_login_info = UnifyLoginArg()
        easy_login_info.userName = self.catchArg.devUserName
        easy_login_info.userPassword = self.catchArg.devPassword
        easy_login_info.devicePort = self.catchArg.devPort
        easy_login_info.deviceAddress = self.catchArg.devIP
        userID, device_info = self.dahuaClient.login(easy_login_info)
        print("硬盘数量", device_info.stuDeviceInfo.nDiskNum)
        self.userID = userID

    @pyqtSlot()
    def catch(self, channel, savePath, time, posUser):
        前一秒 = time
        后一秒 = time + timedelta(seconds=1)
        playBackArg = UnifyPlayBackByTimeArg()
        playBackArg.channel = channel
        playBackArg.startTime = 前一秒
        playBackArg.stopTime = 后一秒
        playBackArg.hwnd = self.label.winId()
        playBackArg.dataCallBack = downLoadDataCallBack
        playBackArg.downLoadPosCallBack = downLoadPosCallBack
        playBackArg.dwPosUser = posUser
        playBackHandle = self.dahuaClient.playBackByTime(self.userID, playBackArg)
        return playBackHandle

    def closeEvent(self, a0) -> None:
        self.dahuaClient.logout(self.userID)
        self.dahuaClient.LogClose()
        self.dahuaClient.cleanup()


if __name__ == "__main__":
    # 大列表存 下载结果和下载ID
    # 自己开一个计时器保证句柄超时断开，但是如何检测？

    app = QApplication(sys.argv)
    widget = CatchPic(testUserConfig)
    widget.show()
    formObject = widget
    formObject.initDaHuaClient()
    sys.exit(app.exec_())
