# 空的回调函数
fTimeDownLoadPosCallBack = CFUNCTYPE(UNCHECKED(None), c_longlong, c_uint, c_uint, c_int, NET_RECORDFILE_INFO, c_long)
大华的下载进度回调函数。
CLIENT_DownloadByTimeEx.argtypes = [c_longlong, c_int, c_int, LPNET_TIME, LPNET_TIME, String, fTimeDownLoadPosCallBack, c_long, fDataCallBack, c_long, POINTER(None)]
大华的按照时间下载视频函数
传入空的回调函数示例
downLoadHandle = cls.sdkDll.CLIENT_DownloadByTimeEx(userID, channel, DH.EM_RECORD_TYPE_ALL, startDateTime, endDateTime, savedFileName, DH.fTimeDownLoadPosCallBack(0), 0, DH.fDataCallBack(0), 0, pReserved)
中的DH.fTimeDownLoadPosCallBack(0)



# 由ctypesgen转换成的POINTER(None)形参类型该如何传参

ctyepsgen转换后:CLIENT_DownloadByTimeEx.argtypes = [c_longlong, c_int, c_int, LPNET_TIME, LPNET_TIME, String, fTimeDownLoadPosCallBack, c_long, fDataCallBack, c_long, POINTER(None)]
源代码:CLIENT_NET_API LLONG CALL_METHOD CLIENT_DownloadByTimeEx(LLONG lLoginID, int nChannelId, int nRecordFileType, LPNET_TIME tmStart, LPNET_TIME tmEnd, char* sSavedFileName,
                                                         fTimeDownLoadPosCallBack cbTimeDownLoadPos, LDWORD dwUserData,
                                                         fDataCallBack fDownLoadDataCallBack, LDWORD dwDataUser, void* pReserved = NULL);
看最后一个形参
