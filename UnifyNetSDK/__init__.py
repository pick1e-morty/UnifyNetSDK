
def DaHuaSDK():
    from .dahua import DaHuaSDK
    return DaHuaSDK()


# 在导入包时就会加载dll，如果仅使用一个sdk，就会造成极大的资源浪费，所以这里做了延迟导入

def HaiKangSDK():
    from .haikang import HaiKangSDK
    return HaiKangSDK()
