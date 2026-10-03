# nanobind compile-time benchmark
# Usage:
#   powershell -ExecutionPolicy Bypass -File build_measure.ps1 -Config Debug
#   powershell -ExecutionPolicy Bypass -File build_measure.ps1 -Config Release -Targets probe_base,probe_500
param(
    [string]$Config = "Debug",
    [string[]]$Targets = @('probe_base', 'probe_500', 'probe_2000', 'probe_5000')
)

$ErrorActionPreference = "Stop"
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $here

# --- helper: write a temp .bat and run it (avoids PS->cmd quoting issues) ---
# NOTE: stdout must go to Out-Host, otherwise it becomes the function's return value.
function Invoke-Bat {
    param([string[]]$Lines)
    $bat = Join-Path $here "_tmp_run.bat"
    ($Lines -join "`r`n") | Out-File -FilePath $bat -Encoding ascii
    # native stderr would abort the script under $ErrorActionPreference='Stop'
    $prev = $ErrorActionPreference
    $ErrorActionPreference = 'Continue'
    & cmd.exe /c $bat 2>&1 | Out-Host
    $code = $LASTEXITCODE
    $ErrorActionPreference = $prev
    return $code
}

# --- 1) locate MSVC via vswhere (do not hardcode VS year/version) ---
$vswhere = 'C:\Program Files (x86)\Microsoft Visual Studio\Installer\vswhere.exe'
$vcvars = $null
if (Test-Path $vswhere) {
    $vsPath = & $vswhere -latest -property installationPath 2>$null
    if ($vsPath) {
        $cand = Join-Path $vsPath 'VC\Auxiliary\Build\vcvarsall.bat'
        if (Test-Path $cand) { $vcvars = Get-Item $cand }
    }
}
if (-not $vcvars) {
    Write-Host ""
    Write-Host "MSVC not found (vcvarsall.bat). Install Microsoft C++ Build Tools:" -ForegroundColor Yellow
    Write-Host "  https://aka.ms/vs/17/release/vs_BuildTools.exe" -ForegroundColor Cyan
    exit 1
}
$vcvarsPath = $vcvars.FullName
Write-Host "MSVC : $vcvarsPath" -ForegroundColor Green

# --- 2) venv python + ninja ---
$venvPy = Join-Path $here ".venv\Scripts\python.exe"
$ninjaExe = Join-Path $here ".venv\Scripts\ninja.exe"
if (-not (Test-Path $venvPy) -or -not (Test-Path $ninjaExe)) {
    Write-Host "Missing .venv or ninja. Run:" -ForegroundColor Red
    Write-Host "  uv venv --python 3.13" -ForegroundColor Cyan
    Write-Host "  uv pip install nanobind ninja" -ForegroundColor Cyan
    exit 1
}
Write-Host "PY   : $venvPy" -ForegroundColor Green
Write-Host "NINJA: $ninjaExe" -ForegroundColor Green

# --- 3) configure (reuse existing build dir if present) ---
$build = Join-Path $here "build"
Write-Host ""
Write-Host "=== configure ($Config) ===" -ForegroundColor Cyan
$rc = Invoke-Bat @(
    '@echo off',
    "call `"$vcvarsPath`" x64",
    "cmake -G Ninja -B build -DCMAKE_BUILD_TYPE=$Config -DNB_PYTHON=`"$venvPy`" -DCMAKE_MAKE_PROGRAM=`"$ninjaExe`" ."
)
if ($rc -ne 0) { Write-Host "configure FAILED (exit $rc)" -ForegroundColor Red; exit 1 }

# --- 4) build each target and time it ---
$rows = @()
foreach ($t in $Targets) {
    Write-Host ""
    Write-Host "=== build $t ===" -ForegroundColor Cyan
    $sw = [System.Diagnostics.Stopwatch]::StartNew()
    $rc = Invoke-Bat @(
        '@echo off',
        "call `"$vcvarsPath`" x64",
        "cmake --build build --target $t"
    )
    $sw.Stop()
    $ok = ($rc -eq 0)
    $secs = [math]::Round($sw.Elapsed.TotalSeconds, 1)

    $pyd = Get-ChildItem (Join-Path $build "*.pyd") -ErrorAction SilentlyContinue |
           Where-Object { $_.Name -like "$t*" } | Select-Object -First 1
    $mb = if ($pyd) { [math]::Round($pyd.Length / 1MB, 2) } else { 0 }

    $rows += [pscustomobject]@{
        target  = $t
        status  = if ($ok) { "OK" } else { "FAIL" }
        time_s  = $secs
        size_mb = $mb
    }
}

Write-Host ""
Write-Host "=== RESULT ===" -ForegroundColor Cyan
$rows | Format-Table -AutoSize | Out-String -Width 120

# --- 5) fit: t = fixed + per_field * N ; extrapolate to full SDK ---
Write-Host "=== FIT (fields -> seconds) ===" -ForegroundColor Cyan
$known = @(
    @('probe_base', 0),
    @('probe_500', 506),
    @('probe_2000', 2005),
    @('probe_5000', 5014)
)
$pts = @()
foreach ($pair in $known) {
    $r = $rows | Where-Object { $_.target -eq $pair[0] } | Select-Object -First 1
    if ($r -and $null -ne $r.time_s) { $pts += @{ n = $pair[1]; t = [double]$r.time_s } }
}
foreach ($p in $pts) { Write-Host ("  {0,6} fields -> {1,8} s" -f $p.n, $p.t) }

if ($pts.Count -ge 2) {
    $sx = 0.0; $sy = 0.0; $sxy = 0.0; $sxx = 0.0; $k = [double]$pts.Count
    foreach ($p in $pts) { $sx += $p.n; $sy += $p.t; $sxy += $p.n * $p.t; $sxx += $p.n * $p.n }
    $denom = ($k * $sxx - $sx * $sx)
    if ($denom -ne 0) {
        $slope = ($k * $sxy - $sx * $sy) / $denom
        $icept = ($sy - $slope * $sx) / $k
        Write-Host ""
        Write-Host ("  model: t = {0:N1} + {1:N5} * fields" -f $icept, $slope)
        $f1 = $icept + $slope * 61881
        $f2 = $icept + $slope * 82755
        Write-Host ("  extrapolate 61881 (dahua full) : {0:N0} s = {1:N1} min" -f $f1, ($f1 / 60))
        Write-Host ("  extrapolate 82755 (dahua+hik)  : {0:N0} s = {1:N1} min" -f $f2, ($f2 / 60))
    }
}
