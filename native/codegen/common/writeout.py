# -*- coding: utf-8 -*-
"""生成产物的落盘工具：write_if_changed。

从 emit.py 挪出成独立模块：emit.py（IR -> C++ 分片）与 emit_stub.py
（IR -> .pyi 存根）都要用它。挪出来的动机是依赖方向 —— emit 调 emit_stub
时若 emit_stub 再回头 import emit 取这个函数，就成环；抽成叶子模块后
依赖保持单向：emit -> writeout <- emit_stub。
"""
import os


def write_if_changed(path, text):
    """内容不变就不写文件，避免 mtime 变化导致 ninja 无谓重编整个分片。

    同时强制 ASCII：生成物是给 MSVC 读的，非 ASCII 会触发 C4819；而
    `open(..., 'w', encoding='ascii')` 是写到第一个非 ASCII 字符时才抛
    UnicodeEncodeError，报错里完全看不出是哪句注释写的。
    """
    try:
        text.encode('ascii')
    except UnicodeEncodeError as e:
        bad = text[max(0, e.start - 60):e.start + 60]
        raise ValueError(
            '生成内容含非 ASCII 字符（写入 %s 会因此崩溃）。\n'
            '  位置: %r\n  上下文: ...%s...\n'
            '  生成代码里的注释必须用 ASCII；中文说明请留在 Python 侧 docstring。'
            % (os.path.basename(path), e.start, bad.replace('\n', '\\n')))
    if os.path.isfile(path):
        try:
            with open(path, 'r', encoding='ascii', errors='replace') as f:
                if f.read() == text:
                    return False
        except OSError:
            pass
    with open(path, 'w', encoding='ascii') as f:
        f.write(text)
    return True
