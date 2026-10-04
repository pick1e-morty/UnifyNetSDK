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
| Python 测试散在三处 | `tests/` 2 个；`native/smoke_test.py` 因构建需要留在 C++ 侧；端到端的模拟器代码**内嵌在字符串字面量里** |
| 手写与生成混在一层 | `native/src/dh_netsdk.cpp`（手写）与 `native/src/gen/`（生成）职责已不同 |
| 没有对外承诺 | README 讲了怎么做，没讲"用户会得到什么" |

### 0.2 目标形态：四层产品结构

**四层是「产品分层」，不是目录分层** —— 回答的是"交付什么"，而不是"代码放哪"。
两者必须映射清楚，否则会出现"照着四层讨论功能、打开仓库却不知道放哪"的情况。

| 产品层 | 交付物 | 源码位置 |
|---|---|---|
| **第 1 层** C → pyd | `unify_dh_gen.pyd` / `unify_hk_gen.pyd` | `native/src/gen/`（生成物，不入库）|
| **第 2 层** 大华厚封装 wheel | `unify-dh` | `python/unify_dh/` |
| **第 3 层** 海康厚封装 wheel | `unify-hk` | `python/unify_hk/` |
| **第 4 层** 跨厂商抽象 | `unify-netsdk` | `python/unify/` |

第 4 层由本层 Python 判断该调哪个厂商，**用户层代码全部抽象、没有厂商方言**。

```
UnifyNetSDK/
├── native/                          # 第 1 层：C++ 绑定（nanobind）
│   ├── CMakeLists.txt / build.ps1
│   ├── src/dh_netsdk.cpp            # 手写部分（登录链路 / 排障工具）
│   └── src/gen/                     # 生成产物（不入库）
│
├── python/                          # 上层：三个待打包的包
│   ├── unify_dh/                    # → 第 2 层，wheel 1
│   │   ├── __init__.py              #   加载胶水：add_dll_directory + 导出 API
│   │   ├── errors.py                #   大华错误码表
│   │   ├── client.py                #   大华版 Client（内部调 unify_dh_gen）
│   │   └── _binding/                #   构建时填充：.pyd + 厂商 DLL（不入库）
│   │       ├── unify_dh_gen.cp313-win_amd64.pyd
│   │       └── dhnetsdk.dll / libeay32.dll / ...
│   │
│   ├── unify_hk/                    # → 第 3 层，wheel 2（同构，指向海康）
│   │   └── ... 同上
│   │
│   └── unify/                       # → 第 4 层，wheel 3（纯 Python，无 .pyd）
│       ├── client.py                #   跨厂商 Client
│       ├── errors.py                #   统一异常
│       └── _vendor/                 #   厂商探测与分发
│           ├── detect.py            #     协议探测 + 未安装时的提示
│           ├── dahua.py
│           └── haikang.py
│
├── tools/                           # 构建期：生成器（不是运行时库）
├── tests/
│   ├── conftest.py
│   ├── test_coverage_regression.py / test_structs.py / test_functions.py
│   └── e2e/                         # 端到端（需模拟器）
│       ├── simulator/               #   模拟器胶水，从字符串字面量挪成真文件
│       └── test_login_callback.py
├── docs/
└── TODO.md
```

**构建流程**：

```
tools/gen_bind.py --sdk dahua
    ↓
native/build/*.pyd  +  dahua/C_Win64/Bin/*.dll        # 1. 两份产物
    ↓
python/unify_dh/_binding/                              # 2. 拷进胶水层
    ↓
bdist_wheel                                           # 3. 打包 → unify_dh-1.0.0-cp313-win_amd64.whl
```

**要分的是「运行时」（C++ 绑定 + Python 上层）和「构建期」（生成器）**，不是简单按
语言分。所以 `tools/` 保持独立，`native/smoke_test.py` 不要为了整齐挪走（构建流程
要用它）。

### 0.3 两个已定的决策

| 决策 | 结论 |
|---|---|
| 交付形态 | **wheel**。一个厂商一个 wheel（见第 6 节），`unify` 是可选的上层抽象 |
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


### 0.5 一条设计原则（决定 `unify` 怎么做）

厂商能力差异是**本质的**，不是接口没对齐。例：大华录像下载只支持同步，海康支持
异步 + 同步。所以 `unify` 的接口必须**明确标注哪些是双厂商都支持的**，不要给一个
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

**② 62884 个字段不可能全做**。只覆盖用户真实调用的操作：登录、预览、报警、布防、
录像查询、PTZ、云台 —— 几十个模型，覆盖 90% 需求。其余结构体保持原始绑定形态。

**③ pydantic 是第三方依赖，要不要强依赖**：

| 方案 | 优点 | 代价 |
|---|---|---|
| 强依赖 pydantic | 体验一致，模型开箱可用 | 轻量用户被迫装（几 MB）|
| **可选依赖** `unify-dh[pydantic]` | 核心 API 零依赖 | 维护两套调用方式 |
| 用 dataclass 替代 | 标准库零依赖 | 无运行时校验、无 JSON schema |

**待定**：取决于想给什么样的用户体验 —— 参数校验（IP 格式、端口范围）在调用前就报错，
是厚封装的核心价值之一，那强依赖也说得通。

**验证方式**：先手工为"登录"写一个 `LoginArgs`（pydantic + `to_struct()`），确认形态
对了，再讨论怎么自动生成。形态不对时现在改成本最低。

厂商能力差异是**本质的**，不是接口没对齐。例：大华录像下载只支持同步，海康支持
异步 + 同步。所以 `unify` 的接口必须**明确标注哪些是双厂商都支持的**，不要给一个
"看起来统一、实际某厂商上会 AttributeError"的假象。

---

## 1. 用 pytest 全面测试绑定层 ⭐

> 目标：在上层 Python 用 pytest 把头文件里的函数、结构体尽可能逐项测一遍。

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

把现有的 `tools/check_coverage.py` 改写成 pytest 断言，让**手写数字变成自动防线**：

```python
def test_no_unknown_type_fields():            # 现在 6 个，修完就是 0
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

- `tests/conftest.py`：导入 `unify_dh_gen`、准备 `dll_directory`
- `tests/test_coverage_regression.py`：Phase 1
- `tests/test_structs.py`：Phase 2
- `tests/test_functions.py`：Phase 3
- 现有 `tests/test_e2e_generated.py` 与 `tests/test_cb_bindings.py` 将来并入 pytest

**结构体/函数清单从哪来**：让生成器输出 `gen_manifest.json`（名字 + 跳过原因 +
字段列表），测试直接读它，免得测试里再解析一遍头文件。

一份数据两用：现在 `emit.py` 的分片 diff 用的是 `_gen_manifest.json`（只有文件名
hash，用于估算编译量），扩展成带字段列表的 manifest 后，同一个文件既服务编译期
diff，也服务测试期断言。

### 1.4 现状

- `tools/check_coverage.py` 已能输出完整覆盖边界，Phase 1 只需把数字改成断言
- 还没有 `pytest` 依赖与 `conftest.py`

---

## 2. 海康接 CMake 编译

验证 `common/` 真的与厂商无关。生成器 dry-run 已通过（2669 结构体 / 18640 字段 /
789 函数），只差编译与 CMake 配置。注意接入会改依赖图 → **一次性全量重编**
（用分片 diff 报告确认规模）。

---

## 3. 输出指针（outptr）自动读回

`outptr` 现在暴露成 `int` 地址，调用后要自己 `ctypes` 预分配缓冲再读回，属于
「能用但别扭」。做完后 Phase 3 的函数测试会简单很多 —— 否则每次都要手工配缓冲。

---

## 4. 未知类型归零（6 个）

`FP_RE` 只认 `typedef ... (*name)(` 一种写法，漏了 5 个函数指针 typedef；另有 1 个
`FIELD_RE` 边界 bug。改完 Phase 1 的 `test_no_unknown_type_fields` 就能转绿。

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

- **一个厂商一个 wheel**：`unify-dh` 只含大华、`unify-hk` 只含海康。
  理由是厂商 DLL 体积大，捆一起会让只需要单家的用户白下载另一家的 SDK。
- **`unify` 是可选的上层抽象**：依赖厂商 wheel，抽象掉厂商差异。
  用户不需要 `unify` 时可以只装 `unify-dh` 自己拼，自由度最高。
- **平台范围先只打通 `win_amd64` + `cp313`**，证明整条路线可行，多平台/多 Python
  版本日后按需再扩。
- `unify` 的 `pyproject.toml` 写清版本依赖限制，三个包用同一套版本号
  （避免"unify-dh 能装、unify-hk 装不上"）。

DLL 加载：随 wheel 打包，import 时由包自己 `os.add_dll_directory` 指向包内目录。
**大华官方 Python SDK 也是这么做的**（手动 add dll path），所以这是厂商生态的
既有做法，不是我们自创的负担。


**厂商探测**（`unify` 在 login 前判断设备是哪家）：两家协议天差地别（大华
`0xA0 0x01` realm 挑战 vs 海康完全不同），端口探测能可靠区分。两个边界：

- **防火墙可能 DROP 未登记端口** → 探测超时。错误信息必须区分「探测到海康但没装
  unify-hk」（提示 pip install unify-hk）与「探测无响应」（提示用 Unify(vendor=...)
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
