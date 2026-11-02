@echo off
chcp 65001 >nul
title Serial Log Monitor - COM Web
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

rem ---- Port 8765 triage ----
rem   free               -> start service below (goto :start_service)
rem   listening + alive  -> healthy: open browser, exit (no restart)
rem   listening + dead   -> zombie: save logs (best effort) -> kill -> restart
netstat -ano | findstr /C:":8765" | findstr /C:"LISTENING" >nul 2>&1
if errorlevel 1 goto :start_service

rem Something holds 8765 - health check (2s timeout, IPv4 loopback)
powershell -NoProfile -Command "try{Invoke-WebRequest -Uri 'http://127.0.0.1:8765/' -UseBasicParsing -TimeoutSec 2|Out-Null;exit 0}catch{exit 1}" >nul 2>&1
if errorlevel 1 goto :zombie_rescue

rem ---- healthy: service already running, just open the browser ----
start "" "%URL%"
echo Service already running (healthy) - browser opened. This window will close.
ping -n 3 127.0.0.1 >nul
exit /b 0

:zombie_rescue
echo [WARN] Port 8765 is held by an unresponsive service - zombie detected.
echo [INFO] Saving its in-memory logs (best effort, default path, no mail)...
rem POST /dump with EMPTY body = default path + mail=false (no popup questions)
powershell -NoProfile -Command "try{Invoke-WebRequest -Uri 'http://127.0.0.1:8765/dump' -Method POST -UseBasicParsing -TimeoutSec 8|Out-Null;exit 0}catch{exit 1}" >nul 2>&1
if errorlevel 1 (
  echo [WARN] Dump failed - process hung, unsaved in-memory logs are LOST.
) else (
  echo [INFO] Logs saved via /dump into output\logs\.
)
echo [INFO] Killing zombie serial_monitor processes...
powershell -NoProfile -Command "Get-CimInstance Win32_Process -Filter \"Name='pythonw.exe' or Name='python.exe'\" | Where-Object {$_.CommandLine -match 'serial_monitor'} | ForEach-Object {Stop-Process -Id $_.ProcessId -Force}"
ping -n 3 127.0.0.1 >nul
netstat -ano | findstr /C:":8765" | findstr /C:"LISTENING" >nul 2>&1
if not errorlevel 1 (
  echo [ERROR] Port 8765 is still held by a process that is NOT serial_monitor.
  echo         Locate it and kill it yourself:   netstat -ano ^| findstr :8765
  pause
  exit /b 1
)
echo [INFO] Port released. Starting a fresh service...

:start_service
echo Starting serial log monitor...
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
