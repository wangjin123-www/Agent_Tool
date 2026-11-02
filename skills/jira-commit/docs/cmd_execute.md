# execute 命令详细步骤

## 目标
创建 JIRA 任务 → jira_id 写入 commit_message → 生成**合并 commit**（commit_preview.md）→ 生成 HTML 报告（commit_report.html，**规范分析结果只读内嵌，无服务**）→ 飞书邮件通知（lark-cli）

**已禁用（不再自动执行）**：git commit / rebase / push / stash 备份——全部改为手动，操作指引见 commit_report.html。

## 强制流程（不可跳过任何步骤）

### 步骤 0: 前置门禁（创建 JIRA 之前，规范建议必须全部人工确认）
```bash
cd "$SKILL_DIR" && python script/generate_report.py --check-norm
```
- 只校验不产出：逐条检查 `$OUTPUT/norm_analysis.json`，任一建议 `status != "checked"`（结构不合法同理）
  → `[ERROR]` 退出，**不创建 JIRA、不生成任何文件**
- 退出信息含未确认 ID + 人工处理指引；用户处理完再重跑 execute
- 通过（含空 `suggestions: []`）→ 继续步骤 1

### 步骤 1: 询问用户是否创建 JIRA
**显示任务列表**，询问：
- 是否自动创建 JIRA 任务？
- 选项：是/否
- 同时告知：execute 只创建 JIRA + 生成合并 commit 与报告，**不会执行任何 git 提交/推送**

### 步骤 2: 创建 JIRA 任务（用户选择"是"）
```bash
cd "$SKILL_DIR" && python script/create_jira_tasks.py
```

**行为**:
- **跳过已有有效 JIRA key 的任务**（不重复创建），但**把本地任务内容追加到该 JIRA 描述后面**（GET 现描述 → 已含同样内容则幂等跳过 → 否则 PUT 追加；失败仅 WARN 不中断）
- 只为空或无效 key 的任务创建/查找 JIRA
- **新建**的工单带上 `tasks[].labels`（来自 analyze 的标签选取）；**已有 jira_key 的工单不补打标签**
  （存量工单不被改动，标签只留在 tasks.json / HTML / preview 本地）
- 无 `labels` 字段的老任务 payload 里不带 `labels` 键，行为与改动前一致
- 更新 commit_message 中的 JIRA ID

**输出**: tasks.json 更新（jira_key、commit_message）

**失败处理**:
- JIRA 未配置 → AskUserQuestion 让用户选择如何处理（配置/跳过）
- JIRA 连接失败 → 显示错误，中止执行

### 步骤 3: 生成合并 commit + HTML 报告（入口硬门禁 + 只读内嵌） + 邮件通知
```bash
cd "$SKILL_DIR" && python script/generate_report.py
```
（入口门禁与步骤 0 同源，这里再校验一次——防步骤 1/2 期间 json 被改动）

**行为**（读取 tasks.json，无任何 git 操作）:
1. **入口硬门禁**（两道，任一不过直接 `[ERROR]` 退出，**HTML 都不生成**）：
   - **结构**：`$OUTPUT/norm_analysis.json` 缺失 / 空文件 / JSON 损坏 / 缺 `suggestions` 键 →
     提示重跑 analyze
   - **人工确认完成**：每条 suggestion 的 `status` 必须为 `checked`；有 `open` 等待确认的 →
     报「未确认: S01, S02...」退出并打印人工处理指引。空 `suggestions: []` 合法（无违规 / 建议全删）
2. 解析每个任务的 commit_message（[what]/[why]/[how]/[影响等级]/[建议测试范围]）
3. 生成**合并 commit** 写入 `commit_preview.md`（所有任务合成一条 commit，整体使用勿拆分）
4. 生成 **MR 标题与描述** 写入 `merge_request.md`：优先取 `tasks.json` 顶层 `merge_request`，
   缺失时按任务清单规则兜底（影响等级排序取样本 + 测试范围归并重编号）
5. 生成 `commit_report.html`：规范分析结果**只读内嵌**（每条显示 ID+严重度+规则+标题），
   卡片 4 展示 MR 标题/描述并支持点击复制/一键复制/下载；
   **无服务、无勾选/删除/编辑按钮、无置灰门禁**，全部操作按钮可用；浏览器 file:// 双击打开
6. 触发 send_mail.py：发飞书邮件（lark-cli）

**人工处理规范建议（execute 前就要做完）**：
- **认可建议** → 按建议改代码，然后**人工编辑** `$OUTPUT/norm_analysis.json`，把该条
  `"status": "open"` 改为 `"status": "checked"`
- **认为建议不对** → **从 suggestions 数组删除该条**，并跑 **`/jira-commit norm`** 交互，
  同步更新规范三件套（`references/norm_spec.md` / 相关 `CLAUDE.md` / memory），
  让下轮 analyze 不再报同类建议
- 全部处理完（剩的都是 checked，或数组已删空）→ 重跑 execute 放行

### 步骤 4: 告知用户操作 HTML（agent 无任何分析动作）

把报告文件路径（`$OUTPUT/commit_report.html`）给用户并简述流程：

1. **第 1 张卡片**规范分析结果（**只读快照**：每条显示 ID + 严重度 + 规则 + 标题，
   完整 detail/suggestion 由卡片 5「一键复制」输出；
   卡片内可「一键复制」）
2. **第 2 张卡片**手动 git 提交 push（add → commit -F → pull main → push）
3. **第 3 张卡片**JIRA 打「待验证」
4. **第 4 张卡片**提 MR（显示 MR 标题与描述，
   标题/描述优先取 `tasks.json` 顶层 `merge_request`，缺失走规则兜底；
   可点击复制、一键复制标题+描述、下载 merge_request.md）
5. **第 5 张卡片**「一键复制」分析结果（按点分条）→「打开本分支提交列表」→ 点顶端 commit →
   **手动粘贴为评论**
6. **第 6 张卡片**按需打 tag

**合并 commit 格式**（任务头一律中文标题，jira 缺失用 `jira#` 占位）:
```
[<type1>][<jira1>][<jira2>]... N commits

[<type1>][<jira1>]<中文标题>

[what]
1. ...

[why]
原因

[how]
思路

[影响等级]B
[建议测试范围]
1. ...
```

**commit_report.html 内容**（6 个卡片；**全部只读可操作，无服务、无门禁置灰**）:
| 卡片 | 内容 |
|------|------|
| 1. 提交规范分析结果 | analyze 产物**只读内嵌**（含 analyzed_at）；**每条显示 ID + 严重度 + 规则 + 标题**（完整 detail/suggestion 由卡片 5「一键复制」输出）；含「一键复制」按钮 |
| 2. 手动提交和 push commit | 合并 commit 内容**可编辑 textarea** + 复制/下载/**同步 commit_preview.md** 按钮；4 步 git：add → `git commit -F commit_preview.md` → `git pull origin main` → `git push -u origin <分支>` |
| 3. 手动把 JIRA 任务打到「待验证」 | 本次创建的全部 JIRA id，可单击跳转；id 后跟标签胶囊（`tasks[].labels`） |
| 4. 在 GitLab 提 merge request | 当前分支 → main 的 MR 链接；**展示 MR 标题与描述**（点击复制 / 一键复制标题+描述 / 下载 merge_request.md），来源：`tasks.json` 顶层 `merge_request`，缺失走规则兜底 |
| 5. 给 commit 添加评论 | **「一键复制规范分析结果」**：按点分条（severity/rule/标题/文件/问题/建议）；**「打开本分支提交列表」**：GitLab `/-/commits/<分支>` 链接（`/-/commit/<id>` 只接受 SHA，传分支名会 404），push 后点顶端 commit，用户**手动粘贴**复制的文本为评论 |
| 6. 如有必要手动打 tag | GitLab 新建 tag 表单链接（`/-/tags/new?ref=<分支>`） |

**邮件内容**（execute 完成时，飞书邮件 via lark-cli mail +send）:
- 主题：jira-commit 执行完成
- 收件人：当前飞书账号邮箱（lark-cli 自动获取）；抄送：config.notification.email_cc
- 正文：
  0. 规范分析结果已只读内嵌报告（**execute 前需人工确认全部 status=checked**）
  1. 手动提交和 push commit（先 git pull origin main 再 push）
  2. 手动把 JIRA 任务打到「待验证」（附本次创建的 JIRA 超链接）
  3. 在 GitLab 提 merge request
  4. 复制规范分析结果贴为 commit 评论
  5. 如有必要手动打 tag
  - 详情链接：commit_report.html；发送失败仅 WARN，不中断

## completed 语义（已变更）
- execute **不再**标记 `completed: true`（commit/push 已改为手动，脚本无法确认完成）
- 任务保持 `completed: false`；如需标记，由用户手动改 tasks.json 或重跑 analyze

## 确认要求

执行前必须 AskUserQuestion 确认：
- 显示任务列表
- 显示即将执行的操作（创建 JIRA + 生成合并 commit/报告，**无 git 提交**）
- 用户确认后再执行

## 错误处理

| 错误 | 处理 |
|------|------|
| JIRA 未配置 | AskUserQuestion 让用户选择处理方式 |
| JIRA 创建失败 | 显示错误，中止执行 |
| tasks.json 不存在 | 提示先执行 /jira-commit analyze |
| norm_analysis.json 缺失/空/损坏/缺 suggestions 键 | generate_report `[ERROR]` 直接退出（HTML 不生成）→ 提示重跑 /jira-commit analyze |
| norm_analysis.json 有建议 `status != "checked"` | generate_report `[ERROR]` 退出，打印未确认 ID 与人工处理指引 → 人工改代码 + 编辑 status，或删建议 + `/jira-commit norm` 后再 execute |
| 邮件发送失败 | 仅打印 WARN，不影响报告生成 |
