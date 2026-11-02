# analyze 命令详细步骤

## 目标
扫描所有未提交文件，分析变更内容，AI生成对应的任务列表。

## 步骤

### 1. 获取所有未提交文件
```bash
git status --porcelain
git diff --name-only
git diff --cached --name-only
```

### 2. 按模块分组文件
根据文件路径分组：
- L2_Task/ → 任务层
- L3_Service/ → 服务层
- L4_EcuAL/ → EcuAL抽象层
- L5_Driver/ → 驱动层
- L6_Public/ → 公共层
- config/ → 配置文件
- MDK/ → 工程文件

### 3. 分析每个模块的变更
使用 git diff 查看具体变更内容，生成任务描述。

#### 输出格式

**tasks.json 格式**:
```json
{
  "generated_at": "YYYY-MM-DD HH:MM:SS",
  "merge_request": {
    "title": "[type] 一句话浓缩本次改动（≤40字，突出主线）",
    "description": "## 背景\n- 为什么要改（取影响等级最高的 1~2 条 why）\n\n## 变更\n- 按主线归纳（同类合并，非逐任务罗列）\n\n## 影响等级\nA\n\n## 测试范围\n1. 按重要性归并去重的测试要点"
  },
  "tasks": [
    {
      "id": 1,
      "title": "中文标题",
      "title_cn": "中文标题",
      "type": "feature|bugfix|refactor|config",
      "difficulty": "A|B|C|D",
      "labels": ["电源管理", "上下电时序"],
      "dirs": ["path1/", "path2/"],
      "git_add_pattern": "path1/ path2/",
      "jira_key": "",
      "completed": false,
      "commit_message": "[type][JIRA-ID]中文标题\n\n[what]\n1.具体变更项1\n2.具体变更项2\n\n[why]\n原因说明（可选，中文）\n\n[how]\n实现思路（可选，中文）\n\n[影响等级]S|A|B|C|D\n\n[建议测试范围]\n测试要点（中文）"
    }
  ]
}
```

**顶层 `merge_request`（必产）**：供 execute 生成 GitLab MR 标题与描述。
- `title`：一行浓缩，`[type]` 取影响等级最高任务的 type；突出主线，不堆括号细节。
- `description`：Markdown，含 `## 背景/## 变更/## 影响等级/## 测试范围` **四段**。
  **不要写「## 关联 JIRA」段**：analyze 时 `jira_key` 必为空，写出来只能是 `AERDM-xxxxx` 占位符；
  该段由 execute 的 `generate_report.py` 按真实 `jira_key` 追加（AI 文本带了会被剥掉重写）。
- `generate_report.py` 优先用该字段；缺失才走规则兜底（质量较低，务必写入）。

**commit_message 格式要求**:

---

**⚠️ 重要格式警告（违反将导致提交被拒）⚠️**

- **标题**: 中文 summary（如 `[feature][AERDM-63016]优化电源管理时序`；禁止纯英文标题）
- **内容**: 中文 what/why/how/建议测试范围（禁止英文）

**错误示例** ❌:
```
[feature][AERDM-63016]Add FreeRTOS recursive mutex  ← 英文标题，错误！
[what]
1. Service_Nvm: Add mutex protection  ← 英文内容，错误！
```

**正确示例** ✅:
```
[feature][AERDM-63016]新增FreeRTOS递归互斥锁保护  ← 中文标题，正确！
[what]
1.实现NVM模块线程安全保护  ← 中文内容，正确！
```

---

- **标题行**: `[type][JIRA-ID]中文 summary`
  - type: feature|bugfix|refactor|config
  - JIRA-ID: agent 生成时空字符串 `""`（不预填）；**用户手动填入的保留**（execute 跳过创建该单、照常显示）
  - summary: 中文简短描述（禁止纯英文）

- **内容部分**: 使用中文
  - `[what]`: 具体变更项列表（1. 2. 3.）
  - `[why]`: 原因说明（可选）
  - `[how]`: 实现思路（可选）
  - `[影响等级]`: S|A|B|C|D
  - `[建议测试范围]`: 测试要点

**commit_message 示例**:
```
[config][AERDM-63016]JIRA commit skill 脚本更新

[what]
1. 更新SKILL.md和README.md说明文档
2. 优化execute_commit.py执行逻辑
3. 更新图片资源
4. 移除validate_jira.py
5. 更新文档截图

[why]
技能文档和实现细节优化。

[how]
文档和脚本内容更新。

[影响等级]A

[建议测试范围]
1. /jira-commit命令验证功能正常
```

### 3.5 给每个任务选标签

词表唯一来源 `template/labels.md`（**唯一收敛点，表外新词一律不打**）：

- 只选表内词；**模块类优先于现象类**（能定位模块就选模块，定位不到才退而选现象）
- 数量 **≤3**（优先 1 模块 + 1 现象，判不出来打 1 个模块标签）
- **不打 `已分析`** —— 那是 `jira-ticket-analysis` 给缺陷分析子任务的标记
- 标签不能含空格、逗号、分号
- **表里找不到合适的词 → 用 Edit 工具往「模块类」或「现象类」小节补一行**
  （三列「标签 / 用途 / 典型触发关键词」都填上），再用这个词。
  **不要打 `待归类`**，也不要把表外词直接写进 tasks.json；补词后随本次变更一起提交本表
- `labels` 是 JIRA 元数据，**不写进 `commit_message`**

### 3.6 提交规范分析（必做，与生成任务同批完成）

分析对象 = **步骤 3 已拿到的同一份 diff**（`git diff HEAD -- <变更所在目录>`），
依据 = `Read references/norm_spec.md` 的检查表 **N-01~N-18**。
**只查规范/分层/命名，不查代码逻辑缺陷**（逻辑问题走 AI 代码审核，不走本流程）。

- 逐条对照 N-01~N-18，命中即产出一条建议；无违规则 `suggestions: []`
- `severity` ∈ `error` / `warn` / `info`，与 norm_spec 检查表一致
- `file` 用仓库相对路径（与 tasks.json 的 `files` 写法一致）
- 结果写入 `output/norm_analysis.json`：

```json
{
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

`suggestions[].status`（open|checked|deleted）：**analyze 生成时显式写 `"status": "open"`**；
之后**由人工编辑本文件**推进状态——认可建议就按建议改代码，再把 `"status": "open"` 改为
`"checked"`；认为建议不对就**从数组删除该条**，并跑 `/jira-commit norm` 同步规范。
**页面/服务不再改写本文件**，它是唯一状态源，execute 前打开就能看到每条当前是否已处理。

**为什么在 analyze 做**：analyze 本来就要读完本次 diff，多对照一份 norm_spec 是零边际成本；
execute 阶段不重复分析——`generate_report.py` 入口校验该文件（不合法或未全 checked
直接 `[ERROR]` 退出，HTML 都不生成），通过则把结果**只读内嵌**进 commit_report.html（无服务，见 execute 步骤 3）。

**files 字段语义**：`files` 记录本次分析覆盖的文件（≈ tasks.json 各任务 `files` 的并集），
**供人核对，不参与 execute 校验**。analyze 之后用户改文件（增/删/改内容）**不需要重新分析**。

**自检**：`norm_analysis.json` 必须存在且含 `suggestions`（可为空数组）与 `files`；
每条建议必须有 `id`/`rule`/`severity`/`title`/`file`/`status`，且 `status ∈ open|checked|deleted`
（analyze 生成时**显式写 `"open"`**，其余两态只能由人工编辑产生）；**不得留空文件**
（空文件 JSON 解析失败，execute 会 `[ERROR]` 退出不生成报告）。

### 4. 特殊处理
- **MDK 工程文件**: 通常不单独提交，合并到其他任务
- **build.log**: 不提交
- **JLinkLog.txt**: 不提交或单独清理任务
- **.gitignore**: 配置变更，单独任务

### 5. 生成输出文件
- `output/tasks.json` - JSON格式任务列表（**顶层带 `"generated_at": "YYYY-MM-DD HH:MM:SS"` 与 `merge_request`**；generated_at 供 execute 门禁校验 norm_analysis.json 是否同批产物）
- `output/commit_preview.md` - 人类可读预览
- `output/norm_analysis.json` - 提交规范分析结果（见 3.6；`analyzed_at` 不得早于 tasks.json 的 `generated_at` 减 5 分钟，否则 execute 拒绝）

## 示例

### 输入
```
M L3_Service/Service_Tuner/Service_Tuner.c
M L3_Service/Service_Com/Service_Com.c
M L4_EcuAL/EcuAL_Tuner/EcuAL_Tuner_Cfg.h
```

### 输出
按模块分组生成对应任务：
- Task 1: Tuner模块重构
- Task 2: Service_Com protobuf更新
