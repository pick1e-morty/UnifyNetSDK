import re
import sys
from pathlib import Path

from UnifyNetSDK.gen_ctypes_file.tools.clang_format.format import clangformat as _clangformat

curPyPath = Path(__file__).parent

notes = """
在进行脚本操作前我修改了四个源头文件内容
1.编码转换为UTF-8,因为clang-format不支持我这两个头文件的gb2312
2.在HK_NetSDK.h文件中14272行的LPBEHAVIOR_PRISON_MODE_TYPE前面添加一个*符号，很明显这是一个枚举指针，不过原作者忘了加了
"""


# clang格式化
def clangformat(fileName):
    print(f"clangformat {fileName} 开始")
    dh_org_headfile_path = str(curPyPath / Step_1_DirName / fileName)
    dh_fod_headfile_path = str(curPyPath / Step_2_DirName / fileName)
    _clangformat(dh_org_headfile_path, dh_fod_headfile_path, notes)
    print(f"clangformat结束 {fileName} ")


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


# 删除注释和空行
def sanitizeText(fileName, copy2replaceDir: bool):
    """
    本函数是修改源文件的，如果copy2replaceDir为True还会将结果复制到_3_replace下
    """
    print(f"sanitizeText {fileName} 开始")
    input_headfile_path = str(curPyPath / Step_2_DirName / fileName)
    with open(input_headfile_path, "r", encoding="utf8") as fp:
        text = delete_comment_and_emptyline(fp.read())
    output_headfile_path = input_headfile_path
    with open(output_headfile_path, "w", encoding="utf8") as fp:
        fp.write(text)
    if copy2replaceDir is True:
        output_headfile_path = str(curPyPath / Step_3_DirName / fileName)
        with open(output_headfile_path, "w", encoding="utf8") as fp:
            fp.write(text)
        print("相同内容已同时复制到在第三步文件夹中")  # 其实是又开了一个文件指针而不是shutil.copyfile()
        print(f"sanitizeText {fileName} 结束，注释已删除")


# 生成头文件的ctypes中间层


def generateCtypesWrapper(fileName: str, log2file: bool = True):
    if fileName == "DH_NetSDK.h":
        dllFile = "Libs/win64/dhnetsdk.dll"
    elif fileName == "DH_PlaySDK.h":
        dllFile = "Libs/win64/play.dll"
    elif fileName == "HK_NetSDK.h":
        dllFile = "lib/win/HCNetSDK.dll"
    elif fileName == "HK_PlaySDK.h":
        dllFile = "lib/win/PlayCtrl.dll"
    else:
        raise Exception("参数有误")

    print("generateCtypesWrapper开始")
    readyToGenCtypesWrapperFile = str((curPyPath / Step_3_DirName / fileName).resolve())
    generatedCtypesWrapperFile = str((curPyPath / Step_4_DirName / fileName).resolve())
    arg_list = [readyToGenCtypesWrapperFile, "-l", dllFile, "-o", generatedCtypesWrapperFile]
    print("指令列表为", arg_list)

    if log2file is True:  # 希望将错误报告输出到文件中
        error_file = open('ctypesgen.log', 'w')
        sys.stderr = error_file
        from UnifyNetSDK.gen_ctypes_file.tools.sub_ctypesgen.run import main as ctypesgenscript
        ctypesgenscript(arg_list)
        error_file.close()
    else:  # 希望将错误报告输出到标准错误输出流中（默认就是终端）中
        from UnifyNetSDK.gen_ctypes_file.tools.sub_ctypesgen.run import main as ctypesgenscript
        ctypesgenscript(arg_list)
    print("generateCtypesWrapper结束")


def _remove_default_parameters(pattern, text):
    """
    删除函数声明中的默认参数部分
    """
    info_log = open("replace.log", "w")

    def fun(matchs):  # 子函数，这个正则需要二次处理
        # 删除可能多次存在的=后面的内容
        # 像这种void * pExtendInfo = NULL, int waittime = 1000);
        # 改为void * pExtendInfo, int waittime);
        matchtext = matchs[0]
        print("matchtext", matchtext)
        info_log.write(f"matchtext,{matchtext}\n")

        sub_pattern = r"(\s*=\s*[\d\w]+)+"
        new_text = re.sub(sub_pattern, "", matchtext)

        print("new_text", {new_text})

        info_log.write(f"new_text,{new_text}\n")
        return new_text

    # ^CLIENT_NET_API[^;]*=[^;]*;
    # ^CLIENT_NET_API               [^;]*                          =          [^;]*                  ;
    #                  只要=左边不是;就说明函数声明还没在(这行)结束                       匹配等号后及分号前的所有内容
    # ^NET_DVR_API[^;]*=[^;]*;   与上同理

    processedText = re.sub(pattern, fun, text, flags=re.M)
    info_log.close()
    return processedText

    # 未完善的处理方案
    # (?<=CLIENT_NET_API).*(\s*=\s*[\d\w]*)+
    # 没做到一步到位，只需要把中间那唯一一个.*匹配到的内容给丢掉就能做到一个re.sub完事


def remove_default_parameters(fileName):
    print(f"remove_default_parameters {fileName} 开始")

    if fileName == "DH_NetSDK.h":
        pattern = dahua_pattern = r"^CLIENT_NET_API[^;]*=[^;]*;"  # 先拿到含有CLIENT_NET_API和=的整条语句,大华函数声明开头
    elif fileName == "DH_PlaySDK.h":
        pattern = dahua_playsdk_pattern = r"^PLAYSDK_API[^;]*=[^;]*;"  # 先拿到含有NET_DVR_API和=的整条语句,海康函数声明开头
    elif fileName == "HK_NetSDK.h":
        pattern = haikang_pattern = r"^NET_DVR_API[^;]*=[^;]*;"  # 先拿到含有NET_DVR_API和=的整条语句,海康函数声明开头
    elif fileName == "HK_PlaySDK.h":
        pattern = haikang_playsdk_pattern = r"^PLAYM4_API[^;]*=[^;]*;"
    else:
        raise Exception("参数有误")

    input_headfile_path = str(curPyPath / Step_3_DirName / fileName)
    with open(input_headfile_path, "r", encoding="utf8") as fp:
        text = _remove_default_parameters(pattern, fp.read())
    output_headfile_path = input_headfile_path
    with open(output_headfile_path, "w", encoding="utf8") as fp:
        fp.write(text)
    print(f"remove_default_parameters {fileName} 结束")


if __name__ == "__main__":  # 一般情况下是，用clangformat格式化后放在第二步文件夹中，但是删除注释是修改第二步的源文件的，第三步就是需要我手动修改头文件的地方，第四步就是完成品

    Step_1_DirName = Path("_1_original")  # 每一步的文件夹名称
    Step_2_DirName = Path("_2_formatted")
    Step_3_DirName = Path("_3_replace")
    Step_4_DirName = Path("_4_completed")
    Step_1_DirName.mkdir(exist_ok=True)
    Step_2_DirName.mkdir(exist_ok=True)
    Step_3_DirName.mkdir(exist_ok=True)
    Step_4_DirName.mkdir(exist_ok=True)

    dahua = "DH_NetSDK.h"  # 头文件名称
    haikang = "HK_NetSDK.h"
    dahua_playsdk = "DH_PlaySDK.h"  # 大华的播放库
    haikang_playsdk = "HK_PlaySDK.h"  # 海康的播放库

    # clangformat(dahua)  # 1格式化，从_1_original读取，写入到_2_formatted
    # sanitizeText(dahua, copy2replaceDir=True)  # 2删注释，从_2_formatted读取，写入到_2_formatted。如果copy2replaceDir为True，还会同时写入到_3_replace
    # remove_default_parameters(dahua)  # 3删除默认参数 =，从_3_replace读取，写入到_3_replace
    # generateCtypesWrapper(dahua, log2file=True)  # 4生成包装器，一定注意同时只能有一个方法的log2file可以为True。从_3_replace读取，写入到_4_completed

    # clangformat(dahua_playsdk)
    # sanitizeText(dahua_playsdk, copy2replaceDir=True)
    # remove_default_parameters(dahua_playsdk)
    # generateCtypesWrapper(dahua_playsdk, log2file=True)

    # clangformat(haikang)
    # sanitizeText(haikang, copy2replaceDir=True)
    # remove_default_parameters(haikang)
    # generateCtypesWrapper(haikang, log2file=True)

    # clangformat(haikang_playsdk)
    # sanitizeText(haikang_playsdk, copy2replaceDir=True)
    # remove_default_parameters(haikang_playsdk)
    generateCtypesWrapper(haikang_playsdk, log2file=True)

"""
运行到第三步之后之后还需要进行一些手动操作
大华netsdk头文件
添加行
#include <stdbool.h>
替换行内容
# non windows分支下的语句替换
    #define CLIENT_NET_API extern "C"  替换为  #define CLIENT_NET_API __declspec(dllimport)  # 这步跟海康对比一下，我应该是做错了的
    #define LPDWORD DWORD*  替换为  #define LPDWORD unsigned int*
    #define LLONG long  替换为  #define LLONG long long


海康playsdk头文件
添加行
#include <windows.h>
    
"""
