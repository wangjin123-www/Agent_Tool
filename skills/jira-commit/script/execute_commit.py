#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
execute_commit.py - 【已禁用】git commit + rebase + push（按需求改为手动操作）

execute 流程现在改为：
    python script/generate_report.py
      → 合并 commit 写入 commit_preview.md
      → 生成 commit_report.html（git 操作 / JIRA 链接 / GitLab MR / tag）
      → 触发 notify.ps1 系统弹窗 + 声音

commit / rebase / push 不再自动执行，由用户按 commit_report.html 手动完成。
本文件保留仅为兼容旧调用入口，直接转发到 generate_report.main()；
原逻辑整体注释保留在文件底部，不再执行。
"""
import os
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE, 'script'))
from generate_report import main  # noqa: E402

if __name__ == '__main__':
    sys.exit(main())


# =============================================================================
# 【已禁用】以下为旧的 git commit + stash 备份 + rebase + push 逻辑（整体注释保留）
# =============================================================================
'''
import io
import json
import shlex
import subprocess
import time
import tempfile
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import jira_paths

# 修复 Windows 控制台编码问题
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')


def run_cmd(cmd, check=True, capture=True):
    """执行 shell 命令"""
    try:
        if capture:
            result = subprocess.run(
                cmd,
                shell=True,
                capture_output=True,
                text=True,
                check=check
            )
            return result.stdout.strip(), result.returncode
        else:
            result = subprocess.run(cmd, shell=True, check=check)
            return "", result.returncode
    except subprocess.CalledProcessError as e:
        if capture:
            return e.stdout.strip(), e.returncode
        raise


def git_cmd(repo_root, args):
    root = shlex.quote(repo_root)
    return f"git -C {root} {args}"


def has_uncommitted_changes(repo_root):
    """检查是否有未提交的修改"""
    stdout, _ = run_cmd(git_cmd(repo_root, "status --porcelain"))
    return len(stdout.strip()) > 0


def get_current_branch(repo_root):
    """获取当前分支名"""
    stdout, _ = run_cmd(git_cmd(repo_root, "branch --show-current"))
    return stdout.strip()


def get_current_commit(repo_root):
    """获取当前 commit hash"""
    stdout, _ = run_cmd(git_cmd(repo_root, "rev-parse HEAD"))
    return stdout.strip()


def print_section(title):
    """打印分隔线"""
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")


def _load_tasks_data(tasks_file):
    with open(tasks_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if isinstance(data, dict):
        tasks = data.get('tasks', [])
        return data, tasks

    if isinstance(data, list):
        # 兼容旧格式
        return {'tasks': data}, data

    raise ValueError("tasks.json 格式错误: 顶层必须是对象或数组")


def _save_tasks_data(tasks_file, data):
    with open(tasks_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def _contains_mojibake(text):
    # 常见 GBK/UTF-8 误解码后出现的乱码字符特征
    suspicious = "üÐ¶ÄÜÌáÉý·½±ã¶ÔÏÖÓëÊԷ¶Χ¼ì²Èë¿ÚÃüÁîÑé֤"
    return any(ch in text for ch in suspicious)


def _validate_commit_message(msg_body):
    msg = (msg_body or "").strip()
    if not msg:
        return False, "commit_message 为空"

    lines = msg.splitlines()
    if not lines or not lines[0].strip():
        return False, "commit_message 标题为空"

    if "[JIRA-ID]" in msg:
        return False, "commit_message 仍包含占位符 [JIRA-ID]"

    if _contains_mojibake(msg):
        return False, "commit_message 疑似乱码（mojibake）"

    required_blocks = ["[what]", "[影响等级]", "[建议测试范围]"]
    for block in required_blocks:
        if block not in msg:
            return False, f"commit_message 缺少必要区块: {block}"

    return True, "OK"


def _read_commit_body(repo_root, commit_hash):
    cmd = git_cmd(repo_root, f"show -s --format=%B {commit_hash}")
    result = subprocess.run(cmd, shell=True, capture_output=True)
    if result.returncode != 0:
        return None
    return result.stdout.decode('utf-8', errors='replace').rstrip()


def old_main():
    print_section("开始执行 jira-commit")

    repo_root, code = run_cmd("git rev-parse --show-toplevel", check=False)
    if code != 0 or not repo_root:
        print("\n❌ 无法定位仓库根目录")
        return 1
    repo_root = repo_root.strip()

    # 检查是否有未提交的修改
    if not has_uncommitted_changes(repo_root):
        print("\n❌ 没有未提交的修改，无需执行")
        return 1

    # 获取任务列表
    tasks_file = Path(jira_paths.get_output_dir()) / "tasks.json"
    if not tasks_file.exists():
        print(f"\n❌ 任务文件不存在: {tasks_file}")
        print("请先执行: /jira-commit analyze")
        return 1

    try:
        tasks_data, tasks = _load_tasks_data(tasks_file)
    except Exception as e:
        print(f"\n❌ 读取任务文件失败: {e}")
        return 1

    # 显示待执行的任务
    pending_tasks = [t for t in tasks if isinstance(t, dict) and not t.get('completed', False)]
    if not pending_tasks:
        print("\n✅ 所有任务已完成")
        return 0

    print(f"\n📋 待执行任务: {len(pending_tasks)} 个")
    for i, task in enumerate(pending_tasks, 1):
        commit_msg = task.get('commit_message', '')
        if isinstance(commit_msg, dict):
            title = commit_msg.get('title', task.get('summary', '无标题'))
        else:
            first_line = str(commit_msg).splitlines()[0] if str(commit_msg).strip() else ''
            title = first_line or task.get('title', task.get('title_cn', '无标题'))
        print(f"  {i}. {title[:60]}")

    # ========== 步骤 1: git commit ==========
    print_section("步骤 1/4: 创建 commit")

    commits_created = []
    for task in pending_tasks:
        pattern = task.get('git_add_pattern', '.')
        commit_msg = task.get('commit_message', '')
        title = task.get('title', task.get('title_cn', ''))

        if isinstance(commit_msg, dict):
            # 新格式：dict 结构
            title = commit_msg.get('title', task.get('summary', ''))
            what = commit_msg.get('what', '')
            why = commit_msg.get('why', '')
            how = commit_msg.get('how', '')
            impact = commit_msg.get('impact', '')
            test = commit_msg.get('test', '')

            msg_body = f"{title}\n\n"
            if what:
                msg_body += f"[what]\n{what}\n\n"
            if why:
                msg_body += f"[why]\n{why}\n\n"
            if how:
                msg_body += f"[how]\n{how}\n\n"
            if impact:
                msg_body += f"[impact]{impact}\n\n"
            if test:
                msg_body += f"[建议测试范围]\n{test}"
        else:
            # 旧格式：直接字符串
            msg_body = str(commit_msg)
            if msg_body.strip():
                title = msg_body.splitlines()[0]

        ok, reason = _validate_commit_message(msg_body)
        if not ok:
            print(f"  ❌ commit_message 校验失败: {reason}")
            print(f"  任务标题: {title}")
            return 1

        # git add
        print(f"\n  添加文件: {pattern}")
        stdout, code = run_cmd(git_cmd(repo_root, f"add {pattern}"), check=False)
        if code != 0:
            print(f"  ⚠️  git add 失败，跳过此任务")
            continue

        # git commit
        print(f"  提交: {title[:50]}...")
        msg_file = None
        try:
            with tempfile.NamedTemporaryFile('w', encoding='utf-8', delete=False, newline='\n') as f:
                f.write(msg_body.rstrip() + "\n")
                msg_file = f.name

            commit_args = f"-c i18n.commitEncoding=utf-8 commit -F {shlex.quote(msg_file)}"
            stdout, code = run_cmd(git_cmd(repo_root, commit_args), check=False)
        finally:
            if msg_file and os.path.exists(msg_file):
                os.remove(msg_file)

        if code != 0:
            print(f"  ❌ git commit 失败")
            return 1

        new_commit = get_current_commit(repo_root)
        actual_body = _read_commit_body(repo_root, new_commit)
        expected_body = msg_body.rstrip()
        if actual_body is None or actual_body != expected_body:
            print("  ❌ 提交后正文校验失败，已阻断后续流程")
            print(f"  commit={new_commit}")
            return 1

        commits_created.append(new_commit)
        print(f"  ✅ Commit: {new_commit[:8]}")

    if not commits_created:
        print("\n❌ 没有创建任何 commit")
        return 1

    # ========== 步骤 2: 创建备份 stash ==========
    print_section("步骤 2/4: 创建备份 stash")

    stash_name = f"JIRA_BACKUP_{int(time.time())}"
    stash_msg = f"[{stash_name}] 执行 rebase 前的备份"

    print(f"\n  创建 stash: {stash_name}")
    run_cmd(git_cmd(repo_root, f"stash push -u -m \"{stash_msg}\""))

    stash_ref = "stash@{0}"
    print(f"  ✅ 备份: {stash_ref}")

    # 记录 commit 后的状态（用于失败时恢复）
    safe_commit = commits_created[-1]

    # ========== 步骤 3: rebase ==========
    print_section("步骤 3/4: 执行 rebase")

    try:
        print("\n  fetching origin/main...")
        stdout, code = run_cmd(git_cmd(repo_root, "fetch origin main"), check=False)
        if code != 0:
            print(f"  ⚠️  fetch 失败，继续尝试 rebase")

        print("  rebasing onto origin/main...")
        stdout, code = run_cmd(git_cmd(repo_root, "rebase origin/main"), check=False)

        if code != 0:
            print(f"\n  ❌ rebase 失败")
            print(f"\n  尝试中止 rebase...")

            # 尝试中止 rebase
            run_cmd(git_cmd(repo_root, "rebase --abort"), check=False)

            # 恢复到安全状态
            print(f"\n  正在恢复到 commit {safe_commit[:8]}...")
            run_cmd(git_cmd(repo_root, f"reset --hard {safe_commit}"))

            print(f"  正在应用备份 stash...")
            run_cmd(git_cmd(repo_root, f"stash pop {stash_ref}"))

            print_section("执行失败")
            print(f"\n✅ 已恢复到安全状态:")
            print(f"   Commit: {safe_commit[:8]}")
            print(f"   工作区: 已恢复备份 stash 的内容")
            print(f"\n💡 提示:")
            print(f"   1. 检查冲突内容")
            print(f"   2. 手动解决冲突")
            print(f"   3. 重新执行: /jira-commit execute")
            return 1

        print("  ✅ Rebase 成功")

    except Exception as e:
        print(f"\n  ❌ 执行出错: {e}")
        print(f"  正在恢复...")

        # 恢复到安全状态
        run_cmd(git_cmd(repo_root, f"reset --hard {safe_commit}"))
        run_cmd(git_cmd(repo_root, f"stash pop {stash_ref}"))

        print_section("执行失败")
        print(f"\n✅ 已恢复到安全状态: {safe_commit[:8]}")
        return 1

    # ========== 步骤 4: push ==========
    print_section("步骤 4/4: 执行 push")

    current_branch = get_current_branch(repo_root)
    print(f"\n  推送分支: {current_branch}")

    stdout, code = run_cmd(git_cmd(repo_root, f"push -u origin {current_branch}"), check=False)

    if code != 0:
        print(f"\n  ❌ push 失败")
        print(f"\n  ⚠️  rebase 已完成，但 push 失败")
        print(f"\n  💡 可能的原因:")
        print(f"     - 网络问题")
        print(f"     - 权限不足")
        print(f"     - 远程有新的提交")

        print(f"\n  📌 备份 stash 仍保留: {stash_ref}")
        print(f"\n  解决问题后，可以手动 push:")
        print(f"     git push")

        return 1

    print("  ✅ Push 成功")

    # ========== 标记任务完成 ==========
    tasks_data, tasks = _load_tasks_data(tasks_file)
    for task in tasks:
        if not task.get('completed', False):
            task['completed'] = True
    tasks_data['tasks'] = tasks
    _save_tasks_data(tasks_file, tasks_data)

    # ========== 成功完成 ==========
    print_section("执行成功")

    print(f"\n✅ 所有操作完成!")
    print(f"\n📌 备份 stash 仍保留: {stash_ref}")
    print(f"\n请确认一切正常后，手动删除备份:")
    print(f"   git stash drop {stash_ref}")
    print(f"\n或保留备份以防万一。")

    return 0
'''
