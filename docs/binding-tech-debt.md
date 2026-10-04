# 绑定生成器技术债清单

> 记录生成器当前「故意没实现 / 降级处理」的部分。数字以 `python tools/gen_bind.py --sdk X --dry-run` 实测为准。
> 修完一项就打勾，或直接删掉该节。
>
> **踩坑细节见 `implementation-notes.md`**（nanobind / CPython C API / MSVC / 大华 SDK 头文件的脾气）。

## 已完成

### ~~1. 回调~~ ✅ 2026-10-04

大华 289 个回调 typedef 全部生成绑定（`unify_dh_gen`），海康待验证。产出 10 个回调分片 `dh_bind_cbs*.cpp` + 运行时头 `dh_bind_cb.h`（模板源 `tools/common/dhcb.py`）。

Python 侧三个入口：

```python
ptr = unify_dh_gen.bind_fRealDataCallBack(on_data)   # 订阅 + 返回 C 函数指针
unify_dh_gen.CLIENT_SetRealDataCallBack(login, 0, ptr, 0)
unify_dh_gen.set_fRealDataCallBack(on_data)          # 只订阅
unify_dh_gen.unbind_fRealDataCallBack()               # 退订
```

`bind_` 把「订阅 + 取指针」合成一步，避免两步之间的竞态，以及「set 必须写在传指针之前」这个顺序坑。

当初列的三项难点均已解决：

| 难点 | 解法 |
|---|---|
| `cpp_function` 转裸函数指针 | 每回调一个 `static` thunk，`bind_fXxx` 用 `reinterpret_cast` 取地址 |
| 触发时释放 GIL | 以 `PyThreadState_GetUnchecked()` 为判据 —— **不能**用 `PyGILState_Check()` |
| 生命周期（防 Python GC 而 SDK 仍持指针） | 注册表按值持有 `nb::object`；注册表故意不析构 |

参数分类（1146 个参数实测，零误判）：`value 820 / obj 224 / uintptr 48 / cstr 28 / bytes 19 / array 7`。

判定必须**靠参数名**而非位置 —— 289 个回调里 150 个形如 `(NET_X *pInfo, LDWORD dwUser)`，那个整数是用户数据不是数量。且数量/长度关键词要 `$` 锚定在名字末尾：`nFileNum` 的第 4~6 字符忽略大小写正好凑出 `leN` 命中 `len`，不锚定会把数组语义吃掉。

绑定层验证有两条路，现已闭环：

- **端到端（首选）**：`test_e2e_generated.py` 用生成版 `unify_dh_gen` 登录 `Dahua_NVR_Simulator`，验证 Gen2 登录（`nError == 0`）+ 断线回调被真实 SDK 线程触发且参数正确。这条路覆盖了 GIL、生命周期、参数转换，**selftest 因此退休**。
- **selftest（备用）**：`--emit-selftest` 生成 `_selftest_fXxx` 从裸 `std::thread` 调 thunk，268 个钩子全通。ctypes 走不通（它的 `CFUNCTYPE` 回调自建 tstate，GIL 判据会误判导致 `PyThreadState_Attach` 致命错误），所以这是脱离真实设备时唯一能覆盖该路径的手段。默认关。

### ~~2. 指针别名~~ ✅ 2026-10-04

`_split_decl_names` 现在返回 `(类型名, 指针别名)`，`*LPNET_XXX` 进 `ptr_aliases` 集合。厂商头文件大量直接用别名写签名（`fQueryRecordFileCallBack(LLONG, LPNET_RECORDFILE_INFO, int nFileNum, ...)`），漏掉它会把指针当成传值结构体。实测 `value 824→820`、`obj 222→226`、`array 5→7`。

## 核心未完成（影响业务可用性）

### 1. 输出指针不自动读回

`outptr` 参数暴露成 `int`（地址），调用后需手动 `ctypes` 预分配缓冲再传地址，没有自动转成 Python 可读返回值。

## 静默跳过（数据不完整）

### 2. 未知类型字段

大华 12 → 指针别名那类已修（见上），剩两类：

| 类别 | 例子 | 根因 |
|---|---|---|
| 漏网函数指针 | `fNotifyEASWaveInfo` 等 | `FP_RE` 没抓到其 typedef |
| 空类型 | `(空) x1` | `FIELD_RE` 边界 bug |

### 3. 作为结构体成员的函数指针字段

大华 296、海康 11。顶层回调已解决（见上），但**结构体成员**里的函数指针仍按 `skip_funcptr` 跳过：绑成员回调要 `def_readwrite` + 生命周期托管，与顶层回调是两个问题。

### 4. 位字段

大华 8 个（`BYTE byImageQlty:7`）。C 不允许对位字段取地址，nanobind 绑不了——属 C 限制，不算偷懒。

## 降级处理（绑了但只能「看」）

### 5. 内嵌有名 struct/union 字段按 bytes

如 `stuOldLog`，需用户自己 `struct.unpack`。

### 6. 非 char 数组、多维数组按 bytes

没转 list / numpy。

## 其他

- 6 个未导出函数跳过（厂商头文件 vs DLL 版本不一致，`check_exports.py` 验证过，跳过是对的）。
- 海康还没接 CMake + 编译（生成器就绪，dry-run 通过：2669 结构体 / 18640 字段 / 789 函数）。
- 无 `.pyi` stub（IDE 无补全）、错误码是裸数字、无高层封装。
- **两套回调注册表并存**：手写模块 `unify_dh`（`dh_netsdk.cpp` 的 `set_disconnect_callback`）与生成模块 `unify_dh_gen`（`bind_fXxx`）各有独立注册表，同一个 SDK 订阅点只能选一套。长期应收敛到生成版。

## 优先级

1. ~~**回调**（业务核心）~~ ✅
2. ~~**指针别名**~~ ✅
3. **海康编译**（对等、验证通用核）
4. **高层封装**（易用性）
5. **输出指针自动读回**（`outptr` → Python 可读）
