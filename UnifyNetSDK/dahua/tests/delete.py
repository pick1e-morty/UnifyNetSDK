from ctypes import *

import UnifyNetSDK.haikang.hk_netsdk_wrapper as HK
from UnifyNetSDK.parameter import *

new_ntparg = UninfyNTPArg()
new_ntparg.enable = True
new_ntparg.domainOrIP = "ntp.aliyun.com"
new_ntparg.port = 123
new_ntparg.updateInterval = 60

lChannel = 0
dwOutBufferSize = sizeof(HK.NET_DVR_NTPPARA)
lpOutBuffer = HK.NET_DVR_NTPPARA()
lpOutBuffer.byEnableNTP = new_ntparg.enable

ba = bytearray(new_ntparg.domainOrIP.encode('utf-8'))
lpOutBuffer.sNTPServer = (c_ubyte * 64)(*ba)
print(ba, type(ba))
print(lpOutBuffer.sNTPServer, type(lpOutBuffer.sNTPServer))
# 将 c_ubyte_Array_64 对象转换为字符串
ntp_server_str = cast(lpOutBuffer.sNTPServer, c_char_p).value.decode()
for i in range(64):
    print(lpOutBuffer.sNTPServer[i], end='')
print()

# 打印字符串
print(ntp_server_str)

lpOutBuffer.wNtpPort = new_ntparg.port
lpOutBuffer.wInterval = new_ntparg.updateInterval

lpOutBuffer.cTimeDifferenceH = "8".encode('utf-8')  # 默认 东八区，正八
lpOutBuffer.cTimeDifferenceM = "0".encode('utf-8')

# b'\x08' b'\x00'


print(lpOutBuffer.cTimeDifferenceH, lpOutBuffer.cTimeDifferenceM)

# ntp.aliyun.com
# 1101161124697108105121117110469911110900000000000000000000000000000000000000000000000000
# 1101161124697108105121117110469911110900000000000000000000000000000000000000000000000000
# 10.30.9.2
# 4948465148465746500000000000000000000000000000000000000000000000000000000
