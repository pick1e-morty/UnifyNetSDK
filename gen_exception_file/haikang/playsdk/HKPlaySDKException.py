class HKPlaySDKException(Exception):

    def __init__(self):
        self.errorIndex = 0
        self.errorInfo = ""
        super().__init__(self.errorIndex, self.errorInfo)

    def __str__(self):
        if self.errorInfo:
            return str(self.errorIndex) + " " + self.errorInfo
        else:
            return str(self.errorIndex)


class PLAYM4_NOERROR(HKPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 0
        self.errorInfo = errorText


class PLAYM4_PARA_OVER(HKPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1
        self.errorInfo = errorText


class PLAYM4_ORDER_ERROR(HKPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2
        self.errorInfo = errorText


class PLAYM4_TIMER_ERROR(HKPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 3
        self.errorInfo = errorText


class PLAYM4_DEC_VIDEO_ERROR(HKPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 4
        self.errorInfo = errorText


class PLAYM4_DEC_AUDIO_ERROR(HKPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 5
        self.errorInfo = errorText


class PLAYM4_ALLOC_MEMORY_ERROR(HKPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 6
        self.errorInfo = errorText


class PLAYM4_OPEN_FILE_ERROR(HKPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 7
        self.errorInfo = errorText


class PLAYM4_CREATE_OBJ_ERROR(HKPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8
        self.errorInfo = errorText


class PLAYM4_CREATE_DDRAW_ERROR(HKPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 9
        self.errorInfo = errorText


class PLAYM4_CREATE_OFFSCREEN_ERROR(HKPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 10
        self.errorInfo = errorText


class PLAYM4_BUF_OVER(HKPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 11
        self.errorInfo = errorText


class PLAYM4_CREATE_SOUND_ERROR(HKPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 12
        self.errorInfo = errorText


class PLAYM4_SET_VOLUME_ERROR(HKPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 13
        self.errorInfo = errorText


class PLAYM4_SUPPORT_FILE_ONLY(HKPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 14
        self.errorInfo = errorText


class PLAYM4_SUPPORT_STREAM_ONLY(HKPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 15
        self.errorInfo = errorText


class PLAYM4_SYS_NOT_SUPPORT(HKPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 16
        self.errorInfo = errorText


class PLAYM4_FILEHEADER_UNKNOWN(HKPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 17
        self.errorInfo = errorText


class PLAYM4_VERSION_INCORRECT(HKPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 18
        self.errorInfo = errorText


class PLAYM4_INIT_DECODER_ERROR(HKPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 19
        self.errorInfo = errorText


class PLAYM4_CHECK_FILE_ERROR(HKPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 20
        self.errorInfo = errorText


class PLAYM4_INIT_TIMER_ERROR(HKPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 21
        self.errorInfo = errorText


class PLAYM4_BLT_ERROR(HKPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 22
        self.errorInfo = errorText


class PLAYM4_UPDATE_ERROR(HKPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 23
        self.errorInfo = errorText


class PLAYM4_OPEN_FILE_ERROR_MULTI(HKPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 24
        self.errorInfo = errorText


class PLAYM4_OPEN_FILE_ERROR_VIDEO(HKPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 25
        self.errorInfo = errorText


class PLAYM4_JPEG_COMPRESS_ERROR(HKPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 26
        self.errorInfo = errorText


class PLAYM4_EXTRACT_NOT_SUPPORT(HKPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 27
        self.errorInfo = errorText


class PLAYM4_EXTRACT_DATA_ERROR(HKPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 28
        self.errorInfo = errorText


class PLAYM4_SECRET_KEY_ERROR(HKPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 29
        self.errorInfo = errorText


class PLAYM4_DECODE_KEYFRAME_ERROR(HKPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 30
        self.errorInfo = errorText


class PLAYM4_NEED_MORE_DATA(HKPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 31
        self.errorInfo = errorText


class PLAYM4_INVALID_PORT(HKPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 32
        self.errorInfo = errorText


class PLAYM4_NOT_FIND(HKPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 33
        self.errorInfo = errorText


class PLAYM4_NEED_LARGER_BUFFER(HKPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 34
        self.errorInfo = errorText


class PLAYM4_FAIL_UNKNOWN(HKPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 99
        self.errorInfo = errorText


class PLAYM4_FEC_ERR_ENABLEFAIL(HKPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 100
        self.errorInfo = errorText


class PLAYM4_FEC_ERR_NOTENABLE(HKPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 101
        self.errorInfo = errorText


class PLAYM4_FEC_ERR_NOSUBPORT(HKPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 102
        self.errorInfo = errorText


class PLAYM4_FEC_ERR_PARAMNOTINIT(HKPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 103
        self.errorInfo = errorText


class PLAYM4_FEC_ERR_SUBPORTOVER(HKPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 104
        self.errorInfo = errorText


class PLAYM4_FEC_ERR_EFFECTNOTSUPPORT(HKPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 105
        self.errorInfo = errorText


class PLAYM4_FEC_ERR_INVALIDWND(HKPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 106
        self.errorInfo = errorText


class PLAYM4_FEC_ERR_PTZOVERFLOW(HKPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 107
        self.errorInfo = errorText


class PLAYM4_FEC_ERR_RADIUSINVALID(HKPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 108
        self.errorInfo = errorText


class PLAYM4_FEC_ERR_UPDATENOTSUPPORT(HKPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 109
        self.errorInfo = errorText


class PLAYM4_FEC_ERR_NOPLAYPORT(HKPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 110
        self.errorInfo = errorText


class PLAYM4_FEC_ERR_PARAMVALID(HKPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 111
        self.errorInfo = errorText


class PLAYM4_FEC_ERR_INVALIDPORT(HKPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 112
        self.errorInfo = errorText


class PLAYM4_FEC_ERR_PTZZOOMOVER(HKPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 113
        self.errorInfo = errorText


class PLAYM4_FEC_ERR_OVERMAXPORT(HKPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 114
        self.errorInfo = errorText


class PLAYM4_FEC_ERR_ENABLED(HKPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 115
        self.errorInfo = errorText


class PLAYM4_FEC_ERR_D3DACCENOTENABLE(HKPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 116
        self.errorInfo = errorText


class PLAYM4_FEC_ERR_PLACETYPE(HKPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 117
        self.errorInfo = errorText


class PLAYM4_FEC_ERR_CorrectType(HKPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 118
        self.errorInfo = errorText


class PLAYM4_FEC_ERR_NULLWND(HKPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 119
        self.errorInfo = errorText


class PLAYM4_FEC_ERR_PARA(HKPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 120
        self.errorInfo = errorText


HKPlaySDKExceptionDict = {
    0: PLAYM4_NOERROR,
    1: PLAYM4_PARA_OVER,
    2: PLAYM4_ORDER_ERROR,
    3: PLAYM4_TIMER_ERROR,
    4: PLAYM4_DEC_VIDEO_ERROR,
    5: PLAYM4_DEC_AUDIO_ERROR,
    6: PLAYM4_ALLOC_MEMORY_ERROR,
    7: PLAYM4_OPEN_FILE_ERROR,
    8: PLAYM4_CREATE_OBJ_ERROR,
    9: PLAYM4_CREATE_DDRAW_ERROR,
    10: PLAYM4_CREATE_OFFSCREEN_ERROR,
    11: PLAYM4_BUF_OVER,
    12: PLAYM4_CREATE_SOUND_ERROR,
    13: PLAYM4_SET_VOLUME_ERROR,
    14: PLAYM4_SUPPORT_FILE_ONLY,
    15: PLAYM4_SUPPORT_STREAM_ONLY,
    16: PLAYM4_SYS_NOT_SUPPORT,
    17: PLAYM4_FILEHEADER_UNKNOWN,
    18: PLAYM4_VERSION_INCORRECT,
    19: PLAYM4_INIT_DECODER_ERROR,
    20: PLAYM4_CHECK_FILE_ERROR,
    21: PLAYM4_INIT_TIMER_ERROR,
    22: PLAYM4_BLT_ERROR,
    23: PLAYM4_UPDATE_ERROR,
    24: PLAYM4_OPEN_FILE_ERROR_MULTI,
    25: PLAYM4_OPEN_FILE_ERROR_VIDEO,
    26: PLAYM4_JPEG_COMPRESS_ERROR,
    27: PLAYM4_EXTRACT_NOT_SUPPORT,
    28: PLAYM4_EXTRACT_DATA_ERROR,
    29: PLAYM4_SECRET_KEY_ERROR,
    30: PLAYM4_DECODE_KEYFRAME_ERROR,
    31: PLAYM4_NEED_MORE_DATA,
    32: PLAYM4_INVALID_PORT,
    33: PLAYM4_NOT_FIND,
    34: PLAYM4_NEED_LARGER_BUFFER,
    99: PLAYM4_FAIL_UNKNOWN,
    100: PLAYM4_FEC_ERR_ENABLEFAIL,
    101: PLAYM4_FEC_ERR_NOTENABLE,
    102: PLAYM4_FEC_ERR_NOSUBPORT,
    103: PLAYM4_FEC_ERR_PARAMNOTINIT,
    104: PLAYM4_FEC_ERR_SUBPORTOVER,
    105: PLAYM4_FEC_ERR_EFFECTNOTSUPPORT,
    106: PLAYM4_FEC_ERR_INVALIDWND,
    107: PLAYM4_FEC_ERR_PTZOVERFLOW,
    108: PLAYM4_FEC_ERR_RADIUSINVALID,
    109: PLAYM4_FEC_ERR_UPDATENOTSUPPORT,
    110: PLAYM4_FEC_ERR_NOPLAYPORT,
    111: PLAYM4_FEC_ERR_PARAMVALID,
    112: PLAYM4_FEC_ERR_INVALIDPORT,
    113: PLAYM4_FEC_ERR_PTZZOOMOVER,
    114: PLAYM4_FEC_ERR_OVERMAXPORT,
    115: PLAYM4_FEC_ERR_ENABLED,
    116: PLAYM4_FEC_ERR_D3DACCENOTENABLE,
    117: PLAYM4_FEC_ERR_PLACETYPE,
    118: PLAYM4_FEC_ERR_CorrectType,
    119: PLAYM4_FEC_ERR_NULLWND,
    120: PLAYM4_FEC_ERR_PARA,
}
