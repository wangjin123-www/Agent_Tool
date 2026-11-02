#!/usr/bin/env python3
"""
Skill Initializer - Creates a new skill from template

Usage:
    init_skill.py <skill-name> --path <path> [--author <author>] [--company <company>]
                  [--allowed-tools "<tools>"|none] [--context pull|push]

author/company/allowed-tools/context flow from the create wizard (Round 3
answers) into the generated frontmatter; 'none' for --allowed-tools omits
the line (inherit all tools).

Examples:
    init_skill.py my-new-skill --path skills/public --author wangjin0115 --company cviauto
    init_skill.py my-api-helper --path skills/private --allowed-tools none --context push
"""

import re
import sys
from pathlib import Path

# Windows 默认 GBK 控制台打不出 emoji/中文，强制 UTF-8 输出
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


# §2.4.2 frontmatter 动态构建：author/company/allowed-tools/context 来自 create
# 向导的 CLI 参数（Round 3 问答），本脚本不硬编码任何署名。
DESCRIPTION_TODO = ('[TODO: 能力 + 触发场景 + 边界三要素。例：'
                    'Comprehensive PDF manipulation toolkit for extracting text and tables, '
                    'creating/merging/splitting documents. Use when the user asks to fill in a '
                    'PDF form or batch-process PDFs. Not for simple PDF viewing.]')

DEFAULT_ALLOWED_TOOLS = '[Bash, Read, Write, AskUserQuestion, Grep, Glob]'

# argument-hint 子命令分隔符 / 校验子命令名（小写字母数字连字符）
HINT_SEP = '|'
CMD_NAME_RE = re.compile(r'^[a-z][a-z0-9-]*$')


def build_frontmatter(skill_name, author, company, allowed_tools, context_mode,
                      commands=None):
    """Build the §2.4.2 frontmatter block.

    allowed_tools == 'none' 表示继承全部工具：省略 allowed-tools 行。
    commands 非空时自动填 argument-hint，避免生成物留 TODO。
    """
    lines = [
        '---',
        'version: 1.0.0',
        f'author: "{author}"',
        f'company: "{company}"',
        f'name: {skill_name}',
        f'description: "{DESCRIPTION_TODO}"',
        'category: "[TODO: 分类，如 development / documentation / automation / testing]"',
    ]
    if commands:
        lines.append(f'argument-hint: "{HINT_SEP.join(commands)}"')
    else:
        lines.append(
            'argument-hint: "[TODO: 子命令用竖线分隔，如 analyze|preview|execute；'
            '无子命令则删除本行]"'
        )
    if allowed_tools != 'none':
        lines.append(f'allowed-tools: {allowed_tools}')
    lines += [
        f'context: {context_mode}',
        'tags: [TODO]',
        'license: Complete terms in LICENSE.txt',
        '---',
    ]
    return '\n'.join(lines)


SKILL_BODY_TEMPLATE = """
# {skill_title}

一句话说明这个 skill 做什么、边界在哪（与 frontmatter description 呼应，不复述）。

## Entry

`$0` 为空或未匹配 → 用 AskUserQuestion 列出下表。

{entry_table}

## Commands

{command_sections}

## 资源路由规则

- **首选脚本**：确定性操作（相同输入必得相同输出）一律走 `python scripts/cmd/cmd_<verb>.py`，步骤细节写在脚本里，不写在这份 SKILL.md
- **次选参考**：需要背景知识/规范/schema 才读 `references/<verb>.md`
- 命令段只保留：触发条件、调用行、输出位置。**禁止**在此展开多步流程（>10 行即下沉）
- 路径一律相对 skill 根目录；绝对路径放 `config/config.conf`，由 `scripts/common/conf.py` 读取
- 产物统一写 `output/`（已 gitignore）

## 输出约定

| 产物 | 位置 |
|------|------|
| 运行日志/中间产物 | `output/` |
| 用户可见结果 | [TODO: 说明交付形式] |

## 脚本分层（固定，勿改层名）

```
scripts/
├── cmd/       # 入口层：一个子命令一个 cmd_<verb>.py，薄壳 ≤100 行，只做参数解析+调 core
├── core/      # 业务层：core.py，核心逻辑，被 cmd 调用，可复用
└── common/    # 公共层：conf.py 读 config.conf、log.py 统一 UTF-8 输出
```

依赖单向 `cmd → core → common`，禁止反向 import 与跨层调用。
新增能力改 `core/`，新增命令加 `cmd/` 薄壳，目录结构不变。
"""

ENTRY_TABLE_HEADER = """| 命令 | 说明 |
|------|------|"""

ENTRY_ROW_NO_CMD = "| [TODO: 唯一功能名] | [TODO: 一句话说明] |"

ENTRY_ROW_TEMPLATE = "| {verb} | [TODO: 一句话说明] |"

DEFAULT_VERB = "run"

COMMAND_SECTION_TEMPLATE = """### {verb}

触发：[TODO: 什么情况下走这个命令]

首选（脚本）：

```bash
python scripts/cmd/cmd_{verb}.py [args]
```

次选（参考）：`Read references/{verb}.md`

输出：[TODO: 写到哪、怎么告诉用户]
"""

COMMAND_SECTION_PLACEHOLDER = """### [TODO: 命令名]

触发：[TODO]

首选（脚本）：

```bash
python scripts/cmd/cmd_[TODO].py [args]
```

输出：[TODO]
"""

CMD_TEMPLATE = '''#!/usr/bin/env python3
"""__SKILL__ :: __VERB__ 子命令入口（薄壳：只做参数解析 + 调 core，不写业务逻辑）。"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from common.log import setup_stdout          # noqa: E402
from core.core import __VERB_FN__            # noqa: E402


def main():
    setup_stdout()
    parser = argparse.ArgumentParser(description="__SKILL__ :: __VERB__")
    parser.add_argument("input", nargs="?", help="TODO: 输入参数说明")
    args = parser.parse_args()
    return __VERB_FN__(args.input)


if __name__ == "__main__":
    sys.exit(main())
'''

CORE_HEADER_TEMPLATE = '''#!/usr/bin/env python3
"""__SKILL__ 业务层：核心逻辑。只被 scripts/cmd/* 调用，禁止 import cmd。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from common.conf import load_config          # noqa: E402
from common.log import log                   # noqa: E402


'''

CORE_FUNC_TEMPLATE = '''def __VERB_FN__(arg=None):
    """TODO: __VERB__ 的实际逻辑。返回 0 表示成功。"""
    cfg = load_config()
    log(f"__VERB__ 启动, arg={arg}, sections={cfg.sections()}")
    # TODO: 实现业务；耗时/易错步骤封装成独立函数放本文件
    return 0


'''

CONF_TEMPLATE = '''#!/usr/bin/env python3
"""读取 config/config.conf。绝对路径只在这里定义，禁止散落到其他脚本。"""

import configparser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONFIG_PATH = ROOT / "config" / "config.conf"
FALLBACK_PATH = ROOT / "config" / "config.conf.example"

_cache = None


def load_config(path=None):
    """读配置；真实配置缺失时回退 .example。返回 ConfigParser。"""
    global _cache
    if path is None and _cache is not None:
        return _cache
    target = Path(path) if path else (CONFIG_PATH if CONFIG_PATH.exists() else FALLBACK_PATH)
    parser = configparser.ConfigParser()
    if target.exists():
        parser.read(target, encoding="utf-8")
    if path is None:
        _cache = parser
    return parser


def root():
    """skill 根目录。所有相对路径以此为基准。"""
    return ROOT
'''

LOG_TEMPLATE = '''#!/usr/bin/env python3
"""统一 UTF-8 输出：Windows 控制台默认 GBK，中文/emoji 会编码失败。"""

import sys


def setup_stdout():
    """把 stdout/stderr 切成 UTF-8。每个 cmd 入口先调一次。"""
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")


def log(*parts):
    """统一打印：立即 flush，避免后台运行时看不到输出。"""
    setup_stdout()
    print(*parts, flush=True)
'''

EXAMPLE_REFERENCE = """# {verb} 参考文档

> 本文件是 SKILL.md 中 `{verb}` 命令的**次选**路由：仅在需要背景知识/规范/schema
> 时读取。确定性操作请走首选脚本 `scripts/cmd/cmd_{verb}.py`。

## 何时读这份文档

- 需要领域知识、判定标准、数据格式说明
- 脚本报错需要人工判断原因
- 需要给用户解释结论依据

## 内容建议

- 领域术语与枚举含义
- 判定规则/阈值表
- 输入输出格式与示例
- 常见异常与处置
"""

EXAMPLE_ASSET = """# Example Asset File

This placeholder represents where asset files would be stored.
Replace with actual asset files (templates, images, fonts, etc.) or delete if not needed.

Asset files are NOT intended to be loaded into context, but rather used within
the output Claude produces.

Example asset files from other skills:
- Brand guidelines: logo.png, slides_template.pptx
- Frontend builder: hello-world/ directory with HTML/React boilerplate
- Typography: custom-font.ttf, font-family.woff2
- Data: sample_data.csv, test_dataset.json

## Common Asset Types

- Templates: .pptx, .docx, boilerplate directories
- Images: .png, .jpg, .svg, .gif
- Fonts: .ttf, .otf, .woff, .woff2
- Boilerplate code: Project directories, starter files
- Icons: .ico, .svg
- Data files: .csv, .json, .xml, .yaml

Note: This is a text placeholder. Actual assets can be any file type.
"""

EXAMPLE_TEMPLATE = """# Output Template

Placeholder for output templates used by {skill_name}.

Templates are blank skeletons you start from, not reference docs. Copy one into
`output/`, fill in the blanks, and ship the result.

Example templates from other skills:
- report_template.html - fixed report layout with placeholders
- plan-template.md - skeleton for a generated plan document
- slides_template.pptx - deck with placeholder slides

Delete this file and the templates/ directory if the skill has no fixed output shape.
"""

EXAMPLE_CONFIG = """# Configuration for {skill_name}
# Copy to config/config.conf and fill in real values.
# config/config.conf is gitignored; this .example file is committed.
#
# Put machine-specific or project-specific values here (absolute paths, tool
# chain locations, credentials, endpoints). SKILL.md and scripts must read
# these at runtime instead of hardcoding absolute paths.

# Example:
# PROJECT_ROOT=/abs/path/to/project
# TOOLCHAIN_PATH=/abs/path/to/toolchain
"""

EXAMPLE_EXAMPLE_README = """# Example

Placeholder for example inputs and finished outputs.

Put a realistic input next to the output the skill should produce from it, so
Claude has a concrete target to imitate:

- input.md / output.md
- request.txt / response.txt
- before.png / after.png

Delete this directory if concrete examples don't add value.
"""

EXAMPLE_DOCS_README = """# Docs

Placeholder for supporting documentation that ships with {skill_name}.

Use this for user-facing docs, design notes, or background that isn't needed
while the skill runs. Anything Claude must read while working belongs in
`references/` instead.

Delete this directory if there's nothing to document separately.
"""

EXAMPLE_UTILS_README = """# Utils

Placeholder for external tools bundled with {skill_name}.

Put helper tools, third-party binaries, or vendored dependencies here if the
skill needs them. Reference them with relative paths from the skill root.

Delete this directory if the skill relies only on `scripts/`.
"""

EXAMPLE_LICENSE = """[TODO: Choose a license for {skill_name} and replace this file's contents,
or delete the file if the skill is not distributed.]

Common choices: Apache-2.0, MIT, or an internal company license.
"""

GITIGNORE = """# Runtime output - never commit
output/

# Real config holds machine-specific values; commit config/*.example instead
config/config.conf

# Python
__pycache__/
*.pyc
"""


def title_case_skill_name(skill_name):
    """Convert hyphenated skill name to Title Case for display."""
    return ' '.join(word.capitalize() for word in skill_name.split('-'))


def parse_commands(raw):
    """把 --commands 的值（竖线分隔）解析成列表；'none'/空 → 空列表。

    同时校验子命令名合法性，非法直接抛 ValueError（调用方转成友好报错）。
    """
    if not raw or raw.strip().lower() == 'none':
        return []
    verbs = [v.strip() for v in raw.split('|') if v.strip()]
    seen = set()
    for verb in verbs:
        if not CMD_NAME_RE.match(verb):
            raise ValueError(
                f"invalid command name '{verb}': lowercase letters, digits and "
                f"hyphens only, must start with a letter"
            )
        if verb in seen:
            raise ValueError(f"duplicate command name '{verb}'")
        seen.add(verb)
    return verbs


def verb_fn_name(verb):
    """子命令名 → core 里的函数名，如 'auto-baud' → 'cmd_auto_baud'。"""
    return 'cmd_' + verb.replace('-', '_')


def build_entry_table(verbs):
    """Entry 菜单表：有子命令列全，无子命令留一行 TODO。"""
    if not verbs:
        return ENTRY_TABLE_HEADER + '\n' + ENTRY_ROW_NO_CMD
    rows = [ENTRY_TABLE_HEADER] + [ENTRY_ROW_TEMPLATE.format(verb=v) for v in verbs]
    return '\n'.join(rows)


def build_command_sections(verbs):
    """每个子命令一段：触发 / 首选脚本 / 次选参考 / 输出。"""
    if not verbs:
        return COMMAND_SECTION_PLACEHOLDER
    return '\n'.join(
        COMMAND_SECTION_TEMPLATE.format(verb=v) for v in verbs
    )


def build_skill_body(skill_name, skill_title, verbs):
    """组装生成的 SKILL.md 正文（不含 frontmatter）。"""
    return SKILL_BODY_TEMPLATE.format(
        skill_name=skill_name,
        skill_title=skill_title,
        entry_table=build_entry_table(verbs),
        command_sections=build_command_sections(verbs),
    )


def init_skill(skill_name, path, author, company, allowed_tools, context_mode,
               verbs=None):
    """
    Initialize a new skill directory with template SKILL.md.

    Creates the full house-spec directory structure; unused directories can
    be deleted afterwards.

    Args:
        skill_name: Name of the skill
        path: Path where the skill directory should be created
        author: Skill author (from create wizard Q9)
        company: Company/team attribution (from create wizard Q10)
        allowed_tools: allowed-tools value, or 'none' to omit the line (Q11)
        context_mode: 'pull' or 'push' (from create wizard Q12)
        verbs: 子命令名列表（Q5）；空列表表示单功能 skill

    Returns:
        Path to created skill directory, or None if error
    """
    # Determine skill directory path
    skill_dir = Path(path).resolve() / skill_name

    # Check if directory already exists
    if skill_dir.exists():
        print(f"❌ Error: Skill directory already exists: {skill_dir}")
        return None

    # Create skill directory
    try:
        skill_dir.mkdir(parents=True, exist_ok=False)
        print(f"✅ Created skill directory: {skill_dir}")
    except Exception as e:
        print(f"❌ Error creating directory: {e}")
        return None

    # Create SKILL.md from frontmatter + minimalist router body
    skill_title = title_case_skill_name(skill_name)
    skill_content = build_frontmatter(
        skill_name, author, company, allowed_tools, context_mode, verbs
    ) + '\n' + build_skill_body(skill_name, skill_title, verbs)

    skill_md_path = skill_dir / 'SKILL.md'
    try:
        skill_md_path.write_text(skill_content, encoding='utf-8')
        line_count = len(skill_content.splitlines())
        print(f"✅ Created SKILL.md ({line_count} lines)")
    except Exception as e:
        print(f"❌ Error creating SKILL.md: {e}")
        return None

    # Create scripts/ with the fixed three-layer layout: cmd / core / common
    try:
        scripts_dir = skill_dir / 'scripts'
        cmd_dir = scripts_dir / 'cmd'
        core_dir = scripts_dir / 'core'
        common_dir = scripts_dir / 'common'
        for d in (cmd_dir, core_dir, common_dir):
            d.mkdir(parents=True, exist_ok=True)

        # cmd/: one thin entry per subcommand (single-purpose skill gets one too)
        effective_verbs = verbs or [DEFAULT_VERB]
        for verb in effective_verbs:
            cmd_file = cmd_dir / f'cmd_{verb}.py'
            cmd_file.write_text(
                CMD_TEMPLATE
                .replace('__SKILL__', skill_name)
                .replace('__VERB_FN__', verb_fn_name(verb))
                .replace('__VERB__', verb),
                encoding='utf-8',
            )
            print(f"✅ Created scripts/cmd/cmd_{verb}.py")

        # core/: one function per cmd, business layer
        core_file = core_dir / 'core.py'
        core_src = CORE_HEADER_TEMPLATE.replace('__SKILL__', skill_name)
        for verb in effective_verbs:
            core_src += CORE_FUNC_TEMPLATE.replace(
                '__VERB_FN__', verb_fn_name(verb)
            ).replace('__VERB__', verb)
        core_file.write_text(core_src, encoding='utf-8')
        print("✅ Created scripts/core/core.py")

        # common/: config access + UTF-8 logging, ready to use
        (common_dir / 'conf.py').write_text(CONF_TEMPLATE, encoding='utf-8')
        (common_dir / 'log.py').write_text(LOG_TEMPLATE, encoding='utf-8')
        (common_dir / '__init__.py').write_text('', encoding='utf-8')
        (core_dir / '__init__.py').write_text('', encoding='utf-8')
        print("✅ Created scripts/common/{conf.py, log.py}")

        # Per-verb reference stub, second-choice route in SKILL.md
        references_dir = skill_dir / 'references'
        references_dir.mkdir(exist_ok=True)
        for verb in effective_verbs:
            ref_file = references_dir / f'{verb}.md'
            ref_file.write_text(
                EXAMPLE_REFERENCE.format(skill_title=skill_title, verb=verb),
                encoding='utf-8',
            )
            print(f"✅ Created references/{verb}.md")

        # Create assets/ directory with example asset placeholder
        assets_dir = skill_dir / 'assets'
        assets_dir.mkdir(exist_ok=True)
        example_asset = assets_dir / 'example_asset.txt'
        example_asset.write_text(EXAMPLE_ASSET, encoding='utf-8')
        print("✅ Created assets/example_asset.txt")

        # Create templates/ directory with example output template
        templates_dir = skill_dir / 'templates'
        templates_dir.mkdir(exist_ok=True)
        example_template = templates_dir / 'template_example.md'
        example_template.write_text(EXAMPLE_TEMPLATE.format(skill_name=skill_name), encoding='utf-8')
        print("✅ Created templates/template_example.md")

        # Create config/ directory with example config (real config is gitignored)
        config_dir = skill_dir / 'config'
        config_dir.mkdir(exist_ok=True)
        example_config = config_dir / 'config.conf.example'
        example_config.write_text(EXAMPLE_CONFIG.format(skill_name=skill_name), encoding='utf-8')
        print("✅ Created config/config.conf.example")

        # Create example/ directory for sample inputs and finished outputs
        example_dir = skill_dir / 'example'
        example_dir.mkdir(exist_ok=True)
        (example_dir / 'README.md').write_text(EXAMPLE_EXAMPLE_README, encoding='utf-8')
        print("✅ Created example/README.md")

        # Create docs/ directory for supporting documentation
        docs_dir = skill_dir / 'docs'
        docs_dir.mkdir(exist_ok=True)
        (docs_dir / 'README.md').write_text(EXAMPLE_DOCS_README.format(skill_name=skill_name), encoding='utf-8')
        print("✅ Created docs/README.md")

        # Create utils/ directory for bundled external tools
        utils_dir = skill_dir / 'utils'
        utils_dir.mkdir(exist_ok=True)
        (utils_dir / 'README.md').write_text(EXAMPLE_UTILS_README.format(skill_name=skill_name), encoding='utf-8')
        print("✅ Created utils/README.md")

        # Create output/ directory for runtime artifacts (gitignored)
        output_dir = skill_dir / 'output'
        output_dir.mkdir(exist_ok=True)
        print("✅ Created output/")

        # Create .gitignore
        (skill_dir / '.gitignore').write_text(GITIGNORE, encoding='utf-8')
        print("✅ Created .gitignore")

        # Create LICENSE.txt
        (skill_dir / 'LICENSE.txt').write_text(EXAMPLE_LICENSE.format(skill_name=skill_name), encoding='utf-8')
        print("✅ Created LICENSE.txt")
    except Exception as e:
        print(f"❌ Error creating resource directories: {e}")
        return None

    # Create README.md for users
    readme_content = f"""# {skill_name}

[TODO: 一句话描述这个skill做什么]

## 使用

```
/{skill_name}
```

## 操作

| 命令 | 说明 |
|------|------|
@@COMMAND_ROWS@@

## 目录结构

```
{skill_name}/
├── SKILL.md          # 必需：纯路由器（Entry 表 + 各命令首选脚本/次选参考行）
├── scripts/          # 固定三层，勿改层名
│   ├── cmd/          # 入口层：每命令一个 cmd_<verb>.py 薄壳（≤100 行）
│   ├── core/         # 业务层：core.py，核心逻辑
│   └── common/       # 公共层：conf.py 读 config.conf、log.py UTF-8 输出
├── references/       # 次选路由：<verb>.md，按需读取
├── config/           # 配置（绝对路径只放这里，gitignore 真实配置）
├── templates/        # 可选：输出模板（空骨架）
├── assets/           # 可选：资源文件（图片等）
├── example/          # 可选：示例输入和成品输出
├── docs/             # 可选：附带文档
├── utils/            # 可选：相关外部工具
├── output/           # 运行时输出（gitignore）
├── README.md
├── .gitignore
└── LICENSE.txt       # 许可证
```

> 用不到的目录/文件直接删除。分层脚本骨架已可运行，改 `core/core.py` 即可。
"""
    readme_content = readme_content.replace(
        '@@COMMAND_ROWS@@', build_entry_table(verbs)
    )
    readme_path = skill_dir / 'README.md'
    try:
        readme_path.write_text(readme_content, encoding='utf-8')
        print("✅ Created README.md")
    except Exception as e:
        print(f"❌ Error creating README.md: {e}")

    # Print next steps
    print(f"\n✅ Skill '{skill_name}' initialized successfully at {skill_dir}")
    print("\nNext steps:")
    print("1. Fill core/core.py with real logic, then wire args in scripts/cmd/*.py")
    print("2. Test each command: python scripts/cmd/cmd_<verb>.py <args>")
    print("3. Replace the remaining TODOs in SKILL.md and README.md")
    print("4. Delete the directories this skill doesn't need, then run the validator")

    return skill_dir


FLAG_TO_KEY = {
    '--path': 'path',
    '--author': 'author',
    '--company': 'company',
    '--allowed-tools': 'allowed_tools',
    '--context': 'context',
    '--commands': 'commands',
}


def parse_args(argv):
    """Parse positional skill name plus the create-wizard flags.

    Returns an options dict, or None on invalid input (bad flags/values).
    """
    if not argv:
        return None
    opts = {
        'skill_name': argv[0],
        'path': None,
        'author': '[TODO: author]',
        'company': '[TODO: company]',
        'allowed_tools': DEFAULT_ALLOWED_TOOLS,
        'context': 'pull',
        'commands': 'none',
    }
    i = 1
    while i < len(argv):
        flag = argv[i]
        if flag not in FLAG_TO_KEY or i + 1 >= len(argv):
            return None
        opts[FLAG_TO_KEY[flag]] = argv[i + 1]
        i += 2
    if not opts['path']:
        return None
    if opts['context'] not in ('pull', 'push'):
        return None
    try:
        opts['verbs'] = parse_commands(opts['commands'])
    except ValueError as e:
        print(f"❌ Error: {e}")
        return None
    return opts


def main():
    opts = parse_args(sys.argv[1:])
    if opts is None:
        print("Usage: init_skill.py <skill-name> --path <path> "
              "[--author <author>] [--company <company>] "
              "[--allowed-tools \"<tools>\"|none] [--context pull|push] "
              "[--commands \"<verb1|verb2>\"|none]")
        print("\nSkill name requirements:")
        print("  - Hyphen-case identifier (e.g., 'data-analyzer')")
        print("  - Lowercase letters, digits, and hyphens only")
        print("  - Max 64 characters")
        print("  - Must match directory name exactly")
        print("\nFlags (create wizard answers):")
        print("  --author         frontmatter author (Q9)")
        print("  --company        frontmatter company (Q10)")
        print("  --allowed-tools  tool list, or 'none' to omit the line (Q11)")
        print("  --context        'pull' (default) or 'push' (Q12)")
        print("  --commands       subcommands, '|'-separated, or 'none' (Q5);")
        print("                   generates one scripts/cmd/cmd_<verb>.py each")
        print("\nExamples:")
        print("  init_skill.py my-new-skill --path skills/public --author wangjin0115 --company cviauto")
        print("  init_skill.py my-api-helper --path skills/private --allowed-tools none --context push")
        print("  init_skill.py log-analyzer --path skills/private --commands \"analyze|preview|export\"")
        sys.exit(1)

    skill_name = opts['skill_name']
    path = opts['path']

    print(f"🚀 Initializing skill: {skill_name}")
    print(f"   Location: {path}")
    print(f"   Author: {opts['author']} | Company: {opts['company']} | "
          f"Allowed-tools: {opts['allowed_tools']} | Context: {opts['context']}")
    print(f"   Commands: {opts['verbs'] if opts['verbs'] else '(单功能 skill)'}")
    print()

    result = init_skill(
        skill_name,
        path,
        author=opts['author'],
        company=opts['company'],
        allowed_tools=opts['allowed_tools'],
        context_mode=opts['context'],
        verbs=opts['verbs'],
    )

    if result:
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
