# 分析强度（--depth）：低 / 中 / 高

**两条铁律（先记住，再看细节）**

1. **只有"没有特殊要求"时才让用户选强度。** 用户一旦给了特殊要求（`--focus`），
   就**严格按他的要求分析，强度不生效**——不问他强度，传了也忽略。
2. **无论哪个强度，ERROR 和 WARN 都必须分析。** 强度只决定"其他章节给多少"，
   绝不决定"要不要看异常"。三档的 `err_n` / `warn_n` / `top` 都非 0。

强度本身要问用户，不许默认执行。落点：`scripts/analyze/analyze_log.py` 的 `DEPTH_PRESETS`。

## 1. 三档一句话定义

| 强度 | 一句话 | 适用场景 | 邮件正文长度 |
|------|--------|----------|--------------|
| `low` | 只看异常：结论 + 热点 + ERROR/WARN 明细 | 快速冒烟、回归验证、就想知道有没有炸 | 十几行 |
| `medium` | 低的基础上加 高频消息 / 模块分布 / 关键状态行（**推荐默认**） | 日常问题定位，90% 场景 | 几十行 |
| `high` | 全维度聚合 + 逐行挂分析 | 疑难问题、正式报告、要看时序 | 上百行 |

三档都是**全量扫描**（计数全量累加），只是**往外吐多少**不同。
所以强度不影响正确性，只影响信息量和耗时。

## 2. 强度对照表（= DEPTH_PRESETS 实际取值）

```python
DEPTH_PRESETS = {
    #        top  dedup  keep  err_n warn_n  states  mods  buckets  note_all
    "low":    {"top": 10, "dedup": 0,  "keep": 50,  "err_n": 20, "warn_n": 10, "states": 0,  "mods": 0,  "buckets": 0,  "note_all": False},
    "medium": {"top": 10, "dedup": 10, "keep": 200, "err_n": 20, "warn_n": 10, "states": 10, "mods": 10, "buckets": 0,  "note_all": False},
    "high":   {"top": 30, "dedup": 30, "keep": 500, "err_n": 60, "warn_n": 30, "states": 30, "mods": 0,  "buckets": 30, "note_all": True},
}
```

字段含义：

| 字段 | 含义 | low | medium | high |
|------|------|:---:|:---:|:---:|
| `top` | 问题热点(file:line) 展示条数 | 10 | 10 | 30 |
| `dedup` | 高频消息(形状去重) 展示条数；`0` = 不展示该章节 | 0 | 10 | 30 |
| `keep` | ERROR/WARN 明细行保留上限（也控内存） | 50 | 200 | 500 |
| `err_n` | 正文里 ERROR 明细打印条数 | 20 | 20 | 60 |
| `warn_n` | 正文里 WARN 明细打印条数 | 10 | 10 | 30 |
| `states` | 关键状态行（状态机/握手/供电/唤醒）条数；`0` = 不展示 | 0 | 10 | 30 |
| `mods` | 模块 × Level 表的模块数；`0` = 不展示该章节 | 0 | 10 | 0 |
| `buckets` | 时间分布桶（每秒行数）；`0` = 不算 | 0 | 0 | 30 |
| `note_all` | HTML 中每条 WARN/ERROR 都挂分析说明 | — | — | True |

> `note_all` 在 HTML 里**恒为 True**（见铁律 2，任何强度异常行都要有分析）；
> 上表保留该字段只为兼容旧 JSON。
> `--top` / `--keep` 仍可在命令行显式覆盖预设（临时调试用），优先级高于 `--depth`。

## 3. 各强度"邮件正文里到底有哪些章节"

| 章节 | low | medium | high |
|------|:---:|:---:|:---:|
| 文件/方式/强度/总量/时段 | ✅ | ✅ | ✅ |
| 结论（关联工程 / 有无 ERROR/WARN / 主要阶段 / 日志主体 / 源码出处） | ✅ | ✅ | ✅ |
| Level 分布 | ✅ | ✅ | ✅ |
| **问题热点（file:line + 工程源码位置）** | ✅ top10 | ✅ top10 | ✅ top30 |
| **ERROR 明细** | ✅ 20 条 | ✅ 20 条 | ✅ 60 条 |
| **WARN 明细** | ✅ 10 条 | ✅ 10 条 | ✅ 30 条 |
| 高频消息（形状去重） | ❌ | ✅ top10 | ✅ top30 |
| 模块 × Level | ❌ | ✅ 10 个模块 | ❌（改看全量明细） |
| 时间分布（每秒行数 + 峰值） | ❌ | ❌ | ✅ 30 桶 |
| 关键状态行（末次） | ❌ | ✅ 10 条 | ✅ 30 条 |
| 尾部 5 行 | ✅ | ✅ | ✅ |

**工程关联与强度无关**：任何强度下结论都带"关联工程 / 主要阶段 / 源码出处"（见 [analysis_modes.md](analysis_modes.md) 第 5.5 节）。
唯一差异：`low` 不展示去重明细（`dedup=0`），所以"日志主体"退回热点位置前 3 而非最高频消息样本；`medium`/`high` 用去重后的最高频打印样本。

**HTML 附件不受强度影响章节结构**：任何强度下，每条 WARN/ERROR 行后都挂分析说明。

即：**邮件正文用强度裁剪，但异常（ERROR/WARN）永不裁掉；HTML 始终全量逐行 + 逐条分析**。

## 4. 有特殊要求时：强度不生效（铁律 1）

一旦传了 `--focus "正则"`：

- 不再需要 `--analysis-depth`（采集脚本的门禁也不再要求它）
- 传了也忽略，并在输出里明确写 `强度: 不适用(已按你的特殊要求执行, 强度不生效)`
- 改用 `FOCUS_PRESET`（匹配行尽量全量分析）：

```python
FOCUS_PRESET = {"top": 50, "dedup": 50, "keep": 2000, "err_n": 200, "warn_n": 200,
                "states": 50, "mods": 20, "buckets": 0, "note_all": True}
```

- 邮件正文 = 只分析匹配行；HTML 报告 = 仍全量
- 各入口（采集启动 / `capture_cmd mail` / Web `/dump`）都按此处理：
  有 focus 就不问强度，或问了也丢弃

## 5. 强度 × 规模（一万行以上怎么保证不爆）

三档都遵守"输出规模与日志行数解耦"：

| 机制 | 说明 |
|------|------|
| 计数全量累加 | `levels_all` / `err_all` / `warn_all` / `drop_lines` 不受行数影响，永远准 |
| 明细去重 | 明细按"消息形状"（去时间戳/hex/数字）去重，`keep` 是每类上限，不是总上限 |
| 热点 topN | 热点表内部最多留 200 个候选，最终只输出 `top` 条 |
| 时间桶聚合 | 不按行记时间，按"秒"累加行数，只输出 `buckets` 个桶 |
| 尾行定长 | 只留最后 5 行 |

结论：**10 行 log 和 100 万行 log，邮件正文长度一样**（同强度下条数上限相同），
差别只在每个热点/形状的 `count` 数字大小。这是可以放心用 `high` 的原因。

## 6. 选哪个（给 AI 的默认建议，但仍要问）

- 用户说"随便看看/有没有报错" → 建议 `low`
- 用户没特别说明 → 建议 `medium`（默认值）
- 用户说"详细点/要发报告给领导/问题很难复现/要看时序" → 建议 `high`
- 用户有特殊要求 → **跳过此问**，按 focus 执行
- 日志很大（>1 万行）不影响选档（见第 5 节）：`high` 只多花扫描时间，输出不膨胀

## 7. 命令用法

```bash
# 分析（三档）
python -u "$SKILL_DIR/scripts/analyze/analyze_log.py" <log> --mode auto --depth low    --md-out 分析.md --json-out 分析.json
python -u "$SKILL_DIR/scripts/analyze/analyze_log.py" <log> --mode auto --depth medium --md-out 分析.md --json-out 分析.json
python -u "$SKILL_DIR/scripts/analyze/analyze_log.py" <log> --mode auto --depth high   --md-out 分析.md --json-out 分析.json

# 有特殊要求: 不传 --depth, 传了也不生效
python -u "$SKILL_DIR/scripts/analyze/analyze_log.py" <log> --mode auto --focus "HandShake" --md-out 分析.md --json-out 分析.json

# 采集（设了结束条件时 --analysis-mode 必带; 无特殊要求时 --analysis-depth 必带）
python -u "$SKILL_DIR/scripts/capture/capture_serial.py" --port COM9 --baud 115200 --confirm --auto-baud \
    --end-cond duration --duration 30 --analysis-mode auto --analysis-depth medium
python -u "$SKILL_DIR/scripts/capture/capture_serial.py" --port COM9 --confirm --auto-baud \
    --end-cond duration --duration 30 --analysis-mode auto --focus "HandShake"   # 无需强度

# 采集中途发快照邮件（可覆盖本次强度; 有 --focus 则强度被忽略）
python "$SKILL_DIR/scripts/capture/capture_cmd.py" <log路径> mail "备注" --analysis-mode auto --depth high
```

工程关联（不传 `--project` 就用 config `[projects] default`；无 default 时用户答复后传）：

```bash
python -u "$SKILL_DIR/scripts/analyze/analyze_log.py" <log> --mode auto --depth medium --project 2 \
    --md-out 分析.md --json-out 分析.json
python "$SKILL_DIR/scripts/capture/capture_serial.py" --list-projects
```

输出末行固定打印强度确认行：
- 无 focus：`[分析] 方式=xx 强度=low 总行=N 分析范围=N ERROR=n WARN=n`
- 有 focus：`[分析] 方式=xx 强度=不生效(按特殊要求) 总行=N 分析范围=N ERROR=n WARN=n`

## 8. 相关

- 分析方式（fixed / free / auto）与 focus 约定：[analysis_modes.md](analysis_modes.md)
- 采集结束条件与自动发邮件：[../SKILL.md](../SKILL.md)

