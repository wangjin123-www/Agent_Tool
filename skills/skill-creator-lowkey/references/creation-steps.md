# Skill Creation Steps

## Step 1: Understand with Concrete Examples

Ask user:
- What functionality should the skill support?
- Give examples of how it would be used
- What user phrases should trigger this skill?

Avoid asking too many questions at once. Start with the most important.

## Step 2: Plan Reusable Contents

For each example, identify:
1. How to execute from scratch
2. What scripts/references/assets would help when repeated

| Need | Resource | Example |
|------|----------|---------|
| Same code rewritten | `scripts/*.py` | `rotate_pdf.py` |
| Same boilerplate | `assets/template/` | HTML/React boilerplate |
| Schema discovery each time | `references/schema.md` | BigQuery table schemas |

## Step 3: Initialize

```bash
python scripts/init_skill.py <skill-name> --path <output-directory> \
  --author "<Q9>" --company "<Q10>" \
  --allowed-tools "<Q11|none>" --context <Q12> \
  --commands "<Q5 子命令竖线列表|none>"
```

Creates:
- **极简路由版 SKILL.md**：Entry 菜单表 + 每个 Command 一段"首选脚本 + 次选 reference"，全文 ≤120 行
- **scripts/ 固定三层**：`cmd/cmd_<verb>.py`（每子命令一个薄壳）+ `core/core.py` + `common/conf.py、log.py`
- 其余目录按 Round 2 勾选创建占位。Skip if skill already exists. Delete the directories the skill doesn't use.

## Step 4: Edit

### Design Patterns

- **Multi-step processes**: See [workflows.md](workflows.md)
- **Output formats/quality**: See [output-patterns.md](output-patterns.md)

### Implementation Order

1. 自底向上：先 `common/`（conf/log 开箱即用），再 `core/`，最后 `cmd/` 薄壳；每层写完实际运行验证
2. 子命令跑通后，把真实参数回填进 SKILL.md 对应 Command 段（只填调用行，不写步骤）
3. Delete unused example files from init
4. SKILL.md 终检：≤120 行，引用的 scripts/references 路径都存在

### Frontmatter Writing

**Must fill the full §2.4.2 template** — field list, formats and examples → See [skill-basics.md](skill-basics.md). Defaults: `version: 1.0.0`, `author: wangjin0115`, `company: cviauto`.

- `name`: skill identifier (hyphen-case, ≤64 chars)
- `description`: PRIMARY trigger. Include what + when to use + boundary. ALL trigger info here, not in body.

## Step 5: Package

```bash
python scripts/package_skill.py <path/to/skill-folder> [output-dir]
```

Auto-validates then creates `.skill` file (zip with .skill extension).

## Step 6: Iterate

1. Use on real tasks
2. Notice struggles
3. Update SKILL.md or resources
4. Test again
