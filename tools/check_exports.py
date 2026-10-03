#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""检查 dhnetsdk.dll 的导出表，找出「头文件声明了但 DLL 没导出」的函数。

用途：
  1. 验证黑名单（SKIP_FUNCS）是否准确、是否完整
  2. 升级 SDK 后重新发现未导出的函数，自动更新黑名单

原理：GetProcAddress 直接查导出表，不触发任何 SDK 初始化。
"""
import ctypes
import re
import sys

DLL = r'C:\Users\Hast\Documents\CodeProjects\UnifyNetSDK\dahua\C_Win64\Bin\dhnetsdk.dll'
HEADER = r'C:\Users\Hast\Documents\CodeProjects\UnifyNetSDK\dahua\C_Win64\Include\Common\dhnetsdk.h'


def main():
    dll = ctypes.WinDLL(DLL)
    k32 = ctypes.WinDLL('kernel32', use_last_error=True)
    GetProcAddress = k32.GetProcAddress
    GetProcAddress.restype = ctypes.c_void_p
    GetProcAddress.argtypes = [ctypes.c_void_p, ctypes.c_char_p]

    def has_export(name):
        return GetProcAddress(dll._handle, name.encode('ascii')) is not None

    print('=== 对照（应全部已导出）===')
    for probe in ('CLIENT_Init', 'CLIENT_Login', 'CLIENT_Cleanup', 'CLIENT_GetLastError'):
        print('  [%s] %s' % ('OK' if has_export(probe) else 'FAIL', probe))

    text = open(HEADER, encoding='latin-1', errors='replace').read()
    text = re.sub(r'/\*.*?\*/', ' ', text, flags=re.S)
    text = re.sub(r'//[^\n]*', ' ', text)
    names = set(re.findall(
        r'CLIENT_NET_API\s+[A-Za-z_][\w\s*]*?\s+CALL_METHOD\s+(CLIENT_\w+)\s*\(', text))

    missing = sorted(n for n in names if not has_export(n))
    print()
    print('头文件声明 %d 个 CLIENT_ 函数，未导出 %d 个：' % (len(names), len(missing)))
    for n in missing:
        print('  ', n)
    return 0


if __name__ == '__main__':
    sys.exit(main())
