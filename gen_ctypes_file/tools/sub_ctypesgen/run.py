#!/usr/bin/env python3

import sys
import os

# ensure that we can load the ctypesgen library
THIS_DIR = os.path.dirname(__file__)
sys.path.insert(0, THIS_DIR)

from ctypesgen.__main__ import main  # noqa: E402

if __name__ == "__main__":
    main()

# python run.py DH_NetSDK.h -o DH.py


# python run.py --cpp "cl /E" DH_NetSDK.h -o DH.py
# cl指令手册，预处理器节点https://learn.microsoft.com/zh-cn/cpp/build/reference/compiler-options-listed-by-category?view=msvc-170#preprocessor
# 是cl需要找头文件，所以不用对ctypesgen使用-I参数

# python .\run.py -o test.py -l dahua/Libs/win64/dhnetsdk.dll DH_NetSDK.h
