def PlayBackex(self):       # 回放的扩展形式，主要就是用的结构体作为参数
    print(self.label.winId(), type(self.label.winId()))
    两分钟前 = datetime.now() - timedelta(seconds=360)
    一分钟前 = datetime.now() - timedelta(seconds=350)
    startDateTime = self.dahuaClient.datetime2DVR_Struct_TIME(两分钟前)
    endDateTime = self.dahuaClient.datetime2DVR_Struct_TIME(一分钟前)

    inParam = DH.NET_IN_PLAY_BACK_BY_TIME_INFO()

    hend = int(self.label.winId())
    hwnd = cast(c_void_p(hend), c_void_p)
    inParam.hWnd = hwnd

    print(inParam.hWnd)
    inParam.cbDownLoadPos = DownLoadPosCallBack
    inParam.dwPosUser = 0
    inParam.fDownLoadDataCallBack = DownLoadDataCallBack
    inParam.dwDataUser = 0
    # inParam.nPlayDirection = 0
    # inParam.nWaittime = 5000
    inParam.stStartTime.dwYear = startDateTime.dwYear
    inParam.stStartTime.dwMonth = startDateTime.dwMonth
    inParam.stStartTime.dwDay = startDateTime.dwDay
    inParam.stStartTime.dwHour = startDateTime.dwHour
    inParam.stStartTime.dwMinute = startDateTime.dwMinute
    inParam.stStartTime.dwSecond = startDateTime.dwSecond
    inParam.stStopTime.dwYear = endDateTime.dwYear
    inParam.stStopTime.dwMonth = endDateTime.dwMonth
    inParam.stStopTime.dwDay = endDateTime.dwDay
    inParam.stStopTime.dwHour = endDateTime.dwHour
    inParam.stStopTime.dwMinute = endDateTime.dwMinute
    inParam.stStopTime.dwSecond = endDateTime.dwSecond
    outParam = DH.NET_OUT_PLAY_BACK_BY_TIME_INFO()

    nchannel = 29

    loginID = c_longlong(self.userID)
    try:
        self.lPlayHandle = self.dahuaClient.sdkDll.CLIENT_PlayBackByTimeEx2(loginID, nchannel, inParam, outParam)
        print("回访结果", self.lPlayHandle)
        self.dahuaClient.getLastError("PlayBackByTimeEx2", bool(self.lPlayHandle))
    except Exception as e:
        print(e)


####################################################################################################################################################################################################################################


@classmethod
def getFreePort(cls):                                   # 用的dhplay.dll，控制播放库的，
    port = c_int()
    result = cls.playDll.PLAY_GetFreePort(byref(port))
    cls.getLastError("PLAY_GetFreePort", bool(result))
    return port


@classmethod
def setPort(cls, port, hwnd):
    result = cls.playDll.PLAY_OpenStream(port, None, 0, 720 * 1280)
    cls.getLastError("PLAY_OpenStream", bool(result))

    result = cls.playDll.PLAY_SetDecCBStream(port, 1)
    cls.getLastError("PLAY_SetDecCBStream", bool(result))

    # hwnd = pointer(c_int(0))
    result = cls.playDll.PLAY_Play(port, hwnd)
    cls.getLastError("PLAY_Play", bool(result))


@classmethod
def closePortStopPlay(cls, port):
    result = cls.playDll.PLAY_Stop(port)
    cls.getLastError("PLAY_OpenStream", bool(result))

    result = cls.playDll.PLAY_CloseStream(port)
    cls.getLastError("PLAY_OpenStream", bool(result))
