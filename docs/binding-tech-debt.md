# 绑定生成器技术债清单

> 记录生成器当前「故意没实现 / 降级处理」的部分。数字以 `python tools/gen_bind.py --sdk X --dry-run` 实测为准。
> 修完一项就打勾，或直接删掉该节。

## 核心未完成（影响业务可用性）

### 1. 回调（最大缺口）

函数指针字段（大华 296、海康 11）整个跳过；函数参数里的回调（`CLIENT_Init(cbDisConnect, ...)`）暴露成 `int` 传 0。

大华/海康的预览、报警、布防、实时流**全靠回调**——这是从「数据结构绑定」到「真正能用的 SDK」的分水岭。

难点三件：

- nanobind `cpp_function` 转裸函数指针
- 回调触发时释放 GIL（否则 SDK 线程回调会卡死解释器）
- 回调对象生命周期（防 Python 侧 GC，而 SDK 仍持有指针）

### 2. 输出指针不自动读回

`outptr` 参数暴露成 `int`（地址），调用后需手动 `ctypes` 预分配缓冲再传地址，没有自动转成 Python 可读返回值。

## 静默跳过（数据不完整）

### 3. 未知类型字段

大华 12、海康 14，混三类：

| 类别 | 例子 | 根因 |
|---|---|---|
| 指针别名 | `LPNET_TIME`、`LPNET_RECORDFILE_INFO` | `_split_decl_names` 丢弃了 `*LPNET_XXX` |
| 漏网函数指针 | `fNotifyEASWaveInfo` 等 | `FP_RE` 没抓到其 typedef |
| 空类型 | `(空) x1` | `FIELD_RE` 边界 bug |

### 4. 函数指针字段

大华 296、海康 11（与第 1 条同源）。

### 5. 位字段

大华 8 个（`BYTE byImageQlty:7`）。C 不允许对位字段取地址，nanobind 绑不了——属 C 限制，不算偷懒。

## 降级处理（绑了但只能「看」）

### 6. 内嵌有名 struct/union 字段按 bytes

如 `stuOldLog`，需用户自己 `struct.unpack`。

### 7. 非 char 数组、多维数组按 bytes

没转 list / numpy。

## 其他

- 6 个未导出函数跳过（厂商头文件 vs DLL 版本不一致，`check_exports.py` 验证过，跳过是对的）。
- 海康还没接 CMake + 编译（生成器就绪，dry-run 通过：2669 结构体 / 18640 字段 / 789 函数）。
- 无 `.pyi` stub（IDE 无补全）、错误码是裸数字、无高层封装。

## 优先级

1. **回调**（业务核心）
2. **指针别名**（修起来最便宜：`_split_decl_names` 别丢 `*LPNET_XXX` 即可把未知从 12 压到个位数）
3. **海康编译**（对等、验证通用核）
4. **高层封装**（易用性）
