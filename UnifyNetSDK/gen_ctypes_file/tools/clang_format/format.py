import subprocess
from pathlib import Path

clangFormatDirPath = Path(__file__).parent
clangformatExecuteFilePath = str(clangFormatDirPath / "clang-format.exe")
clangformatStyleFilePath = str((clangFormatDirPath / ".clang-format").resolve())


def clangformat(input_file_path, output_file_path):
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
    if not Path(input_file_path).exists():
        print(f"{input_file_path} 输入文件不存在")
        raise Exception(f"{input_file_path} 输入文件不存在")
    elif not Path(clangformatExecuteFilePath).exists():
        print("clang-format.exe不存在")
        raise Exception(f"{clangformatExecuteFilePath} 不存在")
    elif not Path(clangformatStyleFilePath).exists():
        print("clang-format的style文件不存在")
        raise Exception(f"{clangformatStyleFilePath} 不存在")

    cmd = (
            clangformatExecuteFilePath
            + f" -style=file:{clangformatStyleFilePath} "
            + input_file_path
            + " > "
            + output_file_path
    )
    print("执行命令为：", cmd)
    subprocess.call(cmd, shell=True)
