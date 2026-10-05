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
| Python 测试曾散在三处 | 顶层 `tests/` 已撤掉、模拟器胶水已拆出并归到 `python/dhbind/tests/simulator/server.py`（e2e 归 python 层）；`native/smoke_test.py` 因构建需要留在 C++ 侧；`python/` 三层 tests 待填 |
| ~~手写与生成混在一层~~ | ✅ 已解决（2026-10-05）：手写 `native/src/dh_netsdk.cpp` 删除，只剩 `native/src/gen_dh/`（生成）|
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
│   ├── src/gen_dh/                  # 生成产物（不入库；手写 dh_netsdk.cpp 已删）
│   └── tests/                       # ★ 测本层（只测绑定层，不做 e2e）
│       ├── conftest.py              #   fixture：SDK DLL 加载 / pyd 导入（缺厂商自动 skip）
│       │                            #   （原 _paths.py 内容，2026-10-05 并入）
│       ├── _manifest.py             #   gen_manifest.json 读取器（Phase 2/3 共用）
│       ├── _zeroarg_sweep.py        #   空参扫描执行体（必须子进程跑，见 test_functions）
│       ├── test_callbacks.py        #   289 个 bind_/set_ 分类 / 退订 / 异常隔离
│       ├── test_coverage_regression.py  # 头文件 -> pyd 覆盖边界断言（Phase 1）
│       ├── test_structs.py          #   Phase 2：逐个结构体冒烟
│       ├── baseline_sizes.json      #     committed golden：dwSize + 已知不可读字段
│       └── test_functions.py        #   Phase 3：逐个函数空参冒烟（子进程隔离防崩）
│
├── python/                          # 上层：三个待打包的包
│   ├── dhbind/                      # → 第 2 层，wheel 1
│   │   ├── __init__.py              #   加载胶水：add_dll_directory + 导出 API
│   │   ├── errors.py                #   大华错误码表
│   │   ├── client.py                #   大华版 Client（内部调 unify_dh_gen）
│   │   ├── _binding/                #   构建时填充：.pyd + 厂商 DLL（不入库）
│   │   │   ├── unify_dh_gen.cp313-win_amd64.pyd
│   │   │   └── dhnetsdk.dll / libeay32.dll / ...
│   │   └── tests/                   #   测本层：Client 流程 / 错误码 / e2e（连模拟器）
│   │       ├── simulator/server.py  #     模拟器胶水（e2e 归本层，2026-10-05 从 native 搬来）
│   │       ├── test_client_e2e.py   #     e2e：登录/登出（@pytest.mark.e2e，默认不跑）
│   │       └── test_disconnect_callback_e2e.py  # e2e：真实 SDK 线程 -> thunk -> GIL
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
| 交付形态 | **wheel**。一个厂商一个 wheel（见第 4 节），`unify_netsdk` 是可选的上层抽象 |
| 平台范围 | 先只打通 **win_amd64 + cp313**，证明路线可行；多平台/多版本日后按需再扩 |

### 0.4 已定：上层做厚壳，核心是参数模型化

不做薄壳。厚壳 = 薄壳（加载 `.pyd` + dll 路径）+ 以下全部：

| 能力 | 说明 |
|---|---|
| **参数模型化（pydantic）** | ★ 核心，见 0.6 |
| 错误码转 Exception | 见第 3 节 |
| `outptr` 自动读回 | 见第 2 节 |
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
  3. 生成器（现在在 `native/codegen/`）若要与 native 绑定分离成独立仓，依赖怎么表达（见第 4 节：倾向 PyPI，不用 submodule）。

---

## 1. 用 pytest 全面测试绑定层 ⭐（Phase 1/2/3 ✅ 2026-10-05；Phase 4 待模拟器）

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
   真事（已修复）：`test_login_callback.py` 顶层曾 `Popen` 拉起模拟器并 `sleep`，
   跑一次 `pytest` 就意外启动外部进程并阻塞；而且因为没有 `def test_*`，最后报的
   还是 `no tests collected` —— 副作用全占了，断言一个没跑。现已转正为
   `python/dhbind/tests/test_disconnect_callback_e2e.py`（e2e 归 python 层）。
2. **端到端测试必须标 `@pytest.mark.e2e`**。`pytest.ini` 已用
   `addopts = -m "not e2e"` 默认排除，因为它依赖项目外的 `Dahua_NVR_Simulator`。
3. **`pytest.ini` 的 `testpaths` 必须与 TODO 0.2 的目录树一致**。两处不同步的后果
   是"某些测试永远不跑"或者"跑进 vendor/ 里去"。

**e2e 归 python 层**：`native`（pyd）与 `python`（wheel）两个层级产物本质同构，
但"连模拟器"这件事放在 python 层那三个 wheel 里更有归属性 —— native 只测绑定层
本身，不做 e2e。原 `native/tests/e2e/` 已整目录删除。

**已退役的脚本**（2026-10-05，三个脚本全部转正）：

| 文件 | 去向 |
|---|---|
| `native/tests/verify_runtime.py` | → `test_runtime_roundtrip.py`（2026-10-05 转正）→ **已退役**（2026-10-05）：字段往返并入 `test_structs.py`，类型通道（`char[N]`→str / `BYTE[N]`→bytes）、枚举注册、SDK 版本号断言分别并入 `test_structs.py` / `test_functions.py` |
| `native/tests/_paths.py` | 内容并入 `native/tests/conftest.py` |
| `native/tests/e2e/test_login_callback.py` | 转正为 `python/dhbind/tests/test_disconnect_callback_e2e.py`（e2e 归 python 层）|

`native/tests/` 现在只有：`conftest.py`、`_manifest.py`、`_zeroarg_sweep.py`（后两个是
辅助模块，不叫 `test_*` 所以不被收集）、`test_callbacks.py`、`test_coverage_regression.py`、
`test_structs.py`（+ `baseline_sizes.json`）、`test_functions.py`。

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

#### Phase 1：覆盖边界断言（★ 最先做，成本最低价值最高）✅ 2026-10-05

把现有的 `native/codegen/check_coverage.py` 改写成 pytest 断言，让**手写数字变成自动防线**：

```python
def test_no_unknown_type_fields():            # 已归零（2026-10-04），此断言防回归
def test_callback_count_matches():            # 头文件 typedef 数 == bind_* 数（289/289）
def test_struct_field_total_not_shrinking():  # 防某次改动漏绑一大批
def test_skipped_counts_stable():             # 位字段(8)属 C 限制只能持平；函数指针(301)只能减少
```

**为什么最先做**：以后换 SDK 或改生成器，测试立刻告诉你「这次漏了什么」，
而不是靠人肉对比文档里的数字。

**落地情况**（`native/tests/test_coverage_regression.py`，8 passed = 4 断言 × 2 厂商）：
- `check_coverage.py` 拆成纯函数 `collect(sdk)` + `report(c)` + `main()`。
  拆分前它 import 就 argparse、还改 `sys.stdout`，没法被测试复用。打印文案逐字未动
  （改前改后输出做过逐字比对），所以 README / debt 文档里的数字口径不变。
- 断言与打印**共用同一个 `collect()`**：口径只有一处，两边不会漂。
- 基线数字写在测试的 `BASELINE` 里，方向性断言：完全对上的只增不减，跳过的只减不增。
- 该测试只解析头文件与生成物、不 import pyd，所以不需要 `pyd` fixture。

#### Phase 2：结构体冒烟（10557 + 2668 个）✅ 2026-10-05

逐个结构体：构造不崩、`dwSize` 填对、每个字段可读且写回原值往返。

```python
def test_struct_smoke(pyd, sdk, struct_name, baseline):
    size, unreadable, bad = _probe(getattr(g, struct_name), FIELDS_OF[struct_name])
    assert not bad                                    # 逐字段「读 -> 写回 -> 再读」
    if size is not None:
        assert size == baseline[sdk]["sizes"][struct_name]   # dwSize == sizeof（golden）
```

**必须逐个跑，不能抽样** —— nanobind 的 `def_rw` 是模板胶水，一个能跑不代表
另一个能跑（未知类型归零那次一下就找出 6 个漏网的指针别名字段）。

**落地情况**（`native/tests/test_structs.py`，13231 passed，约 16s）：
- 数据源是生成器的 `gen_manifest.json`（名字 -> 字段列表），测试期不再解析头文件，
  避免第二套口径（`_manifest.py` 是共用的读取器）。
- 「读 -> 原样写回 -> 再读」这条对 `str` / `bytes` / 指针 / 数组 / 内嵌结构体 / 枚举
  全都成立，所以不必按类型分支；类型通道另有显式断言（`char[N]`→str、`BYTE[N]`→bytes）。
- `dwSize` 对照 committed 的 `native/tests/baseline_sizes.json`（大华 5983 / 海康 1540
  个带 `dwSize` 的结构体）。换 SDK 后布局变了当场红，不必等接设备。文件缺失会全量扫一遍
  重新生成并提醒提交（见 testing-plan 已定决策 2）。
- **已知读不出来的字段也记在该基线里**（大华 44 / 海康 6），只减不增：新出现的当场红。
  两类成因 —— ① memset 归零后读枚举，`0` 不是合法枚举项（nanobind 固有行为，非绑定缺陷）；
  ② `_DHDEVTIME` 之类类型未注册（真实缺口，可修）。

#### Phase 3：函数签名冒烟（2515 + 785 个）✅ 2026-10-05

空参调用每个函数，检查不崩、不漏绑。

**关键实测量**：绝大多数函数在 nanobind 派发层就因"参数个数不符"抛 `TypeError`，
**根本没进 C** —— 大华 2515 个里 2506 个如此、海康 785 里 757 个；真正执行的只有少数
0 参数函数（大华 9 / 海康 26）。所以"全量空参调用"远没有想象中危险。

**有副作用的函数不必单独列黑名单**：厂商把改设备状态的入口都设计成要传登录句柄
（`CLIENT_Reboot(handle, ...)`），0 参数根本调不到；能覆盖到的天然是"无句柄也能跑"那批。

**必须在子进程里跑**（`_zeroarg_sweep.py` + `test_functions.py`）：实测海康
`NET_DVR_LoadAllCom()` 空参调用直接 ACCESS_VIOLATION（0xC0000005）把整个 python 进程
带走。在 pytest 进程内循环 = 一个函数崩溃就让整个会话无输出地死掉。子进程化后，父进程
靠退出码 + 崩溃前最后一行 `CALL` 定位元凶，报成一条可读的断言失败。

**黑名单与"名单会过期"**：已崩过的函数进 `BLACKLIST`（当前仅海康 `NET_DVR_LoadAllCom`）。
另有一条断言 `test_blacklist_still_crashes` 要求名单里的函数**至今仍崩** —— 一旦它开始
不崩（SDK 修了 / 当初判错），测试就红，逼着清空名单，不让它变成摆设。

**落地情况**（`native/tests/test_functions.py`，4 passed，约 33s）：不崩、`missing == []`
（manifest 里的函数在 pyd 上全部存在）、三种结局（arity / called / raised）能对上账。

#### Phase 4：设备功能测试

依赖 `Dahua_NVR_Simulator` 的实现程度。已覆盖登录 + 断线回调（e2e 归 python 层：
`python/dhbind/tests/test_client_e2e.py` / `test_disconnect_callback_e2e.py`）；待覆盖
预览取流、报警、布防、录像查询、PTZ。**上限取决于模拟器实现了多少**，不是绑定层
能单独决定的。

### 1.3 需要的脚手架

- `native/tests/conftest.py`：**已建**，提供 `pyd(sdk)` fixture（导入 .pyd，缺厂商自动 skip）
- `native/tests/_manifest.py`：**已建**（2026-10-05），`gen_manifest.json` 读取器，
  Phase 2/3 共用；不是 `test_*` 所以不被收集
- `native/tests/test_coverage_regression.py`：**已建**（Phase 1 ✅）
- `native/tests/test_structs.py` + `baseline_sizes.json`：**已建**（Phase 2 ✅）
- `native/tests/test_functions.py` + `_zeroarg_sweep.py`：**已建**（Phase 3 ✅）
- ~~现有三个脚本转 pytest~~ ✅ 已完成（2026-10-05）：`test_callbacks.py`（拆 7 个 test）、
  `test_runtime_roundtrip.py`（原 `verify_runtime.py`，**已被 test_structs/test_functions 取代并退役**）、
  `python/dhbind/tests/test_disconnect_callback_e2e.py`
  （原 `e2e/test_login_callback.py`，e2e 归 python 层）。详见 1.0 的"已退役的脚本"

**结构体/函数清单从哪来** ✅ 已落地：生成器输出 `gen_manifest.json`（结构体 -> 字段列表、
函数表、回调表、各类 skip 计数），测试直接读它，免得再解析一遍头文件
（`emit.py` 的 `write_manifest`，随 `gen_bind.py` 产出）。

一份数据两用：`emit.py` 的分片 diff 仍用 `_gen_manifest.json`（只有文件名 hash，用于估算
编译量）；`gen_manifest.json` 是**语义清单**，服务测试期断言。两者刻意分开：前者是编译
输入、后者不是。

### 1.4 现状

**第 1 层（native）测试基建已全部落地**（2026-10-05）：四个阶段里 Phase 1/2/3 完成，
Phase 4 依赖模拟器（e2e 归 python 层）。

- `native/codegen/check_coverage.py` ✅ Phase 1 已落地：数字已变成断言，见
  `native/tests/test_coverage_regression.py`（`collect(sdk)` 为唯一口径）
- 生成器 ✅ 新增 `gen_manifest.json`（`emit.py` 的 `write_manifest`）：结构体 -> 字段列表、
  函数表、回调表、skip 计数；`--limit` 模式跳过（产物不全时清单会撒谎）
- `native/tests/` 已就位：`conftest.py` + `_manifest.py` + `_zeroarg_sweep.py` +
  `test_callbacks.py` + `test_coverage_regression.py` + `test_structs.py`（+
  `baseline_sizes.json`）+ `test_functions.py`；`e2e/` 已整目录删除（移入
  `python/dhbind/tests/`）；顶层 `tests/` 已撤掉
- `test_runtime_roundtrip.py` **已退役**：字段往返并入 `test_structs.py`，类型通道/枚举/
  SDK 版本号断言分别并入 `test_structs.py` / `test_functions.py`
- ✅ `pytest native/tests -q` → **13250 passed（约 54s）**；`pytest -q`（四层）→
  **13254 passed, 5 deselected**
- ✅ pytest 依赖已声明：根目录 `requirements-dev.txt`（nanobind / ninja / tqdm / pytest），
  README「构建」步骤改用它 —— 此前只存在于 `.venv`，换台机器 clone 下来跑不了测试

**第 1 层剩余**：Phase 4 设备功能测试（受 `Dahua_NVR_Simulator` 实现程度限制）。

---

## 2. 输出指针（outptr）自动读回

`outptr` 现在暴露成 `int` 地址，调用后要自己 `ctypes` 预分配缓冲再读回，属于
「能用但别扭」。做完后 Phase 3 的函数测试会简单很多 —— 否则每次都要手工配缓冲。

---

## 3. 错误码转 Exception

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

## 4. 打包与分发

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

## 5. 那个大华模拟器有空了fork一下，后面还要实现录像下载。
海康模拟器调研结论（2026-10-04 上网检索）：**不存在现成的 HCNetSDK 协议级模拟器**——
检索到的都是 ONVIF/GB28181 模拟器（协议不对口，海康私有二进制协议无公开文档），
详见 `docs/testing-plan.md` 第四节。对齐测试能力的选项：真机 / 自研（抓包逆向，大工程）/
无设备 smoke 保底（已有）。

## 6. ~~`dh_netsdk.cpp` 的定位与清理~~ ✅ 已完成（2026-10-05）

原计划保留它做"GIL 安全的阻塞调用封装"。实际做法反过来了 —— **删掉它**，
把 GIL 释放下沉到生成器的函数绑定模板（`common/parse.py` 给每个 `m.def` 加
`nb::call_guard<nb::gil_scoped_release>()`），理由与判据见
`docs/binding-tech-debt.md` 技术债 #8「等比 ctypes」：

- **接线**：已完成。`python/dhbind/client.py` 的 `Client.login()` 改走生成版
  `CLIENT_LoginWithHighLevelSecurity`，底层不再有手写 pyd。
- **清理**：已完成。模块整体删除，`_test_gil_*` 探针、`init/log_open` 等一并消失；
  同时消除了 5 个类型在两份 pyd 里重复注册的隐患。
