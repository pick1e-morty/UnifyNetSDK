# TODO

按「投入产出比」排序。每条都写清**能不能做、为什么**，避免变成一份做不动的愿望清单。

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
- **结构体/函数清单从哪来**：建议让生成器额外输出 `gen_manifest.json`（名字 +
  跳过原因），测试直接读它，免得测试里再解析一遍头文件
- 现有 `tests/test_e2e_generated.py` 与 `tests/test_cb_bindings.py` 将来并入 pytest

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

## 5. `.pyi` stub

纯生成工作，IDE 补全 + 错误码有类型。与 pytest 无关，但两者都依赖「从 IR 生成
元数据」，可以合并成同一个生成步骤。
