@echo off
REM ===========================================================================
REM jtat.cmd -- jira-ticket-analysis launcher
REM
REM Resolves its own directory, so the tool can be unzipped anywhere and any
REM drive letter works without editing config:
REM   jtat.cmd validate
REM   jtat.cmd run --keys LH2512024-5408
REM   jtat.cmd mail-only --date 2026-09-13 --dry-run
REM
REM Equivalent to:
REM   <TOOL>\.venv\Scripts\python.exe <TOOL>\scripts\jtat.py ...
REM
REM NOTE: kept pure ASCII on purpose -- cmd.exe parses .cmd files using the
REM OEM codepage (cp936 here), so non-ASCII comments would corrupt and break
REM the script. Chinese docs live in README.md / SKILL.md instead.
REM ===========================================================================
setlocal

REM Use UTF-8 console code page so Chinese output and the check marks render
REM correctly instead of turning into mojibake.
chcp 65001 >nul 2>&1

set "TOOL=%~dp0"
set "VPY=%TOOL%.venv\Scripts\python.exe"
set "JTAT=%TOOL%scripts\jtat.py"

if not exist "%VPY%" (
    echo [jtat] venv interpreter not found: %VPY%
    echo.
    echo The distribution does not ship .venv. Build it once after unzipping:
    echo     uv venv --python 3.12 "%TOOL%.venv"
    echo     uv pip install --python "%VPY%" -r "%TOOL%requirements.txt"
    echo.
    echo See https://docs.astral.sh/uv/getting-started/installation/ if uv is missing.
    exit /b 1
)

REM Run inside the tool dir -- there is no jira\ subdir here, so nothing
REM shadows the python-jira package on import.
pushd "%TOOL%"
"%VPY%" "%JTAT%" %*
set "RC=%ERRORLEVEL%"
popd

endlocal ^& exit /b %RC%
