@echo off
rem ============================================================
rem daily.cmd - daily full-auto ticket analysis
rem   1) jtat run          : fetch tickets + prep (skip unchanged)
rem   2) claude -p         : headless AI analysis -> analysis.md
rem   3) jtat feedback     : write back as a SUBTASK (comment + labels); parent untouched
rem   4) jtat summary/mail : SUMMARY.md + email
rem
rem register (run once in your own terminal, adjust /ST time):
rem   schtasks /Create /TN jta-daily /TR "D:\wnagjin\Compay_Project\CDC_7255\cdc_7255\.claude\skills\jira-ticket-analysis\daily.cmd" /SC WEEKLY /D MON,TUE,WED,THU,FRI /ST 08:30 /F
rem
rem manual test:
rem   daily.cmd          (run it now, check log after)
rem unregister:
rem   schtasks /Delete /TN jta-daily /F
rem ============================================================
setlocal
set "TOOL=%~dp0"
cd /d "%TOOL%"

for /f %%i in ('powershell -NoProfile -Command "Get-Date -Format yyyy-MM-dd"') do set "TODAY=%%i"
set "WS=C:\Users\Lenovo\jta_workspace"
set "LOG=%WS%\daily-%TODAY%.log"

echo ===== daily start %TODAY% %time% ===== > "%LOG%"

echo [1/4] fetch + prepare ... >> "%LOG%"
call "%TOOL%jtat.cmd" run >> "%LOG%" 2>&1

echo [2/4] headless AI analysis ... >> "%LOG%"
claude -p "Read the file %TOOL%prompts\orchestrator-headless.md and execute it exactly. Parameters: DATE=%TODAY% WORKSPACE=%WS%\out\%TODAY%. Read that file first, then do what it says. Do not ask questions." --dangerously-skip-permissions >> "%LOG%" 2>&1

echo [3/4] feedback to Jira ... >> "%LOG%"
call "%TOOL%jtat.cmd" feedback --apply --date %TODAY% >> "%LOG%" 2>&1

echo [4/4] summary + mail ... >> "%LOG%"
call "%TOOL%jtat.cmd" summary --date %TODAY% >> "%LOG%" 2>&1
call "%TOOL%jtat.cmd" mail-only --date %TODAY% >> "%LOG%" 2>&1

echo ===== daily end %time% ===== >> "%LOG%"
endlocal
