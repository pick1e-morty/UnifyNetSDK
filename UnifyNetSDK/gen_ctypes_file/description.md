# 包装器生成说明

## 整体流程(文件夹说明)

1. original
源文件
2. formatted
   2.1 首先使用clang-format进行代码格式化， 风格的说明在UnifyNetSDK/gen_ctypes_file/tools/clang_format/format.py的clangformat函数中
   2.2 然后就是删除注释包括单行多行换行注释及空行sanitizeText_xxx，注意删除注释这步是修改formatted下的本身文件的
3. replace
   经过前面两步后头文件相较于original就会非常整洁干净，然后就需要我们手动进行一些单个头文件所特有的手动处理了
4. completed
   无论需不需要手动处理，最终ctypesgen都会读取replace文件夹下的头文件，并生成在completed文件夹下。

## 大华头文件特有的ctypesgen修复方式

有三种走法

- 使用cl编译器正常走向，但是当我尝试使用ctypesgen --cpp "cl -E" 后发现两个头文件都失败了。有个大哥遇到了和我相同的问题，并准备提交pull request！ISSUES地址：https://github.com/ctypesgen/ctypesgen/issues/179
- 使用gcc编译器强制走向只有vs平台才能通过的预处理宏判断_MSC_VER分支，不过我很快就被变量类型的声明给打败了。

### **(目前使用)** 使用gcc编译器走向non windows分支，并成功修补绝大部分错误。下面就是着重介绍我所遇到的问题及解决方式

#### 解决方式整合（这是让我自己看的）

      添加
      #include <stdbool.h>
      替换
      # non windows分支下的语句替换
      #define CLIENT_NET_API extern "C"  替换为  #define CLIENT_NET_API __declspec(dllimport)  
      #define LPDWORD DWORD*  替换为  #define LPDWORD unsigned int*
      #define LLONG long  替换为  #define LLONG long long



#### Q: UnifyNetSDK.dahua.dh_exception.DHException: (4, 'NET_INVALID_HANDLE')
A: 这是变量类型不符合所导致的问题，
猜想：dll那边检测到我是win64平台，所以登录函数返回的是LLONG：c_longlong，而我使用的non windows分支的定义是#define LLONG long
所以改为non windows分支改为#define LLONG longlong就能解决目前这个问题


#### Q: bool未定义

```C
    // ctypesgen错误代码
    ERROR: Typedef "NET_CFG_SIZEFILTER_INFO" depends on an unknown typedef "bool". Typedef "NET_CFG_SIZEFILTER_INFO" will not be output
    // 源代码
    typedef struct tagNET_CFG_SIZEFILTER_INFO
    {
        int nCalibrateBoxNum;                           
        NET_CFG_CALIBRATEBOX_INFO stuCalibrateBoxs[10]; 
        bool bMeasureModeEnable;                        
        BYTE bMeasureMode;   
```

A: 在C++中，"bool"类型是标准库的一部分，所以不需要额外定义。既然他说未定义，那就定义一下 ** #include <stdbool.h> **

#### Q: 语法错误 =

```C
   // ctypesgen错误代码
   ERROR: C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_NetSDK.h:56828: Syntax error at '='
   // DH_NetSDK.h:56828上下行源代码
   CLIENT_NET_API LLONG CALL_METHOD CLIENT_DownloadByTimeEx(LLONG lLoginID, int nChannelId, int nRecordFileType, LPNET_TIME tmStart, LPNET_TIME tmEnd, char* sSavedFileName,
                                                         fTimeDownLoadPosCallBack cbTimeDownLoadPos, LDWORD dwUserData,
                                                         fDataCallBack fDownLoadDataCallBack, LDWORD dwDataUser, void* pReserved = NULL);
```

A: 我发现不带默认参数的CLIENT_DownloadByTime(没有EX)
转换成功了，而两者在语法上的差异也很明显就是被标注出的=，也就是指默认参数。我写了remove_default_parameters脚本用正则删除所有函数声明中的默认参数。

#### Q:语法错误 ”C“

```C
   // ctypesgen错误代码
   ERROR: C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_NetSDK.h:56831: Syntax error at 'C'
   // DH_NetSDK.h:56831行源代码
   CLIENT_NET_API BOOL CALL_METHOD CLIENT_StopDownload(LLONG lFileHandle);
```

A: 很明显这个语句中没有单独存在的字符”C“，但是ctypesgen却这样报错了，在之前就研究预处理宏判断分支走向时就发现

```C
// 部分预处理语句
#if (defined(_MSC_VER)) # vs平台自动定义的一个宏
    #include <windows.h>
    #ifdef NETSDK_EXPORTS                          # 大华的人内部编译的走向
        #if (defined(_WIN64) || defined(WIN64))
            #define CLIENT_NET_API
        #else
            #define CLIENT_NET_API __declspec(dllexport)
        #endif
    #else
        #define CLIENT_NET_API __declspec(dllimport)     # windows平台真正应该用的导入方式
    #endif
#else    # non windows
    #define CLIENT_NET_API extern "C"
#endif    
```   

而我现在刚好是non windows预处理分支，对应上了。但其实我是windows平台的，所以直接将CLIENT_NET_API替换为了__declspec(dllimport)。

#### Q: 宏文本替换失败

```C
// ctypesgen错误代码
WARNING: Could not parse macro "#define LPDWORD DWORD *"
ERROR: C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_NetSDK.h:44: Syntax error at '\n'
```

用了LPDWORD的就两行

      58100源代码：CLIENT_GetPlatFormInfo：CLIENT_NET_API BOOL CALL_METHOD CLIENT_GetPlatFormInfo(LLONG lLoginID, DWORD dwCommand, int nSubCommand, int nParam, LPVOID lpOutBuffer, DWORD dwOutBufferSize,
      LPDWORD lpBytesReturned, int waittime);
      58038源代码：CLIENT_NET_API BOOL CALL_METHOD CLIENT_GetDevConfig(LLONG lLoginID, DWORD dwCommand, LONG lChannel, LPVOID lpOutBuffer, DWORD dwOutBufferSize, LPDWORD lpBytesReturned, int waittime);

“简单”的文本替换ctypesgen作者说过:做不到。
#define LPDWORD DWORD *
DWORD是unsigned int，最终改为#define LPDWORD unsigned int *

#### Q:其他一些暂不处理或者无关紧要的错误及警告

```
1
WARNING: Macro "CLIENT_NET_API" depends on an unknown identifier "dllimport". Macro "CLIENT_NET_API" will not be output
警告，实际测试函数执行结果无影响。

2
ERROR: <built-in>:0: Syntax error at '\n'
ERROR: <built-in>:0: Syntax error at '\n'
ERROR: <built-in>:0: Syntax error at '\n'
ERROR: <built-in>:0: Syntax error at '\n'
ERROR: <built-in>:0: Syntax error at '\n'
ERROR: <built-in>:0: Syntax error at '\n'
ERROR: <built-in>:0: Syntax error at '\n'
ERROR: <built-in>:0: Syntax error at '\n'
毫无价值的报错信息
WARNING: Could not parse macro "#define __declspec(x) __attribute__ ( ( x ) )"
头文件中搜不到__declspec(x)和__attribute__，搞不懂。



3
WARNING: Macro "nEncoderID" depends on an unknown identifier "nDecoderID". Macro "nEncoderID" will not be output
WARNING: Macro "byEncoderID" depends on an unknown identifier "byDecoderID". Macro "byEncoderID" will not be output
58212源代码：typedef void(CALLBACK* fDecPlayBackPosCallBack)(LLONG lLoginID, int nEncoderID, DWORD dwTotalSize, DWORD dwPlaySize, LDWORD dwUser);
“简单”的文本替换ctypesgen作者说过:做不到。
只有nEncoderID被使用上了，而byEncoderID在整个头文件就只出现了一次，这可能需要和其他动态链接库及头文件一起使用的吧？
无所谓，因为ctypesgen转换的回调函数声明根本没带参数名字。看一下ctypesgen转换后的fDecPlayBackPosCallBack是这样的
fDecPlayBackPosCallBack = CFUNCTYPE(UNCHECKED(None), c_long, c_int, c_uint, c_uint, c_long)

4
56310源代码：typedef void(CALLBACK* fSubLogDataCallBack)(LLONG lLogHandle, NET_EM_LOG_QUERY_TYPE emLogType, const DH_DEVICE_LOG_ITEM_EX* pstuLogData, const int& nCount, LDWORD dwUser, void* reserved);
ERROR: C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_NetSDK.h:56310: Syntax error at '&'
ERROR: C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_NetSDK.h:56310: Syntax error at 'void'
估计是ctypesgen还不能处理引用传递符号&和。

5
57183源代码：CLIENT_NET_API void CALL_METHOD CLIENT_SetSubscribeLogCallBack(fSubLogDataCallBack pLogDataCB, LDWORD dwUser);
ERROR: C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\DH_NetSDK.h:57183: Syntax error at 'pLogDataCB'
上面那个回调函数的定义转换失败，直接导致使用该回调函数作为参数类型的函数声明也报错了。
```


## 海康头文件特有的ctypesgen修复方式


#### Q: 语法错误 =

```C
   // ctypesgen错误代码
   ERROR: C:\\Users\\Administrator\\Documents\\CodeProject\\headfile\\UnifyNetSDK\\gen_ctypes_file\\_3_replace\\HK_NetSDK.h:42860: Syntax error at '='
   // HK_NetSDK.h:42860上下行源代码
   NET_DVR_API char* __stdcall NET_DVR_GetErrorMsg(LONG* pErrorNo = NULL);
```

A: 依旧是默认参数的问题，删除默认参数的函数名是remove_default_parameters