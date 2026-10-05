# -*- coding: utf-8 -*-
"""空参调用扫描的执行体 —— **必须作为子进程跑**，不能直接在 pytest 进程里循环。

理由（2026-10-05 实测）：海康 `NET_DVR_LoadAllCom()` 空参调用直接 ACCESS_VIOLATION
（退出码 0xC0000005）把整个进程带走。若在 pytest 进程里全量调用，一个函数崩溃 =
整个测试会话无输出地死掉，连"崩在哪个函数"都拿不到。放到子进程里，父进程（
`test_functions.py`）能拿到退出码与崩溃前最后一行输出。

调用方式：

    python native/tests/_zeroarg_sweep.py <sdk> [--skip fn1,fn2] [--only <函数名>]

- 不带 `--only`：扫 manifest 里的全部函数（减去 `--skip` 的黑名单）。
- `--only <fn>`：只调这一个函数。用来证明"黑名单里的函数**仍然会崩**" —— 黑名单
  不是免死金牌，名单过期（SDK 修了 / 当初判错）要被发现。

输出约定（父进程靠它定位崩溃点）：
  - 每调一个函数前打印一行 `CALL <函数名>`（flush=True），崩溃时最后一行即元凶；
  - 全部跑完打印一行 `RESULT <json>`。

一种函数的结局只有三种：nanobind 派发层因参数个数不符抛 `TypeError`（**根本没进
C**）、真的执行了、或者把进程干掉。
"""
import collections
import importlib.util
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def _project_root():
    d = HERE
    while True:
        if os.path.isfile(os.path.join(d, "native", "CMakeLists.txt")):
            return d
        parent = os.path.dirname(d)
        if parent == d:
            raise RuntimeError("project root not found above %s" % d)
        d = parent


def _load(sdk):
    """返回 (模块, manifest)。路径推导与 conftest.py 同源（向上找锚点）。"""
    root = _project_root()
    sys.path.insert(0, os.path.join(root, "native", "codegen"))
    from config import get_config                             # noqa: E402

    cfg = get_config(sdk)
    os.add_dll_directory(os.path.dirname(cfg["dll"]))

    # pyd 文件名里的 ABI tag 与 conftest.PYDS / CMakeLists 是同一个约定
    pyd = os.path.join(cfg["build_dir"], "%s.cp313-win_amd64.pyd" % cfg["module"])
    spec = importlib.util.spec_from_file_location(cfg["module"], pyd)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[cfg["module"]] = mod
    spec.loader.exec_module(mod)

    with open(os.path.join(cfg["out_dir"], "gen_manifest.json"), encoding="ascii") as f:
        man = json.load(f)
    return mod, man


def main(argv):
    sdk = argv[1]
    only, skip = None, set()
    rest = list(argv[2:])
    while rest:
        arg = rest.pop(0)
        if arg == "--only":
            only = rest.pop(0)
        elif arg == "--skip":
            skip = {x for x in rest.pop(0).split(",") if x}
        else:
            raise SystemExit("unknown argument: %s" % arg)

    mod, man = _load(sdk)
    if only:
        names = [only]
    else:
        names = [n for n in man["functions"] if n not in skip]

    missing, called, arity = [], [], 0
    raised = collections.Counter()

    for fn in names:
        try:
            f = getattr(mod, fn)
        except AttributeError:
            missing.append(fn)
            continue
        print("CALL %s" % fn, flush=True)
        try:
            f()
        except TypeError as exc:
            # nanobind 参数个数不符：在派发层就抛了，没进 C，安全
            if "argument" in str(exc):
                arity += 1
            else:
                raised["TypeError: %s" % str(exc)[:70]] += 1
        except Exception as exc:                              # noqa: BLE001
            # 函数真的执行了，只是报错（无设备时的正常结局），不算失败
            raised["%s: %s" % (type(exc).__name__, str(exc)[:70])] += 1
        else:
            called.append(fn)

    print("RESULT " + json.dumps({
        "sdk": sdk,
        "only": only,
        "total": len(names),
        "missing": missing,
        "arity": arity,
        "called": called,
        "raised": dict(raised),
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))