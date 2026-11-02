#!/usr/bin/env python3
"""显示 tasks.json 详情"""
import io
import json
import os
import sys

# 修复 Windows 控制台 GBK 编码无法输出 emoji 的问题（与 execute_commit.py 同方案）
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import jira_paths

TASKS_FILE = os.path.join(jira_paths.get_output_dir(), "tasks.json")

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        print(f"❌ tasks.json 不存在，请先运行 analyze")
        return None
    with open(TASKS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def format_tasks(data):
    if "tasks" not in data:
        print("❌ tasks.json 格式错误")
        return

    tasks = data["tasks"]
    total = len(tasks)
    metadata = data.get("_metadata", {})

    print(f"\n📋 任务列表 ({total} 个任务)")
    print(f"生成时间: {metadata.get('generated_at', 'N/A')}")
    print("=" * 60)

    for task in tasks:
        print(f"\n任务 {task['id']}: {task.get('title_cn', task['title'])}")
        print(f"  类型: {task['type']} | 难度: {task['difficulty']}")
        print(f"  JIRA: {task.get('jira_key', '(待分配)')}")
        if task.get('labels'):
            print(f"  标签: {', '.join(task['labels'])}")
        print(f"  目录: {', '.join(task['dirs'])}")

        commit_msg = task['commit_message']
        lines = commit_msg.split('\n')
        print(f"  提交信息预览:")
        print(f"    标题: {lines[0]}")

        # 提取 [what] 部分
        if "[what]" in commit_msg:
            what_start = commit_msg.index("[what]") + 6
            what_end = commit_msg.find("\n\n[", what_start)
            if what_end == -1:
                what_end = commit_msg.find("\n\n", what_start)
            what = commit_msg[what_start:what_end].strip()[:100]
            print(f"    内容: {what}...")

    print("\n" + "=" * 60)

    # 统计
    summary = metadata.get("summary", {})
    if summary:
        print(f"\n统计: {', '.join([f'{k}:{v}' for k,v in summary.items()])}")

if __name__ == "__main__":
    data = load_tasks()
    if data:
        format_tasks(data)
