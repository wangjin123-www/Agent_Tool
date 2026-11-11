#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
创建JIRA任务并更新tasks.json中的jira_key
completed标记在git push成功后由execute流程添加
"""

import json
import sys
import os
import re
from datetime import datetime, timedelta

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SCRIPT_DIR)
sys.path.insert(0, BASE_DIR)
from utils import jira_paths
CONFIG_FILE = jira_paths.get_config_file()
TASKS_FILE = os.path.join(jira_paths.get_output_dir(), 'tasks.json')


def load_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_json(data, filepath):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def resolve_placeholders(obj, auth_username):
    if isinstance(obj, dict):
        return {k: resolve_placeholders(v, auth_username) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [resolve_placeholders(item, auth_username) for item in obj]
    elif isinstance(obj, str) and obj == "@auth.username":
        return auth_username
    return obj


def calc_due_date(difficulty, config):
    if difficulty == 'D':
        return datetime.now().strftime('%Y-%m-%d')
    days = config['due_dates'].get(difficulty, {}).get('days', 1)
    due_date = datetime.now() + timedelta(days=days)
    return due_date.strftime('%Y-%m-%d')


def _update_commit_message_jira_key(task, jira_key):
    """更新 commit_message 中的 JIRA ID"""
    commit_msg = task.get('commit_message', '')
    updated = re.sub(r'^(\[[^\]]+\])\[(?:|JIRA-ID)\]', f'\\1[{jira_key}]', commit_msg, count=1, flags=re.MULTILINE)
    task['commit_message'] = updated


def _has_valid_jira_key(jira_key, project):
    """检查是否已有有效的JIRA key (PROJECT-数字格式)"""
    if not jira_key:
        return False
    pattern = f'^{re.escape(project)}-\\d+$'
    return re.match(pattern, jira_key) is not None


def search_jira_issue(title_cn, config):
    """查询JIRA上是否已存在相同标题的任务"""
    import urllib.request
    import urllib.parse
    import ssl

    jira_url = config['jira_url']
    project = config['jira_project']
    auth = (config['auth']['username'], config['auth']['password'])

    jql = f'project={project} and summary="{title_cn}"'
    jql_encoded = urllib.parse.quote(jql, safe='')
    api_url = f"{jira_url}/rest/api/2/search?jql={jql_encoded}"

    try:
        auth_str = f"{auth[0]}:{auth[1]}"
        b64_auth = __import__('base64').b64encode(auth_str.encode()).decode()
        ssl_context = ssl._create_unverified_context()
        req = urllib.request.Request(
            api_url,
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Basic {b64_auth}',
                'User-Agent': 'JIRA-Commit-Script/1.0'
            }
        )
        with urllib.request.urlopen(req, context=ssl_context) as response:
            response_data = json.loads(response.read().decode('utf-8'))
            issues = response_data.get('issues', [])
            if issues:
                return issues[0]['key']
            return None
    except Exception as e:
        print(f"[WARN] JIRA查询失败: {e}", file=sys.stderr)
        return None


def _build_description_block(task):
    """构造 JIRA 描述内容（创建与追加共用）"""
    title = task['title_cn']
    commit_message = task.get('commit_message', '')
    what_match = re.search(r'\[what\](.*?)(?:\[why\]|\[how\]|\[影响等级\]|\[建议测试范围\]|$)', commit_message, re.DOTALL)
    what_content = what_match.group(1).strip() if what_match else title
    return f"{title}\n\n[what]\n{what_content}"


def append_jira_description(jira_key, config, append_text):
    """把本地任务内容追加到已有 JIRA 的描述后面。

    返回 'OK'(已追加) / 'SKIP'(描述已含同样内容，幂等跳过) / 'FAIL'(失败，不中断流程)
    """
    import urllib.request
    import ssl

    jira_url = config['jira_url']
    auth = (config['auth']['username'], config['auth']['password'])
    auth_str = f"{auth[0]}:{auth[1]}"
    b64_auth = __import__('base64').b64encode(auth_str.encode()).decode()
    ssl_context = ssl._create_unverified_context()
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Basic {b64_auth}',
        'User-Agent': 'JIRA-Commit-Script/1.0'
    }

    try:
        # 1. 取当前描述
        api_url = f"{jira_url}/rest/api/2/issue/{jira_key}?fields=description"
        req = urllib.request.Request(api_url, headers=headers)
        with urllib.request.urlopen(req, context=ssl_context) as response:
            fields = json.loads(response.read().decode('utf-8')).get('fields', {})
        current = fields.get('description') or ''

        # 2. 幂等：描述已含同样内容则不重复追加
        text = append_text.strip()
        if text and text in current:
            return 'SKIP'

        # 3. 追加后 PUT 回写
        new_desc = (current.rstrip() + '\n\n' + text) if current.strip() else text
        put_url = f"{jira_url}/rest/api/2/issue/{jira_key}"
        req = urllib.request.Request(
            put_url,
            data=json.dumps({'fields': {'description': new_desc}}).encode('utf-8'),
            headers=headers,
            method='PUT')
        with urllib.request.urlopen(req, context=ssl_context) as response:
            response.read()
        return 'OK'
    except Exception as e:
        print(f"[WARN] JIRA描述追加失败({jira_key}): {e}", file=sys.stderr)
        return 'FAIL'


def create_jira_issue(task, config):
    import urllib.request
    import ssl

    jira_url = config['jira_url']
    api_url = f"{jira_url}/rest/api/2/issue"
    auth = (config['auth']['username'], config['auth']['password'])

    title = task['title_cn']
    difficulty = task['difficulty']
    due_date = calc_due_date(difficulty, config)
    description = _build_description_block(task)

    fields = {
        "project": {"key": config['jira_project']},
        "summary": title,
        "description": description,
        "issuetype": config['field_mappings']['issuetype'],
        "assignee": config['field_mappings']['assignee'],
        "customfield_10447": config['field_mappings']['customfield_10447'],
        "customfield_10310": config['field_mappings']['customfield_10310'],
        "customfield_11110": {"value": difficulty},
        "duedate": due_date
    }

    # 审核人(customfield_14804, 单用户字段): config 未配置则不上送
    if config['field_mappings'].get('customfield_14804'):
        fields['customfield_14804'] = config['field_mappings']['customfield_14804']

    # 标签：词表见 template/labels.md，由 analyze 阶段选定后写进 tasks.json
    if task.get('labels'):
        fields['labels'] = task['labels']

    payload = {"fields": fields}

    try:
        auth_str = f"{auth[0]}:{auth[1]}"
        b64_auth = __import__('base64').b64encode(auth_str.encode()).decode()
        ssl_context = ssl._create_unverified_context()
        req = urllib.request.Request(
            api_url,
            data=json.dumps(payload).encode('utf-8'),
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Basic {b64_auth}',
                'User-Agent': 'JIRA-Commit-Script/1.0'
            }
        )
        with urllib.request.urlopen(req, context=ssl_context) as response:
            response_data = json.loads(response.read().decode('utf-8'))
            return response_data.get('key')
    except Exception as e:
        print(f"[ERROR] 创建JIRA失败: {e}", file=sys.stderr)
        return None


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--validate-only', action='store_true', help='只验证jira_key，不创建')
    args = parser.parse_args()

    if args.validate_only:
        print("=== 验证JIRA Key ===")
        validate_only_mode()
    else:
        print("=== 创建JIRA任务 ===")
        create_mode()


def validate_only_mode():
    """手动模式：验证jira_key格式（不标记completed）"""
    tasks_data = load_json(TASKS_FILE)
    tasks = tasks_data['tasks']

    # 从已有任务中获取project
    project = None
    for task in tasks:
        key = task.get('jira_key', '')
        if key and '-' in key:
            project = key.split('-')[0]
            break

    if not project:
        print("[ERROR] 无法确定JIRA项目")
        project = "AERDM"

    print(f"项目: {project}")
    print(f"任务数: {len(tasks)}")
    print()

    valid_count = 0

    for task in tasks:
        task_id = task['id']
        title_cn = task['title_cn']
        current_key = task.get('jira_key', '')

        print(f"[{task_id}] {title_cn}")

        if _has_valid_jira_key(current_key, project):
            print(f"  [OK] JIRA有效: {current_key}")
            valid_count += 1
        else:
            print(f"  [SKIP] JIRA无效/空: {current_key or '(空)'}")

    # 不标记completed，execute时再根据git操作结果标记
    print()
    print(f"=== 完成 ===")
    print(f"有效任务: {valid_count}, 无效/空: {len(tasks) - valid_count}")
    print(f"注意: validate-only模式不标记completed，execute时将执行git操作")


def create_mode():
    """自动模式：创建JIRA任务，更新jira_key（不标记completed）

    规范门禁（execute 全流程统一硬门禁）：与 generate_report 共用同一道校验，
    norm_analysis.json 缺失/损坏/建议未全部人工确认 → 直接退出，
    一条 JIRA 都不创建，整个 execute 就此中止。
    """
    from generate_report import load_norm_analysis
    norm = load_norm_analysis(jira_paths.get_output_dir())
    n = len(norm['suggestions'])
    print(f"[OK] 规范分析门禁通过：{n} 条建议均已人工确认"
          + ("（无违规 ✓）" if not n else ""))

    config = load_json(CONFIG_FILE)
    config = resolve_placeholders(config, config['auth']['username'])
    tasks_data = load_json(TASKS_FILE)
    tasks = tasks_data['tasks']

    project = config['jira_project']


    print(f"项目: {project}")
    print(f"任务数: {len(tasks)}")
    print()

    for task in tasks:
        task_id = task['id']
        title_cn = task['title_cn']
        current_key = task.get('jira_key', '')
        is_completed = task.get('completed', False)

        print(f"[{task_id}] {title_cn}")

        # 已完成的任务跳过
        if is_completed:
            print(f"  [SKIP] 任务已完成")
            continue

        # 检查是否已有有效 JIRA key：跳过创建，但把本地任务内容追加到该 JIRA 描述后面
        if _has_valid_jira_key(current_key, project):
            _update_commit_message_jira_key(task, current_key)
            ret = append_jira_description(current_key, config, _build_description_block(task))
            if ret == 'OK':
                print(f"  [SKIP] 已有有效JIRA: {current_key}（描述已追加本地内容）")
            elif ret == 'SKIP':
                print(f"  [SKIP] 已有有效JIRA: {current_key}（描述已含内容，跳过追加）")
            else:
                print(f"  [SKIP] 已有有效JIRA: {current_key}（描述追加失败，不中断）")
            continue

        # key 为空或无效，需要创建/查找
        existing_key = search_jira_issue(title_cn, config)
        if existing_key:
            task['jira_key'] = existing_key
            _update_commit_message_jira_key(task, existing_key)
            print(f"  [OK] 找到已存在JIRA: {existing_key}")
        else:
            new_key = create_jira_issue(task, config)
            if new_key:
                task['jira_key'] = new_key
                _update_commit_message_jira_key(task, new_key)
                print(f"  [OK] 创建成功: {new_key}")
            else:
                print(f"  [ERROR] 创建失败")
                sys.exit(1)

    # 更新 tasks.json
    save_json(tasks_data, TASKS_FILE)

    print()
    print("=== 完成 ===")
    print(f"已更新: {TASKS_FILE}")
    print()
    print("JIRA编号:")
    for task in tasks_data['tasks']:
        status = "[OK]" if task.get('jira_key') else "[TODO]"
        print(f"  任务{task['id']}: {status} {task.get('jira_key', '(待创建)')} - {task['title_cn']}")


if __name__ == '__main__':
    main()
