---
version: 2.0.0
author: wangjin0115
company: cviauto
name: proto-toolkit
description: 7255 MCU&SOC 通信协议表（飞书 YrK8sncCThe8UstV0yBcvkjQnMR）全生命周期工具。Use when user mentions "检查协议", "校验协议", "协议检查", "relink", "链接修复", "修改协议", "加接口", "加协约", "解析协议", "protocol.json", "生成代码", "协议代码生成", "命令表", "错误码", or asks to edit/verify the Service Interface / Data Structure / Parameter Enum / 错误码 sheets. 三能力：① sync 校验并直接修正（语义+分节行+链接 E1~E6 全量重算+枚举块边框/样式补齐；--dry-run 只报不改）；② edit 全参数化改表（add-interface/add-struct/add-enum/mod-interface/delete-interface 直接传参→默认直接写表，写完自动复跑 sync+parse）；③ parse 三表→protocol.json 并按 --lang 生成多语言代码（c 就绪 / java 插槽）。④ query 三表关联闭包查询 + console 本地可视化控制台（增删改查 / sync / parse / gen）。统一错误码独立成「错误码」子表，SI P 列 result 参数双向跳转。生成物 protocol.json / codegen/*/generated 禁手改。所有输入均命令行传参，无 AI 逐项问答；可视化需求走 console（本地页面，业务逻辑仍复用 edit apply / query）。
---

# proto-toolkit

7255 协议表（飞书）→ 校验并修正 → protocol.json 契约 → 按语言生成代码，一条命令链全覆盖。

## 初始化

```powershell
$SKILL_DIR = "<repo>\.claude\skills\proto-toolkit"
$PY = "$SKILL_DIR\utils\.venv\Scripts\python.exe"

# 首次/依赖变更：搭环境（建 venv + 装 jinja2/jsonschema，全隔离在 utils\ 内）
powershell -ExecutionPolicy Bypass -File "$SKILL_DIR\utils\setup_env.ps1"
```

lark-cli 需已登录（`lark-cli auth status`）。

## 命令（唯一入口 scripts\cli.py）

| 命令 | 能力 | 说明 | 退出码 |
|------|------|------|--------|
| `sync [--dry-run]` | ① 校验并修正 | 语义(S01~S17) + 分节行(规则27) + 链接 E1~E6 全量重算 + 禁止列多链清理 + 枚举块边框/样式补齐 + 服务块 A~D 合并校验 + 规则表对账(RUL)；缺失/漂移链接重写、多余链接清成纯文本、枚举块缺边框即补写、服务块合并不全即按块重做；`--dry-run` 只报不改 | 0=过，1=有错 |
| `sync --materialize` | ① 校验并修正 | 连带执行「可自动修」规则（当前 R23 枚举取值 `0xNN` 规整）；默认关，因为会改表 | 同上 |
| `sync --emit-fix <json>` | ① 校验并修正 | 把能算出的修法导出成 `edit_request.json`（当前 S17 复合参数→建 struct 三连 op），再走 `edit apply` 落表 | 同上 |
| `sync --freeze-rules` | ① 校验并修正 | 刷新 `config/rule_snapshot.json`（规则表 C 列正文 hash 快照），RUL 对账用 | 同上 |
| `edit add-interface <参数> [--dry-run] [--force]` | ② 修改协议 | 参数化加接口：`--service --direction --name --desc --if-type --tx-type --msg-id --pair-id --transport --qos --param`（可重复）；**默认直接写表** | 0 |
| `edit add-struct <参数> [--dry-run] [--force]` | ② 修改协议 | 参数化加 struct：`--name --service --namespace --desc --member`（可重复）；**默认直接写表** | 0 |
| `edit add-enum <参数> [--dry-run] [--force]` | ② 修改协议 | 参数化加枚举：`--name --msg-id --value`（可重复）；**默认直接写表** | 0 |
| `edit mod-interface <参数> [--dry-run] [--force]` | ② 修改协议 | 参数化改接口：`--name --set 列=值`（F/G/H/J/K/L/M/N/O/P/Q）；**默认直接写表** | 0 |
| `edit delete-interface <参数> [--dry-run] [--force]` | ② 修改协议 | **级联删**：`--name 接口名`。连带删对端接口（K 列互指方）、只被这批接口引用的 struct（DS 整块）与枚举（PE 整块）；仍被其他接口引用的保留并在计划里提示。`delete` 是唯一会 `+dim-delete` 行的 op，固定最后按行号自下而上执行 | 0 |
| `edit apply <json> [--dry-run] [--force]` | ② 修改协议 | 批量落表：**默认直接写表**；`--dry-run` 才只出计划（插入点/写入格/合并/删除/警告）。写前跑**预检**（`scripts/rules/precheck.py`，与 sync 同一套判据）；预检有 ERR 时拒绝写表，`--force` 可越过；写后自动复跑 sync + parse 刷新 | 0=过，1=预检拦截 |
| `query <关键词> [--json]` | ④ 查询协议 | 输入接口名/描述/msg_id/pair_id/服务名/struct 名/枚举名/C 常量名（`0x801`/`2049`/`801` 均可），迭代展开三表关联闭包到不动点，输出接口（含 SI 行号 + 飞书跳转）+ 被引用 struct/enum + 引用方；`--json` 落 `output/query_result.json` | 0 |
| `console [--port 8765]` | ④ 可视化控制台 | 起本地 `http.server`（默认 8765）托管 `utils/protocol_console.html` + JSON API：sync / 跳转校验报告 / parse / gen / 查询 / 增删改查表单；业务逻辑全部复用现成 `edit apply` 与 `query`，页面只做视图 | 0 |
| `langs` | ③ 解析协议 | 列出已注册语言与状态（c=ready / java=todo） | 0 |
| `parse [--lang c\|java\|all\|none]` | ③ 解析协议 | SI+DS+PE 三表 → `output/protocol.json`（含 revision 快照），然后按 `--lang` 生成代码；缺省按注册表 default（`c`），`none` 只出 json | 0 |
| `gen --lang <lang>` | ③ 解析协议 | 只生成代码（不重解析）：`codegen/<lang>/generated/` | 0 |
| `rule` | 辅助 | 打印「AI修订规则」子表原文 | 0 |

```powershell
& $PY "$SKILL_DIR\scripts\cli.py" sync            # 校验 + 自动修正
& $PY "$SKILL_DIR\scripts\cli.py" sync --dry-run  # 只看会改哪些
```

## 路由

- 「检查/校验一下协议」「链接挂了」→ `sync`（校验并直接修正，不需要再加 `--fix`）；
  只想看会改什么 → `sync --dry-run`。
- 「加协约/加接口/加 struct/加枚举」「改协议」「删接口」→ 直接拼 `edit add-interface|add-struct|add-enum|mod-interface|delete-interface`
  命令行（字段值全部当参数传），**默认直接写表**，不再预览确认；
  写完内部已自动复跑 sync + parse，无需再手动补跑。
  只想要计划不落表时才加 `--dry-run`；描述含英文逗号或一次要改多项时，改用 `edit apply <json>` 传文件。
- 「查一下某个接口/协议」「这个 struct 被谁用」→ `query <关键词>`（三表关联闭包，带行号与跳转）。
- 「可视化改协议」→ `console`（浏览器打开控制台，增删改查 + sync/parse/gen 按钮）。
- 「解析协议」「导出 json」→ `parse`（出 protocol.json；要只要 json 就 `parse --lang none`）；
  「生成 C 代码」→ `parse --lang c` 或 `gen --lang c`；「都生成」→ `parse --lang all`；
  「有哪些语言」→ `langs`。**语言必须由参数指定，不得反问用户后再临时实现新语言。**
- 「同步位域图」「Message Layout」→ 该能力已移除，直接 `sync` 即可（位域图子表不存在）。
- 用户只说「看看/问一下」→ `sync --dry-run` 或 `parse --lang none`，不执行任何写表。

## 规则注册表（检查与修改的唯一判据源）

`scripts/rules/` 是全部规范的单一真源。`sync`（全表检查）和 `edit apply`（写表前预检）
调同一套 `Rule`，不再各写一份判据。

| 文件 | 职责 |
|------|------|
| `rules/__init__.py` | `Rule` / `Issue` / `Ctx` / `RULES` / `register()`；入口 `run_sync` `run_precheck` `precheck_blocked` `emit_fix` `freeze` `apply_fix` |
| `rules/legacy.py` | COV 解析覆盖率对账 + 既有 6 个 checker 包成聚合 Rule（SEM / SEC / LNK / STY / S16 / MERGE） |
| `rules/basic.py` | 新增可修规则：S17 复合参数建 struct、R23 枚举取值格式 |
| `rules/precheck.py` | `scope="precheck"` 规则（PRE）：对未落表的 edit ops 做纯逻辑拦截 |
| `rules/drift.py` | 规则表对账（RUL）：代码 `rule_no` ↔ 「AI修订规则」子表序号 |

`Rule` 字段：`id`（检查码）/ `title` / `rule_no`（对应规则表序号，drift 用）/ `scope`
（`table` 全表 / `precheck` 写表前）/ `fixable` / `default`（`False` 表示需 `--materialize`）。

`Issue.fix` 是声明式修法，两种形态：`{"ops": [...]}`（转成 edit_request 走 apply）、
`{"cells": [...]}`（直接写格）。新增一条规范 = 在 `basic.py` 写 `detect` 并 `register`，
sync/edit 自动双向生效。

**修复路径只有一条**：checker 的 `report(ctx)` 只只读校验、`repair(ctx, sink)` 只把
「要写什么」塞进 sink（`writes` / `styles` / `merges`），真正写表统一由 `rules.apply_fix`
执行；dry 与否只由 `Rule.report` 判定，另有 `feishu.set_read_only` 闸门兜底——
dry-run 下任何写表调用直接抛 `ReadOnlyError`。

## 规则

- **真源唯一**：协议表是唯一真源；`output/protocol.json`、`codegen/*/generated/`
  全部是生成物，**禁手改**（下次 parse/gen/apply 即被覆盖）。
- **表格→json 双保险**（2026-10-31 定稿）：
  A 解析覆盖率对账——`parse_*` 把「行有内容但没进模型」的情况记进
  `proto.source.parse_stats.*.skipped`（行号+原因），sync 的 COV 规则汇总告警，
  杜绝静默丢行/错列读空/截断；
  B JSON Schema 契约——`config/protocol.schema.json`（draft-07 子集，执行器
  `scripts/model/jsonschema_lite.py`，无第三方依赖）在 `save()` 落盘前与 `load()`
  读入时双向校验（schema_version 1.1.0），违规抛 `SchemaError`，保护 gen 等下游。
- **全参数化，无 AI 问答**：修改协议用 `edit add-*`/`mod-interface`/`delete-interface` 传参，
  语言用 `--lang` 传参；不逐项问答。批量复杂的才落 JSON 文件给 `edit apply`。
  需要界面时用 `console`：`utils/protocol_console.html` 只做视图，所有写操作调用同一套
  `edit apply`，不新增第二条业务路径（页面按钮 = 命令行参数）。
- **手写代码不动**：`App_SocComSysCmd.h` 的 X-macro 清单仍是编译期真源；
  生成表只做比对视图，不直接编入工程（见 CLAUDE.md SOC 通信链）。
- **链接只认主键**：sync 重算链接按 struct 名/枚举首行/接口行定位，不存绝对 URL；
  base64 一律程序生成，禁手算。
- **消息 id 列不带链接**（2026-10-30 定稿）：SI J（消息 id）、PE E（Message Id）必须纯文本；
  枚举的双向链接只走「SI P 参数描述 ↔ PE A」与「DS K 成员描述 ↔ PE A」，
  struct 走「SI N ↔ DS C」，请求/应答走「SI K ↔ 对端 SI J」，
  统一错误码走「SI P result ↔ 错误码!A（COMM_RESULT 组首行）」；result 按规则 26
  进 struct 时，改走「DS K result 成员描述 ↔ 错误码!A」。
  其余列一律不允许挂链接，sync 会把多余链接清成纯文本。
- **枚举关联真源 = 描述列内链**：表里枚举参数的 O 列写的是基线标量（如 `uint8`），
  枚举归属只体现在「SI P / DS K 内链 → PE 枚举名首行」。解析时把链接解成枚举名存入
  `Param.enum_ref` / `Member.enum_ref`（`type` 保持原文本，C 产物不变），
  `resolve_type` 见 `enum_ref` 优先判 `enum`——只看 type 文本永远判不出枚举。
- **参数值域必须进 Parameter Enum**：SI P 列只放中文描述 + 枚举链接，禁止写
  `0=…/1=…`、`0x00:…` 这类内联值域；`add-interface` 用 `type=enum:枚举名` 会自动写
  `O=uint8` + `P` 链接；sync 的 S16 检查会标记 P 列内联值域。
- **统一错误码进「错误码」子表**：所有应答类接口的返回码参数（`N=result` / `O=uint8` /
  `Q=OUT`，且 P 列写「0=成功，非0=错误码」）的 P 列必须链到 `错误码!A2`（组 `COMM_RESULT`
  首行），错误码表 A2 反向链回首个引用行（E6）。表结构 A 错误码组 / B Value / C 常量名 /
  D 描述 / E 适用消息；取值 `0x00` 成功起、`0x01~0x07` 通用错误，命名 `COMM_*` 全大写。
  「0=OK，1=NOK」这类具体业务二值语义不算统一错误码，仍走 Parameter Enum。
- **复合参数必须建 struct**（规则 8/9/26，sync S17 强制检查）：一个接口的命令字载荷
  成员数 ≥2 时，**不得**在 SI 拆成多行 N/O 参数；必须在 Data Structure 建 struct，
  SI 只留一行 `N=数据结构名（链 DS C）/ O=struct（下拉）/ P 留空`，原多参数行
  **清空内容不删行**。典型反例（S17 会点名）：`SocPowerCtrlReqEvt{powerType,onOff}`、
  `McuPowerCtrlReqMtd{ctrlType,ctrlCmd}`、`TimeZoneSetMtd{sign,offsetSeconds}`。
  判定：同一接口有 ≥2 个参数且其中无 `struct` 类型 → S17 WARN（sync 只报不改，因为
  struct 名与成员语义需人工定；但 `sync --emit-fix out.json` 会按「接口名去 Mtd/Evt + 参数
  顺序」推导出 add_struct + clear_params + mod_interface 三连 op，人工确认后 `edit apply`
  一次落表）；`edit add-interface` 传 ≥2 个标量 `--param` 会被写表前预检直接拦下（ERR）。
  例外：多个**独立**参数（各自是不同物理量、非同一命令字载荷）才拆行，如 0x0108。
- **插行只允许自下而上**（+dim-insert），避免行号漂移；优先填块内缓冲空行。
- **接口参数落行**：第一个参数与接口同行（`N/O/P/Q` 与 `E` 同行），第 2 个起才另起参数行；
  每个接口占 `max(1, len(params))` 行，禁止「接口一行、参数下一行」。
- **枚举块样式**：A 列加粗左对齐、B/E 居中、C/D 左对齐、A~E 四周 `#1F2329` 细边框；
  `add-enum` 只写值，sync 按块比对并补齐边框/对齐。
- **分节行文案一字不改**：`▶ SOC → MCU · 下发/请求` / `▶ MCU → SOC · 上报/应答`。
  分节行**只是排版分组**（表格好看），不是方向真源；方向真源 = msg_id bit15
  （`0x8000` 置位 = MCU→SOC，如 0x8802；为 0 = SOC→MCU，如 0x0100），
  接口 `direction` 由解析层按 bit15 推导，所在分节位置不符只报 S03 排版 WARN。
- **服务块 A~D 纵向合并**：Service Interface 每个服务块（A 列服务首行 → 下一服务首行前一行，
  末块到最后内容行）的 A/B/C/D 四列必须各自**整块纵向合并单段**（`A{首}:A{末}`…`D{首}:D{末}`），
  只首行带值、其余行显示同值；插/删行不会自动扩展已有合并区，故写完表必须按块重算。
  `sync` 比对 `+sheet-info` 的 merged_cells 并在不一致时按块重做（先 unmerge 整块 `A{首}:D{末}`
  再逐列 merge，飞书不允许与既有合并重叠）；`edit` 落表后自动执行同一修复。
  漏合并的表现：块内每行重复显示服务名/服务 id/描述/命名空间（如「48 行起又是 power」）。
- **写表必校验**：任何写表（sync / apply）之后以退出码为准，非 0 不报"完成"。
- **写表前先预检**：`edit` 各命令（含 `delete-interface`）会在写表前先用 `scripts/rules/precheck.py`
  对**未落表的 ops** 跑一遍判据（与 sync 同一套 Rule），有 ERR 时拒绝落表；确要强写才加 `--force`。
  默认直接写表，`--dry-run` 只出计划。
- **配置即真值**：token/sheet_id/列映射只在 `config/proto_config.json`；
  语言清单/默认语言/status 只在 `codegen/config/languages.json`；
  各语言的输出路径/命名/前缀只在 `codegen/<lang>/config/codegen_config.json`；脚本零魔法值。
- **生成器插件化**：语言 = `scripts/gen/lang_<lang>.py` + `codegen/<lang>/` + 注册表一条；
  新语言照 `codegen/java/README.md` 三步接入，不改 `cli.py`。
- **确定性生成**：gen 渲染两次 hash 必须相同（脚本自检），否则中止。

## 状态

- 表 revision 1144（2026-11-01）；13 服务 / 65 接口 / 14 struct / 22 枚举；错误码 1 组 8 条。
  （2026-11-01 删除「Message Layout」子表与 DS G 列位域布局，DS 列 G~K = 字节序号/位/成员/类型/成员描述。）
- 已知遗留数据问题（sync 报 ERR，待表侧修）：
  `SocFanQueryMtd(0x0801)`、`SocFanCtrlMtd(0x0802)` 都单指 `0x8802`，
  而 `SocFanSpeedEvt(0x8802)` 的关联 id（K 列）为空。
- 产物：`output/protocol.json` + `output/_writes_*.json`（临时）；
  `codegen/c/generated/{Proto_Types.h, Proto_Enums.h, Proto_CmdTable.c, Proto_CmdStub.c}`。

## 目录

```
proto-toolkit/
├── SKILL.md / README.md
├── config/proto_config.json        # 表坐标/列映射/分节文案（唯一配置源）
├── config/protocol.schema.json     # protocol.json 契约（校验手段 B，save/load 双向拦）
├── scripts/
│   ├── cli.py                      # 唯一入口
│   ├── common/{conf,log,feishu}.py # 配置 / Report / lark-cli 封装
│   ├── model/protocol.py           # protocol.json 数据模型
│   ├── parse/sheet_reader.py       # SI+DS+PE 三表解析
│   ├── check/{semantics,sections,links,blocks}.py
│   ├── rules/                      # 规则注册表（唯一判据源）
│   │   ├── __init__.py             # Rule/Issue/Ctx + run_sync/run_precheck/emit_fix/freeze
│   │   ├── legacy.py               # 既有 checker → 聚合 Rule 适配器
│   │   ├── basic.py                # 可修规则 S17 / R23
│   │   ├── precheck.py             # 写表前预检（scope=precheck）
│   │   └── drift.py                # 规则表对账 RUL + 快照 freeze
│   ├── edit/{request_builder,apply}.py  # 命令行参数→请求 / edit_request.json 落表引擎
│   └── gen/{__init__,lang_c,lang_java}.py  # 语言分发 + C 生成器 + Java 插槽
├── codegen/
│   ├── config/languages.json       # 语言注册表（--lang 取值 / 默认语言 / status）
│   ├── c/{config,templates,generated}   # C 语言插槽（就绪）
│   └── java/{config,templates,generated} + README.md   # Java 插槽（待实现）
├── utils/{setup_env.ps1, requirements.txt, .venv/}
└── output/                         # protocol.json + 中间产物
```
