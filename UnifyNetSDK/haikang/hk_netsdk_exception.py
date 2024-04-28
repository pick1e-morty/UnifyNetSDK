class HKNetSDKException(Exception):

    def __init__(self):
        self.errorIndex = 0
        self.errorInfo = ""
        super().__init__(self.errorIndex, self.errorInfo)

    def __str__(self):
        if self.errorInfo:
            return str(self.errorIndex) + " " + self.errorInfo
        else:
            return str(self.errorIndex)


class NET_DVR_NOERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 0
        self.errorInfo = errorText


class NET_DVR_PASSWORD_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1
        self.errorInfo = errorText


class NET_DVR_NOENOUGHPRI(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2
        self.errorInfo = errorText


class NET_DVR_NOINIT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 3
        self.errorInfo = errorText


class NET_DVR_CHANNEL_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 4
        self.errorInfo = errorText


class NET_DVR_OVER_MAXLINK(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 5
        self.errorInfo = errorText


class NET_DVR_VERSIONNOMATCH(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 6
        self.errorInfo = errorText


class NET_DVR_NETWORK_FAIL_CONNECT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 7
        self.errorInfo = errorText


class NET_DVR_NETWORK_SEND_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8
        self.errorInfo = errorText


class NET_DVR_NETWORK_RECV_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 9
        self.errorInfo = errorText


class NET_DVR_NETWORK_RECV_TIMEOUT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 10
        self.errorInfo = errorText


class NET_DVR_NETWORK_ERRORDATA(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 11
        tempErrorInfo = "如果你NET_DVR_SetSDKInitCfg传入错误的路径的话，SetSDKInitCfg也不会返回false的，这可能是当前错误的原因之一"
        self.errorInfo = tempErrorInfo + "\n" + str(errorText) if errorText else tempErrorInfo


class NET_DVR_ORDER_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 12
        self.errorInfo = errorText


class NET_DVR_OPERNOPERMIT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 13
        self.errorInfo = errorText


class NET_DVR_COMMANDTIMEOUT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 14
        self.errorInfo = errorText


class NET_DVR_ERRORSERIALPORT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 15
        self.errorInfo = errorText


class NET_DVR_ERRORALARMPORT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 16
        self.errorInfo = errorText


class NET_DVR_PARAMETER_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 17
        self.errorInfo = errorText


class NET_DVR_CHAN_EXCEPTION(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 18
        self.errorInfo = errorText


class NET_DVR_NODISK(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 19
        self.errorInfo = errorText


class NET_DVR_ERRORDISKNUM(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 20
        self.errorInfo = errorText


class NET_DVR_DISK_FULL(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 21
        self.errorInfo = errorText


class NET_DVR_DISK_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 22
        self.errorInfo = errorText


class NET_DVR_NOSUPPORT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 23
        self.errorInfo = errorText


class NET_DVR_BUSY(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 24
        self.errorInfo = errorText


class NET_DVR_MODIFY_FAIL(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 25
        self.errorInfo = errorText


class NET_DVR_PASSWORD_FORMAT_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 26
        self.errorInfo = errorText


class NET_DVR_DISK_FORMATING(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 27
        self.errorInfo = errorText


class NET_DVR_DVRNORESOURCE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 28
        self.errorInfo = errorText


class NET_DVR_DVROPRATEFAILED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 29
        self.errorInfo = errorText


class NET_DVR_OPENHOSTSOUND_FAIL(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 30
        self.errorInfo = errorText


class NET_DVR_DVRVOICEOPENED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 31
        self.errorInfo = errorText


class NET_DVR_TIMEINPUTERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 32
        self.errorInfo = errorText


class NET_DVR_NOSPECFILE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 33
        self.errorInfo = errorText


class NET_DVR_CREATEFILE_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 34
        self.errorInfo = errorText


class NET_DVR_FILEOPENFAIL(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 35
        self.errorInfo = errorText


class NET_DVR_OPERNOTFINISH(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 36
        self.errorInfo = errorText


class NET_DVR_GETPLAYTIMEFAIL(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 37
        self.errorInfo = errorText


class NET_DVR_PLAYFAIL(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 38
        self.errorInfo = errorText


class NET_DVR_FILEFORMAT_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 39
        self.errorInfo = errorText


class NET_DVR_DIR_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 40
        self.errorInfo = errorText


class NET_DVR_ALLOC_RESOURCE_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 41
        self.errorInfo = errorText


class NET_DVR_AUDIO_MODE_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 42
        self.errorInfo = errorText


class NET_DVR_NOENOUGH_BUF(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 43
        self.errorInfo = errorText


class NET_DVR_CREATESOCKET_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 44
        self.errorInfo = errorText


class NET_DVR_SETSOCKET_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 45
        self.errorInfo = errorText


class NET_DVR_MAX_NUM(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 46
        self.errorInfo = errorText


class NET_DVR_USERNOTEXIST(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 47
        self.errorInfo = errorText


class NET_DVR_WRITEFLASHERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 48
        self.errorInfo = errorText


class NET_DVR_UPGRADEFAIL(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 49
        self.errorInfo = errorText


class NET_DVR_CARDHAVEINIT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 50
        self.errorInfo = errorText


class NET_DVR_PLAYERFAILED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 51
        self.errorInfo = errorText


class NET_DVR_MAX_USERNUM(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 52
        self.errorInfo = errorText


class NET_DVR_GETLOCALIPANDMACFAIL(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 53
        self.errorInfo = errorText


class NET_DVR_NOENCODEING(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 54
        self.errorInfo = errorText


class NET_DVR_IPMISMATCH(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 55
        self.errorInfo = errorText


class NET_DVR_MACMISMATCH(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 56
        self.errorInfo = errorText


class NET_DVR_UPGRADELANGMISMATCH(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 57
        self.errorInfo = errorText


class NET_DVR_MAX_PLAYERPORT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 58
        self.errorInfo = errorText


class NET_DVR_NOSPACEBACKUP(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 59
        self.errorInfo = errorText


class NET_DVR_NODEVICEBACKUP(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 60
        self.errorInfo = errorText


class NET_DVR_PICTURE_BITS_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 61
        self.errorInfo = errorText


class NET_DVR_PICTURE_DIMENSION_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 62
        self.errorInfo = errorText


class NET_DVR_PICTURE_SIZ_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 63
        self.errorInfo = errorText


class NET_DVR_LOADPLAYERSDKFAILED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 64
        self.errorInfo = errorText


class NET_DVR_LOADPLAYERSDKPROC_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 65
        self.errorInfo = errorText


class NET_DVR_LOADDSSDKFAILED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 66
        self.errorInfo = errorText


class NET_DVR_LOADDSSDKPROC_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 67
        self.errorInfo = errorText


class NET_DVR_DSSDK_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 68
        self.errorInfo = errorText


class NET_DVR_VOICEMONOPOLIZE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 69
        self.errorInfo = errorText


class NET_DVR_JOINMULTICASTFAILED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 70
        self.errorInfo = errorText


class NET_DVR_CREATEDIR_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 71
        self.errorInfo = errorText


class NET_DVR_BINDSOCKET_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 72
        self.errorInfo = errorText


class NET_DVR_SOCKETCLOSE_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 73
        self.errorInfo = errorText


class NET_DVR_USERID_ISUSING(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 74
        self.errorInfo = errorText


class NET_DVR_SOCKETLISTEN_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 75
        self.errorInfo = errorText


class NET_DVR_PROGRAM_EXCEPTION(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 76
        self.errorInfo = errorText


class NET_DVR_WRITEFILE_FAILED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 77
        self.errorInfo = errorText


class NET_DVR_FORMAT_READONLY(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 78
        self.errorInfo = errorText


class NET_DVR_WITHSAMEUSERNAME(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 79
        self.errorInfo = errorText


class NET_DVR_DEVICETYPE_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 80
        self.errorInfo = errorText


class NET_DVR_LANGUAGE_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 81
        self.errorInfo = errorText


class NET_DVR_PARAVERSION_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 82
        self.errorInfo = errorText


class NET_DVR_IPCHAN_NOTALIVE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 83
        self.errorInfo = errorText


class NET_DVR_RTSP_SDK_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 84
        self.errorInfo = errorText


class NET_DVR_CONVERT_SDK_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 85
        self.errorInfo = errorText


class NET_DVR_IPC_COUNT_OVERFLOW(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 86
        self.errorInfo = errorText


class NET_DVR_MAX_ADD_NUM(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 87
        self.errorInfo = errorText


class NET_DVR_PARAMMODE_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 88
        self.errorInfo = errorText


class NET_DVR_CODESPITTER_OFFLINE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 89
        self.errorInfo = errorText


class NET_DVR_BACKUP_COPYING(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 90
        self.errorInfo = errorText


class NET_DVR_CHAN_NOTSUPPORT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 91
        self.errorInfo = errorText


class NET_DVR_CALLINEINVALID(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 92
        self.errorInfo = errorText


class NET_DVR_CALCANCELCONFLICT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 93
        self.errorInfo = errorText


class NET_DVR_CALPOINTOUTRANGE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 94
        self.errorInfo = errorText


class NET_DVR_FILTERRECTINVALID(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 95
        self.errorInfo = errorText


class NET_DVR_DDNS_DEVOFFLINE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 96
        self.errorInfo = errorText


class NET_DVR_DDNS_INTER_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 97
        self.errorInfo = errorText


class NET_DVR_FUNCTION_NOT_SUPPORT_OS(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 98
        self.errorInfo = errorText


class NET_DVR_DEC_CHAN_REBIND(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 99
        self.errorInfo = errorText


class NET_DVR_INTERCOM_SDK_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 100
        self.errorInfo = errorText


class NET_DVR_NO_CURRENT_UPDATEFILE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 101
        self.errorInfo = errorText


class NET_DVR_USER_NOT_SUCC_LOGIN(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 102
        self.errorInfo = errorText


class NET_DVR_USE_LOG_SWITCH_FILE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 103
        self.errorInfo = errorText


class NET_DVR_POOL_PORT_EXHAUST(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 104
        self.errorInfo = errorText


class NET_DVR_PACKET_TYPE_NOT_SUPPORT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 105
        self.errorInfo = errorText


class NET_DVR_IPPARA_IPID_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 106
        self.errorInfo = errorText


class NET_DVR_LOAD_HCPREVIEW_SDK_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 107
        self.errorInfo = errorText


class NET_DVR_LOAD_HCVOICETALK_SDK_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 108
        self.errorInfo = errorText


class NET_DVR_LOAD_HCALARM_SDK_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 109
        self.errorInfo = errorText


class NET_DVR_LOAD_HCPLAYBACK_SDK_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 110
        self.errorInfo = errorText


class NET_DVR_LOAD_HCDISPLAY_SDK_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 111
        self.errorInfo = errorText


class NET_DVR_LOAD_HCINDUSTRY_SDK_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 112
        self.errorInfo = errorText


class NET_DVR_LOAD_HCGENERALCFGMGR_SDK_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 113
        self.errorInfo = errorText


class NET_DVR_LOAD_HCCOREDEVCFG_SDK_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 114
        self.errorInfo = errorText


class NET_DVR_LOAD_HCNETUTILS_SDK_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 115
        self.errorInfo = errorText


class NET_DVR_CORE_VER_MISMATCH(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 121
        self.errorInfo = errorText


class NET_DVR_CORE_VER_MISMATCH_HCPREVIEW(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 122
        self.errorInfo = errorText


class NET_DVR_CORE_VER_MISMATCH_HCVOICETALK(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 123
        self.errorInfo = errorText


class NET_DVR_CORE_VER_MISMATCH_HCALARM(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 124
        self.errorInfo = errorText


class NET_DVR_CORE_VER_MISMATCH_HCPLAYBACK(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 125
        self.errorInfo = errorText


class NET_DVR_CORE_VER_MISMATCH_HCDISPLAY(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 126
        self.errorInfo = errorText


class NET_DVR_CORE_VER_MISMATCH_HCINDUSTRY(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 127
        self.errorInfo = errorText


class NET_DVR_CORE_VER_MISMATCH_HCGENERALCFGMGR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 128
        self.errorInfo = errorText


class NET_DVR_COM_VER_MISMATCH_HCPREVIEW(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 136
        self.errorInfo = errorText


class NET_DVR_COM_VER_MISMATCH_HCVOICETALK(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 137
        self.errorInfo = errorText


class NET_DVR_COM_VER_MISMATCH_HCALARM(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 138
        self.errorInfo = errorText


class NET_DVR_COM_VER_MISMATCH_HCPLAYBACK(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 139
        self.errorInfo = errorText


class NET_DVR_COM_VER_MISMATCH_HCDISPLAY(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 140
        self.errorInfo = errorText


class NET_DVR_COM_VER_MISMATCH_HCINDUSTRY(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 141
        self.errorInfo = errorText


class NET_DVR_COM_VER_MISMATCH_HCGENERALCFGMGR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 142
        self.errorInfo = errorText


class NET_ERR_CONFIG_FILE_IMPORT_FAILED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 145
        self.errorInfo = errorText


class NET_ERR_CONFIG_FILE_EXPORT_FAILED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 146
        self.errorInfo = errorText


class NET_DVR_CERTIFICATE_FILE_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 147
        self.errorInfo = errorText


class NET_DVR_LOAD_SSL_LIB_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 148
        self.errorInfo = errorText


class NET_DVR_SSL_VERSION_NOT_MATCH(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 149
        self.errorInfo = errorText


class NET_DVR_ALIAS_DUPLICATE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 150
        self.errorInfo = errorText


class NET_DVR_INVALID_COMMUNICATION(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 151
        self.errorInfo = errorText


class NET_DVR_USERNAME_NOT_EXIST(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 152
        self.errorInfo = errorText


class NET_DVR_USER_LOCKED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 153
        self.errorInfo = errorText


class NET_DVR_INVALID_USERID(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 154
        self.errorInfo = errorText


class NET_DVR_LOW_LOGIN_VERSION(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 155
        self.errorInfo = errorText


class NET_DVR_LOAD_LIBEAY32_DLL_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 156
        self.errorInfo = errorText


class NET_DVR_LOAD_SSLEAY32_DLL_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 157
        self.errorInfo = errorText


class NET_ERR_LOAD_LIBICONV(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 158
        self.errorInfo = errorText


class NET_ERR_SSL_CONNECT_FAILED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 159
        self.errorInfo = errorText


class NET_ERR_MCAST_ADDRESS_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 160
        self.errorInfo = errorText


class NET_ERR_LOAD_ZLIB(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 161
        self.errorInfo = errorText


class NET_ERR_OPENSSL_NO_INIT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 162
        self.errorInfo = errorText


class NET_DVR_SERVER_NOT_EXIST(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 164
        self.errorInfo = errorText


class NET_DVR_TEST_SERVER_FAIL_CONNECT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 165
        self.errorInfo = errorText


class NET_DVR_NAS_SERVER_INVALID_DIR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 166
        self.errorInfo = errorText


class NET_DVR_NAS_SERVER_NOENOUGH_PRI(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 167
        self.errorInfo = errorText


class NET_DVR_EMAIL_SERVER_NOT_CONFIG_DNS(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 168
        self.errorInfo = errorText


class NET_DVR_EMAIL_SERVER_NOT_CONFIG_GATEWAY(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 169
        self.errorInfo = errorText


class NET_DVR_TEST_SERVER_PASSWORD_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 170
        self.errorInfo = errorText


class NET_DVR_EMAIL_SERVER_CONNECT_EXCEPTION_WITH_SMTP(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 171
        self.errorInfo = errorText


class NET_DVR_FTP_SERVER_FAIL_CREATE_DIR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 172
        self.errorInfo = errorText


class NET_DVR_FTP_SERVER_NO_WRITE_PIR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 173
        self.errorInfo = errorText


class NET_DVR_IP_CONFLICT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 174
        self.errorInfo = errorText


class NET_DVR_INSUFFICIENT_STORAGEPOOL_SPACE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 175
        self.errorInfo = errorText


class NET_DVR_STORAGEPOOL_INVALID(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 176
        self.errorInfo = errorText


class NET_DVR_EFFECTIVENESS_REBOOT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 177
        self.errorInfo = errorText


class NET_ERR_ANR_ARMING_EXIST(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 178
        self.errorInfo = errorText


class NET_ERR_UPLOADLINK_EXIST(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 179
        self.errorInfo = errorText


class NET_ERR_INCORRECT_FILE_FORMAT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 180
        self.errorInfo = errorText


class NET_ERR_INCORRECT_FILE_CONTENT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 181
        self.errorInfo = errorText


class NET_ERR_MAX_HRUDP_LINK(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 182
        self.errorInfo = errorText


class NET_SDK_ERR_ACCESSKEY_SECRETKEY(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 183
        self.errorInfo = errorText


class NET_SDK_ERR_CREATE_PORT_MULTIPLEX(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 184
        self.errorInfo = errorText


class NET_DVR_NONBLOCKING_CAPTURE_NOTSUPPORT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 185
        self.errorInfo = errorText


class NET_SDK_ERR_FUNCTION_INVALID(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 186
        self.errorInfo = errorText


class NET_SDK_ERR_MAX_PORT_MULTIPLEX(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 187
        self.errorInfo = errorText


class NET_DVR_INVALID_LINK(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 188
        self.errorInfo = errorText


class NET_DVR_ISAPI_NOT_SUPPORT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 189
        self.errorInfo = errorText


class NET_DVR_NAME_NOT_ONLY(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 200
        self.errorInfo = errorText


class NET_DVR_OVER_MAX_ARRAY(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 201
        self.errorInfo = errorText


class NET_DVR_OVER_MAX_VD(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 202
        self.errorInfo = errorText


class NET_DVR_VD_SLOT_EXCEED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 203
        self.errorInfo = errorText


class NET_DVR_PD_STATUS_INVALID(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 204
        self.errorInfo = errorText


class NET_DVR_PD_BE_DEDICATE_SPARE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 205
        self.errorInfo = errorText


class NET_DVR_PD_NOT_FREE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 206
        self.errorInfo = errorText


class NET_DVR_CANNOT_MIG2NEWMODE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 207
        self.errorInfo = errorText


class NET_DVR_MIG_PAUSE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 208
        self.errorInfo = errorText


class NET_DVR_MIG_CANCEL(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 209
        self.errorInfo = errorText


class NET_DVR_EXIST_VD(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 210
        self.errorInfo = errorText


class NET_DVR_TARGET_IN_LD_FUNCTIONAL(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 211
        self.errorInfo = errorText


class NET_DVR_HD_IS_ASSIGNED_ALREADY(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 212
        self.errorInfo = errorText


class NET_DVR_INVALID_HD_COUNT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 213
        self.errorInfo = errorText


class NET_DVR_LD_IS_FUNCTIONAL(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 214
        self.errorInfo = errorText


class NET_DVR_BGA_RUNNING(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 215
        self.errorInfo = errorText


class NET_DVR_LD_NO_ATAPI(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 216
        self.errorInfo = errorText


class NET_DVR_MIGRATION_NOT_NEED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 217
        self.errorInfo = errorText


class NET_DVR_HD_TYPE_MISMATCH(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 218
        self.errorInfo = errorText


class NET_DVR_NO_LD_IN_DG(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 219
        self.errorInfo = errorText


class NET_DVR_NO_ROOM_FOR_SPARE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 220
        self.errorInfo = errorText


class NET_DVR_SPARE_IS_IN_MULTI_DG(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 221
        self.errorInfo = errorText


class NET_DVR_DG_HAS_MISSING_PD(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 222
        self.errorInfo = errorText


class NET_DVR_NAME_EMPTY(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 223
        self.errorInfo = errorText


class NET_DVR_INPUT_PARAM(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 224
        self.errorInfo = errorText


class NET_DVR_PD_NOT_AVAILABLE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 225
        self.errorInfo = errorText


class NET_DVR_ARRAY_NOT_AVAILABLE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 226
        self.errorInfo = errorText


class NET_DVR_PD_COUNT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 227
        self.errorInfo = errorText


class NET_DVR_VD_SMALL(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 228
        self.errorInfo = errorText


class NET_DVR_NO_EXIST(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 229
        self.errorInfo = errorText


class NET_DVR_NOT_SUPPORT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 230
        self.errorInfo = errorText


class NET_DVR_NOT_FUNCTIONAL(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 231
        self.errorInfo = errorText


class NET_DVR_DEV_NODE_NOT_FOUND(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 232
        self.errorInfo = errorText


class NET_DVR_SLOT_EXCEED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 233
        self.errorInfo = errorText


class NET_DVR_NO_VD_IN_ARRAY(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 234
        self.errorInfo = errorText


class NET_DVR_VD_SLOT_INVALID(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 235
        self.errorInfo = errorText


class NET_DVR_PD_NO_ENOUGH_SPACE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 236
        self.errorInfo = errorText


class NET_DVR_ARRAY_NONFUNCTION(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 237
        self.errorInfo = errorText


class NET_DVR_ARRAY_NO_ENOUGH_SPACE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 238
        self.errorInfo = errorText


class NET_DVR_STOPPING_SCANNING_ARRAY(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 239
        self.errorInfo = errorText


class NET_DVR_NOT_SUPPORT_16T(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 240
        self.errorInfo = errorText


class NET_DVR_ARRAY_FORMATING(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 241
        self.errorInfo = errorText


class NET_DVR_QUICK_SETUP_PD_COUNT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 242
        self.errorInfo = errorText


class NET_DVR_ERROR_DEVICE_NOT_ACTIVATED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 250
        self.errorInfo = errorText


class NET_DVR_ERROR_RISK_PASSWORD(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 251
        self.errorInfo = errorText


class NET_DVR_ERROR_DEVICE_HAS_ACTIVATED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 252
        self.errorInfo = errorText


class NET_DVR_ID_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 300
        self.errorInfo = errorText


class NET_DVR_POLYGON_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 301
        self.errorInfo = errorText


class NET_DVR_RULE_PARAM_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 302
        self.errorInfo = errorText


class NET_DVR_RULE_CFG_CONFLICT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 303
        self.errorInfo = errorText


class NET_DVR_CALIBRATE_NOT_READY(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 304
        self.errorInfo = errorText


class NET_DVR_CAMERA_DATA_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 305
        self.errorInfo = errorText


class NET_DVR_CALIBRATE_DATA_UNFIT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 306
        self.errorInfo = errorText


class NET_DVR_CALIBRATE_DATA_CONFLICT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 307
        self.errorInfo = errorText


class NET_DVR_CALIBRATE_CALC_FAIL(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 308
        self.errorInfo = errorText


class NET_DVR_CALIBRATE_LINE_OUT_RECT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 309
        self.errorInfo = errorText


class NET_DVR_ENTER_RULE_NOT_READY(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 310
        self.errorInfo = errorText


class NET_DVR_AID_RULE_NO_INCLUDE_LANE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 311
        self.errorInfo = errorText


class NET_DVR_LANE_NOT_READY(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 312
        self.errorInfo = errorText


class NET_DVR_RULE_INCLUDE_TWO_WAY(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 313
        self.errorInfo = errorText


class NET_DVR_LANE_TPS_RULE_CONFLICT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 314
        self.errorInfo = errorText


class NET_DVR_NOT_SUPPORT_EVENT_TYPE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 315
        self.errorInfo = errorText


class NET_DVR_LANE_NO_WAY(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 316
        self.errorInfo = errorText


class NET_DVR_SIZE_FILTER_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 317
        self.errorInfo = errorText


class NET_DVR_LIB_FFL_NO_FACE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 318
        self.errorInfo = errorText


class NET_DVR_LIB_FFL_IMG_TOO_SMALL(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 319
        self.errorInfo = errorText


class NET_DVR_LIB_FD_IMG_NO_FACE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 320
        self.errorInfo = errorText


class NET_DVR_LIB_FACE_TOO_SMALL(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 321
        self.errorInfo = errorText


class NET_DVR_LIB_FACE_QUALITY_TOO_BAD(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 322
        self.errorInfo = errorText


class NET_DVR_KEY_PARAM_ERR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 323
        self.errorInfo = errorText


class NET_DVR_CALIBRATE_DATA_ERR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 324
        self.errorInfo = errorText


class NET_DVR_CALIBRATE_DISABLE_FAIL(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 325
        self.errorInfo = errorText


class NET_DVR_VCA_LIB_FD_SCALE_OUTRANGE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 326
        self.errorInfo = errorText


class NET_DVR_LIB_FD_REGION_TOO_LARGE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 327
        self.errorInfo = errorText


class NET_DVR_TRIAL_OVERDUE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 328
        self.errorInfo = errorText


class NET_DVR_CONFIG_FILE_CONFLICT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 329
        self.errorInfo = errorText


class NET_DVR_FR_FPL_FAIL(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 330
        self.errorInfo = errorText


class NET_DVR_FR_IQA_FAIL(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 331
        self.errorInfo = errorText


class NET_DVR_FR_FEM_FAIL(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 332
        self.errorInfo = errorText


class NET_DVR_FPL_DT_CONF_TOO_LOW(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 333
        self.errorInfo = errorText


class NET_DVR_FPL_CONF_TOO_LOW(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 334
        self.errorInfo = errorText


class NET_DVR_E_DATA_SIZE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 335
        self.errorInfo = errorText


class NET_DVR_FR_MODEL_VERSION_ERR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 336
        self.errorInfo = errorText


class NET_DVR_FR_FD_FAIL(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 337
        self.errorInfo = errorText


class NET_DVR_FA_NORMALIZE_ERR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 338
        self.errorInfo = errorText


class NET_DVR_DOG_PUSTREAM_NOT_MATCH(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 339
        self.errorInfo = errorText


class NET_DVR_DEV_PUSTREAM_NOT_MATCH(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 340
        self.errorInfo = errorText


class NET_DVR_PUSTREAM_ALREADY_EXISTS(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 341
        self.errorInfo = errorText


class NET_DVR_SEARCH_CONNECT_FAILED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 342
        self.errorInfo = errorText


class NET_DVR_INSUFFICIENT_DISK_SPACE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 343
        self.errorInfo = errorText


class NET_DVR_DATABASE_CONNECTION_FAILED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 344
        self.errorInfo = errorText


class NET_DVR_DATABASE_ADM_PW_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 345
        self.errorInfo = errorText


class NET_DVR_DECODE_YUV(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 346
        self.errorInfo = errorText


class NET_DVR_IMAGE_RESOLUTION_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 347
        self.errorInfo = errorText


class NET_DVR_CHAN_WORKMODE_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 348
        self.errorInfo = errorText


class NET_DVR_RTSP_ERROR_NOENOUGHPRI(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 401
        self.errorInfo = errorText


class NET_DVR_RTSP_ERROR_ALLOC_RESOURCE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 402
        self.errorInfo = errorText


class NET_DVR_RTSP_ERROR_PARAMETER(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 403
        self.errorInfo = errorText


class NET_DVR_RTSP_ERROR_NO_URL(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 404
        self.errorInfo = errorText


class NET_DVR_RTSP_ERROR_FORCE_STOP(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 406
        self.errorInfo = errorText


class NET_DVR_RTSP_GETPORTFAILED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 407
        self.errorInfo = errorText


class NET_DVR_RTSP_DESCRIBERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 410
        self.errorInfo = errorText


class NET_DVR_RTSP_DESCRIBESENDTIMEOUT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 411
        self.errorInfo = errorText


class NET_DVR_RTSP_DESCRIBESENDERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 412
        self.errorInfo = errorText


class NET_DVR_RTSP_DESCRIBERECVTIMEOUT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 413
        self.errorInfo = errorText


class NET_DVR_RTSP_DESCRIBERECVDATALOST(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 414
        self.errorInfo = errorText


class NET_DVR_RTSP_DESCRIBERECVERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 415
        self.errorInfo = errorText


class NET_DVR_RTSP_DESCRIBESERVERERR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 416
        self.errorInfo = errorText


class NET_DVR_RTSP_SETUPERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 420
        self.errorInfo = errorText


class NET_DVR_RTSP_SETUPSENDTIMEOUT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 421
        self.errorInfo = errorText


class NET_DVR_RTSP_SETUPSENDERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 422
        self.errorInfo = errorText


class NET_DVR_RTSP_SETUPRECVTIMEOUT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 423
        self.errorInfo = errorText


class NET_DVR_RTSP_SETUPRECVDATALOST(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 424
        self.errorInfo = errorText


class NET_DVR_RTSP_SETUPRECVERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 425
        self.errorInfo = errorText


class NET_DVR_RTSP_OVER_MAX_CHAN(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 426
        self.errorInfo = errorText


class NET_DVR_RTSP_SETUPSERVERERR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 427
        self.errorInfo = errorText


class NET_DVR_RTSP_PLAYERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 430
        self.errorInfo = errorText


class NET_DVR_RTSP_PLAYSENDTIMEOUT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 431
        self.errorInfo = errorText


class NET_DVR_RTSP_PLAYSENDERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 432
        self.errorInfo = errorText


class NET_DVR_RTSP_PLAYRECVTIMEOUT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 433
        self.errorInfo = errorText


class NET_DVR_RTSP_PLAYRECVDATALOST(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 434
        self.errorInfo = errorText


class NET_DVR_RTSP_PLAYRECVERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 435
        self.errorInfo = errorText


class NET_DVR_RTSP_PLAYSERVERERR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 436
        self.errorInfo = errorText


class NET_DVR_RTSP_TEARDOWNERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 440
        self.errorInfo = errorText


class NET_DVR_RTSP_TEARDOWNSENDTIMEOUT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 441
        self.errorInfo = errorText


class NET_DVR_RTSP_TEARDOWNSENDERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 442
        self.errorInfo = errorText


class NET_DVR_RTSP_TEARDOWNRECVTIMEOUT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 443
        self.errorInfo = errorText


class NET_DVR_RTSP_TEARDOWNRECVDATALOST(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 444
        self.errorInfo = errorText


class NET_DVR_RTSP_TEARDOWNRECVERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 445
        self.errorInfo = errorText


class NET_DVR_RTSP_TEARDOWNSERVERERR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 446
        self.errorInfo = errorText


class NET_PLAYM4_NOERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 500
        self.errorInfo = errorText


class NET_PLAYM4_PARA_OVER(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 501
        self.errorInfo = errorText


class NET_PLAYM4_ORDER_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 502
        self.errorInfo = errorText


class NET_PLAYM4_TIMER_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 503
        self.errorInfo = errorText


class NET_PLAYM4_DEC_VIDEO_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 504
        self.errorInfo = errorText


class NET_PLAYM4_DEC_AUDIO_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 505
        self.errorInfo = errorText


class NET_PLAYM4_ALLOC_MEMORY_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 506
        self.errorInfo = errorText


class NET_PLAYM4_OPEN_FILE_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 507
        self.errorInfo = errorText


class NET_PLAYM4_CREATE_OBJ_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 508
        self.errorInfo = errorText


class NET_PLAYM4_CREATE_DDRAW_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 509
        self.errorInfo = errorText


class NET_PLAYM4_CREATE_OFFSCREEN_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 510
        self.errorInfo = errorText


class NET_PLAYM4_BUF_OVER(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 511
        self.errorInfo = errorText


class NET_PLAYM4_CREATE_SOUND_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 512
        self.errorInfo = errorText


class NET_PLAYM4_SET_VOLUME_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 513
        self.errorInfo = errorText


class NET_PLAYM4_SUPPORT_FILE_ONLY(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 514
        self.errorInfo = errorText


class NET_PLAYM4_SUPPORT_STREAM_ONLY(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 515
        self.errorInfo = errorText


class NET_PLAYM4_SYS_NOT_SUPPORT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 516
        self.errorInfo = errorText


class NET_PLAYM4_FILEHEADER_UNKNOWN(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 517
        self.errorInfo = errorText


class NET_PLAYM4_VERSION_INCORRECT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 518
        self.errorInfo = errorText


class NET_PALYM4_INIT_DECODER_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 519
        self.errorInfo = errorText


class NET_PLAYM4_CHECK_FILE_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 520
        self.errorInfo = errorText


class NET_PLAYM4_INIT_TIMER_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 521
        self.errorInfo = errorText


class NET_PLAYM4_BLT_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 522
        self.errorInfo = errorText


class NET_PLAYM4_UPDATE_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 523
        self.errorInfo = errorText


class NET_PLAYM4_OPEN_FILE_ERROR_MULTI(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 524
        self.errorInfo = errorText


class NET_PLAYM4_OPEN_FILE_ERROR_VIDEO(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 525
        self.errorInfo = errorText


class NET_PLAYM4_JPEG_COMPRESS_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 526
        self.errorInfo = errorText


class NET_PLAYM4_EXTRACT_NOT_SUPPORT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 527
        self.errorInfo = errorText


class NET_PLAYM4_EXTRACT_DATA_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 528
        self.errorInfo = errorText


class NET_CONVERT_ERROR_NOT_SUPPORT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 581
        self.errorInfo = errorText


class NET_AUDIOINTERCOM_OK(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 600
        self.errorInfo = errorText


class NET_AUDIOINTECOM_ERR_NOTSUPORT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 601
        self.errorInfo = errorText


class NET_AUDIOINTECOM_ERR_ALLOC_MEMERY(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 602
        self.errorInfo = errorText


class NET_AUDIOINTECOM_ERR_PARAMETER(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 603
        self.errorInfo = errorText


class NET_AUDIOINTECOM_ERR_CALL_ORDER(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 604
        self.errorInfo = errorText


class NET_AUDIOINTECOM_ERR_FIND_DEVICE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 605
        self.errorInfo = errorText


class NET_AUDIOINTECOM_ERR_OPEN_DEVICE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 606
        self.errorInfo = errorText


class NET_AUDIOINTECOM_ERR_NO_CONTEXT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 607
        self.errorInfo = errorText


class NET_AUDIOINTECOM_ERR_NO_WAVFILE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 608
        self.errorInfo = errorText


class NET_AUDIOINTECOM_ERR_INVALID_TYPE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 609
        self.errorInfo = errorText


class NET_AUDIOINTECOM_ERR_ENCODE_FAIL(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 610
        self.errorInfo = errorText


class NET_AUDIOINTECOM_ERR_DECODE_FAIL(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 611
        self.errorInfo = errorText


class NET_AUDIOINTECOM_ERR_NO_PLAYBACK(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 612
        self.errorInfo = errorText


class NET_AUDIOINTECOM_ERR_DENOISE_FAIL(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 613
        self.errorInfo = errorText


class NET_AUDIOINTECOM_ERR_UNKOWN(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 619
        self.errorInfo = errorText


class NET_QOS_OK(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 700
        self.errorInfo = errorText


class NET_QOS_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 699
        self.errorInfo = errorText


class NET_QOS_ERR_INVALID_ARGUMENTS(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 698
        self.errorInfo = errorText


class NET_QOS_ERR_SESSION_NOT_FOUND(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 697
        self.errorInfo = errorText


class NET_QOS_ERR_LIB_NOT_INITIALIZED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 696
        self.errorInfo = errorText


class NET_QOS_ERR_OUTOFMEM(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 695
        self.errorInfo = errorText


class NET_QOS_ERR_PACKET_UNKNOW(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 690
        self.errorInfo = errorText


class NET_QOS_ERR_PACKET_VERSION(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 689
        self.errorInfo = errorText


class NET_QOS_ERR_PACKET_LENGTH(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 688
        self.errorInfo = errorText


class NET_QOS_ERR_PACKET_TOO_BIG(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 687
        self.errorInfo = errorText


class NET_QOS_ERR_SCHEDPARAMS_INVALID_BANDWIDTH(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 680
        self.errorInfo = errorText


class NET_QOS_ERR_SCHEDPARAMS_BAD_FRACTION(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 679
        self.errorInfo = errorText


class NET_QOS_ERR_SCHEDPARAMS_BAD_MINIMUM_INTERVAL(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 678
        self.errorInfo = errorText


class NET_ERROR_TRUNK_LINE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 711
        self.errorInfo = errorText


class NET_ERROR_MIXED_JOINT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 712
        self.errorInfo = errorText


class NET_ERROR_DISPLAY_SWITCH(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 713
        self.errorInfo = errorText


class NET_ERROR_USED_BY_BIG_SCREEN(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 714
        self.errorInfo = errorText


class NET_ERROR_USE_OTHER_DEC_RESOURCE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 715
        self.errorInfo = errorText


class NET_ERROR_DISP_MODE_SWITCH(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 716
        self.errorInfo = errorText


class NET_ERROR_SCENE_USING(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 717
        self.errorInfo = errorText


class NET_ERR_NO_ENOUGH_DEC_RESOURCE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 718
        self.errorInfo = errorText


class NET_ERR_NO_ENOUGH_FREE_SHOW_RESOURCE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 719
        self.errorInfo = errorText


class NET_ERR_NO_ENOUGH_VIDEO_MEMORY(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 720
        self.errorInfo = errorText


class NET_ERR_MAX_VIDEO_NUM(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 721
        self.errorInfo = errorText


class NET_ERR_WIN_COVER_FREE_SHOW_AND_NORMAL(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 722
        self.errorInfo = errorText


class NET_ERR_FREE_SHOW_WIN_SPLIT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 723
        self.errorInfo = errorText


class NET_ERR_INAPPROPRIATE_WIN_FREE_SHOW(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 724
        self.errorInfo = errorText


class NET_DVR_TRANSPARENT_WIN_NOT_SUPPORT_SPLIT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 725
        self.errorInfo = errorText


class NET_DVR_SPLIT_WIN_NOT_SUPPORT_TRANSPARENT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 726
        self.errorInfo = errorText


class NET_ERR_MAX_LOGO_NUM(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 727
        self.errorInfo = errorText


class NET_ERR_MAX_WIN_LOOP_NUM(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 728
        self.errorInfo = errorText


class NET_ERR_VIRTUAL_LED_VERTICAL_CROSS(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 729
        self.errorInfo = errorText


class NET_ERR_MAX_VIRTUAL_LED_HEIGHT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 730
        self.errorInfo = errorText


class NET_ERR_VIRTUAL_LED_ILLEGAL_CHARACTER(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 731
        self.errorInfo = errorText


class NET_ERR_BASEMAP_NOT_EXIST(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 732
        self.errorInfo = errorText


class NET_ERR_LED_NOT_SUPPORT_VIRTUAL_LED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 733
        self.errorInfo = errorText


class NET_ERR_LED_RESOLUTION_NOT_SUPPORT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 734
        self.errorInfo = errorText


class NET_ERR_PLAN_OVERDUE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 735
        self.errorInfo = errorText


class NET_ERR_PROCESSER_MAX_SCREEN_BLK(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 736
        self.errorInfo = errorText


class NET_ERR_WND_SIZE_TOO_SMALL(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 737
        self.errorInfo = errorText


class NET_ERR_WND_SPLIT_NOT_SUPPORT_ROAM(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 738
        self.errorInfo = errorText


class NET_ERR_OUTPUT_ONE_BOARD_ONE_WALL(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 739
        self.errorInfo = errorText


class NET_ERR_WND_CANNOT_LCD_AND_LED_OUTPUT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 740
        self.errorInfo = errorText


class NET_ERR_MAX_OSD_NUM(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 741
        self.errorInfo = errorText


class NET_SDK_CANCEL_WND_TOPKEEP_ATTR_FIRST(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 751
        self.errorInfo = errorText


class NET_SDK_ERR_LED_SCREEN_CHECKING(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 752
        self.errorInfo = errorText


class NET_SDK_ERR_NOT_SUPPORT_SINGLE_RESOLUTION(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 753
        self.errorInfo = errorText


class NET_SDK_ERR_LED_RESOLUTION_MISMATCHED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 754
        self.errorInfo = errorText


class NET_SDK_ERR_MAX_VIRTUAL_LED_WIDTH(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 755
        self.errorInfo = errorText


class NET_SDK_ERR_MAX_VIRTUAL_LED_IN_SCREEN(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 756
        self.errorInfo = errorText


class NET_SDK_ERR_MAX_VIRTUAL_LED_IN_WALL(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 757
        self.errorInfo = errorText


class NET_SDK_ERR_VIRTUAL_LED_OVERLAP(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 758
        self.errorInfo = errorText


class NET_SDK_ERR_VIRTUAL_LED_TYPE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 759
        self.errorInfo = errorText


class NET_SDK_ERR_VIRTUAL_LED_COLOUR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 760
        self.errorInfo = errorText


class NET_SDK_ERR_VIRTUAL_LED_MOVE_DIRECTION(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 761
        self.errorInfo = errorText


class NET_SDK_ERR_VIRTUAL_LED_MOVE_MODE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 762
        self.errorInfo = errorText


class NET_SDK_ERR_VIRTUAL_LED_MOVE_SPEED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 763
        self.errorInfo = errorText


class NET_SDK_ERR_VIRTUAL_LED_DISP_MODE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 764
        self.errorInfo = errorText


class NET_SDK_ERR_VIRTUAL_LED_NO(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 765
        self.errorInfo = errorText


class NET_SDK_ERR_VIRTUAL_LED_PARA(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 766
        self.errorInfo = errorText


class NET_SDK_ERR_BASEMAP_POSITION(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 767
        self.errorInfo = errorText


class NET_SDK_ERR_BASEMAP_PICTURE_LEN(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 768
        self.errorInfo = errorText


class NET_SDK_ERR_BASEMAP_PICTURE_RESOLUTION(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 769
        self.errorInfo = errorText


class NET_SDK_ERR_BASEMAP_PICTURE_FORMAT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 770
        self.errorInfo = errorText


class NET_SDK_ERR_MAX_VIRTUAL_LED_NUM(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 771
        self.errorInfo = errorText


class NET_SDK_ERR_MAX_TIME_VIRTUAL_LED_IN_WALL(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 772
        self.errorInfo = errorText


class NET_ERR_TERMINAL_BUSY(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 780
        self.errorInfo = errorText


class NET_ERR_DATA_RETURNED_ILLEGAL(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 790
        self.errorInfo = errorText


class NET_DVR_FUNCTION_RESOURCE_USAGE_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 791
        self.errorInfo = errorText


class NET_DVR_ERR_IMPORT_EMPTY_FILE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 792
        self.errorInfo = errorText


class NET_DVR_ERR_IMPORT_TOO_LARGE_FILE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 793
        self.errorInfo = errorText


class NET_DVR_ERR_BAD_IPV4_ADDRESS(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 794
        self.errorInfo = errorText


class NET_DVR_ERR_BAD_NET_MASK(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 795
        self.errorInfo = errorText


class NET_DVR_ERR_INVALID_NET_GATE_ADDRESS(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 796
        self.errorInfo = errorText


class NET_DVR_ERR_BAD_DNS(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 797
        self.errorInfo = errorText


class NET_DVR_ERR_ILLEGAL_PASSWORD(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 798
        self.errorInfo = errorText


class NET_DVR_DEV_NET_OVERFLOW(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 800
        self.errorInfo = errorText


class NET_DVR_STATUS_RECORDFILE_WRITING_NOT_LOCK(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 801
        self.errorInfo = errorText


class NET_DVR_STATUS_CANT_FORMAT_LITTLE_DISK(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 802
        self.errorInfo = errorText


class NET_SDK_ERR_REMOTE_DISCONNECT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 803
        self.errorInfo = errorText


class NET_SDK_ERR_RD_ADD_RD(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 804
        self.errorInfo = errorText


class NET_SDK_ERR_BACKUP_DISK_EXCEPT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 805
        self.errorInfo = errorText


class NET_SDK_ERR_RD_LIMIT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 806
        self.errorInfo = errorText


class NET_SDK_ERR_ADDED_RD_IS_WD(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 807
        self.errorInfo = errorText


class NET_SDK_ERR_ADD_ORDER_WRONG(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 808
        self.errorInfo = errorText


class NET_SDK_ERR_WD_ADD_WD(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 809
        self.errorInfo = errorText


class NET_SDK_ERR_WD_SERVICE_EXCETP(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 810
        self.errorInfo = errorText


class NET_SDK_ERR_RD_SERVICE_EXCETP(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 811
        self.errorInfo = errorText


class NET_SDK_ERR_ADDED_WD_IS_RD(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 812
        self.errorInfo = errorText


class NET_SDK_ERR_PERFORMANCE_LIMIT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 813
        self.errorInfo = errorText


class NET_SDK_ERR_ADDED_DEVICE_EXIST(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 814
        self.errorInfo = errorText


class NET_SDK_ERR_INQUEST_RESUMING(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 815
        self.errorInfo = errorText


class NET_SDK_ERR_RECORD_BACKUPING(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 816
        self.errorInfo = errorText


class NET_SDK_ERR_DISK_PLAYING(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 817
        self.errorInfo = errorText


class NET_SDK_ERR_INQUEST_STARTED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 818
        self.errorInfo = errorText


class NET_SDK_ERR_LOCAL_OPERATING(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 819
        self.errorInfo = errorText


class NET_SDK_ERR_INQUEST_NOT_START(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 820
        self.errorInfo = errorText


class NET_SDK_ERR_CHAN_AUDIO_BIND(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 821
        self.errorInfo = errorText


class NET_DVR_N_PLUS_ONE_MODE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 822
        self.errorInfo = errorText


class NET_DVR_CLOUD_STORAGE_OPENED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 823
        self.errorInfo = errorText


class NET_DVR_ERR_OPER_NOT_ALLOWED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 824
        self.errorInfo = errorText


class NET_DVR_ERR_NEED_RELOCATE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 825
        self.errorInfo = errorText


class NET_SDK_ERR_IR_PORT_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 830
        self.errorInfo = errorText


class NET_SDK_ERR_IR_CMD_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 831
        self.errorInfo = errorText


class NET_SDK_ERR_NOT_INQUESTING(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 832
        self.errorInfo = errorText


class NET_SDK_ERR_INQUEST_NOT_PAUSED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 833
        self.errorInfo = errorText


class NET_DVR_CHECK_PASSWORD_MISTAKE_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 834
        self.errorInfo = errorText


class NET_DVR_CHECK_PASSWORD_NULL_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 835
        self.errorInfo = errorText


class NET_DVR_UNABLE_CALIB_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 836
        self.errorInfo = errorText


class NET_DVR_PLEASE_CALIB_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 837
        self.errorInfo = errorText


class NET_DVR_ERR_PANORAMIC_CAL_EMPTY(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 838
        self.errorInfo = errorText


class NET_DVR_ERR_CALIB_FAIL_PLEASEAGAIN(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 839
        self.errorInfo = errorText


class NET_DVR_ERR_DETECTION_LINE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 840
        self.errorInfo = errorText


class NET_DVR_ERR_TURN_OFF_IMAGE_PARA(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 841
        self.errorInfo = errorText


class NET_DVR_EXCEED_FACE_IMAGES_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 843
        self.errorInfo = errorText


class NET_DVR_ANALYSIS_FACE_IMAGES_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 844
        self.errorInfo = errorText


class NET_ERR_ALARM_INPUT_OCCUPIED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 845
        self.errorInfo = errorText


class NET_DVR_FACELIB_DATABASE_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 846
        self.errorInfo = errorText


class NET_DVR_FACELIB_DATA_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 847
        self.errorInfo = errorText


class NET_DVR_FACE_DATA_ID_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 848
        self.errorInfo = errorText


class NET_DVR_FACELIB_ID_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 849
        self.errorInfo = errorText


class NET_DVR_EXCEED_FACE_LIBARY_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 850
        self.errorInfo = errorText


class NET_DVR_PIC_ANALYSIS_NO_TARGET_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 851
        self.errorInfo = errorText


class NET_DVR_SUBPIC_ANALYSIS_MODELING_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 852
        self.errorInfo = errorText


class NET_DVR_PIC_ANALYSIS_NO_RESOURCE_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 853
        self.errorInfo = errorText


class NET_DVR_ANALYSIS_ENGINES_NO_RESOURCE_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 854
        self.errorInfo = errorText


class NET_DVR_ANALYSIS_ENGINES_USAGE_EXCEED_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 855
        self.errorInfo = errorText


class NET_DVR_EXCEED_HUMANMISINFO_FILTER_ENABLED_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 856
        self.errorInfo = errorText


class NET_DVR_NAME_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 857
        self.errorInfo = errorText


class NET_DVR_NAME_EXIST_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 858
        self.errorInfo = errorText


class NET_DVR_FACELIB_PIC_IMPORTING_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 859
        self.errorInfo = errorText


class NET_DVR_ERR_CALIB_POSITION(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 860
        self.errorInfo = errorText


class NET_DVR_ERR_DELETE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 861
        self.errorInfo = errorText


class NET_DVR_ERR_SCENE_ID(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 862
        self.errorInfo = errorText


class NET_DVR_ERR_CALIBING(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 863
        self.errorInfo = errorText


class NET_DVR_PIC_FORMAT_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 864
        self.errorInfo = errorText


class NET_DVR_PIC_RESOLUTION_INVALID_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 865
        self.errorInfo = errorText


class NET_DVR_PIC_SIZE_EXCEED_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 866
        self.errorInfo = errorText


class NET_DVR_PIC_ANALYSIS_TARGRT_NUM_EXCEED_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 867
        self.errorInfo = errorText


class NET_DVR_ANALYSIS_ENGINES_LOADING_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 868
        self.errorInfo = errorText


class NET_DVR_ANALYSIS_ENGINES_ABNORMA_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 869
        self.errorInfo = errorText


class NET_DVR_ANALYSIS_ENGINES_FACELIB_IMPORTING(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 870
        self.errorInfo = errorText


class NET_DVR_NO_DATA_FOR_MODELING_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 871
        self.errorInfo = errorText


class NET_DVR_FACE_DATA_MODELING_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 872
        self.errorInfo = errorText


class NET_ERR_FACELIBDATA_OVERLIMIT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 873
        self.errorInfo = errorText


class NET_DVR_ANALYSIS_ENGINES_ASSOCIATED_CHANNEL(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 874
        self.errorInfo = errorText


class NET_DVR_ERR_CUSTOMID_LEN(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 875
        self.errorInfo = errorText


class NET_DVR_ERR_CUSTOMFACELIBID_REPEAT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 876
        self.errorInfo = errorText


class NET_DVR_ERR_CUSTOMHUMANID_REPEAT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 877
        self.errorInfo = errorText


class NET_DVR_ERR_URL_DOWNLOAD_FAIL(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 878
        self.errorInfo = errorText


class NET_DVR_ERR_URL_DOWNLOAD_NOTSTART(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 879
        self.errorInfo = errorText


class NET_DVR_CFG_FILE_SECRETKEY_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 880
        self.errorInfo = errorText


class NET_DVR_WDR_NOTDISABLE_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 881
        self.errorInfo = errorText


class NET_DVR_HLC_NOTDISABLE_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 882
        self.errorInfo = errorText


class NET_DVR_THERMOMETRY_REGION_OVERSTEP_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 883
        self.errorInfo = errorText


class NET_DVR_ERR_MODELING_DEVICEINTERNAL(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 884
        self.errorInfo = errorText


class NET_DVR_ERR_MODELING_FACE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 885
        self.errorInfo = errorText


class NET_DVR_ERR_MODELING_FACEGRADING(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 886
        self.errorInfo = errorText


class NET_DVR_ERR_MODELING_FACEGFEATURE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 887
        self.errorInfo = errorText


class NET_DVR_ERR_MODELING_FACEGANALYZING(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 888
        self.errorInfo = errorText


class NET_DVR_ERR_STREAM_LIMIT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 889
        self.errorInfo = errorText


class NET_DVR_ERR_STREAM_DESCRIPTION(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 890
        self.errorInfo = errorText


class NET_DVR_ERR_STREAM_DELETE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 891
        self.errorInfo = errorText


class NET_DVR_ERR_CUSTOMSTREAM_NAME(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 892
        self.errorInfo = errorText


class NET_DVR_ERR_CUSTOMSTREAM_NOTEXISTED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 893
        self.errorInfo = errorText


class NET_DVR_ERR_TOO_SHORT_CALIBRATING_TIME(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 894
        self.errorInfo = errorText


class NET_DVR_ERR_AUTO_CALIBRATE_FAILED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 895
        self.errorInfo = errorText


class NET_DVR_ERR_VERIFICATION_FAILED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 896
        self.errorInfo = errorText


class NET_DVR_NO_TEMP_SENSOR_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 897
        self.errorInfo = errorText


class NET_DVR_PUPIL_DISTANCE_OVERSIZE_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 898
        self.errorInfo = errorText


class NET_DVR_ERR_UNOPENED_FACE_SNAP(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 899
        self.errorInfo = errorText


class NET_ERR_CUT_INPUTSTREAM_OVERLIMIT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 900
        self.errorInfo = errorText


class NET_ERR_WINCHAN_IDX(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 901
        self.errorInfo = errorText


class NET_ERR_WIN_LAYER(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 902
        self.errorInfo = errorText


class NET_ERR_WIN_BLK_NUM(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 903
        self.errorInfo = errorText


class NET_ERR_OUTPUT_RESOLUTION(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 904
        self.errorInfo = errorText


class NET_ERR_LAYOUT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 905
        self.errorInfo = errorText


class NET_ERR_INPUT_RESOLUTION(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 906
        self.errorInfo = errorText


class NET_ERR_SUBDEVICE_OFFLINE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 907
        self.errorInfo = errorText


class NET_ERR_NO_DECODE_CHAN(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 908
        self.errorInfo = errorText


class NET_ERR_MAX_WINDOW_ABILITY(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 909
        self.errorInfo = errorText


class NET_ERR_ORDER_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 910
        self.errorInfo = errorText


class NET_ERR_PLAYING_PLAN(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 911
        self.errorInfo = errorText


class NET_ERR_DECODER_USED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 912
        self.errorInfo = errorText


class NET_ERR_OUTPUT_BOARD_DATA_OVERFLOW(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 913
        self.errorInfo = errorText


class NET_ERR_SAME_USER_NAME(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 914
        self.errorInfo = errorText


class NET_ERR_INVALID_USER_NAME(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 915
        self.errorInfo = errorText


class NET_ERR_MATRIX_USING(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 916
        self.errorInfo = errorText


class NET_ERR_DIFFERENT_CHAN_TYPE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 917
        self.errorInfo = errorText


class NET_ERR_INPUT_CHAN_BINDED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 918
        self.errorInfo = errorText


class NET_ERR_BINDED_OUTPUT_CHAN_OVERFLOW(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 919
        self.errorInfo = errorText


class NET_ERR_MAX_SIGNAL_NUM(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 920
        self.errorInfo = errorText


class NET_ERR_INPUT_CHAN_USING(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 921
        self.errorInfo = errorText


class NET_ERR_MANAGER_LOGON(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 922
        self.errorInfo = errorText


class NET_ERR_USERALREADY_LOGON(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 923
        self.errorInfo = errorText


class NET_ERR_LAYOUT_INIT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 924
        self.errorInfo = errorText


class NET_ERR_BASEMAP_SIZE_NOT_MATCH(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 925
        self.errorInfo = errorText


class NET_ERR_WINDOW_OPERATING(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 926
        self.errorInfo = errorText


class NET_ERR_SIGNAL_UPLIMIT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 927
        self.errorInfo = errorText


class NET_ERR_SIGNAL_MAX_ENLARGE_TIMES(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 928
        self.errorInfo = errorText


class NET_ERR_ONE_SIGNAL_MULTI_CROSS(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 929
        self.errorInfo = errorText


class NET_ERR_ULTRA_HD_SIGNAL_MULTI_WIN(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 930
        self.errorInfo = errorText


class NET_ERR_MAX_VIRTUAL_LED_WIDTH(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 931
        self.errorInfo = errorText


class NET_ERR_MAX_VIRTUAL_LED_WORD_LEN(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 932
        self.errorInfo = errorText


class NET_ERR_SINGLE_OUTPUTPARAM_CONFIG(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 933
        self.errorInfo = errorText


class NET_ERR_MULTI_WIN_BE_COVER(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 934
        self.errorInfo = errorText


class NET_ERR_WIN_NOT_EXIST(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 935
        self.errorInfo = errorText


class NET_ERR_WIN_MAX_SIGNALSOURCE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 936
        self.errorInfo = errorText


class NET_ERR_MULTI_WIN_MOVE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 937
        self.errorInfo = errorText


class NET_ERR_MULTI_WIN_YPBPR_SDI(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 938
        self.errorInfo = errorText


class NET_ERR_DIFF_TYPE_OUTPUT_MIXUSE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 939
        self.errorInfo = errorText


class NET_ERR_SPLIT_WIN_CROSS(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 940
        self.errorInfo = errorText


class NET_ERR_SPLIT_WIN_NOT_FULL_SCREEN(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 941
        self.errorInfo = errorText


class NET_ERR_SPLIT_WIN_MANY_WIN(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 942
        self.errorInfo = errorText


class NET_ERR_WINDOW_SIZE_OVERLIMIT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 943
        self.errorInfo = errorText


class NET_ERR_INPUTSTREAM_ALREADY_JOINT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 944
        self.errorInfo = errorText


class NET_ERR_JOINT_INPUTSTREAM_OVERLIMIT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 945
        self.errorInfo = errorText


class NET_ERR_LED_RESOLUTION(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 946
        self.errorInfo = errorText


class NET_ERR_JOINT_SCALE_OVERLIMIT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 947
        self.errorInfo = errorText


class NET_ERR_INPUTSTREAM_ALREADY_DECODE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 948
        self.errorInfo = errorText


class NET_ERR_INPUTSTREAM_NOTSUPPORT_CAPTURE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 949
        self.errorInfo = errorText


class NET_ERR_JOINT_NOTSUPPORT_SPLITWIN(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 950
        self.errorInfo = errorText


class NET_ERR_MAX_WIN_OVERLAP(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 951
        self.errorInfo = errorText


class NET_ERR_STREAMID_CHAN_BOTH_VALID(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 952
        self.errorInfo = errorText


class NET_ERR_NO_ZERO_CHAN(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 953
        self.errorInfo = errorText


class NEED_RECONNECT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 955
        self.errorInfo = errorText


class NET_ERR_NO_STREAM_ID(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 956
        self.errorInfo = errorText


class NET_DVR_TRANS_NOT_START(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 957
        self.errorInfo = errorText


class NET_ERR_MAXNUM_STREAM_ID(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 958
        self.errorInfo = errorText


class NET_ERR_WORKMODE_MISMATCH(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 959
        self.errorInfo = errorText


class NET_ERR_MODE_IS_USING(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 960
        self.errorInfo = errorText


class NET_ERR_DEV_PROGRESSING(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 961
        self.errorInfo = errorText


class NET_ERR_PASSIVE_TRANSCODING(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 962
        self.errorInfo = errorText


class NET_ERR_RING_NOT_CONFIGURE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 964
        self.errorInfo = errorText


class NET_ERR_CLOSE_WINDOW_FIRST(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 971
        self.errorInfo = errorText


class NET_ERR_SPLIT_WINDOW_NUM_NOT_SUPPORT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 972
        self.errorInfo = errorText


class NET_ERR_REACH_ONE_SIGNAL_PREVIEW_MAX_LINK(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 973
        self.errorInfo = errorText


class NET_ERR_ONLY_SPLITWND_SUPPORT_AMPLIFICATION(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 974
        self.errorInfo = errorText


class NET_DVR_ERR_WINDOW_SIZE_PLACE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 975
        self.errorInfo = errorText


class NET_DVR_ERR_RGIONAL_RESTRICTIONS(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 976
        self.errorInfo = errorText


class NET_ERR_WNDZOOM_NOT_SUPPORT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 977
        self.errorInfo = errorText


class NET_ERR_LED_SCREEN_SIZE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 978
        self.errorInfo = errorText


class NET_ERR_OPEN_WIN_IN_ERROR_AREA(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 979
        self.errorInfo = errorText


class NET_ERR_TITLE_WIN_NOT_SUPPORT_MOVE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 980
        self.errorInfo = errorText


class NET_ERR_TITLE_WIN_NOT_SUPPORT_COVER(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 981
        self.errorInfo = errorText


class NET_ERR_TITLE_WIN_NOT_SUPPORT_SPLIT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 982
        self.errorInfo = errorText


class NET_DVR_LED_WINDOWS_ALREADY_CLOSED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 983
        self.errorInfo = errorText


class NET_DVR_ERR_CLOSE_WINDOWS(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 984
        self.errorInfo = errorText


class NET_DVR_ERR_MATRIX_LOOP_ABILITY(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 985
        self.errorInfo = errorText


class NET_DVR_ERR_MATRIX_LOOP_TIME(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 986
        self.errorInfo = errorText


class NET_DVR_ERR_LINKED_OUT_ABILITY(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 987
        self.errorInfo = errorText


class NET_ERR_REACH_SCENE_MAX_NUM(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 988
        self.errorInfo = errorText


class NET_ERR_SCENE_MEM_NOT_ENOUGH(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 989
        self.errorInfo = errorText


class NET_ERR_RESOLUTION_NOT_SUPPORT_ODD_VOUT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 990
        self.errorInfo = errorText


class NET_ERR_RESOLUTION_NOT_SUPPORT_EVEN_VOUT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 991
        self.errorInfo = errorText


class NET_DVR_CANCEL_WND_OPENKEEP_ATTR_FIRST(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 992
        self.errorInfo = errorText


class NET_SDK_LED_MODE_NOT_SUPPORT_SPLIT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 993
        self.errorInfo = errorText


class NET_ERR_VOICETALK_ONLY_SUPPORT_ONE_TALK(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 994
        self.errorInfo = errorText


class NET_ERR_WND_POSITION_ADJUSTED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 995
        self.errorInfo = errorText


class NET_SDK_ERR_STARTTIME_CANNOT_LESSTHAN_CURTIME(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 996
        self.errorInfo = errorText


class NET_SDK_ERR_NEED_ADJUST_PLAN(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 997
        self.errorInfo = errorText


class NET_ERR_UnitConfig_Failed(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 998
        self.errorInfo = errorText


class XML_ABILITY_NOTSUPPORT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1000
        self.errorInfo = errorText


class XML_ANALYZE_NOENOUGH_BUF(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1001
        self.errorInfo = errorText


class XML_ANALYZE_FIND_LOCALXML_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1002
        self.errorInfo = errorText


class XML_ANALYZE_LOAD_LOCALXML_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1003
        self.errorInfo = errorText


class XML_NANLYZE_DVR_DATA_FORMAT_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1004
        self.errorInfo = errorText


class XML_ANALYZE_TYPE_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1005
        self.errorInfo = errorText


class XML_ANALYZE_XML_NODE_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1006
        self.errorInfo = errorText


class XML_INPUT_PARAM_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1007
        self.errorInfo = errorText


class NET_DVR_ERR_RETURNED_XML_DATA(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1008
        self.errorInfo = errorText


class NET_ERR_LEDAREA_EXIST_WINDOW(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1051
        self.errorInfo = errorText


class NET_ERR_AUDIO_EXIST(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1052
        self.errorInfo = errorText


class NET_ERR_MATERIAL_NAME_EXIST(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1053
        self.errorInfo = errorText


class NET_ERR_MATERIAL_APPROVE_STATE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1054
        self.errorInfo = errorText


class NET_ERR_DATAHD_SIGNAL_FORMAT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1055
        self.errorInfo = errorText


class NET_ERR_SCENE_SWITCHING(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1056
        self.errorInfo = errorText


class NER_ERR_DATA_TRANSFER(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1057
        self.errorInfo = errorText


class NET_ERR_DATA_RESTORE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1058
        self.errorInfo = errorText


class NET_ERR_CHECK_NOT_ENABLE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1059
        self.errorInfo = errorText


class NET_ERR_AREA_OFFLINE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1060
        self.errorInfo = errorText


class NET_ERR_SCREEN_TYPE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1061
        self.errorInfo = errorText


class NET_ERR_MIN_OPERATE_UNIT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1062
        self.errorInfo = errorText


class NET_ERR_MAINHD_NOT_BACKUP(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1063
        self.errorInfo = errorText


class NET_ERR_ONE_BACKUP_HD(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1064
        self.errorInfo = errorText


class NET_ERR_CONNECT_SUB_SYSTEM_ABNORMAL(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1065
        self.errorInfo = errorText


class NET_ERR_SERIAL_PORT_VEST(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1066
        self.errorInfo = errorText


class NET_ERR_BLOCKLIST_FULL(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1067
        self.errorInfo = errorText


class NET_ERR_NOT_MATCH_SOURCE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1068
        self.errorInfo = errorText


class NET_ERR_CLOCK_VIRTUAL_LED_FULL(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1069
        self.errorInfo = errorText


class NET_ERR_MAX_WIN_SIGNAL_LOOP_NUM(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1070
        self.errorInfo = errorText


class NET_ERR_RESOLUTION_NO_MATCH_FRAME(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1071
        self.errorInfo = errorText


class NET_ERR_NOT_UPDATE_LOW_VERSION(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1072
        self.errorInfo = errorText


class NET_ERR_NO_CUSTOM_TO_UPDATE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1073
        self.errorInfo = errorText


class NET_ERR_CHAN_RESOLUTION_NOT_SUPPORT_SPLIT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1074
        self.errorInfo = errorText


class NET_ERR_HIGH_DEFINITION_NOT_SUPPORT_SPLIT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1075
        self.errorInfo = errorText


class NET_ERR_MIRROR_IMAGE_BY_VIDEO_WALL(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1076
        self.errorInfo = errorText


class NET_ERR_MAX_OSD_FONT_SIZE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1077
        self.errorInfo = errorText


class NET_ERR_HIGH_DEFINITION_NOT_SUPPORT_VIDEO_SET(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1078
        self.errorInfo = errorText


class NET_ERR_TILE_MODE_NOT_SUPPORT_JOINT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1079
        self.errorInfo = errorText


class NET_ERR_ADD_AUDIO_MATRIX_FAILED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1080
        self.errorInfo = errorText


class NET_ERR_ONE_VIRTUAL_LED_AREA_BIND_ONE_AUDIO_AREA(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1081
        self.errorInfo = errorText


class NET_ERR_NAT_NOT_MODIFY_SERVER_NETWORK_PARAM(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1082
        self.errorInfo = errorText


class NET_ERR_ORIGINAL_CHECH_DATA_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1083
        self.errorInfo = errorText


class NET_ERR_INPUT_BOARD_SPLICED_IN_DIFFERENT_NETWORKAREAS(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1084
        self.errorInfo = errorText


class NET_ERR_SPLICINGSOURCE_ONWALL_IN_DIFFERENT_NETWORKAREAS(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1085
        self.errorInfo = errorText


class NET_ERR_ONWALL_OUTPUTBOARD_MODIFY_NETWORKAREAS(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1086
        self.errorInfo = errorText


class NET_ERR_LAN_AND_WAN_CANNOT_SAME_NET_SEGMENT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1087
        self.errorInfo = errorText


class NET_ERR_USERNAME_REPETITIVE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1088
        self.errorInfo = errorText


class NET_ERR_ASSOCIATED_SAMEWALL_IN_DIFFERENT_NETWORKAREAS(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1089
        self.errorInfo = errorText


class NET_ERR_BASEMAP_ROAM_IN_LED_AREA(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1090
        self.errorInfo = errorText


class NET_ERR_VIRTUAL_LED_NOT_SUPPORT_4K_OUTPUT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1091
        self.errorInfo = errorText


class NET_ERR_BASEMAP_NOT_SUPPORT_4K_OUTPUT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1092
        self.errorInfo = errorText


class NET_ERR_MIN_BLOCK_IN_VIRTUAL_LED_AND_OUTPUT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1093
        self.errorInfo = errorText


class NET_ERR_485FIlE_VERSION_INVALID(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1094
        self.errorInfo = errorText


class NET_ERR_485FIlE_CHECK_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1095
        self.errorInfo = errorText


class NET_ERR_485FIlE_ABNORMAL_SIZE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1096
        self.errorInfo = errorText


class NET_ERR_MODIFY_SUBBOARD_NETCFG_IN_NAT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1097
        self.errorInfo = errorText


class NET_ERR_OSD_CONTENT_WITH_ILLEGAL_CHARACTERS(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1098
        self.errorInfo = errorText


class NET_ERR_NON_SLAVE_DEVICE_INSERT_SYNC_LINE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1099
        self.errorInfo = errorText


class NET_ERR_PLT_USERID(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1100
        self.errorInfo = errorText


class NET_ERR_TRANS_CHAN_START(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1101
        self.errorInfo = errorText


class NET_ERR_DEV_UPGRADING(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1102
        self.errorInfo = errorText


class NET_ERR_MISMATCH_UPGRADE_PACK_TYPE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1103
        self.errorInfo = errorText


class NET_ERR_DEV_FORMATTING(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1104
        self.errorInfo = errorText


class NET_ERR_MISMATCH_UPGRADE_PACK_VERSION(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1105
        self.errorInfo = errorText


class NET_ERR_PT_LOCKED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1106
        self.errorInfo = errorText


class NET_DVR_LOGO_OVERLAY_WITHOUT_UPLOAD_PIC(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1110
        self.errorInfo = errorText


class NET_DVR_ERR_ILLEGAL_VERIFICATION_CODE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1111
        self.errorInfo = errorText


class NET_DVR_ERR_LACK_VERIFICATION_CODE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1112
        self.errorInfo = errorText


class NET_DVR_ERR_FORBIDDEN_IP(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1113
        self.errorInfo = errorText


class NET_DVR_ERR_UNLOCKPTZ(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1114
        self.errorInfo = errorText


class NET_DVR_ERR_COUNTAREA_LARGE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1116
        self.errorInfo = errorText


class NET_DVR_ERR_LABEL_ID_EXCEED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1117
        self.errorInfo = errorText


class NET_DVR_ERR_LABEL_TYPE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1118
        self.errorInfo = errorText


class NET_DVR_ERR_LABEL_FULL(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1119
        self.errorInfo = errorText


class NET_DVR_ERR_LABEL_DISABLED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1120
        self.errorInfo = errorText


class NET_DVR_ERR_DOME_PT_TRANS_TO_DOME_XY(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1121
        self.errorInfo = errorText


class NET_DVR_ERR_DOME_PT_TRANS_TO_PANORAMA_XY(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1122
        self.errorInfo = errorText


class NET_DVR_ERR_PANORAMA_XY_TRANS_TO_DOME_PT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1123
        self.errorInfo = errorText


class NET_DVR_ERR_SCENE_DUR_TIME_LESS_THAN_INTERV_TIME(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1124
        self.errorInfo = errorText


class NET_DVR_ERR_HTTP_BKN_EXCEED_ONE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1125
        self.errorInfo = errorText


class NET_DVR_ERR_DELETING_FAILED_TURN_OFF_HTTPS_ESDK_WEBSOCKETS_FIRST(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1126
        self.errorInfo = errorText


class NET_DVR_ERR_DELETING_FAILED_TURN_OFF_HTTPS_ESDK_FIRST(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1127
        self.errorInfo = errorText


class NET_DVR_ERR_PTZ_OCCUPIED_PRIORITY(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1128
        self.errorInfo = errorText


class NET_DVR_ERR_INCORRECT_VIDEOAUDIO_ID(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1129
        self.errorInfo = errorText


class NET_DVR_ERR_REPETITIONTIME_OVER_MAXIMUM(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1130
        self.errorInfo = errorText


class NET_DVR_ERR_FORMATTING_FAILED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1131
        self.errorInfo = errorText


class NET_DVR_ERR_ENCRYPTED_FORMATTING_FAILED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1132
        self.errorInfo = errorText


class NET_DVR_ERR_WRONG_PASSWORD(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1133
        self.errorInfo = errorText


class NET_DVR_ERR_EXPOSURE_SYNC(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1134
        self.errorInfo = errorText


class NET_ERR_SEARCHING_MODULE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1201
        self.errorInfo = errorText


class NET_ERR_REGISTERING_MODULE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1202
        self.errorInfo = errorText


class NET_ERR_GETTING_ZONES(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1203
        self.errorInfo = errorText


class NET_ERR_GETTING_TRIGGERS(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1204
        self.errorInfo = errorText


class NET_ERR_ARMED_STATUS(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1205
        self.errorInfo = errorText


class NET_ERR_PROGRAM_MODE_STATUS(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1206
        self.errorInfo = errorText


class NET_ERR_WALK_TEST_MODE_STATUS(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1207
        self.errorInfo = errorText


class NET_ERR_BYPASS_STATUS(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1208
        self.errorInfo = errorText


class NET_ERR_DISABLED_MODULE_STATUS(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1209
        self.errorInfo = errorText


class NET_ERR_NOT_SUPPORT_OPERATE_ZONE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1210
        self.errorInfo = errorText


class NET_ERR_NOT_SUPPORT_MOD_MODULE_ADDR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1211
        self.errorInfo = errorText


class NET_ERR_UNREGISTERED_MODULE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1212
        self.errorInfo = errorText


class NET_ERR_PUBLIC_SUBSYSTEM_ASSOCIATE_SELF(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1213
        self.errorInfo = errorText


class NET_ERR_EXCEEDS_ASSOCIATE_SUBSYSTEM_NUM(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1214
        self.errorInfo = errorText


class NET_ERR_BE_ASSOCIATED_BY_PUBLIC_SUBSYSTEM(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1215
        self.errorInfo = errorText


class NET_ERR_ZONE_FAULT_STATUS(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1216
        self.errorInfo = errorText


class NET_ERR_SAME_EVENT_TYPE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1217
        self.errorInfo = errorText


class NET_ERR_ZONE_ALARM_STATUS(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1218
        self.errorInfo = errorText


class NET_ERR_EXPANSION_BUS_SHORT_CIRCUIT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1219
        self.errorInfo = errorText


class NET_ERR_PWD_CONFLICT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1220
        self.errorInfo = errorText


class NET_ERR_DETECTOR_GISTERED_BY_OTHER_ZONE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1221
        self.errorInfo = errorText


class NET_ERR_DETECTOR_GISTERED_BY_OTHER_PU(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1222
        self.errorInfo = errorText


class NET_ERR_DETECTOR_DISCONNECT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1223
        self.errorInfo = errorText


class NET_ERR_CALL_BUSY(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1224
        self.errorInfo = errorText


class NET_DVR_ERR_ZONE_TAMPER_STAUS(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1225
        self.errorInfo = errorText


class NET_DVR_ERR_WIRELESS_DEV_REGISTER(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1226
        self.errorInfo = errorText


class NET_DVR_ERR_WIRELESS_DEV_ADDED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1227
        self.errorInfo = errorText


class NET_DVR_ERR_WIRELESS_DEV_OFFLINE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1228
        self.errorInfo = errorText


class NET_DVR_ERR_WIRELESS_DEV_TAMPER_STATUS(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1229
        self.errorInfo = errorText


class NET_DVR_ERR_GPRS_PHONE_CONFLICT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1230
        self.errorInfo = errorText


class NET_ERR_INIT_PASSWORD_NOT_MODIFY(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1231
        self.errorInfo = errorText


class NET_ERR_USER_DISABLED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1232
        self.errorInfo = errorText


class NET_ERR_DEVICE_DEBUGGING(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1233
        self.errorInfo = errorText


class NET_ERR_GET_ALL_RETURN_OVER(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1300
        self.errorInfo = errorText


class NET_ERR_RESOURCE_USING(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1301
        self.errorInfo = errorText


class NET_ERR_FILE_SIZE_OVERLIMIT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1302
        self.errorInfo = errorText


class NET_ERR_MATERIAL_NAME(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1303
        self.errorInfo = errorText


class NET_ERR_MATERIAL_NAME_LEN(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1304
        self.errorInfo = errorText


class NET_ERR_MATERIAL_REMARK(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1305
        self.errorInfo = errorText


class NET_ERR_MATERIAL_REMARK_LEN(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1306
        self.errorInfo = errorText


class NET_ERR_MATERIAL_SHARE_PROPERTY(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1307
        self.errorInfo = errorText


class NET_ERR_UNSUPPORT_MATERIAL_TYPE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1308
        self.errorInfo = errorText


class NET_ERR_MATERIAL_NOT_EXIST(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1309
        self.errorInfo = errorText


class NET_ERR_READ_FROM_DISK(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1310
        self.errorInfo = errorText


class NET_ERR_WRITE_TO_DISK(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1311
        self.errorInfo = errorText


class NET_ERR_WRITE_DATA_BASE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1312
        self.errorInfo = errorText


class NET_ERR_NO_APPROVED_NOT_EXPORT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1313
        self.errorInfo = errorText


class NET_ERR_MATERIAL_EXCEPTION(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1314
        self.errorInfo = errorText


class NET_ERR_NO_MISINFO(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1315
        self.errorInfo = errorText


class NET_ERR_LAN_NOT_SUP_DHCP_CLIENT_CONFIGURATION(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1316
        self.errorInfo = errorText


class NET_ERR_VIDEOWALL_OPTPORT_RESOLUTION_INCONSISTENT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1317
        self.errorInfo = errorText


class NET_ERR_VIDEOWALL_OPTPORT_RESOLUTION_INCONSISTENT_UNBIND_OPTPORT_FIRST(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1318
        self.errorInfo = errorText


class NET_ERR_FOUR_K_OUTPUT_RESOLUTION_UNSUPPORT_NINE_TO_SIXTEEN_SPLIT_SCREEN(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1319
        self.errorInfo = errorText


class NET_ERR_SIGNAL_SOURCE_UNSUPPORT_CUSTOM_RESOLUTION(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1320
        self.errorInfo = errorText


class NET_ERR_DVI_UNSUPPORT_FOURK_OUTPUT_RESOLUTION(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1321
        self.errorInfo = errorText


class NET_ERR_BNC_UNSUPPORT_SOURCE_CROPPING(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1322
        self.errorInfo = errorText


class NET_ERR_OUTPUT_NOT_SUPPORT_VIDEOWALL_RESOLUTION(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1323
        self.errorInfo = errorText


class NET_ERR_MAX_SCREEN_CTRL_NUM(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1351
        self.errorInfo = errorText


class NET_ERR_FILE_NOT_EXIST(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1352
        self.errorInfo = errorText


class NET_ERR_THUMBNAIL_NOT_EXIST(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1353
        self.errorInfo = errorText


class NET_ERR_DEV_OPEN_FILE_FAIL(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1354
        self.errorInfo = errorText


class NET_ERR_SERVER_READ_FILE_FAIL(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1355
        self.errorInfo = errorText


class NET_ERR_FILE_SIZE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1356
        self.errorInfo = errorText


class NET_ERR_FILE_NAME(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1357
        self.errorInfo = errorText


class NET_ERR_BROADCAST_BUSY(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1358
        self.errorInfo = errorText


class NET_DVR_ERR_LANENUM_EXCEED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1400
        self.errorInfo = errorText


class NET_DVR_ERR_PRAREA_EXCEED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1401
        self.errorInfo = errorText


class NET_DVR_ERR_LIGHT_PARAM(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1402
        self.errorInfo = errorText


class NET_DVR_ERR_LANE_LINE_INVALID(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1403
        self.errorInfo = errorText


class NET_DVR_ERR_STOP_LINE_INVALID(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1404
        self.errorInfo = errorText


class NET_DVR_ERR_LEFTORRIGHT_LINE_INVALID(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1405
        self.errorInfo = errorText


class NET_DVR_ERR_LANE_NO_REPEAT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1406
        self.errorInfo = errorText


class NET_DVR_ERR_PRAREA_INVALID(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1407
        self.errorInfo = errorText


class NET_DVR_ERR_LIGHT_NUM_EXCEED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1408
        self.errorInfo = errorText


class NET_DVR_ERR_SUBLIGHT_NUM_INVALID(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1409
        self.errorInfo = errorText


class NET_DVR_ERR_LIGHT_AREASIZE_INVALID(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1410
        self.errorInfo = errorText


class NET_DVR_ERR_LIGHT_COLOR_INVALID(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1411
        self.errorInfo = errorText


class NET_DVR_ERR_LIGHT_DIRECTION_INVALID(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1412
        self.errorInfo = errorText


class NET_DVR_ERR_LACK_IOABLITY(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1413
        self.errorInfo = errorText


class NET_DVR_ERR_FTP_PORT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1414
        self.errorInfo = errorText


class NET_DVR_ERR_FTP_CATALOGUE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1415
        self.errorInfo = errorText


class NET_DVR_ERR_FTP_UPLOAD_TYPE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1416
        self.errorInfo = errorText


class NET_DVR_ERR_FLASH_PARAM_WRITE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1417
        self.errorInfo = errorText


class NET_DVR_ERR_FLASH_PARAM_READ(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1418
        self.errorInfo = errorText


class NET_DVR_ERR_PICNAME_DELIMITER(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1419
        self.errorInfo = errorText


class NET_DVR_ERR_PICNAME_ITEM(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1420
        self.errorInfo = errorText


class NET_DVR_ERR_PLATE_RECOGNIZE_TYPE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1421
        self.errorInfo = errorText


class NET_DVR_ERR_CAPTURE_TIMES(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1422
        self.errorInfo = errorText


class NET_DVR_ERR_LOOP_DISTANCE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1423
        self.errorInfo = errorText


class NET_DVR_ERR_LOOP_INPUT_STATUS(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1424
        self.errorInfo = errorText


class NET_DVR_ERR_RELATE_IO_CONFLICT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1425
        self.errorInfo = errorText


class NET_DVR_ERR_INTERVAL_TIME(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1426
        self.errorInfo = errorText


class NET_DVR_ERR_SIGN_SPEED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1427
        self.errorInfo = errorText


class NET_DVR_ERR_PIC_FLIP(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1428
        self.errorInfo = errorText


class NET_DVR_ERR_RELATE_LANE_NUMBER(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1429
        self.errorInfo = errorText


class NET_DVR_ERR_TRIGGER_MODE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1430
        self.errorInfo = errorText


class NET_DVR_ERR_DELAY_TIME(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1431
        self.errorInfo = errorText


class NET_DVR_ERR_EXCEED_RS485_COUNT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1432
        self.errorInfo = errorText


class NET_DVR_ERR_RADAR_TYPE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1433
        self.errorInfo = errorText


class NET_DVR_ERR_RADAR_ANGLE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1434
        self.errorInfo = errorText


class NET_DVR_ERR_RADAR_SPEED_VALID_TIME(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1435
        self.errorInfo = errorText


class NET_DVR_ERR_RADAR_LINE_CORRECT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1436
        self.errorInfo = errorText


class NET_DVR_ERR_RADAR_CONST_CORRECT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1437
        self.errorInfo = errorText


class NET_DVR_ERR_RECORD_PARAM(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1438
        self.errorInfo = errorText


class NET_DVR_ERR_LIGHT_WITHOUT_COLOR_AND_DIRECTION(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1439
        self.errorInfo = errorText


class NET_DVR_ERR_LIGHT_WITHOUT_DETECTION_REGION(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1440
        self.errorInfo = errorText


class NET_DVR_ERR_RECOGNIZE_PROVINCE_PARAM(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1441
        self.errorInfo = errorText


class NET_DVR_ERR_SPEED_TIMEOUT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1442
        self.errorInfo = errorText


class NET_DVR_ERR_NTP_TIMEZONE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1443
        self.errorInfo = errorText


class NET_DVR_ERR_NTP_INTERVAL_TIME(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1444
        self.errorInfo = errorText


class NET_DVR_ERR_NETWORK_CARD_NUM(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1445
        self.errorInfo = errorText


class NET_DVR_ERR_DEFAULT_ROUTE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1446
        self.errorInfo = errorText


class NET_DVR_ERR_BONDING_WORK_MODE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1447
        self.errorInfo = errorText


class NET_DVR_ERR_SLAVE_CARD(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1448
        self.errorInfo = errorText


class NET_DVR_ERR_PRIMARY_CARD(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1449
        self.errorInfo = errorText


class NET_DVR_ERR_DHCP_PPOE_WORK(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1450
        self.errorInfo = errorText


class NET_DVR_ERR_NET_INTERFACE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1451
        self.errorInfo = errorText


class NET_DVR_ERR_MTU(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1452
        self.errorInfo = errorText


class NET_DVR_ERR_NETMASK(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1453
        self.errorInfo = errorText


class NET_DVR_ERR_IP_INVALID(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1454
        self.errorInfo = errorText


class NET_DVR_ERR_MULTICAST_IP_INVALID(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1455
        self.errorInfo = errorText


class NET_DVR_ERR_GATEWAY_INVALID(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1456
        self.errorInfo = errorText


class NET_DVR_ERR_DNS_INVALID(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1457
        self.errorInfo = errorText


class NET_DVR_ERR_ALARMHOST_IP_INVALID(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1458
        self.errorInfo = errorText


class NET_DVR_ERR_IP_CONFLICT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1459
        self.errorInfo = errorText


class NET_DVR_ERR_NETWORK_SEGMENT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1460
        self.errorInfo = errorText


class NET_DVR_ERR_NETPORT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1461
        self.errorInfo = errorText


class NET_DVR_ERR_PPPOE_NOSUPPORT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1462
        self.errorInfo = errorText


class NET_DVR_ERR_DOMAINNAME_NOSUPPORT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1463
        self.errorInfo = errorText


class NET_DVR_ERR_NO_SPEED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1464
        self.errorInfo = errorText


class NET_DVR_ERR_IOSTATUS_INVALID(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1465
        self.errorInfo = errorText


class NET_DVR_ERR_BURST_INTERVAL_INVALID(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1466
        self.errorInfo = errorText


class NET_DVR_ERR_RESERVE_MODE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1467
        self.errorInfo = errorText


class NET_DVR_ERR_LANE_NO(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1468
        self.errorInfo = errorText


class NET_DVR_ERR_COIL_AREA_TYPE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1469
        self.errorInfo = errorText


class NET_DVR_ERR_TRIGGER_AREA_PARAM(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1470
        self.errorInfo = errorText


class NET_DVR_ERR_SPEED_LIMIT_PARAM(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1471
        self.errorInfo = errorText


class NET_DVR_ERR_LANE_PROTOCOL_TYPE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1472
        self.errorInfo = errorText


class NET_DVR_ERR_INTERVAL_TYPE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1473
        self.errorInfo = errorText


class NET_DVR_ERR_INTERVAL_DISTANCE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1474
        self.errorInfo = errorText


class NET_DVR_ERR_RS485_ASSOCIATE_DEVTYPE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1475
        self.errorInfo = errorText


class NET_DVR_ERR_RS485_ASSOCIATE_LANENO(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1476
        self.errorInfo = errorText


class NET_DVR_ERR_LANENO_ASSOCIATE_MULTIRS485(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1477
        self.errorInfo = errorText


class NET_DVR_ERR_LIGHT_DETECTION_REGION(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1478
        self.errorInfo = errorText


class NET_DVR_ERR_DN2D_NOSUPPORT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1479
        self.errorInfo = errorText


class NET_DVR_ERR_IRISMODE_NOSUPPORT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1480
        self.errorInfo = errorText


class NET_DVR_ERR_WB_NOSUPPORT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1481
        self.errorInfo = errorText


class NET_DVR_ERR_IO_EFFECTIVENESS(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1482
        self.errorInfo = errorText


class NET_DVR_ERR_LIGHTNO_MAX(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1483
        self.errorInfo = errorText


class NET_DVR_ERR_LIGHTNO_CONFLICT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1484
        self.errorInfo = errorText


class NET_DVR_ERR_CANCEL_LINE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1485
        self.errorInfo = errorText


class NET_DVR_ERR_STOP_LINE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1486
        self.errorInfo = errorText


class NET_DVR_ERR_RUSH_REDLIGHT_LINE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1487
        self.errorInfo = errorText


class NET_DVR_ERR_IOOUTNO_MAX(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1488
        self.errorInfo = errorText


class NET_DVR_ERR_IOOUTNO_AHEADTIME_MAX(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1489
        self.errorInfo = errorText


class NET_DVR_ERR_IOOUTNO_IOWORKTIME(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1490
        self.errorInfo = errorText


class NET_DVR_ERR_IOOUTNO_FREQMULTI(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1491
        self.errorInfo = errorText


class NET_DVR_ERR_IOOUTNO_DUTYRATE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1492
        self.errorInfo = errorText


class NET_DVR_ERR_VIDEO_WITH_EXPOSURE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1493
        self.errorInfo = errorText


class NET_DVR_ERR_PLATE_BRIGHTNESS_WITHOUT_FLASHDET(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1494
        self.errorInfo = errorText


class NET_DVR_ERR_RECOGNIZE_TYPE_PARAM(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1495
        self.errorInfo = errorText


class NET_DVR_ERR_PALTE_RECOGNIZE_AREA_PARAM(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1496
        self.errorInfo = errorText


class NET_DVR_ERR_PORT_CONFLICT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1497
        self.errorInfo = errorText


class NET_DVR_ERR_LOOP_IP(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1498
        self.errorInfo = errorText


class NET_DVR_ERR_DRIVELINE_SENSITIVE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1499
        self.errorInfo = errorText


class NET_ERR_VQD_TIME_CONFLICT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1500
        self.errorInfo = errorText


class NET_ERR_VQD_PLAN_NO_EXIST(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1501
        self.errorInfo = errorText


class NET_ERR_VQD_CHAN_NO_EXIST(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1502
        self.errorInfo = errorText


class NET_ERR_VQD_CHAN_MAX(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1503
        self.errorInfo = errorText


class NET_ERR_VQD_TASK_MAX(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1504
        self.errorInfo = errorText


class NET_SDK_GET_INPUTSTREAMCFG(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1551
        self.errorInfo = errorText


class NET_SDK_AUDIO_SWITCH_CONTROL(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1552
        self.errorInfo = errorText


class NET_SDK_GET_VIDEOWALLDISPLAYNO(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1553
        self.errorInfo = errorText


class NET_SDK_GET_ALLSUBSYSTEM_BASIC_INFO(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1554
        self.errorInfo = errorText


class NET_SDK_SET_ALLSUBSYSTEM_BASIC_INFO(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1555
        self.errorInfo = errorText


class NET_SDK_GET_AUDIO_INFO(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1556
        self.errorInfo = errorText


class NET_SDK_GET_MATRIX_STATUS_V50(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1557
        self.errorInfo = errorText


class NET_SDK_DELETE_MONITOR_INFO(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1558
        self.errorInfo = errorText


class NET_SDK_DELETE_CAMERA_INFO(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1559
        self.errorInfo = errorText


class NET_DVR_ERR_EXCEED_MAX_CAPTURE_TIMES(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1600
        self.errorInfo = errorText


class NET_DVR_ERR_REDAR_TYPE_CONFLICT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1601
        self.errorInfo = errorText


class NET_DVR_ERR_LICENSE_PLATE_NULL(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1602
        self.errorInfo = errorText


class NET_DVR_ERR_WRITE_DATABASE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1603
        self.errorInfo = errorText


class NET_DVR_ERR_LICENSE_EFFECTIVE_TIME(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1604
        self.errorInfo = errorText


class NET_DVR_ERR_PRERECORDED_STARTTIME_LONG(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1605
        self.errorInfo = errorText


class NET_DVR_ERR_TRIGGER_RULE_LINE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1606
        self.errorInfo = errorText


class NET_DVR_ERR_LEFTRIGHT_TRIGGERLINE_NOTVERTICAL(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1607
        self.errorInfo = errorText


class NET_DVR_ERR_FLASH_LAMP_MODE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1608
        self.errorInfo = errorText


class NET_DVR_ERR_ILLEGAL_SNAPSHOT_NUM(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1609
        self.errorInfo = errorText


class NET_DVR_ERR_ILLEGAL_DETECTION_TYPE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1610
        self.errorInfo = errorText


class NET_DVR_ERR_POSITIVEBACK_TRIGGERLINE_HIGH(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1611
        self.errorInfo = errorText


class NET_DVR_ERR_MIXEDMODE_CAPTYPE_ALLTARGETS(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1612
        self.errorInfo = errorText


class NET_DVR_ERR_CARSIGNSPEED_GREATERTHAN_LIMITSPEED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1613
        self.errorInfo = errorText


class NET_DVR_ERR_BIGCARSIGNSPEED_GREATERTHAN_LIMITSPEED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1614
        self.errorInfo = errorText


class NET_DVR_ERR_BIGCARSIGNSPEED_GREATERTHAN_CARSIGNSPEED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1615
        self.errorInfo = errorText


class NET_DVR_ERR_BIGCARLIMITSPEED_GREATERTHAN_CARLIMITSPEED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1616
        self.errorInfo = errorText


class NET_DVR_ERR_BIGCARLOWSPEEDLIMIT_GREATERTHAN_CARLOWSPEEDLIMIT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1617
        self.errorInfo = errorText


class NET_DVR_ERR_CARLIMITSPEED_GREATERTHAN_EXCEPHIGHSPEED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1618
        self.errorInfo = errorText


class NET_DVR_ERR_BIGCARLIMITSPEED_GREATERTHAN_EXCEPHIGHSPEED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1619
        self.errorInfo = errorText


class NET_DVR_ERR_STOPLINE_MORETHAN_TRIGGERLINE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1620
        self.errorInfo = errorText


class NET_DVR_ERR_YELLOWLIGHTTIME_INVALID(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1621
        self.errorInfo = errorText


class NET_DVR_ERR_TRIGGERLINE1_FOR_NOT_YIELD_TO_PEDESTRIAN_CANNOT_EXCEED_TRIGGERLINE2(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1622
        self.errorInfo = errorText


class NET_DVR_ERR_TRIGGERLINE2_FOR_NOT_YIELD_TO_PEDESTRIAN_CANNOT_EXCEED_TRIGGERLINE1(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1623
        self.errorInfo = errorText


class NET_ERR_TIME_OVERLAP(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1900
        self.errorInfo = errorText


class NET_ERR_HOLIDAY_PLAN_OVERLAP(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1901
        self.errorInfo = errorText


class NET_ERR_CARDNO_NOT_SORT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1902
        self.errorInfo = errorText


class NET_ERR_CARDNO_NOT_EXIST(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1903
        self.errorInfo = errorText


class NET_ERR_ILLEGAL_CARDNO(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1904
        self.errorInfo = errorText


class NET_ERR_ZONE_ALARM(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1905
        self.errorInfo = errorText


class NET_ERR_ZONE_OPERATION_NOT_SUPPORT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1906
        self.errorInfo = errorText


class NET_ERR_INTERLOCK_ANTI_CONFLICT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1907
        self.errorInfo = errorText


class NET_ERR_DEVICE_CARD_FULL(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1908
        self.errorInfo = errorText


class NET_ERR_HOLIDAY_GROUP_DOWNLOAD(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1909
        self.errorInfo = errorText


class NET_ERR_LOCAL_CONTROL_OFF(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1910
        self.errorInfo = errorText


class NET_ERR_LOCAL_CONTROL_DISADD(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1911
        self.errorInfo = errorText


class NET_ERR_LOCAL_CONTROL_HASADD(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1912
        self.errorInfo = errorText


class NET_ERR_LOCAL_CONTROL_DOORNO_CONFLICT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1913
        self.errorInfo = errorText


class NET_ERR_LOCAL_CONTROL_COMMUNICATION_FAIL(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1914
        self.errorInfo = errorText


class NET_ERR_OPERAND_INEXISTENCE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1915
        self.errorInfo = errorText


class NET_ERR_LOCAL_CONTROL_OVER_LIMIT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1916
        self.errorInfo = errorText


class NET_ERR_DOOR_OVER_LIMIT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1917
        self.errorInfo = errorText


class NET_ERR_ALARM_OVER_LIMIT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1918
        self.errorInfo = errorText


class NET_ERR_LOCAL_CONTROL_ADDRESS_INCONFORMITY_TYPE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1919
        self.errorInfo = errorText


class NET_ERR_NOT_SUPPORT_ONE_MORE_CARD(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1920
        self.errorInfo = errorText


class NET_ERR_DELETE_NO_EXISTENCE_FACE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1921
        self.errorInfo = errorText


class NET_ERR_DOOR_SPECIAL_PASSWORD_REPEAT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1922
        self.errorInfo = errorText


class NET_ERR_AUTH_CODE_REPEAT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1923
        self.errorInfo = errorText


class NET_ERR_DEPLOY_EXCEED_MAX(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1924
        self.errorInfo = errorText


class NET_ERR_NOT_SUPPORT_DEL_FP_BY_ID(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1925
        self.errorInfo = errorText


class NET_ERR_TIME_RANGE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1926
        self.errorInfo = errorText


class NET_ERR_CAPTURE_TIMEOUT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1927
        self.errorInfo = errorText


class NET_ERR_LOW_SCORE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1928
        self.errorInfo = errorText


class NET_ERR_OFFLINE_CAPTURING(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1929
        self.errorInfo = errorText


class NET_DVR_ERR_OUTDOOR_COMMUNICATION(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1950
        self.errorInfo = errorText


class NET_DVR_ERR_ROOMNO_UNDEFINED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1951
        self.errorInfo = errorText


class NET_DVR_ERR_NO_CALLING(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1952
        self.errorInfo = errorText


class NET_DVR_ERR_RINGING(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1953
        self.errorInfo = errorText


class NET_DVR_ERR_IS_CALLING_NOW(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1954
        self.errorInfo = errorText


class NET_DVR_ERR_LOCK_PASSWORD_WRONG(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1955
        self.errorInfo = errorText


class NET_DVR_ERR_CONTROL_LOCK_FAILURE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1956
        self.errorInfo = errorText


class NET_DVR_ERR_CONTROL_LOCK_OVERTIME(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1957
        self.errorInfo = errorText


class NET_DVR_ERR_LOCK_DEVICE_BUSY(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1958
        self.errorInfo = errorText


class NET_DVR_ERR_UNOPEN_REMOTE_LOCK_FUNCTION(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1959
        self.errorInfo = errorText


class NET_DVR_ERR_FILE_NOT_COMPLETE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2100
        self.errorInfo = errorText


class NET_DVR_ERR_IPC_EXIST(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2101
        self.errorInfo = errorText


class NET_DVR_ERR_ADD_IPC(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2102
        self.errorInfo = errorText


class NET_DVR_ERR_OUT_OF_RES(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2103
        self.errorInfo = errorText


class NET_DVR_ERR_CONFLICT_TO_LOCALIP(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2104
        self.errorInfo = errorText


class NET_DVR_ERR_IP_SET(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2105
        self.errorInfo = errorText


class NET_DVR_ERR_PORT_SET(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2106
        self.errorInfo = errorText


class NET_ERR_WAN_NOTSUPPORT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2107
        self.errorInfo = errorText


class NET_ERR_MUTEX_FUNCTION(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2108
        self.errorInfo = errorText


class NET_ERR_QUESTION_CONFIGNUM(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2109
        self.errorInfo = errorText


class NET_ERR_FACECHAN_NORESOURCE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2110
        self.errorInfo = errorText


class NET_ERR_DATA_CALLBACK(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2111
        self.errorInfo = errorText


class NET_ERR_ATM_VCA_CHAN_IS_RELATED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2112
        self.errorInfo = errorText


class NET_ERR_ATM_VCA_CHAN_IS_OVERLAPED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2113
        self.errorInfo = errorText


class NET_ERR_FACE_CHAN_UNOVERLAP_EACH_OTHER(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2114
        self.errorInfo = errorText


class NET_ERR_ACHIEVE_MAX_CHANNLE_LIMIT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2115
        self.errorInfo = errorText


class NET_DVR_SMD_ENCODING_NORESOURSE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2116
        self.errorInfo = errorText


class NET_DVR_SMD_DECODING_NORESOURSE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2117
        self.errorInfo = errorText


class NET_DVR_FACELIB_DATA_PROCESSING(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2118
        self.errorInfo = errorText


class NET_DVR_ERR_LARGE_TIME_DIFFRENCE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2119
        self.errorInfo = errorText


class NET_DVR_NO_SUPPORT_WITH_PLAYBACK(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2120
        self.errorInfo = errorText


class NET_DVR_CHANNEL_NO_SUPPORT_WITH_SMD(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2121
        self.errorInfo = errorText


class NET_DVR_CHANNEL_NO_SUPPORT_WITH_FD(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2122
        self.errorInfo = errorText


class NET_DVR_ILLEGAL_PHONE_NUMBER(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2123
        self.errorInfo = errorText


class NET_DVR_ILLEGAL_CERITIFICATE_NUMBER(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2124
        self.errorInfo = errorText


class NET_DVR_ERR_CHANNEL_RESOLUTION_NO_SUPPORT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2125
        self.errorInfo = errorText


class NET_DVR_ERR_CHANNEL_COMPRESSION_NO_SUPPORT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2126
        self.errorInfo = errorText


class NET_DVR_ERR_CLUSTER_DEVICE_TOO_LESS(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2127
        self.errorInfo = errorText


class NET_DVR_ERR_CLUSTER_DEL_DEVICE_CM_PLAYLOAD(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2128
        self.errorInfo = errorText


class NET_DVR_ERR_CLUSTER_DEVNUM_OVER_UPPER_LIMIT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2129
        self.errorInfo = errorText


class NET_DVR_ERR_CLUSTER_DEVICE_TYPE_INCONFORMITY(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2130
        self.errorInfo = errorText


class NET_DVR_ERR_CLUSTER_DEVICE_VERSION_INCONFORMITY(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2131
        self.errorInfo = errorText


class NET_DVR_ERR_CLUSTER_IP_CONFLICT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2132
        self.errorInfo = errorText


class NET_DVR_ERR_CLUSTER_IP_INVALID(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2133
        self.errorInfo = errorText


class NET_DVR_ERR_CLUSTER_PORT_CONFLICT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2134
        self.errorInfo = errorText


class NET_DVR_ERR_CLUSTER_PORT_INVALID(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2135
        self.errorInfo = errorText


class NET_DVR_ERR_CLUSTER_USERNAEM_OR_PASSWORD_INVALID(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2136
        self.errorInfo = errorText


class NET_DVR_ERR_CLUSTER_DEVICE_ALREADY_EXIST(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2137
        self.errorInfo = errorText


class NET_DVR_ERR_CLUSTER_DEVICE_NOT_EXIST(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2138
        self.errorInfo = errorText


class NET_DVR_ERR_CLUSTER_NON_CLUSTER_MODE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2139
        self.errorInfo = errorText


class NET_DVR_ERR_CLUSTER_IP_NOT_SAME_LAN(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2140
        self.errorInfo = errorText


class NET_DVR_ERR_CAPTURE_PACKAGE_FAILED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2141
        self.errorInfo = errorText


class NET_DVR_ERR_CAPTURE_PACKAGE_PROCESSING(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2142
        self.errorInfo = errorText


class NET_DVR_ERR_SAFETY_HELMET_NO_RESOURCE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2143
        self.errorInfo = errorText


class NET_DVR_NO_SUPPORT_WITH_ABSTRACT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2144
        self.errorInfo = errorText


class NET_DVR_ERR_TAPE_LIB_NEED_STOP_ARCHIVE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2145
        self.errorInfo = errorText


class NET_DVR_INSUFFICIENT_DEEP_LEARNING_RESOURCES(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2146
        self.errorInfo = errorText


class NET_DVR_ERR_IDENTITY_KEY(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2147
        self.errorInfo = errorText


class NET_DVR_MISSING_IDENTITY_KEY(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2148
        self.errorInfo = errorText


class NET_DVR_NO_SUPPORT_WITH_PERSON_DENSITY_DETECT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2149
        self.errorInfo = errorText


class NET_DVR_IPC_RESOLUTION_OVERFLOW(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2150
        self.errorInfo = errorText


class NET_DVR_IPC_BITRATE_OVERFLOW(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2151
        self.errorInfo = errorText


class NET_DVR_ERR_INVALID_TASKID(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2152
        self.errorInfo = errorText


class NET_DVR_PANEL_MODE_NOT_CONFIG(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2153
        self.errorInfo = errorText


class NET_DVR_NO_HUMAN_ENGINES_RESOURCE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2154
        self.errorInfo = errorText


class NET_DVR_ERR_TASK_NUMBER_OVERFLOW(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2155
        self.errorInfo = errorText


class NET_DVR_ERR_COLLISION_TIME_OVERFLOW(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2156
        self.errorInfo = errorText


class NET_DVR_ERR_CAPTURE_PACKAGE_NO_USB(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2157
        self.errorInfo = errorText


class NET_DVR_ERR_NO_SET_SECURITY_EMAIL(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2158
        self.errorInfo = errorText


class NET_DVR_ERR_EVENT_NOTSUPPORT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2159
        self.errorInfo = errorText


class NET_DVR_ERR_PASSWORD_FORMAT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2160
        self.errorInfo = errorText


class NET_DVR_ACCESS_FRONT_DEVICE_PARAM_FAILURE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2161
        self.errorInfo = errorText


class NET_DVR_ACCESS_FRONT_DEVICE_STREAM_FAILURE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2162
        self.errorInfo = errorText


class NET_DVR_ERR_USERNAME_FORMAT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2163
        self.errorInfo = errorText


class NET_DVR_ERR_UNOPENED_HIGH_RESOLUTION_MODE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2164
        self.errorInfo = errorText


class NET_DVR_ERR_TOO_SMALL_QUATO(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2165
        self.errorInfo = errorText


class NET_DVR_ERR_EMAIL_FORMAT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2166
        self.errorInfo = errorText


class NET_DVR_ERR_SECURITY_CODE_FORMAT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2167
        self.errorInfo = errorText


class NET_DVR_PD_SPACE_TOO_SMALL(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2168
        self.errorInfo = errorText


class NET_DVR_PD_NUM_TOO_BIG(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2169
        self.errorInfo = errorText


class NET_DVR_ERR_USB_IS_FULL(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2170
        self.errorInfo = errorText


class NET_DVR_EXCEED_MAX_SMD_TYPE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2171
        self.errorInfo = errorText


class NET_DVR_CHANNEL_NO_SUPPORT_WITH_BEHAVIOR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2172
        self.errorInfo = errorText


class NET_DVR_NO_BEHAVIOR_ENGINES_RESOURCE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2173
        self.errorInfo = errorText


class NET_DVR_NO_RETENTION_ENGINES_RESOURCE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2174
        self.errorInfo = errorText


class NET_DVR_NO_LEAVE_POSITION_ENGINES_RESOURCE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2175
        self.errorInfo = errorText


class NET_DVR_NO_PEOPLE_NUM_CHANGE_ENGINES_RESOURCE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2176
        self.errorInfo = errorText


class NET_DVR_PANEL_MODE_NUM_OVER_LIMIT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2177
        self.errorInfo = errorText


class NET_DVR_SURROUND_MODE_NUM_OVER_LIMIT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2178
        self.errorInfo = errorText


class NET_DVR_FACE_MODE_NUM_OVER_LIMIT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2179
        self.errorInfo = errorText


class NET_DVR_SAFETYCABIN_MODE_NUM_OVER_LIMIT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2180
        self.errorInfo = errorText


class NET_DVR_DETECT_REGION_RANGE_INVALID(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2181
        self.errorInfo = errorText


class NET_DVR_CHANNEL_CAPTURE_PICTURE_FAILURE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2182
        self.errorInfo = errorText


class NET_DVR_VCACHAN_IS_NORESOURCE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2183
        self.errorInfo = errorText


class NET_DVR_IPC_NUM_REACHES_LIMIT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2184
        self.errorInfo = errorText


class NET_DVR_IOT_NUM_REACHES_LIMIT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2185
        self.errorInfo = errorText


class NET_DVR_IOT_CHANNEL_DEVICE_EXIST(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2186
        self.errorInfo = errorText


class NET_DVR_IOT_CHANNEL_DEVICE_NOT_EXIST(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2187
        self.errorInfo = errorText


class NET_DVR_INVALID_IOT_PROTOCOL_TYPE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2188
        self.errorInfo = errorText


class NET_DVR_INVALID_EZVIZ_SECRET_KEY(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2189
        self.errorInfo = errorText


class NET_DVR_DUPLICATE_IOT_DEVICE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2190
        self.errorInfo = errorText


class NET_DVR_SADP_MODIFY_FALIURE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2191
        self.errorInfo = errorText


class NET_DVR_IPC_NETWORK_ABNORMAL(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2192
        self.errorInfo = errorText


class NET_DVR_IPC_PASSWORD_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2193
        self.errorInfo = errorText


class NET_DVR_ERROR_IPC_TYPE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2194
        self.errorInfo = errorText


class NET_DVR_ERROR_IPC_LIST_NOT_EMPTY(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2195
        self.errorInfo = errorText


class NET_DVR_ERROR_IPC_LIST_NOT_MATCH_PAIRING(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2196
        self.errorInfo = errorText


class NET_DVR_ERROR_IPC_BAD_LANGUAGE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2197
        self.errorInfo = errorText


class NET_DVR_ERROR_IPC_IS_LOCKING(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2198
        self.errorInfo = errorText


class NET_DVR_ERROR_IPC_NOT_ACTIVATED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2199
        self.errorInfo = errorText


class NET_DVR_FIELD_CODING_NOT_SUPPORT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2200
        self.errorInfo = errorText


class NET_DVR_ERROR_H323_NOT_SUPPORT_H265(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2201
        self.errorInfo = errorText


class NET_DVR_ERROR_EXPOSURE_TIME_TOO_BIG_IN_MODE_P(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2202
        self.errorInfo = errorText


class NET_DVR_ERROR_EXPOSURE_TIME_TOO_BIG_IN_MODE_N(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2203
        self.errorInfo = errorText


class NET_DVR_ERROR_PING_PROCESSING(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2204
        self.errorInfo = errorText


class NET_DVR_ERROR_PING_NOT_START(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2205
        self.errorInfo = errorText


class NET_DVR_ERROR_NEED_DOUBLE_VERIFICATION(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2206
        self.errorInfo = errorText


class NET_DVR_NO_DOUBLE_VERIFICATION_USER(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2207
        self.errorInfo = errorText


class NET_DVR_CHANNEL_OFFLINE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2208
        self.errorInfo = errorText


class NET_DVR_TIMESPAN_NUM_OVER_LIMIT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2209
        self.errorInfo = errorText


class NET_DVR_CHANNEL_NUM_OVER_LIMIT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2210
        self.errorInfo = errorText


class NET_DVR_NO_SEARCH_ID_RESOURCE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2211
        self.errorInfo = errorText


class NET_DVR_ERROR_ONEKEY_EXPORT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2212
        self.errorInfo = errorText


class NET_DVR_NO_CITY_MANAGEMENT_ENGINES_RESOURCE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2213
        self.errorInfo = errorText


class NET_DVR_NO_SITUATION_ANALYSIS_ENGINES_RESOURCE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2214
        self.errorInfo = errorText


class NET_DVR_INTELLIGENT_ANALYSIS_IPC_CANNT_DELETE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2215
        self.errorInfo = errorText


class NET_DVR_NOSUPPORT_RESET_PASSWORD(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2216
        self.errorInfo = errorText


class NET_DVR_ERROR_IPC_NEED_ON_LAN(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2217
        self.errorInfo = errorText


class NET_DVR_CHANNEL_NO_SUPPORT_WITH_SAFETY_HELMET(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2218
        self.errorInfo = errorText


class NET_DVR_ERROR_GET_RESETPASSWORDTYPE_IS_ABNORMAL(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2219
        self.errorInfo = errorText


class NET_DVR_ERROR_IPC_NOSUPPORT_RESET_PASSWORD(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2220
        self.errorInfo = errorText


class NET_DVR_ERROR_IP_IS_NOT_ONLY_ONE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2221
        self.errorInfo = errorText


class NET_DVR_NO_SUPPORT_WITH_SMD_OR_SCD(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2222
        self.errorInfo = errorText


class NET_DVR_NO_SUPPORT_WITH_FD(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2223
        self.errorInfo = errorText


class NET_DVR_NO_FD_ENGINES_RESOURCE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2224
        self.errorInfo = errorText


class NET_DVR_ERROR_ONEKEY_REMOVE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2225
        self.errorInfo = errorText


class NET_DVR_FACE_PIP_BACKGROUND_CHANNEL_OVERFLOW(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2226
        self.errorInfo = errorText


class NET_DVR_MICIN_CHANNEL_OCCUPIED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2227
        self.errorInfo = errorText


class NET_DVR_IPC_CHANNEL_IS_IN_PIP(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2228
        self.errorInfo = errorText


class NET_DVR_CHANNEL_NO_SUPPORT_WITH_FACE_CONTRAST(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2229
        self.errorInfo = errorText


class NET_DVR_INVALID_RECHARGE_CARD(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2230
        self.errorInfo = errorText


class NET_DVR_CLOUD_PLATFORM_SERVER_EXCEPTION(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2231
        self.errorInfo = errorText


class NET_DVR_OPERATION_FAILURE_WITHOUT_LOGIN(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2232
        self.errorInfo = errorText


class NET_DVR_INVALID_ASSOCIATED_SERIAL_NUMBER(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2233
        self.errorInfo = errorText


class NET_DVR_CLOUD_PLATFORM_ACCOUNT_NOT_EXIST(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2234
        self.errorInfo = errorText


class NET_DVR_DEVICE_SERIAL_NUMBER_REGISTERED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2235
        self.errorInfo = errorText


class NET_DVR_CONFERENCE_ROOM_NOT_EXIST(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2236
        self.errorInfo = errorText


class NET_DVR_NEED_DISABLED_ANALOG_CHANNEL(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2237
        self.errorInfo = errorText


class NET_DVR_STUDENT_ROLL_CALL_FAILURE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2238
        self.errorInfo = errorText


class NET_DVR_SUB_DEVICE_NOT_ENABLE_INDIVIDUAL_BEHAVIOR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2239
        self.errorInfo = errorText


class NET_DVR_SUB_DEVICE_CHANNEL_CONTROL_FAILED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2240
        self.errorInfo = errorText


class NET_DVR_DEVICE_NOT_IN_CONFERENCE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2241
        self.errorInfo = errorText


class NET_DVR_ALREADY_EXIST_CONFERENCE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2242
        self.errorInfo = errorText


class NET_DVR_NO_SUPPORT_WITH_VIDEO_CONFERENCE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2243
        self.errorInfo = errorText


class NET_DVR_START_INTERACTION_FAILURE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2244
        self.errorInfo = errorText


class NET_DVR_ASK_QUESTION_STARTED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2245
        self.errorInfo = errorText


class NET_DVR_ASK_QUESTION_CLOSED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2246
        self.errorInfo = errorText


class NET_DVR_UNABLE_OPERATE_BY_HOST(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2247
        self.errorInfo = errorText


class NET_DVR_REPEATED_ASK_QUESTION(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2248
        self.errorInfo = errorText


class NET_DVR_SWITCH_TIMEDIFF_LESS_LIMIT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2249
        self.errorInfo = errorText


class NET_DVR_CHANNEL_DEVICE_EXIST(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2250
        self.errorInfo = errorText


class NET_DVR_CHANNEL_DEVICE_NOT_EXIST(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2251
        self.errorInfo = errorText


class NET_DVR_ERROR_ADJUSTING_RESOLUTION(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2252
        self.errorInfo = errorText


class NET_DVR_SSD_FILE_SYSTEM_IS_UPGRADING(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2253
        self.errorInfo = errorText


class NET_DVR_SSD_FILE_SYSTEM_IS_FORMAT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2254
        self.errorInfo = errorText


class NET_DVR_CHANNEL_IS_CONNECTING(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2255
        self.errorInfo = errorText


class NET_DVR_CHANNEL_STREAM_TYPE_NOT_SUPPORT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2257
        self.errorInfo = errorText


class NET_DVR_CHANNEL_USERNAME_NOT_EXIST(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2258
        self.errorInfo = errorText


class NET_DVR_CHANNEL_ACCESS_PARAM_FAILURE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2259
        self.errorInfo = errorText


class NET_DVR_CHANNEL_GET_STREAM_FAILURE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2260
        self.errorInfo = errorText


class NET_DVR_CHANNEL_RISK_PASSWORD(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2261
        self.errorInfo = errorText


class NET_DVR_NO_SUPPORT_DELETE_STRANGER_LIB(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2262
        self.errorInfo = errorText


class NET_DVR_NO_SUPPORT_CREATE_STRANGER_LIB(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2263
        self.errorInfo = errorText


class NET_DVR_NETWORK_PORT_CONFLICT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2264
        self.errorInfo = errorText


class NET_DVR_TRANSCODE_NO_RESOURCES(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2265
        self.errorInfo = errorText


class NET_DVR_SSD_FILE_SYSTEM_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2266
        self.errorInfo = errorText


class NET_DVR_INSUFFICIENT_SSD__FOR_FPD(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2267
        self.errorInfo = errorText


class NET_DVR_ASSOCIATED_FACELIB_OVER_LIMIT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2268
        self.errorInfo = errorText


class NET_DVR_NEED_DELETE_DIGITAL_CHANNEL(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2269
        self.errorInfo = errorText


class NET_DVR_ERR_FALL_DOWN_RULENUM_LIMIT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2270
        self.errorInfo = errorText


class NET_DVR_ERR_VIOLENT_MOTION_RULENUM_LIMIT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2271
        self.errorInfo = errorText


class NET_DVR_UPGRADE_ENGINE_VERSION_MISMATCH(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2272
        self.errorInfo = errorText


class NET_DVR_ERR_NOTSUPPORT_DEICING(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 3001
        self.errorInfo = errorText


class NET_DVR_ERR_THERMENABLE_CLOSE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 3002
        self.errorInfo = errorText


class NET_DVR_ERR_NOTMEET_DEICING(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 3003
        self.errorInfo = errorText


class NET_DVR_ERR_PANORAMIC_LIMIT_OPERATED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 3004
        self.errorInfo = errorText


class NET_DVR_ERR_SMARTH264_ROI_OPERATED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 3005
        self.errorInfo = errorText


class NET_DVR_ERR_RULENUM_LIMIT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 3006
        self.errorInfo = errorText


class NET_DVR_ERR_LASER_DEICING_OPERATED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 3007
        self.errorInfo = errorText


class NET_DVR_ERR_OFFDIGITALZOOM_OR_MINZOOMLIMIT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 3008
        self.errorInfo = errorText


class NET_DVR_ERR_FIREWAITING(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 3009
        self.errorInfo = errorText


class NET_DVR_SYNCHRONIZEFOV_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 3010
        self.errorInfo = errorText


class NET_DVR_CERTIFICATE_VALIDATION_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 3011
        self.errorInfo = errorText


class NET_DVR_CERTIFICATES_NUM_EXCEED_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 3012
        self.errorInfo = errorText


class NET_DVR_RULE_SHIELDMASK_CONFLICT_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 3013
        self.errorInfo = errorText


class NET_DVR_MOTOR_PREHEATING_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 3014
        self.errorInfo = errorText


class NET_DVR_PT_DEICING_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 3015
        self.errorInfo = errorText


class NET_DVR_ERR_NO_SAFETY_HELMET_REGION(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 3501
        self.errorInfo = errorText


class NET_DVR_ERR_UNCLOSED_SAFETY_HELMET(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 3502
        self.errorInfo = errorText


class NET_DVR_ERR_MUX_RECV_STATE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 3503
        self.errorInfo = errorText


class NET_DVR_UPLOAD_HBDLIBID_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 3504
        self.errorInfo = errorText


class NET_DVR_NOTSUPPORT_SMALLER_RATIOS(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 3505
        self.errorInfo = errorText


class NET_ERR_ACCOUNT_NOT_ACTIVED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 3506
        self.errorInfo = errorText


class NET_ERR_NPQ_BASE_INDEX(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8000
        self.errorInfo = errorText


class NET_ERR_NPQ_PARAM(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8001
        self.errorInfo = errorText


class NET_ERR_NPQ_SYSTEM(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8002
        self.errorInfo = errorText


class NET_ERR_NPQ_GENRAL(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8003
        self.errorInfo = errorText


class NET_ERR_NPQ_PRECONDITION(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8004
        self.errorInfo = errorText


class NET_ERR_NPQ_NOTSUPPORT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8005
        self.errorInfo = errorText


class NET_ERR_NPQ_NOTCALLBACK(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8100
        self.errorInfo = errorText


class NET_ERR_NPQ_LOADLIB(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8101
        self.errorInfo = errorText


class NET_ERR_NPQ_STEAM_CLOSE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8104
        self.errorInfo = errorText


class NET_ERR_NPQ_MAX_LINK(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8110
        self.errorInfo = errorText


class NET_ERR_NPQ_STREAM_CFG(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8111
        self.errorInfo = errorText


class NET_ERR_NPQ_PLAYBACK_OVERSPEED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8112
        self.errorInfo = errorText


class NET_ERR_NPQ_PLAYBACK_BELOWSPEED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8113
        self.errorInfo = errorText


class NET_EZVIZ_P2P_BASE_INDEX(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8300
        self.errorInfo = errorText


class NET_DVR_EZVIZ_P2P_REGISTER_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8301
        self.errorInfo = errorText


class NET_DVR_EZVIZ_P2P_LOGIN_2C_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8302
        self.errorInfo = errorText


class NET_DVR_EZVIZ_P2P_LOGIN_2B_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8303
        self.errorInfo = errorText


class NET_DVR_EZVIZ_P2P_BUILDLINK_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8304
        self.errorInfo = errorText


class NET_DVR_EZVIZ_P2P_PORTMAPPING_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8305
        self.errorInfo = errorText


class NET_DVR_EZVIZ_P2P_COULDNT_RESOLVE_HOST(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8306
        self.errorInfo = errorText


class NET_DVR_EZVIZ_P2P_COULDNT_CONNECT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8307
        self.errorInfo = errorText


class NET_DVR_EZVIZ_P2P_OPERATION_TIMEOUT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8308
        self.errorInfo = errorText


class NET_DVR_EZVIZ_P2P_NOT_INITIALIZED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8309
        self.errorInfo = errorText


class NET_DVR_EZVIZ_P2P_INVALID_ARG(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8310
        self.errorInfo = errorText


class NET_DVR_EZVIZ_P2P_EXCEED_MAX_SERVICE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8311
        self.errorInfo = errorText


class NET_DVR_EZVIZ_P2P_TOKEN_NOT_EXIST(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8312
        self.errorInfo = errorText


class NET_DVR_EZVIZ_P2P_DISCONNECTED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8313
        self.errorInfo = errorText


class NET_DVR_EZVIZ_P2P_RELAY_ADDR_NOT_EXIST(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8314
        self.errorInfo = errorText


class NET_DVR_EZVIZ_P2P_DEV_NOT_ONLINE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8315
        self.errorInfo = errorText


class NET_DVR_EZVIZ_P2P_DEV_CONNECT_EXCEED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8316
        self.errorInfo = errorText


class NET_DVR_EZVIZ_P2P_DEV_CONNECT_FAILED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8317
        self.errorInfo = errorText


class NET_DVR_EZVIZ_P2P_DEV_RECV_TIMEOUT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8318
        self.errorInfo = errorText


class NET_DVR_EZVIZ_P2P_USER_FORCE_STOP(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8319
        self.errorInfo = errorText


class NET_DVR_EZVIZ_P2P_NO_PERMISSION(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8320
        self.errorInfo = errorText


class NET_DVR_EZVIZ_P2P_DEV_PU_NOT_FOUND(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8321
        self.errorInfo = errorText


class NET_DVR_EZVIZ_P2P_DEV_CONN_NOLONGER_AVAIL(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8322
        self.errorInfo = errorText


class NET_DVR_EZVIZ_P2P_DEV_NOT_LISTENING(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8323
        self.errorInfo = errorText


class NET_DVR_EZVIZ_P2P_DEV_TUNNEL_SOCKET_LIMITED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8324
        self.errorInfo = errorText


class NET_DVR_EZVIZ_P2P_FAIL_CREATE_THREAD(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8325
        self.errorInfo = errorText


class NET_DVR_EZVIZ_P2P_FAIL_ALLOC_BUFFERS(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8326
        self.errorInfo = errorText


class NET_DVR_EZVIZ_P2P_FAIL_CREATE_SOCKET(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8327
        self.errorInfo = errorText


class NET_DVR_EZVIZ_P2P_BIND_LOCAL_SERVICE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8328
        self.errorInfo = errorText


class NET_DVR_EZVIZ_P2P_LISTEN_LOCAL_SERVICE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8329
        self.errorInfo = errorText


class NET_DVR_EZVIZ_P2P_SVR_RSP_BAD(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8330
        self.errorInfo = errorText


class NET_DVR_EZVIZ_P2P_SVR_RSP_INVALID(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8331
        self.errorInfo = errorText


class NET_DVR_EZVIZ_P2P_SVR_LOGIN_FAILED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8332
        self.errorInfo = errorText


class NET_DVR_EZVIZ_P2P_SVR_TOKEN_EXPIRED(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8333
        self.errorInfo = errorText


class NET_DVR_EZVIZ_P2P_SVR_DEV_NOT_BELONG_TO_USER(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8334
        self.errorInfo = errorText


class NET_ERR_UPGRADE_PROG_ERR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8501
        self.errorInfo = errorText


class NET_ERR_UPGRADE_NO_DEVICE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8502
        self.errorInfo = errorText


class NET_ERR_UPGRADE_NO_FILE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8503
        self.errorInfo = errorText


class NET_ERR_UPGRADE_DATA_ERROR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8504
        self.errorInfo = errorText


class NET_ERR_UPGRADE_LINK_SERVER_ERR(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8505
        self.errorInfo = errorText


class NET_ERR_UPGRADE_OEMCODE_NOMATCH(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8506
        self.errorInfo = errorText


class NET_ERR_UPGRADE_FLASH_NOENOUGH(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8507
        self.errorInfo = errorText


class NET_ERR_UPGRADE_RAM_NOENOUGH(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8508
        self.errorInfo = errorText


class NET_ERR_UPGRADE_DSPRAM_NOENOUGH(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8509
        self.errorInfo = errorText


class NET_ERR_NOT_SUPPORT_CHECK(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8510
        self.errorInfo = errorText


class NET_ERR_LED_DEVICE_BUSY_CHECK(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8511
        self.errorInfo = errorText


class NET_ERR_DEVICE_MEM_NOT_ENOUGH(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8512
        self.errorInfo = errorText


class NET_ERR_CHECK_PARAM(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8513
        self.errorInfo = errorText


class NET_ERR_RESOLUTION_OVER_LIMIT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8514
        self.errorInfo = errorText


class NET_ERR_NO_CUSTOM_BASE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8515
        self.errorInfo = errorText


class NET_ERR_PRIORITY_LOWER(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8516
        self.errorInfo = errorText


class NET_ERR_SEND_MESSAGE_EXCEPT(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8517
        self.errorInfo = errorText


class NET_ERR_SENDCARD_UPGRADING(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8518
        self.errorInfo = errorText


class NET_ERR_NO_WIRELESS_NETCARD(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8519
        self.errorInfo = errorText


class NET_ERR_LOAD_FS_FAIL(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8520
        self.errorInfo = errorText


class NET_ERR_FLASH_UNSTORAGE_RECCARD(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8521
        self.errorInfo = errorText


class NET_ERR_NOT_SUPPORT_SINGLE_NETWORKCARD_AGGREGA(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8522
        self.errorInfo = errorText


class NET_ERR_DISPLAYRESOLUTION_LESSTHAN_SMALLESTRESOLUTION(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8523
        self.errorInfo = errorText


class NET_ERR_NOT_SUPPORT_LOCAL_SOURCE_DRAG_MORE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8524
        self.errorInfo = errorText


class NET_ERR_CANCEL_CURRENT_LED_AREA(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8525
        self.errorInfo = errorText


class NET_ERR_LED_OUT_ASSOCIATED_AREA(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8526
        self.errorInfo = errorText


class NET_ERR_MAX_VIRTUAL_LED_PICTURE_SIZE(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8527
        self.errorInfo = errorText


class NET_ERR_DEVICE_CTRLED_BY_REMOTER(HKNetSDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8528
        self.errorInfo = errorText


HKNetSDKExceptionDict = {
    0: NET_DVR_NOERROR,
    1: NET_DVR_PASSWORD_ERROR,
    2: NET_DVR_NOENOUGHPRI,
    3: NET_DVR_NOINIT,
    4: NET_DVR_CHANNEL_ERROR,
    5: NET_DVR_OVER_MAXLINK,
    6: NET_DVR_VERSIONNOMATCH,
    7: NET_DVR_NETWORK_FAIL_CONNECT,
    8: NET_DVR_NETWORK_SEND_ERROR,
    9: NET_DVR_NETWORK_RECV_ERROR,
    10: NET_DVR_NETWORK_RECV_TIMEOUT,
    11: NET_DVR_NETWORK_ERRORDATA,
    12: NET_DVR_ORDER_ERROR,
    13: NET_DVR_OPERNOPERMIT,
    14: NET_DVR_COMMANDTIMEOUT,
    15: NET_DVR_ERRORSERIALPORT,
    16: NET_DVR_ERRORALARMPORT,
    17: NET_DVR_PARAMETER_ERROR,
    18: NET_DVR_CHAN_EXCEPTION,
    19: NET_DVR_NODISK,
    20: NET_DVR_ERRORDISKNUM,
    21: NET_DVR_DISK_FULL,
    22: NET_DVR_DISK_ERROR,
    23: NET_DVR_NOSUPPORT,
    24: NET_DVR_BUSY,
    25: NET_DVR_MODIFY_FAIL,
    26: NET_DVR_PASSWORD_FORMAT_ERROR,
    27: NET_DVR_DISK_FORMATING,
    28: NET_DVR_DVRNORESOURCE,
    29: NET_DVR_DVROPRATEFAILED,
    30: NET_DVR_OPENHOSTSOUND_FAIL,
    31: NET_DVR_DVRVOICEOPENED,
    32: NET_DVR_TIMEINPUTERROR,
    33: NET_DVR_NOSPECFILE,
    34: NET_DVR_CREATEFILE_ERROR,
    35: NET_DVR_FILEOPENFAIL,
    36: NET_DVR_OPERNOTFINISH,
    37: NET_DVR_GETPLAYTIMEFAIL,
    38: NET_DVR_PLAYFAIL,
    39: NET_DVR_FILEFORMAT_ERROR,
    40: NET_DVR_DIR_ERROR,
    41: NET_DVR_ALLOC_RESOURCE_ERROR,
    42: NET_DVR_AUDIO_MODE_ERROR,
    43: NET_DVR_NOENOUGH_BUF,
    44: NET_DVR_CREATESOCKET_ERROR,
    45: NET_DVR_SETSOCKET_ERROR,
    46: NET_DVR_MAX_NUM,
    47: NET_DVR_USERNOTEXIST,
    48: NET_DVR_WRITEFLASHERROR,
    49: NET_DVR_UPGRADEFAIL,
    50: NET_DVR_CARDHAVEINIT,
    51: NET_DVR_PLAYERFAILED,
    52: NET_DVR_MAX_USERNUM,
    53: NET_DVR_GETLOCALIPANDMACFAIL,
    54: NET_DVR_NOENCODEING,
    55: NET_DVR_IPMISMATCH,
    56: NET_DVR_MACMISMATCH,
    57: NET_DVR_UPGRADELANGMISMATCH,
    58: NET_DVR_MAX_PLAYERPORT,
    59: NET_DVR_NOSPACEBACKUP,
    60: NET_DVR_NODEVICEBACKUP,
    61: NET_DVR_PICTURE_BITS_ERROR,
    62: NET_DVR_PICTURE_DIMENSION_ERROR,
    63: NET_DVR_PICTURE_SIZ_ERROR,
    64: NET_DVR_LOADPLAYERSDKFAILED,
    65: NET_DVR_LOADPLAYERSDKPROC_ERROR,
    66: NET_DVR_LOADDSSDKFAILED,
    67: NET_DVR_LOADDSSDKPROC_ERROR,
    68: NET_DVR_DSSDK_ERROR,
    69: NET_DVR_VOICEMONOPOLIZE,
    70: NET_DVR_JOINMULTICASTFAILED,
    71: NET_DVR_CREATEDIR_ERROR,
    72: NET_DVR_BINDSOCKET_ERROR,
    73: NET_DVR_SOCKETCLOSE_ERROR,
    74: NET_DVR_USERID_ISUSING,
    75: NET_DVR_SOCKETLISTEN_ERROR,
    76: NET_DVR_PROGRAM_EXCEPTION,
    77: NET_DVR_WRITEFILE_FAILED,
    78: NET_DVR_FORMAT_READONLY,
    79: NET_DVR_WITHSAMEUSERNAME,
    80: NET_DVR_DEVICETYPE_ERROR,
    81: NET_DVR_LANGUAGE_ERROR,
    82: NET_DVR_PARAVERSION_ERROR,
    83: NET_DVR_IPCHAN_NOTALIVE,
    84: NET_DVR_RTSP_SDK_ERROR,
    85: NET_DVR_CONVERT_SDK_ERROR,
    86: NET_DVR_IPC_COUNT_OVERFLOW,
    87: NET_DVR_MAX_ADD_NUM,
    88: NET_DVR_PARAMMODE_ERROR,
    89: NET_DVR_CODESPITTER_OFFLINE,
    90: NET_DVR_BACKUP_COPYING,
    91: NET_DVR_CHAN_NOTSUPPORT,
    92: NET_DVR_CALLINEINVALID,
    93: NET_DVR_CALCANCELCONFLICT,
    94: NET_DVR_CALPOINTOUTRANGE,
    95: NET_DVR_FILTERRECTINVALID,
    96: NET_DVR_DDNS_DEVOFFLINE,
    97: NET_DVR_DDNS_INTER_ERROR,
    98: NET_DVR_FUNCTION_NOT_SUPPORT_OS,
    99: NET_DVR_DEC_CHAN_REBIND,
    100: NET_DVR_INTERCOM_SDK_ERROR,
    101: NET_DVR_NO_CURRENT_UPDATEFILE,
    102: NET_DVR_USER_NOT_SUCC_LOGIN,
    103: NET_DVR_USE_LOG_SWITCH_FILE,
    104: NET_DVR_POOL_PORT_EXHAUST,
    105: NET_DVR_PACKET_TYPE_NOT_SUPPORT,
    106: NET_DVR_IPPARA_IPID_ERROR,
    107: NET_DVR_LOAD_HCPREVIEW_SDK_ERROR,
    108: NET_DVR_LOAD_HCVOICETALK_SDK_ERROR,
    109: NET_DVR_LOAD_HCALARM_SDK_ERROR,
    110: NET_DVR_LOAD_HCPLAYBACK_SDK_ERROR,
    111: NET_DVR_LOAD_HCDISPLAY_SDK_ERROR,
    112: NET_DVR_LOAD_HCINDUSTRY_SDK_ERROR,
    113: NET_DVR_LOAD_HCGENERALCFGMGR_SDK_ERROR,
    114: NET_DVR_LOAD_HCCOREDEVCFG_SDK_ERROR,
    115: NET_DVR_LOAD_HCNETUTILS_SDK_ERROR,
    121: NET_DVR_CORE_VER_MISMATCH,
    122: NET_DVR_CORE_VER_MISMATCH_HCPREVIEW,
    123: NET_DVR_CORE_VER_MISMATCH_HCVOICETALK,
    124: NET_DVR_CORE_VER_MISMATCH_HCALARM,
    125: NET_DVR_CORE_VER_MISMATCH_HCPLAYBACK,
    126: NET_DVR_CORE_VER_MISMATCH_HCDISPLAY,
    127: NET_DVR_CORE_VER_MISMATCH_HCINDUSTRY,
    128: NET_DVR_CORE_VER_MISMATCH_HCGENERALCFGMGR,
    136: NET_DVR_COM_VER_MISMATCH_HCPREVIEW,
    137: NET_DVR_COM_VER_MISMATCH_HCVOICETALK,
    138: NET_DVR_COM_VER_MISMATCH_HCALARM,
    139: NET_DVR_COM_VER_MISMATCH_HCPLAYBACK,
    140: NET_DVR_COM_VER_MISMATCH_HCDISPLAY,
    141: NET_DVR_COM_VER_MISMATCH_HCINDUSTRY,
    142: NET_DVR_COM_VER_MISMATCH_HCGENERALCFGMGR,
    145: NET_ERR_CONFIG_FILE_IMPORT_FAILED,
    146: NET_ERR_CONFIG_FILE_EXPORT_FAILED,
    147: NET_DVR_CERTIFICATE_FILE_ERROR,
    148: NET_DVR_LOAD_SSL_LIB_ERROR,
    149: NET_DVR_SSL_VERSION_NOT_MATCH,
    150: NET_DVR_ALIAS_DUPLICATE,
    151: NET_DVR_INVALID_COMMUNICATION,
    152: NET_DVR_USERNAME_NOT_EXIST,
    153: NET_DVR_USER_LOCKED,
    154: NET_DVR_INVALID_USERID,
    155: NET_DVR_LOW_LOGIN_VERSION,
    156: NET_DVR_LOAD_LIBEAY32_DLL_ERROR,
    157: NET_DVR_LOAD_SSLEAY32_DLL_ERROR,
    158: NET_ERR_LOAD_LIBICONV,
    159: NET_ERR_SSL_CONNECT_FAILED,
    160: NET_ERR_MCAST_ADDRESS_ERROR,
    161: NET_ERR_LOAD_ZLIB,
    162: NET_ERR_OPENSSL_NO_INIT,
    164: NET_DVR_SERVER_NOT_EXIST,
    165: NET_DVR_TEST_SERVER_FAIL_CONNECT,
    166: NET_DVR_NAS_SERVER_INVALID_DIR,
    167: NET_DVR_NAS_SERVER_NOENOUGH_PRI,
    168: NET_DVR_EMAIL_SERVER_NOT_CONFIG_DNS,
    169: NET_DVR_EMAIL_SERVER_NOT_CONFIG_GATEWAY,
    170: NET_DVR_TEST_SERVER_PASSWORD_ERROR,
    171: NET_DVR_EMAIL_SERVER_CONNECT_EXCEPTION_WITH_SMTP,
    172: NET_DVR_FTP_SERVER_FAIL_CREATE_DIR,
    173: NET_DVR_FTP_SERVER_NO_WRITE_PIR,
    174: NET_DVR_IP_CONFLICT,
    175: NET_DVR_INSUFFICIENT_STORAGEPOOL_SPACE,
    176: NET_DVR_STORAGEPOOL_INVALID,
    177: NET_DVR_EFFECTIVENESS_REBOOT,
    178: NET_ERR_ANR_ARMING_EXIST,
    179: NET_ERR_UPLOADLINK_EXIST,
    180: NET_ERR_INCORRECT_FILE_FORMAT,
    181: NET_ERR_INCORRECT_FILE_CONTENT,
    182: NET_ERR_MAX_HRUDP_LINK,
    183: NET_SDK_ERR_ACCESSKEY_SECRETKEY,
    184: NET_SDK_ERR_CREATE_PORT_MULTIPLEX,
    185: NET_DVR_NONBLOCKING_CAPTURE_NOTSUPPORT,
    186: NET_SDK_ERR_FUNCTION_INVALID,
    187: NET_SDK_ERR_MAX_PORT_MULTIPLEX,
    188: NET_DVR_INVALID_LINK,
    189: NET_DVR_ISAPI_NOT_SUPPORT,
    200: NET_DVR_NAME_NOT_ONLY,
    201: NET_DVR_OVER_MAX_ARRAY,
    202: NET_DVR_OVER_MAX_VD,
    203: NET_DVR_VD_SLOT_EXCEED,
    204: NET_DVR_PD_STATUS_INVALID,
    205: NET_DVR_PD_BE_DEDICATE_SPARE,
    206: NET_DVR_PD_NOT_FREE,
    207: NET_DVR_CANNOT_MIG2NEWMODE,
    208: NET_DVR_MIG_PAUSE,
    209: NET_DVR_MIG_CANCEL,
    210: NET_DVR_EXIST_VD,
    211: NET_DVR_TARGET_IN_LD_FUNCTIONAL,
    212: NET_DVR_HD_IS_ASSIGNED_ALREADY,
    213: NET_DVR_INVALID_HD_COUNT,
    214: NET_DVR_LD_IS_FUNCTIONAL,
    215: NET_DVR_BGA_RUNNING,
    216: NET_DVR_LD_NO_ATAPI,
    217: NET_DVR_MIGRATION_NOT_NEED,
    218: NET_DVR_HD_TYPE_MISMATCH,
    219: NET_DVR_NO_LD_IN_DG,
    220: NET_DVR_NO_ROOM_FOR_SPARE,
    221: NET_DVR_SPARE_IS_IN_MULTI_DG,
    222: NET_DVR_DG_HAS_MISSING_PD,
    223: NET_DVR_NAME_EMPTY,
    224: NET_DVR_INPUT_PARAM,
    225: NET_DVR_PD_NOT_AVAILABLE,
    226: NET_DVR_ARRAY_NOT_AVAILABLE,
    227: NET_DVR_PD_COUNT,
    228: NET_DVR_VD_SMALL,
    229: NET_DVR_NO_EXIST,
    230: NET_DVR_NOT_SUPPORT,
    231: NET_DVR_NOT_FUNCTIONAL,
    232: NET_DVR_DEV_NODE_NOT_FOUND,
    233: NET_DVR_SLOT_EXCEED,
    234: NET_DVR_NO_VD_IN_ARRAY,
    235: NET_DVR_VD_SLOT_INVALID,
    236: NET_DVR_PD_NO_ENOUGH_SPACE,
    237: NET_DVR_ARRAY_NONFUNCTION,
    238: NET_DVR_ARRAY_NO_ENOUGH_SPACE,
    239: NET_DVR_STOPPING_SCANNING_ARRAY,
    240: NET_DVR_NOT_SUPPORT_16T,
    241: NET_DVR_ARRAY_FORMATING,
    242: NET_DVR_QUICK_SETUP_PD_COUNT,
    250: NET_DVR_ERROR_DEVICE_NOT_ACTIVATED,
    251: NET_DVR_ERROR_RISK_PASSWORD,
    252: NET_DVR_ERROR_DEVICE_HAS_ACTIVATED,
    300: NET_DVR_ID_ERROR,
    301: NET_DVR_POLYGON_ERROR,
    302: NET_DVR_RULE_PARAM_ERROR,
    303: NET_DVR_RULE_CFG_CONFLICT,
    304: NET_DVR_CALIBRATE_NOT_READY,
    305: NET_DVR_CAMERA_DATA_ERROR,
    306: NET_DVR_CALIBRATE_DATA_UNFIT,
    307: NET_DVR_CALIBRATE_DATA_CONFLICT,
    308: NET_DVR_CALIBRATE_CALC_FAIL,
    309: NET_DVR_CALIBRATE_LINE_OUT_RECT,
    310: NET_DVR_ENTER_RULE_NOT_READY,
    311: NET_DVR_AID_RULE_NO_INCLUDE_LANE,
    312: NET_DVR_LANE_NOT_READY,
    313: NET_DVR_RULE_INCLUDE_TWO_WAY,
    314: NET_DVR_LANE_TPS_RULE_CONFLICT,
    315: NET_DVR_NOT_SUPPORT_EVENT_TYPE,
    316: NET_DVR_LANE_NO_WAY,
    317: NET_DVR_SIZE_FILTER_ERROR,
    318: NET_DVR_LIB_FFL_NO_FACE,
    319: NET_DVR_LIB_FFL_IMG_TOO_SMALL,
    320: NET_DVR_LIB_FD_IMG_NO_FACE,
    321: NET_DVR_LIB_FACE_TOO_SMALL,
    322: NET_DVR_LIB_FACE_QUALITY_TOO_BAD,
    323: NET_DVR_KEY_PARAM_ERR,
    324: NET_DVR_CALIBRATE_DATA_ERR,
    325: NET_DVR_CALIBRATE_DISABLE_FAIL,
    326: NET_DVR_VCA_LIB_FD_SCALE_OUTRANGE,
    327: NET_DVR_LIB_FD_REGION_TOO_LARGE,
    328: NET_DVR_TRIAL_OVERDUE,
    329: NET_DVR_CONFIG_FILE_CONFLICT,
    330: NET_DVR_FR_FPL_FAIL,
    331: NET_DVR_FR_IQA_FAIL,
    332: NET_DVR_FR_FEM_FAIL,
    333: NET_DVR_FPL_DT_CONF_TOO_LOW,
    334: NET_DVR_FPL_CONF_TOO_LOW,
    335: NET_DVR_E_DATA_SIZE,
    336: NET_DVR_FR_MODEL_VERSION_ERR,
    337: NET_DVR_FR_FD_FAIL,
    338: NET_DVR_FA_NORMALIZE_ERR,
    339: NET_DVR_DOG_PUSTREAM_NOT_MATCH,
    340: NET_DVR_DEV_PUSTREAM_NOT_MATCH,
    341: NET_DVR_PUSTREAM_ALREADY_EXISTS,
    342: NET_DVR_SEARCH_CONNECT_FAILED,
    343: NET_DVR_INSUFFICIENT_DISK_SPACE,
    344: NET_DVR_DATABASE_CONNECTION_FAILED,
    345: NET_DVR_DATABASE_ADM_PW_ERROR,
    346: NET_DVR_DECODE_YUV,
    347: NET_DVR_IMAGE_RESOLUTION_ERROR,
    348: NET_DVR_CHAN_WORKMODE_ERROR,
    401: NET_DVR_RTSP_ERROR_NOENOUGHPRI,
    402: NET_DVR_RTSP_ERROR_ALLOC_RESOURCE,
    403: NET_DVR_RTSP_ERROR_PARAMETER,
    404: NET_DVR_RTSP_ERROR_NO_URL,
    406: NET_DVR_RTSP_ERROR_FORCE_STOP,
    407: NET_DVR_RTSP_GETPORTFAILED,
    410: NET_DVR_RTSP_DESCRIBERROR,
    411: NET_DVR_RTSP_DESCRIBESENDTIMEOUT,
    412: NET_DVR_RTSP_DESCRIBESENDERROR,
    413: NET_DVR_RTSP_DESCRIBERECVTIMEOUT,
    414: NET_DVR_RTSP_DESCRIBERECVDATALOST,
    415: NET_DVR_RTSP_DESCRIBERECVERROR,
    416: NET_DVR_RTSP_DESCRIBESERVERERR,
    420: NET_DVR_RTSP_SETUPERROR,
    421: NET_DVR_RTSP_SETUPSENDTIMEOUT,
    422: NET_DVR_RTSP_SETUPSENDERROR,
    423: NET_DVR_RTSP_SETUPRECVTIMEOUT,
    424: NET_DVR_RTSP_SETUPRECVDATALOST,
    425: NET_DVR_RTSP_SETUPRECVERROR,
    426: NET_DVR_RTSP_OVER_MAX_CHAN,
    427: NET_DVR_RTSP_SETUPSERVERERR,
    430: NET_DVR_RTSP_PLAYERROR,
    431: NET_DVR_RTSP_PLAYSENDTIMEOUT,
    432: NET_DVR_RTSP_PLAYSENDERROR,
    433: NET_DVR_RTSP_PLAYRECVTIMEOUT,
    434: NET_DVR_RTSP_PLAYRECVDATALOST,
    435: NET_DVR_RTSP_PLAYRECVERROR,
    436: NET_DVR_RTSP_PLAYSERVERERR,
    440: NET_DVR_RTSP_TEARDOWNERROR,
    441: NET_DVR_RTSP_TEARDOWNSENDTIMEOUT,
    442: NET_DVR_RTSP_TEARDOWNSENDERROR,
    443: NET_DVR_RTSP_TEARDOWNRECVTIMEOUT,
    444: NET_DVR_RTSP_TEARDOWNRECVDATALOST,
    445: NET_DVR_RTSP_TEARDOWNRECVERROR,
    446: NET_DVR_RTSP_TEARDOWNSERVERERR,
    500: NET_PLAYM4_NOERROR,
    501: NET_PLAYM4_PARA_OVER,
    502: NET_PLAYM4_ORDER_ERROR,
    503: NET_PLAYM4_TIMER_ERROR,
    504: NET_PLAYM4_DEC_VIDEO_ERROR,
    505: NET_PLAYM4_DEC_AUDIO_ERROR,
    506: NET_PLAYM4_ALLOC_MEMORY_ERROR,
    507: NET_PLAYM4_OPEN_FILE_ERROR,
    508: NET_PLAYM4_CREATE_OBJ_ERROR,
    509: NET_PLAYM4_CREATE_DDRAW_ERROR,
    510: NET_PLAYM4_CREATE_OFFSCREEN_ERROR,
    511: NET_PLAYM4_BUF_OVER,
    512: NET_PLAYM4_CREATE_SOUND_ERROR,
    513: NET_PLAYM4_SET_VOLUME_ERROR,
    514: NET_PLAYM4_SUPPORT_FILE_ONLY,
    515: NET_PLAYM4_SUPPORT_STREAM_ONLY,
    516: NET_PLAYM4_SYS_NOT_SUPPORT,
    517: NET_PLAYM4_FILEHEADER_UNKNOWN,
    518: NET_PLAYM4_VERSION_INCORRECT,
    519: NET_PALYM4_INIT_DECODER_ERROR,
    520: NET_PLAYM4_CHECK_FILE_ERROR,
    521: NET_PLAYM4_INIT_TIMER_ERROR,
    522: NET_PLAYM4_BLT_ERROR,
    523: NET_PLAYM4_UPDATE_ERROR,
    524: NET_PLAYM4_OPEN_FILE_ERROR_MULTI,
    525: NET_PLAYM4_OPEN_FILE_ERROR_VIDEO,
    526: NET_PLAYM4_JPEG_COMPRESS_ERROR,
    527: NET_PLAYM4_EXTRACT_NOT_SUPPORT,
    528: NET_PLAYM4_EXTRACT_DATA_ERROR,
    581: NET_CONVERT_ERROR_NOT_SUPPORT,
    600: NET_AUDIOINTERCOM_OK,
    601: NET_AUDIOINTECOM_ERR_NOTSUPORT,
    602: NET_AUDIOINTECOM_ERR_ALLOC_MEMERY,
    603: NET_AUDIOINTECOM_ERR_PARAMETER,
    604: NET_AUDIOINTECOM_ERR_CALL_ORDER,
    605: NET_AUDIOINTECOM_ERR_FIND_DEVICE,
    606: NET_AUDIOINTECOM_ERR_OPEN_DEVICE,
    607: NET_AUDIOINTECOM_ERR_NO_CONTEXT,
    608: NET_AUDIOINTECOM_ERR_NO_WAVFILE,
    609: NET_AUDIOINTECOM_ERR_INVALID_TYPE,
    610: NET_AUDIOINTECOM_ERR_ENCODE_FAIL,
    611: NET_AUDIOINTECOM_ERR_DECODE_FAIL,
    612: NET_AUDIOINTECOM_ERR_NO_PLAYBACK,
    613: NET_AUDIOINTECOM_ERR_DENOISE_FAIL,
    619: NET_AUDIOINTECOM_ERR_UNKOWN,
    700: NET_QOS_OK,
    699: NET_QOS_ERROR,
    698: NET_QOS_ERR_INVALID_ARGUMENTS,
    697: NET_QOS_ERR_SESSION_NOT_FOUND,
    696: NET_QOS_ERR_LIB_NOT_INITIALIZED,
    695: NET_QOS_ERR_OUTOFMEM,
    690: NET_QOS_ERR_PACKET_UNKNOW,
    689: NET_QOS_ERR_PACKET_VERSION,
    688: NET_QOS_ERR_PACKET_LENGTH,
    687: NET_QOS_ERR_PACKET_TOO_BIG,
    680: NET_QOS_ERR_SCHEDPARAMS_INVALID_BANDWIDTH,
    679: NET_QOS_ERR_SCHEDPARAMS_BAD_FRACTION,
    678: NET_QOS_ERR_SCHEDPARAMS_BAD_MINIMUM_INTERVAL,
    711: NET_ERROR_TRUNK_LINE,
    712: NET_ERROR_MIXED_JOINT,
    713: NET_ERROR_DISPLAY_SWITCH,
    714: NET_ERROR_USED_BY_BIG_SCREEN,
    715: NET_ERROR_USE_OTHER_DEC_RESOURCE,
    716: NET_ERROR_DISP_MODE_SWITCH,
    717: NET_ERROR_SCENE_USING,
    718: NET_ERR_NO_ENOUGH_DEC_RESOURCE,
    719: NET_ERR_NO_ENOUGH_FREE_SHOW_RESOURCE,
    720: NET_ERR_NO_ENOUGH_VIDEO_MEMORY,
    721: NET_ERR_MAX_VIDEO_NUM,
    722: NET_ERR_WIN_COVER_FREE_SHOW_AND_NORMAL,
    723: NET_ERR_FREE_SHOW_WIN_SPLIT,
    724: NET_ERR_INAPPROPRIATE_WIN_FREE_SHOW,
    725: NET_DVR_TRANSPARENT_WIN_NOT_SUPPORT_SPLIT,
    726: NET_DVR_SPLIT_WIN_NOT_SUPPORT_TRANSPARENT,
    727: NET_ERR_MAX_LOGO_NUM,
    728: NET_ERR_MAX_WIN_LOOP_NUM,
    729: NET_ERR_VIRTUAL_LED_VERTICAL_CROSS,
    730: NET_ERR_MAX_VIRTUAL_LED_HEIGHT,
    731: NET_ERR_VIRTUAL_LED_ILLEGAL_CHARACTER,
    732: NET_ERR_BASEMAP_NOT_EXIST,
    733: NET_ERR_LED_NOT_SUPPORT_VIRTUAL_LED,
    734: NET_ERR_LED_RESOLUTION_NOT_SUPPORT,
    735: NET_ERR_PLAN_OVERDUE,
    736: NET_ERR_PROCESSER_MAX_SCREEN_BLK,
    737: NET_ERR_WND_SIZE_TOO_SMALL,
    738: NET_ERR_WND_SPLIT_NOT_SUPPORT_ROAM,
    739: NET_ERR_OUTPUT_ONE_BOARD_ONE_WALL,
    740: NET_ERR_WND_CANNOT_LCD_AND_LED_OUTPUT,
    741: NET_ERR_MAX_OSD_NUM,
    751: NET_SDK_CANCEL_WND_TOPKEEP_ATTR_FIRST,
    752: NET_SDK_ERR_LED_SCREEN_CHECKING,
    753: NET_SDK_ERR_NOT_SUPPORT_SINGLE_RESOLUTION,
    754: NET_SDK_ERR_LED_RESOLUTION_MISMATCHED,
    755: NET_SDK_ERR_MAX_VIRTUAL_LED_WIDTH,
    756: NET_SDK_ERR_MAX_VIRTUAL_LED_IN_SCREEN,
    757: NET_SDK_ERR_MAX_VIRTUAL_LED_IN_WALL,
    758: NET_SDK_ERR_VIRTUAL_LED_OVERLAP,
    759: NET_SDK_ERR_VIRTUAL_LED_TYPE,
    760: NET_SDK_ERR_VIRTUAL_LED_COLOUR,
    761: NET_SDK_ERR_VIRTUAL_LED_MOVE_DIRECTION,
    762: NET_SDK_ERR_VIRTUAL_LED_MOVE_MODE,
    763: NET_SDK_ERR_VIRTUAL_LED_MOVE_SPEED,
    764: NET_SDK_ERR_VIRTUAL_LED_DISP_MODE,
    765: NET_SDK_ERR_VIRTUAL_LED_NO,
    766: NET_SDK_ERR_VIRTUAL_LED_PARA,
    767: NET_SDK_ERR_BASEMAP_POSITION,
    768: NET_SDK_ERR_BASEMAP_PICTURE_LEN,
    769: NET_SDK_ERR_BASEMAP_PICTURE_RESOLUTION,
    770: NET_SDK_ERR_BASEMAP_PICTURE_FORMAT,
    771: NET_SDK_ERR_MAX_VIRTUAL_LED_NUM,
    772: NET_SDK_ERR_MAX_TIME_VIRTUAL_LED_IN_WALL,
    780: NET_ERR_TERMINAL_BUSY,
    790: NET_ERR_DATA_RETURNED_ILLEGAL,
    791: NET_DVR_FUNCTION_RESOURCE_USAGE_ERROR,
    792: NET_DVR_ERR_IMPORT_EMPTY_FILE,
    793: NET_DVR_ERR_IMPORT_TOO_LARGE_FILE,
    794: NET_DVR_ERR_BAD_IPV4_ADDRESS,
    795: NET_DVR_ERR_BAD_NET_MASK,
    796: NET_DVR_ERR_INVALID_NET_GATE_ADDRESS,
    797: NET_DVR_ERR_BAD_DNS,
    798: NET_DVR_ERR_ILLEGAL_PASSWORD,
    800: NET_DVR_DEV_NET_OVERFLOW,
    801: NET_DVR_STATUS_RECORDFILE_WRITING_NOT_LOCK,
    802: NET_DVR_STATUS_CANT_FORMAT_LITTLE_DISK,
    803: NET_SDK_ERR_REMOTE_DISCONNECT,
    804: NET_SDK_ERR_RD_ADD_RD,
    805: NET_SDK_ERR_BACKUP_DISK_EXCEPT,
    806: NET_SDK_ERR_RD_LIMIT,
    807: NET_SDK_ERR_ADDED_RD_IS_WD,
    808: NET_SDK_ERR_ADD_ORDER_WRONG,
    809: NET_SDK_ERR_WD_ADD_WD,
    810: NET_SDK_ERR_WD_SERVICE_EXCETP,
    811: NET_SDK_ERR_RD_SERVICE_EXCETP,
    812: NET_SDK_ERR_ADDED_WD_IS_RD,
    813: NET_SDK_ERR_PERFORMANCE_LIMIT,
    814: NET_SDK_ERR_ADDED_DEVICE_EXIST,
    815: NET_SDK_ERR_INQUEST_RESUMING,
    816: NET_SDK_ERR_RECORD_BACKUPING,
    817: NET_SDK_ERR_DISK_PLAYING,
    818: NET_SDK_ERR_INQUEST_STARTED,
    819: NET_SDK_ERR_LOCAL_OPERATING,
    820: NET_SDK_ERR_INQUEST_NOT_START,
    821: NET_SDK_ERR_CHAN_AUDIO_BIND,
    822: NET_DVR_N_PLUS_ONE_MODE,
    823: NET_DVR_CLOUD_STORAGE_OPENED,
    824: NET_DVR_ERR_OPER_NOT_ALLOWED,
    825: NET_DVR_ERR_NEED_RELOCATE,
    830: NET_SDK_ERR_IR_PORT_ERROR,
    831: NET_SDK_ERR_IR_CMD_ERROR,
    832: NET_SDK_ERR_NOT_INQUESTING,
    833: NET_SDK_ERR_INQUEST_NOT_PAUSED,
    834: NET_DVR_CHECK_PASSWORD_MISTAKE_ERROR,
    835: NET_DVR_CHECK_PASSWORD_NULL_ERROR,
    836: NET_DVR_UNABLE_CALIB_ERROR,
    837: NET_DVR_PLEASE_CALIB_ERROR,
    838: NET_DVR_ERR_PANORAMIC_CAL_EMPTY,
    839: NET_DVR_ERR_CALIB_FAIL_PLEASEAGAIN,
    840: NET_DVR_ERR_DETECTION_LINE,
    841: NET_DVR_ERR_TURN_OFF_IMAGE_PARA,
    843: NET_DVR_EXCEED_FACE_IMAGES_ERROR,
    844: NET_DVR_ANALYSIS_FACE_IMAGES_ERROR,
    845: NET_ERR_ALARM_INPUT_OCCUPIED,
    846: NET_DVR_FACELIB_DATABASE_ERROR,
    847: NET_DVR_FACELIB_DATA_ERROR,
    848: NET_DVR_FACE_DATA_ID_ERROR,
    849: NET_DVR_FACELIB_ID_ERROR,
    850: NET_DVR_EXCEED_FACE_LIBARY_ERROR,
    851: NET_DVR_PIC_ANALYSIS_NO_TARGET_ERROR,
    852: NET_DVR_SUBPIC_ANALYSIS_MODELING_ERROR,
    853: NET_DVR_PIC_ANALYSIS_NO_RESOURCE_ERROR,
    854: NET_DVR_ANALYSIS_ENGINES_NO_RESOURCE_ERROR,
    855: NET_DVR_ANALYSIS_ENGINES_USAGE_EXCEED_ERROR,
    856: NET_DVR_EXCEED_HUMANMISINFO_FILTER_ENABLED_ERROR,
    857: NET_DVR_NAME_ERROR,
    858: NET_DVR_NAME_EXIST_ERROR,
    859: NET_DVR_FACELIB_PIC_IMPORTING_ERROR,
    860: NET_DVR_ERR_CALIB_POSITION,
    861: NET_DVR_ERR_DELETE,
    862: NET_DVR_ERR_SCENE_ID,
    863: NET_DVR_ERR_CALIBING,
    864: NET_DVR_PIC_FORMAT_ERROR,
    865: NET_DVR_PIC_RESOLUTION_INVALID_ERROR,
    866: NET_DVR_PIC_SIZE_EXCEED_ERROR,
    867: NET_DVR_PIC_ANALYSIS_TARGRT_NUM_EXCEED_ERROR,
    868: NET_DVR_ANALYSIS_ENGINES_LOADING_ERROR,
    869: NET_DVR_ANALYSIS_ENGINES_ABNORMA_ERROR,
    870: NET_DVR_ANALYSIS_ENGINES_FACELIB_IMPORTING,
    871: NET_DVR_NO_DATA_FOR_MODELING_ERROR,
    872: NET_DVR_FACE_DATA_MODELING_ERROR,
    873: NET_ERR_FACELIBDATA_OVERLIMIT,
    874: NET_DVR_ANALYSIS_ENGINES_ASSOCIATED_CHANNEL,
    875: NET_DVR_ERR_CUSTOMID_LEN,
    876: NET_DVR_ERR_CUSTOMFACELIBID_REPEAT,
    877: NET_DVR_ERR_CUSTOMHUMANID_REPEAT,
    878: NET_DVR_ERR_URL_DOWNLOAD_FAIL,
    879: NET_DVR_ERR_URL_DOWNLOAD_NOTSTART,
    880: NET_DVR_CFG_FILE_SECRETKEY_ERROR,
    881: NET_DVR_WDR_NOTDISABLE_ERROR,
    882: NET_DVR_HLC_NOTDISABLE_ERROR,
    883: NET_DVR_THERMOMETRY_REGION_OVERSTEP_ERROR,
    884: NET_DVR_ERR_MODELING_DEVICEINTERNAL,
    885: NET_DVR_ERR_MODELING_FACE,
    886: NET_DVR_ERR_MODELING_FACEGRADING,
    887: NET_DVR_ERR_MODELING_FACEGFEATURE,
    888: NET_DVR_ERR_MODELING_FACEGANALYZING,
    889: NET_DVR_ERR_STREAM_LIMIT,
    890: NET_DVR_ERR_STREAM_DESCRIPTION,
    891: NET_DVR_ERR_STREAM_DELETE,
    892: NET_DVR_ERR_CUSTOMSTREAM_NAME,
    893: NET_DVR_ERR_CUSTOMSTREAM_NOTEXISTED,
    894: NET_DVR_ERR_TOO_SHORT_CALIBRATING_TIME,
    895: NET_DVR_ERR_AUTO_CALIBRATE_FAILED,
    896: NET_DVR_ERR_VERIFICATION_FAILED,
    897: NET_DVR_NO_TEMP_SENSOR_ERROR,
    898: NET_DVR_PUPIL_DISTANCE_OVERSIZE_ERROR,
    899: NET_DVR_ERR_UNOPENED_FACE_SNAP,
    900: NET_ERR_CUT_INPUTSTREAM_OVERLIMIT,
    901: NET_ERR_WINCHAN_IDX,
    902: NET_ERR_WIN_LAYER,
    903: NET_ERR_WIN_BLK_NUM,
    904: NET_ERR_OUTPUT_RESOLUTION,
    905: NET_ERR_LAYOUT,
    906: NET_ERR_INPUT_RESOLUTION,
    907: NET_ERR_SUBDEVICE_OFFLINE,
    908: NET_ERR_NO_DECODE_CHAN,
    909: NET_ERR_MAX_WINDOW_ABILITY,
    910: NET_ERR_ORDER_ERROR,
    911: NET_ERR_PLAYING_PLAN,
    912: NET_ERR_DECODER_USED,
    913: NET_ERR_OUTPUT_BOARD_DATA_OVERFLOW,
    914: NET_ERR_SAME_USER_NAME,
    915: NET_ERR_INVALID_USER_NAME,
    916: NET_ERR_MATRIX_USING,
    917: NET_ERR_DIFFERENT_CHAN_TYPE,
    918: NET_ERR_INPUT_CHAN_BINDED,
    919: NET_ERR_BINDED_OUTPUT_CHAN_OVERFLOW,
    920: NET_ERR_MAX_SIGNAL_NUM,
    921: NET_ERR_INPUT_CHAN_USING,
    922: NET_ERR_MANAGER_LOGON,
    923: NET_ERR_USERALREADY_LOGON,
    924: NET_ERR_LAYOUT_INIT,
    925: NET_ERR_BASEMAP_SIZE_NOT_MATCH,
    926: NET_ERR_WINDOW_OPERATING,
    927: NET_ERR_SIGNAL_UPLIMIT,
    928: NET_ERR_SIGNAL_MAX_ENLARGE_TIMES,
    929: NET_ERR_ONE_SIGNAL_MULTI_CROSS,
    930: NET_ERR_ULTRA_HD_SIGNAL_MULTI_WIN,
    931: NET_ERR_MAX_VIRTUAL_LED_WIDTH,
    932: NET_ERR_MAX_VIRTUAL_LED_WORD_LEN,
    933: NET_ERR_SINGLE_OUTPUTPARAM_CONFIG,
    934: NET_ERR_MULTI_WIN_BE_COVER,
    935: NET_ERR_WIN_NOT_EXIST,
    936: NET_ERR_WIN_MAX_SIGNALSOURCE,
    937: NET_ERR_MULTI_WIN_MOVE,
    938: NET_ERR_MULTI_WIN_YPBPR_SDI,
    939: NET_ERR_DIFF_TYPE_OUTPUT_MIXUSE,
    940: NET_ERR_SPLIT_WIN_CROSS,
    941: NET_ERR_SPLIT_WIN_NOT_FULL_SCREEN,
    942: NET_ERR_SPLIT_WIN_MANY_WIN,
    943: NET_ERR_WINDOW_SIZE_OVERLIMIT,
    944: NET_ERR_INPUTSTREAM_ALREADY_JOINT,
    945: NET_ERR_JOINT_INPUTSTREAM_OVERLIMIT,
    946: NET_ERR_LED_RESOLUTION,
    947: NET_ERR_JOINT_SCALE_OVERLIMIT,
    948: NET_ERR_INPUTSTREAM_ALREADY_DECODE,
    949: NET_ERR_INPUTSTREAM_NOTSUPPORT_CAPTURE,
    950: NET_ERR_JOINT_NOTSUPPORT_SPLITWIN,
    951: NET_ERR_MAX_WIN_OVERLAP,
    952: NET_ERR_STREAMID_CHAN_BOTH_VALID,
    953: NET_ERR_NO_ZERO_CHAN,
    955: NEED_RECONNECT,
    956: NET_ERR_NO_STREAM_ID,
    957: NET_DVR_TRANS_NOT_START,
    958: NET_ERR_MAXNUM_STREAM_ID,
    959: NET_ERR_WORKMODE_MISMATCH,
    960: NET_ERR_MODE_IS_USING,
    961: NET_ERR_DEV_PROGRESSING,
    962: NET_ERR_PASSIVE_TRANSCODING,
    964: NET_ERR_RING_NOT_CONFIGURE,
    971: NET_ERR_CLOSE_WINDOW_FIRST,
    972: NET_ERR_SPLIT_WINDOW_NUM_NOT_SUPPORT,
    973: NET_ERR_REACH_ONE_SIGNAL_PREVIEW_MAX_LINK,
    974: NET_ERR_ONLY_SPLITWND_SUPPORT_AMPLIFICATION,
    975: NET_DVR_ERR_WINDOW_SIZE_PLACE,
    976: NET_DVR_ERR_RGIONAL_RESTRICTIONS,
    977: NET_ERR_WNDZOOM_NOT_SUPPORT,
    978: NET_ERR_LED_SCREEN_SIZE,
    979: NET_ERR_OPEN_WIN_IN_ERROR_AREA,
    980: NET_ERR_TITLE_WIN_NOT_SUPPORT_MOVE,
    981: NET_ERR_TITLE_WIN_NOT_SUPPORT_COVER,
    982: NET_ERR_TITLE_WIN_NOT_SUPPORT_SPLIT,
    983: NET_DVR_LED_WINDOWS_ALREADY_CLOSED,
    984: NET_DVR_ERR_CLOSE_WINDOWS,
    985: NET_DVR_ERR_MATRIX_LOOP_ABILITY,
    986: NET_DVR_ERR_MATRIX_LOOP_TIME,
    987: NET_DVR_ERR_LINKED_OUT_ABILITY,
    988: NET_ERR_REACH_SCENE_MAX_NUM,
    989: NET_ERR_SCENE_MEM_NOT_ENOUGH,
    990: NET_ERR_RESOLUTION_NOT_SUPPORT_ODD_VOUT,
    991: NET_ERR_RESOLUTION_NOT_SUPPORT_EVEN_VOUT,
    992: NET_DVR_CANCEL_WND_OPENKEEP_ATTR_FIRST,
    993: NET_SDK_LED_MODE_NOT_SUPPORT_SPLIT,
    994: NET_ERR_VOICETALK_ONLY_SUPPORT_ONE_TALK,
    995: NET_ERR_WND_POSITION_ADJUSTED,
    996: NET_SDK_ERR_STARTTIME_CANNOT_LESSTHAN_CURTIME,
    997: NET_SDK_ERR_NEED_ADJUST_PLAN,
    998: NET_ERR_UnitConfig_Failed,
    1000: XML_ABILITY_NOTSUPPORT,
    1001: XML_ANALYZE_NOENOUGH_BUF,
    1002: XML_ANALYZE_FIND_LOCALXML_ERROR,
    1003: XML_ANALYZE_LOAD_LOCALXML_ERROR,
    1004: XML_NANLYZE_DVR_DATA_FORMAT_ERROR,
    1005: XML_ANALYZE_TYPE_ERROR,
    1006: XML_ANALYZE_XML_NODE_ERROR,
    1007: XML_INPUT_PARAM_ERROR,
    1008: NET_DVR_ERR_RETURNED_XML_DATA,
    1051: NET_ERR_LEDAREA_EXIST_WINDOW,
    1052: NET_ERR_AUDIO_EXIST,
    1053: NET_ERR_MATERIAL_NAME_EXIST,
    1054: NET_ERR_MATERIAL_APPROVE_STATE,
    1055: NET_ERR_DATAHD_SIGNAL_FORMAT,
    1056: NET_ERR_SCENE_SWITCHING,
    1057: NER_ERR_DATA_TRANSFER,
    1058: NET_ERR_DATA_RESTORE,
    1059: NET_ERR_CHECK_NOT_ENABLE,
    1060: NET_ERR_AREA_OFFLINE,
    1061: NET_ERR_SCREEN_TYPE,
    1062: NET_ERR_MIN_OPERATE_UNIT,
    1063: NET_ERR_MAINHD_NOT_BACKUP,
    1064: NET_ERR_ONE_BACKUP_HD,
    1065: NET_ERR_CONNECT_SUB_SYSTEM_ABNORMAL,
    1066: NET_ERR_SERIAL_PORT_VEST,
    1067: NET_ERR_BLOCKLIST_FULL,
    1068: NET_ERR_NOT_MATCH_SOURCE,
    1069: NET_ERR_CLOCK_VIRTUAL_LED_FULL,
    1070: NET_ERR_MAX_WIN_SIGNAL_LOOP_NUM,
    1071: NET_ERR_RESOLUTION_NO_MATCH_FRAME,
    1072: NET_ERR_NOT_UPDATE_LOW_VERSION,
    1073: NET_ERR_NO_CUSTOM_TO_UPDATE,
    1074: NET_ERR_CHAN_RESOLUTION_NOT_SUPPORT_SPLIT,
    1075: NET_ERR_HIGH_DEFINITION_NOT_SUPPORT_SPLIT,
    1076: NET_ERR_MIRROR_IMAGE_BY_VIDEO_WALL,
    1077: NET_ERR_MAX_OSD_FONT_SIZE,
    1078: NET_ERR_HIGH_DEFINITION_NOT_SUPPORT_VIDEO_SET,
    1079: NET_ERR_TILE_MODE_NOT_SUPPORT_JOINT,
    1080: NET_ERR_ADD_AUDIO_MATRIX_FAILED,
    1081: NET_ERR_ONE_VIRTUAL_LED_AREA_BIND_ONE_AUDIO_AREA,
    1082: NET_ERR_NAT_NOT_MODIFY_SERVER_NETWORK_PARAM,
    1083: NET_ERR_ORIGINAL_CHECH_DATA_ERROR,
    1084: NET_ERR_INPUT_BOARD_SPLICED_IN_DIFFERENT_NETWORKAREAS,
    1085: NET_ERR_SPLICINGSOURCE_ONWALL_IN_DIFFERENT_NETWORKAREAS,
    1086: NET_ERR_ONWALL_OUTPUTBOARD_MODIFY_NETWORKAREAS,
    1087: NET_ERR_LAN_AND_WAN_CANNOT_SAME_NET_SEGMENT,
    1088: NET_ERR_USERNAME_REPETITIVE,
    1089: NET_ERR_ASSOCIATED_SAMEWALL_IN_DIFFERENT_NETWORKAREAS,
    1090: NET_ERR_BASEMAP_ROAM_IN_LED_AREA,
    1091: NET_ERR_VIRTUAL_LED_NOT_SUPPORT_4K_OUTPUT,
    1092: NET_ERR_BASEMAP_NOT_SUPPORT_4K_OUTPUT,
    1093: NET_ERR_MIN_BLOCK_IN_VIRTUAL_LED_AND_OUTPUT,
    1094: NET_ERR_485FIlE_VERSION_INVALID,
    1095: NET_ERR_485FIlE_CHECK_ERROR,
    1096: NET_ERR_485FIlE_ABNORMAL_SIZE,
    1097: NET_ERR_MODIFY_SUBBOARD_NETCFG_IN_NAT,
    1098: NET_ERR_OSD_CONTENT_WITH_ILLEGAL_CHARACTERS,
    1099: NET_ERR_NON_SLAVE_DEVICE_INSERT_SYNC_LINE,
    1100: NET_ERR_PLT_USERID,
    1101: NET_ERR_TRANS_CHAN_START,
    1102: NET_ERR_DEV_UPGRADING,
    1103: NET_ERR_MISMATCH_UPGRADE_PACK_TYPE,
    1104: NET_ERR_DEV_FORMATTING,
    1105: NET_ERR_MISMATCH_UPGRADE_PACK_VERSION,
    1106: NET_ERR_PT_LOCKED,
    1110: NET_DVR_LOGO_OVERLAY_WITHOUT_UPLOAD_PIC,
    1111: NET_DVR_ERR_ILLEGAL_VERIFICATION_CODE,
    1112: NET_DVR_ERR_LACK_VERIFICATION_CODE,
    1113: NET_DVR_ERR_FORBIDDEN_IP,
    1114: NET_DVR_ERR_UNLOCKPTZ,
    1116: NET_DVR_ERR_COUNTAREA_LARGE,
    1117: NET_DVR_ERR_LABEL_ID_EXCEED,
    1118: NET_DVR_ERR_LABEL_TYPE,
    1119: NET_DVR_ERR_LABEL_FULL,
    1120: NET_DVR_ERR_LABEL_DISABLED,
    1121: NET_DVR_ERR_DOME_PT_TRANS_TO_DOME_XY,
    1122: NET_DVR_ERR_DOME_PT_TRANS_TO_PANORAMA_XY,
    1123: NET_DVR_ERR_PANORAMA_XY_TRANS_TO_DOME_PT,
    1124: NET_DVR_ERR_SCENE_DUR_TIME_LESS_THAN_INTERV_TIME,
    1125: NET_DVR_ERR_HTTP_BKN_EXCEED_ONE,
    1126: NET_DVR_ERR_DELETING_FAILED_TURN_OFF_HTTPS_ESDK_WEBSOCKETS_FIRST,
    1127: NET_DVR_ERR_DELETING_FAILED_TURN_OFF_HTTPS_ESDK_FIRST,
    1128: NET_DVR_ERR_PTZ_OCCUPIED_PRIORITY,
    1129: NET_DVR_ERR_INCORRECT_VIDEOAUDIO_ID,
    1130: NET_DVR_ERR_REPETITIONTIME_OVER_MAXIMUM,
    1131: NET_DVR_ERR_FORMATTING_FAILED,
    1132: NET_DVR_ERR_ENCRYPTED_FORMATTING_FAILED,
    1133: NET_DVR_ERR_WRONG_PASSWORD,
    1134: NET_DVR_ERR_EXPOSURE_SYNC,
    1201: NET_ERR_SEARCHING_MODULE,
    1202: NET_ERR_REGISTERING_MODULE,
    1203: NET_ERR_GETTING_ZONES,
    1204: NET_ERR_GETTING_TRIGGERS,
    1205: NET_ERR_ARMED_STATUS,
    1206: NET_ERR_PROGRAM_MODE_STATUS,
    1207: NET_ERR_WALK_TEST_MODE_STATUS,
    1208: NET_ERR_BYPASS_STATUS,
    1209: NET_ERR_DISABLED_MODULE_STATUS,
    1210: NET_ERR_NOT_SUPPORT_OPERATE_ZONE,
    1211: NET_ERR_NOT_SUPPORT_MOD_MODULE_ADDR,
    1212: NET_ERR_UNREGISTERED_MODULE,
    1213: NET_ERR_PUBLIC_SUBSYSTEM_ASSOCIATE_SELF,
    1214: NET_ERR_EXCEEDS_ASSOCIATE_SUBSYSTEM_NUM,
    1215: NET_ERR_BE_ASSOCIATED_BY_PUBLIC_SUBSYSTEM,
    1216: NET_ERR_ZONE_FAULT_STATUS,
    1217: NET_ERR_SAME_EVENT_TYPE,
    1218: NET_ERR_ZONE_ALARM_STATUS,
    1219: NET_ERR_EXPANSION_BUS_SHORT_CIRCUIT,
    1220: NET_ERR_PWD_CONFLICT,
    1221: NET_ERR_DETECTOR_GISTERED_BY_OTHER_ZONE,
    1222: NET_ERR_DETECTOR_GISTERED_BY_OTHER_PU,
    1223: NET_ERR_DETECTOR_DISCONNECT,
    1224: NET_ERR_CALL_BUSY,
    1225: NET_DVR_ERR_ZONE_TAMPER_STAUS,
    1226: NET_DVR_ERR_WIRELESS_DEV_REGISTER,
    1227: NET_DVR_ERR_WIRELESS_DEV_ADDED,
    1228: NET_DVR_ERR_WIRELESS_DEV_OFFLINE,
    1229: NET_DVR_ERR_WIRELESS_DEV_TAMPER_STATUS,
    1230: NET_DVR_ERR_GPRS_PHONE_CONFLICT,
    1231: NET_ERR_INIT_PASSWORD_NOT_MODIFY,
    1232: NET_ERR_USER_DISABLED,
    1233: NET_ERR_DEVICE_DEBUGGING,
    1300: NET_ERR_GET_ALL_RETURN_OVER,
    1301: NET_ERR_RESOURCE_USING,
    1302: NET_ERR_FILE_SIZE_OVERLIMIT,
    1303: NET_ERR_MATERIAL_NAME,
    1304: NET_ERR_MATERIAL_NAME_LEN,
    1305: NET_ERR_MATERIAL_REMARK,
    1306: NET_ERR_MATERIAL_REMARK_LEN,
    1307: NET_ERR_MATERIAL_SHARE_PROPERTY,
    1308: NET_ERR_UNSUPPORT_MATERIAL_TYPE,
    1309: NET_ERR_MATERIAL_NOT_EXIST,
    1310: NET_ERR_READ_FROM_DISK,
    1311: NET_ERR_WRITE_TO_DISK,
    1312: NET_ERR_WRITE_DATA_BASE,
    1313: NET_ERR_NO_APPROVED_NOT_EXPORT,
    1314: NET_ERR_MATERIAL_EXCEPTION,
    1315: NET_ERR_NO_MISINFO,
    1316: NET_ERR_LAN_NOT_SUP_DHCP_CLIENT_CONFIGURATION,
    1317: NET_ERR_VIDEOWALL_OPTPORT_RESOLUTION_INCONSISTENT,
    1318: NET_ERR_VIDEOWALL_OPTPORT_RESOLUTION_INCONSISTENT_UNBIND_OPTPORT_FIRST,
    1319: NET_ERR_FOUR_K_OUTPUT_RESOLUTION_UNSUPPORT_NINE_TO_SIXTEEN_SPLIT_SCREEN,
    1320: NET_ERR_SIGNAL_SOURCE_UNSUPPORT_CUSTOM_RESOLUTION,
    1321: NET_ERR_DVI_UNSUPPORT_FOURK_OUTPUT_RESOLUTION,
    1322: NET_ERR_BNC_UNSUPPORT_SOURCE_CROPPING,
    1323: NET_ERR_OUTPUT_NOT_SUPPORT_VIDEOWALL_RESOLUTION,
    1351: NET_ERR_MAX_SCREEN_CTRL_NUM,
    1352: NET_ERR_FILE_NOT_EXIST,
    1353: NET_ERR_THUMBNAIL_NOT_EXIST,
    1354: NET_ERR_DEV_OPEN_FILE_FAIL,
    1355: NET_ERR_SERVER_READ_FILE_FAIL,
    1356: NET_ERR_FILE_SIZE,
    1357: NET_ERR_FILE_NAME,
    1358: NET_ERR_BROADCAST_BUSY,
    1400: NET_DVR_ERR_LANENUM_EXCEED,
    1401: NET_DVR_ERR_PRAREA_EXCEED,
    1402: NET_DVR_ERR_LIGHT_PARAM,
    1403: NET_DVR_ERR_LANE_LINE_INVALID,
    1404: NET_DVR_ERR_STOP_LINE_INVALID,
    1405: NET_DVR_ERR_LEFTORRIGHT_LINE_INVALID,
    1406: NET_DVR_ERR_LANE_NO_REPEAT,
    1407: NET_DVR_ERR_PRAREA_INVALID,
    1408: NET_DVR_ERR_LIGHT_NUM_EXCEED,
    1409: NET_DVR_ERR_SUBLIGHT_NUM_INVALID,
    1410: NET_DVR_ERR_LIGHT_AREASIZE_INVALID,
    1411: NET_DVR_ERR_LIGHT_COLOR_INVALID,
    1412: NET_DVR_ERR_LIGHT_DIRECTION_INVALID,
    1413: NET_DVR_ERR_LACK_IOABLITY,
    1414: NET_DVR_ERR_FTP_PORT,
    1415: NET_DVR_ERR_FTP_CATALOGUE,
    1416: NET_DVR_ERR_FTP_UPLOAD_TYPE,
    1417: NET_DVR_ERR_FLASH_PARAM_WRITE,
    1418: NET_DVR_ERR_FLASH_PARAM_READ,
    1419: NET_DVR_ERR_PICNAME_DELIMITER,
    1420: NET_DVR_ERR_PICNAME_ITEM,
    1421: NET_DVR_ERR_PLATE_RECOGNIZE_TYPE,
    1422: NET_DVR_ERR_CAPTURE_TIMES,
    1423: NET_DVR_ERR_LOOP_DISTANCE,
    1424: NET_DVR_ERR_LOOP_INPUT_STATUS,
    1425: NET_DVR_ERR_RELATE_IO_CONFLICT,
    1426: NET_DVR_ERR_INTERVAL_TIME,
    1427: NET_DVR_ERR_SIGN_SPEED,
    1428: NET_DVR_ERR_PIC_FLIP,
    1429: NET_DVR_ERR_RELATE_LANE_NUMBER,
    1430: NET_DVR_ERR_TRIGGER_MODE,
    1431: NET_DVR_ERR_DELAY_TIME,
    1432: NET_DVR_ERR_EXCEED_RS485_COUNT,
    1433: NET_DVR_ERR_RADAR_TYPE,
    1434: NET_DVR_ERR_RADAR_ANGLE,
    1435: NET_DVR_ERR_RADAR_SPEED_VALID_TIME,
    1436: NET_DVR_ERR_RADAR_LINE_CORRECT,
    1437: NET_DVR_ERR_RADAR_CONST_CORRECT,
    1438: NET_DVR_ERR_RECORD_PARAM,
    1439: NET_DVR_ERR_LIGHT_WITHOUT_COLOR_AND_DIRECTION,
    1440: NET_DVR_ERR_LIGHT_WITHOUT_DETECTION_REGION,
    1441: NET_DVR_ERR_RECOGNIZE_PROVINCE_PARAM,
    1442: NET_DVR_ERR_SPEED_TIMEOUT,
    1443: NET_DVR_ERR_NTP_TIMEZONE,
    1444: NET_DVR_ERR_NTP_INTERVAL_TIME,
    1445: NET_DVR_ERR_NETWORK_CARD_NUM,
    1446: NET_DVR_ERR_DEFAULT_ROUTE,
    1447: NET_DVR_ERR_BONDING_WORK_MODE,
    1448: NET_DVR_ERR_SLAVE_CARD,
    1449: NET_DVR_ERR_PRIMARY_CARD,
    1450: NET_DVR_ERR_DHCP_PPOE_WORK,
    1451: NET_DVR_ERR_NET_INTERFACE,
    1452: NET_DVR_ERR_MTU,
    1453: NET_DVR_ERR_NETMASK,
    1454: NET_DVR_ERR_IP_INVALID,
    1455: NET_DVR_ERR_MULTICAST_IP_INVALID,
    1456: NET_DVR_ERR_GATEWAY_INVALID,
    1457: NET_DVR_ERR_DNS_INVALID,
    1458: NET_DVR_ERR_ALARMHOST_IP_INVALID,
    1459: NET_DVR_ERR_IP_CONFLICT,
    1460: NET_DVR_ERR_NETWORK_SEGMENT,
    1461: NET_DVR_ERR_NETPORT,
    1462: NET_DVR_ERR_PPPOE_NOSUPPORT,
    1463: NET_DVR_ERR_DOMAINNAME_NOSUPPORT,
    1464: NET_DVR_ERR_NO_SPEED,
    1465: NET_DVR_ERR_IOSTATUS_INVALID,
    1466: NET_DVR_ERR_BURST_INTERVAL_INVALID,
    1467: NET_DVR_ERR_RESERVE_MODE,
    1468: NET_DVR_ERR_LANE_NO,
    1469: NET_DVR_ERR_COIL_AREA_TYPE,
    1470: NET_DVR_ERR_TRIGGER_AREA_PARAM,
    1471: NET_DVR_ERR_SPEED_LIMIT_PARAM,
    1472: NET_DVR_ERR_LANE_PROTOCOL_TYPE,
    1473: NET_DVR_ERR_INTERVAL_TYPE,
    1474: NET_DVR_ERR_INTERVAL_DISTANCE,
    1475: NET_DVR_ERR_RS485_ASSOCIATE_DEVTYPE,
    1476: NET_DVR_ERR_RS485_ASSOCIATE_LANENO,
    1477: NET_DVR_ERR_LANENO_ASSOCIATE_MULTIRS485,
    1478: NET_DVR_ERR_LIGHT_DETECTION_REGION,
    1479: NET_DVR_ERR_DN2D_NOSUPPORT,
    1480: NET_DVR_ERR_IRISMODE_NOSUPPORT,
    1481: NET_DVR_ERR_WB_NOSUPPORT,
    1482: NET_DVR_ERR_IO_EFFECTIVENESS,
    1483: NET_DVR_ERR_LIGHTNO_MAX,
    1484: NET_DVR_ERR_LIGHTNO_CONFLICT,
    1485: NET_DVR_ERR_CANCEL_LINE,
    1486: NET_DVR_ERR_STOP_LINE,
    1487: NET_DVR_ERR_RUSH_REDLIGHT_LINE,
    1488: NET_DVR_ERR_IOOUTNO_MAX,
    1489: NET_DVR_ERR_IOOUTNO_AHEADTIME_MAX,
    1490: NET_DVR_ERR_IOOUTNO_IOWORKTIME,
    1491: NET_DVR_ERR_IOOUTNO_FREQMULTI,
    1492: NET_DVR_ERR_IOOUTNO_DUTYRATE,
    1493: NET_DVR_ERR_VIDEO_WITH_EXPOSURE,
    1494: NET_DVR_ERR_PLATE_BRIGHTNESS_WITHOUT_FLASHDET,
    1495: NET_DVR_ERR_RECOGNIZE_TYPE_PARAM,
    1496: NET_DVR_ERR_PALTE_RECOGNIZE_AREA_PARAM,
    1497: NET_DVR_ERR_PORT_CONFLICT,
    1498: NET_DVR_ERR_LOOP_IP,
    1499: NET_DVR_ERR_DRIVELINE_SENSITIVE,
    1500: NET_ERR_VQD_TIME_CONFLICT,
    1501: NET_ERR_VQD_PLAN_NO_EXIST,
    1502: NET_ERR_VQD_CHAN_NO_EXIST,
    1503: NET_ERR_VQD_CHAN_MAX,
    1504: NET_ERR_VQD_TASK_MAX,
    1551: NET_SDK_GET_INPUTSTREAMCFG,
    1552: NET_SDK_AUDIO_SWITCH_CONTROL,
    1553: NET_SDK_GET_VIDEOWALLDISPLAYNO,
    1554: NET_SDK_GET_ALLSUBSYSTEM_BASIC_INFO,
    1555: NET_SDK_SET_ALLSUBSYSTEM_BASIC_INFO,
    1556: NET_SDK_GET_AUDIO_INFO,
    1557: NET_SDK_GET_MATRIX_STATUS_V50,
    1558: NET_SDK_DELETE_MONITOR_INFO,
    1559: NET_SDK_DELETE_CAMERA_INFO,
    1600: NET_DVR_ERR_EXCEED_MAX_CAPTURE_TIMES,
    1601: NET_DVR_ERR_REDAR_TYPE_CONFLICT,
    1602: NET_DVR_ERR_LICENSE_PLATE_NULL,
    1603: NET_DVR_ERR_WRITE_DATABASE,
    1604: NET_DVR_ERR_LICENSE_EFFECTIVE_TIME,
    1605: NET_DVR_ERR_PRERECORDED_STARTTIME_LONG,
    1606: NET_DVR_ERR_TRIGGER_RULE_LINE,
    1607: NET_DVR_ERR_LEFTRIGHT_TRIGGERLINE_NOTVERTICAL,
    1608: NET_DVR_ERR_FLASH_LAMP_MODE,
    1609: NET_DVR_ERR_ILLEGAL_SNAPSHOT_NUM,
    1610: NET_DVR_ERR_ILLEGAL_DETECTION_TYPE,
    1611: NET_DVR_ERR_POSITIVEBACK_TRIGGERLINE_HIGH,
    1612: NET_DVR_ERR_MIXEDMODE_CAPTYPE_ALLTARGETS,
    1613: NET_DVR_ERR_CARSIGNSPEED_GREATERTHAN_LIMITSPEED,
    1614: NET_DVR_ERR_BIGCARSIGNSPEED_GREATERTHAN_LIMITSPEED,
    1615: NET_DVR_ERR_BIGCARSIGNSPEED_GREATERTHAN_CARSIGNSPEED,
    1616: NET_DVR_ERR_BIGCARLIMITSPEED_GREATERTHAN_CARLIMITSPEED,
    1617: NET_DVR_ERR_BIGCARLOWSPEEDLIMIT_GREATERTHAN_CARLOWSPEEDLIMIT,
    1618: NET_DVR_ERR_CARLIMITSPEED_GREATERTHAN_EXCEPHIGHSPEED,
    1619: NET_DVR_ERR_BIGCARLIMITSPEED_GREATERTHAN_EXCEPHIGHSPEED,
    1620: NET_DVR_ERR_STOPLINE_MORETHAN_TRIGGERLINE,
    1621: NET_DVR_ERR_YELLOWLIGHTTIME_INVALID,
    1622: NET_DVR_ERR_TRIGGERLINE1_FOR_NOT_YIELD_TO_PEDESTRIAN_CANNOT_EXCEED_TRIGGERLINE2,
    1623: NET_DVR_ERR_TRIGGERLINE2_FOR_NOT_YIELD_TO_PEDESTRIAN_CANNOT_EXCEED_TRIGGERLINE1,
    1900: NET_ERR_TIME_OVERLAP,
    1901: NET_ERR_HOLIDAY_PLAN_OVERLAP,
    1902: NET_ERR_CARDNO_NOT_SORT,
    1903: NET_ERR_CARDNO_NOT_EXIST,
    1904: NET_ERR_ILLEGAL_CARDNO,
    1905: NET_ERR_ZONE_ALARM,
    1906: NET_ERR_ZONE_OPERATION_NOT_SUPPORT,
    1907: NET_ERR_INTERLOCK_ANTI_CONFLICT,
    1908: NET_ERR_DEVICE_CARD_FULL,
    1909: NET_ERR_HOLIDAY_GROUP_DOWNLOAD,
    1910: NET_ERR_LOCAL_CONTROL_OFF,
    1911: NET_ERR_LOCAL_CONTROL_DISADD,
    1912: NET_ERR_LOCAL_CONTROL_HASADD,
    1913: NET_ERR_LOCAL_CONTROL_DOORNO_CONFLICT,
    1914: NET_ERR_LOCAL_CONTROL_COMMUNICATION_FAIL,
    1915: NET_ERR_OPERAND_INEXISTENCE,
    1916: NET_ERR_LOCAL_CONTROL_OVER_LIMIT,
    1917: NET_ERR_DOOR_OVER_LIMIT,
    1918: NET_ERR_ALARM_OVER_LIMIT,
    1919: NET_ERR_LOCAL_CONTROL_ADDRESS_INCONFORMITY_TYPE,
    1920: NET_ERR_NOT_SUPPORT_ONE_MORE_CARD,
    1921: NET_ERR_DELETE_NO_EXISTENCE_FACE,
    1922: NET_ERR_DOOR_SPECIAL_PASSWORD_REPEAT,
    1923: NET_ERR_AUTH_CODE_REPEAT,
    1924: NET_ERR_DEPLOY_EXCEED_MAX,
    1925: NET_ERR_NOT_SUPPORT_DEL_FP_BY_ID,
    1926: NET_ERR_TIME_RANGE,
    1927: NET_ERR_CAPTURE_TIMEOUT,
    1928: NET_ERR_LOW_SCORE,
    1929: NET_ERR_OFFLINE_CAPTURING,
    1950: NET_DVR_ERR_OUTDOOR_COMMUNICATION,
    1951: NET_DVR_ERR_ROOMNO_UNDEFINED,
    1952: NET_DVR_ERR_NO_CALLING,
    1953: NET_DVR_ERR_RINGING,
    1954: NET_DVR_ERR_IS_CALLING_NOW,
    1955: NET_DVR_ERR_LOCK_PASSWORD_WRONG,
    1956: NET_DVR_ERR_CONTROL_LOCK_FAILURE,
    1957: NET_DVR_ERR_CONTROL_LOCK_OVERTIME,
    1958: NET_DVR_ERR_LOCK_DEVICE_BUSY,
    1959: NET_DVR_ERR_UNOPEN_REMOTE_LOCK_FUNCTION,
    2100: NET_DVR_ERR_FILE_NOT_COMPLETE,
    2101: NET_DVR_ERR_IPC_EXIST,
    2102: NET_DVR_ERR_ADD_IPC,
    2103: NET_DVR_ERR_OUT_OF_RES,
    2104: NET_DVR_ERR_CONFLICT_TO_LOCALIP,
    2105: NET_DVR_ERR_IP_SET,
    2106: NET_DVR_ERR_PORT_SET,
    2107: NET_ERR_WAN_NOTSUPPORT,
    2108: NET_ERR_MUTEX_FUNCTION,
    2109: NET_ERR_QUESTION_CONFIGNUM,
    2110: NET_ERR_FACECHAN_NORESOURCE,
    2111: NET_ERR_DATA_CALLBACK,
    2112: NET_ERR_ATM_VCA_CHAN_IS_RELATED,
    2113: NET_ERR_ATM_VCA_CHAN_IS_OVERLAPED,
    2114: NET_ERR_FACE_CHAN_UNOVERLAP_EACH_OTHER,
    2115: NET_ERR_ACHIEVE_MAX_CHANNLE_LIMIT,
    2116: NET_DVR_SMD_ENCODING_NORESOURSE,
    2117: NET_DVR_SMD_DECODING_NORESOURSE,
    2118: NET_DVR_FACELIB_DATA_PROCESSING,
    2119: NET_DVR_ERR_LARGE_TIME_DIFFRENCE,
    2120: NET_DVR_NO_SUPPORT_WITH_PLAYBACK,
    2121: NET_DVR_CHANNEL_NO_SUPPORT_WITH_SMD,
    2122: NET_DVR_CHANNEL_NO_SUPPORT_WITH_FD,
    2123: NET_DVR_ILLEGAL_PHONE_NUMBER,
    2124: NET_DVR_ILLEGAL_CERITIFICATE_NUMBER,
    2125: NET_DVR_ERR_CHANNEL_RESOLUTION_NO_SUPPORT,
    2126: NET_DVR_ERR_CHANNEL_COMPRESSION_NO_SUPPORT,
    2127: NET_DVR_ERR_CLUSTER_DEVICE_TOO_LESS,
    2128: NET_DVR_ERR_CLUSTER_DEL_DEVICE_CM_PLAYLOAD,
    2129: NET_DVR_ERR_CLUSTER_DEVNUM_OVER_UPPER_LIMIT,
    2130: NET_DVR_ERR_CLUSTER_DEVICE_TYPE_INCONFORMITY,
    2131: NET_DVR_ERR_CLUSTER_DEVICE_VERSION_INCONFORMITY,
    2132: NET_DVR_ERR_CLUSTER_IP_CONFLICT,
    2133: NET_DVR_ERR_CLUSTER_IP_INVALID,
    2134: NET_DVR_ERR_CLUSTER_PORT_CONFLICT,
    2135: NET_DVR_ERR_CLUSTER_PORT_INVALID,
    2136: NET_DVR_ERR_CLUSTER_USERNAEM_OR_PASSWORD_INVALID,
    2137: NET_DVR_ERR_CLUSTER_DEVICE_ALREADY_EXIST,
    2138: NET_DVR_ERR_CLUSTER_DEVICE_NOT_EXIST,
    2139: NET_DVR_ERR_CLUSTER_NON_CLUSTER_MODE,
    2140: NET_DVR_ERR_CLUSTER_IP_NOT_SAME_LAN,
    2141: NET_DVR_ERR_CAPTURE_PACKAGE_FAILED,
    2142: NET_DVR_ERR_CAPTURE_PACKAGE_PROCESSING,
    2143: NET_DVR_ERR_SAFETY_HELMET_NO_RESOURCE,
    2144: NET_DVR_NO_SUPPORT_WITH_ABSTRACT,
    2145: NET_DVR_ERR_TAPE_LIB_NEED_STOP_ARCHIVE,
    2146: NET_DVR_INSUFFICIENT_DEEP_LEARNING_RESOURCES,
    2147: NET_DVR_ERR_IDENTITY_KEY,
    2148: NET_DVR_MISSING_IDENTITY_KEY,
    2149: NET_DVR_NO_SUPPORT_WITH_PERSON_DENSITY_DETECT,
    2150: NET_DVR_IPC_RESOLUTION_OVERFLOW,
    2151: NET_DVR_IPC_BITRATE_OVERFLOW,
    2152: NET_DVR_ERR_INVALID_TASKID,
    2153: NET_DVR_PANEL_MODE_NOT_CONFIG,
    2154: NET_DVR_NO_HUMAN_ENGINES_RESOURCE,
    2155: NET_DVR_ERR_TASK_NUMBER_OVERFLOW,
    2156: NET_DVR_ERR_COLLISION_TIME_OVERFLOW,
    2157: NET_DVR_ERR_CAPTURE_PACKAGE_NO_USB,
    2158: NET_DVR_ERR_NO_SET_SECURITY_EMAIL,
    2159: NET_DVR_ERR_EVENT_NOTSUPPORT,
    2160: NET_DVR_ERR_PASSWORD_FORMAT,
    2161: NET_DVR_ACCESS_FRONT_DEVICE_PARAM_FAILURE,
    2162: NET_DVR_ACCESS_FRONT_DEVICE_STREAM_FAILURE,
    2163: NET_DVR_ERR_USERNAME_FORMAT,
    2164: NET_DVR_ERR_UNOPENED_HIGH_RESOLUTION_MODE,
    2165: NET_DVR_ERR_TOO_SMALL_QUATO,
    2166: NET_DVR_ERR_EMAIL_FORMAT,
    2167: NET_DVR_ERR_SECURITY_CODE_FORMAT,
    2168: NET_DVR_PD_SPACE_TOO_SMALL,
    2169: NET_DVR_PD_NUM_TOO_BIG,
    2170: NET_DVR_ERR_USB_IS_FULL,
    2171: NET_DVR_EXCEED_MAX_SMD_TYPE,
    2172: NET_DVR_CHANNEL_NO_SUPPORT_WITH_BEHAVIOR,
    2173: NET_DVR_NO_BEHAVIOR_ENGINES_RESOURCE,
    2174: NET_DVR_NO_RETENTION_ENGINES_RESOURCE,
    2175: NET_DVR_NO_LEAVE_POSITION_ENGINES_RESOURCE,
    2176: NET_DVR_NO_PEOPLE_NUM_CHANGE_ENGINES_RESOURCE,
    2177: NET_DVR_PANEL_MODE_NUM_OVER_LIMIT,
    2178: NET_DVR_SURROUND_MODE_NUM_OVER_LIMIT,
    2179: NET_DVR_FACE_MODE_NUM_OVER_LIMIT,
    2180: NET_DVR_SAFETYCABIN_MODE_NUM_OVER_LIMIT,
    2181: NET_DVR_DETECT_REGION_RANGE_INVALID,
    2182: NET_DVR_CHANNEL_CAPTURE_PICTURE_FAILURE,
    2183: NET_DVR_VCACHAN_IS_NORESOURCE,
    2184: NET_DVR_IPC_NUM_REACHES_LIMIT,
    2185: NET_DVR_IOT_NUM_REACHES_LIMIT,
    2186: NET_DVR_IOT_CHANNEL_DEVICE_EXIST,
    2187: NET_DVR_IOT_CHANNEL_DEVICE_NOT_EXIST,
    2188: NET_DVR_INVALID_IOT_PROTOCOL_TYPE,
    2189: NET_DVR_INVALID_EZVIZ_SECRET_KEY,
    2190: NET_DVR_DUPLICATE_IOT_DEVICE,
    2191: NET_DVR_SADP_MODIFY_FALIURE,
    2192: NET_DVR_IPC_NETWORK_ABNORMAL,
    2193: NET_DVR_IPC_PASSWORD_ERROR,
    2194: NET_DVR_ERROR_IPC_TYPE,
    2195: NET_DVR_ERROR_IPC_LIST_NOT_EMPTY,
    2196: NET_DVR_ERROR_IPC_LIST_NOT_MATCH_PAIRING,
    2197: NET_DVR_ERROR_IPC_BAD_LANGUAGE,
    2198: NET_DVR_ERROR_IPC_IS_LOCKING,
    2199: NET_DVR_ERROR_IPC_NOT_ACTIVATED,
    2200: NET_DVR_FIELD_CODING_NOT_SUPPORT,
    2201: NET_DVR_ERROR_H323_NOT_SUPPORT_H265,
    2202: NET_DVR_ERROR_EXPOSURE_TIME_TOO_BIG_IN_MODE_P,
    2203: NET_DVR_ERROR_EXPOSURE_TIME_TOO_BIG_IN_MODE_N,
    2204: NET_DVR_ERROR_PING_PROCESSING,
    2205: NET_DVR_ERROR_PING_NOT_START,
    2206: NET_DVR_ERROR_NEED_DOUBLE_VERIFICATION,
    2207: NET_DVR_NO_DOUBLE_VERIFICATION_USER,
    2208: NET_DVR_CHANNEL_OFFLINE,
    2209: NET_DVR_TIMESPAN_NUM_OVER_LIMIT,
    2210: NET_DVR_CHANNEL_NUM_OVER_LIMIT,
    2211: NET_DVR_NO_SEARCH_ID_RESOURCE,
    2212: NET_DVR_ERROR_ONEKEY_EXPORT,
    2213: NET_DVR_NO_CITY_MANAGEMENT_ENGINES_RESOURCE,
    2214: NET_DVR_NO_SITUATION_ANALYSIS_ENGINES_RESOURCE,
    2215: NET_DVR_INTELLIGENT_ANALYSIS_IPC_CANNT_DELETE,
    2216: NET_DVR_NOSUPPORT_RESET_PASSWORD,
    2217: NET_DVR_ERROR_IPC_NEED_ON_LAN,
    2218: NET_DVR_CHANNEL_NO_SUPPORT_WITH_SAFETY_HELMET,
    2219: NET_DVR_ERROR_GET_RESETPASSWORDTYPE_IS_ABNORMAL,
    2220: NET_DVR_ERROR_IPC_NOSUPPORT_RESET_PASSWORD,
    2221: NET_DVR_ERROR_IP_IS_NOT_ONLY_ONE,
    2222: NET_DVR_NO_SUPPORT_WITH_SMD_OR_SCD,
    2223: NET_DVR_NO_SUPPORT_WITH_FD,
    2224: NET_DVR_NO_FD_ENGINES_RESOURCE,
    2225: NET_DVR_ERROR_ONEKEY_REMOVE,
    2226: NET_DVR_FACE_PIP_BACKGROUND_CHANNEL_OVERFLOW,
    2227: NET_DVR_MICIN_CHANNEL_OCCUPIED,
    2228: NET_DVR_IPC_CHANNEL_IS_IN_PIP,
    2229: NET_DVR_CHANNEL_NO_SUPPORT_WITH_FACE_CONTRAST,
    2230: NET_DVR_INVALID_RECHARGE_CARD,
    2231: NET_DVR_CLOUD_PLATFORM_SERVER_EXCEPTION,
    2232: NET_DVR_OPERATION_FAILURE_WITHOUT_LOGIN,
    2233: NET_DVR_INVALID_ASSOCIATED_SERIAL_NUMBER,
    2234: NET_DVR_CLOUD_PLATFORM_ACCOUNT_NOT_EXIST,
    2235: NET_DVR_DEVICE_SERIAL_NUMBER_REGISTERED,
    2236: NET_DVR_CONFERENCE_ROOM_NOT_EXIST,
    2237: NET_DVR_NEED_DISABLED_ANALOG_CHANNEL,
    2238: NET_DVR_STUDENT_ROLL_CALL_FAILURE,
    2239: NET_DVR_SUB_DEVICE_NOT_ENABLE_INDIVIDUAL_BEHAVIOR,
    2240: NET_DVR_SUB_DEVICE_CHANNEL_CONTROL_FAILED,
    2241: NET_DVR_DEVICE_NOT_IN_CONFERENCE,
    2242: NET_DVR_ALREADY_EXIST_CONFERENCE,
    2243: NET_DVR_NO_SUPPORT_WITH_VIDEO_CONFERENCE,
    2244: NET_DVR_START_INTERACTION_FAILURE,
    2245: NET_DVR_ASK_QUESTION_STARTED,
    2246: NET_DVR_ASK_QUESTION_CLOSED,
    2247: NET_DVR_UNABLE_OPERATE_BY_HOST,
    2248: NET_DVR_REPEATED_ASK_QUESTION,
    2249: NET_DVR_SWITCH_TIMEDIFF_LESS_LIMIT,
    2250: NET_DVR_CHANNEL_DEVICE_EXIST,
    2251: NET_DVR_CHANNEL_DEVICE_NOT_EXIST,
    2252: NET_DVR_ERROR_ADJUSTING_RESOLUTION,
    2253: NET_DVR_SSD_FILE_SYSTEM_IS_UPGRADING,
    2254: NET_DVR_SSD_FILE_SYSTEM_IS_FORMAT,
    2255: NET_DVR_CHANNEL_IS_CONNECTING,
    2257: NET_DVR_CHANNEL_STREAM_TYPE_NOT_SUPPORT,
    2258: NET_DVR_CHANNEL_USERNAME_NOT_EXIST,
    2259: NET_DVR_CHANNEL_ACCESS_PARAM_FAILURE,
    2260: NET_DVR_CHANNEL_GET_STREAM_FAILURE,
    2261: NET_DVR_CHANNEL_RISK_PASSWORD,
    2262: NET_DVR_NO_SUPPORT_DELETE_STRANGER_LIB,
    2263: NET_DVR_NO_SUPPORT_CREATE_STRANGER_LIB,
    2264: NET_DVR_NETWORK_PORT_CONFLICT,
    2265: NET_DVR_TRANSCODE_NO_RESOURCES,
    2266: NET_DVR_SSD_FILE_SYSTEM_ERROR,
    2267: NET_DVR_INSUFFICIENT_SSD__FOR_FPD,
    2268: NET_DVR_ASSOCIATED_FACELIB_OVER_LIMIT,
    2269: NET_DVR_NEED_DELETE_DIGITAL_CHANNEL,
    2270: NET_DVR_ERR_FALL_DOWN_RULENUM_LIMIT,
    2271: NET_DVR_ERR_VIOLENT_MOTION_RULENUM_LIMIT,
    2272: NET_DVR_UPGRADE_ENGINE_VERSION_MISMATCH,
    3001: NET_DVR_ERR_NOTSUPPORT_DEICING,
    3002: NET_DVR_ERR_THERMENABLE_CLOSE,
    3003: NET_DVR_ERR_NOTMEET_DEICING,
    3004: NET_DVR_ERR_PANORAMIC_LIMIT_OPERATED,
    3005: NET_DVR_ERR_SMARTH264_ROI_OPERATED,
    3006: NET_DVR_ERR_RULENUM_LIMIT,
    3007: NET_DVR_ERR_LASER_DEICING_OPERATED,
    3008: NET_DVR_ERR_OFFDIGITALZOOM_OR_MINZOOMLIMIT,
    3009: NET_DVR_ERR_FIREWAITING,
    3010: NET_DVR_SYNCHRONIZEFOV_ERROR,
    3011: NET_DVR_CERTIFICATE_VALIDATION_ERROR,
    3012: NET_DVR_CERTIFICATES_NUM_EXCEED_ERROR,
    3013: NET_DVR_RULE_SHIELDMASK_CONFLICT_ERROR,
    3014: NET_DVR_MOTOR_PREHEATING_ERROR,
    3015: NET_DVR_PT_DEICING_ERROR,
    3501: NET_DVR_ERR_NO_SAFETY_HELMET_REGION,
    3502: NET_DVR_ERR_UNCLOSED_SAFETY_HELMET,
    3503: NET_DVR_ERR_MUX_RECV_STATE,
    3504: NET_DVR_UPLOAD_HBDLIBID_ERROR,
    3505: NET_DVR_NOTSUPPORT_SMALLER_RATIOS,
    3506: NET_ERR_ACCOUNT_NOT_ACTIVED,
    8000: NET_ERR_NPQ_BASE_INDEX,
    8001: NET_ERR_NPQ_PARAM,
    8002: NET_ERR_NPQ_SYSTEM,
    8003: NET_ERR_NPQ_GENRAL,
    8004: NET_ERR_NPQ_PRECONDITION,
    8005: NET_ERR_NPQ_NOTSUPPORT,
    8100: NET_ERR_NPQ_NOTCALLBACK,
    8101: NET_ERR_NPQ_LOADLIB,
    8104: NET_ERR_NPQ_STEAM_CLOSE,
    8110: NET_ERR_NPQ_MAX_LINK,
    8111: NET_ERR_NPQ_STREAM_CFG,
    8112: NET_ERR_NPQ_PLAYBACK_OVERSPEED,
    8113: NET_ERR_NPQ_PLAYBACK_BELOWSPEED,
    8300: NET_EZVIZ_P2P_BASE_INDEX,
    8301: NET_DVR_EZVIZ_P2P_REGISTER_ERROR,
    8302: NET_DVR_EZVIZ_P2P_LOGIN_2C_ERROR,
    8303: NET_DVR_EZVIZ_P2P_LOGIN_2B_ERROR,
    8304: NET_DVR_EZVIZ_P2P_BUILDLINK_ERROR,
    8305: NET_DVR_EZVIZ_P2P_PORTMAPPING_ERROR,
    8306: NET_DVR_EZVIZ_P2P_COULDNT_RESOLVE_HOST,
    8307: NET_DVR_EZVIZ_P2P_COULDNT_CONNECT,
    8308: NET_DVR_EZVIZ_P2P_OPERATION_TIMEOUT,
    8309: NET_DVR_EZVIZ_P2P_NOT_INITIALIZED,
    8310: NET_DVR_EZVIZ_P2P_INVALID_ARG,
    8311: NET_DVR_EZVIZ_P2P_EXCEED_MAX_SERVICE,
    8312: NET_DVR_EZVIZ_P2P_TOKEN_NOT_EXIST,
    8313: NET_DVR_EZVIZ_P2P_DISCONNECTED,
    8314: NET_DVR_EZVIZ_P2P_RELAY_ADDR_NOT_EXIST,
    8315: NET_DVR_EZVIZ_P2P_DEV_NOT_ONLINE,
    8316: NET_DVR_EZVIZ_P2P_DEV_CONNECT_EXCEED,
    8317: NET_DVR_EZVIZ_P2P_DEV_CONNECT_FAILED,
    8318: NET_DVR_EZVIZ_P2P_DEV_RECV_TIMEOUT,
    8319: NET_DVR_EZVIZ_P2P_USER_FORCE_STOP,
    8320: NET_DVR_EZVIZ_P2P_NO_PERMISSION,
    8321: NET_DVR_EZVIZ_P2P_DEV_PU_NOT_FOUND,
    8322: NET_DVR_EZVIZ_P2P_DEV_CONN_NOLONGER_AVAIL,
    8323: NET_DVR_EZVIZ_P2P_DEV_NOT_LISTENING,
    8324: NET_DVR_EZVIZ_P2P_DEV_TUNNEL_SOCKET_LIMITED,
    8325: NET_DVR_EZVIZ_P2P_FAIL_CREATE_THREAD,
    8326: NET_DVR_EZVIZ_P2P_FAIL_ALLOC_BUFFERS,
    8327: NET_DVR_EZVIZ_P2P_FAIL_CREATE_SOCKET,
    8328: NET_DVR_EZVIZ_P2P_BIND_LOCAL_SERVICE,
    8329: NET_DVR_EZVIZ_P2P_LISTEN_LOCAL_SERVICE,
    8330: NET_DVR_EZVIZ_P2P_SVR_RSP_BAD,
    8331: NET_DVR_EZVIZ_P2P_SVR_RSP_INVALID,
    8332: NET_DVR_EZVIZ_P2P_SVR_LOGIN_FAILED,
    8333: NET_DVR_EZVIZ_P2P_SVR_TOKEN_EXPIRED,
    8334: NET_DVR_EZVIZ_P2P_SVR_DEV_NOT_BELONG_TO_USER,
    8501: NET_ERR_UPGRADE_PROG_ERR,
    8502: NET_ERR_UPGRADE_NO_DEVICE,
    8503: NET_ERR_UPGRADE_NO_FILE,
    8504: NET_ERR_UPGRADE_DATA_ERROR,
    8505: NET_ERR_UPGRADE_LINK_SERVER_ERR,
    8506: NET_ERR_UPGRADE_OEMCODE_NOMATCH,
    8507: NET_ERR_UPGRADE_FLASH_NOENOUGH,
    8508: NET_ERR_UPGRADE_RAM_NOENOUGH,
    8509: NET_ERR_UPGRADE_DSPRAM_NOENOUGH,
    8510: NET_ERR_NOT_SUPPORT_CHECK,
    8511: NET_ERR_LED_DEVICE_BUSY_CHECK,
    8512: NET_ERR_DEVICE_MEM_NOT_ENOUGH,
    8513: NET_ERR_CHECK_PARAM,
    8514: NET_ERR_RESOLUTION_OVER_LIMIT,
    8515: NET_ERR_NO_CUSTOM_BASE,
    8516: NET_ERR_PRIORITY_LOWER,
    8517: NET_ERR_SEND_MESSAGE_EXCEPT,
    8518: NET_ERR_SENDCARD_UPGRADING,
    8519: NET_ERR_NO_WIRELESS_NETCARD,
    8520: NET_ERR_LOAD_FS_FAIL,
    8521: NET_ERR_FLASH_UNSTORAGE_RECCARD,
    8522: NET_ERR_NOT_SUPPORT_SINGLE_NETWORKCARD_AGGREGA,
    8523: NET_ERR_DISPLAYRESOLUTION_LESSTHAN_SMALLESTRESOLUTION,
    8524: NET_ERR_NOT_SUPPORT_LOCAL_SOURCE_DRAG_MORE,
    8525: NET_ERR_CANCEL_CURRENT_LED_AREA,
    8526: NET_ERR_LED_OUT_ASSOCIATED_AREA,
    8527: NET_ERR_MAX_VIRTUAL_LED_PICTURE_SIZE,
    8528: NET_ERR_DEVICE_CTRLED_BY_REMOTER,
}
