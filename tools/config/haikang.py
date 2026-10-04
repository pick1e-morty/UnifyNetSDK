# -*- coding: utf-8 -*-
"""海康 NetSDK 配置：纯数据 + 函数正则。

与 dahua 的差异都在数据层：
  - 头文件/输出目录/模块名/前缀不同
  - 函数声明里调用约定三种混用（__stdcall / CALLBACK / WINAPI）
  - 结构体有 42 个含嵌套 union/struct（common 的扁平解析会跳过，待 hook）

**回调参数语义钩子：故意留空。**
common/classify_cb_params 在没有钩子时保守退化——BYTE* 只给地址、结构体指针
只给单对象、不产出 list。这是有意的：海康 26 个回调的命名风格与大华完全不同
（REALDATACALLBACK / MSGCallBack / DVCS_UPGRADESTATE_CB / _CB 后缀，没有统一的
fXxx 前缀），大华那套"靠参数名猜数量"的规律照搬过来只会误判。
等真跑通海康 SDK、拿到实际回调行为后再照事实写规则，那时才是"我们吃苦"。
少给可接受，给错无法排查。

尚未填 skip_funcs：等 check_exports.py 扫出 HCNetSDK.dll 未导出函数后填入。
"""
import os

from common.parse import make_func_re

PROJECT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

HAIKANG = {
    'name': 'haikang',
    'header': os.path.join(PROJECT, 'haikang', 'HCNetSDK_Win64',
                          'HCNetSDKV6.1.11.30_build20260805_Win64_ZH',
                          '头文件', 'HCNetSDK.h'),
    'dll': os.path.join(PROJECT, 'haikang', 'HCNetSDK_Win64',
                        'HCNetSDKV6.1.11.30_build20260805_Win64_ZH',
                        '库文件', 'HCNetSDK.dll'),
    'out_dir': os.path.join(PROJECT, 'native', 'src', 'gen_hk'),
    'module': 'unify_hk_gen',
    'include': '#include <HCNetSDK.h>',
    'file_prefix': 'hk_bind',
    'doc': 'auto-generated Hikvision NetSDK binding (structs + enums)',
    # cb_qty_pred / cb_count_pred **故意不设** —— 见模块 docstring。
    'probe_funcs': ('NET_DVR_Init', 'NET_DVR_Login_V30', 'NET_DVR_Cleanup',
                    'NET_DVR_GetLastError'),
    # 头文件声明了但 HCNetSDK.dll 未导出（tools/check_exports.py --sdk haikang
    # 实测 789 声明 / 4 缺失）。不填会 LNK2019。
    'skip_funcs': {
        'NET_DVR_GetAirCondition',
        'NET_DVR_GetMatrixPuChan',
        'NET_DVR_Login_Check',
        'NET_DVR_StopPlayDirect',
    },
}
HAIKANG['func_re'] = make_func_re('NET_DVR_API', '(?:__stdcall|CALLBACK|WINAPI)', 'NET_DVR_')
