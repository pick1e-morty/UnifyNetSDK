# -*- coding: utf-8 -*-
"""海康 NetSDK 配置：纯数据 + 函数正则。

与 dahua 的差异都在数据层：
  - 头文件/输出目录/模块名/前缀不同
  - 函数声明里调用约定三种混用（__stdcall / CALLBACK / WINAPI）
  - 结构体有 42 个含嵌套 union/struct（common 的扁平解析会跳过，待 hook）

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
    'out_dir': os.path.join(PROJECT, 'native', 'src', 'gen_hk'),
    'module': 'unify_hk_gen',
    'include': '#include <HCNetSDK.h>',
    'file_prefix': 'hk_bind',
    'doc': 'auto-generated Hikvision NetSDK binding (structs + enums)',
    'skip_funcs': set(),
}
HAIKANG['func_re'] = make_func_re('NET_DVR_API', '(?:__stdcall|CALLBACK|WINAPI)', 'NET_DVR_')
