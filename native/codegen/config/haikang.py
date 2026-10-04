# -*- coding: utf-8 -*-
"""海康 NetSDK 配置：纯数据 + 函数正则。

与 dahua 的差异都在数据层：
  - 头文件/输出目录/模块名/前缀不同
  - 函数声明里调用约定三种混用（__stdcall / CALLBACK / WINAPI）
  - 结构体大量含嵌套 union/struct（common 已用平衡花括号 + _scan_body 递归
    统一处理：嵌套匿名 union 成员提升、有名块按 bytes 暴露）

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

from common.parse import make_func_re, strip_inactive_branches

from .paths import PROJECT

HAIKANG = {
    'name': 'haikang',
    # SDK 源目录（vendor 原始包，只读）。注意"头文件"/"库文件"是中文 ——
    # MSVC 编译能过（内部走 Unicode），但 CMake 的 message() 会打印乱码、
    # bat 里传中文路径会让 dumpbin 之类工具直接失败。所以统一复制到 sdk_dir。
    'sdk_src': {
        'include': os.path.join(PROJECT, 'vendor', 'haikang', 'HCNetSDK_Win64',
                                'HCNetSDKV6.1.11.30_build20260805_Win64_ZH',
                                '头文件'),
        'lib': os.path.join(PROJECT, 'vendor', 'haikang', 'HCNetSDK_Win64',
                            'HCNetSDKV6.1.11.30_build20260805_Win64_ZH',
                            '库文件'),
        'bin': os.path.join(PROJECT, 'vendor', 'haikang', 'HCNetSDK_Win64',
                            'HCNetSDKV6.1.11.30_build20260805_Win64_ZH',
                            '库文件'),
    },
    # SDK 副本：与 config/dahua.py 完全同构 —— vendor/<厂商>/sdk_win64/{include,lib,bin}。
    # 两边结构对不齐，后来的人就得猜哪个是有意的，所以哪怕大华原本就是纯 ASCII，
    # 也一起走这个布局。用 tools/sync_sdk.py 同步。
    'sdk_dir': os.path.join(PROJECT, 'vendor', 'haikang', 'sdk_win64'),
    'header': os.path.join(PROJECT, 'vendor', 'haikang', 'sdk_win64', 'include',
                           'HCNetSDK.h'),
    'dll': os.path.join(PROJECT, 'vendor', 'haikang', 'sdk_win64', 'bin', 'HCNetSDK.dll'),
    'lib_dir': os.path.join(PROJECT, 'vendor', 'haikang', 'sdk_win64', 'lib'),
    'include_dir': os.path.join(PROJECT, 'vendor', 'haikang', 'sdk_win64', 'include'),
    'bin_dir': os.path.join(PROJECT, 'vendor', 'haikang', 'sdk_win64', 'bin'),
    # 产物目录与 config/dahua.py 同一套命名规则：gen_<厂商缩写>，
    # 与 file_prefix（hk_bind_*）、module（unify_hk_gen）保持一致。
    'out_dir': os.path.join(PROJECT, 'native', 'src', 'gen_hk'),
    # pyd 的构建输出目录：emit_stub 会把 {module}.pyi 再放一份到这里
    # （与 dahua 同构；目录不存在时静默跳过）。
    'build_dir': os.path.join(PROJECT, 'native', 'build'),
    'module': 'unify_hk_gen',
    'include': '#include <HCNetSDK.h>',
    'file_prefix': 'hk_bind',
    'doc': 'auto-generated Hikvision NetSDK binding (structs + enums)',
    # cb_qty_pred / cb_count_pred **故意不设** —— 见模块 docstring。
    #
    # text_filters：裁掉非活动的条件编译分支。海康头文件把 DC / INITINFO 等
    # 类型放在 `#if defined(__linux__)` 里，Windows 下不存在，绑定它们会报
    # C2653 "不是类或命名空间名称"，是 121 处编译错误的主因。
    #
    # 开启前踩过一个很隐蔽的坑，务必留意：裁剪本身是对的（Windows 下这些基础
    # 类型由 windows.h 提供），但**白名单一度依赖"头文件里写了哪些 typedef"**，
    # 而 DWORD / BYTE / LONG 这些别名恰好就住在 Linux 分支里。裁掉之后白名单
    # 断裂，所有 DWORD 字段被判未知类型，结构体因提不出字段被整体跳过 ——
    # 海康字段从 18635 掉到 3225（-82.7%），而**编译错误数反而下降**，
    # 看起来像"修好了"。修法是把 Windows SDK 的整数别名显式列进
    # common.parse.BASE_TYPES（它们来自 windows.h，不是厂商知识）。
    #
    # parse.parse_header 里有自检：裁剪导致可提取字段数下跌超过 10% 就直接
    # 抛异常中止，不让残缺的绑定被静默生成。当前实测 -0.2%，健康。
    'text_filters': [strip_inactive_branches],
    # check_exports.py 的连通性探针（确认 GetProcAddress 查得到，
    # 否则"全部未导出"会是 DLL 加载失败的假象）。
    'probe_funcs': ('NET_DVR_Init', 'NET_DVR_Login_V30', 'NET_DVR_Cleanup',
                    'NET_DVR_GetLastError'),
    # 头文件声明了但 HCNetSDK.dll 未导出（native/codegen/check_exports.py --sdk haikang
    # 实测 789 声明 / 4 缺失）。不填会 LNK2019。
    'skip_funcs': {
        'NET_DVR_GetAirCondition',
        'NET_DVR_GetMatrixPuChan',
        'NET_DVR_Login_Check',
        'NET_DVR_StopPlayDirect',
    },
}
HAIKANG['func_re'] = make_func_re('NET_DVR_API', '(?:__stdcall|CALLBACK|WINAPI)', 'NET_DVR_')
