# -*- coding: utf-8 -*-
"""hkbind —— 海康 NetSDK 厚封装 wheel（第 3 层）。

**骨架**：与 dhbind 同构（加载胶水 + Client + errors 的文件布局一致），
但 Client 刻意留空 —— 海康侧"真实 SDK 线程登录"尚无可验证手段
（无模拟器，见 docs/testing-plan.md 第四节的选项 A/B/C）。
先写 Client 再补验证，正是"代码白写"的来源：等登录链路在哪条路上
验证通过后，照 dhbind.client 的结构落 hkbind.client。

_binding 由 `tools/fill_binding.py --sdk haikang` 填充（DLL 白名单
同样待登录跑通后回填）。
"""
__version__ = "1.0.0"
