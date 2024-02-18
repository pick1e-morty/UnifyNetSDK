# 在导入包时就会加载dll，如果仅使用一个sdk，就会造成极大的资源浪费，所以这里做了延迟导入
# 默认是直接加载大华的两个sdk及exception，因为在我们这些子公司里大华设备是居多的。


def DaHuaNetSDK():
    from UnifyNetSDK.dahua.dh_netsdk import DaHuaNetSDK
    return DaHuaNetSDK


def DHNetSDKException():
    from UnifyNetSDK.dahua.dh_netsdk_exception import DHNetSDKException
    return DHNetSDKException


def DaHuaPlaySDK():
    from UnifyNetSDK.dahua.dh_playsdk import DaHuaPlaySDK
    return DaHuaPlaySDK


def DHPlaySDKException():
    from UnifyNetSDK.dahua.dh_playsdk_exception import DHPlaySDKException
    return DHPlaySDKException


def HaikangNetSDK():
    from .haikang.hk_netsdk import HaikangNetSDK
    return HaikangNetSDK()


def HKNetSDKException():
    from .haikang.hk_netsdk_exception import HKNetSDKException
    return HKNetSDKException()


def HaikangPlaySDK():
    from .haikang.hk_playsdk import HaikangPlaySDK
    return HaikangPlaySDK()


def HKPlaySDKException():
    from .haikang.hk_playsdk_exception import HKPlaySDKException
    return HKPlaySDKException()
# 海康
## 海康没有下载视频时的回调函数功能
## 查询录像是否存在还必须用另一个时间结构体NET_DVR_TIME_SEARCH_COND


# 大华
## 能通过时间查询的就这一个CLIENT_QueryRecordFile，且没有返回给我查找句柄，所以大华这边只能有sync了


# 海康还是大华来着，如果login时ip参数是127.0.0.1他居然不报错
