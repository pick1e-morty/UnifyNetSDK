# -*- coding: utf-8 -*-
"""大华 NetSDK 配置：纯数据 + 函数正则。无任何 hook（解析/生成直接用 common 默认实现）。"""
import os

from common.parse import make_func_re

PROJECT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

DAHUA = {
    'name': 'dahua',
    'header': os.path.join(PROJECT, 'dahua', 'C_Win64', 'Include', 'Common', 'dhnetsdk.h'),
    'out_dir': os.path.join(PROJECT, 'native', 'src', 'gen'),
    'module': 'unify_dh_gen',
    'include': '#include <dhnetsdk.h>',
    'file_prefix': 'dh_bind',
    'doc': 'auto-generated Dahua NetSDK binding (structs + enums)',
    # 头文件里声明了、但 dhnetsdk.dll 实际没导出的函数（链接报 LNK2019）。
    # 用 tools/check_exports.py 验证/更新。
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
