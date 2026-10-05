# -*- coding: utf-8 -*-
"""pyd 加载器与 SDK 生命周期：dhbind 唯一碰 native 产物的地方。

加载布局（wheel 安装后与源码仓库里完全一致）：

    dhbind/
    ├── __init__.py / client.py / errors.py / _native.py
    └── _binding/
        ├── unify_dh_gen.cp313-win_amd64.pyd    # 生成版全量绑定
        ├── dhnetsdk.dll                        # 厂商运行库
        └── libeay32.dll / ssleay32.dll / ...

_binding 由 `tools/fill_binding.py --sdk dahua` 填充，不入库。

两个设计点：

1. **add_dll_directory 必须在 exec_module 之前**：import pyd 时 Windows 按依赖
   链解析 dhnetsdk.dll -> libeay32/ssleay32，目录没先注册就报 DLL load failed。
2. **eager 加载，不搞懒加载**：`import dhbind` 就该证明"包是完整的"——这正是
   wheel 归属性的体现（artifact smoke 的核心断言也是它）。_binding 缺失时报
   带 remediation 的错误，而不是让用户在半初始化状态下撞到 AttributeError。
"""
import importlib.util
import os
import sys
import threading

_BINDING = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_binding")

#: (模块名, _binding 下的文件名模板)。pyd 文件名带 ABI 标签，按前缀匹配。
_MODULES = {
    "unify_dh_gen": "unify_dh_gen.cp313-win_amd64.pyd",
}

_loaded = {}
_loaded_lock = threading.Lock()
_sdk_inited = False


def _load_one(modname, filename):
    path = os.path.join(_BINDING, filename)
    spec = importlib.util.spec_from_file_location(modname, path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load extension module from %s" % path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[modname] = module
    spec.loader.exec_module(module)
    return module


def _ensure_loaded():
    """加载 _binding 下的全部 pyd（幂等，线程安全）。"""
    global _sdk_inited
    with _loaded_lock:
        if _loaded:
            return _loaded
        if not os.path.isdir(_BINDING):
            raise RuntimeError(
                "dhbind/_binding 不存在。先运行:\n"
                "    python tools/fill_binding.py --sdk dahua\n"
                "把 pyd 与厂商 DLL 填进包里（wheel 打包同样依赖它）。")
        missing = [f for f in _MODULES.values()
                   if not os.path.isfile(os.path.join(_BINDING, f))]
        if missing:
            raise RuntimeError(
                "dhbind/_binding 缺少 %s。先运行:\n"
                "    python tools/fill_binding.py --sdk dahua" % ", ".join(missing))
        # DLL 目录必须先注册（见模块 docstring 第 1 点）
        os.add_dll_directory(_BINDING)
        for modname, filename in _MODULES.items():
            _loaded[modname] = _load_one(modname, filename)
        # CLIENT_Init 是进程级的：init 一次，所有 Client 共享
        _loaded["unify_dh_gen"].CLIENT_Init(0, 0)   # 无断线回调（MVP）
        _loaded["unify_dh_gen"].CLIENT_SetConnectTime(5000, 3)
        _sdk_inited = True
        return _loaded


def gen():
    """生成版全量绑定模块（unify_dh_gen）：结构体 / 函数 / 回调三件套。

    所有函数绑定一律带 ``nb::call_guard<nb::gil_scoped_release>()``，语义与
    ``ctypes.CDLL`` 等比：每次外部调用都不持 GIL。线程安全由 Python 上层负责。
    """
    return _ensure_loaded()["unify_dh_gen"]


def sdk_inited():
    return _sdk_inited


def shutdown():
    """CLIENT_Cleanup。进程级操作：会断开所有会话，仅测试收尾时调用。"""
    global _sdk_inited
    with _loaded_lock:
        if _loaded and _sdk_inited:
            _loaded["unify_dh_gen"].CLIENT_Cleanup()
            _sdk_inited = False


# eager：import dhbind 即加载并 CLIENT_Init —— "包是完整的"由 import 本身证明
_ensure_loaded()
