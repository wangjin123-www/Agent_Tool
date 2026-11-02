# jira-ticket-analysis — Jira 工单 → 代码感知分析 → 邮件审核

把「翻 Jira → 下附件 → 解日志 → 对照代码 → 写分析 → 发邮件」这条原本全手工的链路做成流水线。

**核心设计**：每张工单派一个**隔离 subagent** 分析，避免上下文爆炸与跨单污染；主 agent 只收 ≤10 行回执。
**自包含**：外部工具源码内嵌在 `vendor/`，路径全部相对工具目录解析 —— 整个目录能 zip 走、解压即用。

版本：V1.1.0　｜　首次跑通：2026-09-13（黄金用例 `LH2512024-5408`）；V1.1.0 起自包含化

---

## 1. 它做什么

```
        ┌─ 拉工单（名下未关闭）        vendor/jira-tool（python-jira）
        │
        ├─ 下附件 + 分类解析           图片 / CAN BLF / 5AA5 帧日志 / 压缩包
        │                              （图片交给视觉直接读，不 OCR）
        │
工单 ───┤
        ├─ 取对应代码                  工具自己的工作区，blobless+sparse 浅克隆
        │                              + CLAUDE.md 分层文档（本地生成/播种、长期复用）
        │
        ├─ 单票隔离 subagent           结合证据链 + 代码 → analysis.md
        │
        ├─ 邮件发我审核                vendor/lark-cli 发 HTML 汇总 + 报告附件
        │
        └─ 回写 Jira                    在工单下建子任务：报告挂附件全文 + 打标签
```

**它不做什么**（刻意划界）：**不碰父单**（父单不改标题、不加评论、不打标签、不改状态）、
不改任何代码、不跑构建/烧写/签名命令。回写的产出全部落在新建的分析子任务上。

## 2. 环境

Windows + Python 3.12。依赖装在**工具自带的 `.venv`**（与系统环境、其它工具完全隔离，可整体搬走）：

```bash
TOOL="<本工具所在目录>"        # 解压到哪就是哪
uv venv --python 3.12 "$TOOL/.venv"
uv pip install --python "$TOOL/.venv/Scripts/python.exe" -r "$TOOL/requirements.txt"
```

依赖：`jira`、`requests`、`python-gitlab`、`cantools`、`python-can`、`pillow`、`openpyxl`、`python-docx`。

> ⚠ **公司 DLP 会破坏 venv 里的 `packaging` / `charset_normalizer`**（把 `*.py` 改名成 `*.py.IPGSD`，包退化成命名空间包，报 `No module named 'packaging.version'`）。
> 合法修法（从 wheel 重建，绕开被污染的 uv 缓存）：
> ```bash
> uv pip install --python "$TOOL/.venv/Scripts/python.exe" --no-cache --reinstall packaging charset-normalizer
> ```
> **不要手工把 `.IPGSD` 改回 `.py`** —— 那是绕过 DLP 管控。
>
> 实测：在公司网络里**新装的 venv 几乎必然命中这一条**（`packaging/` 下每个 `*.py` 旁边都多一个 `*.py.IPGSD`）。
> 所以建完 venv 直接把上面那条重装命令跑一遍，是最省事的做法。

### 2.1 自包含说明：什么随包走，什么要自备

| 组件 | 位置 | 随包？ |
|---|---|---|
| 工具本体（CLI + 流水线） | `scripts/` | ✓ |
| Jira 访问（jira_bootstrap + 12 个 ops CLI） | `vendor/jira-tool/` | ✓ |
| 5AA5 帧提取 | `vendor/frame_extractor/` | ✓ |
| BLF + DBC 解码 | `vendor/canlog/` | ✓ |
| 分层 CLAUDE.md 生成器 | `vendor/claude-md-map/` | ✓ |
| DBC 文件 | `dbc/` | ✓ |
| 预生成的分层 CLAUDE.md | `docs_seed/` | ✓ |
| **`.venv`** | `.venv/` | ✗ 42MB，解压后自建 |
| **Jira 凭据** | `vendor/jira-tool/scripts/config.json` | ✗ 含 PAT，用 `config.example.json` 代替 |
| **lark-cli.exe** | `vendor/lark-cli/` | ✗ 49MB，且换机器要重新登录 |
| **GitLab 凭据** | Windows 凭据管理器 | ✗ 机器本地 |

## 3. 快速开始

```bash
TOOL="<本工具所在目录>"
cd "$TOOL"                    # 在工具目录内运行（无 jira/ 同名目录遮蔽 import jira）

# 0. 环境自检（首次或环境变动后跑）
./jtat.cmd validate

# 1. 拉单 + 解析附件 + 取代码 + 组装输入包
./jtat.cmd all --keys LH2512024-5408     # 指定单
./jtat.cmd all                           # 或按 JQL 拉全部未关闭单

# 2. 【Claude 会话动作】按上一步输出的提示，对每单派一个 subagent
#    prompt 直接取该单的 worker_prompt.md；一次一单、顺序执行

# 3. 汇总 + 发邮件
./jtat.cmd summary   --date 2026-09-13
./jtat.cmd mail-only --date 2026-09-13

# 4. 回写：在工单下建子任务（报告挂附件全文 + 打标签），父单不动
./jtat.cmd feedback  --date 2026-09-13            # 先 dry-run 看要写什么
./jtat.cmd feedback  --date 2026-09-13 --apply    # 确认后实跑
```

`jtat.cmd` 只是薄启动器，等价于：

```bash
"$TOOL/.venv/Scripts/python.exe" "$TOOL/scripts/jtat.py" <子命令> [参数]
```

### 3.1 首次使用要配的三样

1. **建 venv** —— 见第 2 节。
2. **配 Jira 凭据**（二选一）：
   ```bash
   cp vendor/jira-tool/scripts/config.example.json vendor/jira-tool/scripts/config.json
   # 填入 server / email / token(PAT)
   ```
   或设环境变量 `JIRA_PAT` / `JIRA_SERVER`（优先级更高）。
3. **（可选）发邮件**：把 `lark-cli.exe` 放进 `vendor/lark-cli/`，见该目录 `README.md`。
   不发邮件的话整条分析链路照跑。

## 4. 命令一览

| 命令 | 作用 |
|---|---|
| `validate` | 环境自检：venv 依赖 / Jira 探活 / GitLab PAT 与各工程可达 / `vendor/` 内嵌工具 / 目录可写 / DBC 数量 |
| `list` | 只列符合条件的工单，不下载 |
| `fetch` | 拉工单 + 评论 + 附件 → staging |
| `prepare` | 附件解析 + 取代码 + DBC 索引 + 组装 `bundle.md` / `worker_prompt.md` |
| `run` | `fetch` + `prepare` + `summary` |
| `all` | `run` + 提示派发（`--send` 则发信） |
| `repo` | 只取代码 + CLAUDE.md（调试用） |
| `dbc` | 只做 DBC 索引（调试用） |
| `summary` | 从各单 `receipt.json` 生成 `SUMMARY.md` |
| `mail-only` | 只发邮件（`--dry-run` 只打印命令） |
| `feedback` | 回写：在工单下**建子任务**（`analysis.md` 全文挂附件 + 打标签），父单不动；默认 dry-run，`--apply` 实跑，`--force` 重写已成功单，`--subtask-type` 覆盖子任务类型 |
| `labels` | 打印 `template/labels.md` 的词表（同时自检该文件对 Python 是明文可读） |
| `status` | 看水位 `state.json` |

通用参数：`--keys K1,K2`　`--jql "..."`　`--limit N`　`--date YYYY-MM-DD`

退出码沿袭 jira-tool：`0` 成功 / `1` 脚本错误 / `2` 参数错误 / `3` 鉴权失败 / `4` 上游 API 错误 / `5` 有单失败。

## 5. 配置：你只需要管三件事

### 5.1 把各版本 DBC 丢进 `dbc/`

AI 按四级依据自行挑选，**不需要你指定**：

| 依据 | 内容 |
|---|---|
| A | 工单里写的「问题版本名/日期」 |
| B | DBC 文件名里的版本号与日期 |
| C | 工单组件/车型（如 `WB102（柴油）`）—— 索引里有「车型 → 版本/日期」对照表 |
| D | 日志里实际出现的 CAN ID 与各 DBC 的 ID 集合求**命中率** |

规则：A/B/C 选候选 → **时间新者优先** → 无法区分用 D 决胜 → **时间新与命中率冲突时以命中率为准**（这通常意味着工单描述与实际抓包版本不一致，本身就是线索）。

索引生成：`./jtat.cmd dbc` → `<workspace>/dbc_index.md`

### 5.2 在 `config.json` 的 `projects[]` 里给每个工程写一段描述

**不需要精确匹配规则**，只要一段大概描述（产品 / 芯片 / RTOS / 负责功能 / 适用车型），AI 读工单后自行判断归属：

```jsonc
{
  "name": "S32K312 车载仪表主控平台",
  "desc": "CVI 车载仪表主控 MCU 工程，NXP S32K312 + FreeRTOS。含 L1~L5 分层与 HSE 安全模块。负责仪表显示、CAN/CANFD、UART 与 SOC 交互、电源与待机模式、音频/语音链路、诊断与签名。适用车型含 WB101、WB102 等。",
  "gitlab": { "project": "ae_mcu_projects/platform/ae_mcu_general_platform", "branch": "Mcu_GeneralPlatform_YB103" },
  "analysis_scope": "FreeRTOS_S32K312"
}
```

**没有「未映射所以跳过」这条路**：判断置信度低也照常分析，只在报告头部与第 9 节标注置信度和理由；subagent 读代码后还可提出改判。

### 5.3 配 Jira 凭据（不进版本库）

`config.json` 里**不放任何 token**。Jira PAT 走这两条路之一：

- `vendor/jira-tool/scripts/config.json`（从同目录 `config.example.json` 复制后填）
- 环境变量 `JIRA_PAT` / `JIRA_SERVER`（优先级更高）

GitLab PAT 走 `git credential fill`（Windows 凭据管理器），`config.json` 里只记 `token_source`。

### 5.4 路径配置（`config.json` 的 `paths` 块）

**一律写相对工具目录的路径**，这是「整包搬走」的关键：

```jsonc
"paths": {
  "workspace_root":  "workspace",                              // 工作区，默认工具内
  "jira_ops":        "vendor/jira-tool/scripts/ops",
  "frame_extractor": "vendor/frame_extractor/frame_extractor.py",
  "canlog_dir":      "vendor/canlog",
  "claude_md_map":   "vendor/claude-md-map/mdmap.py",
  "lark_cli":        "vendor/lark-cli/lark-cli.exe",
  "uv":              "uv",                                     // 走 PATH
  "venv_py":         "",                                       // 留空 = <工具目录>/.venv
  "base_python":     ""                                        // 留空 = 3.12
}
```

写绝对路径也支持（会原样使用），但那就失去可搬迁性了。
唯一的例外是 `vendor/sources.json` —— 那是**开发期**刷新 vendor 用的本机源路径映射，已 gitignore，不进包。

## 6. 产物结构

```
<工具目录>/workspace/
├── repos/<repo>/<branch>@<sha8>/src/     ← 代码快照（**无 .git**，物理上无法 push）
├── claude_md_cache/<repo>@<branch>/      ← CLAUDE.md 缓存（按分支键，非 sha）
└── out/<日期>/
    ├── <KEY>/
    │   ├── ticket.md                     工单正文+评论（图片引用已换成本地路径）
    │   ├── attachments/                  原始附件
    │   ├── evidence/
    │   │   ├── INDEX.md                  ★ 证据索引：该读什么、不要整读什么
    │   │   ├── *_frames_digest.md        ★ 降维摘要（几 KB）
    │   │   ├── *_frames.md               中等（几十 KB）
    │   │   ├── *_frames.jsonl            ⚠ 可达 10MB+，**只定向 Grep，不整读**
    │   │   └── unpacked_*/               解包后的日志
    │   ├── bundle.md                     输入包总览
    │   ├── worker_prompt.md              ★ 派发给 subagent 的完整提示词
    │   ├── analysis.md                   ★ 分析报告（邮件附件）
    │   └── receipt.json                  回执
    ├── SUMMARY.md
    └── _dispatch.json
```

整个 `workspace/` 都是**可再生数据**，已进 `.gitignore`，不进分发包。

## 7. 分析报告结构

固定 12 节，其中 **2.4 证据缺口** 与 **第 9 节待确认问题** 是防幻觉的关键 —— 明确区分「有证据支撑的结论」与「需要你确认的推断」：

```
0 一句话结论      1 背景与复现条件
2 证据链（2.1 图片 / 2.2 日志 / 2.3 CAN信号 / 2.4 证据缺口）
3 根因假设（分高/中/低置信，各带依据与反证）
4 涉及模块与关键文件（路径:行号 + 来源）   5 建议实施方案
6 风险与约束（引用工程 CLAUDE.md 的 Gotchas） 7 验证方法
8 工作量估计 S/M/L   9 待确认问题    附 证据文件清单
```

**质量要求**：图片必须真看（报告里要出现从图里读到的具体文字/数值/CAN ID）；证据不足就如实说不确定，**宁可承认不知道也不要编一个像样的根因**。

## 8. 设计上的关键约束（改代码前必读）

| 约束 | 原因 |
|---|---|
| 只在工具内的 `workspace/` 下工作 | 与你的本地 clone 物理隔离；该目录**没有 `.git`**，不可能推送云端 |
| 所有路径经 `jta_env.tool_path()` / `cfg_path()` 解析 | config 里只写相对路径，工具才能整包搬走 |
| CLAUDE.md 本地生成、长期复用 | 该仓库 `.gitignore` 忽略 `**/CLAUDE.md`（追踪数为 0），取下来的代码里根本没有；缓存键是 `<repo>@<branch>` 而非 sha，否则每个 commit 都要重生成 |
| CLAUDE.md 只来自 `docs_seed/` 或内嵌 `mdmap.py` | **不碰用户本地 clone** —— 代码与文档都只来自工具自己的工作区快照 |
| 所有 Python 子进程经 `jta_env.run_*` | 统一注入 `PYTHONUTF8=1`（否则 `frame_extractor` 在 cp936 下崩，退出码 120）与安全 cwd |
| 绝不整读 `_frames.jsonl` | 可达 10MB+，会冲爆 subagent 上下文；只用 digest + 定向 Grep |
| 帧日志**按目录**成组解析 | 同一次会话被拆成 `main_log` / `main_log_1` / `sys_log` 等同目录多文件，逐文件跑会把时间线切碎 |
| 密码/token 不进 `config.json` | GitLab PAT 走 `git credential fill` 运行时读取；Jira PAT 走 `vendor/jira-tool/scripts/config.json` 或 `JIRA_PAT` 环境变量 |
| subagent 只写 `analysis.md`（+ 按需补 `template/labels.md`） | 只读分析，不碰代码、不碰别的工单目录；唯一的例外是标签表里没有合适的词时往表里补一行（加词的唯一合法途径） |
| 回写只落到**子任务**，父单不动 | 分析结论是「附加产出」而非对原工单的改动；父单保持报告人写的原样，避免污染原始描述与状态 |
| 回写靠 summary 前缀 `【分析】` 识别子任务 | 不额外加标记标签污染 JIRA；`parent = <KEY>` 的结果集很小，本地按前缀过滤足够 |
| 标签只能取自 `template/labels.md` | 自由标签一旦散开无法收敛；表里没有合适的词时 worker 直接往表里补一行再用，回写时表外词仍丢弃并记进结果 JSON（最后一道闸） |
| 报告全文走**附件**而不是评论 | JIRA Server 的评论按 wiki 标记渲染，Markdown 报告贴进评论会显示成字面的 `##`/`**`；`.md` 附件是干净的可下载文件。幂等因此改认**附件文件名** |

## 9. 故障排查

| 现象 | 处置 |
|---|---|
| 找不到 `.venv` | 分发包不含 venv，按第 2 节建一次 |
| `No module named 'packaging.version'` / `charset_normalizer` | DLP 改名了 venv 里的 `.py`。见第 2 节的 uv 重装修复命令 |
| validate 里 `vendor/` 某项 ✗ | `vendor/` 不完整，重跑 `python tools/sync_vendor.py`（需先配 `vendor/sources.json`） |
| `frame_extractor` 崩溃、退出码 **120** | `PYTHONUTF8=1` 没生效。确认走的是 `jta_env.run_python`，别裸调 subprocess |
| `ImportError: cannot import name 'JIRA'` | cwd 下有个 `jira/` 同名目录遮蔽了包。`cd` 到工具目录再跑（`jtat.cmd` 已自动处理） |
| `WinError 193 %1 不是有效的 Win32 应用程序` | 直接拿 `.py` 当可执行文件跑了。用 `jta_env.run_python_json` |
| Jira 退出码 3 / 401 / 403 | PAT 过期 → 更新 `vendor/jira-tool/scripts/config.json`，或设 `JIRA_PAT` |
| `git clone` 被拒 | settings 里 `git clone/fetch` 的 deny 已放开；若被改回，脚本会自动退到 GitLab archive API |
| 邮件只拿到 `draft_id` | `jta_mail` 会自动补发草稿；若仍失败，看 `--dry-run` 打印的命令手工执行 |
| `lark-cli 不存在` | 不随包分发，按报错提示放进 `vendor/lark-cli/`，或改 `paths.lark_cli` |
| `dbc/` 为空 | 放进 DBC 后跑 `./jtat.cmd dbc` 重建索引 |
| 帧日志「一帧都没解析出来」 | 检查 `evidence/*_frames.md` 里的「扫描文件 N 候选 / M 含帧」。帧主要在 `main_log*` 与 `dumplog/dumpsys_*.txt` |

## 10. 已实测的事实（免得重踩）

- **5AA5 帧是日志里的 hex 文本**，不是二进制字节（`raw b'\x5a\xa5'` 在这些文件里为 0）。真实形态：
  `... Write: size:9 ... propid:557862919 data:0x5a 0xa5 0x00 0x00 0x03 0x00 ...`
  **每个字节都带 `0x` 前缀**，所以 `5a\s*a5` 这种朴素正则**匹配不到**。
- **`\b` 在中日韩字符与数字之间不成立**（CJK 算 `\w`）：`"监听了3D5和583"`、`"log时间15:30"` 用 `\b...\b` 都匹配不到，必须用前后瞻。
- **GitLab 凭证已存在**（Windows 凭据管理器，账号 `luziyu`），`GET /api/v4/version` → 200（GitLab 19.0.8）。**不需要新建 PAT**。
- **mcp-atlassian 已失效**（401），Jira 一律走内嵌的 `vendor/jira-tool`（本地 python-jira）。
- **lark-cli 不在 PATH**，路径见 `config.paths.lark_cli`（默认 `vendor/lark-cli/lark-cli.exe`）；`--attach` 只接受 cwd 相对路径，正文必须内联 `--body`。
- **视觉可用**：Read 工具读 PNG 能准确识别中英文文字，所以截图不需要 OCR 工具。
- **DLP 对 Python 透明**：`vendor/` 里有些 `.py` 被 DLP 加了 `%TSD-Header` 密文头，但 Python 的 `open()` / `shutil.copy2` / `zipfile` 读到的都是明文 —— 搬运和打包不受影响。（用 `head` / `cat` / `grep` 看才会看到密文，别被吓到。）

## 11. 分发给别人 / 换机器

```bash
python tools/pack.py            # → dist/jira-ticket-analysis-<日期>.zip
```

打包脚本会**自动排除** `.venv`、`workspace/`、`vendor/sources.json`、Jira PAT 配置、`lark-cli.exe`，
并做一次自检：扫描包内文本文件，确认没有绝对路径与凭据泄漏，发现即中止。

解压方需要做的三件事（脚本结束时也会打印）：

1. `uv venv --python 3.12 .venv && uv pip install -r requirements.txt`
2. 复制 `vendor/jira-tool/scripts/config.example.json` → `config.json` 并填 Jira PAT
3. 要发邮件的话，把 `lark-cli.exe` 放进 `vendor/lark-cli/`

**搬迁验证**：把整个工具目录移到任意路径（不改任何配置），`./jtat.cmd validate` 应仍全部通过 ——
这是自包含是否成立的唯一验收标准。

## 12. 二期（未实施）

定时无人值守：Windows 任务计划程序 → `pythonw.exe jtat.py all` + 锁文件防重叠。

**上二期之前必须先实测**：① headless 下 Read 工具能否同样返回图像内容（视觉是本流水线的核心假设）；② headless 下 `--attach` 相对路径与 DLP 行为是否一致；③ 中转 API 在无人值守长任务下的稳定性。

## 13. 相关文件

| 位置 | 说明 |
|---|---|
| `SKILL.md` | 作为 Claude Code skill 的入口说明与触发词 |
| `jtat.cmd` | 统一入口启动器（自解析工具目录与 .venv） |
| `config.json` | 唯一配置源（工程描述 + 相对路径），**不含任何 token** |
| `config.example.json` | 配置模板 |
| `requirements.txt` | 钉住的依赖，可重建 `.venv` |
| `docs_seed/` | 预生成的分层 CLAUDE.md 投放点（见其 README） |
| `prompts/orchestrator.md` | 主 agent：判断工程归属、逐单派发、汇总 |
| `prompts/ticket_worker.md` | 单票 subagent：隔离规则 + 报告模板 |
| `scripts/jtat.py` | CLI 入口 |
| `scripts/jta_env.py` | 统一环境（解释器 / UTF-8 / cwd / **路径解析 tool_path** / 子进程） |
| `scripts/jta_fetch.py` | 拉工单（复用内嵌 jira-tool 的 ops，不重造） |
| `scripts/jta_attach.py` | 附件分类、解包、帧解析、digest |
| `scripts/jta_repo.py` | 取代码 + CLAUDE.md 生成/缓存 |
| `scripts/jta_dbc.py` | DBC 索引与车型-版本对照 |
| `scripts/jta_bundle.py` | 组装 subagent 输入包与提示词 |
| `scripts/jta_labels.py` | 读 `template/labels.md` 词表、收敛表外词、渲染进 worker 提示词 |
| `scripts/jta_feedback.py` | 回写：建子任务 + 报告挂附件 + 打标签 + 台账（**父单不动**） |
| `template/labels.md` | 标签词表（模块类 / 现象类 / 系统类），回写时唯一取词来源 |
| `scripts/jta_dispatch.py` | 派发材料、回执、水位、SUMMARY |
| `scripts/jta_mail.py` | 发 HTML 汇总邮件 |
| `tools/sync_vendor.py` | 把外部工具源码搬进 `vendor/`（开发期用） |
| `tools/pack.py` | 打可分发 zip + 泄漏自检 |

内嵌的外部工具（`vendor/`）：`jira-tool`（Jira 访问）、`frame_extractor`（5AA5 帧提取）、
`canlog`（BLF+DBC 解码）、`claude-md-map`（分层 CLAUDE.md）、`lark-cli`（邮件，需自备 exe）。
刷新方式见 `vendor/sources.example.json` 与 `tools/sync_vendor.py`。
