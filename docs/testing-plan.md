# 测试建设计划（pytest 全面测试绑定层）

> 对应 TODO 第 1 节。状态：**第 1 层已实施完毕**（Phase 1/2/3 完成，2026-10-05），
> Phase 4（设备功能）待模拟器。
> 实施后事实：`pytest.ini` 就位；`pytest` 依赖已声明（根目录 `requirements-dev.txt`）；
> `native/tests/` 下 pytest 测试齐备（`pytest native/tests -q` → 13250 passed）。

---

## 一、分层原则（TODO 1.0，已按用户决定修订）

测试跟着被测对象走。**e2e 场景测试归 `python/dhbind/tests/`**：

| 位置 | 测什么 |
|---|---|
| `native/tests/` | 第 1 层 pyd：覆盖断言、结构体冒烟、回调分类（后续 test_coverage_regression / test_structs / test_callbacks） |
| `python/dhbind/tests/e2e/` | **e2e 场景**：登录 + 断线回调 + 模拟器。现状直接驱动生成版 pyd（TODO 旧 9 节承认"绕着走"），dhbind Client 落地后改走 `Client.login()`，正是厚壳的第一个场景测试 |

## 二、实施步骤

| Step | 内容 | 位置 | 验证 |
|---|---|---|---|
| 0 | ✅ `pytest` 依赖声明：根目录 `requirements-dev.txt`（nanobind / ninja / tqdm / pytest），README 构建步骤改用它 | — | `pytest --version` |
| 1 | ✅ `test_callbacks.py` 转正：7 个 `def test_*`（bytes / obj / array / 数组经指针别名 / 退订+异常隔离 / 钩子覆盖 / 268 钩子 sweep），print+fails → assert；保留"钩子缺失打印重生成命令"检测 | native/tests | `pytest native/tests` 全绿 |
| 2 | ✅ Phase 1：`emit.py` 的 manifest 扩展为完整 IR 清单（结构体→字段、函数、回调数、各类 skip 计数）→ `gen_manifest.json`，`test_coverage_regression.py` 四断言。注意**实现上仍读了头文件**（`check_coverage.collect()`，与打印共用同一口径、只需一处维护）；`gen_manifest.json` 改由 Phase 2/3 消费 | native/tests + codegen | 覆盖断言全绿；重跑 gen 分片 diff 为零 |
| 3 | ✅ Phase 2：`test_structs.py` 逐个结构体（10557 + 2668，不抽样）：构造、字段「读 v → 写 v → 再读 == v」、dwSize 对照 committed golden。已知不可读字段记进 golden（只减不增） | native/tests | 13231 passed（约 16s） |
| 4 | ✅ e2e 迁移：`native/tests/e2e/` → **`python/dhbind/tests/`**（模拟器胶水 `tests/simulator/server.py`），加 `@pytest.mark.e2e`，模拟器 `Popen` 挪进 fixture，路径推导改为"项目根的兄弟目录 `Dahua_NVR_Simulator`" | python/dhbind | 默认收集不含 e2e；有模拟器时 `-m e2e` 实跑 |
| 5 | ✅ 文档同步：README 测试命令改 pytest；onboarding §四§七；TODO 0.2 目录树（e2e 归 dhbind、`_paths.py`/`verify_runtime.py` 移除）与 §1 勾选 | docs | — |
| 6 | ✅ Phase 3：`test_functions.py` 全量空参调用，**子进程隔离**（`_zeroarg_sweep.py`）；实测海康 `NET_DVR_LoadAllCom()` 空参即 ACCESS_VIOLATION，黑名单 + "名单必须仍崩"的反向断言 | native/tests | 4 passed（约 33s） |

## 三、已定决策

1. **e2e 归 `python/dhbind/tests/`**（用户定，2026-10-04）——理由见第一节。
2. **dwSize 用 committed golden file**（`native/tests/baseline_sizes.json`）：首跑生成、之后断言相等；换 SDK 刷新基线是升级流程的一部分。已知不可读字段（大华 44 / 海康 6）也记在这里，只减不增。
3. ~~Phase 3 本轮不碰~~ **已做**（2026-10-05）：实测"全量空参调用"并不危险 —— 大华 2515 个里 2506 个、海康 785 里 757 个在 nanobind 派发层就因参数个数不符抛 `TypeError`，**根本没进 C**；真正执行的是少数 0 参数函数。唯一实测崩溃是海康 `NET_DVR_LoadAllCom()`（ACCESS_VIOLATION）。
4. **函数空参扫描必须在子进程里跑**（新增，2026-10-05）：崩溃会带走整个 python 进程，在 pytest 进程内循环等于"一个函数崩溃 = 整个会话无输出地死掉"。执行体 `native/tests/_zeroarg_sweep.py`，父进程靠退出码 + 崩溃前最后一行 `CALL` 定位元凶。黑名单条目另配"必须仍崩"的反向断言，防止名单过期变摆设。
5. `verify_runtime.py` → `test_runtime_roundtrip.py`（2026-10-05 转正）→ **已退役**（2026-10-05）：字段往返/类型通道/枚举并入 `test_structs.py`，SDK 版本号断言并入 `test_functions.py`。

## 四、海康模拟器调研（2026-10-04，上网多轮检索）

**结论：不存在现成的 HCNetSDK 协议级模拟器**，与大华 `Dahua_NVR_Simulator` 对等的
开源项目没有检索到（github / gitee / CSDN）。明细：

- 检索到的"设备模拟器"（Qt `bin_video_simulate`、feiyangqingyun 的 ONVIF/GB28181
  模拟组件等）说的是 **ONVIF / GB28181(SIP)** 协议——与 HCNetSDK 的海康私有二进制
  协议不对口，且该私有协议无公开文档。
- CSDN 有一个付费闭源的"海康 DVR 模拟环境"（2026-08 上传），无源码、无法审计是否
  协议级，不可依赖。
- 其余检索结果（pyhikvision / HCNetSDK-python / 各语言封装）都是 **SDK 的 ctypes
  封装**，不是模拟器。`Dahua_NVR_Simulator` 本身也未见公开仓库。

**对齐两厂商测试能力的选项**：

| 选项 | 内容 | 代价 |
|---|---|---|
| A. 真机 | 拿一台海康设备跑登录/断线回调 e2e | 要有设备在手上 |
| B. 自研协议模拟器 | 抓包逆向海康私有登录协议，仿照大华模拟器实现 | 大工程，协议无文档是硬门槛 |
| C. 降级保底 | 海康 e2e 缺位期间，靠无设备测试保底：结构体逐项冒烟 + 函数空参冒烟 + 回调 selftest 钩子（`test_structs` / `test_functions` / `test_callbacks` 已覆盖） | 覆盖不了"真实 SDK 线程登录"链路 |

**倾向**：C 先行（已覆盖），A 按设备到位情况，B 仅在确有需要时立项。
海康 e2e 的缺口由此计划显式记录，不假装已覆盖。
