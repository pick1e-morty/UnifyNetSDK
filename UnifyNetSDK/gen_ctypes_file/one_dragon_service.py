# python调用clang-format.exe格式化C++代码
import re
from pathlib import Path
from UnifyNetSDK.gen_ctypes_file.tools.clang_format.format import clangformat

from UnifyNetSDK.gen_ctypes_file.tools.sub_ctypesgen.run import main as ctypesgenscript

"""
在进行脚本操作前我修改了两个源头文件内容
1.编码转换为UTF-8,因为clang-format不支持我这两个头文件的gb2312
2.在HK_NetSDK.h文件中14272行的LPBEHAVIOR_PRISON_MODE_TYPE前面添加一个*符号，很明显这是一个枚举指针，不过原作者忘了加了
"""


# 现在还没有验证这个做法是正确的3.在DH_NetSDK.h文件第一行插入一句#include <stdbool.h>。解决跟bool有联系的结构体无法转换的问题

# TODO，海康那边还没加这个库
# 但其实这是我用错了编译器的原因对吧，只要我换成g++，问题就不存在了，一定是这样的！


# 正则删除注释和空行
def delete_comment_and_emptyline(orgText):
    # 用正则删除三种注释
    # 1.多行注释 /* */                      2.单行注释 // 用了换行符 \        3.单行注释 //
    # (/*(.|\r\n|\n)*?\*/)        |        (//(.*\\\n)+.*)        |         (//.*)
    pattern = r"(/\*(.|\r\n|\n)*?\*/)|(\/\/(.*\\\n)+.*)|(\/\/.*)"
    processedText1 = re.sub(pattern, "", orgText, flags=re.M)
    # 正则删除所有空行
    pattern = "^\\s*(?=\r?$)\n"  # 这句是从网上“学习”来的，我也不知道怎么写的这么奇怪
    processedText2 = re.sub(pattern, "", processedText1, flags=re.M)
    return processedText2


curPyPath = Path(__file__).parent


# clang格式化
def clangformat_dahua():
    print("clangformat_dahua开始")
    dh_org_headfile_path = str(curPyPath / "_1_original/DH_NetSDK.h")
    dh_fod_headfile_path = str(curPyPath / "_2_formatted/DH_NetSDK.h")
    clangformat(dh_org_headfile_path, dh_fod_headfile_path)
    print("clangformat_dahua结束")


def clangformat_haikang():
    print("clangformat_haikang开始")
    hk_org_headfile_path = str(curPyPath / "_1_original/HK_NetSDK.h")
    hk_fod_headfile_path = str(curPyPath / "_2_formatted/HK_NetSDK.h")
    clangformat(hk_org_headfile_path, hk_fod_headfile_path)
    print("clangformat_haikang结束")


# 删除注释和空行
def sanitizeText_dahua():
    print("sanitizeText_dahua开始")
    input_dh_headfile_path = str(curPyPath / "_2_formatted/DH_NetSDK.h")
    with open(input_dh_headfile_path, "r", encoding="utf8") as dh:
        dh_text = delete_comment_and_emptyline(dh.read())
    with open(input_dh_headfile_path, "w", encoding="utf8") as dh:
        dh.write(dh_text)
    print("sanitizeText_dahua结束")


def sanitizeText_haikang():
    print("sanitizeText_haikang开始")
    input_hk_headfile_path = str(curPyPath / "_2_formatted/HK_NetSDK.h")
    with open(input_hk_headfile_path, "r", encoding="utf8") as hk:
        hk_text = delete_comment_and_emptyline(hk.read())
    with open(input_hk_headfile_path, "w", encoding="utf8") as hk:
        hk.write(hk_text)
    print("sanitizeText_haikang结束")


# 生成头文件的ctypes中间层
def generateCtypesWrapper_dahua():
    print("generateCtypesWrapper_dahua开始")
    dahua_readyToGenCtypesWrapperFile = str((curPyPath / "_2_formatted/DH_NetSDK.h").resolve())
    dahua_generatedCtypesWrapperFile = str((curPyPath / "_4_completed/DH_NetSDK.py").resolve())
    print("指令列表为", [dahua_readyToGenCtypesWrapperFile, "-o", dahua_generatedCtypesWrapperFile])
    ctypesgenscript([dahua_readyToGenCtypesWrapperFile, "-o", dahua_generatedCtypesWrapperFile])
    print("generateCtypesWrapper_dahua结束")


def generateCtypesWrapper_haikang():
    print("generateCtypesWrapper_haikang开始")
    haikang_readyToGenCtypesWrapperFile = str((curPyPath / "_2_formatted/HK_NetSDK.h").resolve())
    haikang_generatedCtypesWrapperFile = str((curPyPath / "_4_completed/HK_NetSDK.py").resolve())
    print("指令列表为", [haikang_readyToGenCtypesWrapperFile, "-o", haikang_generatedCtypesWrapperFile])
    ctypesgenscript([haikang_readyToGenCtypesWrapperFile, "-o", haikang_generatedCtypesWrapperFile])
    print("generateCtypesWrapper_haikang结束")

# TODO　那个stderr的指向失败了，现去试试它本文件运行是否正常
# TODO 这个ctypesgen的子模块推送失败，我需要先fork到我自己的名下，放到gitee中吧
# 那这样的话会影响commit的同步吗？
# 目前没有对我的子模块进行什么程度级的修改，丢失也无所谓



if __name__ == "__main__":
    # clangformat_dahua()
    # clangformat_haikang()  # 格式化
    #
    # sanitizeText_dahua()
    # sanitizeText_haikang()  # 删注释

    generateCtypesWrapper_dahua()  # 生成包装器
    # generateCtypesWrapper_haikang()

# TODO 我想删除头文件中宏对平台的判断，我要直接指定这个是windows平台
# 但是有一个重要的宏NETSDK_EXPORTS是否被定义，暂无从得知
# 所以我要先搭建一个大华的vs运行环境，完成之后可以使用cl -E指令来检测宏展的最终结果

# 说不定这是一个正确的走向，

# 宏的格式化缩进对齐就显得不是那么着急了，如果上面成功了，宏或许就不用存在了
