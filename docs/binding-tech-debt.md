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
| 字段 | **63044 / 63353 = 99.51%** | 跳过见下方"静默跳过" |

字段里的数组进一步分两种，**这个区别比"跳过多少"更重要**：

| 数组类型 | 数量 | Python 侧 | 性质 |
|---|---|---|---|
| `char[N]` | 11211 | `str` | 无损，自动截断防溢出 |
| 其余（`BYTE[N]` / `int[N]` / `NET_X[N]` / 多维）| 6420 | `bytes` | **降级**，需自己 `struct.unpack` |

## 覆盖边界 —— 海康（2026-10-04 实测）

| 类别 | 已绑定 / 总数 | 说明 |
|---|---|---|
| 枚举 | 264 / 264 | 全对 |
| 结构体 | 2670 / 2670 | 全对 |
| 函数 | 785 / 789 | 4 个 DLL 未导出，跳过是对的 |
| 回调 typedef | 26 / 26 | 保守退化（见下） |
| 字段 | **18810 / 18821 = 99.94%** | 跳过 11：全是成员函数指针（未知类型已归零） |

海康回调参数分类（26 回调 / 110 参数）：`value 59 / cstr 8 / obj 13 / uintptr 30 / bytes 0 / array 0`。
`config/haikang.py` 故意不设数量/长度语义钩子，`array` 恒为 0、`BYTE*` 只能给 int 地址 ——
少给而非给错的保守退化，规则等接上设备照实际行为再写。

> **口径说明**：本表（`check_coverage.py`）是**头文件全量口径**，不做条件编译裁剪。
> pyd 实际产物与其差两类：① 海康 Linux 分支被 `text_filters` 裁掉的约 29 个字段
> （Windows 下本就不存在，属正确裁剪）；② 句柄字段（`HWND` 等 7 个）——2026-10-04
> 起已通过把 `OPAQUE_PTR` 并入白名单 + emit 按地址读写而归零。保持全量口径是为了
> 让"升级 SDK 后生成器漏了什么"继续可见，pyd 差异以本注为准。

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

参数分类（1146 个参数实测，零误判）：`value 819 / obj 224 / uintptr 49 / cstr 28 /
bytes 19 / array 7`。判定必须**靠参数名**而非位置 —— 289 个回调里 150 个形如
`(NET_X *pInfo, LDWORD dwUser)`，那个整数是用户数据不是数量；且数量/长度关键词要 `$`
锚定在名字末尾：`nFileNum` 的第 4~6 字符忽略大小写正好凑出 `leN` 命中 `len`。

验证：端到端 `python/dhbind/tests/test_disconnect_callback_e2e.py`（真实 SDK 线程触发，参数全对）；
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

### 2. 作为结构体成员的函数指针字段（大华 301 个）

顶层回调已全部解决，但**结构体成员**里的函数指针仍按 `skip_funcptr` 跳过。绑成员回调要
`def_readwrite` + 生命周期托管（成员可能被 SDK 长期持有），与顶层回调是两个问题。
实际影响有限：业务代码基本都走 `CLIENT_xxx` 的顶层回调参数。

## 静默跳过（数据不完整）

### ~~3. 未知类型字段~~ ✅ 2026-10-04 归零（大华 0 / 海康 0）

四条根因全在 `common/parse.py` 的通用 C 语法层，与厂商无关（踩坑细节见
`implementation-notes.md` 第十节）：

| 根因 | 修法 |
|---|---|
| `strip_comments` 先块后行两趟，行注释里的 `/*` 被误当块注释开头，吞掉真代码（海康 `NET_DVR_ALARMHOST_NETPARAM_V50` 整个消失） | 单趟交替匹配 `/\*.*?\*/\|//[^\n]*` |
| `FP_RE` 要求调用约定宏后有空格，漏掉 `(CALLBACK* fXxx)` 无空格写法（大华 5 个 `fNotifyXxx`） | 宏后 `\s+` → `\s*` |
| `UNION_RE` 的 `[^{}]*` 抓不到体内嵌套花括号的 union（海康 2 个） | 改用平衡花括号扫描 |
| `FIELD_RE` 名字前 `\s+` 匹配不上 `unsigned char *in_buf`（5 个"空类型"实为字段名错、类型成空） | 星号并入分隔组 `[\s*]+` |

注释吞噬的修复还找回了被吞掉的字段：大华 62884 → 63353（+469）、海康 18639 → 18821（+182）、
海康结构体 +1。大华成员函数指针 296 → 301（5 个 `fNotifyXxx` 从"未知"转入此已知限制类）。

### 4. 位字段（大华 8 个）

`BYTE byImageQlty:7`。C 不允许对位字段取地址，nanobind 绑不了——**属 C 限制，不算偷懒**。

## 降级处理（绑了但只能「看」）

### 5. 非 char 数组、多维数组按 bytes（大华 6420 个）

拿到 `bytes` 需自己 `struct.unpack`。要转 list/numpy 的话在 `emit.gen_fields` 扩展。

### 6. 内嵌有名 struct/union 字段按 bytes

如 `stuOldLog`，需用户自己 `struct.unpack`.

### ~~7. 无 `.pyi` stub~~ ✅ 2026-10-04（`emit_stub.py`）；错误码仍是裸数字

IDE 补全已由随生成产出的 `{module}.pyi` 解决（pyd 同目录自动生效）。
剩余：厂商错误码无符号名，调用方只能拿到裸数字 —— 待错误码表（优先级表第 6 项高层封装）。

### ~~8. 函数调用持 GIL 阻塞其他线程~~ ✅ 2026-10-05（无条件 `gil_scoped_release`）

**决策**：native 只负责复刻 `ctypes.CDLL` 的语义 —— **每次外部调用都不持 GIL**；
线程安全 / 并发语义不在 native 职责内，由 Python 上层自己加锁。验收判据原文：
「只要能等比 ctypes 的效果就行，其他问题有 python 上层解决。我们 native 不考虑。」

**实现**：`native/codegen/common/parse.py` 的函数绑定模板给每个 `m.def` 尾部追加
`nb::call_guard<nb::gil_scoped_release>()`。落地范围：大华 2515/2515、海康 785/785，
等于全部函数绑定（`m.def` 计数逐一吻合）。

**为什么无条件、不挑"可能阻塞"的函数**：没法从声明上判断一个函数会不会长时间阻塞
（除了反编译拿绝对证据），按名字/形态挑必然漏。既然判据是"等比 ctypes"，就一律放。

**为什么安全**：`nb::call_guard` 被 nanobind 包在裸调用外层
（`nb_func.h`：`typename Info::call_guard::type g; (void)g; return func(args...);`），
guard 在**返回值转成 Python 之前**析构 —— 参数转换（Python→C）与返回值构造
（C→Python）仍持 GIL，释放只覆盖那一次 C 调用，与 ctypes 精确等比。

**排除项**（不能加 guard，因为会碰 Python 对象）：回调注册走 `m.attr`
（`common/emit.py` 的 `gen_callback_binding`），结构体字段访问器走 `nb::class_`。

**验证**：后台线程 tick 从 1 涨到 ~274（持 GIL 时被饿死 vs 释放后可跑）。

## 其他

- ~~两套回调注册表并存~~ ✅ 已收敛（2026-10-04）。手写版 `set_disconnect_callback`
  与 4 个 `_test_*` 转换探针已删除，回调统一走生成版。此前两套注册表独立，
  同一 SDK 订阅点混用会静默不触发。
- ~~手写 `unify_dh` 模块~~ ✅ 已删除（2026-10-05）。它的存在理由（登录释放 GIL、
  自动填 `dwSize`）已被生成版完全覆盖：函数绑定统一带 `gil_scoped_release`
  （见下节），结构体 `__init__` 自动填 `dwSize`。删除同时消除了 5 个类型
  （`EM_LOGIN_SPAC_CAP_TYPE` / `EM_LOGIN_TLS_TYPE` / `NET_DEVICEINFO_Ex` /
  两个登录结构体）在两份 pyd 里重复注册、后加载方静默丢属性的隐患。
- 生成物 `native/src/gen_dh/` 不入库（可重建），改代码请改 `native/codegen/` 下的源头。

## 优先级

| # | 事项 | 理由 |
|---|---|---|
| ~~1~~ | ~~回调~~ | ✅ 已完成 |
| ~~2~~ | ~~指针别名~~ | ✅ 已完成 |
| ~~3~~ | ~~未知类型归零~~ | ✅ 已完成（2026-10-04，根因见上）|
| ~~4~~ | ~~海康编译~~ | ✅ 已完成（2026-10-04，见上方海康覆盖边界表）|
| ~~5~~ | ~~`.pyi` stub~~ | ✅ 已完成（2026-10-04，`common/emit_stub.py`，随 gen_bind 自动产出）|
| 6 | **高层封装** | 错误码表、输出缓冲自动读回（技术债 #1）|
| 7 | **成员函数指针**（301 个）| 最贵，且要解决生命周期托管；实际影响有限 |
