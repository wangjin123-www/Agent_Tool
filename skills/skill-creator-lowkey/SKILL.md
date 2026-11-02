---
version: 1.0.0
author: wangjin0115
company: cviauto
name: skill-creator-lowkey
description: 技能创建向导。用于创建或编辑扩展 Claude 能力的专用技能，包含工作流、工具集成、领域专家和知识库等类型。
argument-hint: create|edit|package|validate
tags:
    - skill
    - creator
    - workflow
    - tool
    - domain
    - reference
---

# Skill Creator

## Entry

**先输出以下说明给用户：**

> 本工具基于官方 skill-creator 改造，核心特点：
> 1. **Token 节省** — SKILL.md 仅做路由（~50行），设计指南按需从 references/ 加载，非全量注入
> 2. **交互式路由** — argument-hint + AskUserQuestion 菜单，选哪个命令才加载对应文档
> 3. **脚本外置** — 脚本直接执行不进入上下文，省 token
>
> 对比官方：465行单文件全量加载 → 本版50行路由 + 5个references按需读取

`$0` is empty or unmatched → AskUserQuestion with menu.

| Option | Description |
|--------|-------------|
| create | Create a new skill from scratch |
| edit | Edit/improve an existing skill |
| package | Package a skill into .skill file |
| validate | Validate a skill's structure |

## Command: create

### Step 1: Gather requirements

Use AskUserQuestion in **three rounds** (每轮 ≤4 问), collecting everything needed to fill the full §2.4.2 frontmatter:

**Round 1:**

**Q1: skill type**
| Option | Description |
|--------|-------------|
| workflow | 多步骤流程类（编译、部署、测试） |
| tool | 工具集成类（API、格式转换） |
| domain | 领域专家类（编码规范、业务逻辑） |
| reference | 知识库类（文档查询、schema） |

**Q2: skill name** — AskUserQuestion with user typing skill name（小写字母/数字/连字符，≤64 字符）

**Q3: trigger description** — AskUserQuestion: "用户说什么话应该触发这个 skill？"（按能力+触发场景+边界三要素引导，见 [skill-basics.md](references/skill-basics.md)）

**Q4: category** — 分类标签（development / documentation / automation / testing，可 Other 手动输入）

**Round 2:**

**Q5: 子命令 argument-hint**（有子命令时手动输入，如 `analyze|preview|execute`；无子命令选"无"）
| Option | Description |
|--------|-------------|
| 无子命令 | 单一功能 skill，删除 argument-hint 字段 |
| 有子命令 | 手动输入竖线分隔的子命令列表 |

**Q6: 资源目录 A** — AskUserQuestion (multiSelect):
| Option | Description |
|--------|-------------|
| scripts | 需要可执行脚本 |
| references | 需要参考文档 |
| templates | 需要输出模板（空骨架） |
| assets | 需要资源文件（图片、字体等） |

**Q7: 资源目录 B** — AskUserQuestion (multiSelect):
| Option | Description |
|--------|-------------|
| config | 需要环境配置（绝对路径等放这里） |
| example | 需要示例输入和成品输出 |
| docs | 需要附带文档 |
| utils | 需要外部工具 |

**Q8: tags** — 根据 skill 功能自动生成（推荐），或用户手动输入

**Round 3:**

**Q9: author** — AskUserQuestion: "skill 作者署名？"（默认选项 `wangjin0115`，可 Other 手动输入）

**Q10: company** — AskUserQuestion: "归属公司/团队？"（默认选项 `cviauto`，可 Other 手动输入）

**Q11: allowed-tools** — AskUserQuestion: "skill 执行期间允许哪些工具？"
| Option | Description |
|--------|-------------|
| 继承全部工具 | 删除 allowed-tools 字段 |
| 常用默认集 | `[Bash, Read, Write, AskUserQuestion, Grep, Glob]` |
| 手动输入 | Other 填写逗号分隔的工具列表 |

**Q12: context** — AskUserQuestion: "skill 加载方式？"
| Option | Description |
|--------|-------------|
| pull | 按需激活（默认，多数 skill 用这个） |
| push | 始终注入上下文（持续生效的规范类 skill） |

### Step 2: Plan & Scaffold

Plan reusable resources → See [creation-steps.md](references/creation-steps.md) Step 1-2

Run scaffold（Q5/Q9-Q12 的答案通过参数传入，不留硬编码默认值）:
```bash
python scripts/init_skill.py <name> --path <dir> \
  --author "<Q9 答案>" \
  --company "<Q10 答案>" \
  --allowed-tools "<Q11 工具列表，选继承全部工具时传 none>" \
  --context <Q12: pull|push> \
  --commands "<Q5 子命令列表，无子命令传 none>"
```

### Step 3: Implement

Implement resources and write SKILL.md → See [creation-steps.md](references/creation-steps.md) Step 4

**重要规则：**
1. SKILL.md 正文必须使用中文（frontmatter 的 name/description 可用英文）
2. **生成的 SKILL.md frontmatter 必须填满 §2.4.2 完整模板（11 字段一个不少）**：`version` 固定 1.0.0；`author`/`company` 取 Round 3 用户输入（**禁止硬编码**）；`allowed-tools`/`context` 按 Q11/Q12 取值；`license` 默认 `Complete terms in LICENSE.txt`；`tags` 取 Q8。字段与格式参照 [skill-basics.md](references/skill-basics.md)。仅两处可删行：无子命令删 `argument-hint`，Q11 选"继承全部工具"删 `allowed-tools`
3. **禁止硬编码绝对路径**。SKILL.md、scripts、references 中一律使用相对路径（相对于 skill 根目录）。如果必须使用绝对路径（如工具链路径、项目根路径），必须放在 `config/config.conf` 中配置，运行时读取
4. **输出文件统一放在 `output/` 目录**，并在 `.gitignore` 中忽略该目录
5. init 脚手架会生成完整 §2.4.3 目录结构，**按 Round 2 用户勾选结果删除未用目录**，不留无用占位文件
6. **生成的 SKILL.md 是纯路由器（含 frontmatter ≤120 行）**：Entry 菜单表 + 每命令"首选 `python scripts/cmd/cmd_<verb>.py` + 次选 `Read references/<verb>.md`"；步骤细节一律下沉 scripts/references，不写长流程
7. **scripts/ 固定三层 `cmd/core/common`，依赖单向 `cmd → core → common`**（详见 [design-principles.md](references/design-principles.md)）；新增命令只加 cmd 薄壳，新增能力改 core，结构永不变

Read design references as needed:
- Skill structure & basics → [skill-basics.md](references/skill-basics.md)
- Design patterns (interactive, token optimization) → [design-principles.md](references/design-principles.md)
- Workflow patterns → [workflows.md](references/workflows.md)
- Output patterns → [output-patterns.md](references/output-patterns.md)

### Step 4: Confirm

Use AskUserQuestion: "skill 已创建完成，是否需要打包？"
| Option | Description |
|--------|-------------|
| yes | 立即打包为 .skill 文件 |
| no | 仅创建，稍后打包 |
| test | 先验证再决定 |

## Command: edit

### Step 1: Select skill

Scan `.claude/skills/` for available skills → Use AskUserQuestion to list them as options.

### Step 2: Select edit type

Use AskUserQuestion:
| Option | Description |
|--------|-------------|
| SKILL.md | 修改 frontmatter 或指令内容（按 §2.4.2 模板校对字段完整性，缺 version/category/tags 等时补全） |
| 资源目录 | 在 scripts / references / templates / assets / config / example / docs / utils 中新增或修改内容（选后追问具体哪个目录） |
| structure | 重构 skill 目录结构（对齐 §2.4.3 完整结构） |
| 全部 | 扫描并按规范检查所有内容，统一修改 |

### Step 3: Apply changes

Read the target skill's SKILL.md → Apply changes → See [skill-basics.md](references/skill-basics.md) for design principles

Test modified scripts if any.

## Command: package

### Step 1: Select skill

Scan `.claude/skills/` for available skills → Use AskUserQuestion to list them as options.

### Step 2: Run

```bash
python scripts/package_skill.py <path/to/skill-folder> [output-dir]
```

Auto-validates then creates `.skill` file.

## Command: validate

### Step 1: Select skill

Scan `.claude/skills/` for available skills → Use AskUserQuestion to list them as options.

### Step 2: Run

```bash
python scripts/quick_validate.py <path/to/skill-folder>
```

Checks frontmatter format, required fields, naming conventions, plus house conventions:
SKILL.md ≤120 行、引用的 scripts/references 路径存在、scripts/ 三层齐全且 core 未反向 import cmd。
Warnings don't fail the run — treat them as the fix list.
