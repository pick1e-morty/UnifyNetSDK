ErrorCode = {0: "PLAYM4_NOERROR",
             1: "PLAYM4_PARA_OVER",
             2: "PLAYM4_ORDER_ERROR",
             3: "PLAYM4_TIMER_ERROR",
             4: "PLAYM4_DEC_VIDEO_ERROR",
             5: "PLAYM4_DEC_AUDIO_ERROR",
             6: "PLAYM4_ALLOC_MEMORY_ERROR",
             7: "PLAYM4_OPEN_FILE_ERROR",
             8: "PLAYM4_CREATE_OBJ_ERROR",
             9: "PLAYM4_CREATE_DDRAW_ERROR",
             10: "PLAYM4_CREATE_OFFSCREEN_ERROR",
             11: "PLAYM4_BUF_OVER",
             12: "PLAYM4_CREATE_SOUND_ERROR",
             13: "PLAYM4_SET_VOLUME_ERROR",
             14: "PLAYM4_SUPPORT_FILE_ONLY",
             15: "PLAYM4_SUPPORT_STREAM_ONLY",
             16: "PLAYM4_SYS_NOT_SUPPORT",
             17: "PLAYM4_FILEHEADER_UNKNOWN",
             18: "PLAYM4_VERSION_INCORRECT",
             19: "PLAYM4_INIT_DECODER_ERROR",
             20: "PLAYM4_CHECK_FILE_ERROR",
             21: "PLAYM4_INIT_TIMER_ERROR",
             22: "PLAYM4_BLT_ERROR",
             23: "PLAYM4_UPDATE_ERROR",
             24: "PLAYM4_OPEN_FILE_ERROR_MULTI",
             25: "PLAYM4_OPEN_FILE_ERROR_VIDEO",
             26: "PLAYM4_JPEG_COMPRESS_ERROR",
             27: "PLAYM4_EXTRACT_NOT_SUPPORT",
             28: "PLAYM4_EXTRACT_DATA_ERROR",
             29: "PLAYM4_SECRET_KEY_ERROR",
             30: "PLAYM4_DECODE_KEYFRAME_ERROR",
             31: "PLAYM4_NEED_MORE_DATA",
             32: "PLAYM4_INVALID_PORT",
             33: "PLAYM4_NOT_FIND",
             34: "PLAYM4_NEED_LARGER_BUFFER",
             99: "PLAYM4_FAIL_UNKNOWN",
             100: "PLAYM4_FEC_ERR_ENABLEFAIL",
             101: "PLAYM4_FEC_ERR_NOTENABLE",
             102: "PLAYM4_FEC_ERR_NOSUBPORT",
             103: "PLAYM4_FEC_ERR_PARAMNOTINIT",
             104: "PLAYM4_FEC_ERR_SUBPORTOVER",
             105: "PLAYM4_FEC_ERR_EFFECTNOTSUPPORT",
             106: "PLAYM4_FEC_ERR_INVALIDWND",
             107: "PLAYM4_FEC_ERR_PTZOVERFLOW",
             108: "PLAYM4_FEC_ERR_RADIUSINVALID",
             109: "PLAYM4_FEC_ERR_UPDATENOTSUPPORT",
             110: "PLAYM4_FEC_ERR_NOPLAYPORT",
             111: "PLAYM4_FEC_ERR_PARAMVALID",
             112: "PLAYM4_FEC_ERR_INVALIDPORT",
             113: "PLAYM4_FEC_ERR_PTZZOOMOVER",
             114: "PLAYM4_FEC_ERR_OVERMAXPORT",
             115: "PLAYM4_FEC_ERR_ENABLED",
             116: "PLAYM4_FEC_ERR_D3DACCENOTENABLE",
             117: "PLAYM4_FEC_ERR_PLACETYPE",
             118: "PLAYM4_FEC_ERR_CorrectType",
             119: "PLAYM4_FEC_ERR_NULLWND",
             120: "PLAYM4_FEC_ERR_PARA",
             }


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


from gen_exception_file.utils import genrateExceptionDict, genrateException

AppendErrorInfo = {}
if __name__ == '__main__':
    genrateException(HKPlaySDKException, ErrorCode, AppendErrorInfo)
    genrateExceptionDict("HKPlaySDKExceptionDict", ErrorCode, fileName="HKPlaySDKException")
