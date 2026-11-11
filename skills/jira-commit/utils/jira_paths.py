#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
jira-commit 路径解析工具

输出目录解析优先级：
  1. 环境变量 JIRA_COMMIT_OUTPUT_DIR —— 由 SKILL.md 在 git 仓库内运行时设为
     <项目根>/.jira-commit/output（项目本地输出，用户要求）
  2. 回退到 skill 自带目录 <skill>/output（仓库外 / 未设置环境变量时）

项目根解析优先级：
  1. 环境变量 JIRA_COMMIT_PROJECT_ROOT（SKILL.md 显式设置）
  2. 从 JIRA_COMMIT_OUTPUT_DIR 反推：<项目根>/.jira-commit/output → <项目根>
  3. 空（调用方回退到当前工作目录，并应给出告警）
"""

import os


def get_skill_dir():
    """skill 根目录（utils 的上一级）"""
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_output_dir():
    """解析输出目录：优先环境变量，回退 skill 自带 output"""
    env = os.environ.get('JIRA_COMMIT_OUTPUT_DIR')
    if env:
        return env
    return os.path.join(get_skill_dir(), 'output')


def get_project_root():
    """业务工程根（不是 .claude 技能仓库）。

    报告脚本里的 git remote/branch 必须在这个根下执行；否则从 skill 目录
    运行时会被 .claude 自带的 .git 劫持（曾出现 MR 链接指向 Agent_Tool/main）。
    """
    env = os.environ.get('JIRA_COMMIT_PROJECT_ROOT')
    if env:
        return os.path.abspath(env)
    out = os.environ.get('JIRA_COMMIT_OUTPUT_DIR')
    if out:
        out_abs = os.path.abspath(out)
        parent = os.path.dirname(out_abs)          # .../.jira-commit
        if os.path.basename(parent) == '.jira-commit':
            return os.path.dirname(parent)         # <项目根>
    return ''


def get_config_file():
    """config 文件路径（含敏感认证信息，不入库）"""
    return os.path.join(get_skill_dir(), 'config', 'jira_commit_config.json')
