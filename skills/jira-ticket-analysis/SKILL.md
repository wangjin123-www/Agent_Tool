---
name: jira-ticket-analysis
description: >-
  拉取 Jira 工单（名下未关闭）→ 下载并解析附件（截图 / CAN BLF / 5AA5 串口日志）→ 取对应 GitLab 分支代码到工具自有工作区
  → 结合 CLAUDE.md 分层文档做单票隔离分析 → 产出问题分析+解决计划 → 邮件发我审核。触发词：「分析工单」「跑工单分析」「工单分析
  LH2512024-5408」「看下我的工单」。
author: luziyu
version: 0.0.2
---

# jira-ticket-analysis

把「翻 Jira → 下附件 → 解日志 → 对照代码 → 写分析」这条人工链路做成流水线。
**每单一个隔离 subagent**，避免上下文爆炸与跨单污染。

**自包含**：外部工具（jira-tool / frame_extractor / AI_canlog / claude-md-map）都以源码形式
内嵌在 `vendor/` 下，路径全部相对工具目录解析。整个目录可以 zip 走、解压到任意位置就能跑，
不依赖任何工具目录之外的东西。

## 环境（唯一入口）

```bash
./jtat.cmd validate          # Windows 启动器，自己解析工具目录与 .venv
./jtat.cmd run --keys LH2512024-5408
```

`jtat.cmd` 等价于下面这条（非 Windows 或想手工调用时用）：

```bash
TOOL="<本工具所在目录>"       # 解压到哪就是哪，不用改配置
"$TOOL/.venv/Scripts/python.exe" "$TOOL/scripts/jtat.py" validate
```

所有步骤都用工具自带的 `.venv`（自包含，与系统环境隔离）。

> **首次使用**：分发包不含 `.venv`，先建一次：
>
> ```bash
> uv venv --python 3.12 "$TOOL/.venv"
> uv pip install --python "$TOOL/.venv/Scripts/python.exe" -r "$TOOL/requirements.txt"
> ```
>
> 再配 Jira 凭据（见下方「配置」）。

## 使用流程（TL;DR）

```bash
./jtat.cmd validate                  # 0. 环境自检（首次或环境变动后）
./jtat.cmd all --keys <KEY>          # 1. 拉单+解析+取码+组装（--keys 省略则按 JQL 拉全部）
                                     #    输出会提示：几单已就绪、worker_prompt 路径
# 2. 【Claude 会话动作】按上面提示，对每单派一个 subagent（prompt 取 worker_prompt.md）
./jtat.cmd summary --date <日期>     # 3. 汇总（从 receipt 生成 SUMMARY.md）
./jtat.cmd mail-only --date <日期>   # 4. 发邮件
./jtat.cmd feedback --date <日期>    # 5. 回写：建子任务 + 报告挂附件 + 打标签（先 dry-run）
./jtat.cmd feedback --date <日期> --apply   #    确认后加 --apply 实跑
./jtat.cmd labels                    #    随时看标签表里有哪些词可选
```

### 0. 首次：自检

```bash
./jtat.cmd validate
```

会检查：venv 依赖、Jira 探活、GitLab PAT 与各工程可达性、`vendor/` 内嵌工具、目录可写、DBC 目录。
**任何一项 ✗ 都要先修**，别往下跑。

### 1. 拉工单 + 解析附件 + 取代码 + 组装输入包

```bash
./jtat.cmd run                      # 按 config.jira.jql 拉（默认名下未关闭单）
./jtat.cmd run --keys LH2512024-5408   # 只跑指定单
./jtat.cmd list                     # 先看看有哪些单，不下载
```

产出在 `<工具目录>/workspace/out/<日期>/<KEY>/`：
`ticket.md` `attachments/` `evidence/` `bundle.md` `worker_prompt.md`

### 2. 派发隔离 subagent（本 skill 的核心动作）

`run` 完成后，**你（Claude）要按 `prompts/orchestrator.md` 执行**：

1. 读 `out/<日期>/_assignments.json` 与各单 `ticket.md` 前 80 行，
   对照 `config.json` 的 `projects[].desc`，**逐单判断工程归属**并把判断回写进 `_assignments.json`。
2. 若判断结果与占位不同，重跑 `./jtat.cmd prepare --date <日期>` 以按新归属取代码。
3. 对每单，**用 Agent 工具派一个 `general-purpose` subagent**，
   prompt 直接取该单的 `worker_prompt.md` 全文。
   - **一次一票，顺序执行**，不要并发。
   - 单票失败不中断，记下原因继续下一单。
4. subagent 会写 `analysis.md` 与 `receipt.json`。

**你绝对不要读** `_frames.jsonl`、`evidence/INDEX.md` 全文或大附件 —— 那是 subagent 的活。
你只读各单 `receipt.json`。

### 3. 汇总与发邮件

```bash
./jtat.cmd mail-only --date <日期>            # 真发
./jtat.cmd mail-only --date <日期> --dry-run  # 只看命令不发送
```

### 4. 回写到 Jira（建子任务，父单不动）

```bash
./jtat.cmd feedback --date <日期>              # dry-run：只打印将写什么
./jtat.cmd feedback --date <日期> --apply      # 实跑
./jtat.cmd feedback --date <日期> --force      # 台账里已成功的单也重写
./jtat.cmd feedback --date <日期> --subtask-type 子任务   # 覆盖子任务类型
```

每张工单产出**一个子任务**，父单完全不动：

| 落点 | 内容 |
| ---- | ---- |
| 子任务 summary | `【分析】<父单原标题>`（回写时也靠这个前缀认「已建过」） |
| 子任务 description | 一句话结论 + 前 3 条关键假设（摘要，不放全文） |
| 子任务附件 | `analysis.md` **全文**，文件名 `<父单key>-分析报告.md` |
| 子任务标签 | 取自 `template/labels.md` 的词，含 `已分析` 共 ≤3 个；表里没有合适的词时由 worker 用 Edit 往表中补一行再用（表外词在回写时仍会被丢弃，作为最后一道闸） |

**不发评论**：JIRA Server 的评论按 wiki 标记渲染，而报告是 Markdown，贴进评论会显示成
字面的 `##` / `**`；做成 `.md` 附件反倒是干净的可下载文件。

三层幂等，重复跑不会重复建：① 台账 `workspace/out/ledger.json`（只跳过 `status=ok` 的单，
`partial` 下次会重试）② 按 `parent = <KEY>` 查已有 `【分析】` 子任务则复用
③ 子任务上已有同名附件就不重传。

> **改标签表**：直接编辑 `template/labels.md` 后跑 `./jtat.cmd labels` 自检能读到明文。
> 注意 worker subagent 在表里没有合适词时**也会自行补词** —— 跑完分析看到本表有新增行属正常，提交前过一眼即可。
> 若该文件被 DLP 拦成密文，`feedback` 会**直接报错中止**而不是把所有单打成「待归类」。

## 配置（用户只需要管三件事）

1. **把各版本 DBC 丢进** `dbc/` 目录 —— AI 会按「工单问题版本名/文件名日期，时间新者优先，
   CAN ID 命中率决胜」自行挑选，并把选择理由写进报告。
2. **在 `config.json` 的 `projects[]` 里给每个工程写一段大概描述**（产品/芯片/RTOS/负责功能/适用车型）。
   AI 靠它判断工单属于哪个工程，**不要求精确匹配规则**。
3. **配 Jira 凭据**（不进版本库）：

   ```bash
   cp vendor/jira-tool/scripts/config.example.json vendor/jira-tool/scripts/config.json
   # 编辑填入 server / email / token（PAT）
   ```

   或者改用环境变量 `JIRA_PAT` / `JIRA_SERVER`（优先级更高，适合临时或无人值守场景）。

`config.json` 里**不放任何 token**：GitLab PAT 走 `git credential fill`，Jira PAT 见上面两条途径。

> 想发邮件还要把 `lark-cli.exe` 放进 `vendor/lark-cli/` —— 它 49MB 且换机器要重新登录，
> 所以**不随分发包提供**。见该目录下的 `README.md`。不发邮件的话整条分析链路照跑。

## 关键设计约束（改代码前必读）

| 约束                                                  | 原因                                                                                             |
| ----------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| 只在工具内的 `workspace/` 下工作                      | 与用户本地 clone 物理隔离；快照目录**没有 .git**，不可能推送云端                                 |
| 所有路径经 `jta_env.tool_path()` / `cfg_path()` 解析  | config 里只写相对路径，工具才能整包搬走；绝对路径仅在 `vendor/sources.*.json` 里出现（开发期用） |
| CLAUDE.md 本地生成、长期复用                          | 仓库 `.gitignore` 忽略 `**/CLAUDE.md`，取下来的代码里没有；缓存键是 `<repo>@<branch>` 而非 sha   |
| CLAUDE.md 来源限工具内 `docs_seed/` 或内嵌 `mdmap.py` | 不碰用户本地 clone —— 代码与文档都只来自工具自己的工作区快照                                     |
| 所有 Python 子进程经 `jta_env.run_*`                  | 统一注入 `PYTHONUTF8=1`（否则 frame_extractor 在 cp936 下崩，退出码 120）与安全 cwd              |
| 绝不整读 `_frames.jsonl`                              | 可达 10MB+，会冲爆上下文；只用 `digest.md` + 定向 Grep                                           |
| 分析阶段只读（唯一例外：按需补标签词）；回写只落到**子任务** | subagent 不评论、不改状态、不做构建/烧写/签名；唯一被允许写入的工具文件是标签表，且仅在表内所有词都对不上时补一行（见 `prompts/ticket_worker.md` 规则 2）。回写由 `jtat feedback` 在该工单下**新建子任务**承载（报告挂附件 + 打标签），**父单不动**：不改标题、不加评论、不打标签 |
| 标签只能取自 `template/labels.md`                     | 表里没有合适的词时，worker **直接往表里补一行再用**（加词的唯一合法途径）；回写时表外词仍一律丢弃（只记进结果 JSON）作为最后一道闸，避免 JIRA 自由标签发散 |

## 故障排查

| 现象                                                                                                | 处置                                                                                                                                                                                                                                                                                                                                 |
| --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 找不到 `.venv` / `No module named ...`                                                              | 分发包不含 venv，按上面「首次使用」建一次                                                                                                                                                                                                                                                                                            |
| `ModuleNotFoundError: No module named 'packaging.version'` / `No module named 'charset_normalizer'` | 公司 DLP 把 venv 里这两个包的 `.py` 改名成 `.py.IPGSD`，包退化成命名空间包。**用 uv 重装（走 wheel 重建、绕开被污染的 uv 缓存）**：<br>`uv pip install --python ".venv/Scripts/python.exe" --no-cache --reinstall packaging charset-normalizer`<br>⚠ 不要手工把 `.IPGSD` 改回 `.py` —— 那是绕过 DLP 管控，权限系统会（正确地）拦截。 |
| validate 里 `vendor/` 某项 ✗                                                                        | `vendor/` 不完整，重跑 `python tools/sync_vendor.py` 重建（需先配好 `vendor/sources.json`）                                                                                                                                                                                                                                          |
| `frame_extractor` 崩溃、退出码 120                                                                  | `PYTHONUTF8=1` 没生效。确认走的是 `jta_env.run_python`，别裸调 subprocess                                                                                                                                                                                                                                                            |
| `ImportError: cannot import name 'JIRA'`                                                            | cwd 下有个 `jira/` 同名声明的目录遮蔽了包。`cd` 到工具目录再跑（`jtat.cmd` 已自动处理）                                                                                                                                                                                                                                              |
| Jira 退出码 3 / 401 / 403                                                                           | PAT 过期 → 更新 `vendor/jira-tool/scripts/config.json`，或设环境变量 `JIRA_PAT`                                                                                                                                                                                                                                                      |
| 403 `若要放弃用户通知，管理员或项目管理员权限是必需的`                                              | 不是鉴权问题。`update_issue.py` 默认 `notify=False`，会给 PUT 拼 `?notifyUsers=false`，而 JIRA Server 只允许管理员抑制通知。**调 update 一律加 `--notify`**（`jta_feedback` 已带）。                                                                                     |
| `git clone` 被拒                                                                                    | settings 里 `git clone/fetch` 的 deny 已由用户放开；若被改回，脚本会自动退到 GitLab archive API                                                                                                                                                                                                                                      |
| 邮件只拿到 `draft_id`                                                                               | `jta_mail` 会自动补发草稿；若仍失败，看 `--dry-run` 的 cmd 手工执行                                                                                                                                                                                                                                                                  |
| `lark-cli 不存在` 报错                                                                              | 不随包分发，按报错提示把它放进 `vendor/lark-cli/`，或在 config 里改 `paths.lark_cli`                                                                                                                                                                                                                                                 |
| DBC 目录为空                                                                                        | 放进 `dbc/`，然后 `./jtat.cmd dbc` 重建索引                                                                                                                                                                                                                                                                                          |
| `feedback` 报「标签表读到的是密文」                                                                 | `template/labels.md` 被 DLP 拦成密文，Python 读不到明文。先用 Read 工具确认文件本身是明文；若仍不行，把词表挪到 `scripts/` 下（该目录的文本文件对 Python 可读），并改 `jta_labels.TABLE_PATH`                                                                                                                                        |
| `feedback` 报「没有可用的子任务类型」                                                               | 该项目没启用子任务类型。在 `config.json` 的 `feedback.subtask_type` 显式写类型名（如 `子任务`），或先跑 `vendor/jira-tool/scripts/ops/createmeta.py --project <KEY> --list-types` 看有哪些                          |
| 建了子任务但附件没传上去                                                                            | 看结果 JSON 的 `attachment_error`；`status=partial` 的单**下次跑会自动重试**（台账只跳过 `ok`）                                                                                                                                                        |
| 报告内容有更新，想重传附件                                                                          | 附件是按文件名幂等的，同名就不再传。先在子任务上删掉旧附件，再 `--force` 重跑（否则会出现两个同名附件）                                                                                  |
| 同一工单下出现多个分析子任务                                                                        | 子任务是按 summary 前缀 `【分析】` 认的；有人改了子任务标题就会认不出。先手工合并/关掉多余子任务，再用 `--force` 重跑                                                                                                                |
