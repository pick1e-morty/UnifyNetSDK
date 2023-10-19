from UnifyNetSDK.define import UnifyLoginArg
from UnifyNetSDK.haikang.haikangsdk import HaiKangSDK

def test_login():
    easy_login_info = UnifyLoginArg()
    easy_login_info.user_name = "admin"
    easy_login_info.user_password = "zzfb450000"
    easy_login_info.device_port = 8000
    easy_login_info.device_address = "10.200.15.41"

    hk_client = HaiKangSDK()
    hk_client.init()
    userID = hk_client.login(easy_login_info)
    print(userID)
    hk_client.logout(userID)

    hk_client.cleanup()

def test_loadLibrary():
    hk_client = HaiKangSDK()
    hk_client.init()

    hk_client.cleanup()

if __name__ == "__main__":
    test_login()