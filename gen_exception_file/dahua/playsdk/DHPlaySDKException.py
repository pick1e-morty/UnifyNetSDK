class DHPlaySDKException(Exception):

    def __init__(self):
        self.errorIndex = 0
        self.errorInfo = ""
        super().__init__(self.errorIndex, self.errorInfo)

    def __str__(self):
        if self.errorInfo:
            return str(self.errorIndex) + " " + self.errorInfo
        else:
            return str(self.errorIndex)


class PLAY_NOERROR(DHPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 0
        self.errorInfo = errorText


class PLAY_COMMON_ERROR(DHPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 1
        self.errorInfo = errorText


class PLAY_PARA_INVALID(DHPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 2
        self.errorInfo = errorText


class PLAY_ORDER_ERROR(DHPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 3
        self.errorInfo = errorText


class PLAY_PORT_OPEN(DHPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 4
        self.errorInfo = errorText


class PLAY_PORT_CLOSE(DHPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 5
        self.errorInfo = errorText


class PLAY_PORT_INVALID(DHPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 6
        self.errorInfo = errorText


class PLAY_PORT_EXIST(DHPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 7
        self.errorInfo = errorText


class PLAY_OPEN_FILE_ERROR(DHPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 8
        self.errorInfo = errorText


class PLAY_INTERFACE_NOT_SUPPORT(DHPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 9
        self.errorInfo = errorText


class PLAY_HWND_INVALID(DHPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 10
        self.errorInfo = errorText


class PLAY_PLAY_ERROR(DHPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 11
        self.errorInfo = errorText


class PLAY_SPEED_INVALID(DHPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 12
        self.errorInfo = errorText


class PLAY_NOT_FILE(DHPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 13
        self.errorInfo = errorText


class PLAY_NOT_STREAM(DHPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 14
        self.errorInfo = errorText


class PLAY_NO_FRAME(DHPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 15
        self.errorInfo = errorText


class PLAY_INDEX_NOT_COMPLETE(DHPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 16
        self.errorInfo = errorText


class PLAY_INDEX_COMPLETE(DHPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 17
        self.errorInfo = errorText


class PLAY_GET_FILE_SIZE_ERROR(DHPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 18
        self.errorInfo = errorText


class PLAY_CREATE_THREAD_FAIL(DHPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 19
        self.errorInfo = errorText


class PLAY_CREATE_EVENT_FAIL(DHPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 20
        self.errorInfo = errorText


class PLAY_SOUND_SHARE_MODE(DHPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 21
        self.errorInfo = errorText


class PLAY_INCLUDE_SOUND_SHARE_PORT(DHPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 22
        self.errorInfo = errorText


class PLAY_NOT_INCLUDE_SOUND_SHARE_PORT(DHPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 23
        self.errorInfo = errorText


class PLAY_CREATE_DIR_ERROR(DHPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 24
        self.errorInfo = errorText


class PLAY_CREATE_FILE_ERROR(DHPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 25
        self.errorInfo = errorText


class PLAY_CONVERT_YUV_ERROR(DHPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 26
        self.errorInfo = errorText


class PLAY_CONVERT_JPG_ERROR(DHPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 27
        self.errorInfo = errorText


class PLAY_CONVERT_BMP_ERROR(DHPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 28
        self.errorInfo = errorText


class PLAY_CONVERT_TIFF_ERROR(DHPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 29
        self.errorInfo = errorText


class PLAY_HW_CATCH_ERROR(DHPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 30
        self.errorInfo = errorText


class PLAY_CREATE_VIDEO_RENDER_ERROR(DHPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 31
        self.errorInfo = errorText


class PLAY_NOT_SUPPORT_REF_VALUE(DHPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 32
        self.errorInfo = errorText


class PLAY_FORMAT_NOT_SUPPORT(DHPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 33
        self.errorInfo = errorText


class PLAY_CREATE_RECORD_ERROR(DHPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 34
        self.errorInfo = errorText


class PLAY_OPEN_RECORD_ERROR(DHPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 35
        self.errorInfo = errorText


class PLAY_FRAMERATE_ERROR(DHPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 36
        self.errorInfo = errorText


class PLAY_CREATE_AUDIO_RECORD_ERROR(DHPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 37
        self.errorInfo = errorText


class PLAY_OPEN_AUDIO_RECORD_ERROR(DHPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 38
        self.errorInfo = errorText


class PLAY_AES_ALLOC_ERROR(DHPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 39
        self.errorInfo = errorText


class PLAY_BUF_OVER(DHPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 40
        self.errorInfo = errorText


class PLAY_ALLOC_MEMORY_ERROR(DHPlaySDKException):
    def __init__(self, errorText=None):
        self.errorIndex = 41
        self.errorInfo = errorText


DHPlaySDKExceptionDict = {
    0: PLAY_NOERROR,
    1: PLAY_COMMON_ERROR,
    2: PLAY_PARA_INVALID,
    3: PLAY_ORDER_ERROR,
    4: PLAY_PORT_OPEN,
    5: PLAY_PORT_CLOSE,
    6: PLAY_PORT_INVALID,
    7: PLAY_PORT_EXIST,
    8: PLAY_OPEN_FILE_ERROR,
    9: PLAY_INTERFACE_NOT_SUPPORT,
    10: PLAY_HWND_INVALID,
    11: PLAY_PLAY_ERROR,
    12: PLAY_SPEED_INVALID,
    13: PLAY_NOT_FILE,
    14: PLAY_NOT_STREAM,
    15: PLAY_NO_FRAME,
    16: PLAY_INDEX_NOT_COMPLETE,
    17: PLAY_INDEX_COMPLETE,
    18: PLAY_GET_FILE_SIZE_ERROR,
    19: PLAY_CREATE_THREAD_FAIL,
    20: PLAY_CREATE_EVENT_FAIL,
    21: PLAY_SOUND_SHARE_MODE,
    22: PLAY_INCLUDE_SOUND_SHARE_PORT,
    23: PLAY_NOT_INCLUDE_SOUND_SHARE_PORT,
    24: PLAY_CREATE_DIR_ERROR,
    25: PLAY_CREATE_FILE_ERROR,
    26: PLAY_CONVERT_YUV_ERROR,
    27: PLAY_CONVERT_JPG_ERROR,
    28: PLAY_CONVERT_BMP_ERROR,
    29: PLAY_CONVERT_TIFF_ERROR,
    30: PLAY_HW_CATCH_ERROR,
    31: PLAY_CREATE_VIDEO_RENDER_ERROR,
    32: PLAY_NOT_SUPPORT_REF_VALUE,
    33: PLAY_FORMAT_NOT_SUPPORT,
    34: PLAY_CREATE_RECORD_ERROR,
    35: PLAY_OPEN_RECORD_ERROR,
    36: PLAY_FRAMERATE_ERROR,
    37: PLAY_CREATE_AUDIO_RECORD_ERROR,
    38: PLAY_OPEN_AUDIO_RECORD_ERROR,
    39: PLAY_AES_ALLOC_ERROR,
    40: PLAY_BUF_OVER,
    41: PLAY_ALLOC_MEMORY_ERROR,
}
