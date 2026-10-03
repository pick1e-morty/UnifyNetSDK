# 大华 NetSDK nanobind 绑定：配置 + 编译 + 冒烟测试
#
# 用法:
#   powershell -ExecutionPolicy Bypass -File build.ps1
#   powershell -ExecutionPolicy Bypass -File build.ps1 -Config Debug
#   powershell -ExecutionPolicy Bypass -File build.ps1 -SkipTest
param(
    [string]$Config = "Release",
    [switch]$SkipTest,
    # 0 = 交给 ninja 自行决定（CPU 核数+2）。122 个大 TU 并发编译时
    # 每个 cl 都要吞 8.7MB 的 dhnetsdk.h，内存峰值高，用 -Jobs 8 收敛一下。
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

# stdout 必须走 Out-Host，否则会成为函数返回值
function Invoke-Bat {
    param([string[]]$Lines)
    $bat = Join-Path $here "_tmp_build.bat"
    ($Lines -join "`r`n") | Out-File -FilePath $bat -Encoding ascii
    $prev = $ErrorActionPreference
    $ErrorActionPreference = 'Continue'
    & cmd.exe /c $bat 2>&1 | Out-Host
    $code = $LASTEXITCODE
    $ErrorActionPreference = $prev
    Remove-Item $bat -ErrorAction SilentlyContinue
    return $code
}

Write-Host ""
Write-Host "=== configure ($Config) ===" -ForegroundColor Cyan
$rc = Invoke-Bat @(
    '@echo off',
    "call `"$vcvars`" x64",
    "cmake -G Ninja -B build -DCMAKE_BUILD_TYPE=$Config -DNB_PYTHON=`"$venvPy`" -DPython_EXECUTABLE=`"$venvPy`" -DCMAKE_MAKE_PROGRAM=`"$ninja`" ."
)
if ($rc -ne 0) { Write-Host "configure FAILED (exit $rc)" -ForegroundColor Red; exit 1 }

Write-Host ""
Write-Host "=== build ===" -ForegroundColor Cyan
$buildLine = "cmake --build build"
if ($Jobs -gt 0) { $buildLine += " -- -j $Jobs" }
$sw = [System.Diagnostics.Stopwatch]::StartNew()
$rc = Invoke-Bat @(
    '@echo off',
    "call `"$vcvars`" x64",
    $buildLine
)
$sw.Stop()
Write-Host ("build 耗时: {0:N1} s" -f $sw.Elapsed.TotalSeconds) -ForegroundColor Green
if ($rc -ne 0) { Write-Host "build FAILED (exit $rc)" -ForegroundColor Red; exit 1 }

if (-not $SkipTest) {
    Write-Host ""
    Write-Host "=== smoke test ===" -ForegroundColor Cyan
    & $venvPy (Join-Path $here 'smoke_test.py')
    exit $LASTEXITCODE
}
