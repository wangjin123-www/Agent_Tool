# Design Principles

## Interactive Skill Pattern

For skills with multiple operations, use `argument-hint` + AskUserQuestion routing:

**1. Set `argument-hint` in frontmatter:**
```yaml
argument-hint: analyze|preview|execute|reset
```

**2. Route in SKILL.md body:**
```markdown
## Entry
`$0` is empty or unmatched → AskUserQuestion with menu.

| Option | Description |
|--------|-------------|
| analyze | Scan files, generate tasks |
| preview | Show task details |

## Command: analyze
→ Read `docs/cmd_analyze.md` for detailed steps
```

**3. Create per-command docs** — only loaded when selected.

Benefits: SKILL.md stays minimal, each command isolated, token usage scales with usage.

## Token Optimization

| Strategy | Bad | Good |
|----------|-----|------|
| Extract code | 50-line bash in SKILL.md | `python scripts/do_it.py` |
| On-demand loading | All instructions in SKILL.md | `→ Read docs/cmd_x.md` |
| Minimize injection | `!git status` in SKILL.md | Run explicitly when needed |
| Config dedup | Values in SKILL.md + config/ | `source scripts/init_env.sh` |

Scripts execute without loading into context, saving tokens every invocation.

## 路由决策：脚本优先，参考次选

生成的 SKILL.md 里每个 Command 段固定两行路由——首选脚本调用，次选 reference：

| 动作特征 | 落点 | SKILL.md 写法 |
|----------|------|---------------|
| 相同输入必得相同输出（编译/校验/转换/收发/打包） | `scripts/cmd/cmd_<verb>.py` | `python scripts/cmd/cmd_<verb>.py ...` |
| 固定流程含少量分支 | 脚本为主 | 同上，另加次选 `Read references/<verb>.md` |
| 纯知识/规范/schema，需 Claude 读后思考 | `references/<verb>.md` | `Read references/<verb>.md` |

口诀：**每次都一样 → 脚本；每次要现想 → 参考**。两者都不满足才允许在 SKILL.md 里写步骤，且 ≤10 行。

## scripts/ 固定分层架构

init 脚手架固定生成三层，不改层名、不增顶层目录：

```
scripts/
├── cmd/            # 入口层：一个子命令一个文件，薄壳 ≤100 行
│   └── cmd_<verb>.py
├── core/           # 业务层：实际逻辑，被 cmd 调用，可复用
│   └── core.py
└── common/         # 公共层
    ├── conf.py     # 读 config/config.conf（绝对路径只放这里）
    └── log.py      # 强制 UTF-8 输出
```

| 层 | 职责 | 禁止 |
|----|------|------|
| cmd | 参数解析、调 core、退出码与打印 | 写业务逻辑 |
| core | 业务实现，可被多个 cmd 复用 | import cmd；出现绝对路径 |
| common | conf 读配置、log 统一输出 | 出现业务名词 |

依赖单向 `cmd → core → common`（cmd 亦可直接用 common），禁止反向与跨层。新增子命令 = 新增 cmd 薄壳 + core 加函数，结构不变。

## Security

- `allowed-tools`: Specify minimum required tools
- `.gitignore`: Must include `output/` and config with secrets
- Config templates: Provide `*_example.conf`, gitignore actual config
- Confirmation gates: Use AskUserQuestion before destructive operations
