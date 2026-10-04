# -*- coding: utf-8 -*-
"""项目根推导。**不要改成"从本文件往上数 N 层"。**

那种写法在本项目已经坑过一次：config/ 从 tools/ 挪到 native/codegen/ 之后，
`dirname x3` 少算一层，PROJECT 静默变成 native/，于是所有 SDK 路径整体错位，
而症状表现为"找不到 dhnetsdk.h" —— 报错信息与真因隔着两层，排查成本极高。
目录每挪一次就得记得改这里的数字，改漏了没有任何提示。

改成向上找锚点标记文件：只要项目根还在，codegen 挪到哪一层都不用改这里，
将来加厂商、拆仓库也不用动。它唯一的职责就是回答"项目根在哪"。
"""
import os

#: 项目根的标记文件。native/ 由 CMake 流程使用，必然存在。
_ANCHOR = os.path.join('native', 'CMakeLists.txt')


def _find_project_root(start):
    d = os.path.abspath(start)
    while True:
        if os.path.isfile(os.path.join(d, _ANCHOR)):
            return d
        parent = os.path.dirname(d)
        if parent == d:                      # 已到盘符根仍未命中
            raise RuntimeError('project root not found: no %s above %s'
                               % (_ANCHOR, start))
        d = parent


PROJECT = _find_project_root(os.path.dirname(os.path.abspath(__file__)))
