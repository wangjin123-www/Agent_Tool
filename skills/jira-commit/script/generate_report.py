#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_report.py - execute 的后半段：生成合并 commit + HTML 报告 + 飞书邮件通知

不执行任何 git commit/rebase/push（已按需求禁用，全部改为手动）。
前置：create_jira_tasks.py 已把 jira_key 写回 tasks.json 的 commit_message。

输出（均在 $JIRA_COMMIT_OUTPUT_DIR）：
  commit_preview.md   - 合并后的单次 commit 消息（整体使用，勿拆成单个）
  merge_request.md    - MR 标题 + 描述（优先 tasks.json 顶层 merge_request，缺失则规则聚合兜底）
  commit_report.html  - 人工指引报告（git 操作 / JIRA 链接 / GitLab MR / tag）
完成后调用 send_mail.py 发飞书邮件（lark-cli，收件人自动获取，抄送见 config.notification.email_cc）。

可选参数：
  --check-norm  只校验规范分析门禁（execute 建单前调用），不产出
  --no-mail     跳过飞书通知（改了 tasks.json 只想刷新 merge_request.md/HTML 时用）

合并 commit 格式约定：
  首行  [type][jira1][jira2]... N commits   （jira 缺失用 jira# 占位）
  各任务 [type][jira 或 jira#]中文标题（title_cn） + what/why/how/影响等级/建议测试范围
"""
import html as html_mod
import io
import json
import os
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import jira_paths

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')


# ---------------------------------------------------------------- 工具函数
def load_tasks_doc():
    f = Path(jira_paths.get_output_dir()) / 'tasks.json'
    if not f.exists():
        sys.exit(f"[ERROR] tasks.json 不存在: {f}\n请先执行 /jira-commit analyze")
    with open(f, encoding='utf-8') as fh:
        return json.load(fh)


def load_tasks():
    return load_tasks_doc().get('tasks', [])


def load_config():
    cfg_file = jira_paths.get_config_file()
    if not os.path.exists(cfg_file):
        return {}
    with open(cfg_file, encoding='utf-8') as fh:
        return json.load(fh)


def extract_section(msg, key):
    """提取 [key] 之后到下一个 [标记] 或结尾的内容"""
    m = re.search(r'\[' + re.escape(key) + r'\](.*?)(?=\n\[|\n\n\[|$)', msg, re.DOTALL)
    return m.group(1).strip() if m else ''


def parse_task(task):
    """解析任务：从 commit_message 拆出 type/jira/summary/what/why/how/impact/test"""
    msg = task.get('commit_message', '') or ''
    first = msg.splitlines()[0] if msg.strip() else ''
    m = re.match(r'^\[([^\]]+)\](?:\[([^\]]+)\])?\s*(.*)$', first)
    return {
        'id': task.get('id'),
        'title_cn': task.get('title_cn', task.get('title', '')),
        'type': m.group(1) if m else task.get('type', ''),
        'jira': (m.group(2) if m else '') or task.get('jira_key', ''),
        'summary': (m.group(3) if m else '').strip(),
        'what': extract_section(msg, 'what'),
        'why': extract_section(msg, 'why'),
        'how': extract_section(msg, 'how'),
        'impact': extract_section(msg, '影响等级') or task.get('impact', ''),
        'test': extract_section(msg, '建议测试范围'),
        'labels': task.get('labels') or [],
        'files': task.get('files') or [],
        'commit_message': msg,
    }


def build_combined(tasks):
    """生成合并 commit 消息。

    首行  [type][jira1][jira2]... N commits（jira 缺失用 jira# 占位）
    各任务头 [type][jira 或 jira#]中文标题 —— 任务头一律中文标题
    """
    parsed = [parse_task(t) for t in tasks]
    first_type = parsed[0]['type'] if parsed else ''
    top = (f"[{first_type}]"
           + ''.join(f"[{p['jira'] or 'jira#'}]" for p in parsed)
           + f" {len(parsed)} commits")

    blocks = []
    for p in parsed:
        header = f"[{p['type']}][{p['jira'] or 'jira#'}]{p['title_cn']}"
        lines = [header, ""]
        if p['what']:
            lines += ["[what]", p['what'], ""]
        if p['why']:
            lines += ["[why]", p['why'], ""]
        if p['how']:
            lines += ["[how]", p['how'], ""]
        lines += [f"[影响等级]{p['impact']}", "[建议测试范围]", p['test']]
        blocks.append('\n'.join(lines))

    return top + "\n\n" + "\n\n".join(blocks), parsed


IMPACT_ORDER = ('S', 'A', 'B', 'C', 'D')


def _impact_rank(val):
    """影响等级排序用：S 最高(=0)…D 最低(=4)；非法/缺失排最后"""
    v = (val or '').strip().upper()
    return IMPACT_ORDER.index(v) if v in IMPACT_ORDER else len(IMPACT_ORDER)


def _strip_num(block):
    """把一段 '1. xxx'/'2、xxx' 列表剥掉自带序号，返回纯条目文本"""
    items = []
    for line in (block or '').splitlines():
        s = line.strip()
        if not s:
            continue
        items.append(re.sub(r'^\d+[.、)]\s*', '', s))
    return items


def _real_jiras(parsed):
    """按任务顺序取真实 JIRA 号（去重）。

    execute 建单后 create_jira_tasks.py 把真号写回各任务 jira_key；MR 描述
    的「关联 JIRA」段一律以此为准。
    """
    out = []
    for p in parsed:
        if p['jira'] and p['jira'] not in out:
            out.append(p['jira'])
    return out


def _strip_jira_section(desc):
    """剥掉文本里的「## 关联 JIRA」段。

    analyze 阶段 jira_key 必为空（规范硬约束），AI 写不出真号，该段只能是占位符
    （如 AERDM-xxxxx），不能原样透传；统一由 build_merge_request 用真实 id 重写。
    """
    return re.sub(r'\n*#{1,6}[ \t]*关联[ \t]*JIRA\b[\s\S]*?(?=\n#{1,6}[ \t]|\Z)',
                  '', desc).rstrip()


def build_merge_request(doc, parsed):
    """生成 GitLab MR 的标题与描述（从本次 commit 内容浓缩）。

    优先用 analyze 产出的 tasks.json 顶层 merge_request:{title,description}（AI 浓缩）；
    缺失时按任务清单规则聚合兜底（保证 execute 一定有可复制的文案）。
    AI 文本里的「## 关联 JIRA」段不做透传：改用各任务真实 jira_key 重写（无真号则删该段）。
    返回 (title, description)。
    """
    mr = doc.get('merge_request') or {}
    title = (mr.get('title') or '').strip()
    desc = (mr.get('description') or '').strip()
    if title and desc:
        # AI 文本优先，但「关联 JIRA」段一律以真实 jira_key 为准（占位符不可透传）
        jiras = _real_jiras(parsed)
        desc = _strip_jira_section(desc)
        if jiras:
            desc += '\n\n## 关联 JIRA\n' + ' '.join(jiras)
        return title, desc
    if not parsed:
        return title, desc

    # 按影响等级排序（最高影响在前），兜底文案据此取样本
    ranked = sorted(parsed, key=lambda p: _impact_rank(p['impact']))

    # ---- 标题兜底：取影响等级最高的任务标题，去掉括号内的细节补充 ----
    if not title:
        first_type = ranked[0]['type'] or 'feature'
        subject = re.sub(r'[（(].*?[)）]', '', ranked[0]['title_cn'] or '').strip()
        title = (f"[{first_type}] {subject}" if len(parsed) == 1
                 else f"[{first_type}] {subject}")

    # ---- 描述兜底：背景/变更/影响等级/测试范围/关联 JIRA ----
    if not desc:
        # 背景：取影响等级最高的前 2 条 why，避免堆成一大段
        whys = []
        for p in ranked:
            if p['why'] and p['why'] not in whys:
                whys.append(p['why'])
            if len(whys) >= 2:
                break
        # 测试范围：各任务先剥序号再合并去重，最后统一从 1 连续编号
        tests = []
        for p in ranked:
            for item in _strip_num(p['test']):
                if item not in tests:
                    tests.append(item)
        jiras = _real_jiras(parsed)
        lines = ['## 背景']
        lines += [f"- {w}" for w in whys] if whys else ['- （详见各 JIRA 工单）']
        lines += ['', '## 变更'] + [f"- {p['title_cn']}" for p in parsed]
        lines += ['', '## 影响等级', ranked[0]['impact'] or '（未标注）', '', '## 测试范围']
        lines += [f"{i}. {t}" for i, t in enumerate(tests, 1)] if tests \
            else ['- （见各任务 [建议测试范围]）']
        if jiras:
            lines += ['', '## 关联 JIRA', ' '.join(jiras)]
        desc = '\n'.join(lines)
    return title, desc


def write_merge_request(title, desc):
    """写 merge_request.md（MR 标题 + 描述，供复制/下载）"""
    out = Path(jira_paths.get_output_dir()) / 'merge_request.md'
    out.write_text(f"# MR 标题\n{title}\n\n# MR 描述\n{desc}\n", encoding='utf-8')
    return out


def _read_git_file(*parts, root=None):
    """直接读 <root>/.git 下文件（git 子进程偶发失败时的兜底）。"""
    base = Path(root) if root else Path('.')
    p = base.joinpath('.git', *parts)
    try:
        return p.read_text(encoding='utf-8', errors='replace').strip()
    except Exception:
        return ''


def _remote_url_from_config(root=None):
    """解析 <root>/.git/config 中 [remote "origin"] 的 url"""
    text = _read_git_file('config', root=root)
    if not text:
        return ''
    in_origin = False
    for line in text.splitlines():
        s = line.strip()
        if s == '[remote "origin"]':
            in_origin = True
            continue
        if s.startswith('['):          # 进入其它 section
            in_origin = False
            continue
        if in_origin and s.startswith('url') and '=' in s:
            return s.split('=', 1)[1].strip()
    return ''


def _web_url_from_remote(out):
    """remote url（ssh 或 http 格式）→ GitLab 网页地址；无法解析返回 ''"""
    if out.startswith('git@'):
        rest = out[4:]
        if ':' in rest:
            host, path = rest.split(':', 1)
            path = path[:-4] if path.endswith('.git') else path
            return f"https://{host}/{path}"
    if out.startswith('http'):
        return out[:-4] if out.endswith('.git') else out
    return ''


def gitlab_web_url(root=None):
    """从 <root> 的 git remote origin 推导 GitLab 网页地址。

    root 必须是业务工程根；不能依赖当前 cwd——从 .claude/skills/jira-commit
    运行时，git 会命中 .claude 自己的仓库（Agent_Tool），导致 MR 链接指错项目。
    """
    out = ''
    try:
        out = subprocess.run(['git', 'remote', 'get-url', 'origin'],
                             capture_output=True, text=True, timeout=10,
                             cwd=root or None).stdout.strip()
    except Exception:
        pass
    if not out:
        out = _remote_url_from_config(root)
    return _web_url_from_remote(out)


def current_branch(root=None):
    """<root> 当前分支；git 子进程失败时读 .git/HEAD 兜底（detached HEAD 返回 ''）"""
    try:
        branch = subprocess.run(['git', 'branch', '--show-current'],
                                capture_output=True, text=True, timeout=10,
                                cwd=root or None).stdout.strip()
        if branch:
            return branch
    except Exception:
        pass
    head = _read_git_file('HEAD', root=root)
    if head.startswith('ref: refs/heads/'):
        return head[len('ref: refs/heads/'):].strip()
    return ''


# ---------------------------------------------------------------- 规范分析（analyze 产出）
def load_norm_analysis(out_dir):
    """读 analyze 阶段产出的 norm_analysis.json——execute 的**入口硬门禁**。

    三道校验，任一不过直接 ERROR 退出（HTML 都不生成）：
    1. 结构：不存在 / 空文件 / JSON 损坏 / 缺 suggestions 键 → 退出，提示重跑 analyze
    2. **人工处理完成**：每条 suggestion 的 status 必须为 checked——
       人工流程 = 按建议改代码后把该条 status 改为 checked；认为建议不对则**删除该条**
       （并用 /jira-commit norm 交互同步更新规范）。还有未确认的 → 退出；
       空 suggestions 数组合法（无违规 / 建议全部被删）。
    3. **同批时序**：analyzed_at 不得早于 tasks.json 顶层 generated_at（容差 5 分钟）——
       防"上次 analyze 的规范分析残留"被静默内嵌进本次报告（文件存在+全 checked
       骗过前两道校验的假阳性）。
    校验通过 → 返回 {'analyzed_at','base','files','suggestions'}，只读内嵌进 commit_report.html。
    """
    path = Path(out_dir) / 'norm_analysis.json'
    if not path.exists():
        sys.exit(f"[ERROR] 未找到 {path}（analyze 阶段未产出规范分析）\n"
                 f"请先重新执行 /jira-commit analyze")
    try:
        data = json.loads(path.read_text(encoding='utf-8'))
    except Exception as e:
        sys.exit(f"[ERROR] norm_analysis.json 解析失败({e})——分析产物不合法\n"
                 f"请重新执行 /jira-commit analyze")
    if not isinstance(data, dict) or not isinstance(data.get('suggestions'), list):
        sys.exit(f"[ERROR] norm_analysis.json 结构不合法（缺 suggestions 数组）\n"
                 f"请重新执行 /jira-commit analyze")

    # ---- 第 3 道：同批时序（norm 与 tasks 必须同一次 analyze 产出）----
    from datetime import datetime, timedelta
    tasks_path = Path(out_dir) / 'tasks.json'
    try:
        tasks_data = json.loads(tasks_path.read_text(encoding='utf-8'))
    except Exception as e:
        sys.exit(f"[ERROR] tasks.json 解析失败({e})——请重新执行 /jira-commit analyze")
    gen_at = str(tasks_data.get('generated_at') or '').strip()
    ana_at = str(data.get('analyzed_at') or '').strip()
    if not gen_at:
        sys.exit("[ERROR] tasks.json 缺顶层 generated_at 字段（旧版 analyze 产物）\n"
                 "请重新执行 /jira-commit analyze（新版会与 norm_analysis.json 同批生成）")
    try:
        t_gen = datetime.strptime(gen_at, '%Y-%m-%d %H:%M:%S')
        t_norm = datetime.strptime(ana_at, '%Y-%m-%d %H:%M:%S')
    except ValueError as e:
        sys.exit(f"[ERROR] 时间字段格式不合法({e})：generated_at={gen_at!r} / analyzed_at={ana_at!r}\n"
                 f"请重新执行 /jira-commit analyze")
    if t_norm < t_gen - timedelta(minutes=5):
        sys.exit("[ERROR] 规范分析是上次 analyze 的残留，与本次任务清单不同批：\n"
                 f"        tasks.json     generated_at = {gen_at}\n"
                 f"        norm_analysis  analyzed_at  = {ana_at}\n"
                 f"        请重新执行 /jira-commit analyze（diff 对照 norm_spec 重新产出规范分析）")

    sugg = []
    for s in data['suggestions']:
        if not isinstance(s, dict):
            continue
        st = s.get('status') or 'open'
        if st not in ('open', 'checked', 'deleted'):
            st = 'open'
        s['status'] = st
        sugg.append(s)
    open_ids = [str(s.get('id') or '?') for s in sugg if s['status'] != 'checked']
    if open_ids:
        sys.exit("[ERROR] 规范分析建议尚未全部确认，不能执行 execute：\n"
                 f"        未确认: {', '.join(open_ids)}\n"
                 f"        人工处理: 按建议改代码后，编辑 {path}\n"
                 f"                  把对应建议的 status 改为 \"checked\"；\n"
                 f"        认为建议不对: 从 suggestions 数组删除该条，并运行 /jira-commit norm\n"
                 f"                  交互更新规范文件（norm_spec.md / CLAUDE.md / memory）后再 execute")
    return {'analyzed_at': data.get('analyzed_at', ''),
            'base': data.get('base', ''),
            'files': data.get('files', []),
            'suggestions': sugg}


# ---------------------------------------------------------------- 输出
# 必须用 raw string：模板内 JS 含 /\r\n/g、'\n'，普通字符串会被 Python 提前转义成
# 真实换行，导致正则/字符串字面量跨行、整段 script 语法错误（页面列表渲染为空白）
HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>jira-commit 执行报告</title>
<style>
  :root { --accent:#4c6ef5; --accent-dark:#3b5bdb; --bg:#f4f6fb; --card:#ffffff;
          --text:#2b2f36; --muted:#868e96; --border:#e5e9f2; --code-bg:#f8f9fc; }
  * { box-sizing:border-box; }
  body { margin:0; background:var(--bg); color:var(--text);
         font:14px/1.75 "Segoe UI","Microsoft YaHei","PingFang SC",sans-serif; }
  .wrap { max-width:920px; margin:0 auto; padding:36px 20px 64px; }
  header h1 { margin:0 0 6px; font-size:22px; }
  header .meta { color:var(--muted); font-size:12.5px; }
  .card { background:var(--card); border:1px solid var(--border); border-radius:12px;
          padding:22px 26px; margin-bottom:18px; box-shadow:0 1px 4px rgba(35,45,80,.05); }
  .card h2 { display:flex; align-items:center; gap:10px; font-size:16px; margin:0 0 14px; }
  .num { flex:none; width:26px; height:26px; border-radius:50%; background:var(--accent);
         color:#fff; display:flex; align-items:center; justify-content:center;
         font-size:13px; font-weight:600; }
  p { margin:8px 0; }
  pre { background:var(--code-bg); border:1px solid var(--border); border-radius:8px;
        padding:14px 16px; margin:10px 0; overflow-x:auto; }
  code, textarea { font:13px/1.65 Consolas,"Courier New",monospace; }
  .btn { display:inline-block; padding:7px 16px; margin:8px 8px 0 0; border:none;
         border-radius:6px; background:var(--accent); color:#fff; font-size:13.5px;
         cursor:pointer; text-decoration:none; }
  .btn:hover { background:var(--accent-dark); }
  .btn.ghost { background:#fff; color:var(--accent); border:1px solid var(--accent); }
  .btn.ghost:hover { background:#f0f4ff; }
  textarea#commitMsg { width:100%; min-height:340px; padding:14px 16px;
                       background:var(--code-bg); border:1px solid var(--border);
                       border-radius:8px; color:var(--text); resize:vertical; }
  .hint { color:var(--muted); font-size:12.5px; }
  ul.jira { list-style:none; margin:0; padding:0; }
  ul.jira li { padding:9px 2px; border-bottom:1px dashed var(--border); }
  ul.jira li:last-child { border-bottom:none; }
  ul.jira a { color:var(--accent); font-weight:600; text-decoration:none; }
  ul.jira a:hover { text-decoration:underline; }
  ul.jira .tag { display:inline-block; margin-left:6px; padding:1px 9px; border-radius:10px;
                 background:#eef2ff; border:1px solid var(--border); color:var(--accent);
                 font-size:12px; font-weight:500; }
  a { color:var(--accent); }

  /* ---- 规范分析结果（只读展示） ---- */
  .banner { display:none; padding:11px 14px; border-radius:8px; margin:10px 0; font-size:13px; }
  .banner.err { display:block; background:#fff5f5; border:1px solid #ffc9c9; color:#c92a2a; }
  .banner.ok  { display:block; background:#ebfbee; border:1px solid #b2f2bb; color:#2b8a3e; }
  .banner.info{ display:block; background:#eef2ff; border:1px solid #d0d9ff; color:#3b5bdb; }
  .sugg { border:1px solid var(--border); border-radius:9px; padding:12px 14px; margin:10px 0;
          background:#fff; }
  .sugg.checked { background:#f3fbf5; border-color:#b2f2bb; }
  .sugg .top { display:flex; align-items:center; gap:8px; flex-wrap:wrap; }
  .sugg .rid { font:12px Consolas,monospace; color:var(--muted); }
  .sugg .ttl { font-weight:600; }
  .sugg .sev { font:11px Consolas,monospace; padding:1px 6px; border-radius:4px;
               text-transform:uppercase; }
  .sugg .sev.error { background:#ffe3e3; color:#c92a2a; }
  .sugg .sev.warn { background:#fff3bf; color:#e67700; }
  .sugg .sev.info { background:#e7f5ff; color:#1971c2; }
  .gate-hint { font-weight:600; color:#2b8a3e; }
</style>
</head>
<body>
<div class="wrap">
<header>
  <h1>jira-commit 执行完成</h1>
  <div class="meta">生成时间：__NOW__ ｜ 分支：<b>__BRANCH__</b> ｜ 任务：__NTASKS__ 个</div>
</header>

<div class="card">
  <h2><span class="num">1</span>提交规范分析结果（只读）</h2>
  <p class="hint">每条建议显示 ID / 严重度 / 规则 / 标题；完整问题与建议见第 5 张卡片「一键复制」。
     分析时间：__NORM_AT__</p>
  <div id="suggList"></div>
</div>

<div class="card">
  <h2><span class="num">2</span>手动提交和 push commit</h2>
  <p>所有任务合并成<b>一次</b> commit 提交。commit 内容可在下方编辑框中直接修改：
     改完点「复制」粘贴使用，或点「下载 commit_preview.md」替换原文件后再 <code>commit -F</code>。</p>
  <div class="hint">合并 commit 内容（可直接编辑；若你改过本地 commit_preview.md，点「同步」选中原文件载入最新内容）：</div>
  <textarea id="commitMsg" spellcheck="false">__COMBINED_ESC__</textarea>
  <button class="btn" onclick="copyCommit(this)">复制 commit 内容</button>
  <button class="btn ghost" onclick="downloadCommit()">下载 commit_preview.md</button>
  <button class="btn ghost" onclick="document.getElementById('mdFile').click()">同步 commit_preview.md</button>
  <button class="btn ghost" onclick="resetCommit()">恢复原始内容</button>
  <input type="file" id="mdFile" accept=".md" style="display:none" onchange="syncFromMd(this)">

  <p class="gate-hint open" id="gateHint">规范分析已全部确认 ✓（execute 入口校验通过）</p>

  <div id="addBlock">
  <pre><code># 1. 添加本次变更的全部文件（可用具体路径，或用变更目录）
git add &lt;本次变更的全部文件或目录&gt;

# 2. 提交（所有任务合并成一次 commit，不要分开提交；内容改过请先「下载」替换文件）
git commit -F "commit_preview.md"

# 3. 先同步 __MR_TARGET__（避免推送冲突）
git pull origin __MR_TARGET__

# 4. 推送当前分支
git push -u origin __BRANCH__</code></pre>
  </div>
</div>

<div class="card">
  <h2><span class="num">3</span>手动把 JIRA 任务打到「待验证」</h2>
  <p>依次打开下面的 JIRA 任务，将状态改为「待验证」：</p>
__JIRA_HTML__
</div>

<div class="card">
  <h2><span class="num">4</span>在 GitLab 提 merge request</h2>
  <p>推送完成后，从当前分支 <b>__BRANCH__</b> 向 <b>__MR_TARGET__</b> 提交 MR。标题与描述已按本次 commit 内容浓缩，
     可直接复制粘贴：</p>
  <p><a class="btn" id="mrBtn" href="__MR_URL__" target="_blank">新建 Merge Request：__BRANCH__ → __MR_TARGET__</a></p>
  <div class="hint">MR 标题（点击复制）：</div>
  <pre id="mrTitle" style="cursor:pointer" onclick="copyEl('mrTitle', this)">__MR_TITLE_ESC__</pre>
  <div class="hint">MR 描述（点击复制）：</div>
  <pre id="mrDesc" style="cursor:pointer;max-height:320px;overflow:auto" onclick="copyEl('mrDesc', this)">__MR_DESC_ESC__</pre>
  <button class="btn" onclick="copyMr(this)">一键复制标题 + 描述</button>
  <button class="btn ghost" onclick="downloadMr()">下载 merge_request.md</button>
</div>

<div class="card">
  <h2><span class="num">5</span>给 commit 添加评论（规范分析结果）</h2>
  <p><b>第 1 张卡片是 analyze 的规范分析结果快照（只读）</b>：先「一键复制」分析结果
     （按点分条），再打开该分支提交列表、点顶端 commit，把内容粘贴为评论。</p>
  <button class="btn" onclick="copyNorm(this)">一键复制规范分析结果</button>
  <a class="btn ghost" id="commitPageBtn" href="__COMMIT_URL__" target="_blank">打开本分支提交列表（先 push，点顶端 commit）</a>
  <div class="banner" id="commentBanner"></div>
</div>

<div class="card">
  <h2><span class="num">6</span>如有必要手动打 tag</h2>
  <p>需要发版时给本次合并 commit 打 tag。<b>先完成第 2 步的 push</b>，
     再从下面表单新建 tag（来源已预填当前分支，push 后分支顶端即本次 commit）：</p>
  <p><a class="btn" id="tagBtn" href="__TAGS_URL__" target="_blank">新建 Tag（来源：__BRANCH__）</a></p>
</div>
</div>

<script>
const ORIGINAL = __COMBINED_JSON__;
// 规范分析结果（analyze 产出，生成报告时内嵌，只读展示）：{analyzed_at, base, files, branch, suggestions}
// 页面不提供编辑/勾选/删除——人工流程 = 改代码后编辑 norm_analysis.json 的 status，
// 或删建议 + /jira-commit norm 交互更新规范；execute 入口校验全 checked 才生成本页面
const NORM = __NORM_JSON__;

function copyCommit(btn) {
  const t = document.getElementById('commitMsg');
  t.focus(); t.select();
  let ok = false;
  try { ok = document.execCommand('copy'); } catch (e) {}
  if (!ok && navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(t.value); ok = true;
  }
  const old = btn.textContent;
  btn.textContent = ok ? '已复制 ✓' : '复制失败，请 Ctrl+C';
  setTimeout(() => { btn.textContent = old; }, 1500);
}
function downloadCommit() {
  const blob = new Blob([document.getElementById('commitMsg').value],
                        { type: 'text/plain;charset=utf-8' });
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = 'commit_preview.md';
  a.click();
  URL.revokeObjectURL(a.href);
}
function resetCommit() {
  document.getElementById('commitMsg').value = ORIGINAL;
}
function syncFromMd(input) {
  const f = input.files && input.files[0];
  if (!f) return;
  const r = new FileReader();
  r.onload = function (e) {
    // 统一换行为 LF，避免 CRLF 混入 commit 内容
    document.getElementById('commitMsg').value = e.target.result.replace(/\r\n/g, '\n');
  };
  r.readAsText(f, 'utf-8');
  input.value = '';  // 清空以允许再次选同一个文件
}

// ------------------------------------------------ 规范分析（本地状态，无服务）
function esc(s) {
  return String(s == null ? '' : s)
    .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;').replace(/'/g, '&#39;');
}
function showBanner(id, kind, text) {
  const el = document.getElementById(id);
  if (!el) return;
  el.className = 'banner' + (kind ? ' ' + kind : '');
  el.textContent = text || '';
}
// ------------------------------------------------ 规范分析结果（只读展示）
// 页面不提供任何编辑/勾选/删除——人工流程 = 改代码后编辑 norm_analysis.json 的 status，
// 或删建议 + /jira-commit norm 交互更新规范；execute 入口校验全 checked 才生成本页面
function suggRow(s, i) {
  const sev = (s.severity || 'info').toLowerCase();
  return '<div class="sugg"><div class="top">' +
    '<span class="rid">' + esc(s.id || ('S' + (i + 1))) + '</span>' +
    '<span class="sev ' + esc(sev) + '">' + esc(sev) + '</span>' +
    '<span class="rid">' + esc(s.rule || '') + '</span>' +
    '<span class="ttl">' + esc(s.title || '') + '</span>' +
    '</div></div>';
}
function renderSuggestions() {
  const list = document.getElementById('suggList');
  const sugg = NORM.suggestions || [];
  list.innerHTML = sugg.length
    ? sugg.map(suggRow).join('')
    : '<p class="hint">未发现规范问题 ✓</p>';
}

// 一键复制规范分析结果：按点分条（severity/rule/标题/文件/问题/建议），贴 GitLab commit 评论用
function normText() {
  const sugg = NORM.suggestions || [];
  const lines = [];
  lines.push('【提交规范分析】分支 ' + (NORM.branch || '') +
    (NORM.analyzed_at ? '（分析于 ' + NORM.analyzed_at + '）' : '') +
    '，共 ' + sugg.length + ' 条');
  if (!sugg.length) lines.push('未发现规范问题（对照 norm_spec N-01~N-18）。');
  sugg.forEach(function (s, i) {
    lines.push('');
    lines.push((i + 1) + '. [' + (s.severity || 'info') + '][' + (s.rule || '') + '] ' +
      (s.title || ''));
    if (s.file) lines.push('   文件：' + s.file);
    if (s.detail) lines.push('   问题：' + s.detail);
    if (s.suggestion) lines.push('   建议：' + s.suggestion);
  });
  return lines.join('\n');
}
function copyNorm(btn) {
  const text = normText();
  const ta = document.createElement('textarea');
  ta.value = text;
  ta.style.position = 'fixed'; ta.style.opacity = '0';
  document.body.appendChild(ta);
  ta.focus(); ta.select();
  let ok = false;
  try { ok = document.execCommand('copy'); } catch (e) {}
  if (!ok && navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(text); ok = true;
  }
  document.body.removeChild(ta);
  const old = btn.textContent;
  btn.textContent = ok ? '已复制 ✓（去第 5 步粘贴为 commit 评论）' : '复制失败，请 Ctrl+C';
  setTimeout(function () { btn.textContent = old; }, 2000);
  showBanner('commentBanner', 'ok',
    ok ? '已复制 ' + (NORM.suggestions || []).length + ' 条分析结果。打开本分支提交列表、点顶端 commit 粘贴为评论。'
       : '');
}

renderSuggestions();

// ------------------------------------------------ MR 标题/描述（复制/下载）
function copyText(text, btn, okMsg) {
  const ta = document.createElement('textarea');
  ta.value = text;
  ta.style.position = 'fixed'; ta.style.opacity = '0';
  document.body.appendChild(ta);
  ta.focus(); ta.select();
  let ok = false;
  try { ok = document.execCommand('copy'); } catch (e) {}
  if (!ok && navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(text); ok = true;
  }
  document.body.removeChild(ta);
  if (btn) {
    const old = btn.textContent;
    btn.textContent = ok ? (okMsg || '已复制 ✓') : '复制失败，请 Ctrl+C';
    setTimeout(function () { btn.textContent = old; }, 1500);
  }
  return ok;
}
function copyEl(id, btn) {
  const el = document.getElementById(id);
  if (el) copyText(el.textContent, null, '');
  if (btn) {
    const old = btn.style.borderColor;
    btn.style.borderColor = '#2b8a3e';
    setTimeout(function () { btn.style.borderColor = old; }, 800);
  }
}
function copyMr(btn) {
  const t = document.getElementById('mrTitle');
  const d = document.getElementById('mrDesc');
  const text = '【标题】\n' + (t ? t.textContent : '') +
               '\n\n【描述】\n' + (d ? d.textContent : '');
  copyText(text, btn, '已复制 ✓（去 GitLab 粘贴）');
}
function downloadMr() {
  const t = document.getElementById('mrTitle');
  const d = document.getElementById('mrDesc');
  const text = '# MR 标题\n' + (t ? t.textContent : '') +
               '\n\n# MR 描述\n' + (d ? d.textContent : '') + '\n';
  const blob = new Blob([text], { type: 'text/plain;charset=utf-8' });
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = 'merge_request.md';
  a.click();
  URL.revokeObjectURL(a.href);
}
</script>
</body>
</html>
"""


def write_combined(combined, parsed):
    out = Path(jira_paths.get_output_dir()) / 'commit_preview.md'
    out.write_text(combined + "\n", encoding='utf-8')
    return out


def _label_chips(labels, esc):
    """工单 id 后面的标签小胶囊；无标签时返回空串（不渲染空括号）。

    标签来自 tasks.json 的 labels 字段（analyze 阶段按 template/labels.md 选定）。
    """
    if not labels:
        return ''
    return ''.join(f'<span class="tag">{esc(l)}</span>' for l in labels)


def write_html(combined, parsed, jira_links, web_url, branch, target_branch, norm, mr, out_path):
    esc = html_mod.escape

    if jira_links:
        jira_items = "\n".join(
            f'<li><a href="{esc(url)}" target="_blank">{esc(key)}</a>'
            f'{_label_chips(labels, esc)} - {esc(t)}</li>'
            for key, t, labels, url in jira_links)
        jira_html = f'<ul class="jira">{jira_items}</ul>'
    else:
        jira_html = '<p>本次未创建 JIRA 任务（jira_key 为空）。</p>'

    mr_url = (f"{web_url}/-/merge_requests/new?"
              f"merge_request%5Bsource_branch%5D={esc(branch)}"
              f"&merge_request%5Btarget_branch%5D={esc(target_branch)}") if web_url else '#'
    # tag：commit 此刻尚未创建（SHA 未知），链接到"新建 tag"表单并预填当前分支；
    # 用户 push 后分支顶端即本次合并 commit，从该表单建 tag 正好落在正确 commit 上
    tags_url = f"{web_url}/-/tags/new?ref={esc(branch)}" if web_url else '#'
    # 评论：跳到该分支 commit 列表页（GitLab `/-/commits/<ref>` 接受分支名；
    # `/-/commit/<id>` 只接受 SHA，传分支名会 404。push 后列表顶端即本次合并 commit），
    # 用户点进顶端 commit 粘贴复制好的分析结果
    commit_url = f"{web_url}/-/commits/{esc(branch)}" if web_url else '#'

    # JS 内嵌原始内容：JSON 序列化并防 </script> 截断
    combined_json = json.dumps(combined, ensure_ascii=False).replace('</', '<\\/')
    first_line = next((l.strip() for l in combined.splitlines() if l.strip()), '')
    norm_json = json.dumps({
        'analyzed_at': norm.get('analyzed_at', ''),
        'base': norm.get('base', ''),
        'files': norm.get('files', []),
        'branch': branch,           # 「一键复制」评论文本头用
        'suggestions': norm.get('suggestions', []),
    }, ensure_ascii=False).replace('</', '<\\/')

    html = (HTML_TEMPLATE
            .replace('__NOW__', esc(_now()))
            .replace('__BRANCH__', esc(branch))
            .replace('__MR_TARGET__', esc(target_branch))
            .replace('__NTASKS__', str(len(parsed)))
            .replace('__COMBINED_ESC__', esc(combined))
            .replace('__COMBINED_JSON__', combined_json)
            .replace('__NORM_JSON__', norm_json)
            .replace('__NORM_AT__', esc(norm.get('analyzed_at', '')) or '（未记录）')
            .replace('__JIRA_HTML__', jira_html)
            .replace('__MR_URL__', esc(mr_url))
            .replace('__MR_TITLE_ESC__', esc(mr[0]))
            .replace('__MR_DESC_ESC__', esc(mr[1]))
            .replace('__COMMIT_URL__', esc(commit_url))
            .replace('__TAGS_URL__', esc(tags_url)))
    Path(out_path).write_text(html, encoding='utf-8')

    # 兜底：模板占位符漏替换会导致 JS 直接崩（SyntaxError），宁可在生成期暴露
    for ph in ('__COMBINED_JSON__', '__NORM_JSON__'):
        if ph in html:
            raise RuntimeError(f"HTML 占位符 {ph} 未替换，模板与 write_html 不一致")


def _now():
    from datetime import datetime
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def notify(title, message, scene='execute'):
    """完成后通知：发飞书邮件（send_mail.py → lark-cli），失败不影响主流程"""
    script = Path(jira_paths.get_skill_dir()) / 'script' / 'send_mail.py'
    try:
        # Popen 不等待：lark-cli 发信可能耗时数秒，等待会阻塞主流程；
        # stdout/stderr 重定向 DEVNULL，避免子进程占住父进程管道导致调用方挂起
        subprocess.Popen(
            [sys.executable, str(script), scene, title, message],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception as e:
        print(f"[WARN] 邮件通知调用失败: {e}", file=sys.stderr)


# ---------------------------------------------------------------- main
def main():
    # --check-norm：execute 的**前置拦截**（创建 JIRA 之前调用，只校验不产出）
    if '--check-norm' in sys.argv:
        norm = load_norm_analysis(jira_paths.get_output_dir())
        n = len(norm['suggestions'])
        print(f"[OK] 规范分析门禁通过：{n} 条建议均已人工确认"
              + ("（无违规 ✓）" if not n else ""))
        return 0
    tasks_doc = load_tasks_doc()
    tasks = tasks_doc.get('tasks', [])
    if not tasks:
        sys.exit("[ERROR] tasks.json 中无任务")
    out_dir = jira_paths.get_output_dir()
    # 入口硬校验：规范分析产物不合法 → 直接退出，HTML 都不生成（先重跑 analyze）
    norm = load_norm_analysis(out_dir)
    config = load_config()
    project_root = jira_paths.get_project_root()
    if project_root:
        print(f"[INFO] 项目根: {project_root}")
    else:
        print("[WARN] 未解析到项目根，git 查询回退到当前目录"
              "（可能命中 .claude 仓库）；请设置 JIRA_COMMIT_PROJECT_ROOT",
              file=sys.stderr)
    web_url = gitlab_web_url(project_root)
    branch = current_branch(project_root)
    target_branch = (config.get('mr_target_branch') or 'main').strip() or 'main'
    if web_url and ('Agent_Tool' in web_url or '/.claude' in web_url):
        print(f"[WARN] Git remote 解析到技能仓库自身: {web_url}；"
              f"请把 JIRA_COMMIT_PROJECT_ROOT 指向业务工程根", file=sys.stderr)
    if not branch or not web_url:
        print(f"[WARN] GitLab 信息获取不完整 branch={branch!r} web_url={web_url!r}："
              f"报告 MR/tag 按钮将是空链接；请在工程仓库根目录重跑本脚本重新生成",
              file=sys.stderr)

    combined, parsed = build_combined(tasks)

    # JIRA 链接（带该单标签，供第 3 步卡片显示）
    jira_base = (config.get('jira_url') or '').rstrip('/')
    has_base = '://' in jira_base
    jira_links = [(p['jira'], p['title_cn'], p['labels'],
                   f"{jira_base}/browse/{p['jira']}" if has_base else '#')
                  for p in parsed if p['jira']]

    prev_path = write_combined(combined, parsed)
    # MR 标题+描述（优先 analyze 产出的 tasks.json 顶层 merge_request，缺失则规则聚合兜底）
    mr_title, mr_desc = build_merge_request(tasks_doc, parsed)
    mr_path = write_merge_request(mr_title, mr_desc)
    html_path = os.path.join(out_dir, 'commit_report.html')
    # 规范分析结果只读内嵌 HTML（入口已校验全 checked；无服务，file:// 双击打开）
    write_html(combined, parsed, jira_links, web_url, branch, target_branch, norm,
               (mr_title, mr_desc), html_path)

    err_n = sum(1 for s in norm['suggestions'] if (s.get('severity') or 'info') == 'error')
    print("=== 合并 commit 已生成 ===")
    print(f"  commit_preview.md : {prev_path}")
    print(f"  merge_request.md  : {mr_path}")
    print(f"  commit_report.html: {html_path}（浏览器直接打开，分析结果只读内嵌）")
    print(f"  规范分析: {len(norm['suggestions'])} 条已全部人工确认 ✓（error {err_n}）"
          f"{'，无违规 ✓' if not norm['suggestions'] else ''}")
    print()
    print("=== 合并 commit 内容 ===")
    print(combined)
    print()
    print("=== 请手动执行（commit_report.html 有完整指引） ===")
    print(f"  1. 手动提交和 push commit（git pull origin {target_branch} 后再 push）")
    print("  2. 手动把 JIRA 任务打到「待验证」")
    print("  3. 在 GitLab 提 merge request")
    print("  4. 一键复制分析结果 → 打开本分支提交列表 → 点顶端 commit 粘贴为评论")
    print("  5. 如有必要手动打 tag")

    # 飞书邮件（execute 完成提示，lark-cli；scene=execute 附 JIRA 链接与清单）
    msg = ("jira-commit 执行完成 ✅\n\n"
           "规范分析建议已全部人工确认 ✓\n\n"
           f"1. 手动提交和 push commit（先 pull {target_branch} 再 push）\n"
           "2. 手动把 JIRA 任务打到「待验证」\n"
           "3. 在 GitLab 提 merge\n"
           "4. 报告页一键复制分析结果贴为 commit 评论\n"
           "5. 如有必要手动打 tag\n\n"
           f"详情见: {html_path}")
    if '--no-mail' in sys.argv:
        print("[skip] --no-mail：未发送飞书通知")
    else:
        notify("jira-commit 执行完成", msg, scene='execute')
    return 0


if __name__ == '__main__':
    sys.exit(main())
