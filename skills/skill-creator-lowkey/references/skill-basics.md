# Skill Basics

## What Skills Provide

1. Specialized workflows - Multi-step procedures for specific domains
2. Tool integrations - Instructions for working with specific file formats or APIs
3. Domain expertise - Company-specific knowledge, schemas, business logic
4. Bundled resources - Scripts, references, and assets for complex and repetitive tasks

## Core Principles

### Concise is Key

The context window is a public good. Skills share the context window with everything else Claude needs.

**Default assumption: Claude is already very smart.** Only add context Claude doesn't already have.

Prefer concise examples over verbose explanations.

### Set Appropriate Degrees of Freedom

**High freedom (text-based instructions)**: Multiple approaches valid, decisions depend on context.
**Medium freedom (pseudocode or scripts with parameters)**: Preferred pattern exists, some variation acceptable.
**Low freedom (specific scripts, few parameters)**: Operations fragile and error-prone, consistency critical.

## Anatomy of a Skill

采用 **YAML Frontmatter + Markdown Body** 格式：

```
my-skill/
├── SKILL.md        # 必需：技能定义（frontmatter + 指令正文）
├── references/     # 可选：参考文档（规范、技术主题，实现【渐进式披露】）
├── config/         # 可选：配置文件（绝对路径等放这里，运行时读取）
├── templates/      # 可选：输出模板（空骨架和积木，从模板开始工作）
├── assets/         # 可选：资源文件（图片等）
├── scripts/        # 可选：辅助脚本（validate.py、process.sh 等）
├── example/        # 可选：示例输入和成品输出
├── output/         # 输出文件（gitignore）
├── docs/           # 可选：附带文档
├── utils/          # 可选：相关外部工具
├── README.md
├── .gitignore
└── LICENSE         # 许可证
```

### SKILL.md Frontmatter

```yaml
---
version: 2.0.7
author: wangjin0115
company: cviauto
name: my-skill-name
description: "Skill 的触发描述，决定何时被调用"
category: development         # 分类
argument-hint: analyze|preview|execute|reset|tag|help
allowed-tools: [Bash, Read, Write, AskUserQuestion, Grep, Glob]
context: project
tags: [git, jira, commit, automation]
license: Complete terms in LICENSE.txt
---

# Skill 的核心指令

## Overview
功能概述...

## Instructions
具体执行指令...
```

**核心字段说明**：

| 字段              | 作用                                         | 要求 |
|-----------------|--------------------------------------------|------|
| `name`          | Skill 的唯一标识符 | 小写字母、数字和连字符，最多 64 字符，如 `pdf-editor`；不能用下划线、XML 标签或 `anthropic`/`claude` 等保留词。API/平台规范必填；Claude Code 中 frontmatter 可省略，`name` 默认取目录名 |
| `description`   | **最关键字段：决定 Skill 何时被触发** | 详细描述能力、触发场景、边界条件 |
| `version/author/company` | 版本与归属信息 | 可选 |
| `license`       | 许可证信息 | 可选 |
| `category`      | 分类标签，UI 中分组展示（Claude Code 扩展字段） | 可选，字符串 |
| `argument-hint` | 参数提示，显示在斜杠命令自动补全中 | 可选，如 `"<file_path> [--verbose]"` |
| `allowed-tools` | 限制执行期间可用的工具 | 可选，逗号分隔，如 `Read, Grep, Bash`；未指定则继承全部。等效别名 `tools`（Claude Code 旧写法），校验器两者均接受 |
| `context`       | 加载方式：`pull`（默认，按需激活）或 `push`（始终注入） | 可选，规范类 Skill 用 `push` |
| `tags`          | 附加标签，便于组织和搜索 | 可选，YAML 列表 |

> API/平台规范中 `name` 和 `description` 是触发判断的核心输入，正文只在 Skill 激活后才读取。Claude Code 另有 `when_to_use`、`disable-model-invocation`、`user-invocable`、`paths` 等扩展字段。

### Description 编写指南

❌ 弱 Description（太模糊，Claude 不知道何时该用）：

```
This skill helps with PDFs and documents.
```

✅ 强 Description（能力 + 触发场景 + 边界）：

```
Comprehensive PDF manipulation toolkit for extracting text and tables,
creating new PDFs, merging/splitting documents, and handling forms.
When Claude needs to fill in a PDF form or programmatically process,
generate, or analyze PDF documents at scale. Use for document workflows
and batch operations. Not for simple PDF viewing or basic conversions.
```

强版本三要素：
- **具体能力**：extract, create, merge, split, handle forms
- **触发场景**：fill in forms, batch operations
- **明确边界**：not for simple viewing（何时**不**该用）

### Bundled Resources

| Dir | Purpose | When to include |
|-----|---------|----------------|
| `scripts/` | Deterministic, repeatedly rewritten code | Same code rewritten each time |
| `references/` | On-demand docs for Claude's thinking | API docs, schemas, policies |
| `assets/` | Files used in output (templates, images) | Need files in final output |
| `config/` | Machine/project-specific settings | Tool paths, device settings |
| `output/` | Runtime artifacts (always gitignored) | Logs, build results |

### What NOT to Include

No CHANGELOG, INSTALLATION_GUIDE, or unused auxiliary docs. Only essential files plus README.md / LICENSE / docs/ when they carry real content.

## Progressive Disclosure

Three levels:
1. **Metadata** (always in context, ~100 words)
2. **SKILL.md body** (when triggered, <500 lines)
3. **Bundled resources** (as needed, unlimited)

### Patterns

**Pattern 1: High-level + references**
```markdown
## Advanced features
- **Form filling**: See [FORMS.md](FORMS.md)
- **API reference**: See [REFERENCE.md](REFERENCE.md)
```

**Pattern 2: Domain-specific files**
```
skill/
├── SKILL.md (router)
└── references/
    ├── domain-a.md
    └── domain-b.md
```

**Pattern 3: Conditional details**
```markdown
For tracked changes: See [REDLINING.md](REDLINING.md)
For OOXML details: See [OOXML.md](OOXML.md)
```

Guidelines:
- Keep references one level deep from SKILL.md
- Files >100 lines: add table of contents at top
