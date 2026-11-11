# 分析方式（--analysis-mode）：fixed / free / auto

**分析方式必须问用户，不许默认执行。** 用途不同、结论口径不同。
落点：`scripts/analyze/analyze_log.py` 的 `analyze()` / `detect_mode()`。

## 0. 两条铁律（优先级最高，先看这节）

| # | 铁律 | 含义 | 落点 |
|---|------|------|------|
| **1** | **有特殊要求（`--focus`）时，强度不生效** | 强度（low/medium/high）**只在我没有特殊要求时才让我选**。一旦我给了 focus，就严格按我的要求分析——**不问强度、传了也忽略**，脚本不要求 `--analysis-depth` | `analyze_log.py` 的 `focus_override` + `FOCUS_PRESET`；`capture_serial.py` 门禁；`capture_cmd.py`；`serial_monitor.py` `/dump` |
| **2** | **无论哪个强度，ERROR 和 WARN 都必须分析** | 强度只裁剪其他章节（热点条数/模块分布/时间桶/去重明细），**绝不裁掉异常**。三档 `err_n`/`warn_n`/`top` 均非 0；HTML 里 WARN/ERROR 每一行恒挂分析块 | `DEPTH_PRESETS`（见 [analysis_depth.md](analysis_depth.md)）；`gen_report.py` `note_all = True` |

三处入口都必须按此处理，行为一致：

| 入口 | 铁律 1 的实现 |
|------|----------------|
| 采集启动（`capture_serial.py`） | 有 `--focus` 时不要求 `--analysis-depth`（门禁只查 `--analysis-mode`）；有 focus 则把 `analysis_depth` 置 None 透传 |
| 采集中途（`capture_cmd.py mail`） | 有 `--focus` 时丢弃 `--depth` 并提示"已忽略" |
| Web 保存日志（`serial_monitor.py` /dump） | 前端**先问特殊要求，填了就不再问强度**；后端有 focus 则 `a_depth = None` |

## 1. 三种方式

| 方式 | 是什么 | 适用日志 | 落点 |
|------|--------|----------|------|
| `fixed` | 按 **module / level / 具体内容** 三维聚合 | DAB_BOX 固件（有 `[ts][LEVEL][file:line] [module]` 结构） | `FIXED_RE` 解析 + 热点/模块×Level |
| `free` | 无结构裸打印 → **消息形状归一化去重** + 关键词分级 + 关键状态行 | SoC / BSP / 上位机 / 第三方日志 | `normalize_shape()` + `ERR_PAT`/`WARN_PAT` |
| `auto` | 采样前 2000 行，**固定格式占比 ≥ 0.5 → fixed，否则 free** | 不确定、混合格式 | `detect_mode()` |

固定格式正则（与 SKILL.md 一致）：

```python
FIXED_RE = re.compile(
    r"^\[(\d+)\](?:\[(DEBUG|INFO|WARN|ERROR|D|I|W|E)\])?\[([^\]:]+):(\d+)\]\s*\[([^\]]+)\]\s?(.*)$")
```

## 2. fixed 与 free 的差异（结论口径不一样）

| 维度 | fixed | free |
|------|-------|------|
| level 来源 | **优先取 `[LEVEL]` 字段**，无字段再用关键词兜底 | 只有关键词兜底（`ERR_PAT` / `WARN_PAT`） |
| 热点单位 | `file:line`（能直接指到代码位置） | 无 file:line，热点退化为"消息形状" |
| 模块维度 | 有 `[module]`，能出 模块 × Level 表 | 无模块（统一记 `-`） |
| 时间来源 | `[timestamp]` 毫秒数（可算跨度/时间桶） | 多数无时间戳（时间分布不可用） |
| 去重 | 消息形状去重（在 msg 上做） | 消息形状去重（在整行上做） |
| **工程反查路径** | **`file:line` → 工程里同名文件第 N 行 + 所在函数**（`locate_fixed`） | **打印内容里的字段名 → 工程源码的打印行**（`grep_project`） |

**共同点**：计数全量累加（`levels_all` / `err_all` / `warn_all` 不受方式影响），
`drop_cnt` 专项、尾部 5 行、结论段在三方式下都有。

关键词兜底正则（free 的主要判据）：

```python
ERR_PAT  = re.compile(r"HardFault|CmBacktrace|ASSERT|assert|ERROR|ERR_|error|FAIL|fail|Fault|fault|panic|Panic")
WARN_PAT = re.compile(r"retry|RETRY|timeout|TIMEOUT|Timeout|WARN|\[W\]")
```

## 3. 消息形状归一化（free 去重的核心）

```python
def normalize_shape(text):
    t = re.sub(r"^\[\d+\]", "", text)      # 去开头时间戳
    t = re.sub(r"0x[0-9a-fA-F]+", "0xH", t) # hex -> 0xH
    t = re.sub(r"\b\d+\b", "N", t)          # 数字 -> N
    t = re.sub(r"\s+", " ", t).strip()
    return t[:120]
```

效果：`[123] wakeup count=5` 与 `[456] wakeup count=9` → 同一条形状 `wakeup count=N`，
计数合并，详情只留一条代表行。**这是万行日志不膨胀的关键**（见下节）。

`gen_report.py` 里有同名的 `shape_key()`，必须与它保持一致，否则 HTML 逐行分析块挂不上。

## 4. 一万行以上怎么分析（规模无关策略）

| 策略 | 实现 | 效果 |
|------|------|------|
| 计数全量累加 | `Counter` 逐行 `+= 1` | 数字永远准，与行数无关 |
| 明细去重保留代表 | 按 shape 去重，每类上限 `--keep` | 明细条数恒定 |
| 热点取 top N | 内部候选 200 → 输出 `--top` 条 | 热点条数恒定 |
| 时间分布按桶 | `buckets[ts // 1000] += 1` | 不按行记时间 |
| 尾行定长 | 只留最后 5 行 | 定长 |
| HTML 行数限幅 | `gen_report.py --max-lines 20000`（默认） | 页面不卡；**log 附件仍完整** |

结论：**输出规模与日志行数解耦**。10 行和 100 万行，邮件正文长度在同一强度下相同（差异只在 count 数字）。
HTML 报告超 `--max-lines` 会截断并在页首提示"已截断，完整内容见附件 log"。

## 5. focus（特殊要求）：正文裁剪，HTML 全量

用户可能有特殊要求，例如**"只分析握手相关打印"**。

```bash
--focus "HandShake"
```

行为约定（**必须按此执行，不许全量全写正文**）：

| 位置 | 行为 |
|------|------|
| 邮件正文 | **只分析匹配行**；结论段写明 `特殊要求: 只分析匹配 /HandShake/ 的行 -> 命中 N 行(全量仍计入上方总数)` |
| 分析强度 | **不生效**（铁律 1）——有 focus 就严格按此分析，不看 low/medium/high；结论段写 `强度: 不适用(已按你的特殊要求执行, 强度不生效)`，内部 `depth_effective=None` / `focus_override=True`，改用 `FOCUS_PRESET` |
| 全量计数 | 匹配行**之外**的行仍计入 `levels_all`（总数/level 分布不失真），但只输出"全量对照"一行 |
| 异常 | 匹配范围内的 ERROR/WARN **照常全部分析**（铁律 2 不许因 focus 而漏） |
| HTML 报告 | **保持全量逐行**（不裁剪），Ctrl+F 能查到所有行 |
| 未命中 | 若匹配 0 行，正文明确报"特殊要求命中 0 行"，不假装有结论 |

即：**正文按 focus 裁剪，HTML 始终全量，强度让位给 focus**——正文给人扫结论，HTML 给人翻细节。

## 5.5 工程关联（结论必须落到代码）

**结论不能只有"0 个 ERROR"，要说出"当前在打什么、这行打印来自哪个工程的哪个文件/函数"。**
落点：`analyze_log.py` 的 `load_projects / resolve_project / locate_fixed / grep_project / infer_stages / build_conclusion`。

### 工程注册表：config `[projects]`

```ini
[projects]
1 = d:\wnagjin\Compay_Project\DAB_BOX\DAB_BOX_CODE\dabbox_app
2 = d:\wnagjin\Compay_Project\CDC_7255\cdc_7255
default = 2
```

| config 有 `default` | 行为 |
|---------------------|------|
| **有**（当前 = 2） | 分析**自动**关联该工程，不再问用户；`project_desc` 写 `2(config 默认) = <路径>` |
| **无** | **每次分析前必须问用户"关联哪个工程"**；用户答复 → `--project <编号\|路径>`；**不回答 → `project_linked=False`，结论只基于日志本身**并显式写明"未关联工程" |

- `--project` 也可直接给绝对路径（`Path(key).is_dir()` 时按直接路径处理）
- `--list-projects` 打印注册表并标出 `<- 默认`

### 反查机制（四个日志字段都用来定位工程）

| 字段 | 用途 | 对应函数 |
|------|------|----------|
| `file:line` | **主路径（fixed）**：文件名 lower 建索引 → 定位源文件 → 取第 N 行 + 向上找所属函数 | `project_index` → `locate_fixed` → `enclosing_function` |
| `打印内容` | **主路径（free）**：提字段标识符（`IDENT_RE` 去 `IDENT_STOP` 噪声词）→ 只在**打印行**（`PRINT_RE`）里检索 | `extract_tokens` → `grep_project` |
| `[module]` / `level` | 参与阶段语义推断 | `infer_stages` + `SEMANTIC_HINTS` |
| `timestamp` | 时间跨度/时间桶（high） | `buckets` |

### 模块漏斗定位（v2.6：位置 → 模块 → 模块内 → 全局兜底）

反查不是"逐条孤立跳"，按漏斗收敛范围，结论里每条 code_link/token_link 带 `[定位: via]` 标注：

| 层级 | 触发对象 | 动作 | via 标注 |
|------|----------|------|----------|
| ⓪ 内容验真 | 每次 `locate_fixed` 命中 | **接口名无关**：源码行字符串字面量按格式符切段（`src_msg_affinity`），字面段按序出现在日志样本中才算同源；多候选时优先取验真通过者 | 验真失败 → `内容不符(疑同名文件误命中)`，不宣称模块内定位、不挂调用方 |
| ① 异常全局反查 | **ERROR/WARN 热点**（铁律延伸：异常常是跨模块因果，**不走漏斗**） | `locate_fixed` + `find_callers`（全工程搜调用点，**跨模块调用方排序在前**） | `异常全局反查` |
| ② 模块内定位 | 常规 INFO/DEBUG 热点 | `locate_fixed` 命中工程文件且行有效且内容验真通过即成；模块 = 命中文件相对路径的**最近两级目录**（`module_of`，如 `L1_APP/APP_Tuner`、`CVI_McuPlatform/L4_Service/Power`） | `模块内(层级/模块)` |
| ③ 模块上下文 | 热点行数最多的前 3 个模块 | `module_context` 按代码模块聚合全量热点（未被 top 裁剪）：热点数/行数/level 分布/首末时间/代表样本 | 结论段"模块上下文:" |
| ④ 全局兜底 | 常规热点行号失效（`out_of_range`）或 free 单命中 | `grep_project` 全工程打印行检索；free 多命中时**按命中文件模块分组，同模块 ≥2 个命中优先**（消除跨模块同名打印歧义） | `全局兜底` |

内容验真不依赖 `printf`/`LOG_INFO` 等接口名（接口改名不受影响），验的是"打印文本同源"——防两工程同名文件（如都有 `APP_Power.c`）把注释行/无关行当打印出处。

调用方检索（`find_callers`）是模块分析的标准动作而非"跳出模块"：ERROR 打印点所在函数往往不是触发者（实测案例：`Service_Com.c:1239` 的发送失败，触发方在 `APP_Tuner` 2s 周期上报 + USB 主机端不消费队列）。


- `SEMANTIC_HINTS`：文件名/函数名关键词 → 中文阶段，如 `HandShake|SocComm` → "MCU<->SoC 握手/通信"、`PowerHsm` → "电源状态机(上电/唤醒/休眠)"。**按命中次数排序取前 4**，让反复出现的阶段优先进结论
- `project_index` 结果缓存（`INDEX_CACHE`），同一工程只遍历一次
- 反查不到时（第三方库打印/版本不一致/纯数字字段）结论明确写"未能把日志对到工程源码"，**不编造**
- `--project` 传入的路径不存在且不是 config 编号 → `project_linked=False`，`project_desc` 写 `<key>(config 无此编号且不是有效目录)`

### 结论正文结构（`build_conclusion`）

```text
关联工程: 2(config 默认) = d:\wnagjin\Compay_Project\CDC_7255\cdc_7255
【结论】未发现 ERROR/WARN, 主要阶段: 电源状态机(上电/唤醒/休眠) / 电源管理 / MCU<->SoC 握手/通信 (按文件名/函数名判断); 这段日志是设备正常输出。
日志主体(最高频打印, 即判定依据): InAmp=0,ExAmp=0,AvAmp=0! | IcPwrSta=0,IviPwrSta=0,StrPin=0! | AppPowerHsmState=2
固定格式热点已定位到工程源码(file:line -> 文件:行, 所在函数):
  Service_Com.c:1239 -> <相对路径>:1239, 函数 COM_Resp_Handshake()  [定位: 异常全局反查]
        源码: MCU_Printf("COM_Resp_Handshake send failed: ret=0x%08X\r\n", ret);
        调用方: L1_APP/APP_Tuner/APP_Tuner.c:136 函数 APP_Tuner_InitStatusReport()  <- 异常触发链, 跨模块看这里
日志打印字段在工程源码中的出处(按字段名检索打印语句):
  AvAmp -> CVI_McuPlatform/L1_APP/APP_Power/App_PowerHsm.c:1774, 函数 App_Power_MuteMainFunction()  [定位: 模块内(L1_APP/APP_Power)]
        源码: MCU_Printf("InAmp=%d,ExAmp=%d,AvAmp=%d!\r\n", ...);
模块上下文(热点所在模块在干什么, 供逻辑范围定位):
  L1_APP/APP_Power: 2 个热点 / 41 行 (INFO=2)
        例: [67990][App_Power.c:60] [POWER] ADC:1158, Pin:932 mV, Vbat:11930 mV ...
```

- **日志主体**来源 `body_samples`：free 取去重后最高频消息样本前 3；无 dedup（low）时退回热点位置前 3。这就是"当前是握手相关打印"这类人话判断的依据
- `token_links` 按 `(file, line)` 去重，同一处打印只报一次
- HTML 报告顶部结论块由 `gen_report.py summarize()` 生成，**与 `build_conclusion` 同一口径**（关联工程 / 结论 / 阶段 / 日志主体 / code_links / token_links / 未能对到源码说明 / 热点挂代码行）

## 6. 什么时候必须问、什么时候不用问

| 场景 | 是否问分析方式 | 说明 |
|------|----------------|------|
| 后台采集 + **设了结束条件**（duration / end-time / stop-pattern） | **必须问**（第五问），`--analysis-mode` 硬门禁 | 脚本不带即 `exit 1`，防 AI 幻觉 |
| 后台采集 + **有特殊要求**（`--focus`） | 问方式 + 问特殊要求，**不问强度**（铁律 1） | `--analysis-depth` 不传也放行；传了脚本会置 None |
| 后台采集 + `unlimited` | 启动时也问；不传则门禁后兜底 `auto`+`medium`，手动发邮件时再问一次 | |
| 采集中途发快照邮件（`capture_cmd mail`） | 问，可覆盖启动时默认 | 传 `--analysis-mode` / `--depth` / `--focus`；有 `--focus` 则 `--depth` 被忽略 |
| Web 实时模式点"保存日志"并发邮件 | 前端弹窗：**先问特殊要求，填了就不再弹强度** | `POST /dump` 带 `analysis_mode`/`depth`/`focus`；有 focus 时 `depth` 置 None |
| 只看不发的分析（手动跑 analyze_log.py） | 由 AI 询问后带 `--mode` | |

工程关联（第八问）同理：**只在 config `[projects]` 没有 `default` 时才问**；有 default 自动关联、不问；无 default 且用户不回答 → 结论不按工程来。

## 7. 交互话术（照抄）

> 分析方式要选一个：
> **1) 固定格式分析**（DAB_BOX 固件日志，按 模块/级别/内容 聚合，能定位到 file:line）
> **2) 自由格式分析**（SoC/BSP 裸打印，按消息形状去重 + 关键词分级）
> **3) 让 AI 按日志当前格式自动判定**（推荐，不确定就选这个）
>
> 有没有特殊要求？比如"只分析握手相关打印"——填了的话**严格按这条要求分析，强度就不问了**（邮件正文只分析这部分，HTML 报告仍是全量）。
>
> 没有特殊要求才问强度：**低**（只看异常）/ **中**（结论+热点+明细，推荐）/ **高**（全维度聚合）。
> **任何强度都会分析 ERROR 与 WARN**，强度只影响其他章节的详略。
>
> （仅当 config `[projects]` 没写 `default` 时才问）**这次分析关联哪个工程？**给我编号或工程根目录绝对路径；
> 不回答的话，结论就只基于日志本身，不会定位到源码/函数。

## 8. 命令用法

```bash
# 没有特殊要求 -> 才给 --depth（三档都必然分析 ERROR/WARN）
python -u "$SKILL_DIR/scripts/analyze/analyze_log.py" <log> --mode auto --depth medium \
    --md-out 分析.md --json-out 分析.json

# 有特殊要求 -> 只给 --focus，不给 --depth（强度不生效）
python -u "$SKILL_DIR/scripts/analyze/analyze_log.py" <log> --mode auto --focus "HandShake" \
    --md-out 分析.md --json-out 分析.json

# 工程关联: 不传 --project = 用 config [projects] default(当前 2); 无 default 时用户答复后传
python -u "$SKILL_DIR/scripts/analyze/analyze_log.py" <log> --mode auto --depth medium --project 2 \
    --md-out 分析.md --json-out 分析.json
python -u "$SKILL_DIR/scripts/analyze/analyze_log.py" <log> --project "d:\path\to\project" ...   # 或直接路径
python -u "$SKILL_DIR/scripts/analyze/analyze_log.py" --list-projects                            # 查注册表

python -u "$SKILL_DIR/scripts/analyze/gen_report.py" <log> --analysis 分析.json --out 报告.html [--max-lines 20000]
```

末行打印会体现实际生效口径：

```text
[分析] 方式=fixed 强度=low     总行=300 分析范围=300 ERROR=6 WARN=17
[分析] 方式=free  强度=不生效(按特殊要求) 总行=39 分析范围=4 ERROR=0 WARN=0
```

## 9. 相关

- 分析强度（低/中/高 + 两条铁律）：[analysis_depth.md](analysis_depth.md)
- 采集结束条件与自动发邮件：[../SKILL.md](../SKILL.md)
