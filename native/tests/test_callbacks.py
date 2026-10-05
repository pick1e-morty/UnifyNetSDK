# -*- coding: utf-8 -*-
"""unify_dh_gen 的回调绑定验证（走自测钩子，真 C++ 线程）。

为什么不用 ctypes 调 thunk：ctypes 的 CFUNCTYPE 回调会自己 swap 一个 thread
state 进去，判据"当前线程是否已附着"在那种线程上恒为假（PyThreadState_
GetUnchecked() 读不到它），于是绑定会二次 attach 而 Fatal。真实 SDK 工作线程
不是那种情形，所以验证必须用生成出来的 _selftest_fXxx 钩子——它从裸
std::thread 调用 thunk，复现真实路径。

真链路的验证在 e2e/test_login_callback.py（真 SDK 线程），本文件只到"裸线程"为止。

覆盖：
  1. bind_/set_ 与自测钩子的对应关系
  2. bytes 分类：BYTE* + 长度 -> bytes
  3. obj 分类：结构体指针 -> 借用视图，且 dwUser 不被误判成数量
  4. array 分类：结构体指针 + 元素个数 -> list
  5. array 分类的指针别名写法（LPNET_XXX）
  6. 退订、异常隔离
  7. 遍历全部自测钩子，确认没有一个会崩或抛未捕获异常

**不要在 import 期替换 sys.stdout**：pytest 在 collection 阶段就 import 本模块，
一旦换掉它捕获用的流，收尾时会报 `ValueError: I/O operation on closed file`
且一个测试都收不到。进度打点保持 ASCII，交给 pytest 的捕获机制处理编码。
"""
import time
import traceback

import pytest

_T0 = time.time()


def mark(msg):
    """进度打点：native 线程/GIL 相关调用可能卡死或崩，必须能在日志里看到
    停在哪一个 _selftest_ 之前（flush=True 是关键，否则卡住时缓冲区里啥都没有）。"""
    print("[%7.3fs] %s" % (time.time() - _T0, msg), flush=True)


def _selftest_names(g):
    return sorted(n for n in dir(g) if n.startswith("_selftest_"))


@pytest.fixture(scope="module")
def g(pyd):
    """大华生成版模块。绑定层测试依赖 _selftest_fXxx 钩子（gen_bind.py 默认生成，
    --no-selftest 可关）；万一产物是关掉钩子编出来的，明确 skip 而不是抛
    AttributeError 让整个 suite 飘红。"""
    mod = pyd("dahua")
    if not _selftest_names(mod):
        pytest.skip("当前产物是用 --no-selftest 生成的，没有 _selftest_* 钩子；"
                    "重新生成：python native/codegen/gen_bind.py --sdk dahua")
    return mod


def test_hooks_cover_binds(g):
    """自测钩子是 bind_* 的子集（只有标量参数的回调才生成钩子）。"""
    binds = [n for n in dir(g) if n.startswith("bind_")]
    setters = [n for n in dir(g) if n.startswith("set_")]
    hooks = _selftest_names(g)
    mark("bind_* %d / set_* %d / _selftest_* %d" % (len(binds), len(setters), len(hooks)))
    assert binds, "没有 bind_* 回调注册函数"
    assert setters, "没有 set_* 回调注册函数"
    missing = ["bind_" + h[len("_selftest_"):] for h in hooks
               if ("bind_" + h[len("_selftest_"):]) not in binds]
    assert not missing, "有钩子却没有对应 bind_*：%s" % missing


def test_bytes_classification(g):
    """bytes: fDataCallBack(LLONG, DWORD, BYTE*, DWORD, LDWORD)。"""
    seen = []
    g.bind_fDataCallBack(lambda h, dt, buf, sz, user: seen.append((h, dt, buf, sz, user)))
    mark("calling _selftest_fDataCallBack")
    # b"x" = 走完整 thunk；b"" 只做 Stage 1（线程+GIL 往返），用于二分定位
    g._selftest_fDataCallBack(b"x")
    mark("returned from _selftest_fDataCallBack")
    assert len(seen) == 1
    handle, _dt, buf, size, _user = seen[0]
    assert handle == 0x1234
    assert buf == b"\x01\x02\x03\x04"
    assert size == 4


def test_obj_classification_dwuser_not_count(g):
    """obj: 结构体指针 -> 借用视图，且 dwUser 不能被当成数量。

    借用视图只在回调期间有效，所以按真实用法在回调里取走类型/字段，不留引用
    （留着会让 nanobind 在退出时报 leaked instance）。
    """
    seen = []
    g.bind_fVideoAnalyseState(
        lambda *a: seen.append((type(a[1]).__name__, len(a), a[-2])))
    g._selftest_fVideoAnalyseState(b"x")
    assert len(seen) == 1
    name, nargs, dwuser = seen[0]
    assert name == "NET_VIDEOANALYSE_STATE"
    assert nargs == 4
    assert dwuser == 0x1234


def test_array_classification(g):
    """array: 结构体指针 + 元素个数 -> list。"""
    seen = []
    g.bind_fNotifyCarPassInfo(
        lambda *a: seen.append((isinstance(a[1], list), len(a[1]),
                                type(a[1][0]).__name__)))
    g._selftest_fNotifyCarPassInfo(b"x")
    assert len(seen) == 1
    is_list, n, elem = seen[0]
    assert is_list is True
    assert n == 2
    assert elem == "NET_CAR_PASS_INFO"


def test_array_via_pointer_alias(g):
    """指针别名写法（LPNET_XXX）也要成数组。"""
    seen = []
    g.bind_fQueryRecordFileCallBack(
        lambda *a: seen.append((isinstance(a[1], list), type(a[1][0]).__name__)))
    g._selftest_fQueryRecordFileCallBack(b"x")
    assert len(seen) == 1
    assert seen[0][0] is True
    assert seen[0][1] == "NET_RECORDFILE_INFO"


def test_unsubscribe_and_exception_isolation(g):
    seen = []
    g.bind_fDataCallBack(lambda h, dt, buf, sz, user: seen.append(1))
    g._selftest_fDataCallBack(b"x")
    assert len(seen) == 1

    g.unbind_fDataCallBack()
    g._selftest_fDataCallBack(b"x")
    assert len(seen) == 1, "退订之后回调仍被调用"

    def boom(*a):
        raise ValueError("intentional test error")

    g.bind_fDataCallBack(boom)
    g._selftest_fDataCallBack(b"x")
    mark("survived user exception, no crash")


def test_all_selftest_hooks_survive(g):
    """遍历全部钩子：没有一个会崩或抛未捕获异常。"""
    hooks = _selftest_names(g)
    crashed = []
    for idx, name in enumerate(hooks):
        mark("selftest %d/%d: %s" % (idx + 1, len(hooks), name))
        try:
            getattr(g, name)(b"x")
        except Exception:
            crashed.append((name, traceback.format_exc(limit=1).strip().splitlines()[-1]))
    mark("sweep done")
    assert not crashed, "自测钩子崩溃或抛未捕获异常：%s" % (crashed[:10],)