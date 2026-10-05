# -*- coding: utf-8 -*-
"""Phase 3：函数空参冒烟（TODO 1.2 Phase 3）。

对 manifest 里的每个函数调一次 `f()`，然后分类：

- **多数函数在 nanobind 派发层就因"参数个数不符"抛 TypeError，根本没进 C**
  （实测大华 2515 个里 2506 个如此，海康 785 里 757 个）—— 所以"全量空参调用"
  远比想象中安全：真正执行的只有少数 0 参数函数（实测大华 9 / 海康 26）；
- 真的执行了、报错返回：无设备时的正常结局，不算失败；
- 把进程干掉：也不怕 —— 见下。

**为什么在子进程里跑**：实测海康 `NET_DVR_LoadAllCom()` 空参调用直接
ACCESS_VIOLATION（0xC0000005），把整个 python 进程带走。若在 pytest 进程内循环，
一个函数崩溃 = 整个会话无输出地死掉，连"崩在哪个函数"都拿不到。执行体见
`_zeroarg_sweep.py`；父进程在这里，靠子进程退出码 + 崩溃前最后一行 `CALL` 定位。

**黑名单**：已知空参即崩的函数排除在扫描之外，免得每次测试都去踩。黑名单不是
免死金牌 —— `test_blacklist_still_crashes` 要求名单里的函数**至今仍会崩**：一旦
它开始不崩（SDK 修了 / 当初判错），测试就红，逼着把名单清空。

**有副作用的函数**：不需要单独列名单。厂商把"改设备状态"的入口都设计成要传登录
句柄（`CLIENT_Reboot(handle, ...)`），0 参数根本调不到 —— 冒烟能覆盖到的 0 参数
函数天然是"无句柄也能跑"的那批。
"""
import json
import os
import subprocess
import sys

import pytest

from _manifest import SDKS, load as load_manifest, project_root

SWEEP = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_zeroarg_sweep.py")

#: 实测空参调用即崩（ACCESS_VIOLATION）。每条都必须"至今仍崩"，见模块 docstring。
BLACKLIST = {
    "dahua": set(),
    "haikang": {"NET_DVR_LoadAllCom"},
}


def _skip_if_no_manifest(sdk):
    if load_manifest(sdk) is None:
        pytest.skip("gen_manifest.json 缺失：先跑 "
                    "`python native/codegen/gen_bind.py --sdk %s`" % sdk)


def _run(sdk, extra=()):
    """子进程跑一次扫描。返回 (returncode, stdout, stderr)。"""
    argv = [sys.executable, SWEEP, sdk] + list(extra)
    proc = subprocess.run(argv, capture_output=True, text=True, encoding="utf-8",
                          errors="replace", cwd=project_root())
    return proc.returncode, proc.stdout, proc.stderr


def _last_call(stdout):
    """崩溃前打印的最后一个 `CALL <fn>` —— 就是元凶。"""
    calls = [ln.strip()[5:] for ln in stdout.splitlines() if ln.strip().startswith("CALL ")]
    return calls[-1] if calls else None


def _result(stdout):
    for ln in reversed(stdout.splitlines()):
        if ln.startswith("RESULT "):
            return json.loads(ln[len("RESULT "):])
    return None


@pytest.mark.parametrize("sdk", SDKS)
def test_zeroarg_sweep(pyd, sdk):
    """全量空参调用：不崩、不漏绑、分类能对上账。"""
    _skip_if_no_manifest(sdk)
    pyd(sdk)                     # 没编译就 skip，别让子进程报难懂的 import 错

    skip = BLACKLIST[sdk]
    code, out, err = _run(sdk, ("--skip", ",".join(sorted(skip))) if skip else ())

    if code != 0:
        crashed = _last_call(out)
        pytest.fail(
            "[%s] 空参扫描子进程异常退出（code=%s），崩在 %s\n"
            "0xC0000005 / 3221225477 = ACCESS_VIOLATION：这是**真的会崩进程**的调用，\n"
            "确认后加进本文件的 BLACKLIST；否则是绑定回归。\n"
            "--- stderr ---\n%s" % (sdk, code, crashed or "(未捕获到 CALL 行)", err[-2000:]))

    res = _result(out)
    assert res is not None, "[%s] 子进程正常退出但没打印 RESULT：\n%s" % (sdk, out[-2000:])

    assert res["missing"] == [], (
        "[%s] manifest 里有 %d 个函数在 pyd 上不存在：%s\n"
        "生成器漏绑了，或 manifest 与 pyd 不同步（重跑 gen_bind.py）"
        % (sdk, len(res["missing"]), ", ".join(res["missing"][:20])))

    expected = len(load_manifest(sdk)["functions"]) - len(skip)
    assert res["total"] == expected, (
        "[%s] 扫描了 %d 个函数，manifest 减去黑名单应是 %d 个"
        % (sdk, res["total"], expected))

    # 三种结局必须刚好覆盖全部：arity（没进 C）+ called（执行了）+ raised（执行后报错）
    accounted = res["arity"] + len(res["called"]) + sum(res["raised"].values())
    assert accounted == res["total"], (
        "[%s] 分类对不上账：arity %d + called %d + raised %d != total %d"
        % (sdk, res["arity"], len(res["called"]), sum(res["raised"].values()), res["total"]))


@pytest.mark.parametrize("sdk,fn", [
    (sdk, fn) for sdk in SDKS for fn in sorted(BLACKLIST[sdk])
])
def test_blacklist_still_crashes(sdk, fn):
    """黑名单不是免死金牌：名单里的函数必须**至今仍崩**，否则该条目已过期。"""
    _skip_if_no_manifest(sdk)
    code, _out, _err = _run(sdk, ("--only", fn))
    assert code != 0, (
        "[%s] %s 空参调用不再崩进程了 —— 要么 SDK 修了，要么当初判错。\n"
        "请从 test_functions.py 的 BLACKLIST 里删掉它，让它重新回到全量扫描。"
        % (sdk, fn))


def test_dahua_sdk_version_matches_header(pyd):
    """运行时 DLL 报的 build 号 == 绑定所依据的 SDK 版本（承接原 verify_runtime.py）。

    36192074 是 dhnetsdk **3.6.1.92074** 的 build 号，见 README「SDK 版本」表。
    两者不一致说明 pyd 与 DLL 版本对不上 —— 那种"编译能过、程序能跑、但字段与
    DLL 实际行为对不上"的问题最难查，值得一条断言守着。

    海康没有对应断言：`NET_DVR_GetSDKVersion()` 未 Init 时返回 0，不适合作 golden。
    """
    assert pyd("dahua").CLIENT_GetSDKVersion() == 36192074