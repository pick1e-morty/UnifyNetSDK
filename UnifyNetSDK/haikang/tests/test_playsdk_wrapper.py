import time
from pathlib import Path

import UnifyNetSDK.haikang.playsdk.hk_playsdk_wrapper as playDll
from ctypes import *

nPort = c_long(0)
bFlag = bool(playDll.PlayM4_GetPort(byref(nPort)))
if bFlag is False:
    print("PlayM4_GetPort", playDll.PlayM4_GetLastError(nPort))
    exit(1)

bFlag = bool(playDll.PlayM4_SetJpegQuality(c_long(70)))  # 设置抓图质量为 jpeg，压缩70%
if bFlag is False:
    print("PlayM4_SetJpegQuality", playDll.PlayM4_GetLastError(nPort))
    exit(1)

videoName = create_string_buffer("test.mp4".encode("gbk"))
bFlag = bool(playDll.PlayM4_OpenFile(nPort, videoName))
if bFlag is False:
    print("PlayM4_OpenFile", playDll.PlayM4_GetLastError(nPort))
    exit(1)

# 开始播放文件
bFlag = bool(playDll.PlayM4_Play(nPort, None))
if bFlag is False:
    print("PlayM4_Play", playDll.PlayM4_GetLastError(nPort))
    exit(1)

time.sleep(0.1)

# // 获取当前视频文件的分辨率
dwWidth = c_long(0)
dwHeight = c_long(0)
bFlag = bool(playDll.PlayM4_GetPictureSize(nPort, byref(dwWidth), byref(dwHeight)))
if bFlag is False:
    print("PLAY_CatchPicEx", playDll.PlayM4_GetLastError(nPort))
    exit(1)

dwSize = dwWidth.value * dwHeight.value * 5  # 预计大小
m_pCapBuf = (c_ubyte * dwSize)()  # m_pCapBuf 是一个 c_ubyte 数组的实例，而不是一个指针。你可以直接传递 m_pCapBuf，因为 ctypes 会自动将数组转换为指针。
dwCapSize = c_ulong(0)  # [out] 获取到的实际JPEG图像数据大小

bFlag = bool(playDll.PlayM4_GetJPEG(nPort, m_pCapBuf, dwSize, byref(dwCapSize)))
if bFlag is False:
    print("PlayM4_GetJPEG", playDll.PlayM4_GetLastError(nPort))
    exit(1)

truely_buf = (c_ubyte * dwCapSize.value)()  # 真正需要用到的内存空间
memmove(truely_buf, m_pCapBuf, sizeof(truely_buf))  # 大数组内容移动到小数组中

absPath = Path(__file__).absolute()
picName = absPath.with_name("test.jpg")  # 源数据就是一帧jpeg，直接以二进制写入就能用图像查看器打开了
with open(picName, "wb") as f:
    f.write(truely_buf)

# 停止播放
bFlag = bool(playDll.PlayM4_Stop(nPort))
if bFlag is False:
    print("PlayM4_Stop", playDll.PlayM4_GetLastError(nPort))
    exit(1)
# 关闭文件
bFlag = bool(playDll.PlayM4_CloseFile(nPort))
if bFlag is False:
    print("PLAY_CloseFile", playDll.PlayM4_GetLastError(nPort))
    exit(1)

bFlag = bool(playDll.PlayM4_FreePort(nPort))
if bFlag is False:
    print("PlayM4_FreePort", playDll.PlayM4_GetLastError(nPort))
    exit(1)
