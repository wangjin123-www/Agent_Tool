# 模块：串口日志采集与分析

> embedded-data-analysis（嵌入式数据分析）的串口日志模块（原独立 skill `serial-log`，2026-10-26 并入）。
> 由顶层 [../../SKILL.md](../../SKILL.md) 按意图路由进入；本文件不再带 skill frontmatter。

## 日志格式规范（固定格式）

```text
[timestamp][level][file:line] [module] message
```

- level **全称**：`DEBUG` / `INFO` / `WARN` / `ERROR`（兼容旧固件无 level 字段、旧缩写 D/I/W/E）
- 解析正则：`^\[(\d+)\](?:\[(DEBUG|INFO|WARN|ERROR|D|I|W|E)\])?\[([^\]:]+):(\d+)\]\s*\[([^\]]+)\]\s?(.*)$`

示例：

```text
[12345678][INFO][Service_Com.c:277] [COM] SendWithAck success count=5
[12345679][ERROR][Service_Com.c:1059] [COM] COM_Resp_Handshake send failed: ret=0x00000016
[12345680][Service_Com.c:300] [COM] 旧格式无level也兼容
```

## 工程关联（结论必须落到代码，v2.5）

**结论不是只说"有 0 个 ERROR"，而要说出"当前在打什么、这行打印来自哪个工程的哪个文件/函数"。**

### 工程注册表：config `[projects]`

```ini
[projects]
# 编号 = 工程根目录绝对路径
1 = d:\wnagjin\Compay_Project\DAB_BOX\DAB_BOX_CODE\dabbox_app
2 = d:\wnagjin\Compay_Project\CDC_7255\cdc_7255
# 默认工程编号: 分析时自动关联它(当前 = 2)
default = 2
```

**默认工程决定行为（不许含糊）**：

| config 有 `default` | 行为 |
|---------------------|------|
| **有** | 分析**自动**关联该工程：结论与源码出处都基于该工程，无需再问 |
| **无**（留空/注释掉） | **每次分析前 AI 必须先问用户"本次关联哪个工程（给绝对路径或编号）"**；用户答复→带 `--project` 重启；**用户不回答 → 分析结果与结论都不按工程来**（只基于日志本身，并显式写明"未关联工程"） |

- 查询注册表：`python "$SKILL_DIR/scripts/capture/capture_serial.py" --list-projects`（打印编号→路径，标出 `<- 默认`；并提示"未设置默认工程 → 每次分析需询问"）
- 采集启动时脚本会打 `[工程] 关联 2 = <路径>  (config 默认)`；若无默认且未传 `--project`，会打提示块要求 AI 先问用户
- 指定方式：`--project 2`（编号）或 `--project "d:\path\to\project"`（绝对路径）

### 反查机制（怎么把日志对到代码）

固定格式的四个字段**全部用来定位工程**（时间戳/level/file:line/module/内容）：

| 日志字段 | 用途 |
|----------|------|
| `file:line`（如 `Service_Com.c:1239`） | **主路径**：在工程里按文件名建索引 → 定位源文件 → 取该行 + **向上找所在函数** + **所属代码模块**（最近两级目录，如 `L1_APP/APP_Tuner`）（`locate_fixed`/`module_of`） |
| `打印内容` | **辅助路径**（自由格式主路径）：从最高频打印里提字段标识符（如 `AppPowerHsmState`、`InAmp`）→ 在工程源码**仅打印行**里检索出出处（`grep_project`） |
| `[module]` / `level` | 参与阶段语义推断（`SEMANTIC_HINTS`：文件名/函数名关键词 → 中文阶段，如 `HandShake/PowerHsm` → "MCU<->SoC 握手/通信"） |
| `timestamp` | 时间跨度/时间桶（high 强度） |

**模块漏斗定位（v2.6）**：反查按漏斗收敛范围，每条定位结果带 `[定位: via]` 标注——
- **内容验真（先于一切）**：`locate_fixed` 命中的源码行做**接口名无关**验真（`src_msg_affinity`：字符串字面量按 `%d/%s` 格式符切段，字面段按序出现在日志样本中才算同源；接口改名不影响）。验真失败 → `[定位: 内容不符(疑同名文件误命中)]`，不宣称模块内定位、不挂调用方——防两工程同名文件把注释行当打印出处
- **ERROR/WARN 热点 → 异常全局反查**：无条件全工程反查 + 调用方检索（`find_callers`，跨模块调用方排前），异常常是跨模块因果（打印点 ≠ 触发者）
- **常规热点 → 模块内(层级/模块)**：`locate_fixed` 命中且行有效且验真通过即成；行号失效（版本不一致）才降级 **全局兜底**
- **模块上下文**：热点最多的前 3 个模块聚合出"该模块在干什么"（热点数/level 分布/代表样本），供逻辑范围定位
- **free 多命中分组**：token 命中按文件模块分组，同模块 ≥2 个命中优先（消除跨模块同名打印歧义），详见 [references/analysis_modes.md](references/analysis_modes.md) §5.5


- 自由格式没有 `file:line`，所以走"打印字段 → 工程打印语句"这条路；字段名取不到（纯数字/第三方库打印）时会明确写"未能把日志对到工程源码"，**不编造**
- 结论里"当前在打什么"= 最高频打印（`日志主体(最高频打印, 即判定依据)`），这就是"当前是握手相关打印"这类人话结论的依据

### 结论正文长什么样

```text
关联工程: 2(config 默认) = d:\wnagjin\Compay_Project\CDC_7255\cdc_7255
【结论】未发现 ERROR/WARN, 主要阶段: 电源状态机(上电/唤醒/休眠) / 电源管理 / MCU<->SoC 握手/通信 (按文件名/函数名判断); 这段日志是设备正常输出。
日志主体(最高频打印, 即判定依据): InAmp=0,ExAmp=0,AvAmp=0! | IcPwrSta=0,IviPwrSta=0,StrPin=0! | AppPowerHsmState=2
固定格式热点已定位到工程源码(file:line -> 文件:行, 所在函数):
  Service_Com.c:1239 -> CVI_McuPlatform/.../Service_Com.c:1239, 函数 COM_Resp_Handshake()
        源码: MCU_Printf("COM_Resp_Handshake send failed: ret=0x%08X\r\n", ret);
日志打印字段在工程源码中的出处(按字段名检索打印语句):
  AvAmp -> CVI_McuPlatform/L1_APP/APP_Power/App_PowerHsm.c:1774, 函数 App_Power_MuteMainFunction()
        源码: MCU_Printf("InAmp=%d,ExAmp=%d,AvAmp=%d!\r\n", ...);
```

同一段落口径也写进 HTML 报告顶部结论块（`gen_report.py summarize()`），邮件正文/HTML 结论**一致**。

## 交互入口

**`$0` 为空时必须让用户选择，禁止直接执行。**

**`$0` 有值时路由：**

| 参数 | 说明 |
|------|------|
| ports | 列串口 |
| live | 实时查看模式（Web 界面） |
| record | 后台写入模式 |
| analyze | 固定格式分析 |
| analyze_free | 任意格式 AI 自由分析 |

`SKILL_DIR="$(git rev-parse --show-toplevel)/.claude/skills/embedded-data-analysis/modules/serial-log"`（模块根；脚本内部用 `Path(__file__).parent.parent.parent` 自定位到同一路径，模块整体搬移不影响脚本）

## 启动采集前强制交互（两项都必须问，不许默认执行）

**第一项：模式**

| 模式 | 命令 | 说明 |
|------|------|------|
| 实时查看 | `serial_monitor.py` | Web 界面 http://localhost:8765 持续滚动（内存保存，不写log）。**启动只起服务、不碰串口**；串口下拉+刷新、波特率手填+下拉候选、自动检测波特率、连接/断开、查看详情 全部在网页操作。另有：level彩色标签、WARN/ERROR行下即时分析、自动滚动开关、点击选中行、"保存日志"按钮（弹窗选默认/自定义路径dump）、仅看WARN/ERROR、关键词过滤、**5A A5 协议帧按字节流重组并 HEX 显示（跨行/帧内 0x0A 也能重装）+ "隐藏5A A5"开关（只隐藏帧、保留日志）**、assets/ 图做背景 |
| 后台写入 | `capture_serial.py` | 无界面安静采集，压测/长稳用 |

**第二项：日志输出（record 模式必问；live 模式界面里随时点"保存日志"选择）**

- 默认：`output/logs/serial_时间戳.log`
- 落盘格式：每行行首带主机时间戳 `[YYYY-MM-DD HH:MM:SS.mmm] `（**写文件那一刻拼接**，内存/网页实时显示不带；Web 保存与后台采集同一格式，分析脚本读取时自动剥掉）
- 自定义路径：用户给，传 `--out`

**文件归档约定（v2.3，`output/logs/` 根目录只留"正在采集"的主 log）**：

| 位置 | 内容 | 命名 |
|------|------|------|
| `output/logs/`（根） | **仅**正在采集的主 log | `serial_<开始时间>.log`（只有开始时间） |
| `output/logs/完成采集/` | 采集结束（正常/异常）归档的主 log | `serial_<开始>_结束<结束>.log` |
| `output/logs/告警/` | 告警邮件附的快照副本 | `serial_<开始>_告警<HHMMSS>.log` |
| `output/logs/快照/` | 采集中手动发邮件的快照副本 | `serial_<开始>_快照<HHMMSS>.log` |
| `output/logs/分析/` | md/json/html 分析产物 | `serial_<开始>..._分析.md/.json/.html` |
| `output/logs/ctl/` | status.json / cmd.json / 看门狗日志（`<log名>.ctl/` 目录） | — |

- 采集**结束即归档**：脚本把主 log 改名带上结束时间（`_结束YYYYMMDD_HHMMSS.log`）并移入 `完成采集/`；根目录那份"正在采集"名随即消失（下次采集写全新主 log）
- Web"保存日志"落盘同样带结束时间，默认落 `完成采集/`；自定义完整路径则原地写、不搬进 skill 目录
- 非主 log（告警/快照/分析/ctl）一律落对应中文子目录，**不许直接堆在 `logs/` 根目录**

**--confirm 硬门禁（v2.1）**：用户明确答复两项之前，脚本不带 `--confirm` 会直接拒绝启动（exit 1）。即使用户说"直接跑"，也必须先完成两项确认再带 `--confirm` 启动——这是防止 AI 偷懒跳过交互的脚本级强制，不许绕过。`--list` / `--detect-baud` 属查询，无需门禁。

**波特率规则（v2.2，血的教训：921600 假设让采集 23 秒 0 字节）**：

- **禁止凭历史记忆/上一次配置假设波特率**——波特率跟设备走不跟串口线走，同一根 CH340 可能从 DAB_BOX(921600) 换接到 SoC(115200)
- config.conf 里的 port/baud 仅作参考展示，不作为启动依据
- **record（后台采集）启动命令必须带 `--auto-baud`**：脚本先按给定波特率收 5 秒，0 字节自动逐档检测并切换（要求设备正在打日志），从机制上消灭猜错
- **live（Web）不在启动时定波特率**：启动只起服务；波特率在网页里手填、从下拉候选选、或用"自动检测波特率"按钮（试错法，要求设备正在打日志），点"连接"时才打开串口
- **波特率下拉候选来自 config**：config.conf `[serial] bauds`（逗号分隔，从低到高），默认内置常用档 9600~3000000；网页输入框仍可手填任意值
- 采集启动后 10 秒仍 0 字节：立即怀疑波特率/接线/设备静默，跑 `--detect-baud` 或问用户，**不要**归因为"设备没打日志"就干等

## 实时查看流程（live）

1. **启动前不用找串口/波特率**：启动只起 Web 服务，不打开串口（`--port`/`--baud` 仅作网页的预选/默认值，可完全省略）
2. 启动（**非阻塞**，确认两项后带 --confirm）：

```bash
python -u "$SKILL_DIR/scripts/web/serial_monitor.py" --confirm
# 可选: --port COM6 只把 COM6 作为网页下拉的预选项; --web-port 8766 换端口
```

3. 浏览器打开 http://localhost:8765（脚本已自动打开，`--no-browser` 可关）。**串口操作全部在网页顶部工具条完成**：

| 网页控件 | 说明 |
|----------|------|
| 串口下拉 + 刷新 | 下拉列出系统串口（`GET /ports`，点"刷新"重新扫描）；无串口时提示先去插线 |
| 波特率 输入框 + 下拉候选 | 可手填任意值，也可从 config `[serial] bauds` 的候选档位选（`GET /bauds`，默认 9600~3000000）；默认 921600 |
| 自动检测波特率 按钮 | 试错法检测（`POST /detect_baud`，要求设备正在打日志）；成功后自动填入波特率框；检测需独占串口，已连接时须先断开；**检测中（约20秒）按钮变为"停止检测"，再点即 `POST /detect_stop` 中止**（最迟 1.8 秒生效，弹窗提示"已手动停止"） |
| 连接 / 断开 按钮 | `POST /connect` / `POST /disconnect`；连接**只用波特率框里的值直连**（`auto_baud:false`，不探测）；不知道波特率就先点"自动检测波特率"按钮检测并回填，再点连接；状态灯显示 `已连接 COM6 @ 921600` 或错误原因（`GET /conn`，网页每 3 秒轮询） |
| 查看详情 按钮 | 弹出诊断（`GET /diag`）：逐项说明"为什么未连接/当前错误"——串口服务、系统串口数量、目标串口是否存在、连接状态、串口占用探测、最近错误；弹窗底部「后台采集」区块（`GET /captures`）列出正在跑的 record 采集（端口/波特率/pid/行数/WARN/ERROR/心跳），每项带「停止后台采集」按钮 |
| 停止后台采集 按钮 | 详情弹窗内，停掉正在跑的 record 采集以释放串口给本网页。**双重确认**：①警告弹窗（说明会统计+归档为 `_完成采集.log`、串口释放后网页才能连接）→ ②最后确认弹窗（"不可撤销"）→ 才 `POST /stop_capture`（body `{"ctl":"<log名>.ctl"}`），走 cmd.json `{"cmd":"stop"}` 让采集进程自行收尾。下发后弹窗内轮询 `GET /captures` 直到该采集消失，提示"串口已释放" |
| 背景 | `assets/` 目录里的图片（`GET /bg` 取第一张，`GET /assets/<file>` 取图）；放图进目录并刷新即换背景，目录空则纯色；读取带路径穿越防护 |

**用户想自己双击打开（不经过 AI）**：双击 `嵌入式_超级串口工具.bat`（或 `嵌入式_超级串口工具.bat COM9` 只把 COM9 预选到下拉框，仍需在网页点"连接"）。
bat 只做「起服务 + 自动开浏览器」，**不找串口、不检测波特率**。
**分析能力不受影响**：网页"保存日志"仍在进程内自动跑 `analyze_log.py` + `gen_report.py` 并发信，与 AI 模式一致；
只有「AI分析选中」必须回 TRAE 对话里让 AI 读 `output/logs/ctl/selection_pending.json`。

4. **选中分析**：用户点选日志行 → 点"AI分析选中" → 内容写入 `output/logs/ctl/selection_pending.json` → 用户在对话里说一声 → AI 读该文件分析 → `POST http://localhost:8765/ai_result`（body: `{"text":"分析内容"}`）→ 网页顶部显示分析结果
5. **保存日志**：用户在网页点"保存日志"按钮 → 依次弹窗：①路径（留空=默认 `output/logs/完成采集/serial_开始时间_结束时间.log`，**文件名带结束时间**）→ ②是否发飞书邮件（确定=发送）→ ③选了发送则继续弹 **分析方式**（1 固定 / 2 自由 / 3 自动判定，推荐 3）→ ④**特殊要求**（可选正则，如 `HandShake`，填了则邮件正文只分析匹配行，HTML 仍全量，**且不再问强度**）→ ⑤**仅当特殊要求留空时**才弹 **分析强度**（1 低 / 2 中 / 3 高，三档都必然分析 ERROR/WARN）→ ⑥**是否关联工程**（留空=用 config `[projects] default`；config 无 default 且留空 → 本次结论不关联工程代码）。POST /dump 落盘并发信（附件=日志+分析HTML，正文=分析摘要含工程关联/结论/源码出处）。**停止时不再自动dump**，提醒用户先保存
6. 用户说"停"：先确认已保存（未保存则提醒先点"保存日志"）→ StopCommand → 问是否"分析并发邮件"（**同时问分析方式/特殊要求；特殊要求留空才问强度；config 无 `[projects] default` 时还要问工程**）
7. **统计接口** http://localhost:8765/stats ：返回 total/warn/error 数与最近 error/warn 明细，供 AI 回答"有没有 error/warn"

## 后台写入流程（record）

1. **四问（都要问，不许默认）**：串口号 / 波特率（不确定走检测）/ 日志输出（默认或自定义）/ **结束条件**
2. 结束条件四选一（第四问，**必须显式声明**，脚本 `--end-cond` 门禁强制；可组合 --stop-pattern 与时长类）：

| 选项 | 参数 | 说明 |
|------|------|------|
| A. 无限采集直到手动停 | `--end-cond unlimited` | 必须原样告知用户"进程不会自行结束，只能靠你手动停" |
| B. 采集时长 | `--end-cond duration --duration 秒` | |
| C. 结束时间点 | `--end-cond end-time --end-time HH:MM` | 24h 制，已过算明天 |
| D. 读到某日志停止 | `--end-cond stop-pattern --stop-pattern "正则"` | 如升级完成标志 |

3. **分析三问（第五/六/七问；设了结束条件时启动前必须问，脚本硬门禁）**

设了结束条件（B/C/D）＝结束会自动发邮件，所以**启动前**就要问清分析口径，不许默认：

| 问 | 参数 | 选项 | 说明 |
|----|------|------|------|
| 五、分析方式 | `--analysis-mode` | `fixed` / `free` / `auto` | fixed=固定格式(module/level/内容三维聚合)；free=自由格式(形状去重+关键词分级)；auto=按日志格式自动判定，**推荐** |
| 六、特殊要求 | `--focus`（可选） | 正则，如 `HandShake` | 填了则**严格按此要求分析，强度不生效**（不问第七问）；邮件正文只分析匹配行（全量仍计入总数），**HTML 报告仍为全量** |
| 七、分析强度 | `--analysis-depth` | `low` / `medium` / `high` | **仅在没有特殊要求（未给 `--focus`）时才问/才必填**。low=只看异常；medium=结论+热点+明细（**推荐**）；high=全维度聚合。**三档都必然分析 ERROR 与 WARN**（强度只裁剪其他章节） |

**工程关联（第八问，只在 config `[projects]` 没有 `default` 时才问）**：

- config 有 `default`（当前 = `2`）→ **不问**，脚本自动关联该工程，启动时打印 `[工程] 关联 2 = <路径>  (config 默认)`
- config 无 `default` → **必须先问"本次分析关联哪个工程？给我编号或工程根目录绝对路径"**：
  - 用户答复 → 带 `--project <编号|路径>` 启动
  - 用户不回答 → **照常采集，但分析结果与结论都不关联工程**（只基于日志本身），结论里显式写"未关联工程"
- 查候选：`capture_serial.py --list-projects`；启动若没传且无默认，脚本会打 `[工程]` 提示块提醒 AI 先问

**两条铁律（优先级最高，高于所有门禁）**：

1. **有特殊要求 → 强度不生效**：用户给了 `--focus` 就严格照做，**不问强度、传了也忽略**。脚本门禁**不再要求** `--analysis-depth`（只查 `--analysis-mode`），有 focus 时内部把深度置 None，结论段打印 `强度: 不适用(已按你的特殊要求执行, 强度不生效)`
2. **无论哪个强度，ERROR 和 WARN 都必须分析**：三档 `err_n`/`warn_n`/`top` 均非 0；HTML 里 WARN/ERROR 每一行恒挂分析块（`note_all = True`）。强度只影响热点条数/模块分布/时间桶/去重明细

- **硬门禁（v2.4）**：设了结束条件时，`--analysis-mode` 不传 → 脚本打印"拒绝启动: 未声明 xxx" 并 **exit 1**；`--analysis-depth` 仅在**没有 `--focus`** 时必填。这是把交互要求下沉到脚本，防 AI 幻觉跳过
- 命令示例：有特殊要求 `--analysis-mode auto --focus "HandShake"`（**不带** `--analysis-depth`）；无特殊要求 `--analysis-mode auto --analysis-depth medium`
- `unlimited` 场景门禁不生效（因为不自动发邮件）：先兜底 `auto`+`medium`，等用户手动发邮件时再问一次
- 详细定义见 [references/analysis_modes.md](references/analysis_modes.md) 与 [references/analysis_depth.md](references/analysis_depth.md)

4. 启动（非阻塞，`python -u`，带 --confirm --auto-baud --end-cond --analysis-mode；无特殊要求再带 --analysis-depth）：
   - **`--project` 一般不用传**：config `[projects]` 有 `default`（= 2）时脚本自动关联；**只有 config 无 `default` 且用户答复了工程时才传** `--project <编号|路径>`

```bash
# 无特殊要求（带 --analysis-depth）
python -u "$SKILL_DIR/scripts/capture/capture_serial.py" --port COM6 --baud 921600 --out 路径 --confirm --auto-baud --end-cond <A|B|C|D> --analysis-mode <fixed|free|auto> --analysis-depth <low|medium|high> [--duration N | --end-time HH:MM | --stop-pattern "xxx"]

# 有特殊要求（不带 --analysis-depth，强度不生效）
python -u "$SKILL_DIR/scripts/capture/capture_serial.py" --port COM6 --baud 921600 --out 路径 --confirm --auto-baud --end-cond <B|C|D> --analysis-mode <fixed|free|auto> --focus "正则"

# config 无 default 时，用户答复了工程 -> 追加 --project
python -u "$SKILL_DIR/scripts/capture/capture_serial.py" ... --analysis-mode auto --analysis-depth medium --project 2

# 查工程注册表
python "$SKILL_DIR/scripts/capture/capture_serial.py" --list-projects
```

5. **停止 / 发邮件语义（严格区分，违反=事故）**：

**用户说"发邮件"（没说停止）→ 绝对不许停采集**。用固定工具发当前快照，采集继续：

```bash
python "$SKILL_DIR/scripts/capture/capture_cmd.py" <log路径> mail ["备注"] [--analysis-mode fixed|free|auto] [--depth low|medium|high] [--focus 正则] [--project 编号|路径]
# mail = 复制当前 log 为 快照/xxx_快照HHMMSS.log, 按所选方式/强度出分析(正文摘要+HTML附件), 采集进程继续跑, 不中断
# 本次不传参数则沿用采集启动时的默认(含 --project: 不传=用 config default)
# 铁律: 带 --focus 时 --depth 不生效(脚本会提示已忽略), 严格按 --focus 分析; 三档都必分析 ERROR/WARN
# 工程: config 无 default 时必须先问用户, 答复后带 --project; 不回答则本次结论不关联工程代码
```

**用户说"停止采集" → 按此顺序，不许跳步**：

```bash
python "$SKILL_DIR/scripts/capture/capture_cmd.py" <log路径> stop    # ①请求停止(脚本统计+归档主 log 到 完成采集/)
# ②读脚本输出, 先向用户报告 ERROR/WARN 行数与明细
# ③再问"要发邮件吗"; 同意的话同时问分析方式/特殊要求(特殊要求留空才问强度) → 用 analyze_log.py 出分析
# ④附件 = 完成日志 + 分析 HTML, 正文含分析摘要 → 发完才说结束
```

- `capture_cmd.py <log路径> status` 或 `capture_cmd.py --list` 查看采集状态，不会打断采集
- **禁止**用 StopCommand 停采集进程（进程内收尾/备份不会执行）

5. **结束保障（脚本级，AI 不参与判断，防幻觉）**：
   - 正常结束（Ctrl+C / 时长到 / 时间到 / 关键字命中 / `capture_cmd stop`）→ 脚本自动把 log 改名带结束时间并移入 `完成采集/`：`xxx_结束YYYYMMDD_HHMMSS.log`（需求 4）
   - **预设结束条件达成（时长 / 结束时间 / 命中关键字）→ 脚本自动发完成邮件**（`[已完成] 串口采集结束`，**附件 = `完成采集/xxx_结束<时间>.log` + `分析/xxx_分析.html`，正文 = 分析摘要**），**不依赖 AI 记得发**（需求：设了结束条件就默认发）
     - 分析口径用启动时的 `--analysis-mode` / `--analysis-depth` / `--focus`；有 `--focus` 时**强度不生效**（严格按 focus 分析），且只裁剪正文，HTML 仍全量；**ERROR/WARN 无论何种口径都必分析**
     - 分析失败（如 `--focus` 正则非法）不影响发信：正文写"分析未生成"，附件仍带 log
   - 手动停止（Ctrl+C / `capture_cmd stop`）**不发**完成邮件 → 由 AI 先报 ERROR/WARN 再问用户是否发
   - **异常中断（拔线 / 崩溃 / 进程被强杀 / 假死）→ 独立看门狗 `capture_watchdog.py` 自动备份 + 发飞书邮件**。看门狗由 `capture_serial.py` 自动以独立进程拉起，判据全部来自 `output/logs/ctl/<log名>.ctl/status.json`，不看 AI 说法：
     - `state=RUNNING` 但 pid 已消失 → 异常中断
     - 心跳超时 15s → 进程假死
     - 读到 `state=DONE` / `ABNORMAL` → 正常退出，不发异常邮件
     事件记录：`output/logs/ctl/<log名>.ctl/watchdog_events.log`
   - 采集进程与看门狗**双保险**：进程内异常（串口拔出）走进程内发信；进程直接消失走看门狗发信
   - 看门狗启动失败时输出会打 `[看门狗] 启动失败`：此时 AI 停完进程必须手动 `copy` log 为 `完成采集/xxx_结束<时间>.log`
   - 采集启动即打印 `[看门狗] 已启动(异常中断将自动备份并发邮件)`，没这行就说明保障缺失，要检查

## 停止后：分析 + 报告 + 邮件（用户同意才发）

**先问（不许默认）**：分析方式（fixed/free/auto）/ 特殊要求（可选，正则）/ 分析强度（low/medium/high，**仅在特殊要求留空时才问**）/ 工程（**仅 config `[projects]` 无 `default` 时才问**，见上文"工程关联"——有默认自动用，无默认且用户不回答则不按工程分析）。
**两条铁律**：① 有特殊要求就不问强度、强度不生效，严格照用户要求分析；② 无论哪个强度，ERROR 与 WARN 都必须分析。

```bash
# 1. 分析: 出 邮件正文摘要(md) + 结构化结果(json)  [抗万行, 输出条数由 --depth 控制]
#    结论会关联工程代码(自动用 config default; 无 default 则须用户答复后带 --project)
#    无特殊要求:
python "$SKILL_DIR/scripts/analyze/analyze_log.py" <log> --mode auto --depth medium \
    --md-out output/logs/分析/分析.md --json-out output/logs/分析/分析.json
#    有特殊要求(不给 --depth, 强度不生效):
python "$SKILL_DIR/scripts/analyze/analyze_log.py" <log> --mode auto --focus "HandShake" \
    --md-out output/logs/分析/分析.md --json-out output/logs/分析/分析.json
#    指定工程(config 无 default 时):
python "$SKILL_DIR/scripts/analyze/analyze_log.py" <log> --mode auto --depth medium --project 2 \
    --md-out output/logs/分析/分析.md --json-out output/logs/分析/分析.json

# 2. 生成 HTML 报告(level着色/Ctrl+F检索/WARN/ERROR行后带分析块)
python "$SKILL_DIR/scripts/analyze/gen_report.py" <log> --analysis output/logs/分析/分析.json --out output/logs/分析/报告.html

# 3. 发飞书邮件(收件人=当前飞书账号, 抄送=config.conf [mail] cc, 附件=报告html+原始log)
python "$SKILL_DIR/scripts/common/send_mail.py" "串口日志分析报告 <摘要>" "<分析.md 内容>" output/logs/分析/报告.html <log>
```

邮件规则（不许违反）：
- **附件必须含 HTML 报告 + 原始 log 两个**（用户已投诉过只有 .log 没有 html）
- **正文必须是分析摘要**（含结论/level 分布/热点/明细），不是"见附件"
- **结论必须关联工程代码**：写明关联了哪个工程、当前主要阶段（"在打什么"）、日志主体（最高频打印）、以及热点/字段在工程里的 `文件:行, 函数`；未关联工程时须显式说明原因
- **ERROR/WARN 必须出现在正文里**（任何强度都分析异常，三档都不许省）
- 有 `--focus` 时：正文只分析匹配行，**HTML 仍全量**，**强度不生效**
- 邮件配置：`config/config.conf`（example 同目录）。抄送默认为空=只发自己

## 分析流程

- **analyze**：`analyze_log.py <log> --mode fixed|free|auto [--depth low|medium|high] [--focus 正则] [--project 编号|路径]`
  - 固定格式：按 module / level / 内容(形状去重) 三维聚合，热点用 `file:line` **反查工程源码（文件:行 + 所在函数 + 源码行）**
  - 自由格式：消息形状归一化去重 + 关键词分级 + 关键状态行；用**打印内容里的字段名**反查工程里的打印语句
  - 结论含：关联工程 / 人话结论（有无异常 + 主要阶段）/ 日志主体（最高频打印）/ 源码出处；未关联工程时显式说明
  - **两条铁律**：① 带 `--focus`（特殊要求）时**强度不生效**，严格按 focus 分析；② 无论 `--depth` 哪一档，**ERROR 与 WARN 都必须分析**
  - `--list-projects` 查工程注册表；`--project` 不传=用 config `[projects] default`，无 default 则须先问用户
  - 详见 [references/analysis_modes.md](references/analysis_modes.md) 与 [references/analysis_depth.md](references/analysis_depth.md)
- `parse_fixed.py <log>`（旧工具，仍可用于快速统计）：level/模块分布、WARN/ERROR热点top10、drop_cnt专项；`--min-level WARN --module COM IAP --errors-only` 过滤

## 串口打开失败（拒绝访问）

```bash
python "$SKILL_DIR/scripts/common/find_com_holder.py" COM6           # 查占用(句柄优先)
python "$SKILL_DIR/scripts/common/find_com_holder.py" COM6 --kill    # 用户确认后结束真凶(仅杀句柄命中的)
python "$SKILL_DIR/scripts/common/find_com_holder.py" COM6 --no-probe  # 跳过打开测试, 纯句柄查询
```

**判定顺序（v2.7，防"按进程名误报"）**——旧版第一层按进程名关键词匹配就直接报"疑似占用"，会把只是名字里带 `data center`/`串口` 的无辜进程当成元凶（实测 `Data Center.exe` 根本没占 COM6，真凶是 python）。现改为：

1. **句柄精确查询**：`handle64.exe` 按注册表 `SERIALCOMM` 映射的 NT 设备名（如 `\Device\Serial19`）搜句柄 → 命中即真凶，输出"句柄精确命中"
2. **打开测试（金标准）**：句柄查不到时，用 pyserial 独占打开该口——**能打开 = 未被占用**（直接下结论，不再猜进程名）；**打开被拒 = 真被占**，只是没定位到持有进程
3. **进程名匹配仅作"未验证参考"**：只在"打开被拒且句柄查不到"时才列，且明确标注`仅供参考(未验证句柄, 不一定是它)`，绝不当成占用结论；`--kill` 也只杀句柄命中的进程

坑（实测）：
- **真凶常是自家进程**：Web 服务 `serial_monitor.py` 或 `capture_serial.py` 连上串口后，COM 口就被它们占着——`--list` 看不到、但句柄查询会点到它。启动 record 前若报"拒绝访问"，先查自家有无 Web/采集进程在跑
- 串口助手最小化到托盘无窗口标题，须扫全进程
- CH340 拔插后 COM 号会变，先 `--list` 确认
- handle64.exe 首跑 EULA 弹窗超时，重跑一次即可（脚本带 -accepteula）；句柄查询需管理员权限，无权限时降级到"打开测试 + 未验证参考"（不会误报）

## 固件端（level 输出 / drop counter / 移植其他项目）

见 [references/firmware_porting.md](references/firmware_porting.md)：DAB_BOX 加 level 全称前缀的最小改法、drop counter、可移植 ServiceLog 常驻模块、纯串口配置。

## 参考文档（references/）

| 文档 | 内容 |
|------|------|
| [analysis_modes.md](references/analysis_modes.md) | 分析方式 fixed/free/auto 定义、**两条铁律**（focus 优先于强度、异常必分析）、**工程关联反查（fixed 用 file:line / free 用打印字段）与结论口径**、消息形状归一化、万行策略、focus 与 HTML 差异约定 |
| [analysis_depth.md](references/analysis_depth.md) | 分析强度 low/medium/high 定义（DEPTH_PRESETS 全表）、**有 focus 时强度不生效（FOCUS_PRESET）**、各强度正文章节对照、规模无关性 |
| [firmware_porting.md](references/firmware_porting.md) | 固件端 level 输出 / drop counter / 移植指南 |

## 配置

`config/config.conf`（不入库，example 为模板）：
- `[serial] port/baud`：上次串口参数
- `[serial] bauds`：网页波特率下拉候选（逗号分隔，从低到高；默认 9600~3000000）。仅作下拉候选项，输入框仍可手填任意值
- `[mail] enabled/cc`：邮件开关与抄送人
- `[projects] 编号=工程根目录绝对路径` + `default=默认编号`：**工程关联注册表**（分析结论据此定位到源码文件/函数）。当前 `1`=DAB_BOX、`2`=CDC_7255、`default = 2`
  - `default` 有值 → 分析自动关联，不问用户
  - `default` 留空/注释掉 → **每次分析前必须先问用户用哪个工程**；不回答则结论不关联代码（只基于日志本身）
  - 查询：`capture_serial.py --list-projects`

## 素材（assets/）

`assets/` 目录用于放网页自定义素材，目前支持背景图（`.png/.jpg/.jpeg/.webp/.gif/.bmp`）：
- 放图片进 `assets/` 后刷新网页即换背景，按文件名排序取第一张作为默认背景
- 目录为空则用纯色背景
- 用户要换背景只需往该目录丢图（或删掉旧图），无需改代码
