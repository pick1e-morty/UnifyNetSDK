# 厂商 NetSDK nanobind 绑定：配置 + 编译 + 冒烟测试
#
# 用法:
#   powershell -ExecutionPolicy Bypass -File build.ps1
#   powershell -ExecutionPolicy Bypass -File build.ps1 -Config Debug
#   powershell -ExecutionPolicy Bypass -File build.ps1 -SkipTest
#   powershell -ExecutionPolicy Bypass -File build.ps1 -Sdk dahua
#   powershell -ExecutionPolicy Bypass -File build.ps1 -Sdk haikang
param(
    [string]$Config = "Release",
    [switch]$SkipTest,
    # 构建哪些厂商。两个厂商是彼此独立的 target，ninja 会把它们的 TU 混进
    # 同一个 -j N 池子**并行**编译，不是串行 —— 所以选厂商不是"避免等两个"，
    # 而是日常只改一个时不必让另一个进依赖图。
    #
    #   dahua（默认）：只建大华。**海康还没编通**（SDK 头文件大量类型被
    #     `#if defined(__linux__)` 之类的条件编译包着，生成器无条件绑定会报
    #     "未声明的标识符"），所以默认不选它 —— 裸跑 build.ps1 必须能成功。
    #   haikang：只建海康。
    #   all：两个都建。海康编通后再用它，或在海康专用工作流里显式指定。
    [ValidateSet("dahua", "haikang", "all")]
    [string]$Sdk = "dahua",
    # 0 = 交给 ninja 自行决定（CPU 核数+2）。160+ 个大 TU 并发编译时
    # 每个 cl 都要吞 8.7MB 的 SDK 头，内存峰值高，用 -Jobs 8 收敛一下。
    [int]$Jobs = 0
)

$ErrorActionPreference = "Stop"
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $here

# --- 定位 MSVC ---
$vswhere = 'C:\Program Files (x86)\Microsoft Visual Studio\Installer\vswhere.exe'
$vcvars = $null
if (Test-Path $vswhere) {
    $vsPath = & $vswhere -latest -property installationPath 2>$null
    if ($vsPath) {
        $cand = Join-Path $vsPath 'VC\Auxiliary\Build\vcvarsall.bat'
        if (Test-Path $cand) { $vcvars = $cand }
    }
}
if (-not $vcvars) {
    Write-Host "找不到 MSVC (vcvarsall.bat)。装 Microsoft C++ Build Tools:" -ForegroundColor Yellow
    Write-Host "  https://aka.ms/vs/17/release/vs_BuildTools.exe" -ForegroundColor Cyan
    exit 1
}
Write-Host "MSVC : $vcvars" -ForegroundColor Green

# 项目根的统一 .venv（native/../.venv）
$root = Split-Path -Parent $here
$venvPy = Join-Path $root '.venv\Scripts\python.exe'
$ninja = Join-Path $root '.venv\Scripts\ninja.exe'
if (-not (Test-Path $venvPy) -or -not (Test-Path $ninja)) {
    Write-Host "缺项目根的 .venv 或 ninja。在项目根运行:" -ForegroundColor Red
    Write-Host "  uv venv --python 3.13" -ForegroundColor Cyan
    Write-Host "  uv pip install nanobind ninja tqdm" -ForegroundColor Cyan
    exit 1
}
Write-Host "PY   : $venvPy" -ForegroundColor Green
Write-Host "NINJA: $ninja" -ForegroundColor Green

# 执行一段 bat，**同时**做两件事：把输出逐行实时打到屏幕上，并把同一份输出
# 留下来做统计分析。
#
# 之前只 Out-Host 不保留，脚本无法回答"哪个厂商失败、失败了几处"（两个厂商的
# 产物目录 src/gen 与 src/gen_hk 只差两个字母，肉眼极易看错）。但改成
# `$out = & cmd ...` 之后再 Out-Host 也同样是错的 —— 那会把全部输出攒到命令
# 结束才吐出来，海康编译 160 s 期间屏幕完全空白，而用户正是靠进度条判断
# "还在跑 / 卡住了"。所以必须**边收边打**：ForEach-Object 每收到一行就立刻
# Out-Host，同时追加到缓冲区。
function Invoke-Bat {
    param([string[]]$Lines)
    $bat = Join-Path $here "_tmp_build.bat"
    ($Lines -join "`r`n") | Out-File -FilePath $bat -Encoding ascii
    $prev = $ErrorActionPreference
    $ErrorActionPreference = 'Continue'
    $buf = [System.Collections.ArrayList]::new()
    & cmd.exe /c $bat 2>&1 | ForEach-Object {
        [void]$buf.Add($_)
        $_ | Out-Host
    }
    $code = $LASTEXITCODE
    $ErrorActionPreference = $prev
    Remove-Item $bat -ErrorAction SilentlyContinue
    return @{ Code = $code; Out = $buf }
}

# 数编译错误条数。只认 "error <LETTER><digits>"（MSVC / clang 的诊断格式），
# 避免把 "error C2757: 'cbrt': ...已存在" 里的中文说明二次计入。
function Count-Errors($out) {
    $n = 0
    foreach ($line in $out) {
        if ($line -match '\berror\s+[A-Za-z]+\d+') { $n++ }
    }
    return $n
}

Write-Host ""
Write-Host "=== configure ($Config, Sdk=$Sdk) ===" -ForegroundColor Cyan
$r = Invoke-Bat @(
    '@echo off',
    "call `"$vcvars`" x64",
    "cmake -G Ninja -B build -DCMAKE_BUILD_TYPE=$Config -DUNIFY_SDK=$Sdk -DNB_PYTHON=`"$venvPy`" -DPython_EXECUTABLE=`"$venvPy`" -DCMAKE_MAKE_PROGRAM=`"$ninja`" ."
)
if ($r.Code -ne 0) { Write-Host "configure FAILED (exit $($r.Code))" -ForegroundColor Red; exit 1 }

# ---------------------------------------------------------------
# 按厂商**分别**构建，而不是一次 cmake --build 全部
#
# 为什么不用一次构建：cmake --build 是全有或全无 —— 任一 target 失败，
# 整条命令返回非 0，于是**另一个厂商的 .pyd 也拿不到**。但这两个 pyd
# 是两份独立交付物（unify-dh 与 unify-hk 两个 wheel），海康写坏了不该
# 让大华也编不出来。这才是真正的耦合，而它是可以拆掉的。
#
# 代价：失去跨厂商并行。同一厂商**内部**仍是满并发（-j $Jobs 不变），
# 而日常一次只改一个厂商，另一个 ninja 直接跳过，墙钟基本不受影响。
# ---------------------------------------------------------------
$VENDOR_TARGETS = @{
    'dahua'   = @('unify_dh', 'unify_dh_gen')
    'haikang' = @('unify_hk_gen')
}

$vendors = if ($Sdk -eq 'all') { @('dahua', 'haikang') } else { @($Sdk) }

# 先从 configure 输出里确认哪些 target 真的存在（没有生成产物时 CMake 会 skip），
# 否则 --target 一个不存在的名字会直接报错。
$configured = @{}
foreach ($line in $r.Out) {
    foreach ($v in $vendors) {
        foreach ($t in $VENDOR_TARGETS[$v]) {
            if ($line -match [regex]::Escape($t) -and $line -notmatch 'skipped') {
                $configured[$t] = $true
            }
        }
    }
}

$results = [ordered]@{}
foreach ($v in $vendors) {
    $tgts = @($VENDOR_TARGETS[$v] | Where-Object { $configured.ContainsKey($_) })
    Write-Host ""
    if ($tgts.Count -eq 0) {
        Write-Host "=== build $v : 跳过（本次 configure 未生成该厂商的 target）===" -ForegroundColor Yellow
        $results[$v] = @{ Ok = $true; Errs = 0; Secs = 0.0; Targets = @() }
        continue
    }
    Write-Host ("=== build {0}  ({1}) ===" -f $v, ($tgts -join ' ')) -ForegroundColor Cyan
    $line = "cmake --build build --target " + ($tgts -join ' ')
    if ($Jobs -gt 0) { $line += " -- -j $Jobs" }
    $sw = [System.Diagnostics.Stopwatch]::StartNew()
    $rb = Invoke-Bat @('@echo off', "call `"$vcvars`" x64", $line)
    $sw.Stop()
    $errs = Count-Errors $rb.Out
    $ok = ($rb.Code -eq 0)
    $results[$v] = @{ Ok = $ok; Errs = $errs; Secs = $sw.Elapsed.TotalSeconds; Targets = $tgts }
    if ($ok) {
        Write-Host ("[{0}] 成功  ({1:N1} s)" -f $v, $sw.Elapsed.TotalSeconds) -ForegroundColor Green
    } else {
        Write-Host ("[{0}] 失败  ({1:N1} s, {2} 处编译错误)" -f $v, $sw.Elapsed.TotalSeconds, $errs) -ForegroundColor Red
    }
}

# ---------------------------------------------------------------
# 汇总：一眼看出哪个厂商好了、哪个没好、产物在不在
# ---------------------------------------------------------------
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host " 构建汇总" -ForegroundColor Cyan
$anyFail = $false
foreach ($v in $vendors) {
    $r2 = $results[$v]
    if (-not $r2.Ok) {
        $anyFail = $true
        Write-Host ("   {0,-8} 失败  {1} 处错误   目标: {2}" -f $v, $r2.Errs, ($r2.Targets -join ' ')) -ForegroundColor Red
    } elseif ($r2.Targets.Count -eq 0) {
        Write-Host ("   {0,-8} 跳过  未生成" -f $v) -ForegroundColor Yellow
    } else {
        Write-Host ("   {0,-8} 成功  {1:N1} s" -f $v, $r2.Secs) -ForegroundColor Green
    }
}
Write-Host "========================================" -ForegroundColor Cyan

if ($anyFail) {
    Write-Host ""
    Write-Host "提示：错误行里的路径已标明归属厂商 —— src\gen\   是大华 (dh)，" -ForegroundColor Yellow
    Write-Host "      src\gen_hk\ 是海康 (hk)。文件名只差 hk 两字，注意别看串。" -ForegroundColor Yellow
    Write-Host "      单独重编某个厂商：build.ps1 -Sdk dahua | -Sdk haikang" -ForegroundColor Yellow
    exit 1
}

if (-not $SkipTest) {
    # smoke_test.py 是大华专用的（测 CLIENT_Login / dhnetsdk.dll）。
    # 选了别的厂商就没东西可测，直接跳过而不是报一个误导性的失败。
    if ($vendors -notcontains 'dahua') {
        Write-Host ""
        Write-Host "=== smoke test: 跳过（本次不含大华，smoke_test.py 只覆盖大华）===" -ForegroundColor Yellow
    } else {
        Write-Host ""
        Write-Host "=== smoke test ===" -ForegroundColor Cyan
        & $venvPy (Join-Path $here 'smoke_test.py')
        exit $LASTEXITCODE
    }
}
