@echo off
chcp 65001 >nul
title 串口工具 - COM Web
setlocal
set "SKILL=%~dp0"

rem Usage:
rem   double-click   -> this window KEEPS RUNNING as the service host.
rem                     The page opens automatically by the service itself.
rem                     Close this window (or Ctrl+C) = stop the service.
rem                     (save logs in the web page BEFORE closing)
rem   this bat stop  -> kill a running monitor from another shell.
rem   double-click while a ZOMBIE holds port 8765 (port listening but the
rem   web page is dead) -> auto: save its logs (best effort, no mail)
rem   + kill zombie + restart the service. Record captures are NOT touched.
rem   Serial port / baud / connect are all operated in the web page.

where python >nul 2>nul
if errorlevel 1 (
  echo [ERROR] python not found in PATH. Install Python 3 and retry.
  pause
  exit /b 1
)

rem ---- stop mode: kill the running service then exit ----
if /i "%~1"=="stop" (
  powershell -NoProfile -Command "Get-CimInstance Win32_Process -Filter \"Name='pythonw.exe' or Name='python.exe'\" | Where-Object {$_.CommandLine -match 'serial_monitor'} | ForEach-Object {Stop-Process -Id $_.ProcessId -Force}"
  echo service stopped.
  ping -n 3 127.0.0.1 >nul
  exit /b 0
)

set "URL=http://localhost:8765/"
echo [INFO] Web UI: %URL%

rem ---- Port 8765 triage (真连测试, 不靠 netstat 表, 防鬼魂端口误判) ----
rem   refused/free -> start service below (goto :start_service)
rem   connected    -> open existing web UI (真服务在跑, no kill / no error)
python -c "import socket,sys; s=socket.socket(); s.settimeout(1); sys.exit(0 if s.connect_ex(('127.0.0.1',8765))==0 else 1)" >nul 2>&1
if errorlevel 1 goto :start_service

echo [WARN] Port 8765 is already in use.
echo [INFO] Opening existing web UI: %URL%
start "" "%URL%"
echo [NOTE] If the page does not load, close the old monitor window,
echo        or run this bat with "stop" argument, then start again.
echo.
echo Press any key to close this window.
pause >nul
exit /b 0

:start_service
echo Starting serial log monitor...
echo [INFO] Web UI: %URL%
echo Keep this window OPEN while using the web page.
echo Close this window to stop the service.
echo.

python -u "%SKILL%scripts\web\serial_monitor.py" --confirm
set "RC=%ERRORLEVEL%"

echo.
if not "%RC%"=="0" echo Monitor exited with code %RC%.
echo [NOTE] Before closing, click "save log" in the web page to keep the log.
pause
endlocal
