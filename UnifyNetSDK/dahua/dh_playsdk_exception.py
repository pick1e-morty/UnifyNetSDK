class DHPlaySDKException(Exception):

    def __init__(self, code, value):
        self.code = code
        self.value = value
        super().__init__(self.code, self.value)


ErrorCode = {0: "PLAY_NOERROR",
             1: "PLAY_COMMON_ERROR",
             2: "PLAY_PARA_INVALID",
             3: "PLAY_ORDER_ERROR",
             4: "PLAY_PORT_OPEN",
             5: "PLAY_PORT_CLOSE",
             6: "PLAY_PORT_INVALID",
             7: "PLAY_PORT_EXIST",
             8: "PLAY_OPEN_FILE_ERROR",
             9: "PLAY_INTERFACE_NOT_SUPPORT",
             10: "PLAY_HWND_INVALID",
             11: "PLAY_PLAY_ERROR",
             12: "PLAY_SPEED_INVALID",
             13: "PLAY_NOT_FILE",
             14: "PLAY_NOT_STREAM",
             15: "PLAY_NO_FRAME",
             16: "PLAY_INDEX_NOT_COMPLETE",
             17: "PLAY_INDEX_COMPLETE",
             18: "PLAY_GET_FILE_SIZE_ERROR",
             19: "PLAY_CREATE_THREAD_FAIL",
             20: "PLAY_CREATE_EVENT_FAIL",
             21: "PLAY_SOUND_SHARE_MODE",
             22: "PLAY_INCLUDE_SOUND_SHARE_PORT",
             23: "PLAY_NOT_INCLUDE_SOUND_SHARE_PORT",
             24: "PLAY_CREATE_DIR_ERROR",
             25: "PLAY_CREATE_FILE_ERROR",
             26: "PLAY_CONVERT_YUV_ERROR",
             27: "PLAY_CONVERT_JPG_ERROR",
             28: "PLAY_CONVERT_BMP_ERROR",
             29: "PLAY_CONVERT_TIFF_ERROR",
             30: "PLAY_HW_CATCH_ERROR",
             31: "PLAY_CREATE_VIDEO_RENDER_ERROR",
             32: "PLAY_NOT_SUPPORT_REF_VALUE",
             33: "PLAY_FORMAT_NOT_SUPPORT",
             34: "PLAY_CREATE_RECORD_ERROR",
             35: "PLAY_OPEN_RECORD_ERROR",
             36: "PLAY_FRAMERATE_ERROR",
             37: "PLAY_CREATE_AUDIO_RECORD_ERROR",
             38: "PLAY_OPEN_AUDIO_RECORD_ERROR",
             39: "PLAY_AES_ALLOC_ERROR",
             40: "PLAY_BUF_OVER",
             41: "PLAY_ALLOC_MEMORY_ERROR",

             }
