#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试JIRA连接
"""

import json
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SCRIPT_DIR)
CONFIG_FILE = os.path.join(BASE_DIR, 'config', 'jira_commit_config.json')


def load_json(filepath):
    """加载JSON文件"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def test_jira_connection():
    """测试JIRA连接"""
    import urllib.request
    import ssl

    # 加载配置
    config = load_json(CONFIG_FILE)

    jira_url = config['jira_url']
    project = config['jira_project']
    username = config['auth']['username']
    password = config['auth']['password']

    print("=== JIRA连接测试 ===")
    print(f"JIRA URL: {jira_url}")
    print(f"项目: {project}")
    print(f"用户名: {username}")
    print()

    # 测试1: 简单的API请求
    print("测试1: 获取服务器信息...")
    try:
        ssl_context = ssl._create_unverified_context()
        auth_str = f"{username}:{password}"
        b64_auth = __import__('base64').b64encode(auth_str.encode()).decode()

        req = urllib.request.Request(
            f"{jira_url}/rest/api/2/serverInfo",
            headers={
                'Authorization': f'Basic {b64_auth}',
                'User-Agent': 'JIRA-Connection-Test/1.0'
            }
        )

        with urllib.request.urlopen(req, context=ssl_context) as response:
            data = json.loads(response.read().decode('utf-8'))
            print(f"✓ 连接成功!")
            print(f"  服务器版本: {data.get('version', '未知')}")
            print(f"  服务器标题: {data.get('serverTitle', '未知')}")
    except Exception as e:
        print(f"✗ 失败: {type(e).__name__}: {e}")
        print()
        print("可能的原因:")
        print("1. 需要VPN连接")
        print("2. JIRA URL配置错误")
        print("3. 用户名或密码错误")
        print("4. 防火墙阻止")
        return False

    print()

    # 测试2: 查询项目
    print("测试2: 查询项目...")
    try:
        import urllib.parse

        jql = f'project={project}'
        jql_encoded = urllib.parse.quote(jql, safe='')

        req = urllib.request.Request(
            f"{jira_url}/rest/api/2/search?jql={jql_encoded}",
            headers={
                'Authorization': f'Basic {b64_auth}',
                'User-Agent': 'JIRA-Connection-Test/1.0'
            }
        )

        with urllib.request.urlopen(req, context=ssl_context) as response:
            data = json.loads(response.read().decode('utf-8'))
            print(f"✓ 项目查询成功!")
            print(f"  总任务数: {data.get('total', 0)}")
    except Exception as e:
        print(f"✗ 失败: {type(e).__name__}: {e}")
        return False

    print()
    print("=== 所有测试通过 ===")
    return True


if __name__ == '__main__':
    success = test_jira_connection()
    sys.exit(0 if success else 1)
