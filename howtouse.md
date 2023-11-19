# 空的回调函数怎么写
大华下载进度回调函数 fTimeDownLoadPosCallBack = CFUNCTYPE(UNCHECKED(None), c_longlong, c_uint, c_uint, c_int, NET_RECORDFILE_INFO, c_long)
大华按照时间下载视频函数参数指定 CLIENT_DownloadByTimeEx.argtypes = [c_longlong, c_int, c_int, LPNET_TIME, LPNET_TIME, String, fTimeDownLoadPosCallBack, c_long, fDataCallBack, c_long, POINTER(None)]
传入空的回调函数示例
downLoadHandle = cls.sdkDll.CLIENT_DownloadByTimeEx(userID, channel, DH.EM_RECORD_TYPE_ALL, startDateTime, endDateTime, savedFileName, DH.fTimeDownLoadPosCallBack(0), 0, DH.fDataCallBack(0), 0, pReserved)
DH.fTimeDownLoadPosCallBack(0)就是空的回调函数



# POINTER(None)形参类型该如何传参

源代码:CLIENT_NET_API LLONG CALL_METHOD CLIENT_DownloadByTimeEx(LLONG lLoginID, int nChannelId, int nRecordFileType, LPNET_TIME tmStart, LPNET_TIME tmEnd, char* sSavedFileName,
                                                         fTimeDownLoadPosCallBack cbTimeDownLoadPos, LDWORD dwUserData,
                                                         fDataCallBack fDownLoadDataCallBack, LDWORD dwDataUser, void* pReserved = NULL);
ctyepsgen转换后:CLIENT_DownloadByTimeEx.argtypes = [c_longlong, c_int, c_int, LPNET_TIME, LPNET_TIME, String, fTimeDownLoadPosCallBack, c_long, fDataCallBack, c_long, POINTER(None)]
最后一个形参要求传入POINTER(None)
pReserved = pointer(c_int(0))
