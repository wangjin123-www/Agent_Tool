@echo off
setlocal

rem proto-toolkit protocol console launcher
rem Usage: double-click this file, or:  start_console.bat [port]   (default 8765)
rem Prefers utils\.venv interpreter; falls back to system python.

set "SKILL_DIR=%~dp0"
set "SKILL_DIR=%SKILL_DIR:~0,-1%"
set "PORT=%~1"
if "%PORT%"=="" set "PORT=8765"

set "PY=%SKILL_DIR%\utils\.venv\Scripts\python.exe"
if not exist "%PY%" (
    echo [INFO] venv not found, using system python.
    echo [INFO] first run: powershell -ExecutionPolicy Bypass -File "%SKILL_DIR%\utils\setup_env.ps1"
    set "PY=python"
)

echo ============================================================
echo  Protocol console : http://127.0.0.1:%PORT%/
echo  Check report     : http://127.0.0.1:%PORT%/check_report.html
echo  Stop             : close this window, or Ctrl+C
echo ============================================================
echo.

"%PY%" "%SKILL_DIR%\scripts\cli.py" console --port %PORT%
set "RC=%ERRORLEVEL%"

echo.
if not "%RC%"=="0" echo [FAIL] exit code %RC% ^(lark-cli auth, port in use, or missing deps^)
pause
endlocal
exit /b %RC%
