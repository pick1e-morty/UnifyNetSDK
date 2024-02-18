import sys
from pathlib import Path
# sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
from ctypes import *
from datetime import timedelta, datetime

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QPushButton, QWidget, QLabel, QApplication, QGridLayout
from UnifyNetSDK import DaHuaSDK
from UnifyNetSDK.parameter import UnifyLoginArg, UnifyDownLoadByTimeArg, UnifyPlayBackByTimeArg
import UnifyNetSDK.dahua.ctypes_headfile as DH

global formObject


@DH.fDataCallBack
def DownLoadDataCallBack(lPlayHandle, dwDataType, pBuffer, dwBufSize, dwUser):
    print(lPlayHandle, dwDataType, pBuffer, dwBufSize, dwUser)
    return 1  # 回调函数要求返回值是整数类型的


@DH.fDownLoadPosCallBack
def DownLoadPosCallBack(lPlayHandle, dwTotalSize, dwDownLoadSize, dwUser):
    print(lPlayHandle, dwTotalSize, dwDownLoadSize, dwUser)
    if dwDownLoadSize >= dwTotalSize:   # 传完截个图
        formObject.catchPicFun()        # 外部变量控制示例
        print("我截屏了")





class testForm(QWidget):
    def __init__(self):
        super().__init__()
        self.realPlayHandle = None
        self.playBackHandle = None
        self.initUI()
        self.chance = 4

        self.dahuaClient = DaHuaSDK()
        self.dahuaClient.init()
        self.dahuaClient.LogOpen()

        self.login()

    def initUI(self):
        # 界面上添加一个退出按钮和一个抓图按钮还有一个开始下载回放按钮
        self.resize(900, 700)
        self.catchPB = QPushButton("抓图", self)
        self.catchPB.clicked.connect(self.catchPicFun)
        self.downPlayBackPB = QPushButton("下载视频", self)
        self.downPlayBackPB.clicked.connect(self.downPlayBack)

        self.PlayBackPB = QPushButton("开始回放", self)
        self.PlayBackPB.clicked.connect(self.playBack)
        # 实时预览按钮
        self.realTimePB = QPushButton("实时预览", self)
        self.realTimePB.clicked.connect(self.realTime)

        # 再添加一个label，用来显示回放画面
        self.label = QLabel(self)
        # 设置label的背景为白色
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        # 创建一个gridLayout把这些控件放进去
        self.gridLayout = QGridLayout(self)
        self.gridLayout.addWidget(self.catchPB, 0, 0)
        self.gridLayout.addWidget(self.downPlayBackPB, 0, 1)

        self.gridLayout.addWidget(self.realTimePB, 0, 2)
        self.gridLayout.addWidget(self.PlayBackPB, 0, 3)
        self.gridLayout.addWidget(self.label, 1, 0, 1, 4)

        self.setLayout(self.gridLayout)

    def login(self):
        easy_login_info = UnifyLoginArg()
        easy_login_info.userName = "admin"
        easy_login_info.userPassword = "ydfb450000"
        easy_login_info.devicePort = 80
        easy_login_info.deviceAddress = "10.30.15.216"

        userID, device_info = self.dahuaClient.login(easy_login_info)
        print("硬盘数量", device_info.stuDeviceInfo.nDiskNum)
        self.userID = userID

    def catchPicFun(self):

        filePath = Path(__file__).with_name("percent70.jpeg")
        savedFileName = create_string_buffer(str(filePath).encode("gbk"))
        lPlayHandle = self.playBackHandle if self.playBackHandle is not None else self.realPlayHandle
        try:
            catchResult = self.dahuaClient.netDll.CLIENT_CapturePictureEx(lPlayHandle, savedFileName, DH.NET_CAPTURE_JPEG_70)
            self.dahuaClient.getLastError("CLIENT_CapturePictureEx", bool(catchResult))
        except Exception as e:
            print(e)

    @pyqtSlot()
    def downPlayBack(self):
        两分钟前 = datetime.now() - timedelta(seconds=360)
        一分钟前 = datetime.now() - timedelta(seconds=359)

        downloadArg = UnifyDownLoadByTimeArg()
        downloadArg.channel = 31
        downloadArg.saveFilePath = Path.cwd() / "test.mp4"
        downloadArg.startTime = 两分钟前
        downloadArg.stopTime = 一分钟前

        downLoadResult = self.dahuaClient.syncDownLoadByTime(self.userID, downloadArg)
        print(f"下载结果{downLoadResult}")

    @pyqtSlot()
    def realTime(self):
        if self.realTimePB.text() == "实时预览":
            hwnd = self.label.winId()
            self.realPlayHandle = self.dahuaClient.realPlay(self.userID, 29, hwnd)
            # print(f"下载结果{self.realPlayHandle}")
            self.realTimePB.setText("停止预览")
        elif self.realTimePB.text() == "停止预览":
            self.dahuaClient.stopRealPlay(self.realPlayHandle)
            self.realTimePB.setText("实时预览")

    @pyqtSlot()
    def playBack(self):
        if self.PlayBackPB.text() == "开始回放":
            前一秒 = datetime.now() - timedelta(seconds=360)
            后一秒 = datetime.now() - timedelta(seconds=359)
            playBackArg = UnifyPlayBackByTimeArg()
            playBackArg.channel = 31
            playBackArg.startTime = 前一秒
            playBackArg.stopTime = 后一秒
            playBackArg.hwnd = self.label.winId()
            playBackArg.dataCallBack = DownLoadDataCallBack
            playBackArg.downLoadPosCallBack = DownLoadPosCallBack
            # try:
            self.playBackHandle = self.dahuaClient.playBackByTime(self.userID, playBackArg)
            # except Exception as e:
            #     print(e)
            self.PlayBackPB.setText("停止回放")
        elif self.PlayBackPB.text() == "停止回放":
            self.dahuaClient.stopPlayBack(self.playBackHandle)
            self.PlayBackPB.setText("开始回放")

    def closeEvent(self, a0) -> None:
        self.dahuaClient.logout(self.userID)
        self.dahuaClient.LogClose()
        self.dahuaClient.cleanup()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = testForm()
    widget.show()
    formObject = widget
    sys.exit(app.exec_())
