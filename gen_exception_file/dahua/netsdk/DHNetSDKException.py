class DHNetSDKException(Exception):
    def __init__(self):
        self.errorIndex = 0
        self.errorInfo = ""
        super().__init__(self.errorIndex, self.errorInfo)

    def __str__(self):
        if self.errorInfo:
            return str(self.errorIndex) + " " + self.errorInfo
        else:
            return str(self.errorIndex)


class NET_NOERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 0
        self.errorInfo = errorText


class NET_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = -1
        self.errorInfo = errorText


class NET_SYSTEM_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1
        self.errorInfo = errorText


class NET_NETWORK_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2
        self.errorInfo = errorText


class NET_DEV_VER_NOMATCH(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 3
        self.errorInfo = errorText


class NET_INVALID_HANDLE(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 4
        self.errorInfo = errorText


class NET_OPEN_CHANNEL_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 5
        self.errorInfo = errorText


class NET_CLOSE_CHANNEL_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 6
        self.errorInfo = errorText


class NET_ILLEGAL_PARAM(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 7
        self.errorInfo = errorText


class NET_SDK_INIT_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8
        self.errorInfo = errorText


class NET_SDK_UNINIT_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 9
        self.errorInfo = errorText


class NET_RENDER_OPEN_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 10
        self.errorInfo = errorText


class NET_DEC_OPEN_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 11
        self.errorInfo = errorText


class NET_DEC_CLOSE_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 12
        self.errorInfo = errorText


class NET_MULTIPLAY_NOCHANNEL(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 13
        self.errorInfo = errorText


class NET_TALK_INIT_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 14
        self.errorInfo = errorText


class NET_TALK_NOT_INIT(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 15
        self.errorInfo = errorText


class NET_TALK_SENDDATA_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 16
        self.errorInfo = errorText


class NET_REAL_ALREADY_SAVING(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 17
        self.errorInfo = errorText


class NET_NOT_SAVING(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 18
        self.errorInfo = errorText


class NET_OPEN_FILE_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 19
        self.errorInfo = errorText


class NET_PTZ_SET_TIMER_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 20
        self.errorInfo = errorText


class NET_RETURN_DATA_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 21
        self.errorInfo = errorText


class NET_INSUFFICIENT_BUFFER(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 22
        self.errorInfo = errorText


class NET_NOT_SUPPORTED(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 23
        self.errorInfo = errorText


class NET_NO_RECORD_FOUND(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 24
        self.errorInfo = errorText


class NET_NOT_AUTHORIZED(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 25
        self.errorInfo = errorText


class NET_NOT_NOW(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 26
        self.errorInfo = errorText


class NET_NO_TALK_CHANNEL(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 27
        self.errorInfo = errorText


class NET_NO_AUDIO(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 28
        self.errorInfo = errorText


class NET_NO_INIT(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 29
        self.errorInfo = errorText


class NET_DOWNLOAD_END(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 30
        self.errorInfo = errorText


class NET_EMPTY_LIST(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 31
        self.errorInfo = errorText


class NET_ERROR_GETCFG_SYSATTR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 32
        self.errorInfo = errorText


class NET_ERROR_GETCFG_SERIAL(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 33
        self.errorInfo = errorText


class NET_ERROR_GETCFG_GENERAL(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 34
        self.errorInfo = errorText


class NET_ERROR_GETCFG_DSPCAP(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 35
        self.errorInfo = errorText


class NET_ERROR_GETCFG_NETCFG(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 36
        self.errorInfo = errorText


class NET_ERROR_GETCFG_CHANNAME(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 37
        self.errorInfo = errorText


class NET_ERROR_GETCFG_VIDEO(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 38
        self.errorInfo = errorText


class NET_ERROR_GETCFG_RECORD(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 39
        self.errorInfo = errorText


class NET_ERROR_GETCFG_PRONAME(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 40
        self.errorInfo = errorText


class NET_ERROR_GETCFG_FUNCNAME(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 41
        self.errorInfo = errorText


class NET_ERROR_GETCFG_485DECODER(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 42
        self.errorInfo = errorText


class NET_ERROR_GETCFG_232COM(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 43
        self.errorInfo = errorText


class NET_ERROR_GETCFG_ALARMIN(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 44
        self.errorInfo = errorText


class NET_ERROR_GETCFG_ALARMDET(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 45
        self.errorInfo = errorText


class NET_ERROR_GETCFG_SYSTIME(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 46
        self.errorInfo = errorText


class NET_ERROR_GETCFG_PREVIEW(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 47
        self.errorInfo = errorText


class NET_ERROR_GETCFG_AUTOMT(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 48
        self.errorInfo = errorText


class NET_ERROR_GETCFG_VIDEOMTRX(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 49
        self.errorInfo = errorText


class NET_ERROR_GETCFG_COVER(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 50
        self.errorInfo = errorText


class NET_ERROR_GETCFG_WATERMAKE(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 51
        self.errorInfo = errorText


class NET_ERROR_GETCFG_MULTICAST(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 52
        self.errorInfo = errorText


class NET_ERROR_SETCFG_GENERAL(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 55
        self.errorInfo = errorText


class NET_ERROR_SETCFG_NETCFG(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 56
        self.errorInfo = errorText


class NET_ERROR_SETCFG_CHANNAME(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 57
        self.errorInfo = errorText


class NET_ERROR_SETCFG_VIDEO(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 58
        self.errorInfo = errorText


class NET_ERROR_SETCFG_RECORD(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 59
        self.errorInfo = errorText


class NET_ERROR_SETCFG_485DECODER(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 60
        self.errorInfo = errorText


class NET_ERROR_SETCFG_232COM(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 61
        self.errorInfo = errorText


class NET_ERROR_SETCFG_ALARMIN(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 62
        self.errorInfo = errorText


class NET_ERROR_SETCFG_ALARMDET(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 63
        self.errorInfo = errorText


class NET_ERROR_SETCFG_SYSTIME(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 64
        self.errorInfo = errorText


class NET_ERROR_SETCFG_PREVIEW(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 65
        self.errorInfo = errorText


class NET_ERROR_SETCFG_AUTOMT(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 66
        self.errorInfo = errorText


class NET_ERROR_SETCFG_VIDEOMTRX(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 67
        self.errorInfo = errorText


class NET_ERROR_SETCFG_COVER(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 68
        self.errorInfo = errorText


class NET_ERROR_SETCFG_WATERMAKE(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 69
        self.errorInfo = errorText


class NET_ERROR_SETCFG_WLAN(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 70
        self.errorInfo = errorText


class NET_ERROR_SETCFG_WLANDEV(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 71
        self.errorInfo = errorText


class NET_ERROR_SETCFG_REGISTER(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 72
        self.errorInfo = errorText


class NET_ERROR_SETCFG_CAMERA(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 73
        self.errorInfo = errorText


class NET_ERROR_SETCFG_INFRARED(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 74
        self.errorInfo = errorText


class NET_ERROR_SETCFG_SOUNDALARM(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 75
        self.errorInfo = errorText


class NET_ERROR_SETCFG_STORAGE(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 76
        self.errorInfo = errorText


class NET_AUDIOENCODE_NOTINIT(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 77
        self.errorInfo = errorText


class NET_DATA_TOOLONGH(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 78
        self.errorInfo = errorText


class NET_UNSUPPORTED(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 79
        self.errorInfo = errorText


class NET_DEVICE_BUSY(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 80
        self.errorInfo = errorText


class NET_SERVER_STARTED(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 81
        self.errorInfo = errorText


class NET_SERVER_STOPPED(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 82
        self.errorInfo = errorText


class NET_LISTER_INCORRECT_SERIAL(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 83
        self.errorInfo = errorText


class NET_QUERY_DISKINFO_FAILED(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 84
        self.errorInfo = errorText


class NET_ERROR_GETCFG_SESSION(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 85
        self.errorInfo = errorText


class NET_USER_FLASEPWD_TRYTIME(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 86
        self.errorInfo = errorText


class NET_LOGIN_ERROR_PASSWORD_EXPIRED(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 99
        self.errorInfo = errorText


class NET_LOGIN_ERROR_PASSWORD(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 100
        self.errorInfo = errorText


class NET_LOGIN_ERROR_USER(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 101
        self.errorInfo = errorText


class NET_LOGIN_ERROR_TIMEOUT(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 102
        self.errorInfo = errorText


class NET_LOGIN_ERROR_RELOGGIN(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 103
        self.errorInfo = errorText


class NET_LOGIN_ERROR_LOCKED(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 104
        self.errorInfo = errorText


class NET_LOGIN_ERROR_BLACKLIST(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 105
        self.errorInfo = errorText


class NET_LOGIN_ERROR_BUSY(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 106
        self.errorInfo = errorText


class NET_LOGIN_ERROR_CONNECT(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 107
        self.errorInfo = errorText


class NET_LOGIN_ERROR_NETWORK(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 108
        self.errorInfo = errorText


class NET_LOGIN_ERROR_SUBCONNECT(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 109
        self.errorInfo = errorText


class NET_LOGIN_ERROR_MAXCONNECT(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 110
        self.errorInfo = errorText


class NET_LOGIN_ERROR_PROTOCOL3_ONLY(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 111
        self.errorInfo = errorText


class NET_LOGIN_ERROR_UKEY_LOST(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 112
        self.errorInfo = errorText


class NET_LOGIN_ERROR_NO_AUTHORIZED(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 113
        self.errorInfo = errorText


class NET_LOGIN_ERROR_USER_OR_PASSOWRD(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 117
        self.errorInfo = errorText


class NET_LOGIN_ERROR_DEVICE_NOT_INIT(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 118
        self.errorInfo = errorText


class NET_LOGIN_ERROR_LIMITED(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 119
        self.errorInfo = errorText


class NET_RENDER_SOUND_ON_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 120
        self.errorInfo = errorText


class NET_RENDER_SOUND_OFF_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 121
        self.errorInfo = errorText


class NET_RENDER_SET_VOLUME_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 122
        self.errorInfo = errorText


class NET_RENDER_ADJUST_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 123
        self.errorInfo = errorText


class NET_RENDER_PAUSE_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 124
        self.errorInfo = errorText


class NET_RENDER_SNAP_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 125
        self.errorInfo = errorText


class NET_RENDER_STEP_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 126
        self.errorInfo = errorText


class NET_RENDER_FRAMERATE_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 127
        self.errorInfo = errorText


class NET_RENDER_DISPLAYREGION_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 128
        self.errorInfo = errorText


class NET_RENDER_GETOSDTIME_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 129
        self.errorInfo = errorText


class NET_GROUP_EXIST(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 140
        self.errorInfo = errorText


class NET_GROUP_NOEXIST(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 141
        self.errorInfo = errorText


class NET_GROUP_RIGHTOVER(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 142
        self.errorInfo = errorText


class NET_GROUP_HAVEUSER(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 143
        self.errorInfo = errorText


class NET_GROUP_RIGHTUSE(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 144
        self.errorInfo = errorText


class NET_GROUP_SAMENAME(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 145
        self.errorInfo = errorText


class NET_USER_EXIST(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 146
        self.errorInfo = errorText


class NET_USER_NOEXIST(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 147
        self.errorInfo = errorText


class NET_USER_RIGHTOVER(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 148
        self.errorInfo = errorText


class NET_USER_PWD(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 149
        self.errorInfo = errorText


class NET_USER_FLASEPWD(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 150
        self.errorInfo = errorText


class NET_USER_NOMATCHING(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 151
        self.errorInfo = errorText


class NET_USER_INUSE(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 152
        self.errorInfo = errorText


class NET_ERROR_GETCFG_ETHERNET(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 300
        self.errorInfo = errorText


class NET_ERROR_GETCFG_WLAN(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 301
        self.errorInfo = errorText


class NET_ERROR_GETCFG_WLANDEV(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 302
        self.errorInfo = errorText


class NET_ERROR_GETCFG_REGISTER(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 303
        self.errorInfo = errorText


class NET_ERROR_GETCFG_CAMERA(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 304
        self.errorInfo = errorText


class NET_ERROR_GETCFG_INFRARED(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 305
        self.errorInfo = errorText


class NET_ERROR_GETCFG_SOUNDALARM(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 306
        self.errorInfo = errorText


class NET_ERROR_GETCFG_STORAGE(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 307
        self.errorInfo = errorText


class NET_ERROR_GETCFG_MAIL(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 308
        self.errorInfo = errorText


class NET_CONFIG_DEVBUSY(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 309
        self.errorInfo = errorText


class NET_CONFIG_DATAILLEGAL(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 310
        self.errorInfo = errorText


class NET_ERROR_GETCFG_DST(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 311
        self.errorInfo = errorText


class NET_ERROR_SETCFG_DST(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 312
        self.errorInfo = errorText


class NET_ERROR_GETCFG_VIDEO_OSD(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 313
        self.errorInfo = errorText


class NET_ERROR_SETCFG_VIDEO_OSD(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 314
        self.errorInfo = errorText


class NET_ERROR_GETCFG_GPRSCDMA(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 315
        self.errorInfo = errorText


class NET_ERROR_SETCFG_GPRSCDMA(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 316
        self.errorInfo = errorText


class NET_ERROR_GETCFG_IPFILTER(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 317
        self.errorInfo = errorText


class NET_ERROR_SETCFG_IPFILTER(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 318
        self.errorInfo = errorText


class NET_ERROR_GETCFG_TALKENCODE(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 319
        self.errorInfo = errorText


class NET_ERROR_SETCFG_TALKENCODE(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 320
        self.errorInfo = errorText


class NET_ERROR_GETCFG_RECORDLEN(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 321
        self.errorInfo = errorText


class NET_ERROR_SETCFG_RECORDLEN(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 322
        self.errorInfo = errorText


class NET_DONT_SUPPORT_SUBAREA(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 323
        self.errorInfo = errorText


class NET_ERROR_GET_AUTOREGSERVER(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 324
        self.errorInfo = errorText


class NET_ERROR_CONTROL_AUTOREGISTER(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 325
        self.errorInfo = errorText


class NET_ERROR_DISCONNECT_AUTOREGISTER(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 326
        self.errorInfo = errorText


class NET_ERROR_GETCFG_MMS(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 327
        self.errorInfo = errorText


class NET_ERROR_SETCFG_MMS(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 328
        self.errorInfo = errorText


class NET_ERROR_GETCFG_SMSACTIVATION(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 329
        self.errorInfo = errorText


class NET_ERROR_SETCFG_SMSACTIVATION(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 330
        self.errorInfo = errorText


class NET_ERROR_GETCFG_DIALINACTIVATION(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 331
        self.errorInfo = errorText


class NET_ERROR_SETCFG_DIALINACTIVATION(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 332
        self.errorInfo = errorText


class NET_ERROR_GETCFG_VIDEOOUT(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 333
        self.errorInfo = errorText


class NET_ERROR_SETCFG_VIDEOOUT(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 334
        self.errorInfo = errorText


class NET_ERROR_GETCFG_OSDENABLE(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 335
        self.errorInfo = errorText


class NET_ERROR_SETCFG_OSDENABLE(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 336
        self.errorInfo = errorText


class NET_ERROR_SETCFG_ENCODERINFO(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 337
        self.errorInfo = errorText


class NET_ERROR_GETCFG_TVADJUST(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 338
        self.errorInfo = errorText


class NET_ERROR_SETCFG_TVADJUST(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 339
        self.errorInfo = errorText


class NET_ERROR_CONNECT_FAILED(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 340
        self.errorInfo = errorText


class NET_ERROR_SETCFG_BURNFILE(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 341
        self.errorInfo = errorText


class NET_ERROR_SNIFFER_GETCFG(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 342
        self.errorInfo = errorText


class NET_ERROR_SNIFFER_SETCFG(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 343
        self.errorInfo = errorText


class NET_ERROR_DOWNLOADRATE_GETCFG(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 344
        self.errorInfo = errorText


class NET_ERROR_DOWNLOADRATE_SETCFG(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 345
        self.errorInfo = errorText


class NET_ERROR_SEARCH_TRANSCOM(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 346
        self.errorInfo = errorText


class NET_ERROR_GETCFG_POINT(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 347
        self.errorInfo = errorText


class NET_ERROR_SETCFG_POINT(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 348
        self.errorInfo = errorText


class NET_SDK_LOGOUT_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 349
        self.errorInfo = errorText


class NET_ERROR_GET_VEHICLE_CFG(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 350
        self.errorInfo = errorText


class NET_ERROR_SET_VEHICLE_CFG(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 351
        self.errorInfo = errorText


class NET_ERROR_GET_ATM_OVERLAY_CFG(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 352
        self.errorInfo = errorText


class NET_ERROR_SET_ATM_OVERLAY_CFG(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 353
        self.errorInfo = errorText


class NET_ERROR_GET_ATM_OVERLAY_ABILITY(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 354
        self.errorInfo = errorText


class NET_ERROR_GET_DECODER_TOUR_CFG(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 355
        self.errorInfo = errorText


class NET_ERROR_SET_DECODER_TOUR_CFG(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 356
        self.errorInfo = errorText


class NET_ERROR_CTRL_DECODER_TOUR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 357
        self.errorInfo = errorText


class NET_GROUP_OVERSUPPORTNUM(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 358
        self.errorInfo = errorText


class NET_USER_OVERSUPPORTNUM(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 359
        self.errorInfo = errorText


class NET_ERROR_GET_SIP_CFG(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 368
        self.errorInfo = errorText


class NET_ERROR_SET_SIP_CFG(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 369
        self.errorInfo = errorText


class NET_ERROR_GET_SIP_ABILITY(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 370
        self.errorInfo = errorText


class NET_ERROR_GET_WIFI_AP_CFG(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 371
        self.errorInfo = errorText


class NET_ERROR_SET_WIFI_AP_CFG(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 372
        self.errorInfo = errorText


class NET_ERROR_GET_DECODE_POLICY(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 373
        self.errorInfo = errorText


class NET_ERROR_SET_DECODE_POLICY(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 374
        self.errorInfo = errorText


class NET_ERROR_TALK_REJECT(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 375
        self.errorInfo = errorText


class NET_ERROR_TALK_OPENED(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 376
        self.errorInfo = errorText


class NET_ERROR_TALK_RESOURCE_CONFLICIT(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 377
        self.errorInfo = errorText


class NET_ERROR_TALK_UNSUPPORTED_ENCODE(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 378
        self.errorInfo = errorText


class NET_ERROR_TALK_RIGHTLESS(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 379
        self.errorInfo = errorText


class NET_ERROR_TALK_FAILED(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 380
        self.errorInfo = errorText


class NET_ERROR_GET_MACHINE_CFG(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 381
        self.errorInfo = errorText


class NET_ERROR_SET_MACHINE_CFG(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 382
        self.errorInfo = errorText


class NET_ERROR_GET_DATA_FAILED(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 383
        self.errorInfo = errorText


class NET_ERROR_MAC_VALIDATE_FAILED(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 384
        self.errorInfo = errorText


class NET_ERROR_GET_INSTANCE(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 385
        self.errorInfo = errorText


class NET_ERROR_JSON_REQUEST(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 386
        self.errorInfo = errorText


class NET_ERROR_JSON_RESPONSE(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 387
        self.errorInfo = errorText


class NET_ERROR_VERSION_HIGHER(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 388
        self.errorInfo = errorText


class NET_SPARE_NO_CAPACITY(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 389
        self.errorInfo = errorText


class NET_ERROR_SOURCE_IN_USE(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 390
        self.errorInfo = errorText


class NET_ERROR_REAVE(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 391
        self.errorInfo = errorText


class NET_ERROR_NETFORBID(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 392
        self.errorInfo = errorText


class NET_ERROR_GETCFG_MACFILTER(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 393
        self.errorInfo = errorText


class NET_ERROR_SETCFG_MACFILTER(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 394
        self.errorInfo = errorText


class NET_ERROR_GETCFG_IPMACFILTER(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 395
        self.errorInfo = errorText


class NET_ERROR_SETCFG_IPMACFILTER(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 396
        self.errorInfo = errorText


class NET_ERROR_OPERATION_OVERTIME(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 397
        self.errorInfo = errorText


class NET_ERROR_SENIOR_VALIDATE_FAILED(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 398
        self.errorInfo = errorText


class NET_ERROR_DEVICE_ID_NOT_EXIST(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 399
        self.errorInfo = errorText


class NET_ERROR_UNSUPPORTED(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 400
        self.errorInfo = errorText


class NET_ERROR_PROXY_DLLLOAD(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 401
        self.errorInfo = errorText


class NET_ERROR_PROXY_ILLEGAL_PARAM(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 402
        self.errorInfo = errorText


class NET_ERROR_PROXY_INVALID_HANDLE(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 403
        self.errorInfo = errorText


class NET_ERROR_PROXY_LOGIN_DEVICE_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 404
        self.errorInfo = errorText


class NET_ERROR_PROXY_START_SERVER_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 405
        self.errorInfo = errorText


class NET_ERROR_SPEAK_FAILED(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 406
        self.errorInfo = errorText


class NET_ERROR_NOT_SUPPORT_F6(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 407
        self.errorInfo = errorText


class NET_ERROR_CD_UNREADY(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 408
        self.errorInfo = errorText


class NET_ERROR_DIR_NOT_EXIST(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 409
        self.errorInfo = errorText


class NET_ERROR_UNSUPPORTED_SPLIT_MODE(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 410
        self.errorInfo = errorText


class NET_ERROR_OPEN_WND_PARAM(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 411
        self.errorInfo = errorText


class NET_ERROR_LIMITED_WND_COUNT(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 412
        self.errorInfo = errorText


class NET_ERROR_UNMATCHED_REQUEST(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 413
        self.errorInfo = errorText


class NET_RENDER_ENABLELARGEPICADJUSTMENT_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 414
        self.errorInfo = errorText


class NET_ERROR_UPGRADE_FAILED(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 415
        self.errorInfo = errorText


class NET_ERROR_NO_TARGET_DEVICE(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 416
        self.errorInfo = errorText


class NET_ERROR_NO_VERIFY_DEVICE(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 417
        self.errorInfo = errorText


class NET_ERROR_CASCADE_RIGHTLESS(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 418
        self.errorInfo = errorText


class NET_ERROR_LOW_PRIORITY(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 419
        self.errorInfo = errorText


class NET_ERROR_REMOTE_REQUEST_TIMEOUT(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 420
        self.errorInfo = errorText


class NET_ERROR_LIMITED_INPUT_SOURCE(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 421
        self.errorInfo = errorText


class NET_ERROR_SET_LOG_PRINT_INFO(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 422
        self.errorInfo = errorText


class NET_ERROR_PARAM_DWSIZE_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 423
        self.errorInfo = errorText


class NET_ERROR_LIMITED_MONITORWALL_COUNT(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 424
        self.errorInfo = errorText


class NET_ERROR_PART_PROCESS_FAILED(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 425
        self.errorInfo = errorText


class NET_ERROR_TARGET_NOT_SUPPORT(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 426
        self.errorInfo = errorText


class NET_ERROR_VISITE_FILE(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 510
        self.errorInfo = errorText


class NET_ERROR_DEVICE_STATUS_BUSY(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 511
        self.errorInfo = errorText


class NET_USER_PWD_NOT_AUTHORIZED(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 512
        self.errorInfo = errorText


class NET_USER_PWD_NOT_STRONG(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 513
        self.errorInfo = errorText


class NET_ERROR_NO_SUCH_CONFIG(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 514
        self.errorInfo = errorText


class NET_ERROR_AUDIO_RECORD_FAILED(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 515
        self.errorInfo = errorText


class NET_ERROR_SEND_DATA_FAILED(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 516
        self.errorInfo = errorText


class NET_ERROR_OBSOLESCENT_INTERFACE(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 517
        self.errorInfo = errorText


class NET_ERROR_INSUFFICIENT_INTERAL_BUF(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 518
        self.errorInfo = errorText


class NET_ERROR_NEED_ENCRYPTION_PASSWORD(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 519
        self.errorInfo = errorText


class NET_ERROR_NOSUPPORT_RECORD(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 520
        self.errorInfo = errorText


class NET_ERROR_DEVICE_IN_UPGRADING(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 521
        self.errorInfo = errorText


class NET_ERROR_ANALYSE_TASK_NOT_EXIST(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 522
        self.errorInfo = errorText


class NET_ERROR_ANALYSE_TASK_FULL(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 523
        self.errorInfo = errorText


class NET_ERROR_DEVICE_RESTART(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 524
        self.errorInfo = errorText


class NET_ERROR_DEVICE_SHUTDOWN(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 525
        self.errorInfo = errorText


class NET_ERROR_FILE_SYSTEM_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 526
        self.errorInfo = errorText


class NET_ERROR_HARDDISK_WRITE_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 527
        self.errorInfo = errorText


class NET_ERROR_HARDDISK_READ_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 528
        self.errorInfo = errorText


class NET_ERROR_NO_HARDDISK_RECORD_LOG(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 529
        self.errorInfo = errorText


class NET_ERROR_NO_HARDDISK(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 530
        self.errorInfo = errorText


class NET_ERROR_HARDDISK_OTHER_ERRORS(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 531
        self.errorInfo = errorText


class NET_ERROR_HARDDISK_BADSECTORS_MINOR_ERRORS(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 532
        self.errorInfo = errorText


class NET_ERROR_HARDDISK_BADSECTORS_CRITICAL_ERRORS(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 533
        self.errorInfo = errorText


class NET_ERROR_HARDDISK_PHYSICAL_BADSECTORS_SLIGHT(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 534
        self.errorInfo = errorText


class NET_ERROR_HARDDISK_PHYSICAL_BADSECTORS_SERIOUS(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 535
        self.errorInfo = errorText


class NET_ERROR_NETWORK_DISCONNECTION_ALARM(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 536
        self.errorInfo = errorText


class NET_ERROR_NETWORK_DISCONNECTION(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 537
        self.errorInfo = errorText


class NET_ERROR_SET_SOURCE_EXCEED(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 538
        self.errorInfo = errorText


class NET_ERROR_SIZE_EXCEED(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 539
        self.errorInfo = errorText


class NET_ERROR_LOGOPEN_DISABLE(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 540
        self.errorInfo = errorText


class NET_ERROR_STREAM_PACKAGE_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 541
        self.errorInfo = errorText


class NET_ERROR_SERIALIZE_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1010
        self.errorInfo = errorText


class NET_ERROR_DESERIALIZE_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1011
        self.errorInfo = errorText


class NET_ERROR_LOWRATEWPAN_ID_EXISTED(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1012
        self.errorInfo = errorText


class NET_ERROR_LOWRATEWPAN_ID_LIMIT(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1013
        self.errorInfo = errorText


class NET_ERROR_LOWRATEWPAN_ID_ABNORMAL(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1014
        self.errorInfo = errorText


class NET_ERROR_ENCRYPT(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1015
        self.errorInfo = errorText


class NET_ERROR_PWD_ILLEGAL(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1016
        self.errorInfo = errorText


class NET_ERROR_DEVICE_ALREADY_INIT(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1017
        self.errorInfo = errorText


class NET_ERROR_SECURITY_CODE(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1018
        self.errorInfo = errorText


class NET_ERROR_SECURITY_CODE_TIMEOUT(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1019
        self.errorInfo = errorText


class NET_ERROR_GET_PWD_SPECI(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1020
        self.errorInfo = errorText


class NET_ERROR_NO_AUTHORITY_OF_OPERATION(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1021
        self.errorInfo = errorText


class NET_ERROR_DECRYPT(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1022
        self.errorInfo = errorText


class NET_ERROR_2D_CODE(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1023
        self.errorInfo = errorText


class NET_ERROR_INVALID_REQUEST(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1024
        self.errorInfo = errorText


class NET_ERROR_PWD_RESET_DISABLE(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1025
        self.errorInfo = errorText


class NET_ERROR_PLAY_PRIVATE_DATA(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1026
        self.errorInfo = errorText


class NET_ERROR_ROBOT_OPERATE_FAILED(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1027
        self.errorInfo = errorText


class NET_ERROR_PHOTOSIZE_EXCEEDSLIMIT(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1028
        self.errorInfo = errorText


class NET_ERROR_USERID_INVALID(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1029
        self.errorInfo = errorText


class NET_ERROR_EXTRACTFEATURE_FAILED(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1030
        self.errorInfo = errorText


class NET_ERROR_PHOTO_EXIST(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1031
        self.errorInfo = errorText


class NET_ERROR_PHOTO_OVERFLOW(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1032
        self.errorInfo = errorText


class NET_ERROR_CHANNEL_ALREADY_OPENED(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1033
        self.errorInfo = errorText


class NET_ERROR_CREATE_SOCKET(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1034
        self.errorInfo = errorText


class NET_ERROR_CHANNEL_NUM(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1035
        self.errorInfo = errorText


class NET_ERROR_PHOTO_FORMAT(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1036
        self.errorInfo = errorText


class NET_ERROR_DIGITAL_CERTIFICATE_INTERNAL_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1037
        self.errorInfo = errorText


class NET_ERROR_DIGITAL_CERTIFICATE_GET_ID_FAILED(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1038
        self.errorInfo = errorText


class NET_ERROR_DIGITAL_CERTIFICATE_IMPORT_ILLEGAL(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1039
        self.errorInfo = errorText


class NET_ERROR_DIGITAL_CERTIFICATE_SN_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1040
        self.errorInfo = errorText


class NET_ERROR_DIGITAL_CERTIFICATE_COMMON_NAME_ILLEGAL(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1041
        self.errorInfo = errorText


class NET_ERROR_DIGITAL_CERTIFICATE_NO_ROOT_CERT(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1042
        self.errorInfo = errorText


class NET_ERROR_DIGITAL_CERTIFICATE_CERT_REVOKED(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1043
        self.errorInfo = errorText


class NET_ERROR_DIGITAL_CERTIFICATE_CERT_INVALID(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1044
        self.errorInfo = errorText


class NET_ERROR_DIGITAL_CERTIFICATE_CERT_ERROR_SIGN(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1045
        self.errorInfo = errorText


class NET_ERROR_DIGITAL_CERTIFICATE_COUNTS_UPPER_LIMIT(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1046
        self.errorInfo = errorText


class NET_ERROR_DIGITAL_CERTIFICATE_CERT_NO_EXIST(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1047
        self.errorInfo = errorText


class NET_ERROR_DEFULAT_SEARCH_PORT(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1048
        self.errorInfo = errorText


class NET_ERROR_FACE_RECOGNITION_SERVER_MULTI_APPEND_STOUP(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1049
        self.errorInfo = errorText


class NET_ERROR_FACE_RECOGNITION_SERVER_MULTI_APPEND_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1050
        self.errorInfo = errorText


class NET_ERROR_FACE_RECOGNITION_SERVER_GROUP_ID_EXCEED(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1051
        self.errorInfo = errorText


class NET_ERROR_FACE_RECOGNITION_SERVER_GROUP_ID_NOT_IN_REGISTER_GROUP(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1052
        self.errorInfo = errorText


class NET_ERROR_FACE_RECOGNITION_SERVER_PICTURE_NOT_FOUND(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1053
        self.errorInfo = errorText


class NET_ERROR_FACE_RECOGNITION_SERVER_GENERATE_GROUP_ID_FAILED(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1054
        self.errorInfo = errorText


class NET_ERROR_FACE_RECOGNITION_SERVER_SET_CONFIG_FAILED(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1055
        self.errorInfo = errorText


class NET_ERROR_FACE_RECOGNITION_SERVER_FILE_OPEN_FAILED(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1056
        self.errorInfo = errorText


class NET_ERROR_FACE_RECOGNITION_SERVER_FILE_READ_FAILED(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1057
        self.errorInfo = errorText


class NET_ERROR_FACE_RECOGNITION_SERVER_FILE_WRITE_FAILED(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1058
        self.errorInfo = errorText


class NET_ERROR_FACE_RECOGNITION_SERVER_PICTURE_DPI_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1059
        self.errorInfo = errorText


class NET_ERROR_FACE_RECOGNITION_SERVER_PICTURE_PX_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1060
        self.errorInfo = errorText


class NET_ERROR_FACE_RECOGNITION_SERVER_PICTURE_SIZE_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1061
        self.errorInfo = errorText


class NET_ERROR_FACE_RECOGNITION_SERVER_DATA_BASE_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1062
        self.errorInfo = errorText


class NET_ERROR_FACE_RECOGNITION_SERVER_FACE_MAX_NUM(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1063
        self.errorInfo = errorText


class NET_ERROR_FACE_RECOGNITION_SERVER_BIRTH_DAY_FORMAT_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1064
        self.errorInfo = errorText


class NET_ERROR_FACE_RECOGNITION_SERVER_UID_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1065
        self.errorInfo = errorText


class NET_ERROR_FACE_RECOGNITION_SERVER_TOKEN_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1066
        self.errorInfo = errorText


class NET_ERROR_FACE_RECOGNITION_SERVER_BEGIN_NUM_OVER_RUN(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1067
        self.errorInfo = errorText


class NET_ERROR_FACE_RECOGNITION_SERVER_ABSTRACT_NUM_ZERO(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1068
        self.errorInfo = errorText


class NET_ERROR_FACE_RECOGNITION_SERVER_ABSTRACT_INIT_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1069
        self.errorInfo = errorText


class NET_ERROR_FACE_RECOGNITION_SERVER_AUTO_ABSTRACT_STATE(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1070
        self.errorInfo = errorText


class NET_ERROR_FACE_RECOGNITION_SERVER_ABSTRACT_STATE(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1071
        self.errorInfo = errorText


class NET_ERROR_FACE_RECOGNITION_SERVER_IM_EX_STATE(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1072
        self.errorInfo = errorText


class NET_ERROR_FACE_RECOGNITION_SERVER_PIC_WRITE_FAILED(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1073
        self.errorInfo = errorText


class NET_ERROR_FACE_RECOGNITION_SERVER_GROUP_SPACE_EXCEED(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1074
        self.errorInfo = errorText


class NET_ERROR_FACE_RECOGNITION_SERVER_GROUP_PIC_COUNT_EXCEED(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1075
        self.errorInfo = errorText


class NET_ERROR_FACE_RECOGNITION_SERVER_GROUP_NOT_FOUND(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1076
        self.errorInfo = errorText


class NET_ERROR_FACE_RECOGNITION_SERVER_FIND_RECORDS_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1077
        self.errorInfo = errorText


class NET_ERROR_FACE_RECOGNITION_SERVER_DELETE_PERSON_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1078
        self.errorInfo = errorText


class NET_ERROR_DEVICE_PARSE_PROTOCOL(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1079
        tempErrorInfo = "错误码索引重复了，该错误码所对应的另一个类型为NET_ERROR_FACE_RECOGNITION_SERVER_DELETE_GROUP_ERROR"
        self.errorInfo = tempErrorInfo + "\n" + str(errorText) if errorText else tempErrorInfo


class NET_ERROR_DEVICE_INVALID_REQUEST(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1080
        tempErrorInfo = "错误码索引重复了，该错误码所对应的另一个类型为NET_ERROR_FACE_RECOGNITION_SERVER_NAME_FORMAT_ERROR"
        self.errorInfo = tempErrorInfo + "\n" + str(errorText) if errorText else tempErrorInfo


class NET_ERROR_DEVICE_INTERNAL_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1081
        tempErrorInfo = "错误码索引重复了，该错误码所对应的另一个类型为NET_ERROR_FACE_RECOGNITION_SERVER_FILEPATH_NOT_SET"
        self.errorInfo = tempErrorInfo + "\n" + str(errorText) if errorText else tempErrorInfo


class NET_ERROR_DEVICE_REQUEST_TIMEOUT(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1082
        self.errorInfo = errorText


class NET_ERROR_DEVICE_KEEPALIVE_FAIL(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1083
        self.errorInfo = errorText


class NET_ERROR_DEVICE_NETWORK_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1084
        self.errorInfo = errorText


class NET_ERROR_DEVICE_UNKNOWN_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1085
        self.errorInfo = errorText


class NET_ERROR_DEVICE_COM_INTERFACE_NOTFOUND(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1086
        self.errorInfo = errorText


class NET_ERROR_DEVICE_COM_IMPLEMENT_NOTFOUND(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1087
        self.errorInfo = errorText


class NET_ERROR_DEVICE_COM_NOTFOUND(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1088
        self.errorInfo = errorText


class NET_ERROR_DEVICE_COM_INSTANCE_NOTEXIST(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1089
        self.errorInfo = errorText


class NET_ERROR_DEVICE_CREATE_COM_FAIL(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1090
        self.errorInfo = errorText


class NET_ERROR_DEVICE_GET_COM_FAIL(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1091
        self.errorInfo = errorText


class NET_ERROR_DEVICE_BAD_REQUEST(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1092
        self.errorInfo = errorText


class NET_ERROR_DEVICE_REQUEST_IN_PROGRESS(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1093
        self.errorInfo = errorText


class NET_ERROR_DEVICE_LIMITED_RESOURCE(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1094
        self.errorInfo = errorText


class NET_ERROR_DEVICE_BUSINESS_TIMEOUT(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1095
        self.errorInfo = errorText


class NET_ERROR_DEVICE_TOO_MANY_REQUESTS(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1096
        self.errorInfo = errorText


class NET_ERROR_DEVICE_NOT_ALREADY(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1097
        self.errorInfo = errorText


class NET_ERROR_DEVICE_SEARCHRECORD_TIMEOUT(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1098
        self.errorInfo = errorText


class NET_ERROR_DEVICE_SEARCHTIME_INVALID(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1099
        self.errorInfo = errorText


class NET_ERROR_DEVICE_SSID_INVALID(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1100
        self.errorInfo = errorText


class NET_ERROR_DEVICE_CHANNEL_STREAMTYPE_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1101
        self.errorInfo = errorText


class NET_ERROR_DEVICE_STREAM_PACKINGFORMAT_UNSUPPORT(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1102
        self.errorInfo = errorText


class NET_ERROR_DEVICE_AUDIO_ENCODINGFORMAT_UNSUPPORT(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1103
        self.errorInfo = errorText


class NET_ERROR_SECURITY_ERROR_SUPPORT_GUI(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1104
        self.errorInfo = errorText


class NET_ERROR_SECURITY_ERROR_SUPPORT_MULT(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1105
        self.errorInfo = errorText


class NET_ERROR_SECURITY_ERROR_SUPPORT_UNIQUE(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1106
        self.errorInfo = errorText


class NET_ERROR_STREAMCONVERTOR_DEFECT(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1107
        self.errorInfo = errorText


class NET_ERROR_SECURITY_GENERATE_SAFE_CODE(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1108
        self.errorInfo = errorText


class NET_ERROR_SECURITY_GET_CONTACT(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1109
        self.errorInfo = errorText


class NET_ERROR_SECURITY_GET_QRCODE(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1110
        self.errorInfo = errorText


class NET_ERROR_SECURITY_CANNOT_RESET(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1111
        self.errorInfo = errorText


class NET_ERROR_SECURITY_NOT_SUPPORT_CONTACT_MODE(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1112
        self.errorInfo = errorText


class NET_ERROR_SECURITY_RESPONSE_TIMEOUT(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1113
        self.errorInfo = errorText


class NET_ERROR_SECURITY_AUTHCODE_FORBIDDEN(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1114
        self.errorInfo = errorText


class NET_ERROR_TRANCODE_LOGIN_REMOTE_DEV(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1115
        self.errorInfo = errorText


class NET_ERROR_TRANCODE_NOFREE_CHANNEL(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1116
        self.errorInfo = errorText


class NET_ERROR_VK_INFO_DECRYPT_FAILED(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1117
        self.errorInfo = errorText


class NET_ERROR_VK_INFO_DESERIALIZE_FAILED(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1118
        self.errorInfo = errorText


class NET_ERROR_GDPR_ABILITY_NOT_ENABLE(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1119
        self.errorInfo = errorText


class NET_ERROR_FAST_CHECK_NO_AUTH(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1120
        self.errorInfo = errorText


class NET_ERROR_FAST_CHECK_NO_FILE(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1121
        self.errorInfo = errorText


class NET_ERROR_FAST_CHECK_FILE_FAIL(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1122
        self.errorInfo = errorText


class NET_ERROR_FAST_CHECK_BUSY(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1123
        self.errorInfo = errorText


class NET_ERROR_FAST_CHECK_NO_PASSWORD(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1124
        self.errorInfo = errorText


class NET_ERROR_IMPORT_ACCESS_SEND_FAILD(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1125
        self.errorInfo = errorText


class NET_ERROR_IMPORT_ACCESS_BUSY(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1126
        self.errorInfo = errorText


class NET_ERROR_IMPORT_ACCESS_DATAERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1127
        self.errorInfo = errorText


class NET_ERROR_IMPORT_ACCESS_DATAINVALID(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1128
        self.errorInfo = errorText


class NET_ERROR_IMPORT_ACCESS_SYNC_FALID(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1129
        self.errorInfo = errorText


class NET_ERROR_IMPORT_ACCESS_DBFULL(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1130
        self.errorInfo = errorText


class NET_ERROR_IMPORT_ACCESS_SDFULL(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1131
        self.errorInfo = errorText


class NET_ERROR_IMPORT_ACCESS_CIPHER_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1132
        self.errorInfo = errorText


class NET_ERROR_INVALID_PARAM(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1133
        self.errorInfo = errorText


class NET_ERROR_INVALID_PASSWORD(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1134
        self.errorInfo = errorText


class NET_ERROR_INVALID_FINGERPRINT(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1135
        self.errorInfo = errorText


class NET_ERROR_INVALID_FACE(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1136
        self.errorInfo = errorText


class NET_ERROR_INVALID_CARD(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1137
        self.errorInfo = errorText


class NET_ERROR_INVALID_USER(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1138
        self.errorInfo = errorText


class NET_ERROR_GET_SUBSERVICE(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1139
        self.errorInfo = errorText


class NET_ERROR_GET_METHOD(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1140
        self.errorInfo = errorText


class NET_ERROR_GET_SUBCAPS(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1141
        self.errorInfo = errorText


class NET_ERROR_UPTO_INSERT_LIMIT(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1142
        self.errorInfo = errorText


class NET_ERROR_UPTO_MAX_INSERT_RATE(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1143
        self.errorInfo = errorText


class NET_ERROR_ERASE_FINGERPRINT(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1144
        self.errorInfo = errorText


class NET_ERROR_ERASE_FACE(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1145
        self.errorInfo = errorText


class NET_ERROR_ERASE_CARD(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1146
        self.errorInfo = errorText


class NET_ERROR_NO_RECORD(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1147
        self.errorInfo = errorText


class NET_ERROR_NOMORE_RECORDS(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1148
        self.errorInfo = errorText


class NET_ERROR_RECORD_ALREADY_EXISTS(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1149
        self.errorInfo = errorText


class NET_ERROR_EXCEED_MAX_FINGERPRINT_PERUSER(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1150
        self.errorInfo = errorText


class NET_ERROR_EXCEED_MAX_CARD_PERUSER(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1151
        self.errorInfo = errorText


class NET_ERROR_EXCEED_ADMINISTRATOR_LIMIT(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1152
        self.errorInfo = errorText


class NET_LOGIN_ERROR_DEVICE_NOT_SUPPORT_HIGHLEVEL_SECURITY_LOGIN(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1153
        self.errorInfo = errorText


class NET_LOGIN_ERROR_DEVICE_ONLY_SUPPORT_HIGHLEVEL_SECURITY_LOGIN(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1154
        self.errorInfo = errorText


class NET_ERROR_VIDEO_CHANNEL_OFFLINE(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1155
        self.errorInfo = errorText


class NET_ERROR_USERID_FORMAT_INCORRECT(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1156
        self.errorInfo = errorText


class NET_ERROR_CANNOT_FIND_CHANNEL_RELATE_TO_SN(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1157
        self.errorInfo = errorText


class NET_ERROR_TASK_QUEUE_OF_CHANNEL_IS_FULL(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1158
        self.errorInfo = errorText


class NET_ERROR_APPLY_USER_INFO_BLOCK_FAIL(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1159
        self.errorInfo = errorText


class NET_ERROR_EXCEED_MAX_PASSWD_PERUSER(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1160
        self.errorInfo = errorText


class NET_ERROR_PARSE_PROTOCOL(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1161
        self.errorInfo = errorText


class NET_ERROR_CARD_NUM_EXIST(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1162
        self.errorInfo = errorText


class NET_ERROR_FINGERPRINT_EXIST(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1163
        self.errorInfo = errorText


class NET_ERROR_OPEN_PLAYGROUP_FAIL(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1164
        self.errorInfo = errorText


class NET_ERROR_ALREADY_IN_PLAYGROUP(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1165
        self.errorInfo = errorText


class NET_ERROR_QUERY_PLAYGROUP_TIME_FAIL(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1166
        self.errorInfo = errorText


class NET_ERROR_SET_PLAYGROUP_BASECHANNEL_FAIL(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1167
        self.errorInfo = errorText


class NET_ERROR_SET_PLAYGROUP_DIRECTION_FAIL(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1168
        self.errorInfo = errorText


class NET_ERROR_SET_PLAYGROUP_SPEED_FAIL(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1169
        self.errorInfo = errorText


class NET_ERROR_ADD_PLAYGROUP_FAIL(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1170
        self.errorInfo = errorText


class NET_ERROR_EXPORT_AOL_LOGFILE_NO_AUTH(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1171
        self.errorInfo = errorText


class NET_ERROR_EXPORT_AOL_LOGFILE_NO_FILE(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1172
        self.errorInfo = errorText


class NET_ERROR_EXPORT_AOL_LOGFILE_FILE_FAIL(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1173
        self.errorInfo = errorText


class NET_ERROR_EXPORT_AOL_LOGFILE_BUSY(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1174
        self.errorInfo = errorText


class NET_ERROR_EMPTY_LICENSE(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1175
        self.errorInfo = errorText


class NET_ERROR_UNSUPPORTED_MODE(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1176
        self.errorInfo = errorText


class NET_ERROR_URL_APP_NOT_MATCH(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1177
        self.errorInfo = errorText


class NET_ERROR_READ_INFO_FAILED(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1178
        self.errorInfo = errorText


class NET_ERROR_WRITE_FAILED(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1179
        self.errorInfo = errorText


class NET_ERROR_NO_SUCH_APP(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1180
        self.errorInfo = errorText


class NET_ERROR_VERIFIF_FAILED(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1181
        self.errorInfo = errorText


class NET_ERROR_LICENSE_OUT_DATE(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1182
        self.errorInfo = errorText


class NET_ERROR_UPGRADE_PROGRAM_TOO_OLD(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1183
        self.errorInfo = errorText


class NET_ERROR_SECURE_TRANSMIT_BEEN_CUT(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1184
        self.errorInfo = errorText


class NET_ERROR_DEVICE_NOT_SUPPORT_SECURE_TRANSMIT(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1185
        self.errorInfo = errorText


class NET_ERROR_EXTRA_STREAM_LOGIN_FAIL_CAUSE_BY_MAIN_STREAM(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1186
        self.errorInfo = errorText


class NET_ERROR_EXTRA_STREAM_CLOSED_BY_REMOTE_DEVICE(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1187
        self.errorInfo = errorText


class NET_ERROR_IMPORT_FACEDB_SEND_FAILD(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1188
        self.errorInfo = errorText


class NET_ERROR_IMPORT_FACEDB_BUSY(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1189
        self.errorInfo = errorText


class NET_ERROR_IMPORT_FACEDB_DATAERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1190
        self.errorInfo = errorText


class NET_ERROR_IMPORT_FACEDB_DATAINVALID(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1191
        self.errorInfo = errorText


class NET_ERROR_IMPORT_FACEDB_UPGRADE_FAILD(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1192
        self.errorInfo = errorText


class NET_ERROR_IMPORT_FACEDB_NO_AUTHORITY(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1193
        self.errorInfo = errorText


class NET_ERROR_IMPORT_FACEDB_ABNORMAL_FILE(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1194
        self.errorInfo = errorText


class NET_ERROR_IMPORT_FACEDB_SYNC_FALID(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1195
        self.errorInfo = errorText


class NET_ERROR_IMPORT_FACEDB_DBFULL(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1196
        self.errorInfo = errorText


class NET_ERROR_IMPORT_FACEDB_SDFULL(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1197
        self.errorInfo = errorText


class NET_ERROR_IMPORT_FACEDB_CIPHER_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1198
        self.errorInfo = errorText


class NET_ERROR_EXPORT_FACEDB_NO_AUTH(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1199
        self.errorInfo = errorText


class NET_ERROR_EXPORT_FACEDB_NO_FILE(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1200
        self.errorInfo = errorText


class NET_ERROR_EXPORT_FACEDB_FILE_FAIL(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1201
        self.errorInfo = errorText


class NET_ERROR_EXPORT_FACEDB_BUSY(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1202
        self.errorInfo = errorText


class NET_ERROR_EXPORT_FACEDB_NO_PASSWORD(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1203
        self.errorInfo = errorText


class NET_ERROR_REQUESTED_TOO_MUCH_DATA(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1204
        self.errorInfo = errorText


class NET_ERROR_BATCH_PROCESS_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1205
        self.errorInfo = errorText


class NET_ERROR_OPERATION_CANCELLED(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1206
        self.errorInfo = errorText


class NET_ERROR_DEVICE_INVALID(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1207
        self.errorInfo = errorText


class NET_ERROR_DEVICE_UNAVAILABLE(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1208
        self.errorInfo = errorText


class NET_ERROR_FINGERPRINT_DOWNLOAD_FAIL(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1209
        self.errorInfo = errorText


class NET_ERROR_ACCOUNT_IN_USE(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1210
        self.errorInfo = errorText


class NET_ERROR_IRIS_INFO_NOT_EXISTED(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1211
        self.errorInfo = errorText


class NET_ERROR_INVALID_IRIS_DATA(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1212
        self.errorInfo = errorText


class NET_ERROR_IRIS_ALREADY_EXIST(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1213
        self.errorInfo = errorText


class NET_ERROR_ERASE_IRIS_FAILED(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1214
        self.errorInfo = errorText


class NET_ERROR_EXCEED_MAX_IRIS_GROUP_COUNT_PER_USER(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1215
        self.errorInfo = errorText


class NET_ERROR_EXCEED_MAX_IRIS_COUNT_PER_GROUP(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1216
        self.errorInfo = errorText


class NET_ERROR_FACEMANAGER_NO_FACE_DETECTED(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1300
        self.errorInfo = errorText


class NET_ERROR_FACEMANAGER_MULTI_FACE_DETECTED(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1301
        self.errorInfo = errorText


class NET_ERROR_FACEMANAGER_PICTURE_DECODING_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1302
        self.errorInfo = errorText


class NET_ERROR_FACEMANAGER_LOW_PICTURE_QUALITY(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1303
        self.errorInfo = errorText


class NET_ERROR_FACEMANAGER_NOT_RECOMMENDED(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1304
        self.errorInfo = errorText


class NET_ERROR_FACEMANAGER_FACE_FEATURE_ALREADY_EXIST(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1305
        self.errorInfo = errorText


class NET_ERROR_FACEMANAGER_FACE_ANGLE_OVER_THRESHOLDS(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1307
        self.errorInfo = errorText


class NET_ERROR_FACEMANAGER_FACE_RADIO_EXCEEDS_RANGE(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1308
        self.errorInfo = errorText


class NET_ERROR_FACEMANAGER_FACE_OVER_EXPOSED(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1309
        self.errorInfo = errorText


class NET_ERROR_FACEMANAGER_FACE_UNDER_EXPOSED(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1310
        self.errorInfo = errorText


class NET_ERROR_FACEMANAGER_BRIGHTNESS_IMBALANCE(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1311
        self.errorInfo = errorText


class NET_ERROR_FACEMANAGER_FACE_LOWER_CONFIDENCE(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1312
        self.errorInfo = errorText


class NET_ERROR_FACEMANAGER_FACE_LOW_ALIGN(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1313
        self.errorInfo = errorText


class NET_ERROR_FACEMANAGER_FRAGMENTARY_FACE_DETECTED(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1314
        self.errorInfo = errorText


class NET_ERROR_FACEMANAGER_PUPIL_DISTANCE_NOT_ENOUGH(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1315
        self.errorInfo = errorText


class NET_ERROR_FACEMANAGER_FACE_DATA_DOWNLOAD_FAILED(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1316
        self.errorInfo = errorText


class NET_ERROR_CITIZENMANAGER_ERROR_WORKINGMODE_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1317
        self.errorInfo = errorText


class NET_ERROR_CITIZENMANAGER_ERROR_CAPTURE_BUSY(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1318
        self.errorInfo = errorText


class NET_ERROR_CITIZENMANAGER_ERROR_CAPTURE_TYPE_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1319
        self.errorInfo = errorText


class NET_ERROR_NORMAL_USER_NOTSUPPORT(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1320
        self.errorInfo = errorText


class NET_ERROR_THERMOGRAPHY_REF_SENSOR_OPEN_INVALID(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1321
        self.errorInfo = errorText


class NET_ERROR_THERMOGRAPHY_REF_DELAY_SHUT_DOWN_INVALID(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1322
        self.errorInfo = errorText


class NET_ERROR_CITIZENID_EXIST(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1323
        self.errorInfo = errorText


class NET_ERROR_FACEMANAGER_FACE_FFE_FAILED(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1324
        self.errorInfo = errorText


class NET_ERROR_FACEMANAGER_PHOTO_FEATURE_FAILED_FOR_FA(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1325
        self.errorInfo = errorText


class NET_ERROR_FACEMANAGER_FACE_DATA_PHOTO_INCOMPLETE(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1326
        self.errorInfo = errorText


class NET_ERROR_DATABASE_ERROR_INSERT_OVERFLOW(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1327
        self.errorInfo = errorText


class NET_ERROR_WORKSUIT_COMPARE_SERVER_GROUPID_EXCEED(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1328
        self.errorInfo = errorText


class NET_ERROR_WORKSUIT_COMPARE_SERVER_ABSTRACT_INIT_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1329
        self.errorInfo = errorText


class NET_ERROR_WORKSUIT_COMPARE_SERVER_GROUPID_NOT_FOUND(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1330
        self.errorInfo = errorText


class NET_ERROR_WORKSUIT_COMPARE_SERVER_DATABASE_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1331
        self.errorInfo = errorText


class NET_ERROR_WORKSUIT_COMPARE_SERVER_TOKEN_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1332
        self.errorInfo = errorText


class NET_ERROR_WORKSUIT_COMPARE_SERVER_BEGINNUM_OVERRUN(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1333
        self.errorInfo = errorText


class NET_ERROR_WORKSUIT_COMPARE_SERVER_ABSTRACT_STATE(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1334
        self.errorInfo = errorText


class NET_ERROR_WORKSUIT_COMPARE_SERVER_BIGPIC_MAXNUM(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1335
        self.errorInfo = errorText


class NET_ERROR_WORKSUIT_COMPARE_SERVER_OBJECT_MAXNUM(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1336
        self.errorInfo = errorText


class NET_ERROR_WORKSUIT_COMPARE_SERVER_GROUP_SPACE_EXCEED(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1337
        self.errorInfo = errorText


class NET_ERROR_WORKSUIT_COMPARE_SERVER_ABSTRACTNUM_ZERO(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1338
        self.errorInfo = errorText


class NET_ERROR_WORKSUIT_COMPARE_SERVER_INVALID_PARAM(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1339
        self.errorInfo = errorText


class NET_ERROR_CARD_NOT_EXIST(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1340
        self.errorInfo = errorText


class NET_ERROR_TEMPORARY_OUTDATED(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1341
        self.errorInfo = errorText


class NET_SUBBIZ_INVALID_SOCKET(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1401
        self.errorInfo = errorText


class NET_SUBBIZ_PAUSE_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1402
        self.errorInfo = errorText


class NET_SUBBIZ_GET_PORT_ERROR(DHNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1403
        self.errorInfo = errorText


DHNetSDKExceptionDict = {
    0: NET_NOERROR,
    -1: NET_ERROR,
    1: NET_SYSTEM_ERROR,
    2: NET_NETWORK_ERROR,
    3: NET_DEV_VER_NOMATCH,
    4: NET_INVALID_HANDLE,
    5: NET_OPEN_CHANNEL_ERROR,
    6: NET_CLOSE_CHANNEL_ERROR,
    7: NET_ILLEGAL_PARAM,
    8: NET_SDK_INIT_ERROR,
    9: NET_SDK_UNINIT_ERROR,
    10: NET_RENDER_OPEN_ERROR,
    11: NET_DEC_OPEN_ERROR,
    12: NET_DEC_CLOSE_ERROR,
    13: NET_MULTIPLAY_NOCHANNEL,
    14: NET_TALK_INIT_ERROR,
    15: NET_TALK_NOT_INIT,
    16: NET_TALK_SENDDATA_ERROR,
    17: NET_REAL_ALREADY_SAVING,
    18: NET_NOT_SAVING,
    19: NET_OPEN_FILE_ERROR,
    20: NET_PTZ_SET_TIMER_ERROR,
    21: NET_RETURN_DATA_ERROR,
    22: NET_INSUFFICIENT_BUFFER,
    23: NET_NOT_SUPPORTED,
    24: NET_NO_RECORD_FOUND,
    25: NET_NOT_AUTHORIZED,
    26: NET_NOT_NOW,
    27: NET_NO_TALK_CHANNEL,
    28: NET_NO_AUDIO,
    29: NET_NO_INIT,
    30: NET_DOWNLOAD_END,
    31: NET_EMPTY_LIST,
    32: NET_ERROR_GETCFG_SYSATTR,
    33: NET_ERROR_GETCFG_SERIAL,
    34: NET_ERROR_GETCFG_GENERAL,
    35: NET_ERROR_GETCFG_DSPCAP,
    36: NET_ERROR_GETCFG_NETCFG,
    37: NET_ERROR_GETCFG_CHANNAME,
    38: NET_ERROR_GETCFG_VIDEO,
    39: NET_ERROR_GETCFG_RECORD,
    40: NET_ERROR_GETCFG_PRONAME,
    41: NET_ERROR_GETCFG_FUNCNAME,
    42: NET_ERROR_GETCFG_485DECODER,
    43: NET_ERROR_GETCFG_232COM,
    44: NET_ERROR_GETCFG_ALARMIN,
    45: NET_ERROR_GETCFG_ALARMDET,
    46: NET_ERROR_GETCFG_SYSTIME,
    47: NET_ERROR_GETCFG_PREVIEW,
    48: NET_ERROR_GETCFG_AUTOMT,
    49: NET_ERROR_GETCFG_VIDEOMTRX,
    50: NET_ERROR_GETCFG_COVER,
    51: NET_ERROR_GETCFG_WATERMAKE,
    52: NET_ERROR_GETCFG_MULTICAST,
    55: NET_ERROR_SETCFG_GENERAL,
    56: NET_ERROR_SETCFG_NETCFG,
    57: NET_ERROR_SETCFG_CHANNAME,
    58: NET_ERROR_SETCFG_VIDEO,
    59: NET_ERROR_SETCFG_RECORD,
    60: NET_ERROR_SETCFG_485DECODER,
    61: NET_ERROR_SETCFG_232COM,
    62: NET_ERROR_SETCFG_ALARMIN,
    63: NET_ERROR_SETCFG_ALARMDET,
    64: NET_ERROR_SETCFG_SYSTIME,
    65: NET_ERROR_SETCFG_PREVIEW,
    66: NET_ERROR_SETCFG_AUTOMT,
    67: NET_ERROR_SETCFG_VIDEOMTRX,
    68: NET_ERROR_SETCFG_COVER,
    69: NET_ERROR_SETCFG_WATERMAKE,
    70: NET_ERROR_SETCFG_WLAN,
    71: NET_ERROR_SETCFG_WLANDEV,
    72: NET_ERROR_SETCFG_REGISTER,
    73: NET_ERROR_SETCFG_CAMERA,
    74: NET_ERROR_SETCFG_INFRARED,
    75: NET_ERROR_SETCFG_SOUNDALARM,
    76: NET_ERROR_SETCFG_STORAGE,
    77: NET_AUDIOENCODE_NOTINIT,
    78: NET_DATA_TOOLONGH,
    79: NET_UNSUPPORTED,
    80: NET_DEVICE_BUSY,
    81: NET_SERVER_STARTED,
    82: NET_SERVER_STOPPED,
    83: NET_LISTER_INCORRECT_SERIAL,
    84: NET_QUERY_DISKINFO_FAILED,
    85: NET_ERROR_GETCFG_SESSION,
    86: NET_USER_FLASEPWD_TRYTIME,
    99: NET_LOGIN_ERROR_PASSWORD_EXPIRED,
    100: NET_LOGIN_ERROR_PASSWORD,
    101: NET_LOGIN_ERROR_USER,
    102: NET_LOGIN_ERROR_TIMEOUT,
    103: NET_LOGIN_ERROR_RELOGGIN,
    104: NET_LOGIN_ERROR_LOCKED,
    105: NET_LOGIN_ERROR_BLACKLIST,
    106: NET_LOGIN_ERROR_BUSY,
    107: NET_LOGIN_ERROR_CONNECT,
    108: NET_LOGIN_ERROR_NETWORK,
    109: NET_LOGIN_ERROR_SUBCONNECT,
    110: NET_LOGIN_ERROR_MAXCONNECT,
    111: NET_LOGIN_ERROR_PROTOCOL3_ONLY,
    112: NET_LOGIN_ERROR_UKEY_LOST,
    113: NET_LOGIN_ERROR_NO_AUTHORIZED,
    117: NET_LOGIN_ERROR_USER_OR_PASSOWRD,
    118: NET_LOGIN_ERROR_DEVICE_NOT_INIT,
    119: NET_LOGIN_ERROR_LIMITED,
    120: NET_RENDER_SOUND_ON_ERROR,
    121: NET_RENDER_SOUND_OFF_ERROR,
    122: NET_RENDER_SET_VOLUME_ERROR,
    123: NET_RENDER_ADJUST_ERROR,
    124: NET_RENDER_PAUSE_ERROR,
    125: NET_RENDER_SNAP_ERROR,
    126: NET_RENDER_STEP_ERROR,
    127: NET_RENDER_FRAMERATE_ERROR,
    128: NET_RENDER_DISPLAYREGION_ERROR,
    129: NET_RENDER_GETOSDTIME_ERROR,
    140: NET_GROUP_EXIST,
    141: NET_GROUP_NOEXIST,
    142: NET_GROUP_RIGHTOVER,
    143: NET_GROUP_HAVEUSER,
    144: NET_GROUP_RIGHTUSE,
    145: NET_GROUP_SAMENAME,
    146: NET_USER_EXIST,
    147: NET_USER_NOEXIST,
    148: NET_USER_RIGHTOVER,
    149: NET_USER_PWD,
    150: NET_USER_FLASEPWD,
    151: NET_USER_NOMATCHING,
    152: NET_USER_INUSE,
    300: NET_ERROR_GETCFG_ETHERNET,
    301: NET_ERROR_GETCFG_WLAN,
    302: NET_ERROR_GETCFG_WLANDEV,
    303: NET_ERROR_GETCFG_REGISTER,
    304: NET_ERROR_GETCFG_CAMERA,
    305: NET_ERROR_GETCFG_INFRARED,
    306: NET_ERROR_GETCFG_SOUNDALARM,
    307: NET_ERROR_GETCFG_STORAGE,
    308: NET_ERROR_GETCFG_MAIL,
    309: NET_CONFIG_DEVBUSY,
    310: NET_CONFIG_DATAILLEGAL,
    311: NET_ERROR_GETCFG_DST,
    312: NET_ERROR_SETCFG_DST,
    313: NET_ERROR_GETCFG_VIDEO_OSD,
    314: NET_ERROR_SETCFG_VIDEO_OSD,
    315: NET_ERROR_GETCFG_GPRSCDMA,
    316: NET_ERROR_SETCFG_GPRSCDMA,
    317: NET_ERROR_GETCFG_IPFILTER,
    318: NET_ERROR_SETCFG_IPFILTER,
    319: NET_ERROR_GETCFG_TALKENCODE,
    320: NET_ERROR_SETCFG_TALKENCODE,
    321: NET_ERROR_GETCFG_RECORDLEN,
    322: NET_ERROR_SETCFG_RECORDLEN,
    323: NET_DONT_SUPPORT_SUBAREA,
    324: NET_ERROR_GET_AUTOREGSERVER,
    325: NET_ERROR_CONTROL_AUTOREGISTER,
    326: NET_ERROR_DISCONNECT_AUTOREGISTER,
    327: NET_ERROR_GETCFG_MMS,
    328: NET_ERROR_SETCFG_MMS,
    329: NET_ERROR_GETCFG_SMSACTIVATION,
    330: NET_ERROR_SETCFG_SMSACTIVATION,
    331: NET_ERROR_GETCFG_DIALINACTIVATION,
    332: NET_ERROR_SETCFG_DIALINACTIVATION,
    333: NET_ERROR_GETCFG_VIDEOOUT,
    334: NET_ERROR_SETCFG_VIDEOOUT,
    335: NET_ERROR_GETCFG_OSDENABLE,
    336: NET_ERROR_SETCFG_OSDENABLE,
    337: NET_ERROR_SETCFG_ENCODERINFO,
    338: NET_ERROR_GETCFG_TVADJUST,
    339: NET_ERROR_SETCFG_TVADJUST,
    340: NET_ERROR_CONNECT_FAILED,
    341: NET_ERROR_SETCFG_BURNFILE,
    342: NET_ERROR_SNIFFER_GETCFG,
    343: NET_ERROR_SNIFFER_SETCFG,
    344: NET_ERROR_DOWNLOADRATE_GETCFG,
    345: NET_ERROR_DOWNLOADRATE_SETCFG,
    346: NET_ERROR_SEARCH_TRANSCOM,
    347: NET_ERROR_GETCFG_POINT,
    348: NET_ERROR_SETCFG_POINT,
    349: NET_SDK_LOGOUT_ERROR,
    350: NET_ERROR_GET_VEHICLE_CFG,
    351: NET_ERROR_SET_VEHICLE_CFG,
    352: NET_ERROR_GET_ATM_OVERLAY_CFG,
    353: NET_ERROR_SET_ATM_OVERLAY_CFG,
    354: NET_ERROR_GET_ATM_OVERLAY_ABILITY,
    355: NET_ERROR_GET_DECODER_TOUR_CFG,
    356: NET_ERROR_SET_DECODER_TOUR_CFG,
    357: NET_ERROR_CTRL_DECODER_TOUR,
    358: NET_GROUP_OVERSUPPORTNUM,
    359: NET_USER_OVERSUPPORTNUM,
    368: NET_ERROR_GET_SIP_CFG,
    369: NET_ERROR_SET_SIP_CFG,
    370: NET_ERROR_GET_SIP_ABILITY,
    371: NET_ERROR_GET_WIFI_AP_CFG,
    372: NET_ERROR_SET_WIFI_AP_CFG,
    373: NET_ERROR_GET_DECODE_POLICY,
    374: NET_ERROR_SET_DECODE_POLICY,
    375: NET_ERROR_TALK_REJECT,
    376: NET_ERROR_TALK_OPENED,
    377: NET_ERROR_TALK_RESOURCE_CONFLICIT,
    378: NET_ERROR_TALK_UNSUPPORTED_ENCODE,
    379: NET_ERROR_TALK_RIGHTLESS,
    380: NET_ERROR_TALK_FAILED,
    381: NET_ERROR_GET_MACHINE_CFG,
    382: NET_ERROR_SET_MACHINE_CFG,
    383: NET_ERROR_GET_DATA_FAILED,
    384: NET_ERROR_MAC_VALIDATE_FAILED,
    385: NET_ERROR_GET_INSTANCE,
    386: NET_ERROR_JSON_REQUEST,
    387: NET_ERROR_JSON_RESPONSE,
    388: NET_ERROR_VERSION_HIGHER,
    389: NET_SPARE_NO_CAPACITY,
    390: NET_ERROR_SOURCE_IN_USE,
    391: NET_ERROR_REAVE,
    392: NET_ERROR_NETFORBID,
    393: NET_ERROR_GETCFG_MACFILTER,
    394: NET_ERROR_SETCFG_MACFILTER,
    395: NET_ERROR_GETCFG_IPMACFILTER,
    396: NET_ERROR_SETCFG_IPMACFILTER,
    397: NET_ERROR_OPERATION_OVERTIME,
    398: NET_ERROR_SENIOR_VALIDATE_FAILED,
    399: NET_ERROR_DEVICE_ID_NOT_EXIST,
    400: NET_ERROR_UNSUPPORTED,
    401: NET_ERROR_PROXY_DLLLOAD,
    402: NET_ERROR_PROXY_ILLEGAL_PARAM,
    403: NET_ERROR_PROXY_INVALID_HANDLE,
    404: NET_ERROR_PROXY_LOGIN_DEVICE_ERROR,
    405: NET_ERROR_PROXY_START_SERVER_ERROR,
    406: NET_ERROR_SPEAK_FAILED,
    407: NET_ERROR_NOT_SUPPORT_F6,
    408: NET_ERROR_CD_UNREADY,
    409: NET_ERROR_DIR_NOT_EXIST,
    410: NET_ERROR_UNSUPPORTED_SPLIT_MODE,
    411: NET_ERROR_OPEN_WND_PARAM,
    412: NET_ERROR_LIMITED_WND_COUNT,
    413: NET_ERROR_UNMATCHED_REQUEST,
    414: NET_RENDER_ENABLELARGEPICADJUSTMENT_ERROR,
    415: NET_ERROR_UPGRADE_FAILED,
    416: NET_ERROR_NO_TARGET_DEVICE,
    417: NET_ERROR_NO_VERIFY_DEVICE,
    418: NET_ERROR_CASCADE_RIGHTLESS,
    419: NET_ERROR_LOW_PRIORITY,
    420: NET_ERROR_REMOTE_REQUEST_TIMEOUT,
    421: NET_ERROR_LIMITED_INPUT_SOURCE,
    422: NET_ERROR_SET_LOG_PRINT_INFO,
    423: NET_ERROR_PARAM_DWSIZE_ERROR,
    424: NET_ERROR_LIMITED_MONITORWALL_COUNT,
    425: NET_ERROR_PART_PROCESS_FAILED,
    426: NET_ERROR_TARGET_NOT_SUPPORT,
    510: NET_ERROR_VISITE_FILE,
    511: NET_ERROR_DEVICE_STATUS_BUSY,
    512: NET_USER_PWD_NOT_AUTHORIZED,
    513: NET_USER_PWD_NOT_STRONG,
    514: NET_ERROR_NO_SUCH_CONFIG,
    515: NET_ERROR_AUDIO_RECORD_FAILED,
    516: NET_ERROR_SEND_DATA_FAILED,
    517: NET_ERROR_OBSOLESCENT_INTERFACE,
    518: NET_ERROR_INSUFFICIENT_INTERAL_BUF,
    519: NET_ERROR_NEED_ENCRYPTION_PASSWORD,
    520: NET_ERROR_NOSUPPORT_RECORD,
    521: NET_ERROR_DEVICE_IN_UPGRADING,
    522: NET_ERROR_ANALYSE_TASK_NOT_EXIST,
    523: NET_ERROR_ANALYSE_TASK_FULL,
    524: NET_ERROR_DEVICE_RESTART,
    525: NET_ERROR_DEVICE_SHUTDOWN,
    526: NET_ERROR_FILE_SYSTEM_ERROR,
    527: NET_ERROR_HARDDISK_WRITE_ERROR,
    528: NET_ERROR_HARDDISK_READ_ERROR,
    529: NET_ERROR_NO_HARDDISK_RECORD_LOG,
    530: NET_ERROR_NO_HARDDISK,
    531: NET_ERROR_HARDDISK_OTHER_ERRORS,
    532: NET_ERROR_HARDDISK_BADSECTORS_MINOR_ERRORS,
    533: NET_ERROR_HARDDISK_BADSECTORS_CRITICAL_ERRORS,
    534: NET_ERROR_HARDDISK_PHYSICAL_BADSECTORS_SLIGHT,
    535: NET_ERROR_HARDDISK_PHYSICAL_BADSECTORS_SERIOUS,
    536: NET_ERROR_NETWORK_DISCONNECTION_ALARM,
    537: NET_ERROR_NETWORK_DISCONNECTION,
    538: NET_ERROR_SET_SOURCE_EXCEED,
    539: NET_ERROR_SIZE_EXCEED,
    540: NET_ERROR_LOGOPEN_DISABLE,
    541: NET_ERROR_STREAM_PACKAGE_ERROR,
    1010: NET_ERROR_SERIALIZE_ERROR,
    1011: NET_ERROR_DESERIALIZE_ERROR,
    1012: NET_ERROR_LOWRATEWPAN_ID_EXISTED,
    1013: NET_ERROR_LOWRATEWPAN_ID_LIMIT,
    1014: NET_ERROR_LOWRATEWPAN_ID_ABNORMAL,
    1015: NET_ERROR_ENCRYPT,
    1016: NET_ERROR_PWD_ILLEGAL,
    1017: NET_ERROR_DEVICE_ALREADY_INIT,
    1018: NET_ERROR_SECURITY_CODE,
    1019: NET_ERROR_SECURITY_CODE_TIMEOUT,
    1020: NET_ERROR_GET_PWD_SPECI,
    1021: NET_ERROR_NO_AUTHORITY_OF_OPERATION,
    1022: NET_ERROR_DECRYPT,
    1023: NET_ERROR_2D_CODE,
    1024: NET_ERROR_INVALID_REQUEST,
    1025: NET_ERROR_PWD_RESET_DISABLE,
    1026: NET_ERROR_PLAY_PRIVATE_DATA,
    1027: NET_ERROR_ROBOT_OPERATE_FAILED,
    1028: NET_ERROR_PHOTOSIZE_EXCEEDSLIMIT,
    1029: NET_ERROR_USERID_INVALID,
    1030: NET_ERROR_EXTRACTFEATURE_FAILED,
    1031: NET_ERROR_PHOTO_EXIST,
    1032: NET_ERROR_PHOTO_OVERFLOW,
    1033: NET_ERROR_CHANNEL_ALREADY_OPENED,
    1034: NET_ERROR_CREATE_SOCKET,
    1035: NET_ERROR_CHANNEL_NUM,
    1036: NET_ERROR_PHOTO_FORMAT,
    1037: NET_ERROR_DIGITAL_CERTIFICATE_INTERNAL_ERROR,
    1038: NET_ERROR_DIGITAL_CERTIFICATE_GET_ID_FAILED,
    1039: NET_ERROR_DIGITAL_CERTIFICATE_IMPORT_ILLEGAL,
    1040: NET_ERROR_DIGITAL_CERTIFICATE_SN_ERROR,
    1041: NET_ERROR_DIGITAL_CERTIFICATE_COMMON_NAME_ILLEGAL,
    1042: NET_ERROR_DIGITAL_CERTIFICATE_NO_ROOT_CERT,
    1043: NET_ERROR_DIGITAL_CERTIFICATE_CERT_REVOKED,
    1044: NET_ERROR_DIGITAL_CERTIFICATE_CERT_INVALID,
    1045: NET_ERROR_DIGITAL_CERTIFICATE_CERT_ERROR_SIGN,
    1046: NET_ERROR_DIGITAL_CERTIFICATE_COUNTS_UPPER_LIMIT,
    1047: NET_ERROR_DIGITAL_CERTIFICATE_CERT_NO_EXIST,
    1048: NET_ERROR_DEFULAT_SEARCH_PORT,
    1049: NET_ERROR_FACE_RECOGNITION_SERVER_MULTI_APPEND_STOUP,
    1050: NET_ERROR_FACE_RECOGNITION_SERVER_MULTI_APPEND_ERROR,
    1051: NET_ERROR_FACE_RECOGNITION_SERVER_GROUP_ID_EXCEED,
    1052: NET_ERROR_FACE_RECOGNITION_SERVER_GROUP_ID_NOT_IN_REGISTER_GROUP,
    1053: NET_ERROR_FACE_RECOGNITION_SERVER_PICTURE_NOT_FOUND,
    1054: NET_ERROR_FACE_RECOGNITION_SERVER_GENERATE_GROUP_ID_FAILED,
    1055: NET_ERROR_FACE_RECOGNITION_SERVER_SET_CONFIG_FAILED,
    1056: NET_ERROR_FACE_RECOGNITION_SERVER_FILE_OPEN_FAILED,
    1057: NET_ERROR_FACE_RECOGNITION_SERVER_FILE_READ_FAILED,
    1058: NET_ERROR_FACE_RECOGNITION_SERVER_FILE_WRITE_FAILED,
    1059: NET_ERROR_FACE_RECOGNITION_SERVER_PICTURE_DPI_ERROR,
    1060: NET_ERROR_FACE_RECOGNITION_SERVER_PICTURE_PX_ERROR,
    1061: NET_ERROR_FACE_RECOGNITION_SERVER_PICTURE_SIZE_ERROR,
    1062: NET_ERROR_FACE_RECOGNITION_SERVER_DATA_BASE_ERROR,
    1063: NET_ERROR_FACE_RECOGNITION_SERVER_FACE_MAX_NUM,
    1064: NET_ERROR_FACE_RECOGNITION_SERVER_BIRTH_DAY_FORMAT_ERROR,
    1065: NET_ERROR_FACE_RECOGNITION_SERVER_UID_ERROR,
    1066: NET_ERROR_FACE_RECOGNITION_SERVER_TOKEN_ERROR,
    1067: NET_ERROR_FACE_RECOGNITION_SERVER_BEGIN_NUM_OVER_RUN,
    1068: NET_ERROR_FACE_RECOGNITION_SERVER_ABSTRACT_NUM_ZERO,
    1069: NET_ERROR_FACE_RECOGNITION_SERVER_ABSTRACT_INIT_ERROR,
    1070: NET_ERROR_FACE_RECOGNITION_SERVER_AUTO_ABSTRACT_STATE,
    1071: NET_ERROR_FACE_RECOGNITION_SERVER_ABSTRACT_STATE,
    1072: NET_ERROR_FACE_RECOGNITION_SERVER_IM_EX_STATE,
    1073: NET_ERROR_FACE_RECOGNITION_SERVER_PIC_WRITE_FAILED,
    1074: NET_ERROR_FACE_RECOGNITION_SERVER_GROUP_SPACE_EXCEED,
    1075: NET_ERROR_FACE_RECOGNITION_SERVER_GROUP_PIC_COUNT_EXCEED,
    1076: NET_ERROR_FACE_RECOGNITION_SERVER_GROUP_NOT_FOUND,
    1077: NET_ERROR_FACE_RECOGNITION_SERVER_FIND_RECORDS_ERROR,
    1078: NET_ERROR_FACE_RECOGNITION_SERVER_DELETE_PERSON_ERROR,
    1079: NET_ERROR_DEVICE_PARSE_PROTOCOL,
    1080: NET_ERROR_DEVICE_INVALID_REQUEST,
    1081: NET_ERROR_DEVICE_INTERNAL_ERROR,
    1082: NET_ERROR_DEVICE_REQUEST_TIMEOUT,
    1083: NET_ERROR_DEVICE_KEEPALIVE_FAIL,
    1084: NET_ERROR_DEVICE_NETWORK_ERROR,
    1085: NET_ERROR_DEVICE_UNKNOWN_ERROR,
    1086: NET_ERROR_DEVICE_COM_INTERFACE_NOTFOUND,
    1087: NET_ERROR_DEVICE_COM_IMPLEMENT_NOTFOUND,
    1088: NET_ERROR_DEVICE_COM_NOTFOUND,
    1089: NET_ERROR_DEVICE_COM_INSTANCE_NOTEXIST,
    1090: NET_ERROR_DEVICE_CREATE_COM_FAIL,
    1091: NET_ERROR_DEVICE_GET_COM_FAIL,
    1092: NET_ERROR_DEVICE_BAD_REQUEST,
    1093: NET_ERROR_DEVICE_REQUEST_IN_PROGRESS,
    1094: NET_ERROR_DEVICE_LIMITED_RESOURCE,
    1095: NET_ERROR_DEVICE_BUSINESS_TIMEOUT,
    1096: NET_ERROR_DEVICE_TOO_MANY_REQUESTS,
    1097: NET_ERROR_DEVICE_NOT_ALREADY,
    1098: NET_ERROR_DEVICE_SEARCHRECORD_TIMEOUT,
    1099: NET_ERROR_DEVICE_SEARCHTIME_INVALID,
    1100: NET_ERROR_DEVICE_SSID_INVALID,
    1101: NET_ERROR_DEVICE_CHANNEL_STREAMTYPE_ERROR,
    1102: NET_ERROR_DEVICE_STREAM_PACKINGFORMAT_UNSUPPORT,
    1103: NET_ERROR_DEVICE_AUDIO_ENCODINGFORMAT_UNSUPPORT,
    1104: NET_ERROR_SECURITY_ERROR_SUPPORT_GUI,
    1105: NET_ERROR_SECURITY_ERROR_SUPPORT_MULT,
    1106: NET_ERROR_SECURITY_ERROR_SUPPORT_UNIQUE,
    1107: NET_ERROR_STREAMCONVERTOR_DEFECT,
    1108: NET_ERROR_SECURITY_GENERATE_SAFE_CODE,
    1109: NET_ERROR_SECURITY_GET_CONTACT,
    1110: NET_ERROR_SECURITY_GET_QRCODE,
    1111: NET_ERROR_SECURITY_CANNOT_RESET,
    1112: NET_ERROR_SECURITY_NOT_SUPPORT_CONTACT_MODE,
    1113: NET_ERROR_SECURITY_RESPONSE_TIMEOUT,
    1114: NET_ERROR_SECURITY_AUTHCODE_FORBIDDEN,
    1115: NET_ERROR_TRANCODE_LOGIN_REMOTE_DEV,
    1116: NET_ERROR_TRANCODE_NOFREE_CHANNEL,
    1117: NET_ERROR_VK_INFO_DECRYPT_FAILED,
    1118: NET_ERROR_VK_INFO_DESERIALIZE_FAILED,
    1119: NET_ERROR_GDPR_ABILITY_NOT_ENABLE,
    1120: NET_ERROR_FAST_CHECK_NO_AUTH,
    1121: NET_ERROR_FAST_CHECK_NO_FILE,
    1122: NET_ERROR_FAST_CHECK_FILE_FAIL,
    1123: NET_ERROR_FAST_CHECK_BUSY,
    1124: NET_ERROR_FAST_CHECK_NO_PASSWORD,
    1125: NET_ERROR_IMPORT_ACCESS_SEND_FAILD,
    1126: NET_ERROR_IMPORT_ACCESS_BUSY,
    1127: NET_ERROR_IMPORT_ACCESS_DATAERROR,
    1128: NET_ERROR_IMPORT_ACCESS_DATAINVALID,
    1129: NET_ERROR_IMPORT_ACCESS_SYNC_FALID,
    1130: NET_ERROR_IMPORT_ACCESS_DBFULL,
    1131: NET_ERROR_IMPORT_ACCESS_SDFULL,
    1132: NET_ERROR_IMPORT_ACCESS_CIPHER_ERROR,
    1133: NET_ERROR_INVALID_PARAM,
    1134: NET_ERROR_INVALID_PASSWORD,
    1135: NET_ERROR_INVALID_FINGERPRINT,
    1136: NET_ERROR_INVALID_FACE,
    1137: NET_ERROR_INVALID_CARD,
    1138: NET_ERROR_INVALID_USER,
    1139: NET_ERROR_GET_SUBSERVICE,
    1140: NET_ERROR_GET_METHOD,
    1141: NET_ERROR_GET_SUBCAPS,
    1142: NET_ERROR_UPTO_INSERT_LIMIT,
    1143: NET_ERROR_UPTO_MAX_INSERT_RATE,
    1144: NET_ERROR_ERASE_FINGERPRINT,
    1145: NET_ERROR_ERASE_FACE,
    1146: NET_ERROR_ERASE_CARD,
    1147: NET_ERROR_NO_RECORD,
    1148: NET_ERROR_NOMORE_RECORDS,
    1149: NET_ERROR_RECORD_ALREADY_EXISTS,
    1150: NET_ERROR_EXCEED_MAX_FINGERPRINT_PERUSER,
    1151: NET_ERROR_EXCEED_MAX_CARD_PERUSER,
    1152: NET_ERROR_EXCEED_ADMINISTRATOR_LIMIT,
    1153: NET_LOGIN_ERROR_DEVICE_NOT_SUPPORT_HIGHLEVEL_SECURITY_LOGIN,
    1154: NET_LOGIN_ERROR_DEVICE_ONLY_SUPPORT_HIGHLEVEL_SECURITY_LOGIN,
    1155: NET_ERROR_VIDEO_CHANNEL_OFFLINE,
    1156: NET_ERROR_USERID_FORMAT_INCORRECT,
    1157: NET_ERROR_CANNOT_FIND_CHANNEL_RELATE_TO_SN,
    1158: NET_ERROR_TASK_QUEUE_OF_CHANNEL_IS_FULL,
    1159: NET_ERROR_APPLY_USER_INFO_BLOCK_FAIL,
    1160: NET_ERROR_EXCEED_MAX_PASSWD_PERUSER,
    1161: NET_ERROR_PARSE_PROTOCOL,
    1162: NET_ERROR_CARD_NUM_EXIST,
    1163: NET_ERROR_FINGERPRINT_EXIST,
    1164: NET_ERROR_OPEN_PLAYGROUP_FAIL,
    1165: NET_ERROR_ALREADY_IN_PLAYGROUP,
    1166: NET_ERROR_QUERY_PLAYGROUP_TIME_FAIL,
    1167: NET_ERROR_SET_PLAYGROUP_BASECHANNEL_FAIL,
    1168: NET_ERROR_SET_PLAYGROUP_DIRECTION_FAIL,
    1169: NET_ERROR_SET_PLAYGROUP_SPEED_FAIL,
    1170: NET_ERROR_ADD_PLAYGROUP_FAIL,
    1171: NET_ERROR_EXPORT_AOL_LOGFILE_NO_AUTH,
    1172: NET_ERROR_EXPORT_AOL_LOGFILE_NO_FILE,
    1173: NET_ERROR_EXPORT_AOL_LOGFILE_FILE_FAIL,
    1174: NET_ERROR_EXPORT_AOL_LOGFILE_BUSY,
    1175: NET_ERROR_EMPTY_LICENSE,
    1176: NET_ERROR_UNSUPPORTED_MODE,
    1177: NET_ERROR_URL_APP_NOT_MATCH,
    1178: NET_ERROR_READ_INFO_FAILED,
    1179: NET_ERROR_WRITE_FAILED,
    1180: NET_ERROR_NO_SUCH_APP,
    1181: NET_ERROR_VERIFIF_FAILED,
    1182: NET_ERROR_LICENSE_OUT_DATE,
    1183: NET_ERROR_UPGRADE_PROGRAM_TOO_OLD,
    1184: NET_ERROR_SECURE_TRANSMIT_BEEN_CUT,
    1185: NET_ERROR_DEVICE_NOT_SUPPORT_SECURE_TRANSMIT,
    1186: NET_ERROR_EXTRA_STREAM_LOGIN_FAIL_CAUSE_BY_MAIN_STREAM,
    1187: NET_ERROR_EXTRA_STREAM_CLOSED_BY_REMOTE_DEVICE,
    1188: NET_ERROR_IMPORT_FACEDB_SEND_FAILD,
    1189: NET_ERROR_IMPORT_FACEDB_BUSY,
    1190: NET_ERROR_IMPORT_FACEDB_DATAERROR,
    1191: NET_ERROR_IMPORT_FACEDB_DATAINVALID,
    1192: NET_ERROR_IMPORT_FACEDB_UPGRADE_FAILD,
    1193: NET_ERROR_IMPORT_FACEDB_NO_AUTHORITY,
    1194: NET_ERROR_IMPORT_FACEDB_ABNORMAL_FILE,
    1195: NET_ERROR_IMPORT_FACEDB_SYNC_FALID,
    1196: NET_ERROR_IMPORT_FACEDB_DBFULL,
    1197: NET_ERROR_IMPORT_FACEDB_SDFULL,
    1198: NET_ERROR_IMPORT_FACEDB_CIPHER_ERROR,
    1199: NET_ERROR_EXPORT_FACEDB_NO_AUTH,
    1200: NET_ERROR_EXPORT_FACEDB_NO_FILE,
    1201: NET_ERROR_EXPORT_FACEDB_FILE_FAIL,
    1202: NET_ERROR_EXPORT_FACEDB_BUSY,
    1203: NET_ERROR_EXPORT_FACEDB_NO_PASSWORD,
    1204: NET_ERROR_REQUESTED_TOO_MUCH_DATA,
    1205: NET_ERROR_BATCH_PROCESS_ERROR,
    1206: NET_ERROR_OPERATION_CANCELLED,
    1207: NET_ERROR_DEVICE_INVALID,
    1208: NET_ERROR_DEVICE_UNAVAILABLE,
    1209: NET_ERROR_FINGERPRINT_DOWNLOAD_FAIL,
    1210: NET_ERROR_ACCOUNT_IN_USE,
    1211: NET_ERROR_IRIS_INFO_NOT_EXISTED,
    1212: NET_ERROR_INVALID_IRIS_DATA,
    1213: NET_ERROR_IRIS_ALREADY_EXIST,
    1214: NET_ERROR_ERASE_IRIS_FAILED,
    1215: NET_ERROR_EXCEED_MAX_IRIS_GROUP_COUNT_PER_USER,
    1216: NET_ERROR_EXCEED_MAX_IRIS_COUNT_PER_GROUP,
    1300: NET_ERROR_FACEMANAGER_NO_FACE_DETECTED,
    1301: NET_ERROR_FACEMANAGER_MULTI_FACE_DETECTED,
    1302: NET_ERROR_FACEMANAGER_PICTURE_DECODING_ERROR,
    1303: NET_ERROR_FACEMANAGER_LOW_PICTURE_QUALITY,
    1304: NET_ERROR_FACEMANAGER_NOT_RECOMMENDED,
    1305: NET_ERROR_FACEMANAGER_FACE_FEATURE_ALREADY_EXIST,
    1307: NET_ERROR_FACEMANAGER_FACE_ANGLE_OVER_THRESHOLDS,
    1308: NET_ERROR_FACEMANAGER_FACE_RADIO_EXCEEDS_RANGE,
    1309: NET_ERROR_FACEMANAGER_FACE_OVER_EXPOSED,
    1310: NET_ERROR_FACEMANAGER_FACE_UNDER_EXPOSED,
    1311: NET_ERROR_FACEMANAGER_BRIGHTNESS_IMBALANCE,
    1312: NET_ERROR_FACEMANAGER_FACE_LOWER_CONFIDENCE,
    1313: NET_ERROR_FACEMANAGER_FACE_LOW_ALIGN,
    1314: NET_ERROR_FACEMANAGER_FRAGMENTARY_FACE_DETECTED,
    1315: NET_ERROR_FACEMANAGER_PUPIL_DISTANCE_NOT_ENOUGH,
    1316: NET_ERROR_FACEMANAGER_FACE_DATA_DOWNLOAD_FAILED,
    1317: NET_ERROR_CITIZENMANAGER_ERROR_WORKINGMODE_ERROR,
    1318: NET_ERROR_CITIZENMANAGER_ERROR_CAPTURE_BUSY,
    1319: NET_ERROR_CITIZENMANAGER_ERROR_CAPTURE_TYPE_ERROR,
    1320: NET_ERROR_NORMAL_USER_NOTSUPPORT,
    1321: NET_ERROR_THERMOGRAPHY_REF_SENSOR_OPEN_INVALID,
    1322: NET_ERROR_THERMOGRAPHY_REF_DELAY_SHUT_DOWN_INVALID,
    1323: NET_ERROR_CITIZENID_EXIST,
    1324: NET_ERROR_FACEMANAGER_FACE_FFE_FAILED,
    1325: NET_ERROR_FACEMANAGER_PHOTO_FEATURE_FAILED_FOR_FA,
    1326: NET_ERROR_FACEMANAGER_FACE_DATA_PHOTO_INCOMPLETE,
    1327: NET_ERROR_DATABASE_ERROR_INSERT_OVERFLOW,
    1328: NET_ERROR_WORKSUIT_COMPARE_SERVER_GROUPID_EXCEED,
    1329: NET_ERROR_WORKSUIT_COMPARE_SERVER_ABSTRACT_INIT_ERROR,
    1330: NET_ERROR_WORKSUIT_COMPARE_SERVER_GROUPID_NOT_FOUND,
    1331: NET_ERROR_WORKSUIT_COMPARE_SERVER_DATABASE_ERROR,
    1332: NET_ERROR_WORKSUIT_COMPARE_SERVER_TOKEN_ERROR,
    1333: NET_ERROR_WORKSUIT_COMPARE_SERVER_BEGINNUM_OVERRUN,
    1334: NET_ERROR_WORKSUIT_COMPARE_SERVER_ABSTRACT_STATE,
    1335: NET_ERROR_WORKSUIT_COMPARE_SERVER_BIGPIC_MAXNUM,
    1336: NET_ERROR_WORKSUIT_COMPARE_SERVER_OBJECT_MAXNUM,
    1337: NET_ERROR_WORKSUIT_COMPARE_SERVER_GROUP_SPACE_EXCEED,
    1338: NET_ERROR_WORKSUIT_COMPARE_SERVER_ABSTRACTNUM_ZERO,
    1339: NET_ERROR_WORKSUIT_COMPARE_SERVER_INVALID_PARAM,
    1340: NET_ERROR_CARD_NOT_EXIST,
    1341: NET_ERROR_TEMPORARY_OUTDATED,
    1401: NET_SUBBIZ_INVALID_SOCKET,
    1402: NET_SUBBIZ_PAUSE_ERROR,
    1403: NET_SUBBIZ_GET_PORT_ERROR,
}
