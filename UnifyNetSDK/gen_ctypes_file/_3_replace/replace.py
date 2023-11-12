# 正则删除注释和空行
import re
import time
from pathlib import Path


def remove_default_parameters(text):
    info_log = open("replace_log.txt", "w")

    def fun(matchs):  # 子函数，这个正则需要二次处理
        # 删除可能多次存在的=后面的内容
        # 像这种void * pExtendInfo = NULL, int waittime = 1000);
        # 变成void * pExtendInfo, int waittime);
        matchtext = matchs[0]
        print("matchtext", matchtext)
        info_log.write(f"matchtext,{matchtext}\n")

        sub_pattern = r"(\s*=\s*[\d\w]+)+"
        new_text = re.sub(sub_pattern, "", matchtext)

        print("new_text", {new_text})

        info_log.write(f"new_text,{new_text}\n")
        return new_text

    main_pattern = r"^CLIENT_NET_API[^;]*=[^;]*;"  # 先拿到含有CLIENT_NET_API和=的整条语句
    # ^CLIENT_NET_API[^;]*=[^;]*;
    # ^CLIENT_NET_API               [^;]*                          =          [^;]*                  ;
    #                  只要=左边不是;就说明函数声明还没在(这行)结束                       匹配等号后及分号前的所有内容
    processedText = re.sub(main_pattern, fun, text, flags=re.M)
    info_log.close()
    return processedText

    # 未完善的处理方案
    # (?<=CLIENT_NET_API).*(\s*=\s*[\d\w]*)+
    # 没做到一步到位，只需要把中间那唯一一个.*匹配到的内容给丢掉就能做到一个re.sub完事


if __name__ == "__main__":
    #     text = """CLIENT_NET_API BOOL CALL_METHOD CLIENT_QueryNewSystemInfoEx(LLONG lLoginID, char* szCommand, int nChannelID, char* szOutBuffer, DWORD dwOutBufferSize, int* error, void* pExtendInfo = NULL, int waittime = 1000);
    # CLIENT_NET_API BOOL CALL_METHOD CLIENT_QueryRemotDevState(LLONG lLoginID, int nType, int nChannelID, char* pBuf, int nBufLen, int* pRetLen, int waittime = 1000);
    # CLIENT_NET_API BOOL CALL_METHOD CLIENT_QuerySystemInfo(LLONG lLoginID, int nSystemType, char* pSysInfoBuffer, int maxlen, int* nSysInfolen, int waittime = 1000);
    # CLIENT_NET_API BOOL CALL_METHOD CLIENT_QueryNewSystemInfo(LLONG lLoginID, char* szCommand, int nChannelID, char* szOutBuffer, DWORD dwOutBufferSize, int* error, int waittime = 1000);
    #             """
    #
    #     print(remove_default_parameters(text))

    curPyPath = Path(__file__)
    input_dh_headfile_path = str(curPyPath.with_name("DH_NetSDK.h"))
    print(input_dh_headfile_path)
    with open(input_dh_headfile_path, "r", encoding="utf8") as dh:
        dh_text = remove_default_parameters(dh.read())
    time.sleep(1)
    with open(input_dh_headfile_path, "w", encoding="utf8") as dh:
        dh.write(dh_text)
    print("完成")

