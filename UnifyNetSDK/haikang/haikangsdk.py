from ctypes import *
import os
import sys

from UnifyNetSDK.define import *
from UnifyNetSDK.haikang.ctypegen.full_headfile import *

# 结构体初始化会被赋值
# 默认应该都是0的形式，特别是bool
from loguru import logger

from glob_path import ProjectPath

logger.add(sys.stdout, level="DEBUG")


# cleanup
# logout还有login都是有返回值的
# 这些估计都要用assert

class HaiKangSDK(AbsNetSDK):
    objDll = None
    playctrlDll = None

    def __init__(self):
        self._loadLibrary()

    def init(cls):
        cls.objDll.NET_DVR_Init()

    # 对着大华的python写初始化，注意，不是复制大华，而是python端的高层抽象
    # 所以不要有那么大的功能要求和压力

    @classmethod
    def _loadLibrary(cls):
        WINDOWS_FLAG = True
        try:
            if WINDOWS_FLAG:
                libPath = ProjectPath / "UnifyNetSDK/haikang/lib/win"
                cls.objDll = CDLL(str(libPath / "HCNetSDK.dll"))  # 加载网络库
                cls.playctrlDll = CDLL(str(libPath / 'PlayCtrl.dll'))  # 加载播放库

                sdk_ComPath = NET_DVR_LOCAL_SDK_PATH()
                sdk_ComPath.sPath = str(libPath).encode("gbk")
                cls.objDll.NET_DVR_SetSDKInitCfg(2, byref(sdk_ComPath))
                libcryptoPath = str(libPath / "libcrypto-1_1-x64.dll").encode("gbk")
                cls.objDll.NET_DVR_SetSDKInitCfg(3, create_string_buffer(libcryptoPath))
                libsslPath = str(libPath / "libssl-1_1-x64.dll").encode("gbk")
                cls.objDll.NET_DVR_SetSDKInitCfg(4, create_string_buffer(libsslPath))

        except OSError as e:
            logger.error(f"动态库加载失败,原错误信息:{e}")
            # logger.exception(e)

    @classmethod
    def login(cls, login_arg: UnifyLoginArg):
        # 登录参数，包括设备地址、登录用户、密码等
        login_info = NET_DVR_USER_LOGIN_INFO()
        login_info.bUseAsynLogin = 0  # 同步通讯登录
        login_info.sDeviceAddress = login_arg.device_address.encode()
        login_info.wPort = login_arg.device_port
        login_info.sUserName = login_arg.user_name.encode()
        login_info.sPassword = login_arg.user_password.encode()
        print(login_info.bUseAsynLogin)

        # 设备信息, 输出参数
        device_info = NET_DVR_DEVICEINFO_V40()

        # 登录，
        userID = cls.objDll.NET_DVR_Login_V40(login_info, device_info)
        # TODO 注意检查设备信息是否被正确映射及正常打印
        print(cls.objDll.NET_DVR_GetLastError())
        print(device_info)
        return userID

    @classmethod
    def realPlay(cls):
        print(123)
        pass

    @classmethod
    def logout(cls, userID):
        cls.objDll.NET_DVR_Logout(userID)

    @classmethod
    def cleanup(cls):
        cls.objDll.NET_DVR_Cleanup()


if __name__ == "__main__":
    pass