@echo off
rem  Delete every __pycache__ directory in this project.
rem  Usage: clean_pycache.bat [project|preview|all]
rem    project (default) delete project code only
rem    preview           list only, delete nothing
rem    all               also descend into .venv
rem  Skipped on purpose:
rem    vendor\  vendor SDK packages are read-only input; some ship Python
rem             demos (with Chinese dir names) whose __pycache__ is part of
rem             the original package. Do not touch.
rem    .venv\   deleting package caches only makes first import slower.
rem  Kept ASCII-only on purpose: paths are discovered at runtime, so the
rem  console code page handles non-ASCII directory names by itself.
setlocal enabledelayedexpansion
cd /d "%~dp0"
set "MODE=%~1"
if not defined MODE set "MODE=project"
if /i not "%MODE%"=="project" if /i not "%MODE%"=="preview" if /i not "%MODE%"=="all" (
    echo Usage: clean_pycache.bat [project^|preview^|all]
    exit /b 2
)
set "COUNT=0"
set "SKIPPED=0"
for /f "delims=" %%D in ('dir /s /b /ad __pycache__ 2^>nul') do (
    set "P=%%D"
    set "SKIP="
    set "T=!P:vendor\=!"
    if not "!T!"=="!P!" set "SKIP=vendor"
    if /i not "!MODE!"=="all" (
        set "T=!P:.venv\=!"
        if not "!T!"=="!P!" set "SKIP=venv"
    )
    if defined SKIP (
        set /a SKIPPED+=1
    ) else (
        if /i "!MODE!"=="preview" (
            echo   would remove  !P!
        ) else (
            rd /s /q "!P!" 2>nul
            if exist "!P!" (echo   FAILED  !P!) else (echo   removed  !P!
            )
        )
        set /a COUNT+=1
    )
)
echo.
if /i "%MODE%"=="preview" (
    echo [preview] would remove %COUNT% dirs, skipped %SKIPPED%
) else (
    echo Done. removed %COUNT% dirs, skipped %SKIPPED%
)
endlocal
