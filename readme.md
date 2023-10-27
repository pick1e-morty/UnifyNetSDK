
# NetSDK
本项目作用于整合同行厂商的设备SDK，为上层调用方 统一Python端的基本登录，预览，下载等接口。


现阶段整合海康和大华两个厂商的C语言SDK接口
两家厂商的SDK都是通过ctypesgen进行转换生成过的
https://github.com/ctypesgen/ctypesgen.git

ctypesgen是一个纯python的ctypes包装生成器。它解析C头文件并根据找到的内容创建库的包装器。

截至**23/09/27**能在官网下载到的最新版本号为

海康：CH-HCNetSDKV6.1.9.48_build20230410_win64

大华：General_NetSDK_Chn_Win64_IS_V3.057.0000002.0.R.230814



# 海康SDK说明
## Exception
1. 报错思路是由GetLastError返回错误代码后直接拿这个数字作为字典的key，故索引值不能重复
2. 取原HCNetSDK.h的第452行到1666行作为错误代码字典内容，共1215行
3. 由于某些错误代码的索引值需要宏展开及宏展开后的索引去重，我使用表格处理软件进行了本次python错误代码字典的辅助编写
4. 在经过分列，“宏展”，”计算真实索引数值“后仅查到200和300两个错误代码索引值为重复，遂删除其一
5. 最后对几个单元格进行文本合并操作就能得到UnifyNetSDK/haikang/HK_Exception.py文件了


# TODO
一、下面这两个问题都是我对ctypesgen和C语言开发环境的不理解所导致而存在的
1.目前SDK头文件中的变量类型是根据gcc内置的头文件进行映射的
这可能是错误的，因为SDK指明了要用VisualStudio。
像这种
BOOL = c_int# C:/Program Files/mingw64/x86_64-w64-mingw32/include/minwindef.h: 131

2.第二个就是宏的展开，gcc编译器的宏展肯定和msvc的cl编译器宏展结果有些不同


