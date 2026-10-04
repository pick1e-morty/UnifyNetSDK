#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""通用 SDK 绑定生成器入口：--sdk dahua|haikang。

把厂商差异收敛到 config/*.py，解析与生成逻辑在 common/ 里，通用且只写一份。

用法
----
    python tools/gen_bind.py --sdk dahua            # 全量生成
    python tools/gen_bind.py --sdk dahua --dry-run  # 只统计，不写文件
    python tools/gen_bind.py --sdk haikang --limit 3000
"""
import argparse
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from common import emit
from config import get_config


def main():
    ap = argparse.ArgumentParser(description='从厂商 SDK 头文件生成 nanobind 绑定代码')
    ap.add_argument('--sdk', choices=['dahua', 'haikang'], default='dahua',
                    help='目标 SDK（默认 dahua）')
    ap.add_argument('--fields-per-tu', type=int, default=500,
                    help='每个结构体分片的字段数上限（默认 500）')
    ap.add_argument('--enums-per-tu', type=int, default=250,
                    help='每个枚举分片的枚举数上限（默认 250）')
    ap.add_argument('--funcs-per-tu', type=int, default=200,
                    help='每个函数分片的函数数上限（默认 200）')
    ap.add_argument('--cbs-per-tu', type=int, default=30,
                    help='每个回调分片的回调数上限（默认 30）')
    ap.add_argument('--emit-selftest', action='store_true',
                    help='为每个回调额外生成 _selftest_fXxx(payload) 钩子，'
                         '从真正的 C++ 线程调用该 thunk。默认关闭：它只是验证'
                         '绑定层的过渡脚手架（ctypes 无法触发无 GIL 的线程路径），'
                         '功能验收应走真实 SDK 端到端')
    ap.add_argument('--limit', type=int, default=0,
                    help='只生成前 N 个字段（试编译用，0=全量）')
    ap.add_argument('--out-dir', default=None,
                    help='覆盖输出目录（默认用 config 里的 out_dir）')
    ap.add_argument('--dry-run', action='store_true', help='只统计，不写文件')
    args = ap.parse_args()

    cfg = get_config(args.sdk)
    return emit.generate(cfg, args)


if __name__ == '__main__':
    sys.exit(main())
