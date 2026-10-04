# UnifyNetSDK

统一大华 / 海康设备网络 SDK 的 Python 绑定。

用 nanobind + 代码生成器，把厂商的 C 头文件转成可直接 `import` 的 Python 模块：结构体、枚举、函数全覆盖，布局由 C++ 编译器保证，不靠手写 ctypes 声明。

> **第一次接触本项目请先读 [`docs/onboarding.md`](docs/onboarding.md)** —— 里面有当前进度、
> 代码地图、标准改动流程和验证清单，能省掉大量摸索。
>
> 想做的需求、已知缺口见 [`TODO.md`](TODO.md)。

## 当前状态

| SDK | 版本 | 结构体 | 字段（绑定/共） | 枚举 | 函数（绑定/共） | 回调 | 状态 |
|---|---|---|---|---|---|---|---|
| 大华 `dhnetsdk` | 3.6.1.92074 | 10557 | 63044 / 63353 | 1873 | 2515 / 2521 | 289 | ✅ 编译 + 运行时验证通过 |
| 海康 `HCNetSDK` | 6.1.11.30 | 2670 | 18810 / 18821 | 264 | 785 / 789 | 26 | ✅ 编译 + 运行时验证通过 |

> 数字来自 `python native/codegen/check_coverage.py --sdk <sdk>` 实测。函数"绑定/共"之差
> 是 DLL 未导出被跳过（大华 6、海康 4）；字段之差见下方"未绑/降级"与
> `docs/binding-tech-debt.md` 的覆盖边界表。

两家各自独立模块：大华 `unify_dh_gen`、海康 `unify_hk_gen`（命名空间天然隔离，同名结构体不冲突）。
两个 pyd 都通过了 `native/tests/verify_runtime.py`：import、字段读写往返、不依赖设备的安全函数
（`CLIENT_GetSDKVersion()` 返回 36192074 = 3.6.1.92074 的 build 号）。

海康的 26 个回调目前走**保守退化**（不识别结构体数组，全部给单个对象）—— 那套
"靠参数名判断数量"的规则是从大华 289 个回调归纳的，对海康不成立，等接上设备后照
它的实际行为再补。

未绑/降级的部分（结构体成员函数指针大华 301 个、海康 11 个，非 `char[N]` 数组按 bytes 暴露等）见
`docs/binding-tech-debt.md`；跑 `python native/codegen/check_coverage.py --sdk <sdk>` 可随时重算。

## 技术方案

- **nanobind**：类型安全，布局由编译器算，杜绝 ctypes 手写偏移的静默错位
- **生成器** `native/codegen/gen_bind.py --sdk dahua|haikang`：通用解析核（`common/parse.py` + `common/emit.py`）配合厂商配置（`config/*.py`），从头文件解析结构体 / 枚举 / 函数，按**依赖拓扑序**切分片，字段类型走白名单兜底
- **增量写入**：内容不变的分片不重写 mtime，ninja 自动跳过，改一处只重编相关分片

关键实测（Ryzen 9 5900HX，8C16T）：

| 指标 | 值 |
|---|---|
| `/Od` 提速 | 单片编译 188s → 23s（约 8×） |
| 全量编译 | 约 13 分钟（`-Jobs 8`，63353 字段 / 126 片） |
| 增量编译 | 改一个函数片约 5s + 链接 |
| import | 0.5s |

> 绑定代码是纯模板胶水，运行时无计算量，所以对生成目标关掉优化（`/Od`），编译时间大幅下降、产物行为不变。

## 目录结构

```
UnifyNetSDK/
├── native/                    # C++ 绑定（nanobind）+ 生成器
│   ├── CMakeLists.txt
│   ├── build.ps1              # 一键生成 + 编译 + 测试（-Sdk dahua|haikang|all）
│   ├── build_one.bat          # 单片编译（调试用）
│   ├── smoke_test.py          # 冒烟测试（大华）
│   ├── codegen/               # 绑定生成器：唯一产物就是下面的 src/gen_*
│   │   ├── gen_bind.py            #   入口（--sdk dahua|haikang）
│   │   ├── check_coverage.py      #   覆盖边界报告（--sdk）
│   │   ├── check_exports.py       #   扫 DLL 导出表，找未导出的函数（--sdk）
│   │   ├── common/                #   通用骨架（零厂商字样：只回答"语法长什么样"）
│   │   │   ├── parse.py               #   C 语法解析 + 条件编译裁剪
│   │   │   ├── emit.py                #   代码生成
│   │   │   └── cb_runtime.py          #   回调运行时模板（槽位注册表 / GIL 宏）
│   │   └── config/                #   厂商语义（路径 / 正则 / 跳过名单 / 参数钩子）
│   │       ├── paths.py                #   项目根推导（向上找锚点，不数层数）
│   │       ├── dahua.py               #   含回调参数分类规则（从 289 个回调归纳）
│   │       └── haikang.py             #   故意不设钩子 —— 缺省即保守退化
│   ├── src/
│   │   ├── dh_netsdk.cpp      # 手写登录链路（第 2 层封装：释放 GIL + 填 dwSize）
│   │   ├── gen_dh/            # 大华生成产物（不入库，可重建）
│   │   │   ├── dh_bind.h          #   分片函数声明
│   │   │   ├── dh_bind_cb.h       #   回调运行时（模板源 common/cb_runtime.py）
│   │   │   ├── dh_bind_cbsNNN.cpp #   回调 thunk + 绑定
│   │   │   ├── dh_bind_partNNN.cpp#   结构体分片
│   │   │   ├── dh_bind_enumsNNN.cpp
│   │   │   ├── dh_bind_funcsNNN.cpp
│   │   │   └── unify_dh_gen.pyi   #   IDE 补全存根（emit_stub.py，build 目录另有副本）
│   │   └── gen_hk/            # 海康生成产物（结构与 gen_dh 同构）
│   └── tests/                 # ★ 测第 1 层：.pyd 绑定层
│       ├── conftest.py            #   fixture：SDK DLL 加载 / pyd 导入（缺厂商自动 skip）
│       ├── _paths.py              #   脚本阶段的路径 helper，转 pytest 后并入 conftest
│       ├── test_callbacks.py      #   289 个 bind_/set_ 分类 / 退订 / 异常隔离
│       ├── verify_runtime.py      #   两厂商 .pyd 读写往返【Phase 2 落地后退役】
│       └── e2e/                   #   需项目外的模拟器，默认不跑（-m e2e）
│           ├── simulator/server.py    #     模拟器胶水（原为内嵌字符串，已拆出）
│           └── test_login_callback.py #     真实 SDK 工作线程 -> thunk -> GIL 回调
├── python/                   # 上层：三个待打包的 wheel（目前只有骨架，内容待填）
│   ├── dhbind/              # → wheel dhbind：加载 unify_dh_gen + 大华错误码 + Client
│   │   ├── _binding/         #   构建时填充 .pyd + 厂商 DLL（不入库）
│   │   └── tests/            #   测第 2 层：Client 流程 / 错误码转换 / outptr 读回
│   ├── hkbind/              # → wheel hkbind：同构，指向海康
│   │   ├── _binding/
│   │   └── tests/
│   └── unify_netsdk/         # → unify-netsdk：纯 Python，跨厂商抽象
│       ├── _vendor/          #   厂商探测与分发（detect.py / dahua.py / haikang.py）
│       └── tests/            #   测跨厂商：探测 / 分发 / 能力标注
├── tools/
│   └── sync_sdk.py           # SDK 同步：原始包 -> vendor/<厂商>/sdk_win64/（--check 只校验）
├── docs/                      # 技术文档
│   ├── onboarding.md              # ★ 先读这个：进度 / 代码地图 / 工作流程
│   ├── binding-tech-evaluation.md  # 技术选型评估
│   ├── binding-tech-debt.md        # 技术债清单（活文档，修完就打勾）
│   └── implementation-notes.md     # 实测踩坑笔记（nanobind / C API / MSVC / SDK）
├── pytest.ini                # testpaths（与上面的树一致）+ e2e marker（e2e 默认不跑）
└── vendor/                   # 厂商原始 SDK（体积大，不入库）
    ├── dahua/                     # 大华 3.6.1.92074
    │   ├── C_Win64/                   #   原始发行包（只读，sync_sdk.py 的源）
    │   └── sdk_win64/                 #   同步副本：{include,lib,bin}（只有 .keep 入库）
    └── haikang/                   # 海康 6.1.11.30，结构同上
```

## SDK 版本

SDK 原始包不入库，需自行从厂商渠道取得。**版本必须与下表一致** —— 结构体布局、
函数签名、导出表都会随版本变化，用错版本会出现"编译能过、程序能跑，但字段与 DLL
实际行为对不上"这类极难排查的问题。

| 厂商 | 版本 | 来源目录 | 产物与规模 |
|---|---|---|---|
| 大华 | **3.6.1.92074** | `vendor/dahua/C_Win64/` | `unify_dh_gen.pyd`：10557 结构体 / 2515 函数 / 289 回调 |
| 海康 | **6.1.11.30**（build 20260805） | `vendor/haikang/HCNetSDK_Win64/HCNetSDKV6.1.11.30_build20260805_Win64_ZH/` | `unify_hk_gen.pyd`：2670 结构体 / 785 函数 / 26 回调 |

版本号取自 DLL 的版本资源，不是目录名 —— 目录名可能与实际版本不符：

```powershell
(Get-Item vendor\dahua\sdk_win64\bin\dhnetsdk.dll).VersionInfo.FileVersion    # 3, 6, 1, 92074
(Get-Item vendor\haikang\sdk_win64\bin\HCNetSDK.dll).VersionInfo.FileVersion  # 6, 1, 11, 30
```

取得 SDK 后先同步一次 —— 把头文件/库/DLL 复制到 `<厂商>/sdk_win64/{include,lib,bin}`，
全 ASCII 路径、两个厂商结构同构（海康 vendor 包里的目录名是中文，MSVC 编译能过但
CMake 的 message() 会乱码、bat 里传中文路径会让 dumpbin 之类工具直接失败）：

```powershell
.venv\Scripts\python.exe tools\sync_sdk.py
```

`build.ps1` 每次 configure 前都会跑 `sync_sdk.py --check`，副本与原始包不一致就报错
并提示同步命令。副本目录里有一个 `.keep` 说明了内容从哪来、怎么重新同步。

## 构建

前置：MSVC（VS 2022+）、CMake 3.27+、[uv](https://github.com/astral-sh/uv)。

```powershell
cd UnifyNetSDK

# 1. 建 venv（项目根统一一份）
uv venv --python 3.13
uv pip install nanobind ninja tqdm

# 2. 同步 SDK 到纯 ASCII 副本（换过 SDK 版本后要重跑）
.venv\Scripts\python.exe tools\sync_sdk.py

# 3. 生成绑定代码（增量，很快）
.venv\Scripts\python.exe native/codegen\gen_bind.py --sdk dahua
.venv\Scripts\python.exe native/codegen\gen_bind.py --sdk haikang

# 4. 编译 + 链接
powershell -ExecutionPolicy Bypass -File native\build.ps1 -SkipTest -Jobs 10
```

`build.ps1` 默认编两个厂商（`-Sdk all`）；只改一个时用 `-Sdk dahua` / `-Sdk haikang`
更快。它会按厂商分段构建并各自汇总成败，一个厂商失败不影响另一个的产物。

## 使用

```python
import os, sys
os.add_dll_directory(r'vendor\dahua\sdk_win64\bin')   # 让 dhnetsdk.dll 及其依赖可被找到
sys.path.insert(0, r'native\build')
import unify_dh_gen as g

# 初始化 SDK
ok = g.CLIENT_Init(0, 0)              # 断线回调传 0 表示不注册
print(ok, g.CLIENT_GetLastError())    # True 0

# 登录（结构体字段直接读写；dwSize 已自动填好）
in_param = g.NET_IN_LOGIN_WITH_HIGHLEVEL_SECURITY()
in_param.szIP = '192.168.1.108'
in_param.nPort = 37777
in_param.szUserName = 'admin'
in_param.szPassword = 'admin123'
out = g.NET_OUT_LOGIN_WITH_HIGHLEVEL_SECURITY()
handle = g.CLIENT_LoginWithHighLevelSecurity(in_param, out)
print('登录句柄:', handle, '错误码:', out.nError)

g.CLIENT_Cleanup()
```

> 两个厂商的 pyd 都要 import 时，**两个 DLL 目录都得先 `add_dll_directory`**，否则
> 跨厂商 import 会报 `DLL load failed: 找不到指定的模块`（依赖解析在进程级）。

类型存根：`gen_bind.py` 同时产出 `unify_<厂商>_gen.pyi`（`--no-stub` 可关），
与 pyd 同放 `native/build/` —— IDE 对上面的 import 直接给出全量补全与字段类型
（`char[N]` → `str`、其余数组 → `bytes`、指针/句柄 → `int` 地址）。

## 回调

预览、报警、布防、实时流全靠回调。289 个回调 typedef 已全部生成绑定：

```python
# 订阅 + 拿 C 函数指针，一步完成（不会弄错顺序）
ptr = unify_dh_gen.bind_fRealDataCallBack(on_data)
unify_dh_gen.CLIENT_SetRealDataCallBack(login, 0, ptr, 0)

unify_dh_gen.set_fRealDataCallBack(on_data)      # 只订阅
unify_dh_gen.unbind_fRealDataCallBack()          # 退订
```

参数映射（1146 个参数实测零误判，判定靠参数名而非位置）：

| C 签名 | Python 收到 |
|---|---|
| `BYTE *pBuffer, DWORD dwBufSize` | `bytes` |
| `NET_X *p, int nNum` | `list` of `NET_X`（借用视图） |
| `NET_X *p, LDWORD dwUser` | `NET_X`（`dwUser` 原样透传） |
| `const char *p` | `str` |
| `void *pReserved` | `int` 地址 |

> 结构体参数是**借用视图**：SDK 回调返回后底层缓冲即失效，需要留存的数据请在回调内取走字段。细节见 `docs/binding-tech-debt.md`。


## 测试

```powershell
# 运行时验证：两个 pyd 的 import / 规模 / 字段读写往返 / 安全函数
.venv\Scripts\python.exe native\tests\verify_runtime.py

# 端到端：生成版登录模拟器 + 验证回调在真实 SDK 线程上触发（需大华模拟器）
.venv\Scripts\python.exe native\tests\e2e\test_login_callback.py

# 绑定层参数分类（bytes / obj / array / 指针别名 / 退订 / 异常隔离）
.venv\Scripts\python.exe native\tests\test_callbacks.py
```

`verify_runtime.py` 是判断"绑定是否真的可用"的最小成本手段 —— 编译通过只证明类型和
语法正确，字段偏移错乱、数组维度算错这类问题只有跑起来才暴露。

`_selftest_fXxx(payload)` 钩子默认随绑定一起生成，从裸 `std::thread` 调真实
thunk，因此**没有设备时也能验证回调处理逻辑**：`g._selftest_fRealDataCallBack(b"")`。
`payload` 为空只做线程往返、非空才走完整 thunk —— 这个二分开关在排查卡死/崩溃时
很好用（先确认是线程机制还是 thunk 内部的问题）。

`native\tests\e2e\test_login_callback.py` 需要模拟器在 `..\Dahua_NVR_Simulator`（脚本会自己
拉起 server，路径从脚本位置推导，无需改配置）。
