# proto-toolkit 运行环境自举（Windows PowerShell）
# 用法: powershell -ExecutionPolicy Bypass -File utils\setup_env.ps1
# 作用: 在 utils\.venv 建独立虚拟环境并安装 requirements.txt；之后所有脚本用该解释器跑。

$ErrorActionPreference = "Stop"
$Here = Split-Path -Parent $MyInvocation.MyCommand.Path
$Venv = Join-Path $Here ".venv"
$Py   = Join-Path $Venv "Scripts\python.exe"

if (-not (Test-Path $Py)) {
    Write-Host "[1/3] 创建虚拟环境 $Venv"
    python -m venv $Venv
} else {
    Write-Host "[1/3] 复用已有虚拟环境 $Venv"
}

Write-Host "[2/3] 安装依赖"
& $Py -m pip install --upgrade pip --quiet
& $Py -m pip install -r (Join-Path $Here "requirements.txt") --quiet

Write-Host "[3/3] 自检"
& $Py -c "import jinja2,jsonschema,sys;print('python',sys.version.split()[0]);print('jinja2',jinja2.__version__);print('jsonschema',jsonschema.__version__)"

Write-Host ""
Write-Host "完成。解释器: $Py"
Write-Host "后续调用示例:"
Write-Host "  & '$Py' scripts\cli.py sync --dry-run"
