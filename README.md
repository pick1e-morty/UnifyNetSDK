# UnifyNetSDK

统一大华 / 海康设备网络 SDK 的 Python 绑定。

用 nanobind + 代码生成器，把厂商的 C 头文件转成可直接 `import` 的 Python 模块：结构体、枚举、函数全覆盖，布局由 C++ 编译器保证，不靠手写 ctypes 声明。

## 当前状态

| SDK | 结构体 | 字段 | 枚举 | 函数 | 回调 | 状态 |
|---|---|---|---|---|---|---|
| 大华 `dhnetsdk` | 10557 | 62574/62884 (99.51%) | 1873 | 2515 | 289 | ✅ 完成 |
| 海康 `HCNetSDK` | 2669 | 18640 | 264 | 789 | 待验证 | 🚧 生成器就绪，待接 CMake 编译 |

两家各自独立模块：大华 `unify_dh_gen`、海康 `unify_hk_gen`（命名空间天然隔离，同名结构体不冲突）。

未绑/降级的部分（296 个结构体成员函数指针、6419 个数组按 bytes 暴露等）见
`docs/binding-tech-debt.md`；跑 `python tools/check_coverage.py` 可随时重算这张表。

## 技术方案

- **nanobind**：类型安全，布局由编译器算，杜绝 ctypes 手写偏移的静默错位
- **生成器** `tools/gen_bind.py --sdk dahua|haikang`：通用解析核（`common/parse.py` + `common/emit.py`）配合厂商配置（`config/*.py`），从头文件解析结构体 / 枚举 / 函数，按**依赖拓扑序**切分片，字段类型走白名单兜底
- **增量写入**：内容不变的分片不重写 mtime，ninja 自动跳过，改一处只重编相关分片

关键实测（Ryzen 9 5900HX，8C16T）：

| 指标 | 值 |
|---|---|
| `/Od` 提速 | 单片编译 188s → 23s（约 8×） |
| 全量编译 | 约 11 分钟（`-Jobs 8`，62886 字段 / 125 片） |
| 增量编译 | 改一个函数片约 5s + 链接 |
| import | 0.5s |

> 绑定代码是纯模板胶水，运行时无计算量，所以对生成目标关掉优化（`/Od`），编译时间大幅下降、产物行为不变。

## 目录结构

```
UnifyNetSDK/
├── native/                    # C++ 绑定（nanobind）
│   ├── CMakeLists.txt
│   ├── build.ps1              # 一键生成 + 编译 + 测试
│   ├── build_one.bat          # 单片编译（调试用）
│   ├── smoke_test.py          # 冒烟测试
│   ├── src/dh_netsdk.cpp      # 手写登录链路（最小端到端验证）
│   └── src/gen/               # 生成产物（不入库，可重建）
│       ├── dh_bind.h          #   分片函数声明
│       ├── dh_bind_cb.h       #   回调运行时（模板源 common/dhcb.py）
│       ├── dh_bind_cbsNNN.cpp #   回调 thunk + 绑定
│       ├── dh_bind_partNNN.cpp#   结构体分片
│       ├── dh_bind_enumsNNN.cpp
│       └── dh_bind_funcsNNN.cpp
├── tools/
│   ├── gen_bind.py            # 生成器入口（--sdk dahua|haikang）
│   ├── common/                # 通用解析 + 代码生成（厂商无关）
│   │   ├── parse.py
│   │   ├── emit.py
│   │   └── dhcb.py            #   回调运行时模板（槽位注册表 / GIL 宏）
│   ├── config/                # 厂商配置（路径 / 函数正则 / 跳过名单）
│   │   ├── dahua.py
│   │   └── haikang.py
│   └── check_exports.py       # 检查 DLL 导出表，发现未导出函数
├── docs/                      # 技术文档
│   ├── binding-tech-evaluation.md  # 技术选型评估
│   ├── binding-tech-debt.md        # 技术债清单（活文档，修完就打勾）
│   └── implementation-notes.md     # 实测踩坑笔记（nanobind / C API / MSVC / 大华 SDK）
├── tests/                     # 端到端 / 绑定层验证脚本
├── dahua/                     # 大华 SDK 原始包（不入库）
└── haikang/                   # 海康 SDK 原始包（不入库）
```

## 构建

前置：MSVC（VS 2022+）、CMake 3.27+、[uv](https://github.com/astral-sh/uv)。

```powershell
cd UnifyNetSDK

# 1. 建 venv（项目根统一一份）
uv venv --python 3.13
uv pip install nanobind ninja tqdm

# 2. 生成绑定代码（增量，很快）
.venv\Scripts\python.exe tools\gen_bind.py --sdk dahua

# 3. 编译 + 链接
powershell -ExecutionPolicy Bypass -File native\build.ps1 -SkipTest -Jobs 10
```

`build.ps1` 会自动定位 vcvarsall、用项目根 venv、对生成目标加 `/Od`。

## 使用

```python
import os, sys
os.add_dll_directory(r'dahua\C_Win64\Bin')   # 让 dhnetsdk.dll 及其依赖可被找到
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
# 端到端：生成版登录模拟器 + 验证回调在真实 SDK 线程上触发
.venv\Scripts\python.exe tests\test_e2e_generated.py

# 绑定层参数分类（bytes / obj / array / 指针别名 / 退订 / 异常隔离）
# 依赖生成器默认产出的 _selftest_fXxx 钩子（--no-selftest 可关掉）
.venv\Scripts\python.exe tests\test_cb_bindings.py
```

`_selftest_fXxx(payload)` 钩子默认随绑定一起生成，从裸 `std::thread` 调真实
thunk，因此**没有设备时也能验证回调处理逻辑**：`g._selftest_fRealDataCallBack(b"")`。
`payload` 为空只做线程往返、非空才走完整 thunk —— 这个二分开关在排查卡死/崩溃时
很好用（先确认是线程机制还是 thunk 内部的问题）。

`tests\test_e2e_generated.py` 需要模拟器在 `..\Dahua_NVR_Simulator`（脚本会自己
拉起 server，路径从脚本位置推导，无需改配置）。

## 参数映射约定

生成器把 C 参数映射成 Python 可用的形式：

| C 类型 | Python 侧 | 说明 |
|---|---|---|
| `LLONG` / `int` / `DWORD` / 枚举 | 对应整数 | 直接传 |
| `char[N]` 结构体字段 | `str` | 自动截断防溢出 |
| `const char*` 参数 | `str` | 输入字符串 |
| `T*` 结构体指针 | `T` 对象 | 传入对象，C++ 写回后 Python 可读 |
| `void*` / `HWND` / 回调 / 输出指针 | `int`（地址） | 传 0，或用 ctypes 预分配缓冲取地址 |
| 带默认值 `=0` 的输出指针 | 可省略 | 如 `CLIENT_Login` 的 `error` |

## 跳过说明

头文件声明了 2521 个 `CLIENT_` 函数，其中 **6 个未导出**（头文件写了、但 `dhnetsdk.dll` 里没有，厂商头文件与 DLL 版本不一致），绑定会链接失败，只能跳过：

```
CLIENT_GetSecurityEncryptInfo
CLIENT_DelayReboot
CLIENT_InitDevGetLocalityConfig
CLIENT_PTZSetLockupStatus
CLIENT_SetTemporaryConfig
CLIENT_ModifyBroadcastPlan
```

用 `tools/check_exports.py` 可随时重扫（升级 SDK 后重新校验）。

## 下一步

- [ ] 海康 `HCNetSDK`：接 CMake + 编译验证（生成器已支持 `--sdk haikang`，dry-run 通过）
- [ ] Python 高层封装：错误码表、输出缓冲自动读回（`outptr` → Python 可读）
- [ ] `.pyi` stub：IDE 补全
