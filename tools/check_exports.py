#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""对照 DLL 导出表，找出「头文件声明了但 DLL 没导出」的函数。

用途：
  1. 验证黑名单（cfg['skip_funcs']）是否准确、是否完整
  2. 升级 SDK 后重新发现未导出的函数，自动更新黑名单

原理：GetProcAddress 直接查导出表，不触发任何 SDK 初始化。

厂商无关：头文件路径、DLL 路径、探针函数、函数名正则全部来自
config/<sdk>.py。函数名用 common.parse.parse_funcs 提取（不自己写正则），
注释剥离也复用 common.parse.strip_comments。

    python tools/check_exports.py --sdk dahua
    python tools/check_exports.py --sdk haikang
"""
import argparse
import ctypes
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

from common import parse
from config import CONFIGS, get_config


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--sdk', required=True, choices=sorted(CONFIGS),
                    help='要检查的厂商')
    args = ap.parse_args()
    cfg = get_config(args.sdk)

    if not os.path.isfile(cfg['dll']):
        print('DLL 不存在: %s' % cfg['dll'])
        return 1

    dll = ctypes.WinDLL(cfg['dll'])
    k32 = ctypes.WinDLL('kernel32', use_last_error=True)
    GetProcAddress = k32.GetProcAddress
    GetProcAddress.restype = ctypes.c_void_p
    GetProcAddress.argtypes = [ctypes.c_void_p, ctypes.c_char_p]

    def has_export(name):
        return GetProcAddress(dll._handle, name.encode('ascii')) is not None

    print('=== [%s] 连通性对照（应全部已导出）===' % cfg['name'])
    ok = True
    for probe in cfg['probe_funcs']:
        hit = has_export(probe)
        ok = ok and hit
        print('  [%s] %s' % ('OK' if hit else 'FAIL', probe))
    if not ok:
        print()
        print('  探针都没命中：多半是 DLL 加载失败（缺依赖 / 32 位 dll），')
        print('  下面的"未导出"清单不可信，先解决加载问题。')
        return 1

    # 函数名提取走 common.parse，与生成器用的是同一套正则 —— 这里若与
    # 生成器不一致，黑名单就会和实际漏绑的函数对不上。
    text = parse.strip_comments(
        open(cfg['header'], encoding='latin-1', errors='replace').read())
    names = {f[0] for f in parse.parse_funcs(text, cfg['func_re'])}

    declared = set(cfg['skip_funcs'])
    missing = sorted(n for n in names if not has_export(n))
    print()
    print('[%s] 头文件声明 %d 个函数，未导出 %d 个：'
          % (cfg['name'], len(names), len(missing)))
    for n in missing:
        mark = ' (已在黑名单)' if n in declared else ''
        print('  %s%s' % (n, mark))

    stale = sorted(declared - set(missing))
    if stale:
        print()
        print('  黑名单里已不再缺失的 %d 个（可删）：%s'
              % (len(stale), ', '.join(stale)))
    if not declared:
        print()
        print('  cfg["skip_funcs"] 为空 —— 把上面 %d 个未导出的函数填进去，'
              % len(missing))
        print('  否则生成时会报 LNK2019。')
    return 0


if __name__ == '__main__':
    sys.exit(main())
