# python调用clang-format.exe格式化C++代码
import re
import sys
from pathlib import Path
from UnifyNetSDK.gen_ctypes_file.tools.clang_format.format import clangformat

curPyPath = Path(__file__).parent

notes = """
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


# clang格式化
def clangformat_dahua():
    print("clangformat_dahua开始")
    dh_org_headfile_path = str(curPyPath / "_1_original/DH_NetSDK.h")
    dh_fod_headfile_path = str(curPyPath / "_2_formatted/DH_NetSDK.h")
    clangformat(dh_org_headfile_path, dh_fod_headfile_path, notes)
    print("clangformat_dahua结束")


def clangformat_haikang():
    print("clangformat_haikang开始")
    hk_org_headfile_path = str(curPyPath / "_1_original/HK_NetSDK.h")
    hk_fod_headfile_path = str(curPyPath / "_2_formatted/HK_NetSDK.h")
    clangformat(hk_org_headfile_path, hk_fod_headfile_path, notes)
    print("clangformat_haikang结束")


# 删除注释和空行
def sanitizeText_dahua(copy2replaceDir: bool):
    print("sanitizeText_dahua开始")
    input_dh_headfile_path = str(curPyPath / "_2_formatted/DH_NetSDK.h")
    with open(input_dh_headfile_path, "r", encoding="utf8") as dh:
        dh_text = delete_comment_and_emptyline(dh.read())
    with open(input_dh_headfile_path, "w", encoding="utf8") as dh:
        dh.write(dh_text)
    if copy2replaceDir is True:
        with open("_3_replace/DH_NetSDK.h", "w", encoding="utf8") as dh:
            dh.write(dh_text)
        print("相同内容已同时复制到在第三步文件夹中")  # 其实是又开了一个文件指针而不是shutil.copyfile()
    print("sanitizeText_dahua结束，注释已删除")


def sanitizeText_haikang(copy2replaceDir: bool):
    print("sanitizeText_haikang开始")
    input_hk_headfile_path = str(curPyPath / "_2_formatted/HK_NetSDK.h")
    with open(input_hk_headfile_path, "r", encoding="utf8") as hk:
        hk_text = delete_comment_and_emptyline(hk.read())
    with open(input_hk_headfile_path, "w", encoding="utf8") as hk:
        hk.write(hk_text)
    if copy2replaceDir is True:
        with open("_3_replace/HK_NetSDK.h", "w", encoding="utf8") as hk:
            hk.write(hk_text)
        print("相同内容已同时复制到在第三步文件夹中")  # 其实是又开了一个文件指针而不是shutil.copyfile()
    print("sanitizeText_haikang结束，注释已删除")


# 生成头文件的ctypes中间层

Log2FileTag = False


def generateCtypesWrapper_dahua(log2file: bool):
    print("generateCtypesWrapper_dahua开始")
    dahua_readyToGenCtypesWrapperFile = str((curPyPath / "_3_replace/DH_NetSDK.h").resolve())
    dahua_generatedCtypesWrapperFile = str((curPyPath / "_4_completed/DH_NetSDK.py").resolve())
    dahua_NetSdkDllFile = "Libs/win64/dhnetsdk.dll"
    print("指令列表为", [dahua_readyToGenCtypesWrapperFile, "-o", dahua_generatedCtypesWrapperFile])
    global Log2FileTag
    if Log2FileTag is True and log2file is True:  # 希望将错误报告输出到文件中，但是已经有一个头文件占用了Log2FileTag标识
        raise Exception("用log2file时，只能跑一个头文件，同时只能有一个错误报告能输出到文件中")
    elif Log2FileTag is False and log2file is True:  # 希望将错误报告输出到文件中，且Log2FileTag标识没有被占用
        Log2FileTag = True
        error_file = open('dahua_ctypesgen_log.txt', 'w')  # 解除注释就会使ctypesgen的错误报告输出到文件中，而不是stderr
        sys.stderr = error_file
        from UnifyNetSDK.gen_ctypes_file.tools.sub_ctypesgen.run import main as ctypesgenscript
        ctypesgenscript([dahua_readyToGenCtypesWrapperFile, "-l", dahua_NetSdkDllFile, "-o", dahua_generatedCtypesWrapperFile])
        error_file.close()
    elif Log2FileTag is False and log2file is False:  # 希望将错误报告输出到标准错误输出流中（默认就是终端）中
        from UnifyNetSDK.gen_ctypes_file.tools.sub_ctypesgen.run import main as ctypesgenscript
        ctypesgenscript([dahua_readyToGenCtypesWrapperFile, "-l", dahua_NetSdkDllFile, "-o", dahua_generatedCtypesWrapperFile])
    elif Log2FileTag is True and log2file is False:  # 希望将错误报告输出到标准错误输出流中（默认就是终端）中
        from UnifyNetSDK.gen_ctypes_file.tools.sub_ctypesgen.run import main as ctypesgenscript
        ctypesgenscript([dahua_readyToGenCtypesWrapperFile, "-l", dahua_NetSdkDllFile, "-o", dahua_generatedCtypesWrapperFile])
    print("generateCtypesWrapper_dahua结束")


def generateCtypesWrapper_haikang(log2file: bool):
    print("generateCtypesWrapper_haikang开始")
    haikang_readyToGenCtypesWrapperFile = str((curPyPath / "_3_replace/HK_NetSDK.h").resolve())
    haikang_generatedCtypesWrapperFile = str((curPyPath / "_4_completed/HK_NetSDK.py").resolve())
    print("指令列表为", [haikang_readyToGenCtypesWrapperFile, "-o", haikang_generatedCtypesWrapperFile])
    global Log2FileTag
    if Log2FileTag is True and log2file is True:  # 希望将错误报告输出到文件中，但是已经有一个头文件占用了Log2FileTag标识
        raise Exception("用log2file时，只能跑一个头文件")
    elif Log2FileTag is False and log2file is True:  # 希望将错误报告输出到文件中，且Log2FileTag标识没有被占用
        Log2FileTag = True
        error_file = open('haikang_ctypesgen_log.txt', 'w')
        sys.stderr = error_file
        from UnifyNetSDK.gen_ctypes_file.tools.sub_ctypesgen.run import main as ctypesgenscript
        ctypesgenscript([haikang_readyToGenCtypesWrapperFile, "-o", haikang_generatedCtypesWrapperFile])
        error_file.close()
    elif Log2FileTag is False and log2file is False:  # 希望将错误报告输出到标准错误输出流中（默认就是终端）中
        from UnifyNetSDK.gen_ctypes_file.tools.sub_ctypesgen.run import main as ctypesgenscript
        ctypesgenscript([haikang_readyToGenCtypesWrapperFile, "-o", haikang_generatedCtypesWrapperFile])
    elif Log2FileTag is True and log2file is False:  # 希望将错误报告输出到标准错误输出流中（默认就是终端）中
        from UnifyNetSDK.gen_ctypes_file.tools.sub_ctypesgen.run import main as ctypesgenscript
        ctypesgenscript([haikang_readyToGenCtypesWrapperFile, "-o", haikang_generatedCtypesWrapperFile])
    print("generateCtypesWrapper_haikang结束")


if __name__ == "__main__":  # 一般情况下是，用clangformat格式化后放在第二步文件夹中，但是删除注释是修改第二步的源文件的，第三步就是需要我手动修改头文件的地方，第四步就是完成品
    # clangformat_dahua()
    # clangformat_haikang()  # 格式化

    # sanitizeText_dahua(copy2replaceDir=True)
    # sanitizeText_haikang(copy2replaceDir=True)  # 删注释

    generateCtypesWrapper_dahua(log2file=True)  # 生成包装器，一定注意同时只能有一个方法的log2file可以为True
    # generateCtypesWrapper_haikang(log2file=True)

"""
replace脚本
#include <stdbool.h>
#define CLIENT_NET_API __declspec(dllimport)
#define LPDWORD DWORD *替换为unsigned int*
#define LPDWORD unsigned int*
"""
