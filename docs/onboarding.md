# 接手这个项目：Orientation

> 给第一次接触本仓库的人或 AI。读完这份（约 10 分钟）应该能：说清项目做到哪、
> 知道要改代码该去哪个文件、照着流程验证一次改动。
>
> 架构与选型见 `docs/binding-tech-evaluation.md`；踩过的坑见
> `docs/implementation-notes.md`；技术债与优先级见 `docs/binding-tech-debt.md`。
> **本文只讲"现在在哪、怎么干活"。**

---

## 一、项目是什么

把大华 / 海康设备网络 SDK 的 C 头文件转成可直接 `import` 的 Python 模块。
结构体、枚举、函数、回调全覆盖，内存布局由 C++ 编译器计算，不手写 ctypes 偏移。

| 模块 | 来源 | 说明 |
|---|---|---|
| `unify_dh_gen` | 生成产物（`native/codegen/gen_bind.py --sdk dahua`）| 大华，**唯一模块**（手写 `unify_dh` 已删）|
| `unify_hk_gen` | 生成产物（`--sdk haikang`）| 海康，✅ 已编译并验证（2026-10-04）；26 回调保守退化 |

两家都只有生成版：**所有函数绑定统一带 `nb::call_guard<nb::gil_scoped_release>()`**，
每次外部调用都不持 GIL，语义与 `ctypes.CDLL` 等比（决策见 `binding-tech-debt.md`）。
线程安全由 Python 上层负责，native 不做并发假设。

---

## 二、现在做到哪

**已完成并验证**：

- 大华 10557 结构体 / 63353 字段（99.51%）/ 1873 枚举 / 2515 函数 / **289 回调**全部绑定
- 海康 2670 结构体 / 18821 字段（99.94%）/ 264 枚举 / 785 函数 / **26 回调**绑定完成
  （`native/tests/test_runtime_roundtrip.py` 通过；回调走保守退化，待接设备后照实际行为补规则）
- 未知类型已归零（大华 0 / 海康 0，2026-10-04）
- `.pyi` stub 随生成产出（`common/emit_stub.py`，IR 的第二个消费者；
  pyd 同目录自动生效，`--no-stub` 可关）
- 端到端跑通：生成版登录 `Dahua_NVR_Simulator`（Gen2 两阶段认证），断线回调被
  **真实 SDK 工作线程**触发、参数全对（e2e 归 python 层：
  `python/dhbind/tests/test_disconnect_callback_e2e.py`）
- 回调参数分类覆盖 289 个 typedef：结构体数组 → `list`、字节缓冲 → `bytes`、
  借用视图 NULL 安全、异常隔离、退订

**下一步（按性价比，见 `binding-tech-debt.md` 末尾表格）**：

1. 高层封装（错误码表、`outptr` 自动读回）
2. 成员函数指针字段（大华 301 个 + 海康 11 个，最贵）

---

## 三、要改代码去哪里

| 想改什么 | 改哪个文件 | 注意 |
|---|---|---|
| 回调运行时（GIL、槽位注册表、borrowed view）| `native/codegen/common/cb_runtime.py` | 它的 `HEADER` 常量就是生成物 `dh_bind_cb.h` 的内容 |
| 回调参数怎么分类成 `bytes`/`list`/单对象 | `native/codegen/common/parse.py` 的 `classify_cb_params` | 判定**靠参数名**；靠位置会误判 150/289 个回调 |
| 生成什么代码（thunk、分片、注册语句）| `native/codegen/common/emit.py` | 改这里会影响编译规模，见第四节 |
| 大华特有的路径/函数正则/跳过名单 | `native/codegen/config/dahua.py` | 厂商差异**只能**加在这里，`common/` 保持厂商无关 |
| GIL 释放策略（函数绑定模板）| `native/codegen/common/parse.py` 的函数绑定段 | 无条件 `gil_scoped_release`，见第五节 |
| 生成物 | **不要直接改** `native/src/gen_dh/` | 下次生成就被覆盖，且不入库 |

改 `common/` 里的厂商无关逻辑时，要问"海康需不需要额外分支"。需要 → 说明抽象漏了，
要么放 `config/`，要么就想清楚为什么两家不同。

---

## 四、标准流程（改任何生成相关代码）

```powershell
# 1. 生成（秒级）
.venv\Scripts\python.exe native/codegen\gen_bind.py --sdk dahua

#    输出末尾会报告分片 diff —— 这决定第 3 步要花多久：
#      分片 diff: 无变化，编译会直接跳过
#      或：修改 95 个 (part 95) => 预计重编 95 个 TU，约 8.7 min

# 2. 确认生成物里真的有新东西（这步别跳）
Select-String -Path native\src\gen_dh\dh_bind_part*.cpp -Pattern '"新字段名"'

# 3. 编译
cd native; powershell -ExecutionPolicy Bypass -File .\build.ps1 -SkipTest -Jobs 8

# 4. 验证（回到项目根）
cd ..
.venv\Scripts\python.exe -m pytest native\tests -q                            # 绑定层全量
.venv\Scripts\python.exe -m pytest -m e2e -q                                  # 端到端（需模拟器）
.venv\Scripts\python.exe native/codegen\check_coverage.py --sdk dahua|haikang             # 覆盖边界统计
```

### 编译由谁来跑

**`build.ps1` 交给用户执行**，除非预估 1 分钟以内（增量通常 7~15 秒，可以自己跑）。
判断依据就是第 1 步输出的"预计重编 N 个 TU / 约 X 秒"：

- 预计 ≤ 1 分钟 → 自己跑
- 预计 > 1 分钟 → 把命令给用户，**不要先跑起来再让用户等**

全量重编约 10 分钟。阻塞着等对谁都没好处：用户在终端前能看见进度、也能中途插手。

---

## 五、验证清单

| 改动 | 至少要跑 |
|---|---|
| 回调运行时（`cb_runtime.py`）| 端到端 + 绑定层（覆盖 GIL / 生命周期 / 参数转换）|
| 回调参数分类（`parse.py`）| 绑定层（逐项断言分类结果）|
| 结构体字段生成（`emit.gen_fields`）| 绑定层 + 手工验一个该字段的读写 |
| 依赖图 / 拓扑序（`build_deps` / `topo_order`）| 端到端（顺序错了运行时才暴露）|
| 纯文档 | 不用跑 |

两个测试都要求 `native/src/gen_dh/` 产物与源码同步。**若产物是旧的**，要么测试给出
提示（绑定层），要么出现莫名其妙的 `hasattr == False` —— 先怀疑产物没重新生成。

---

## 六、容易踩的坑（高频；细项见 implementation-notes）

1. **`build.ps1` 只编译、不生成。** 生成是 `gen_bind.py` 的事。改完生成器直接编译
   = 拿旧产物编一遍，字段压根不存在。
2. **生成的 C++ 必须纯 ASCII。** `write_if_changed` 以 ascii 写出，注释里出现中文会抛
   `UnicodeEncodeError`（且报错看不出是哪句注释）。中文说明写 Python 侧 docstring。
3. **改 `build_deps` / `topo_order` = 一次性全量重编。** 依赖顺序变了 → 95 个分片内容
   跟着变。是一次性的，但事前要有预期（靠分片 diff 报告）。
4. **回调运行时头 `dh_bind_cb.h` 只能被 `*_cbsNNN.cpp` include。** 混进公共 include 会让
   改它拖着 146 个分片重编（12 分钟 vs 7 秒）。
5. **参数分类不能靠位置。** `(NET_X *p, LDWORD dwUser)` 里有 150 个，后者是用户数据
   不是数量；`nBufLen` 是字节长度不是元素个数。
6. **回调注册表只有生成版一套。** 手写 `unify_dh` 已删 —— 之前两套注册表在同一个
   SDK 订阅点混用会静默不触发，且 5 个类型重复注册会让后加载方丢属性。

---

## 七、常用命令速查

```powershell
# 生成（--sdk dahua|haikang，下同）
.venv\Scripts\python.exe native/codegen\gen_bind.py --sdk dahua
.venv\Scripts\python.exe native/codegen\gen_bind.py --sdk dahua --no-selftest  # 少 1.5MB 产物
.venv\Scripts\python.exe native/codegen\gen_bind.py --sdk dahua --dry-run

# 覆盖边界统计（升级 SDK 后重跑，刷新文档里的数字）
.venv\Scripts\python.exe native/codegen\check_coverage.py --sdk dahua|haikang

# 校验 DLL 导出表（头文件声明但实际未导出的函数）
.venv\Scripts\python.exe native/codegen\check_exports.py --sdk dahua|haikang
```

