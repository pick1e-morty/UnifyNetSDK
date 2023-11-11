我希望
CLIENT_NET_API BOOL CALL_METHOD CLIENT_StartBackUpCase(LLONG lLoginID = 123, int nWaitTime = abc);
可以变为
CLIENT_NET_API BOOL CALL_METHOD CLIENT_StartBackUpCase(LLONG lLoginID=123, int nWaitTime);
也就是把它的默认形参给删除掉了，我有多个同等格式的函数声明，正则表达式能做到吗

CLIENT_NET_API BOOL CALL_METHOD CLIENT_StopBackUpCase(LLONG lLoginID, const NET_IN_STOP_CASE_BACK_UP* pstInParam, NET_OUT_STOP_CASE_BACK_UP* pstOutParam, int nWaitTime = NET_INTERFACE_DEFAULT_TIMEOUT);
CLIENT_NET_API LLONG CALL_METHOD CLIENT_AttachBackUpCaseState(LLONG lLoginID, const NET_IN_ATTACH_CASE_BACK_UP_STATE* pstInParam, NET_OUT_ATTACH_CASE_BACK_UP_STATE* pstOutParam, int nWaitTime = NET_INTERFACE_DEFAULT_TIMEOUT);
CLIENT_NET_API BOOL CALL_METHOD CLIENT_DetachBackUpCaseState(LLONG lAttachHandle, const NET_IN_DETACH_CASE_BACK_UP_STATE* pstInParam, NET_OUT_DETACH_CASE_BACK_UP_STATE* pstOutParam, int nWaitTime = NET_INTERFACE_DEFAULT_TIMEOUT);
CLIENT_NET_API BOOL CALL_METHOD CLIENT_GetCaseBackUpInfo(LLONG lLoginID, const NET_IN_GET_CASE_BACK_UP_INFO* pstInParam, NET_OUT_GET_CASE_BACK_UP_INFO* pstOutParam, int nWaitTime = NET_INTERFACE_DEFAULT_TIMEOUT);

CLIENT_NET_API BOOL CALL_METHOD CLIENT_AlarmReset(LLONG lLoginID, DWORD dwAlarmType, int nChannel, void* pReserved = NULL, int nWaitTime = 1000);
tag 789
tag 456
123

# (?<=CLIENT_NET_API.*) = (\d|\w)+


CLIENT_NET_API
BOOL
CALL_METHOD
CLIENT_QueryNewSystemInfoEx(LLONG
lLoginID, char * szCommand, int
nChannelID, char * szOutBuffer, DWORD
dwOutBufferSize, int * error, void * pExtendInfo = NULL, int
waittime = 1000);


CLIENT_NET_API BOOL CALL_METHOD CLIENT_QueryNewSystemInfoEx(int* error, void* pExtendInfo = NULL, int waittime = 1000);
# (?<=CLIENT_NET_API).*(\s*=\s*[\d\w]*)+       # 一步到位做不到
# (?<=CLIENT_NET_API)                        .*                                 (\s*=\s*[\d\w]*)+
# 只有发现CLIENT_NET_API才进行后续操作    全匹配,不过需要丢掉     比如匹配：int waittime = 3000中的 = 3000这一部分，如果成功了，一个re.sub就好了

文本为CLIENT_NET_API
BOOL
CALL_METHOD
CLIENT_QueryLog(LLONG
lLoginID, char * pLogBuffer, int
maxlen, int * nLogBufferlen, int
waittime = 3000);
正则表达式为(? <= CLIENT_NET_API).*(\s *= \s *[\d\w] *) +
我不要. * 所匹配到的内容，只想要第三步所匹配的内容，该如何改写正则表达式