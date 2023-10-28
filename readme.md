
# NetSDK
本项目作用于整合同行厂商的设备SDK，为上层调用方 统一Python端的基本登录，预览，下载等接口。

现阶段仅整合和需要海康和大华两个厂商的C语言SDK接口

截至**23/09/27**能在官网下载到的最新版本号为

海康：CH-HCNetSDKV6.1.9.48_build20230410_win64

大华：General_NetSDK_Chn_Win64_IS_V3.057.0000002.0.R.230814

# ctypes中间层生成过程
clang-format.exe version: 16.0.0
ctypes.exe version: 1.1.2.dev7+gdeb059e.d20230825

1. 我看了头文件的结构体写法各有特色，所以先由clang对头文件进行格式化。
2. 因ctypesgen不支持中文（就算文件是UTF-8），所以我删除了掉所有注释及空行。
3. 本机安装gcc后运行ctypesgen，就算完成了。

## 试错过程
原本找到了21世纪最顶级(github星星最多，等)的C/C++转python的工具，PyBind11，但是这个工具对类似于Char name[5]这种古老的C语言数组完全不理会，不处理。
对比衡量其他几种方案后无奈之下只能再次投入ctypes的怀抱。我开始尝试硬处理C语言语法转换，地址：https://gitee.com/picklemorty/handleHtext.git。
在接近完全解析海康SDK结构体生成ctypes中间层时事情发生了重大转机。当我询问大模型AI相关问题时，他居然直接告诉我这种方法太低效了，随后向我推荐了ctypesgen这个项目，我大为震惊！（在此之前我当然也多维询问过有没有更高效的方案，但只有这一次这个AI说了）
https://github.com/ctypesgen/ctypesgen.git
介绍：ctypesgen是一个纯python的ctypes包装生成器。它解析C头文件并根据找到的内容创建库的包装器。

## 注意
目前我所生成及使用的SDK头文件中的变量类型是根据gcc内置的头文件进行映射的。这可能是错误的（用gcc生成后SDK也能跑），因为SDK手册指明了要用VisualStudio。
像这种 BOOL = c_int# C:/Program Files/mingw64/x86_64-w64-mingw32/include/minwindef.h: 131
对比过后确实有些大大小小的差异，且ctypesgen在生成过程也不断的报错。
本人对C语言的了解止步于上学时期的数据结构 图，我是硬着头皮试了一下发现居然能用，所以就没在这方面耗费太多时间。毕竟上层要做的事也还有好多呀。


# 海康SDK说明
## Exception
1. 报错思路是由GetLastError返回错误代码后直接拿这个数字作为字典的key，故索引值不能重复。
2. 取原HCNetSDK.h的第452行到1666行作为错误代码字典内容，共1215行。
3. 由于某些错误代码的索引值需要宏展开及宏展开后的索引去重，我使用表格处理软件进行了本次python错误代码字典的辅助编写。
4. 在经过分列，“宏展”，”计算真实索引数值“后仅查到200和300两个错误代码索引值为重复，遂删除其一。
5. 最后对几个单元格进行文本合并操作就能得到UnifyNetSDK/haikang/HK_Exception.py文件了。

