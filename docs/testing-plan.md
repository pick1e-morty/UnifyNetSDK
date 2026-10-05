# 测试建设计划（pytest 全面测试绑定层）

> 对应 TODO 第 1 节。状态：**计划已定，待实施**（2026-10-04）。
> 实施前事实：`pytest.ini` 已就位（testpaths + e2e marker + `addopts = -m "not e2e"`）；
> `native/tests/conftest.py` 已有 `pyd(sdk)` fixture；**pytest 依赖未安装**；
> `native/tests/` 下是三个脚本（未转 pytest）。

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
| 0 | `uv pip install pytest`；README 构建前置行补 pytest | — | `pytest --version` |
| 1 | ✅ `test_callbacks.py` 转正：7 个 `def test_*`（bytes / obj / array / 数组经指针别名 / 退订+异常隔离 / 钩子覆盖 / 268 钩子 sweep），print+fails → assert；保留"钩子缺失打印重生成命令"检测 | native/tests | `pytest native/tests` 全绿 |
| 2 | Phase 1：`emit.py` 的 manifest 扩展为完整 IR 清单（结构体→字段、枚举、函数、回调数、各类 skip 计数），新增 `test_coverage_regression.py` 四断言：unknown==0 / 回调数一致 / pyd 字段总数不缩水 / skip 计数持平。断言读 manifest + import pyd 对拍，**不解析头文件** | native/tests + codegen | 覆盖断言全绿；重跑 gen 分片 diff 为零 |
| 3 | Phase 2：`test_structs.py` 逐个结构体 parametrize（10557 + 2668，不抽样）：构造、字段读写往返（读 v → 写 v → 再读 == v；TODO 示例的 `getattr == getattr` 是恒真式，不照抄）、dwSize 基线断言。**`_paths.py` 并入 conftest、`verify_runtime.py` → `test_runtime_roundtrip.py` 已于 2026-10-05 提前完成**；Phase 2 本体（`test_structs.py`）未做 | native/tests | 全量跑通；`test_runtime_roundtrip.py` 原断言逐条确认有归属 |
| 4 | ✅ e2e 迁移：`native/tests/e2e/` → **`python/dhbind/tests/`**（模拟器胶水 `tests/simulator/server.py`），加 `@pytest.mark.e2e`，模拟器 `Popen` 挪进 fixture，路径推导改为"项目根的兄弟目录 `Dahua_NVR_Simulator`" | python/dhbind | 默认收集不含 e2e；有模拟器时 `-m e2e` 实跑 |
| 5 | ✅ 文档同步：README 测试命令改 pytest；onboarding §四§七；TODO 0.2 目录树（e2e 归 dhbind、`_paths.py`/`verify_runtime.py` 移除）与 §1 勾选 | docs | — |

## 三、已定决策

1. **e2e 归 `python/dhbind/tests/`**（用户定，2026-10-04）——理由见第一节。
2. **dwSize 用 committed golden file**（`native/tests/baseline_sizes.json`）：首跑生成、之后断言相等；换 SDK 刷新基线是升级流程的一部分。
3. **Phase 3（函数签名冒烟，2515 个）单独一轮**：黑名单 + 试点先行，风险高（真改设备状态/崩溃），本轮不碰。
4. `verify_runtime.py` 已转正为 `native/tests/test_runtime_roundtrip.py`（2026-10-05）；Phase 2 的 `test_structs.py` 落地后把其中的字段往返断言并入本文件。

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
| C. 降级保底 | 海康 e2e 缺位期间，靠无设备测试保底：`NET_DVR_Init/GetLastError` + 结构体往返 + 回调 selftest 钩子（test_runtime_roundtrip / test_callbacks 已覆盖） | 覆盖不了"真实 SDK 线程登录"链路 |

**倾向**：C 先行（已覆盖），A 按设备到位情况，B 仅在确有需要时立项。
海康 e2e 的缺口由此计划显式记录，不假装已覆盖。
