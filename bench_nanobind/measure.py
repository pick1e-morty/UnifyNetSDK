#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
nanobind 编译耗时实测（带 tqdm 进度条）

在 cmd / PowerShell 里运行:

    .venv\\Scripts\\python.exe measure.py
    .venv\\Scripts\\python.exe measure.py --config Release
    .venv\\Scripts\\python.exe measure.py probe_5000 --config Release
    .venv\\Scripts\\python.exe measure.py --no-configure

关于进度条，有个事实要先说清楚:

  * MSVC 编译**单个** .cpp 期间不输出任何中间状态。所以单文件 target
    （probe_500 / 2000 / 5000）的进度是**按时间插值估算**出来的，
    依据是下面的 ETA 表（fixed + per_field * N 模型）。
  * 一旦把大 TU 拆成多个 .cpp，ninja 会输出 [n/N]，脚本读到后会切成
    **真实进度**。两条曲线取较大值，保证进度条单调不倒退。

外推仍以实测为准，ETA 只影响进度条观感，不影响结果。
"""
import argparse
import os
import re
import subprocess
import sys
import threading
import time

try:
    from tqdm import tqdm
except ImportError:
    sys.exit("缺少 tqdm。先运行:  uv pip install tqdm --python .venv\\Scripts\\python.exe")

HERE = os.path.dirname(os.path.abspath(__file__))
VENV_PY = os.path.join(HERE, '.venv', 'Scripts', 'python.exe')
NINJA = os.path.join(HERE, '.venv', 'Scripts', 'ninja.exe')
DH_INCLUDE = os.path.normpath(
    os.path.join(HERE, '..', 'dahua', 'C_Win64', 'Include', 'Common'))

# 各 probe 实际绑定的字段数（由 gen_probe.py 输出确认）
FIELD_COUNT = {
    'probe_base': 0,
    'probe_500': 506,
    'probe_2000': 2005,
    'probe_5000': 5014,
}

# 进度条 ETA 预估（秒）。Release 下的经验值: t ≈ 5 + 0.0315 * N
ETA_SECONDS = {
    'probe_base': 6.0,
    'probe_500': 21.0,
    'probe_2000': 68.0,
    'probe_5000': 163.0,
}

STEP_RE = re.compile(r'^\s*\[(\d+)/(\d+)\]')


def find_vcvars():
    vswhere = r'C:\Program Files (x86)\Microsoft Visual Studio\Installer\vswhere.exe'
    if os.path.isfile(vswhere):
        try:
            out = subprocess.run([vswhere, '-latest', '-property', 'installationPath'],
                                 capture_output=True, text=True, timeout=30).stdout.strip()
        except Exception:
            out = ''
        if out:
            p = os.path.join(out, 'VC', 'Auxiliary', 'Build', 'vcvarsall.bat')
            if os.path.isfile(p):
                return p
    return None


def estimate_eta(target):
    if target in ETA_SECONDS:
        return ETA_SECONDS[target]
    m = re.search(r'(\d+)', target)
    n = int(m.group(1)) if m else 500
    return max(6.0, 5.0 + 0.0315 * n)


def run_cmd(lines, desc, eta, show_bar=True, log_path=None):
    """把若干行命令写进临时 .bat 执行；返回 (exit_code, 输出文本)。"""
    bat = os.path.join(HERE, '_tmp_measure.bat')
    with open(bat, 'w', encoding='ascii', errors='replace') as f:
        f.write('\r\n'.join(lines) + '\r\n')

    proc = subprocess.Popen(['cmd.exe', '/c', bat], cwd=HERE,
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                            encoding='utf-8', errors='replace', bufsize=1)
    out_lines = []
    state = {'done': 0, 'total': 0}

    def reader():
        for line in proc.stdout:
            out_lines.append(line)
            m = STEP_RE.match(line)
            if m:
                state['done'], state['total'] = int(m.group(1)), int(m.group(2))

    th = threading.Thread(target=reader, daemon=True)
    th.start()

    fmt = '{desc}: {percentage:3.0f}%|{bar:28}| [{elapsed}<{remaining}]'
    t0 = time.perf_counter()
    if show_bar:
        bar = tqdm(total=100, desc=desc, unit='%', leave=True,
                   bar_format=fmt, dynamic_ncols=True)
        cur = 0.0
        while proc.poll() is None:
            time.sleep(0.1)
            el = time.perf_counter() - t0
            by_time = 100.0 * el / eta if eta > 0 else 0.0
            by_step = 100.0 * state['done'] / state['total'] if state['total'] else 0.0
            pct = min(max(by_time, by_step), 99.0)
            if pct > cur:
                bar.update(pct - cur)
                cur = pct
        bar.update(100.0 - cur)
        bar.close()
    else:
        proc.wait()

    th.join(timeout=2)
    code = proc.returncode
    elapsed = time.perf_counter() - t0

    text = ''.join(out_lines)
    if log_path:
        with open(log_path, 'w', encoding='utf-8', errors='replace') as f:
            f.write(text)
    return code, elapsed, text


def main():
    ap = argparse.ArgumentParser(description='nanobind 编译耗时实测')
    ap.add_argument('targets', nargs='*', default=None,
                    help='要编译的 target（默认 probe_base probe_500 probe_2000 probe_5000）')
    ap.add_argument('--config', default='Release', choices=['Release', 'Debug', 'RelWithDebInfo'])
    ap.add_argument('--no-configure', action='store_true')
    ap.add_argument('--verbose', action='store_true', help='编译时透传 -v')
    args = ap.parse_args()

    targets = args.targets or ['probe_base', 'probe_500', 'probe_2000', 'probe_5000']

    vcvars = find_vcvars()
    if not vcvars:
        print('找不到 MSVC。装 Microsoft C++ Build Tools:')
        print('  https://aka.ms/vs/17/release/vs_BuildTools.exe')
        return 1
    print('MSVC  :', vcvars)
    print('PY    :', VENV_PY)
    print('NINJA :', NINJA)
    if not os.path.isfile(VENV_PY) or not os.path.isfile(NINJA):
        print('缺 .venv 或 ninja。先: uv venv --python 3.13 && uv pip install nanobind ninja tqdm')
        return 1

    cfg = {'Release': 'Release', 'Debug': 'Debug', 'RelWithDebInfo': 'RelWithDebInfo'}[args.config]

    if not args.no_configure:
        print()
        print('=== configure (%s) ===' % args.config)
        conf = ['@echo off',
                'call "%s" x64' % vcvars,
                ('cmake -G Ninja -B build -DCMAKE_BUILD_TYPE=%s'
                 ' -DNB_PYTHON="%s" -DPython_EXECUTABLE="%s"'
                 ' -DCMAKE_MAKE_PROGRAM="%s" .'
                 % (cfg, VENV_PY, VENV_PY, NINJA))]
        code, secs, text = run_cmd(conf, 'configure', 3.0, show_bar=False,
                                   log_path=os.path.join(HERE, 'configure.log'))
        # 打印关键行，便于确认用的是 venv 的 Python
        for ln in text.splitlines():
            if re.search(r'nanobind cmake dir|^-- Python|Configuring done|Generating done|Build files', ln):
                print('   ', ln.strip())
        if code != 0:
            print(text[-3000:])
            return code

    rows = []
    for t in targets:
        eta = estimate_eta(t)
        print()
        code, secs, text = run_cmd(
            ['@echo off',
             'call "%s" x64' % vcvars,
             'cmake --build build --target %s%s' % (t, ' -v' if args.verbose else '')],
            t, eta, show_bar=True, log_path=os.path.join(HERE, t + '.log'))
        ok = (code == 0)
        pyd = None
        for fn in os.listdir(os.path.join(HERE, 'build')):
            if fn.startswith(t) and fn.endswith('.pyd'):
                pyd = os.path.join(HERE, 'build', fn)
                break
        mb = round(os.path.getsize(pyd) / 1048576.0, 2) if pyd else 0.0
        if not ok:
            print('    FAILED (exit %d)，日志尾部:' % code)
            for ln in text.strip().splitlines()[-25:]:
                print('   ', ln)
        rows.append((t, ok, secs, mb, eta))

    print()
    print('=== RESULT ===')
    print('%-16s %-6s %10s %10s %10s' % ('target', 'status', 'time_s', 'size_mb', 'fields'))
    for t, ok, secs, mb, _ in rows:
        print('%-16s %-6s %10.1f %10.2f %10s'
              % (t, 'OK' if ok else 'FAIL', secs, mb, FIELD_COUNT.get(t, '-')))

    pts = [(FIELD_COUNT[t], s) for t, ok, s, _, _ in rows if ok and t in FIELD_COUNT]
    if len(pts) < 2:
        print()
        print('（可拟合的点不足 2 个，跳过外推）')
        return 0

    print()
    print('=== FIT (fields -> seconds) ===')
    for n, s in sorted(pts):
        print('  %6d fields -> %8.1f s' % (n, s))

    k = float(len(pts))
    sx = sum(p[0] for p in pts)
    sy = sum(p[1] for p in pts)
    sxy = sum(p[0] * p[1] for p in pts)
    sxx = sum(p[0] * p[0] for p in pts)
    denom = k * sxx - sx * sx
    if denom == 0:
        return 0
    slope = (k * sxy - sx * sy) / denom
    icept = (sy - slope * sx) / k
    print()
    print('  model: t = %.1f + %.6f * fields' % (icept, slope))
    # 60563 = 大华可绑定字段（61881 总量减去 297 函数指针 + 1021 裸指针）
    # 80269 = + 海康 19706（海康尚未过滤指针，是上界估计）
    for n, label in ((60563, 'dahua bindable'), (80269, 'dahua+hik est')):
        v = icept + slope * n
        print('  extrapolate %6d (%-15s): %8.0f s = %6.1f min  [单线程]' % (n, label, v, v / 60.0))
    # 8 核 16 线程，按 12 路并行粗估
    for n, label in ((60563, 'dahua bindable'), (80269, 'dahua+hik est')):
        v = icept + slope * n
        print('  extrapolate %6d (%-15s): %8.0f s = %6.1f min  [假设 12 路并行]'
              % (n, label, v / 12.0, v / 720.0))
    return 0


if __name__ == '__main__':
    sys.exit(main())
