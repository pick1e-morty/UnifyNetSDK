import inspect
import textwrap


def generateCodeText(className):
    """
    Prints the source code of the given class.
    """
    source_code = inspect.getsource(className)
    dedented_source = textwrap.dedent(source_code)
    print(dedented_source)
    return dedented_source


def genrateException(baseException, errorCodeDict, appendErrorInfo):
    """
    把字典的value都作为exception
    模板
    class NET_NOERROR(DHNetSDKException):
        def __init__(self, errorText=None):
            self.errorIndex = 0
            self.errorType = "NET_NOERROR"
            self.errorInfo = errorText
    """
    with open(f"{baseException.__name__}.py", "w", encoding="utf-8") as f:
        baseExceptionCodeText = generateCodeText(baseException)
        f.write(baseExceptionCodeText)  # 先把基类写进去
        f.write("\n")
        for key, value in errorCodeDict.items():
            errorInfoText = appendErrorInfo.get(key, None)
            f.write("\n")
            f.write(f"class {value}({baseException.__name__}):\n")
            f.write(f"    def __init__(self, errorText=None):\n")
            f.write(f"        self.errorIndex = {key}\n")
            if errorInfoText:
                f.write(f"        tempErrorInfo = \"{errorInfoText}\"\n")
                # tempErrorInfo = "错误码索引重复了，该错误码所对应的另一个类型为NET_ERROR_FACE_RECOGNITION_SERVER_DELETE_GROUP_ERROR"
                f.write(f"        self.errorInfo = tempErrorInfo + \"\\n\" + str(errorText) if errorText else tempErrorInfo\n")
                # self.errorInfo = tempErrorInfo + "\n" + str(errorText) if errorText else tempErrorInfo
            else:
                f.write(f"        self.errorInfo = errorText\n")
            f.write("\n")


# 就算已有errorInfo也要判断用户是否输入了errorText参数，
# 然后追加用户的文本

def genrateExceptionDict(dictName, errorCodeDict, fileName):
    # ErrorCode = {
    #     0: "NET_NOERROR",
    #     -1: "NET_ERROR",
    #     1: "NET_SYSTEM_ERROR",
    # 去除value旁边的双引号就行了
    # sdk那边使用getLastErrorIndex()来获取错误码，所以这里需要把错误码转换成对应的错误类型
    with open(f"{fileName}.py", "a+", encoding="utf-8") as f:
        f.write(f"{dictName} = {{\n")
        for key, value in errorCodeDict.items():
            f.write(f"{key}: {value},\n")
        f.write("}")
