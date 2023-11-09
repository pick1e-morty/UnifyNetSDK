# python调用clang-format.exe格式化C++代码
import os
import re
import subprocess
from pathlib import PurePath
from glob_path import ProjectPath

"""
在进行脚本操作前我修改了两个源头文件内容
1.编码转换为UTF-8
2.在HK_NetSDK.h文件中14272行的LPBEHAVIOR_PRISON_MODE_TYPE前面添加一个*符号，很明显这是一个枚举指针，不过原作者忘了加了
"""

# 现在还没有验证这个做法是正确的3.在DH_NetSDK.h文件第一行插入一句#include <stdbool.h>。解决跟bool有联系的结构体无法转换的问题

# TODO，海康那边还没加这个库
# 但其实这是我用错了编译器的原因对吧，只要我换成g++，问题就不存在了，一定是这样的！

def clang_format(input_file_path, output_file_path):
    r"""
    首先生成基于llvm的格式化配置文件
    clang-format -style=llvm -dump-config > .clang-format
    然后修改下面的数值
    ColumnLimit:0             # 每行最大字符数
    IndentWidth: 4            # 缩进宽度
    PointerAlignment: Left  # 指针对齐方式
    BreakBeforeBraces: Custom # 大括号换行方式
    AfterStruct:     true     # 结构体大括号统一格式
    AfterEnum:       true
    AfterUnion:      true      # 虽然这三个都没法控制嵌套数据类型中的{}
    IndentPPDirectives: BeforeHash  # 预处理指令对齐


    这个python文件就是用来执行这段代码的
    .\clang-format.exe -style=file .\IN_原HCNetSDK.h > .\OUT_HCNetSDK.h
    """
    if not os.path.exists(input_file_path):
        print(f"{input_file_path} 输入文件不存在")
        return
    elif not os.path.exists(clangformatExecuteFilePath):
        print("clang-format.exe不存在")
        return
    cmd = (
            clangformatExecuteFilePath + " "
            + "-style=file "
            + input_file_path
            + " > "
            + output_file_path
    )
    print("预执行命令为：", cmd)
    subprocess.call(cmd, shell=True)


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


def ctypesgen_fun(input_file_path, output_file_path):
    r"""
    ctypesgen hcheadfile.h -o ctypesgenHeadFile.py

    """
    if not os.path.exists(input_file_path):
        print(f"{input_file_path} 输入文件不存在")
        return
    elif not os.path.exists(ctypesgenExecuteFilePath):
        print("ctypesgen.exe不存在")
        return
    cmd = (
            ctypesgenExecuteFilePath
            + " "
            + input_file_path
            + " -o "
            + output_file_path
    )
    print("预执行命令为：", cmd)
    subprocess.call(cmd, shell=True)


if __name__ == "__main__":
    scriptFilePath = PurePath(__file__)
    clangformatExecuteFilePath = str(scriptFilePath.with_name("clang-format.exe"))
    ctypesgenExecuteFilePath = str(scriptFilePath.with_name("ctypesgen.exe"))

    curPath = PurePath(__file__).parent


    # clang格式化
    def clang_dahua():
        dh_org_headfile_path = str(curPath / "_1_original/DH_NetSDK.h")
        dh_fod_headfile_path = str(curPath / "_2_formatted/DH_NetSDK.h")
        clang_format(dh_org_headfile_path, dh_fod_headfile_path)

    def clang_haikang():
        hk_org_headfile_path = str(curPath / "_1_original/HK_NetSDK.h")
        hk_fod_headfile_path = str(curPath / "_2_formatted/HK_NetSDK.h")
        clang_format(hk_org_headfile_path, hk_fod_headfile_path)


    # 删除注释和空行
    def delete():
        input_dh_headfile_path = str(curPath / "_2_formatted/DH_NetSDK.h")
        with open(input_dh_headfile_path, "r", encoding="utf8") as dh:
            dh_text = delete_comment_and_emptyline(dh.read())
        with open(input_dh_headfile_path, "w", encoding="utf8") as dh:
            dh.write(dh_text)

        input_hk_headfile_path = str(curPath / "_2_formatted/HK_NetSDK.h")
        with open(input_hk_headfile_path, "r", encoding="utf8") as hk:
            hk_text = delete_comment_and_emptyline(hk.read())
        with open(input_hk_headfile_path, "w", encoding="utf8") as hk:
            hk.write(hk_text)


    clang_dahua()
    clang_haikang()

    # delete()

    # 生成头文件的ctypes中间层
    # input_dh_headfile_path = str(curPath / "_2_formatted/DH_NetSDK.h")
    # output_dh_headfile_path = str(ProjectPath / "UnifyNetSDK/dahua/ctypes_headfile.py")
    # ctypesgen_fun(input_dh_headfile_path, output_dh_headfile_path)
    #
    # input_hk_headfile_path = str(curPath / "_2_formatted/HK_NetSDK.h")
    # output_hk_headfile_path = str(ProjectPath / "UnifyNetSDK/haikang/ctypes_headfile.py")
    # ctypesgen_fun(input_hk_headfile_path, output_hk_headfile_path)


# TODO 我想删除头文件中宏对平台的判断，我要直接指定这个是windows平台
# 但是有一个重要的宏NETSDK_EXPORTS是否被定义，暂无从得知
# 所以我要先搭建一个大华的vs运行环境，完成之后可以使用cl -E指令来检测宏展的最终结果

# 说不定这是一个正确的走向，

# 宏的格式化缩进对齐就显得不是那么着急了，如果上面成功了，宏或许就不用存在了