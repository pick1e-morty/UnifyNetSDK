
# NetSDK
本项目作用于整合同行厂商的设备SDK，为上层调用方 统一Python端的基本登录，预览，下载等接口。

现阶段仅整合和需要海康和大华两个厂商的C语言SDK接口

截至**23/09/27**能在官网下载到的最新版本号为

海康：CH-HCNetSDKV6.1.9.48_build20230410_win64

大华：General_NetSDK_Chn_Win64_IS_V3.057.0000002.0.R.230814

# ctypes中间层生成过程
clang-format.exe version: 16.0.0
ctypesgen version: 1.1.2.dev7+gdeb059e.d20230825
ctypesgen:https://github.com/ctypesgen/ctypesgen



## 将SDK原有的GetLastError改造成python可以跨层向上传递的Exception
1. 报错思路是由GetLastError返回错误代码后直接拿这个数字作为字典的key，故索引值不能重复。
2. 取UnifyNetSDK/gen_ctypes_file/formatted/HK_NetSDK.h的第452行到1667行作为错误代码字典内容，共1215行。
3. 由于某些错误代码的索引值需要宏展开及宏展开后的索引去重，我使用表格处理软件进行了本次python错误代码字典的辅助编写。
4. 在经过分列，“宏展”，”计算真实索引数值“后仅查到200和300两个错误代码索引值为重复，遂删除其一。
5. 最后对几个单元格进行文本合并操作就能得到UnifyNetSDK/haikang/HK_Exception.py文件了。

