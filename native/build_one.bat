@echo off
REM ---------------------------------------------------------------
REM 单独编译一个生成分片。调试 / 增量验证用，比全量 build 快得多。
REM
REM 用法（在项目根或 native\ 下执行都行）:
REM     native\build_one.bat dh_bind_part057.cpp.obj
REM     native\build_one.bat dh_bind_enums003.cpp.obj
REM
REM 想直接跑完整个模块（编译 + 链接），在项目根执行:
REM     powershell -ExecutionPolicy Bypass -File native\build.ps1 -SkipTest -Jobs 8
REM ---------------------------------------------------------------
if "%~1"=="" (
    echo 用法: %~nx0 ^<obj名^>
    echo   例: %~nx0 dh_bind_part057.cpp.obj
    exit /b 1
)

call "C:\Program Files\Microsoft Visual Studio\18\Community\VC\Auxiliary\Build\vcvarsall.bat" x64 >nul
set PATH=%~dp0..\.venv\Scripts;%PATH%

ninja -C "%~dp0build" "CMakeFiles/unify_dh_gen.dir/src/gen/%~1"
