---
version: 2.2.0
author: wangjin0115
company: cviauto
name: jira-commit
description: Git commit automation with JIRA integration. Use when user mentions "commit", "JIRA", "提交代码", "创建任务", or says "把xxx创建一个jira任务" (quick-create a single JIRA task, polishing the user's wording first). Analyzes uncommitted changes, generates JIRA tasks, builds a combined commit message + HTML manual-guide report (git commit/rebase/push are MANUAL, never auto-executed), and manages version tags. Do NOT activate for generic git operations without JIRA context.
---

# jira-commit

## 初始化

```bash
# skill 目录：仓库内 .claude/skills/jira-commit 优先，否则取全局安装位置
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null)/.claude/skills/jira-commit"
[ -d "$SKILL_DIR" ] || SKILL_DIR="$HOME/.claude/skills/jira-commit"

# 输出目录：git 仓库内 → <项目根>/.jira-commit/output（项目本地，用户要求）；
# 仓库外 → 回退 skill 自带 output
PROJECT_ROOT="$(git rev-parse --show-toplevel 2>/dev/null)"
if [ -n "$PROJECT_ROOT" ]; then
    OUTPUT="$PROJECT_ROOT/.jira-commit/output"
else
    OUTPUT="$SKILL_DIR/output"
fi
export JIRA_COMMIT_OUTPUT_DIR="$OUTPUT"
# 报告脚本的 git remote/branch 固定在该根下查询；
# 不设的话脚本从 .claude/skills/jira-commit 运行时会被 .claude 自身 .git 劫持
export JIRA_COMMIT_PROJECT_ROOT="$PROJECT_ROOT"
mkdir -p "$OUTPUT"
```

## 交互入口

`$0` 为空或无法匹配时，用 AskUserQuestion 让用户选择：

| 选项 | 说明 |
|------|------|
| analyze | 扫描未提交文件，AI生成任务 + 规范分析（norm_analysis.json，全部 status=open） |
| preview | 显示tasks.json详情 |
| execute | 前置校验「规范建议全部人工确认」→ 创建JIRA + 生成合并commit/HTML报告（分析结果只读内嵌）+ 飞书邮件通知（**不执行** git commit/rebase/push） |
| norm | 一句规范 → 同步更新 norm_spec.md / 相关 CLAUDE.md / memory 三处 |
| reset | 清理output（产物 + review_* 遗留 + 临时分析文件） |
| tag | 版本打标签 |

**中文别名直入（免菜单）**：参数为下表中文别名时，直接进入对应子命令，不弹选择框：

| 参数 | 子命令 |
|------|--------|
| 分析 | analyze |
| 执行 | execute |
| 规范 | norm |

**自然语言直入（免菜单）**：用户说"把 xxx 创建一个 jira 任务"→ 直接进入 `create` 模式（见命令路由），不弹子命令选择框。

**交互强制规则（新增）**：
- 必须弹出真实 AskUserQuestion 交互，不得根据上下文“猜测”或“默认代选”。
- 不得复用上一轮会话中的选择结果；每次进入都要重新询问。
- 若用户取消交互（cancel/close），立即停止执行，不得继续执行任何子命令。
- 只有收到本轮明确选择后，才允许进入 analyze/preview/execute/reset/tag（create 模式由用户明确措辞触发，等效已确认）。

## 规则

- **禁止自动执行**，必须 `/jira-commit execute` 手动触发
- `config/jira_commit_config.json` 含密码，不提交Git
- **禁止使用绝对路径**，所有 Bash 命令必须使用 `$SKILL_DIR` 相对路径
- 未完成交互选择前，禁止执行任何会修改仓库状态或输出文件的命令

**执行效率硬规则**：
- analyze/preview 阶段优先使用 Read/Grep/Glob/Write，避免长链 Bash。
- 生成 `$OUTPUT/tasks.json` 与 `$OUTPUT/commit_preview.md` 时直接写文件，禁止 heredoc 长命令。
- 单次 Bash 命令控制在 30-60 秒内；超时立即改为更小粒度。
- **diff 一次性原则**：用 `git diff HEAD -- <目录>` 一次拿全部变更，禁止逐文件 diff、禁止先 `--stat` 再分批读。

**路径规则**：
- ✅ 正确：`cd "$SKILL_DIR" && test -f "config/jira_commit_config.json"`
- ❌ 错误：`test -f "D:\项目\绝对路径\.claude\skills\jira-commit\config\jira_commit_config.json"`

## 状态

- **分支**: `!git branch --show-current`
- **未提交数**: `!git status --porcelain | wc -l`
- **最近提交**: `!git log --oneline -3`

## 命令路由

### analyze
→ 流程已在本节完整描述，**默认不读 `docs/cmd_analyze.md`**（仅在遗忘格式细节时按需查阅）。

**强制前置步骤（每次analyze都执行）**：
```bash
# 清空输出 + 校验 config 存在（输出目录 $OUTPUT，仓库内为 .jira-commit/output）
: > "$OUTPUT/tasks.json" && : > "$OUTPUT/commit_preview.md" && : > "$OUTPUT/norm_analysis.json"
test -f "$SKILL_DIR/config/jira_commit_config.json" || echo "CONFIG_MISSING"
```

**config 缺失处理（硬规则）**：
- 前置步骤若输出 `CONFIG_MISSING` → **立即停止 analyze**，不生成任何文件
- 提示用户：
  > ❌ `config/jira_commit_config.json` 不存在，无法分类（commit_types/difficulty_levels/impact_levels 都依赖它）。
  > 请先创建配置文件（含 commit_types/impact_levels/difficulty_levels/due_dates 字段）。

**最小命令集（analyze 阶段仅允许这 4 条，禁止其他）**：
```bash
# 1. 清空输出 + config 存在性校验（前置步骤）
: > "$OUTPUT/tasks.json" && : > "$OUTPUT/commit_preview.md" && : > "$OUTPUT/norm_analysis.json" && (test -f "$SKILL_DIR/config/jira_commit_config.json" || echo "CONFIG_MISSING")

# 2. 拿文件清单
git status --porcelain

# 3. 一次性拿全部 diff（中文路径用目录参数，不逐文件 diff）
git diff HEAD -- <变更所在目录>
```
+ **步骤 4**：`Read config/jira_commit_config.json` —— 拿分类定义（type/difficulty/impact 唯一依据）
+ **步骤 5**：`Read template/labels.md` —— 拿标签词表（labels 唯一依据；表里没有合适词时按「标签选取」规则 4 用 Edit 补词）
+ **步骤 6**：`Read references/norm_spec.md` —— 拿提交规范检查表（N-01~N-18），**同一份 diff 顺手做规范分析**（详见下方「规范分析」）

**分类硬约束**：
- `type` 必须从 `config.commit_types` 选取（feature/bugfix/config/merge/revert，**不含 refactor**）
- `difficulty` 必须从 `config.difficulty_levels` 选取（A/B/C/D）
- `impact`（影响等级）必须从 `config.impact_levels` 选取（S/A/B/C/D）
- 禁止凭直觉/默认值标分类；找不到匹配项 → 停止 + 提示用户更新 config

**任务标题前缀（强制交互，analyze / create 均适用）**：
- 生成 tasks.json **之前**，必须先用 AskUserQuestion 询问任务标题前缀（【】里填什么），禁止猜测、禁止默认代选；用户取消询问则停止
- 用户回答可含多个段，逐段包【】：如回答"yadea_8寸，待审核" → `【yadea_8寸】【待审核】`
- 确认后本轮**所有任务统一**带同一前缀，作用于 `title` / `title_cn` / `commit_message` 首行中文 summary：
  `【yadea_8寸】实现MCU IAP AB分区升级状态机与BootSwap切换`
- 用户明确"无前缀" → 标题不加【】
- 前缀只加任务标题；顶层 `merge_request.title` 不加（用户要求才加）

**显式禁止的命令**（违反即停）：
- ❌ `git log` —— analyze 阶段用不到提交历史
- ❌ `git diff --stat` —— `git status` 已含文件清单
- ❌ `git diff <单文件>` —— 中文路径易失败，且必须一次性看全
- ❌ `ls -la <目录>` —— 不增信息
- ❌ 重复 `git diff` —— 单次 diff 看不全就基于已看到的分析，禁止回头补
- ❌ 默认读 `docs/cmd_analyze.md` —— 本节已自洽

**工具轮次上限**：
- analyze 总工具调用 ≤ 8 次：1 清空+config校验 + 1 status + 1 diff + 1 Read config + 1 Read labels.md + 1 Read norm_spec.md + 3 Write（合并到一轮并行）
- 实际推荐 2 轮：① 前置清空+config校验 + status + diff + Read config + Read labels.md + Read norm_spec.md 并行；② Write tasks.json + Write commit_preview.md + Write norm_analysis.json 并行
- 需要补标签词（Edit labels.md）时额外 +1；仍超 8 次必须停止并复盘，禁止继续补命令

**分析一致性硬规则（新增）**：
- analyze 结果必须仅基于“当前工作区未提交变更”生成。
- 清空输出后，禁止从旧的 `output/tasks.json`、`output/commit_preview.md` 回填任何历史内容。
- 未经用户明确要求，禁止在 analyze 阶段自动标记 `completed=true`。
- 未经用户明确要求，禁止沿用历史 JIRA 号到新任务（**用户自己手动填入 tasks.json 的 `jira_key` 不算**，保留）。
- 若本轮是“全量重新分析”，预览中不得出现“已完成分组”回填内容。
- 禁止沿用旧的 `$OUTPUT/norm_analysis.json`：规范分析必须基于本轮 diff 重新做。

**输出**（同时生成）：
- `$OUTPUT/tasks.json` - jira_key 默认为空 `""`；**顶层必须带 `"generated_at": "YYYY-MM-DD HH:MM:SS"`**（与 tasks 同批写入；execute 门禁用它校验 norm_analysis.json 是否同批产物，缺字段直接 ERROR）
- `$OUTPUT/commit_preview.md` - 人类可读预览
- `$OUTPUT/norm_analysis.json` - 提交规范分析结果（见下方「规范分析」）

**tasks.json 顶层 `merge_request`（analyze 必产，供 execute 生成 MR 文案）**：

除 `generated_at` 与 `tasks` 外，顶层**必须**写入 `merge_request` 对象（AI 按本次 commit 内容浓缩，不是逐任务拼接）：

```json
"merge_request": {
  "title": "[type] 一句话概括本次改动（≤40字，突出主线：改了什么 + 达到什么效果）",
  "description": "## 背景\n- 为什么要改（按影响等级最高的 1~2 条 why，收敛成条目）\n\n## 变更\n- 分主线归纳（非逐任务罗列，同类合并）\n\n## 影响等级\nA\n\n## 测试范围\n1. 按重要性归并去重的测试要点"
}
```

- `title`：一行浓缩，`[type]` 取影响等级最高任务的 type；不要堆括号细节。
- `description`：Markdown，`## 背景` / `## 变更` / `## 影响等级` / `## 测试范围` **四段**。
  **不要写「## 关联 JIRA」段**：analyze 阶段 `jira_key` 必为空（下方硬规则），写出来只能是
  `AERDM-xxxxx` 这类占位符；该段由 execute 的 `generate_report.py` 按各任务真实 `jira_key` 追加
  （AI 文本若已带该段会被剥掉重写，无真号则整段删除）。
- execute 的 `generate_report.py` 优先读该字段；**缺失才走规则兜底**（兜底文案质量明显较低，务必写入）。

**tasks.json 字段要求（每个任务必须完整，缺失会导致 preview/execute/create_jira 脚本报错）**：

| 字段 | 含义 | 约束 |
|------|------|------|
| `id` | 任务序号 | 从 1 递增 |
| `title` | 中文标题 | 首行去掉 `[type][JIRA-ID]` 后的 `【前缀】中文 summary`，脚本展示兜底用 |
| `title_cn` | 中文标题 | **必须生成**，与 `title` 同源，含统一【前缀】；JIRA summary 与 preview 展示用 |
| `type` | 类型 | 必须来自 config.commit_types |
| `difficulty` | 难度 | 必须来自 config.difficulty_levels（A/B/C/D） |
| `impact` | 影响等级 | 必须来自 config.impact_levels（S/A/B/C/D） |
| `labels` | JIRA 标签 | 数组，**≤3** 个，取自 `template/labels.md` 的模块类/现象类（**不打 `已分析`**）；见下方「标签选取」 |
| `dirs` | 变更目录列表 | 数组（preview_tasks.py 强制要求 `task['dirs']`，缺失即 KeyError） |
| `git_add_pattern` | git add 匹配串 | 空格分隔文件/目录路径；execute 执行 `git add <pattern>`，缺省为 `.` 会全量 add，**禁止缺省** |
| `files` | 涉及文件清单 | 数组，便于人工核对 |
| `jira_key` | JIRA 号 | 必须为空字符串 `""` |
| `completed` | 完成标记 | 必须为 `false` |
| `commit_message` | 完整提交消息 | 见下方格式要求 |

```json
示例（每任务结构）：
{
  "id": 1,
  "title": "【项目名】板级上电时序重构",
  "title_cn": "【项目名】板级上电时序重构",
  "type": "feature",
  "difficulty": "D",
  "impact": "B",
  "labels": ["电源管理", "上下电时序"],
  "dirs": ["CVI_McuPlatform/L4_Service/Service_Board"],
  "git_add_pattern": "CVI_McuPlatform/L4_Service/Service_Board/Service_Board.c",
  "files": ["CVI_McuPlatform/L4_Service/Service_Board/Service_Board.c"],
  "jira_key": "",
  "completed": false,
  "commit_message": "[feature][JIRA-ID]【项目名】板级上电时序重构\n\n[what]\n1. 具体变更项\n\n[why]\n原因（中文）\n\n[how]\n思路（中文）\n\n[影响等级]B\n\n[建议测试范围]\n测试要点（中文）"
}
```

`commit_preview.md` 生成规则（新增）：
- 预览内容必须直接来源于 `tasks.json` 的 `tasks[].commit_message`。
- 每个任务必须展示完整 `commit_message` 原文，不得改写为“目录/重点/摘要”。
- 允许保留任务ID与标题用于导航，但不得修改 `commit_message` 文本。

**标签选取（每个任务必做）**：

词表唯一来源是 `template/labels.md`（用 Read 工具读；它是明文）。给每个任务选 `labels`：

1. **只选表内词**。模块类优先于现象类 —— 能定位到具体模块（如 `电源管理`、`CAN通信`）就选模块；
   定位不到才退而选现象（如 `偶发难复现`）。
2. **数量 ≤3**（优先 1 个模块 + 1 个现象；判不出来就打 1 个模块标签）。**不打 `已分析`**
   —— 那是 `jira-ticket-analysis` 给缺陷分析子任务的标记，本流程不用。
3. 标签不能含空格、逗号、分号。
4. **表里找不到合适的词 → 用 Edit 工具往 `template/labels.md` 的「模块类」或「现象类」小节补一行**
   （三列「标签 / 用途 / 典型触发关键词」都要填），再用这个词。**不要打 `待归类`**，也不要把
   表外词直接写进 `tasks.json`。补词后要在汇报里说明"已扩充 labels.md：+xxx"。
5. `labels` 是 JIRA 元数据，**不写进 `commit_message`**。

**规范分析（analyze 阶段必做，与生成任务同批完成）**：

分析对象 = **同一份 diff**（步骤 3 已一次性拿到的 `git diff HEAD -- <变更所在目录>`），
依据 = 步骤 6 读到的 `references/norm_spec.md` 检查表 N-01~N-18。
**只查规范/分层/命名，不查代码逻辑缺陷**（逻辑问题走 AI 代码审核，不走本流程）。

- 逐条对照 N-01~N-18，命中即产出一条建议；无违规则 `suggestions: []`
- severity 取 `error` / `warn` / `info`，与 norm_spec 检查表一致
- `file` 用仓库相对路径（与 tasks.json 的 files 写法一致）
- 结果写入 `$OUTPUT/norm_analysis.json`：

```json
{
  "readme": "人工处理：按建议改完代码后把该条 status 改为 \"checked\"；认为建议不对则从 suggestions 删除该条，并运行 /jira-commit norm 同步规范（norm_spec.md / CLAUDE.md / memory）。全部 status=checked（或数组删空）后才能 execute。",
  "analyzed_at": "2026-09-22 15:04:00",
  "base": "git diff HEAD -- <变更所在目录>",
  "files": ["<本次分析覆盖的文件，取自 diff 文件清单（仅记录，不参与 execute 校验）>"],
  "suggestions": [
    {"id": "S01", "rule": "N-04", "severity": "error", "title": "跨层 include 非 UpInf",
     "detail": "违反事实", "suggestion": "怎么改", "file": "相对路径",
     "status": "open"}
  ]
}
```

**为什么在 analyze 做**：analyze 本来就要读完本次 diff，多对照一份 norm_spec 是零边际成本；
execute 不重复分析——`generate_report.py` 入口校验该文件（不合法直接 `[ERROR]` 退出，HTML 都不生成），
合法则把结果**内嵌**进 commit_report.html（见 execute 步骤 3）。

**files 字段语义**：`files` 只记录本次分析覆盖的文件（≈ tasks.json 各任务 `files` 的并集；
按「特殊处理」排除的 MDK/build.log 等不入 commit 的文件不计入），**供人核对，不参与 execute 校验**。
analyze 之后用户改文件（增/删/改内容）**不需要重新分析**：规范分析针对的是分析时那份 diff；
execute 入口校验只看「文件存在且含 suggestions 数组」，通过即内嵌 HTML。

**生成后强制自检（必须执行）**：
生成 `output/tasks.json` 与 `output/commit_preview.md` 后，**必须立即执行以下自检**，不得跳过：

0. **tasks.json 字段自检**：
   - 每个任务必须包含 `title`（中文）、`title_cn`（中文）、`dirs`（数组非空）、`git_add_pattern`（非空字符串）
   - 缺失或为空 → 立即补全后重写文件

0.2 **前缀自检**：
   - 所有任务的 `title`/`title_cn` 必须带**同一个**【前缀】（用户选"无前缀"则都不带）
   - 任一任务缺失前缀或前后不一致 → 立即修正后重写文件

0.3 **merge_request 自检**：
   - 顶层 `merge_request` 必须存在，且 `title`（非空一句话）与 `description`（含 `## 背景/## 变更/## 影响等级/## 测试范围` 四段）均非空
   - `description` **不得含「## 关联 JIRA」段或 `AERDM-xxxxx` 之类占位符** → 有则删除：
     该段由 execute 的脚本按真实 `jira_key` 追加，analyze 写不出真号
   - `title` 为中文一行浓缩（可带 `[type]` 前缀），`description` 为 Markdown；缺任一 → 立即补写后重写文件

0.5 **标签自检**：
   - 每个任务的 `labels` 必须是非空数组、数量 ≤3、**不含 `已分析`**
   - 每个标签都必须能在 `template/labels.md` 里找到；有表外词 → 要么改回表内词，要么按
     「标签选取」规则 4 补进 labels.md（补了词要说明）

0.7 **规范分析自检**：
   - `norm_analysis.json` 必须存在且含 `suggestions`（可为空数组）与 `files`
   - 每条建议必须有 `id`/`rule`/`severity`/`title`/`file`/`status`，且 `severity ∈ error|warn|info`、`status ∈ open|checked|deleted`（analyze 生成时**显式写 `"status": "open"`**；checked/deleted 只能由**人工编辑该文件**产生——页面只读不回写）
   - `files` 记录本次分析覆盖的文件（≈ diff 涉及源文件，排除不入 commit 的生成物）
   - 缺失或不合规 → 立即重写；**不得留空文件**（空文件 JSON 解析失败，execute 会 `[ERROR]` 退出不生成报告）

1. **读取 tasks.json 自检**：
   - **agent 不得预填 JIRA 号**：analyze 生成任务时 `jira_key` 一律空字符串 `""`
   - **用户手动填入的 `jira_key` 合法**——保留不动（execute 建单时自动跳过已有关键的任务，
     不重复创建，只把任务内容追加到该工单描述；HTML/preview/commit 首行照常显示该 jira id）
   - 分不清是谁填的 → 按 agent 填的处理：清空并说明，让用户自行补
   - 所有任务的 `completed` 必须为 `false`（未经用户明确要求不得标记完成）
   - 若发现 `completed=true`，立即修正为 `false` 并在报告中说明

2. **内容语言自检**：
   - `commit_message` 首行标题必须为中文（`[type][JIRA-ID]【前缀】中文标题`，如 `[feature][JIRA-ID]【项目名】实现SN码`）
   - `commit_message` 的 `[what]` 段落必须为中文（禁止英文）
   - `commit_message` 的 `[why]` 段落必须为中文（可选，但存在时必须是中文）
   - `commit_message` 的 `[how]` 段落必须为中文（可选，但存在时必须是中文）
   - `commit_message` 的 `[建议测试范围]` 段落必须为中文
   - 仅 `[type]`（和 `[JIRA-ID]`）标记允许非中文；标题正文与全部内容一律中文
   - 若发现英文标题或英文内容，立即修正为中文并重写文件

3. **文件一致性自检**：
   - 统计 `tasks.json` 的任务总数
   - 统计 `commit_preview.md` 的任务块数量（通过 `## 任务 X:` 计数）
   - 两者必须完全一致，否则说明生成遗漏
   - 检查 `commit_preview.md` 每个任务块是否包含对应任务的**完整** `commit_message` 原文
   - 不得省略、不得改写为摘要

4. **自检失败处理**：
   - 若发现任何不一致，**立即修正**（重写 `tasks.json` 和 `commit_preview.md`）
   - 修正后再次自检，直到完全通过
   - 向用户汇报时说明："✅ 已通过自检：任务数一致、内容为中文、无意外 completed 标记"

**自检执行时机**：
- 在 Write `tasks.json` 和 `commit_preview.md` 之后立即执行
- 在向用户汇报 analyze 结果之前必须完成自检
- 不得先汇报再自检，不得跳过自检

**完成通知（必须执行）**：
analyze 自检通过后，发飞书邮件（lark-cli；收件人自动取当前飞书账号邮箱，抄送取 config.notification.email_cc）：
```bash
python "$SKILL_DIR/script/send_mail.py" analyze "jira-commit 分析完成" "已生成 N 个任务，预览见 commit_preview.md"
```
（N 为任务数；正文附 tasks.json 任务清单表；发送失败仅 WARN 不中断，脚本内部已处理）

**commit_message格式要求**：
```
[type][JIRA-ID]【前缀】中文 summary

[what]
1.具体变更项1
2.具体变更项2

[why]
原因说明（可选，中文）

[how]
实现思路（可选，中文）

[影响等级]S|A|B|C|D

[建议测试范围]
测试要点（中文）
```

---

**⚠️ 重要格式警告（违反将导致提交被拒）⚠️**

- **标题**: 【前缀】中文 summary（如 `[feature][AERDM-63016]【项目名】优化电源管理时序`；禁止纯英文标题）
- **内容**: 中文 what/why/how/建议测试范围（禁止英文）

**错误示例** ❌:
```
[feature][AERDM-63016]Add FreeRTOS recursive mutex  ← 英文标题，错误！
[what]
1. Service_Nvm: Add FreeRTOS recursive mutex protection  ← 英文内容，错误！
```

**正确示例** ✅:
```
[feature][AERDM-63016]【项目名】新增FreeRTOS递归互斥锁保护  ← 中文标题，正确！
[what]
1.实现NVM模块线程安全保护（FreeRTOS递归互斥锁）  ← 中文内容，正确！
```

---

- 标题：中文
- 内容：中文（what/why/how/建议测试范围）
- jira_key：agent 生成时必须空 `""`（不预填）；**用户手动填入的保留**（execute 跳过创建该单、照常显示）

### preview
```bash
python "$SKILL_DIR/script/preview_tasks.py"   # 输出目录由 JIRA_COMMIT_OUTPUT_DIR 决定
```

### execute
→ 读取 `docs/cmd_execute.md` 获取详细步骤

**已禁用 git commit/rebase/push**——execute 只做：**入口校验规范建议全部人工确认** → 创建 JIRA → jira_id 写入 commit_message → 生成**合并 commit** 与 HTML 报告（分析结果只读内嵌，无服务）→ 飞书邮件通知（lark-cli）。git 操作全部手动（指引见 commit_report.html）。

核心调用：
```bash
python "$SKILL_DIR/script/generate_report.py" --check-norm   # 0. 前置门禁：规范建议全 checked 才继续（错误即停，不建单）
python "$SKILL_DIR/script/create_jira_tasks.py"   # 1. 创建JIRA，jira_id 写回 commit_message（输出目录由 JIRA_COMMIT_OUTPUT_DIR 决定；脚本入口自带规范门禁硬校验——建议未全部确认/产物缺失即退出，一条 JIRA 都不建）
python "$SKILL_DIR/script/generate_report.py"     # 2. 再次校验门禁 → 合并commit → commit_report.html（只读内嵌）→ 飞书邮件
```

**步骤 0：前置门禁（在创建 JIRA 之前）**

`--check-norm` 只校验不产出：规范建议未全部人工确认（有 `status != "checked"`）→ `[ERROR]` 退出，
**不创建 JIRA**；用户按提示处理完（改代码+编辑 status，或删建议+`/jira-commit norm`）再重跑 execute。

**步骤 3：generate_report 入口硬门禁（无服务，无页面交互）**

`generate_report.py` 一上来校验 `$OUTPUT/norm_analysis.json`，两道任一不过**直接 `[ERROR]` 退出，HTML 都不生成**：

1. **结构**：缺失 / 空文件 / JSON 损坏 / 缺 `suggestions` 键 → 提示重跑 analyze
2. **人工确认完成**：每条 suggestion 的 `status` 必须为 `checked`——
   - 未确认（open 等）→ 报「未确认: S01, S02...」退出，并打印人工处理指引
   - 空 `suggestions: []` 合法（无违规 / 建议全部被删）

**人工处理规范建议的流程**（agent 在 analyze 结束时告知用户，报告页面也有同样提示）：

- **认可建议** → 按建议改代码，然后**人工编辑** `$OUTPUT/norm_analysis.json`，把对应建议的
  `"status": "open"` 改为 `"status": "checked"`
- **认为建议不对**（规范本身过时/有误）→ **从 suggestions 数组删除该条**，并运行
  **`/jira-commit norm`** 交互（见下节）同步更新规范，让下轮 analyze 不再报同类建议
- 全部处理完（剩的都是 checked 或数组已删空）→ 重跑 execute 放行

校验通过 → 分析结果**只读内嵌** `commit_report.html`（每条显示 ID+严重度+规则+标题；无勾选/删除/编辑、无置灰门禁，全部操作按钮可用），浏览器 file:// 双击打开。

**用户侧流程**（HTML 有指引）：浏览器打开 commit_report.html →
第 1 张卡片看规范分析快照（只读）→ 第 2 张卡片手动 git 提交 push → 第 3 张 JIRA 打待验证 →
**第 4 张复制 MR 标题/描述并提 MR**（标题/描述来自 `tasks.json` 顶层 `merge_request`，缺失走规则兜底）→
第 5 张「一键复制」分析结果 + 打开本分支提交列表（`/-/commits/<分支>`，点顶端 commit），**手动粘贴为评论** →
第 6 张按需打 tag。

**标签行为**（`tasks[].labels`，来自 analyze 的标签选取）：
- **新建**的 JIRA 工单：标签随建单 payload 一起落盘（`fields.labels`）
- **已有 jira_key** 的工单：**不补打标签**，标签只留在 `tasks.json` / HTML / preview 本地
  （存量工单不去改，除非用户明确要求补）
- 无 `labels` 字段的老任务：payload 里不带 `labels` 键，行为与改动前一致

**输出**：
- `commit_preview.md` - 合并后的单次 commit 消息：首行 `[type][jira1][jira2]... N commits`（**N commits 为固定英文后缀，勿汉化**），后接各任务 `[type][jira]中文标题` + what/why/how/影响等级/建议测试范围；**任务头一律用中文标题（title_cn），jira id 缺失时写占位 `jira#`**（如 `[feature][jira#]中文标题`）（整体使用，勿拆成单个提交）
- `commit_report.html` - 手动指引 + 规范分析报告（**6 张卡片，只读，无服务、无置灰**）：①提交规范分析结果（analyze 产物快照；**每条显示 ID+严重度+规则+标题**，完整 detail/suggestion 由「一键复制」输出）②手动提交和 push（commit 内容可编辑+复制+下载+同步 md）③JIRA 打待验证（id 可点跳转+标签胶囊；**用户手动填的 jira_key 照常显示**）④GitLab 提 merge（**显示 MR 标题与描述，可点击复制/一键复制/下载 merge_request.md**）⑤给 commit 添加评论（「一键复制」分析结果按点分条 + 跳转本分支最新 commit 页手动粘贴）⑥手动打 tag
- `merge_request.md` - MR 标题 + 描述（与卡片④一致，供复制/下载）；标题/描述来自 `tasks.json` 顶层 `merge_request`，缺失时按任务清单规则兜底（影响等级排序取样本 + 测试范围归并重编号）

**execute_commit.py 已禁用**：旧 commit/rebase/push 逻辑整体**注释保留**在该文件内（不删除），文件现已转发到 generate_report.py，不再执行任何 git 操作。

execute前必须 AskUserQuestion 确认。JIRA未配置时也要 AskUserQuestion 让用户选择如何处理。

### create（快捷创建单个 JIRA）
触发：用户说"把 xxx 创建一个 jira 任务"（免子命令菜单，直接进入）：

0. **问前缀（必须）**：AskUserQuestion 询问任务标题【】前缀，规则同 analyze 的「任务标题前缀」
1. **润色（必须）**：把用户的话稍作优化——整理成规范中文标题（`title` / `title_cn` 同源中文，含统一【前缀】）、简要 `[what]` 描述；保持原意，不扩写
2. **生成单任务 tasks.json**（按上方 analyze 的 schema；`type`/`difficulty`/`impact` 从 config 选取，拿不准时 AskUserQuestion 问用户；`labels` 按「标签选取」从 `template/labels.md` 选（≤3，不打 `已分析`，表里没有就补词）；`jira_key=""`、`completed=false`、`dirs`/`git_add_pattern` 可填当前仓库根 `.`）；**同时生成空 suggestions 的 `$OUTPUT/norm_analysis.json`**（`analyzed_at` 与 tasks.json `generated_at` 同批时间）——建单脚本入口有规范门禁，缺该文件会直接拒绝创建
3. **创建**：
```bash
cd "$SKILL_DIR" && python script/create_jira_tasks.py
```
4. **汇报**：返回 JIRA ID 与链接（`{jira_url}/browse/{key}`）

注意：create 模式只创建 JIRA，不生成 commit、不发邮件通知。

### norm（一句规范 → 三处同步）

**触发**：用户说「service 不能跨层调用 app」「规范更新：函数名前缀必须带模块名」「这条规范不对，改成 xxx」这类**规范级表述**，或明确说 `norm` / `规范` 子命令。

**做什么**：把用户给的一条规范，同步落到**三个地方**，保证 agent 行为、代码文档、检查表永远一致：

1. **`references/norm_spec.md`**（检查表唯一依据）——
   - 已有对应条目（N-01~N-18 或分层总则）→ 用 Edit 修改该条
    - 没有对应条目 → 在「四、检查规则表」**新增一行**（Rule ID 顺延 N-17、N-18、N-19...，定名称/层/严重度/检查方法）
2. **相关 CLAUDE.md**——规范涉及的层/模块文档同步：
   - 分层/依赖类规范 → 根 `CLAUDE.md` 或 `CVI_McuPlatform/CLAUDE.md` 的分层约定段
   - 模块级规范（如 Service_Debug 的日志规则）→ 对应模块 `CLAUDE.md` 的规则/Gotchas 段
   - 用 Grep 找到提及相关规则的 CLAUDE.md 再改，**不要盲改所有 CLAUDE.md**
3. **memory**（Claude 工程 memory，`~/.claude/projects/<工程slug>/memory/`）——
   写一条 `jira-commit-norm-<主题>.md`：frontmatter（name/description/metadata.type=norm）+ 正文
   （规范原文 + 落点清单 norm_spec 条目号/CLAUDE.md 路径）。写不进去（沙箱禁写）→
   落 `tmp/memory-pending/` 并明确告知用户手动复制（工程已知限制，见 .claude-md-map/ledger.md）。

**流程**：
1. 复述规范给用户确认（一句中文 + 影响的检查条目/严重度建议）——拿不准 severity 就问
2. Edit norm_spec.md（改/增条目）
3. Grep 定位相关 CLAUDE.md → Edit
4. 写 memory（或落 tmp 并告知）
5. 汇报三处落点（文件+行号级），提醒：**本轮 norm_analysis.json 里因旧规范产生的建议，
   认可删除即可，不需要重新 analyze**（规范已更新，下轮 analyze 自动按新表）

**边界**：norm 只改规范三件套，**不改业务代码、不改 tasks.json/norm_analysis.json**；
用户想连代码一起改，那是普通编码请求，走正常编辑流程。

### reset
```bash
rm -f "$OUTPUT/tasks.json" "$OUTPUT/jira_tasks_result.json" "$OUTPUT/commit_preview.md" "$OUTPUT/norm_analysis.json" "$OUTPUT/commit_report.html" \
      "$OUTPUT/review_fingerprint.json" "$OUTPUT/review_server.json" "$OUTPUT/review_suggestions.json" "$OUTPUT/review_request.json"
# 孤儿文件：历史评审/分析残留（旧 review_server.py 时代的指纹、临时分析产物）
rm -rf "$OUTPUT"/_norm "$OUTPUT"/_*.json "$OUTPUT"/_*.txt
```

- `commit_report.html` 属于过期报告，一并清；`review_*` 为已删除的评审服务遗留；`_norm/`、`_*.json`、`_*.txt` 是历轮临时分析产物。
- 只清 `$OUTPUT` 内内容，不动 `.jira-commit/e2e_sandbox/`（自测沙箱，独立目录）。

### tag
检测 `L6_Public/inc/Public_Project.h` 的 `SOFTWARE_VERSION` 变化，变化则 commit + push + tag。
