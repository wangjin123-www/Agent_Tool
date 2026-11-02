param(
    [string]$Title = "jira-commit",
    [string]$Message = ""
)

# 最简单的系统通知：两声提示音 + 弹窗
[System.Media.SystemSounds]::Exclamation.Play()
Start-Sleep -Milliseconds 150
[System.Media.SystemSounds]::Asterisk.Play()

Add-Type -AssemblyName System.Windows.Forms
[System.Windows.Forms.MessageBox]::Show(
    $Message,
    $Title,
    [System.Windows.Forms.MessageBoxButtons]::OK,
    [System.Windows.Forms.MessageBoxIcon]::Information
)
