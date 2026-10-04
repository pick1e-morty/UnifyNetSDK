# -*- coding: utf-8 -*-
"""大华 NetSDK 配置：数据 + 厂商专属经验规则。

**这里放"只有大华成立"的语义知识**。common/ 只负责 C 语法，不猜参数含义。
下面两条钩子是从大华 289 个回调里统计出来的，改动前请先读
docs/implementation-notes.md 第四节。
"""
import os
import re

from common.parse import make_func_re

PROJECT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# ---------------------------------------------------------------- 大华专属钩子
#
# 1) 哪些整型参数名算「数量/长度」。**必须靠参数名，不能靠"指针后面跟个整数"**：
#    289 个回调里 150 个形如 (NET_X *pInfo, LDWORD dwUser) —— 那个整数是注册时
#    传给 SDK 的用户数据，不是数量。按位置判断会把 150 个全误判成数组。
_NOT_QTY_NAME = re.compile(
    r'(user|error|err|reserved|flag|type|state|reason|code|index|handle|status|port|channel)', re.I)
#
# 2) 数量/长度关键词**必须 $ 锚定在名字末尾**，不能子串搜索：
#    'nFileNum' 的第 4~6 字符是 l/e/N，忽略大小写正好凑出 "leN" 命中 `len`，
#    于是 COUNT 命中、LEN 也命中，is_count 被否 —— fQueryRecordFileCallBack 的数组
#    语义就丢了。末尾锚定后 nInfoNum / nBufLen / dwBufSize / nItemCount 仍正确。
_QTY_NAME = re.compile(r'(num|count|size|len|length)$', re.I)
#
# 3) Num/Count = 元素个数（-> list）；Len/Size = **sizeof 字节长度**（-> 单对象）。
#    后者按数组处理会越界读，实证：
#      fAddFileStateCB(..., NET_CB_ADDFILESTATE *pBuf, int nBufLen)   单结构体+字节长度
#      fNotifyCarPassInfo(..., NET_CAR_PASS_INFO *p, int nInfoNum)     数组+元素个数
_COUNT_NAME = re.compile(r'(num|count)$', re.I)
_LEN_NAME = re.compile(r'(len|size)$', re.I)


def dahua_qty_pred(name):
    """整型参数名是否表示数量/长度（用于 BYTE* 取缓冲区长度）。"""
    return bool(name) and not _NOT_QTY_NAME.search(name) and bool(_QTY_NAME.search(name))


def dahua_count_pred(name):
    """整型参数名是否表示**元素个数**（决定结构体指针给 list 还是单对象）。"""
    return bool(name) and bool(_COUNT_NAME.search(name)) and not _LEN_NAME.search(name)


DAHUA = {
    'name': 'dahua',
    # SDK 源目录（vendor 原始包，只读）。tools/sync_sdk.py 从这里复制到 sdk_dir。
    'sdk_src': {
        'include': os.path.join(PROJECT, 'dahua', 'C_Win64', 'Include', 'Common'),
        'lib': os.path.join(PROJECT, 'dahua', 'C_Win64', 'Lib', 'Win64'),
        'bin': os.path.join(PROJECT, 'dahua', 'C_Win64', 'Bin'),
    },
    # SDK 副本：统一到 <厂商>/sdk_win64/{include,lib,bin}，全 ASCII 路径。
    # 大华原始路径本来已是纯 ASCII，但为了与海康结构一致（海康的"头文件"/"库文件"
    # 是中文，MSVC/batch/dumpbin 处理不可靠），两边一起走这个布局 ——
    # 结构对不齐，后来的人就得猜哪个是有意的。改用 tools/sync_sdk.py 同步。
    'sdk_dir': os.path.join(PROJECT, 'dahua', 'sdk_win64'),
    # 编译与运行都指向副本，不再直接引用 vendor 原始目录。
    'header': os.path.join(PROJECT, 'dahua', 'sdk_win64', 'include', 'dhnetsdk.h'),
    'dll': os.path.join(PROJECT, 'dahua', 'sdk_win64', 'bin', 'dhnetsdk.dll'),
    'lib_dir': os.path.join(PROJECT, 'dahua', 'sdk_win64', 'lib'),
    'include_dir': os.path.join(PROJECT, 'dahua', 'sdk_win64', 'include'),
    'bin_dir': os.path.join(PROJECT, 'dahua', 'sdk_win64', 'bin'),
    # 产物目录带厂商缩写，与 file_prefix / module 保持同一套命名：
    #   gen_dh  / dh_bind_*  / unify_dh_gen
    # 早先是裸 'gen'，靠"先建大华所以没后缀"的历史原因，结果 gen 与 gen_hk
    # 只差两个字母，肉眼极易看串（build.ps1 至今还在为此发提示）。第三方厂商
    # 接入时更会歧义：gen 到底指谁。
    'out_dir': os.path.join(PROJECT, 'native', 'src', 'gen_dh'),
    'module': 'unify_dh_gen',
    'include': '#include <dhnetsdk.h>',
    'file_prefix': 'dh_bind',
    'doc': 'auto-generated Dahua NetSDK binding (structs + enums)',
    # 回调参数语义钩子（见上）。common/classify_cb_params 用它们判断
    # 「紧邻的整型是数量还是错误码」。**大华的规律不适用于海康**，
    # 所以它们属于本文件而不是 common/。
    # cb_qty_pred / cb_count_pred 见文件顶部说明。
    'cb_qty_pred': dahua_qty_pred,
    'cb_count_pred': dahua_count_pred,
    # 头文件预处理过滤器（parse.load_header 的钩子）。大华**不需要**裁剪条件
    # 编译分支：25 个 #if 里没有 Linux/POSIX 专属块，那些条件（如
    # _WIN64、__cplusplus、DHNETSDK_H）在 Windows 下本就为真。
    'text_filters': [],
    # check_exports.py 的连通性探针：随便几个必然已导出的函数，用来确认
    # GetProcAddress 查得到（否则"全部未导出"是 DLL 加载失败的假象）。
    'probe_funcs': ('CLIENT_Init', 'CLIENT_Login', 'CLIENT_Cleanup',
                    'CLIENT_GetLastError'),
    # 头文件里声明了、但 dhnetsdk.dll 实际没导出的函数（链接报 LNK2019）。
    # 用 tools/check_exports.py --sdk dahua 验证/更新。
    'skip_funcs': {
        'CLIENT_GetSecurityEncryptInfo',
        'CLIENT_DelayReboot',
        'CLIENT_InitDevGetLocalityConfig',
        'CLIENT_PTZSetLockupStatus',
        'CLIENT_SetTemporaryConfig',
        'CLIENT_ModifyBroadcastPlan',
    },
}
DAHUA['func_re'] = make_func_re('CLIENT_NET_API', 'CALL_METHOD', 'CLIENT_')
