@echo off
setlocal
chcp 65001 >nul
rem ============================================================
rem  embedded-build-debug / S32DS backend (CDC_7255)
rem  [1] compile check only (-c, no link)
rem  [2] full build (.elf / .map / .hex / .bin)
rem ============================================================
set "SCRIPT=%~dp0..\scripts\s32ds_compile.py"

echo ============================================================
echo   S32DS build - CDC_7255 (Debug_FLASH)
echo   [1] compile check only
echo   [2] full build (.elf/.map/.hex/.bin)
echo ============================================================
choice /C 12 /N /M "select 1 or 2: "
if errorlevel 2 goto :full

:compile
echo --- mode 1: compile check ---
python "%SCRIPT%" check --mode compile
goto :end

:full
echo --- mode 2: full build ---
python "%SCRIPT%" check --mode full
goto :end

:end
set "RC=%ERRORLEVEL%"
echo ============================================================
if "%RC%"=="0" (echo  RESULT: SUCCESS) else (echo  RESULT: FAILED, exit code %RC%)
echo ============================================================
endlocal & exit /b %RC%
