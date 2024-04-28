# 变更日志
## v1.1.0
四个sdk的错误代码不再是str，也不再是raise SDKException(errorIndex)，而是继承于Exception的子类，像这样raise NET_DVR_NOERROR


## v1.0.2
修复错误处理sdk函数返回数值类型的问题

## v1.0.1
修复大华playsdkException与海康playsdkException混淆的问题

## v1.0.1
支持大华异步下载回放
支持大华和海康playsdk的基本功能及catchPic


## v1.0.0
支持

        -大华，除基本登录登出等功能外
            -按照时间下载回放
                -同步
            -按照时间查找回放
                -同步
        -海康，除基本登录登出等功能外
            -按照时间下载回放
                -同步
                -异步
            -按照时间查找回放
                -同步
                -异步
            -调用GetLastError时将错误代码raise出来