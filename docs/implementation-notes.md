# 实现笔记：实测踩出来的坑

> 2026-10-04 做「289 个回调绑定」时踩出来的结论。每条都是 **现象 → 根因 → 正确做法**，
> 报错信息均为原文。**多数不在官方文档里**，属于踩一次记一次。
>
> 涉及四层：nanobind / CPython C API / MSVC+Windows / 大华 SDK。
> 后三者叠加时症状互相伪装，本文按"最终定位点"归类。

---

## 一、nanobind

### 1.1 `m.def` 不能绑"已经构造好的 callable"

**现象**
```
nb_func.h(445): error C3556: "detail::api<handle>::operator ()": "decltype"的参数不正确
nb_func.h(447): error C2955: "analyze_method": 使用类模板需要模板参数列表
```

**根因**　`m.def(name, f)` 走 `analyze_method<decltype(&F::operator())>` 提取**函数签名**，
好让 Python 侧有 `__doc__` / 关键字参数名。传进去的如果是**类型擦除后**的
`nb::object`（`nb::cpp_function(...)` 的返回值），已经没有签名可提取了。

**做法**　已构造的 callable 用属性赋值，两者对 Python 侧完全一样：

```cpp
// 命名空间带项目前缀：曾用 cbrt（callback runtime 缩写），但 <math.h> 里
// 有 double cbrt(double)，MSVC 报 C2757 "该名称的符号已存在"。
m.attr("bind_fRealDataCallBack") = unifycb::binder("fRealDataCallBack", (void*)&thunk);
// Python: g.bind_fRealDataCallBack(cb)  ← 一样是普通函数
```

**判断依据**　有签名的 lambda 用 `m.def`；`nb::object` / 包装器用 `m.attr`。

---

### 1.2 `nb::borrow<T>()` **不持引用** —— 头号杀手

**现象**　绑定层一切正常，但一回调就 `0xC0000005`（访问冲突）。
二分发现：空注册表时不崩、绑了回调就崩；二分到"参数转换 OK / 调用回调崩"；
再用"模块级函数（永不被回收）也崩"排除了悬垂指针，最后定位到 `PyObject_CallObject`
（见 2.1）—— 但**修 2.1 之前，先踩的是这个坑**。

**根因**
```cpp
registry().emplace(name, nb::borrow<nb::object>(cb));   // borrow_t: 不 inc_ref
```
`nb::borrow` 走 `borrow_t` 构造，**不增加引用计数**。Python 侧
`bind_fXxx(lambda: ...)` 返回后 lambda 被回收，注册表里就是野指针。

**做法**　注册表按值持有，把所有权接过去：
```cpp
inline void set(const char *name, nb::object cb) {   // 参数按值
    registry()[name] = std::move(cb);                 // 转移进容器
}
```

> `nb::object` 没有"从单个 handle"的隐式构造（`C2665`）。要自己 inc_ref 就写
> `nb::borrow<nb::object>(h)` + `holder.inc_ref()`，别写 `nb::object(h)`。

---

### 1.3 `nb::object` / `nb::handle` 都**不接受 None**

**现象**
```
TypeError: fDataCallBack(): incompatible function arguments.
    1. fDataCallBack(arg: object, /) -> int
  Invoked with types: NoneType
```

**根因**　它们的 caster 是 `from_python() { if (!isinstance<T>(src)) return false; }`，
而 `nb::object` / `nb::handle` 没有 `handle_type`，`isinstance` 恒为 false。

**做法**　退订用**独立的零参函数**，别用 `None` 当哨兵：
```python
g.unbind_fRealDataCallBack()      # 而不是 g.bind_fRealDataCallBack(None)
```
类型安全，语义也更清楚。

---

### 1.4 `nb::object` 作为**返回值**时要求 `isinstance`

**现象**　回调 `return None` / `return "x"` → `bad cast`；`return 0` 却正常。

**根因**　同 1.3，`type_caster<nb::object>::from_python` 要求
`isinstance<nb::object>(src)`。`0` 恰好能过 isinstance 检查（它有 caster），
`None` / `str` 过不了。

**做法**　**绕过 nanobind 的返回值转换**：参数仍由 nanobind 转好
（`nb::cast` / `nb::bytes` / `nb::list`），最后用 CPython 的
`PyObject_Vectorcall` 调，**直接丢弃返回值**。这样返回什么都接受、行为可预测。
（需要返回值时用 `PyLong_Check` 手动取，见 `dh_bind_cb.h` 的 `DH_CB_RET`。）

---

### 1.5 `nb::print` 只收**单个** handle

**现象**　`error C2661: "nanobind::print": 没有重载函数接受 4 个参数`

**根因**　签名是 `print(handle value, handle end = handle(), handle file = handle())`，
后两个参数是"批量打印的结束位置 / 目标文件"，**不是拼接**。

**做法**　先 `snprintf` 成一个 C 字符串再 `nb::print(buf)`。

---

### 1.6 `gil_scoped_acquire` 可重入

`nb::gil_scoped_acquire` = `PyGILState_Ensure`，**同一线程连续 acquire 两次不会崩**
（实测通过）。它内部的 `NB_CALL(tstate_ensure)` 是 nanobind 的 backend slot，
import 时填充，worker 线程上可正常调用。

---

### 1.7 `nb::cast` 在 worker 线程可用

只要**持有 GIL**，`nb::cast(long long)` / `nb::bytes(p, n)` 在裸 `std::thread` 上
实测正常（`got=[4660]`）。`nb::cast` 内部**不** acquire GIL——头文件里
`gil_scoped_acquire` 只出现在 `nb_misc.h` 的类定义处，无人调用。

**但** `nb::cast` 返回的是**原始类型**，`nb::object args[] = { nb::cast(x), ... }`
靠 `nb::object` 的模板构造二次转换，能编译通过且运行正常。

---

## 二、CPython C API

### 2.1 `PyObject_CallObject` 第二参数是 **tuple**（最隐蔽）

**现象**　`0xC0000005`，崩在调用 Python 回调处。二分定位很干净：
只构造参数数组 → 正常；同一数组 + `PyObject_CallObject` → 崩。

**根因**　名字有迷惑性，但文档写得很清楚：
> `PyObject* PyObject_CallObject(PyObject *callable, PyObject *args)`
> **Call a callable object with the argument tuple args.**

`args` 是**已经构造好的 tuple**，不是 execl 风格的 NULL 结尾数组。
传 `PyObject*[]` 进去，CPython 会去读首元素的 `ob_size` 当 tuple 长度 → 垃圾值 → 崩。

**做法**
```cpp
PyObject_Vectorcall(fn.ptr(),
                    reinterpret_cast<PyObject *const *>(args),  // 已有数组
                    n,                                        // 显式个数
                    nullptr);                                  // 无关键字
```
`PyObject_Vectorcall` 直接吃"数组 + 个数"，正是我们手上有的东西，
连中间的栈/vector 搬运都省了。

---

### 2.2 `PyObject_Call` 第三参数在 3.13 是 `kwargs`

```c
PyObject* PyObject_Call(PyObject *callable, PyObject *args, PyObject *kwargs);
```
不是 `nargs`。想传"数组 + 个数"只能走 `PyObject_Vectorcall`。

---

### 2.3 判断"线程是否已附着"用 `PyThreadState_GetUnchecked()`

**不要用 `PyGILState_Check()`**。它的实现是
`tstate != NULL && tstate->gilstate_counter > 0`，而**调用方自己 swap 进去的
tstate 的 `gilstate_counter` 是 0**（ctypes 的 `CFUNCTYPE` 回调就是这样），
于是会误报"无 GIL" → 再次 attach → `Fatal Python error: _PyThreadState_Attach:
non-NULL old thread state`。

```cpp
inline bool attached() { return PyThreadState_GetUnchecked() != nullptr; }
```
三种场景都正确：SDK 工作线程（无 tstate → attach）/ ctypes 回调（自带 tstate →
不 attach）/ Python 主线程（有 tstate → 不 attach）。

---

## 三、MSVC / Windows

### 3.1 `small` 是 Windows 头里的宏

**现象**　`error C2062: 意外的类型"char"`，报在完全无辜的一行。

**根因**　`#define small char`（来自 objbase / rpcndr），于是
```cpp
PyObject *small[12];      // → PyObject *char[12];
```
参数暂存数组**必须改名**（`stack_args`）。

---

### 3.2 `reinterpret_cast` 不能作用于常量表达式

`nb::cast(reinterpret_cast<std::uintptr_t>(0))` → `C2440 无法从 int 转换为 uintptr_t`。
MSVC 拒绝把 `reinterpret_cast` 用在常量上。生成代码里传的是变量所以没事，
但写示例/探针时会撞上。改用变量或直接 `nb::cast(0)`。

---

### 3.3 生成的 C++ 必须**纯 ASCII**

MSVC 对非 ASCII 源文件可能报 C4819；而 `write_if_changed` 用
`open(..., encoding='ascii')`，是**写到第一个非 ASCII 字符才抛**
`UnicodeEncodeError`，报错里完全看不出是哪句注释。

**做法**　生成代码的注释一律 ASCII，中文说明留在 Python 侧 docstring；
并在 `write_if_changed` 里加前置断言，把失败点连同上下文一起报出来。

---

### 3.4 C++ 不允许在函数体内定义函数

生成 thunk 时若缩进进了 `init_cbsNNN()` 里：
```
error C2267: "dh_thunk_xxx": 具有块范围的静态函数非法
error C2601: "dh_thunk_xxx": 本地函数定义是非法的
```
thunk 必须在**文件作用域**，`init` 里只放注册语句。

---

## 四、大华 SDK 头文件的脾气

### 4.1 指针有两种写法，`LPNET_X` 不是 `NET_X *`

```c
typedef void (CALLBACK *fQueryRecordFileCallBack)(
    LLONG lQueryHandle, LPNET_RECORDFILE_INFO pFileinfos, int nFileNum, ...);
```
厂商大量直接用**指针别名**（`*LPNET_XXX`），类型名里**没有 `*`**。
只按 `ptr = '*' in type` 判断，会把指针当成**传值结构体**：

- 后果：`static_cast<NET_X>(0x1234)` 之类编译错误；数组判定失效
- 修法：`_split_decl_names` 改为返回 `(类型名, 指针别名)`，别名进 `ptr_aliases` 集合
- 实测影响：`value 824→820`、`obj 222→226`、`array 5→7`

### 4.2 `LDWORD dwUser` 是**用户数据**，不是数量

289 个回调里 **150 个**形如：
```c
(..., NET_VIDEOANALYSE_STATE *pAnalyseStateInfos, LDWORD dwUser)
```
"指针后面跟个整数就当数组"会把这 150 个全误判。

### 4.3 `nBufLen` / `dwBufSize` 是 **sizeof 字节长度**，不是元素个数

```c
fAddFileStateCB(..., NET_CB_ADDFILESTATE *pBuf, int nBufLen, ...)            // 单结构体 + 字节长度
fNotifyCarPassInfo(..., NET_CAR_PASS_INFO *pstuCarPassInfos, int nInfoNum, ...) // 数组 + 元素个数
```
按数组处理会越界读。所以只认 `Num|Count`（排除 `Len|Size`）。

### 4.4 数量/长度关键词**必须 `$` 锚定在名字末尾**

`nFileNum` 的第 4~6 个字符是 `l`、`e`、`N`（`nFi**leN**um`），忽略大小写后
**正好凑出 `len`**，命中长度关键词 → 数组语义被吃掉。末尾锚定后
`nInfoNum` / `nBufLen` / `dwBufSize` / `nItemCount` 都仍正确。

**统计口径**（289 回调 / 1146 参数，零误判）：
`value 819 / obj 224 / uintptr 49 / cstr 28 / bytes 19 / array 7`

### 4.5 `dwUser` 就是传给注册函数的那个值

端到端实测：`CLIENT_Init(cb_addr, 0x1234)` → 回调收到 `user=4660`（=0x1234）✓
这是验证参数透传是否正确的天然断言。

---

## 五、ctypes 的限制

`ctypes.CFUNCTYPE` 回调会**自建并 swap 一个 thread state**，导致 2.3 的判据误判，
进而二次 attach 崩溃。所以 **ctypes 无法验证"无 GIL 线程调 thunk"** 这条路径。

这也是 selftest 钩子（`_selftest_fXxx`）存在的唯一理由：从裸 `std::thread` 调 thunk。
钩子现在**默认生成**（`--no-selftest` 可关，省 1.5 MB 产物），因为绑定层
`test_callbacks.py` 依赖它；端到端 `test_login_callback.py` 覆盖的是另一条路径 ——
真实 SDK 工作线程进 thunk。

---

## 六、线程与死锁

### 6.1 `join()` 之前必须释放 GIL

**现象**　进程不死但完全卡住：`CPU=0.015s, threads=3`，日志停在调用点。

**根因**
```
主线程: 持 GIL ──▶ std::thread 创建 ──▶ join() 等待
worker : 需要 GIL ◀─┘                    ↑ 互等
```

**做法**
```cpp
std::thread t([&]{ thunk(); });
{
    nb::gil_scoped_release rel;   // 先放 GIL
    t.join();
}
```
真实 SDK 路径不会这样（注册完就返回、顺带释放了 GIL），但**自测脚手架必须模拟
那个释放动作**，否则根本测不出来。

> 顺带一提：这个死锁本身就是"thunk 确实在 acquire GIL"的证据。

---

---

## 七、SDK 日志里的 warning 不等于错误

**这条单独记，因为它已经害我误判过一次。**

打开 SDK 日志（`CLIENT_LogOpen`）后会看到这几行：

```
[error] OpensslMgr.cpp:866] load rsa encode failed
        LibtinyPath = ...\tinyRSA.dll
```

**它不是登录失败的原因。** Gen2 登录实测正常（`nError == 0`，见
`native/tests/e2e/test_login_callback.py`）。

事实与来源要分清：

| 结论 | 来源 | 强度 |
|---|---|---|
| `tinyRSA.dll` 只是挂载（可选依赖），挂不上仅产生 warning | 上一个 AI 反编译 `OpensslMgr` 得到的机制结论 | 本人**没有独立复验**，仅转述 |
| Gen2 登录成功、`nError == 0` | 本轮端到端实测 | **已验证** |

**曾犯的错**：早期看到这行 warning，我据此断定"Gen2 登录走不通"，还打算改用旧式
digest 绕道；后来登录实测通了，却没回头修正这个结论，甚至又拿它当"wheel 打包
风险"讲了一遍。

**给后来人的规则**：

1. SDK 日志里 `[error]` 字样的行**不等于**这次调用失败了。先看**实际返回码**
   （`nError` / `CLIENT_GetLastError()`），以它为准。
2. 看到可疑 warning 时，先跑一遍端到端确认功能是否真的不通，再决定要不要当根因。
3. 判断根因要求**能解释失败现象**。一条与失败现象无关的 warning，即使它字面写着
   `error`，也不是根因。

---

## 八、工程：编译时间

| 操作 | 耗时 |
|---|---|
| 全量（160 TU / 62884 字段 / 125 结构体分片） | **612 s** |
| 改依赖图导致的重编（95 TU） | **523 s** |
| 增量：只改回调分片 | **7–12 s** |
| 增量：只改手写模块单文件 | **3 s** |

三条来之不易的结论：

1. **回调运行时头（`dh_bind_cb.h`）只能被 `*_cbsNNN.cpp` include**。
   混进公共 `make_includes` 会让它一改就把 146 个结构体/枚举/函数分片全部拖去重编
   （12 分钟 vs 7 秒）。所以 `emit.py` 里 `make_includes` 与 `make_cb_includes`
   是分开的，别合并回去。
2. **`write_if_changed`**：内容不变不重写文件、不动 mtime，ninja 直接跳过整个分片。
   生成器每次全量重写的话，mtime 全变 → 每次都全量重编。
3. **改 `build_deps` / `topo_order` 这类影响全局顺序的逻辑 = 一次性全量重编**。
   把指针别名纳入依赖图后，依赖拓扑序变了，95 个分片的内容跟着变 → 523 s。
   这类代价是**一次性**的：顺序稳定之后再改单个字段只重编那一个分片。
   但要预先知道，别以为是"改一行怎么编了 8 分钟"。

### 8.1 预研：合成基准（`bench_nanobind/`，2026-10-04 已删除）

在真实分片方案定下来之前，"62884 个字段全绑会不会把编译拖垮"是没有答案的。
当时用**合成 probe** 做了一次成本预研（目录已删除，结论保留下列）：

| | |
|---|---|
| **做法** | 造 4 个只含大华头文件、不含真实逻辑的合成 TU，分别绑 0 / 506 / 2005 / 5014 个字段；单文件计时；最小二乘拟合 `t = 固定 + 每字段 × N`；外推到 61881（大华全量）与 82755（大华+海康）字段（当时口径；最终实测 62884 / 81523）|
| **结论** | 可行，编译时间在可接受范围 |
| **印证** | 真实产物随后直接验证了这一点：拆成 125 个分片后全量 612 s（上表），而不是单文件几十分钟 |

**为什么删掉**：合成基准唯一的优势是"干净"（不含 SDK 逻辑、不含回调运行时），
而真实 `unify_dh_gen.pyd` 早就能直接测了 —— 预研阶段结束，对照组失去意义。
它剩下的唯一价值是"换绑定库（nanobind → pybind11）时做 A/B 对比"，但那需要的是
**变量隔离**，这个目录并不自动提供；真要做，重写 30 行 probe 也就十几分钟。

**教训（这次真踩了）**：预研的**结论要当场落盘**。这个基准跑完只留下一个被掐断的
`r500.log` —— 连 `build_measure.ps1` 的 RESULT 表都没打出来，拟合系数至今无法
复原，只能靠真实产物反推。**别把"我看过一眼"当成结论。**

---

## 九、生成代码的自我约束

1. **thunk 一律 `static`**，定义在文件作用域；`init_cbsNNN()` 里只放 `m.attr(...)`。
2. **注册用 `m.attr`**，不用 `m.def`（见 1.1）。
3. **注释一律 ASCII**（见 3.3）。
4. **注册表故意泄漏**：`static auto *r = new std::unordered_map<...>()`。
   否则模块卸载时（解释器已部分销毁）跑 `~nb::object` 会 `0xC0000005`——
   而且是**在脚本已经打印完结果之后**才崩，最难查。退订靠 `unbind_fXxx`。
5. **回调对象是借用视图**：`nb::cast(ptr)` 不拥有内存，SDK 回调返回后底层缓冲即失效。
   上游必须在回调内取走字段。文档和测试都按这个语义写。

### 改了生成器之后的工作流（别再跳过）

`build.ps1` **只编译、不生成**（生成是 `native/codegen/gen_bind.py` 的事）。所以改完
`native/codegen/common/*.py` 直接编译，等于拿旧产物编了一遍——字段根本没进 pyd，
验证脚本会报 `hasattr(...) == False`，而根因在生成流程，不在绑定代码。

正确顺序：

完整命令序列见 `onboarding.md` 第四节（① 重新生成 → ② `Select-String` 确认生成物 →
③ 编译 → ④ 验证），不在此重复。

第 2 步是这轮踩出来的：指针别名修复后直接让用户编译，`.pyd` 里
`NET_IN_DOWNLOAD.lpRecordFile` 压根不存在，而我已经开始写"验证字段是否可用"
的脚本了。**先确认生成物，再编译，再验证**。

同理，**关掉某个生成开关时，要检查依赖它的脚本**。早年 `--emit-selftest` 默认
关闭的阶段，`native/tests/test_callbacks.py` 依赖的 `_selftest_fXxx` 就没了，跑到
第一个用例直接 `AttributeError` traceback，看不出是"忘了加开关重新生成"。该脚本
开头会检测并打印重生成命令。现在钩子默认生成，只有带 `--no-selftest` 重新生成
才会复现这个问题。

