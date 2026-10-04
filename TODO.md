# TODO

按「投入产出比」排序。每条都写清**能不能做、为什么**，避免变成一份做不动的愿望清单。

---

## 0. 项目结构的目标形态（先看清方向，再动手）

> 这一节是**为什么**，后面各项是**做什么**。动手前先确认形态没走偏。

### 0.1 问题不只是"文件夹没分层"

现在的形态更像「一堆脚本 + 一次性验证文件」，不像一个别人能装能用的库：

| 现象 | 现状 |
|---|---|
| 用户没有可 import 的入口 | 要用必须知道 `os.add_dll_directory` → `sys.path.insert(native/build)` → 手动构造结构体填 `dwSize` |
| Python 测试曾散在三处 | 顶层 `tests/` 已撤掉、模拟器代码已拆出 `e2e/simulator/server.py`；`native/smoke_test.py` 因构建需要留在 C++ 侧；`python/` 三层 tests 待填 |
| 手写与生成混在一层 | `native/src/dh_netsdk.cpp`（手写）与 `native/src/gen_dh/`（生成）职责已不同 |
| 没有对外承诺 | README 讲了怎么做，没讲"用户会得到什么" |

### 0.2 目标形态：四层产品结构

**四层是「产品分层」，不是目录分层** —— 回答的是"交付什么"，而不是"代码放哪"。
两者必须映射清楚，否则会出现"照着四层讨论功能、打开仓库却不知道放哪"的情况。

| 产品层 | 交付物 | 源码位置 |
|---|---|---|
| **第 1 层** C → pyd | `unify_dh_gen.pyd` / `unify_hk_gen.pyd` | `native/src/gen_dh/`（生成物，不入库）|
| **第 2 层** 大华厚封装 wheel | `dhbind` | `python/dhbind/` |
| **第 3 层** 海康厚封装 wheel | `hkbind` | `python/hkbind/` |
| **第 4 层** 跨厂商抽象 | `unify-netsdk` | `python/unify_netsdk/` |

第 4 层由本层 Python 判断该调哪个厂商，**用户层代码全部抽象、没有厂商方言**。

```
UnifyNetSDK/
├── native/                          # 第 1 层：C++ 绑定（nanobind）
│   ├── CMakeLists.txt / build.ps1
│   ├── codegen/                     # 构建期生成器：common/（通用语法）+ config/（厂商语义）
│   ├── src/dh_netsdk.cpp            # 手写部分（登录链路 / 排障工具）
│   ├── src/gen_dh/                  # 生成产物（不入库）
│   └── tests/                       # ★ 测本层
│       ├── conftest.py              #   fixture：SDK DLL 加载 / pyd 导入（缺厂商自动 skip）
│       ├── _paths.py                #   脚本阶段的路径 helper，转 pytest 后并入 conftest
│       ├── test_callbacks.py        #   289 个 bind_/set_ 分类 / 退订 / 异常隔离
│       ├── verify_runtime.py        #   两厂商 .pyd 读写往返【Phase 2 落地后退役】
│       ├── test_coverage_regression.py / test_structs.py / test_functions.py
│       └── e2e/                     # 端到端（需模拟器，默认不跑）
│           ├── simulator/server.py  #   模拟器胶水，从字符串字面量挪成真文件
│           └── test_login_callback.py
│
├── python/                          # 上层：三个待打包的包
│   ├── dhbind/                      # → 第 2 层，wheel 1
│   │   ├── __init__.py              #   加载胶水：add_dll_directory + 导出 API
│   │   ├── errors.py                #   大华错误码表
│   │   ├── client.py                #   大华版 Client（内部调 unify_dh_gen）
│   │   ├── _binding/                #   构建时填充：.pyd + 厂商 DLL（不入库）
│   │   │   ├── unify_dh_gen.cp313-win_amd64.pyd
│   │   │   └── dhnetsdk.dll / libeay32.dll / ...
│   │   └── tests/                   #   测本层：Client 流程 / 错误码 / outptr 读回
│   │
│   ├── hkbind/                      # → 第 3 层，wheel 2（同构，指向海康）
│   │   ├── ... 同上
│   │   └── tests/
│   │
│   └── unify_netsdk/                # → 第 4 层，wheel 3（纯 Python，无 .pyd）
│       ├── client.py                #   跨厂商 Client
│       ├── errors.py                #   统一异常
│       ├── _vendor/                 #   厂商探测与分发
│       │   ├── detect.py            #     协议探测 + 未安装时的提示
│       │   ├── dahua.py
│       │   └── haikang.py
│       └── tests/                   #   测本层：探测 / 分发 / 能力标注
│
├── tools/                           # 构建期：SDK 同步（sync_sdk.py）
├── pytest.ini                       # testpaths 与上面的树一致；e2e 默认不跑
├── docs/
└── TODO.md
```

**构建流程**：

```
native/codegen/gen_bind.py --sdk dahua
    ↓
native/build/*.pyd  +  vendor/dahua/sdk_win64/bin/*.dll      # 1. 两份产物（sync_sdk.py 同步副本）
    ↓
python/dhbind/_binding/                              # 2. 拷进胶水层
    ↓
bdist_wheel                                           # 3. 打包 → dhbind-1.0.0-cp313-win_amd64.whl
```

**要分的是「运行时」（C++ 绑定 + Python 上层）和「构建期」（生成器）**，不是简单按
语言分。生成器已从 `tools/` 迁入 `native/codegen/`：它的唯一产物就是
`native/src/gen_*`，与 CMakeLists / build.ps1 属同一条构建链，放在根目录平行于
`native/` 只会让"造弹药的"和"枪"看着无关。`native/smoke_test.py` 同样别为了整齐
挪走（构建流程要用它）。`tools/` 因此只剩 `sync_sdk.py`。

### 0.3 两个已定的决策

| 决策 | 结论 |
|---|---|
| 交付形态 | **wheel**。一个厂商一个 wheel（见第 6 节），`unify_netsdk` 是可选的上层抽象 |
| 平台范围 | 先只打通 **win_amd64 + cp313**，证明路线可行；多平台/多版本日后按需再扩 |

### 0.4 已定：上层做厚壳，核心是参数模型化

不做薄壳。厚壳 = 薄壳（加载 `.pyd` + dll 路径）+ 以下全部：

| 能力 | 说明 |
|---|---|
| **参数模型化（pydantic）** | ★ 核心，见 0.6 |
| 错误码转 Exception | 见第 5 节 |
| `outptr` 自动读回 | 见第 3 节 |
| 回调装饰器 | `@client.on_alarm` 之类，替代手工 `bind_fXxx` |
| `Client` 高层类 | 把"建连接→登录→订阅→预览"串成常规流程 |

**厚壳的形态是"层"，不是"替代"**：底层永远保留原始 nanobind 绑定
（`g.NET_xxx()` 照旧可用）。给需要精细控制的人，也避免老用户觉得"官方逼我改代码"。


### 0.5 一条设计原则（决定 `unify_netsdk` 怎么做）

厂商能力差异是**本质的**，不是接口没对齐。例：大华录像下载只支持同步，海康支持
异步 + 同步。所以 `unify_netsdk` 的接口必须**明确标注哪些是双厂商都支持的**，不要给一个
"看起来统一、实际某厂商上会 AttributeError"的假象。

### 0.6 参数模型化（pydantic）—— 厚壳的核心

**目标形态**：用户写 Python 调用，而不是手工填 C 结构体。

```python
# 现在
in_param = g.NET_IN_LOGIN_WITH_HIGHLEVEL_SECURITY()
in_param.szIP = '192.168.1.108'
in_param.szUserName = 'admin'
handle = g.CLIENT_LoginWithHighLevelSecurity(in_param, out)

# 目标
handle = client.login(LoginArgs(host='192.168.1.108', user='admin', password='...'))
```

`szIP` / `szUserName` 这种 Hungarian 命名对 Python 用户不友好，且 90% 字段根本不用填。

**三个必须先解决的问题**：

**① pydantic 模型不能直接当 C 结构体**（没有内存布局），中间必须有转换层：

```python
class LoginArgs(BaseModel):
    host: str
    port: int = 37777
    user: str = "admin"
    password: str = ""

    def to_struct(self):        # ← 关键
        s = g.NET_IN_LOGIN_WITH_HIGHLEVEL_SECURITY()
        s.szIP = self.host
        s.nPort = self.port
        ...
        return s
```

这层胶水**应当半自动生成**：大华命名规整（`sz`=字符串、`n`=数字、`by`=字节、`dw`=DWORD、
`st`=结构体、`f`=浮点），可写规则从 C 字段名推 Python 名，生成后人工校验。

**② 63353 个字段不可能全做**。只覆盖用户真实调用的操作：登录、预览、报警、布防、
录像查询、PTZ、云台 —— 几十个模型，覆盖 90% 需求。其余结构体保持原始绑定形态。

**③ pydantic 是第三方依赖，要不要强依赖**：

| 方案 | 优点 | 代价 |
|---|---|---|
| 强依赖 pydantic | 体验一致，模型开箱可用 | 轻量用户被迫装（几 MB）|
| **可选依赖** `dhbind[pydantic]` | 核心 API 零依赖 | 维护两套调用方式 |
| 用 dataclass 替代 | 标准库零依赖 | 无运行时校验、无 JSON schema |

**待定**：取决于想给什么样的用户体验 —— 参数校验（IP 格式、端口范围）在调用前就报错，
是厚封装的核心价值之一，那强依赖也说得通。

**验证方式**：先手工为"登录"写一个 `LoginArgs`（pydantic + `to_struct()`），确认形态
对了，再讨论怎么自动生成。形态不对时现在改成本最低。

厂商能力差异是**本质的**，不是接口没对齐。例：大华录像下载只支持同步，海康支持
异步 + 同步。所以 `unify_netsdk` 的接口必须**明确标注哪些是双厂商都支持的**，不要给一个
"看起来统一、实际某厂商上会 AttributeError"的假象。

### 0.7 待定：是否拆成多个 git 仓库（**框架搭出来后再讨论，现在不拆**）

> 之前讨论过"四层产品 = 四个独立 git 库"。**当前决定：先不拆，把框架搭出来再说**，为时不晚。

- **现状**：单一monorepo。已完成的是**目录与逻辑隔离**（`native/codegen/common` 只放通用语法与骨架、`native/codegen/config` 放厂商语义），**不等于仓库隔离**。
- **讨论时机**：等第 1 层 `.pyd` 编译通过、第 2/3/4 层的包骨架落地后再定。届时要回答：
  1. 拆分边界按**产品层**（第 1/2/3/4 层）还是按**运行时 vs 构建期**？
  2. `native/` 的绑定层同时服务两个 wheel，单独成仓还是留在某个 wheel 仓里？
  3. 生成器（现在在 `native/codegen/`）若要与 native 绑定分离成独立仓，依赖怎么表达（见第 6 节：倾向 PyPI，不用 submodule）。

---

## 1. 用 pytest 全面测试绑定层 ⭐

> 目标：在上层 Python 用 pytest 把头文件里的函数、结构体尽可能逐项测一遍。

### 1.0 测试分层约定（写任何测试之前先看这里）

仓库有**四个可独立交付的对象**：`native`（第 1 层 pyd）、`dhbind`、`hkbind`、
`unify_netsdk`。**每个对象的测试放在它自己的 `tests/` 下**，顶层不设 `tests/`：

| 对象 | 测试位置 | 测什么 |
|---|---|---|
| `native` | `native/tests/` | 绑定层：字段覆盖、回调分类、类型往返、函数可调 |
| `dhbind` | `python/dhbind/tests/` | 大华厚壳：Client 流程、错误码转换、`outptr` 自动读回 |
| `hkbind` | `python/hkbind/tests/` | 同上（海康）|
| `unify_netsdk` | `python/unify_netsdk/tests/` | 跨厂商：探测、分发、能力标注是否与实际一致 |

**为什么**：

1. 测试跟着被测对象走 —— 发布 `dhbind` 时不必捎上 `native` 的测试。
2. `conftest.py` **逐层生效**，所以每层的 SDK 加载与夹具各管各的，不需要在
   一个 conftest 里写"当前测的是哪一层"的分支。
3. 顶层 `tests/` 会退化成"混放"，过两年没人说得清哪个测试属于哪个 wheel。

**三条硬约定**（违反会真的坏事，不是风格问题）：

1. **叫 `test_*.py` 的文件必须是 pytest 测试**（含 `def test_*`）。手工脚本不许
   叫 `test_*.py` —— pytest 在 collection 阶段就 import 模块，顶层代码会被执行。
   刚发生过的真事：`test_login_callback.py` 顶层会 `Popen` 拉起模拟器并
   `sleep(20)`，跑一次 `pytest` 就意外启动外部进程并阻塞；而且因为没有
   `def test_*`，最后报的还是 `no tests collected` —— 副作用全占了，断言一个没跑。
2. **端到端测试必须标 `@pytest.mark.e2e`**。`pytest.ini` 已用
   `addopts = -m "not e2e"` 默认排除，因为它依赖项目外的 `Dahua_NVR_Simulator`。
3. **`pytest.ini` 的 `testpaths` 必须与 TODO 0.2 的目录树一致**。两处不同步的后果
   是"某些测试永远不跑"或者"跑进 vendor/ 里去"。

**待退役清单**（避免"落地了就忘"）：

| 文件 | 退役触发条件 | 退役后价值去哪 |
|---|---|---|
| `native/tests/verify_runtime.py` | `native/tests/test_structs.py` 落地并跑通（本节 Phase 2）| DLL 加载知识 → `conftest.py` 的 fixture；字段往返 → `test_structs.py` |
| `native/tests/_paths.py` | 三个脚本转成 pytest 之后 | 内容并入 `conftest.py` |

**在退役条件达成之前不要删** —— 海康 pyd 的编译推进中（第 2 节），
`verify_runtime.py` 是目前唯一能同时验证两个厂商 `.pyd` 可 import + 字段可读写
的跨厂商回归工具，删早了就没有替代品。同一约定也写在该文件的 docstring 顶部。

**新增测试时的自检三问**：① 测的是哪一层？放对目录了吗？② 它是 pytest 测试还是
手工脚本（决定文件名）？③ 依赖外部东西吗（决定要不要 marker）？

### 1.1 可行性结论：能测，但要先分清测什么

关键区分：**我们要测的是「绑定层有没有漏干活」，不是「大华 SDK 能不能用」。**

| 测什么 | 能不能测 | 价值 |
|---|---|---|
| **绑定层完整性**（字段有没有绑上、函数能不能调、参数转换对不对）| 能，且该测 | **高** —— 直接防回归 |
| **字段偏移 / 结构体大小** | 不该测 | 由 C++ 编译器保证，Python 侧测了是在测 nanobind |
| **设备功能**（登录出图、报警触发）| 需设备/模拟器 | 中 —— 关键路径已被端到端覆盖 |

前者 100% 可自动化、成本低；后者受设备限制。

### 1.2 分四阶段，按顺序做

#### Phase 1：覆盖边界断言（★ 最先做，成本最低价值最高）

把现有的 `native/codegen/check_coverage.py` 改写成 pytest 断言，让**手写数字变成自动防线**：

```python
def test_no_unknown_type_fields():            # 已归零（2026-10-04），此断言防回归
def test_callback_count_matches():            # 头文件 typedef 数 == bind_* 数（289/289）
def test_struct_field_total_not_shrinking():  # 防某次改动漏绑一大批
def test_skipped_counts_stable():             # 位字段(8)属 C 限制只能持平；函数指针(296)只能减少
```

**为什么最先做**：以后换 SDK 或改生成器，测试立刻告诉你「这次漏了什么」，
而不是靠人肉对比文档里的数字。

#### Phase 2：结构体冒烟（10557 个）

逐个结构体：构造不崩、`dwSize` 填对、每个字段可读写且写回原值往返。

```python
@pytest.mark.parametrize("name", ALL_STRUCT_NAMES)
def test_struct_smoke(name):
    cls = getattr(g, name)
    obj = cls()                          # 构造不崩
    if hasattr(obj, "dwSize"):
        assert obj.dwSize == EXPECTED_SIZE[name]   # dwSize 自动填对
    for f in FIELDS_OF[name]:             # 字段可读 + 写回原值往返
        assert getattr(obj, f) == getattr(obj, f)
```

**必须逐个跑，不能抽样** —— nanobind 的 `def_rw` 是模板胶水，一个能跑不代表
另一个能跑（本次那 6 个漏网的指针别名字段就是例证）。

#### Phase 3：函数签名冒烟（2515 个，**有风险**）

用「全 0 / 空指针」调用，检查不崩溃、返回合理错误码。

**必须先设计黑名单**，否则会真的改设备状态：`CLIENT_Reboot` / `CLIENT_Shutdown` /
`CLIENT_SetupAlarmChan` / `CLIENT_StartRecord` 之类有副作用的一律排除。也要接受
「部分函数传 0 会崩」——C API 常见，需逐个甄别。

**这是四阶段里最需要小心的**，建议先做一批试点摸清有多少函数能安全空参调用，
再决定是否全量跑。

#### Phase 4：设备功能测试

依赖 `Dahua_NVR_Simulator` 的实现程度。已覆盖登录 + 断线回调；待覆盖预览取流、
报警、布防、录像查询、PTZ。**上限取决于模拟器实现了多少**，不是绑定层能单独决定的。

### 1.3 需要的脚手架

- `native/tests/conftest.py`：**已建**，提供 `pyd(sdk)` fixture（导入 .pyd，缺厂商自动 skip）
- `native/tests/test_coverage_regression.py`：Phase 1
- `native/tests/test_structs.py`：Phase 2（**落地后按 1.0 的待退役清单处理 `verify_runtime.py`**）
- `native/tests/test_functions.py`：Phase 3
- 现有三个脚本转 pytest：`test_callbacks.py`（拆 6 个 test）、`verify_runtime.py`、`e2e/test_login_callback.py`（加 marker）。转正清单见 `native/tests/conftest.py` 的 docstring

**结构体/函数清单从哪来**：让生成器输出 `gen_manifest.json`（名字 + 跳过原因 +
字段列表），测试直接读它，免得测试里再解析一遍头文件。

一份数据两用：现在 `emit.py` 的分片 diff 用的是 `_gen_manifest.json`（只有文件名
hash，用于估算编译量），扩展成带字段列表的 manifest 后，同一个文件既服务编译期
diff，也服务测试期断言。

### 1.4 现状

- `native/codegen/check_coverage.py` 已能输出完整覆盖边界，Phase 1 只需把数字改成断言
- `native/tests/` 已就位（`conftest.py` + `_paths.py` + 三个脚本 + `e2e/`），顶层 `tests/` 已撤掉
- `pytest.ini` 已就位但 **`pytest` 依赖尚未加入**，所以那三个脚本目前不被 pytest 收集（它们也没有 `def test_*`）
- 海康 `.pyd` 已能 import 并通过字段往返：`native/tests/verify_runtime.py` 报 72.2 MB / 3824 导出 / 26 回调（此前卡住的 121 个编译错误已解决）

---

## 2. 海康接 CMake 编译 ✅ 已完成（2026-10-04）

原计划是验证 `common/` 真的与厂商无关（当时生成器 dry-run 通过但编译不过，
121 个错误：Linux 条件分支里的 `DC`/`INITINFO`/`PLAYRECT` 类型被无条件生成、
二维数组参数、输出指针分类）。**现已全部解决** —— `unify_hk_gen.pyd`
72.2 MB / 3824 导出 / 26 回调，import + 字段往返都正常，跑
`native/tests/verify_runtime.py` 即可复核。

**留下的海康遗留**：26 个回调走保守退化 —— `config/haikang.py` 故意**不设**
`cb_qty_pred` / `cb_count_pred`，所以不识别数组、结构体指针只给单对象。这是有意的：
大华那套"靠参数名猜数量"的规律照搬过来只会误判（海康回调命名风格完全不同）。
等接上设备、拿到实际回调行为后照事实写规则 —— 那时才叫"我们吃苦"。
**少给可接受，给错无法排查。**

---

## 3. 输出指针（outptr）自动读回

`outptr` 现在暴露成 `int` 地址，调用后要自己 `ctypes` 预分配缓冲再读回，属于
「能用但别扭」。做完后 Phase 3 的函数测试会简单很多 —— 否则每次都要手工配缓冲。

---

## 4. 未知类型归零（大华 6 个 + 海康 7 个）✅ 已完成（2026-10-04）

实际根因比预想多——不止 `FP_RE` / `FIELD_RE` 两处，共 4 条，全在 `common/parse.py`
的通用 C 语法层：注释剥离顺序（行注释里的 `/*` 被误当块注释开头，吞掉真代码）、
`FP_RE` 调用约定宏后要求空格、`UNION_RE` 抓不到嵌套花括号、`FIELD_RE` 匹配不上
`*` 紧贴字段名的写法。明细与修法见 `binding-tech-debt.md` 和
`implementation-notes.md` 第十节。附带收益：注释修复找回 651 个此前被吞的字段。

---

## 5. 错误码转 Exception

把裸数字错误码变成可捕获的异常。上层 Python 的核心价值之一，也是"用户不必自己
查厂商错误码表"的前提。

落地时要定三件事：

| 决策 | 选项 |
|---|---|
| 异常粒度 | 统一 `NetSdkError(code, name, message)` / 按类别细分（登录失败、网络、参数、状态）|
| 触发方式 | 显式 `check_error()` 调用 / 包装层自动检查每次调用结果 |
| 错误码表来源 | **建议从 `dhnetsdk.h` 自动生成** —— 扫 `NET_xxx_E` 系列宏/枚举，生成字典 + 异常类，和绑定同步更新 |

自动生成能覆盖"有符号名"的错误；厂商很多错误是裸数字无符号名，那部分仍需按文档补。

---

## 6. 打包与分发

目标形态（已确认）：

- **一个厂商一个 wheel**：`dhbind` 只含大华、`hkbind` 只含海康。
  理由是厂商 DLL 体积大，捆一起会让只需要单家的用户白下载另一家的 SDK。
- **`unify_netsdk` 是可选的上层抽象**：依赖厂商 wheel，抽象掉厂商差异。
  用户不需要 `unify_netsdk` 时可以只装 `dhbind` 自己拼，自由度最高。
- **平台范围先只打通 `win_amd64` + `cp313`**，证明整条路线可行，多平台/多 Python
  版本日后按需再扩。
- `unify_netsdk` 的 `pyproject.toml` 写清版本依赖限制，三个包用同一套版本号
  （避免"dhbind 能装、hkbind 装不上"）。

DLL 加载：随 wheel 打包，import 时由包自己 `os.add_dll_directory` 指向包内目录。
**大华官方 Python SDK 也是这么做的**（手动 add dll path），所以这是厂商生态的
既有做法，不是我们自创的负担。


**厂商探测**（`unify_netsdk` 在 login 前判断设备是哪家）：两家协议天差地别（大华
`0xA0 0x01` realm 挑战 vs 海康完全不同），端口探测能可靠区分。两个边界：

- **防火墙可能 DROP 未登记端口** → 探测超时。错误信息必须区分「探测到海康但没装
  hkbind」（提示 pip install hkbind）与「探测无响应」（提示用 Unify(vendor=...)
  显式指定），否则用户会卡在"探测失败"上。
- **探测只做到协议层，不带凭据**。纯协议探测不需要认证就安全；若实现成"直接尝试
  登录"会消耗认证次数，甚至触发设备锁定。

**不要用 git submodule 做多仓协作**。submodule 要管 .gitmodules、克隆时
--recursive、子模块提交冲突，对 Python 项目没有必要。真要拆成多仓就用 **PyPI 发布**
表达依赖关系（生成器可独立成一个包，别人可能复用）。
---

## 7. `.pyi` stub

纯生成工作，IDE 补全 + 错误码有类型。与 pytest 无关，但两者都依赖「从 IR 生成
元数据」，可以合并成同一个生成步骤。



## 8. 那个大华模拟器有空了fork一下，后面还要实现录像下载。
然后记得还有海康模拟器，上网搜一搜有没有现成的。

## 9. `dh_netsdk.cpp` 的定位与清理

它是"GIL 安全的阻塞调用封装"（第 2 层 `dhbind` 的 C++ 侧），两件事没做完：

- **接线**：里面的登录链路要接到 `python/dhbind/client.py`，成为 `Client.login()`
  的底层实现。释放 GIL + 填 `dwSize` 这两件它已经做了，缺的是 Python 侧去调它
  （现在是 `native/tests/e2e/test_login_callback.py` 在直接用生成版 pyd 绕着走）。
- **清理**：`_test_gil_*` 两个探针无人使用，可移除。
