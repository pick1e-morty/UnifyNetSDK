
def DaHuaSDK():
    from .dahua import DaHuaSDK
    return DaHuaSDK()


# 在导入包时就会加载dll，如果仅使用一个sdk，就会造成极大的资源浪费，所以这里做了延迟导入

def HaiKangNetSDK():
    from .haikang.hk_netsdk import HaiKangNetSDK
    return HaiKangNetSDK()



# 海康
## 海康没有下载视频时的回调函数功能
## 查询录像是否存在还必须用另一个时间结构体NET_DVR_TIME_SEARCH_COND


# 大华
## 能通过时间查询的就这一个CLIENT_QueryRecordFile，且没有返回给我查找句柄，所以大华这边只能有sync了



# 海康还是大华来着，如果login时ip参数是127.0.0.1他居然不报错