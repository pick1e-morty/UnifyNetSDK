# 绑定生成器技术债清单

> 记录生成器当前「故意没实现 / 降级处理」的部分。数字以
> `python native/codegen/check_coverage.py` 实测为准（升级 SDK 后重跑即可刷新）。
>
> **踩坑细节见 `implementation-notes.md`**（nanobind / CPython C API / MSVC / 大华 SDK 头文件的脾气）。

## 覆盖边界（2026-10-04 实测）

| 类别 | 已绑定 / 总数 | 说明 |
|---|---|---|
| 枚举 | 1873 / 1873 | 全对 |
| 结构体 | 10557 / 10557 | 全对 |
| 函数 | 2515 / 2521 | 6 个 DLL 未导出，跳过是对的 |
| 回调 typedef | 289 / 289 | 全对（`bind_fXxx` / `set_fXxx` / `unbind_fXxx`）|
| 字段 | **62574 / 62884 = 99.51%** | 详见下方"静默跳过" |

字段里的数组进一步分两种，**这个区别比"跳过多少"更重要**：

| 数组类型 | 数量 | Python 侧 | 性质 |
|---|---|---|---|
| `char[N]` | 11211 | `str` | 无损，自动截断防溢出 |
| 其余（`BYTE[N]` / `int[N]` / `NET_X[N]` / 多维）| 6419 | `bytes` | **降级**，需自己 `struct.unpack` |

## 已完成

### ~~1. 回调~~ ✅ 2026-10-04

大华 289 个回调 typedef 全部生成绑定，产出 10 个分片 `dh_bind_cbs*.cpp` + 运行时头
`dh_bind_cb.h`（模板源 `native/codegen/common/cb_runtime.py`）。

```python
ptr = unify_dh_gen.bind_fRealDataCallBack(on_data)   # 订阅 + 返回 C 函数指针
unify_dh_gen.CLIENT_SetRealDataCallBack(login, 0, ptr, 0)
unify_dh_gen.set_fRealDataCallBack(on_data)          # 只订阅
unify_dh_gen.unbind_fRealDataCallBack()               # 退订
```

`bind_` 把「订阅 + 取指针」合成一步，避免两步之间的竞态、以及「set 必须写在传指针之前」。

三项难点均已解决：

| 难点 | 解法 |
|---|---|
| `cpp_function` 转裸函数指针 | 每回调一个 `static` thunk，`bind_fXxx` 用 `reinterpret_cast` 取地址 |
| 触发时释放 GIL | 以 `PyThreadState_GetUnchecked()` 为判据 —— **不能**用 `PyGILState_Check()` |
| 生命周期（防 Python GC 而 SDK 仍持指针）| 注册表按值持有 `nb::object`；注册表故意不析构 |

参数分类（1146 个参数实测，零误判）：`value 820 / obj 224 / uintptr 48 / cstr 28 /
bytes 19 / array 7`。判定必须**靠参数名**而非位置 —— 289 个回调里 150 个形如
`(NET_X *pInfo, LDWORD dwUser)`，那个整数是用户数据不是数量；且数量/长度关键词要 `$`
锚定在名字末尾：`nFileNum` 的第 4~6 字符忽略大小写正好凑出 `leN` 命中 `len`。

验证：端到端 `native/tests/e2e/test_login_callback.py`（真实 SDK 线程触发，参数全对）；
绑定层 `native/tests/test_callbacks.py`（依赖 `_selftest_fXxx` 钩子从裸
`std::thread` 调 thunk，268 个钩子全通）。钩子**默认生成**（`--no-selftest` 可关），
因为关掉后绑定层测试就完全跑不了；附带好处是上游无设备时也能用钩子验证自己的回调。

### ~~2. 指针别名~~ ✅ 2026-10-04

厂商用 `LPNET_XXX` 写指针，类型名里没有 `*`。原先 `_split_decl_names` 直接丢弃
`*LPNET_XXX`，导致这些字段被当传值结构体或判成未知类型。

现在返回 `{别名: 目标类型}` 映射，三处都要用它：字段白名单（否则判未知）、`gen_fields`
（否则对指针成员 `def_rw` 报 C2440）、`build_deps`（否则注册拓扑序错，运行时找不到类型）。
回调参数分类同步修正后：未知类型 12 → 6，`array 5 → 7`。

## 核心未完成（影响业务可用性）

### 1. 输出指针不自动读回

`outptr` 参数暴露成 `int`（地址），调用后需手动 `ctypes` 预分配缓冲再传地址，没有自动
转成 Python 可读返回值。这是"能用但别扭"的主要来源。

### 2. 作为结构体成员的函数指针字段（大华 296 个）

顶层回调已全部解决，但**结构体成员**里的函数指针仍按 `skip_funcptr` 跳过。绑成员回调要
`def_readwrite` + 生命周期托管（成员可能被 SDK 长期持有），与顶层回调是两个问题。
实际影响有限：业务代码基本都走 `CLIENT_xxx` 的顶层回调参数。

## 静默跳过（数据不完整）

### 3. 未知类型字段（大华 6 个）

| 类别 | 例子 | 根因 |
|---|---|---|
| 漏网函数指针 | `fNotifyEASWaveInfo`、`fNotifyFaultCheckProgress`、`fNotifyFeatureState`、`fNotifyInfraredState`、`fNotifyClassBrand` | `FP_RE` 没抓到其 typedef（正则只认 `typedef ... (*name)(`，这些写法不同）|
| 空类型 | `(空) x1` | `FIELD_RE` 边界 bug |

### 4. 位字段（大华 8 个）

`BYTE byImageQlty:7`。C 不允许对位字段取地址，nanobind 绑不了——**属 C 限制，不算偷懒**。

## 降级处理（绑了但只能「看」）

### 5. 非 char 数组、多维数组按 bytes（大华 6419 个）

拿到 `bytes` 需自己 `struct.unpack`。要转 list/numpy 的话在 `emit.gen_fields` 扩展。

### 6. 内嵌有名 struct/union 字段按 bytes

如 `stuOldLog`，需用户自己 `struct.unpack`.

### 7. 无 `.pyi` stub、错误码是裸数字

IDE 无补全，高层封装未做。

## 其他

- ~~两套回调注册表并存~~ ✅ 已收敛（2026-10-04）。手写版 `set_disconnect_callback`
  与 4 个 `_test_*` 转换探针已删除，回调统一走生成版。此前两套注册表独立，
  同一 SDK 订阅点混用会静默不触发。`unify_dh` 现在只剩登录链路、`log_open`、
  GIL 探针。
- 生成物 `native/src/gen_dh/` 不入库（可重建），改代码请改 `native/codegen/` 下的源头。

## 优先级

| # | 事项 | 理由 |
|---|---|---|
| ~~1~~ | ~~回调~~ | ✅ 已完成 |
| ~~2~~ | ~~指针别名~~ | ✅ 已完成 |
| 3 | **未知类型归零**（6 个）| 最便宜：改 `FP_RE` 一条正则 + `FIELD_RE` 一个边界条件 |
| 4 | **海康编译** | 验证 `common/` 真与厂商无关；dry-run 已通过（2669 结构体 / 18640 字段 / 789 函数）|
| 5 | **`.pyi` stub** | 纯生成工作，体验提升大，且能让错误码有类型 |
| 6 | **高层封装** | 错误码表、输出缓冲自动读回（技术债 #1）|
| 7 | **成员函数指针**（296 个）| 最贵，且要解决生命周期托管；实际影响有限 |
