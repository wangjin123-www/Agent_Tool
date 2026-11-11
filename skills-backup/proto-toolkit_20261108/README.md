# proto-toolkit

7255 MCU&SOC 通信协议表（飞书 `YrK8sncCThe8UstV0yBcvkjQnMR`）全生命周期工具：
检查 → 修改 → 解析 → 生成。

## 一句话

协议表是唯一真源；sync 是按「表该怎么长」重算全表并直接修正（语义+链接+枚举块样式+服务块合并）；
parse 把三张子表固化成 `protocol.json` 契约；gen 按 `--lang` 生成对应语言代码
（当前 C 就绪、Java 留插槽）。`protocol.json` / `codegen/*/generated/` 均为生成物，禁手改。

## 环境搭建（一次性）

前置：Python 3.10+（本机 3.13 可用）、lark-cli 已安装且 `lark-cli auth status` 已登录。

```powershell
$S = "D:\wnagjin\Compay_Project\CDC_7255\cdc_7255\.claude\skills\proto-toolkit"
powershell -ExecutionPolicy Bypass -File "$S\utils\setup_env.ps1"
```

脚本在 `utils\.venv\` 建独立虚拟环境并安装 `jinja2`、`jsonschema`
（清单见 `utils\requirements.txt`），全部隔离在 skill 目录内，不污染系统 Python。
装完自检打印两库版本即成功。

## 使用

```powershell
$PY = "$S\utils\.venv\Scripts\python.exe"

& $PY "$S\scripts\cli.py" sync            # ① 校验并修正：语义+链接重算+枚举块样式+服务块合并
& $PY "$S\scripts\cli.py" sync --dry-run  # ① 只报不改（看会动哪些格）
& $PY "$S\scripts\cli.py" sync --materialize           # ① 连带执行可自动修的规则（会改表，默认关）
& $PY "$S\scripts\cli.py" sync --emit-fix out/fix.json # ① 把可修的改动导出成 edit_request，再 edit apply
& $PY "$S\scripts\cli.py" sync --freeze-rules          # ① 刷新规则表正文快照（确认检查器已跟上规则后）

& $PY "$S\scripts\cli.py" edit add-interface --service PowerMgr --direction "SOC→MCU" `
    --name 接口名 --desc 描述 --if-type "method(rr)" --tx-type event `
    --msg-id 0x0109 --pair-id 0x8109 --transport uart --qos level1 `
    --param name=mode,type=enum:某枚举,io=IN,desc=模式            # ② 直接写表
& $PY "$S\scripts\cli.py" edit add-struct --name Struct名 --service PowerMgr `
    --namespace power --member byte=0-1B,bit=,name=成员,type=uint16,desc=描述
& $PY "$S\scripts\cli.py" edit add-enum --name 枚举名 --msg-id 0x0109 `
    --value value=0x00,c_name=C常量,desc=描述
& $PY "$S\scripts\cli.py" edit mod-interface --name 接口名 --set K=0x0802
& $PY "$S\scripts\cli.py" edit delete-interface --name 接口名   # 级联删（对端 + 专属 struct/枚举）
# 以上命令默认直接写表，只想看计划才加 --dry-run；批量请求走 JSON：
& $PY "$S\scripts\cli.py" edit apply edit_request.json

& $PY "$S\scripts\cli.py" query PowerMgr       # ④ 三表关联闭包（接口/struct/枚举 + 行号 + 跳转）
& $PY "$S\scripts\cli.py" query 0x0801 --json  # ④ 结果落 output/query_result.json
& $PY "$S\scripts\cli.py" console --port 8765  # ④ 本地可视化控制台（增删改查 / sync / parse / gen）
# 或直接双击 start_console.bat（自动用 .venv 解释器，默认端口 8765）

& $PY "$S\scripts\cli.py" langs              # 列出已注册语言（c / arxml=ready，java=todo）
& $PY "$S\scripts\cli.py" parse --lang c     # ③ 三表 → protocol.json，并生成 C 代码
& $PY "$S\scripts\cli.py" parse --lang arxml # ③ 生成 AUTOSAR ARXML（DataType + Interface）
& $PY "$S\scripts\cli.py" parse --lang all   # ③ 生成全部 ready 语言
& $PY "$S\scripts\cli.py" parse --lang none  # ③ 只出 protocol.json，不生成代码
& $PY "$S\scripts\cli.py" gen --lang c       # ③ 只生成代码（不重解析）
& $PY "$S\scripts\cli.py" gen --lang arxml   # ③ 只生成 ARXML
& $PY "$S\scripts\cli.py" rule            # 打印「AI修订规则」子表
```

**改协议表的固定动作**：`edit add-interface/add-struct/add-enum/mod-interface/delete-interface`
**直接传参即落表**（内部已自动复跑 `sync`（链接 + 服务块合并）+ `parse`）→
需要代码时用 `parse --lang c`（或 `gen --lang c`）。只想看不写才加 `--dry-run`。

**语言选择是参数，不是交互**：`--lang` 取值来自 `codegen/config/languages.json`；
不带 `--lang` 时按注册表 `default`（当前 `c`）生成；`--lang none` 只出 protocol.json；
未注册的语言直接报错并列出可用值；`java` 目前 status=todo，调用会打印接入四步。
`arxml` 的版本/命名空间/包名/范围在 `codegen/arxml/config/codegen_config.json`，
默认 AUTOSAR 4.2.2 + DataType/Interface，详见 `codegen/arxml/README.md`。

### edit_request.json 契约

```json
{"ops": [
  {"kind": "add_enum",  "name": "枚举名", "msg_id": "0x0109",
   "values": [{"value": "0x00", "c_name": "C常量名", "desc": "描述"}]},
  {"kind": "add_struct","name": "Struct名", "service": "PowerMgr", "namespace": "power",
   "desc": "描述",
   "members": [{"byte": "0-1B", "bit": "", "name": "成员", "type": "uint16", "desc": "描述"}]},
  {"kind": "add_interface", "service": "PowerMgr", "direction": "SOC→MCU",
   "name": "接口名", "if_type": "method(rr)", "desc": "描述", "tx_type": "event",
   "msg_id": "0x0109", "pair_id": "0x8109", "transport": "uart", "qos": "level1",
   "params": [{"name": "参数名", "type": "uint8|struct:名|enum:名", "io": "IN", "desc": "描述"}]},
  {"kind": "mod_interface", "name": "接口名", "fields": {"K": "0x0802"}}
]}
```

- `byte` 区间：`0B` / `0-3B` / `4-NB`（开放尾）；`bit`：`0-7` 或空
- 单请求可混合多 op；apply 按 add_struct → add_enum → add_interface/mod_interface 顺序处理，
  SI 插行自下而上防行号漂移，struct/枚举同包定义可被接口参数直接引用
- `mod_interface.fields` 可改列：F(描述) G(类型) H(发送类型) J(消息id) K(关联id) L(传输层) M(QoS) N(参数名) O(参数类型) P(参数描述) Q(方向)
- `clear_params`：`{"kind":"clear_params","name":"接口名","count":N}` 清空该接口第 2~N 个参数行的 N~Q（规则 26：行保留不删），与 S17/`--emit-fix` 配套
- `delete_interface`：`{"kind":"delete_interface","name":"接口名"}` 级联删——SI 接口块（接口行 + 参数行）+ 对端接口（K 列互指方）+ 只被这批接口引用的 struct（DS 整块）/ 枚举（PE 整块）；仍被其他接口引用的 struct/enum 保留并在计划里提示。它是唯一会 `+dim-delete` 的 op，固定放到最后按行号自下而上执行（插入位移先补齐）

## 三能力

| # | 能力 | 命令 | 内容 |
|---|------|------|------|
| ① | 校验并修正 | `sync [--dry-run] [--materialize] [--emit-fix <json>] [--freeze-rules]` | 语义 S01~S17（id 唯一/方向位 bit15/服务号/^0x8000 配对/struct 引用/枚举命中/字节空洞/Size 对账/位宽/内联值域/复合参数未建 struct）、链接 E1~E3/E5~E6 全量重算 + 禁止列多链清理、服务块 A~D 纵向合并（不全即按块重做）、规则表对账（RUL）；`--dry-run` 只报不改；`--materialize` 连带执行可自动修规则（当前 R23 枚举取值规整）；`--emit-fix` 把能算出的修法导出成 edit_request；`--freeze-rules` 刷新规则快照 |
| ② | 修改协议 | `edit add-interface` / `add-struct` / `add-enum` / `mod-interface` / `delete-interface` / `apply [--dry-run] [--force]` | 全参数化（无 AI 问答）：命令行直接给接口名/描述/参数/成员/枚举值 → 拼 edit_request.json → **写表前预检** → **默认直接写表**；`--dry-run` 才出计划。预检有 ERR 时拒绝写表（`--force` 可越过）；插行自下而上、删行整体最后自下而上、id 编码约束、struct 参数写法均由引擎保证，写完自动复跑 ①③。`delete-interface` 是级联删：目标接口块 + 对端接口 + 只被这批接口引用的 struct/enum |
| ③ | 解析协议 | `parse --lang c\|java\|all\|none` / `gen --lang …` | SI+DS+PE → `protocol.json`（数组保序、id 双份、revision 快照、不存 URL）；按 `--lang` 分发到 `scripts/gen/lang_<lang>.py`，C 用 jinja2 渲染 4 文件（StrictUndefined + 双渲染 hash 自检），Java 当前为插槽（status=todo） |
| ④ | 查询与可视化 | `query <关键词> [--json]` / `console [--port 8765]` | `query` 按接口名/描述/msg_id/pair_id/服务名/struct/枚举/C 常量展开三表关联闭包（迭代到不动点），输出接口 + SI 行号 + 飞书跳转 + struct/enum 及引用方；`console` 起本地 `http.server` 托管 `utils/protocol_console.html`，页面上做增删改查与 sync/报告/parse/gen 按钮，业务逻辑全部复用 `edit apply` 与 `query` |

## 规则注册表（检查与修改统一调用）

`scripts/rules/` 是全部协议规范的单一真源：`sync` 做全表检查、`edit apply` 做写表前预检，
**调的是同一套 `Rule`**，不再各写一份判据——加一条规范只改一处，检查和修改自动同时生效。

| 文件 | 职责 |
|------|------|
| `rules/__init__.py` | `Rule` / `Issue` / `Ctx` / `RULES` / `register()`；对外只暴露 `run_sync` `run_precheck` `precheck_blocked` `emit_fix` `freeze` |
| `rules/legacy.py` | 既有 6 个 checker 原样包成聚合 Rule（SEM / SEC / LNK / STY / S16 / MERGE），输出逐字不变 |
| `rules/basic.py` | 新写的细粒度可修规则：S17 复合参数建 struct、R23 枚举取值 `0xNN` |
| `rules/precheck.py` | `scope="precheck"` 的 PRE 规则：拦截尚未落表的 edit ops |
| `rules/drift.py` | RUL 规则表对账：代码 `rule_no` ↔ 「AI修订规则」子表序号 + 正文快照 |

- `Rule` 字段：`id`（检查码）/ `title` / `rule_no`（规则表序号，drift 用）/ `scope`
  （`table` 全表检查 / `precheck` 写表前）/ `fixable` / `default`（`False` = 需 `--materialize`）。
- `Issue.fix` 是声明式修法，两种形态：`{"ops": [...]}`（转成 edit_request 走 apply）、
  `{"cells": [...]}`（直接写格）。
- 检查码新增两类：`PRE`（写表前预检）、`RUL`（规则表对账）。

## 链接契约（sync 重算的五对 + 禁止列）

| 对 | 正向 | 反向 | 依据 |
|----|------|------|------|
| E1 | SI P 列（参数描述）→ PE A 列（Enum Type 首行） | PE A → SI P | 规则 8 |
| E2 | DS K 列（成员变量描述）→ PE A 列 | PE A → DS K | 规则 8 |
| E3 | SI N 列（struct 参数）→ DS C 列（数据结构名） | DS C → SI N | 规则 26 |
| E5 | SI K 列（关联 id）→ 对端 SI J 列 | 对端互通 | 规则 15/10 |
| E6 | SI P 列（result 返回码）→ 错误码 A 列（COMM_RESULT 首行）；result 按规则 26 进 struct 时改走 DS K 列（result 成员描述）→ 错误码 A 列 | 错误码 A → SI P / DS K | 规则 15/9/26 |

**复合参数必须建 struct**（规则 8/9/26，sync S17 强制检查）：一个接口的命令字载荷
成员数 ≥2 时不得在 SI 拆成多行 N/O 参数，须在 Data Structure 建 struct，SI 只留一行
`N=数据结构名（链 DS C，E3）/ O=struct / P 留空`，原多参数行清空内容不删行。
S17 只报不改（struct 名与成员语义需人工定）；`edit add-interface` 传 ≥2 个标量
`--param` 也会告警。多个**独立**参数（不同物理量，如 0x0108 IC/IVI 电源状态）才拆行。

**统一错误码**：`错误码` 子表（A 错误码组 / B Value / C 常量名 / D 描述 / E 适用消息），
预置 `COMM_RESULT` 组 8 条（`0x00 COMM_OK` 成功 … `0x07 COMM_ERR_INTERNAL` 内部错误）。
命中条件（两处等价，取其一）：
- SI 行 `N=result` / `O=uint8` / `Q=OUT` 且 P 列含「成功」或「错误码」
- DS 行 `J=result` / `K=uint8` 且 L 列含「成功」或「错误码」（result 进 struct 后）

「0=OK，1=NOK」这类具体业务二值语义不算统一错误码，仍走 Parameter Enum。
判据与链接文案在 `config/proto_config.json` 的 `error_code` 段。

**禁止挂链接**：SI J 列（消息 id）、PE E 列（Message Id），以及以上 E1~E3/E5~E6 未覆盖的任何列。
发现即报 `LNK` 错，`--fix` 把该格重写成纯文本（保留原文案）。

比对只认「目标 sheet_id + 目标 A1」，文案差异不算错；`--fix` 缺失/漂移即重写。
枚举反链目标由其引用源推导（SI P / DS K 的前向链接），一枚举多引用时取参数描述并告警。

## 多语言代码生成（新增语言三步）

语言选择只走参数：`parse --lang c` / `gen --lang c` / `parse --lang all`；`langs` 列出全部。

1. 建目录 `codegen/<lang>/{config,templates,generated}`，照 `codegen/c/config/codegen_config.json`
   填 `protocol_json` / `output_dir` / `file_names`。
2. 写生成器 `scripts/gen/lang_<lang>.py`，导出 `generate(proto, gcfg, root) -> list[str]`
   （模板用 `jinja2.StrictUndefined`，渲染两次比 md5 保证确定性）。
3. `codegen/config/languages.json` 注册一条，`status` 由 `todo` 改 `ready`。

Java 插槽已按此建好（`codegen/java/README.md` 写明接入四步），现在调用会报
「生成器尚未实现」并打印待办，不会静默产出空文件。

## 目录

```
proto-toolkit/
├── SKILL.md                        # 技能主入口（路由/规则/状态）
├── config/proto_config.json        # 表坐标/列映射/分节文案
├── scripts/
│   ├── cli.py                      # 唯一入口：sync|edit|parse|gen|langs|rule
│   ├── common/                     # conf（配置/A1 工具/语言注册表）log feishu（lark-cli 封装）
│   ├── model/protocol.py           # Protocol/Service/Interface/Struct/Enum 数据模型
│   ├── parse/sheet_reader.py       # 三表解析（A~D fill-down/字节区间/方向 bit15）
│   ├── check/                      # semantics + sections + links（relink）+ blocks（A~D 合并）
│   ├── rules/                      # 规则注册表（检查与修改共用的唯一判据源）
│   │   ├── __init__.py             # Rule/Issue/Ctx + run_sync/run_precheck/emit_fix/freeze
│   │   ├── legacy.py               # 既有 checker → 聚合 Rule 适配器（输出不变）
│   │   ├── basic.py                # 可修规则 S17（建 struct）/ R23（枚举取值）
│   │   ├── precheck.py             # 写表前预检（scope=precheck）
│   │   └── drift.py                # 规则表对账 RUL + 快照 freeze
│   ├── edit/                       # request_builder.py（CLI 参数→请求）+ apply.py（落表引擎）
│   └── gen/                        # __init__.py（语言分发）+ lang_c.py + lang_java.py（插槽）
├── codegen/
│   ├── config/languages.json       # 语言注册表（--lang 取值 / 默认语言 / status）
│   ├── c/                          # C 语言插槽
│   │   ├── config/codegen_config.json  # 输出目录/文件名/前缀（改这里不改脚本）
│   │   ├── templates/*.j2          # types_h / enums_h / cmd_table_c / cmd_stub_c
│   │   └── generated/              # 生成物，禁手改
│   └── java/                       # Java 插槽（骨架 + README 接入四步，尚未实现）
│       ├── config/codegen_config.json
│       ├── templates/  generated/
│       └── README.md               # 怎么把 protocol.json 转 Java 的约定
├── utils/                          # setup_env.ps1 + requirements.txt + .venv
└── output/                         # protocol.json + 临时 writes
```

## 排错

| 现象 | 处置 |
|------|------|
| `缺少 jinja2` | 没跑 setup_env.ps1，或没用 `utils\.venv\Scripts\python.exe` 执行 |
| lark-cli 输出非 JSON | `lark-cli auth status` 检查登录；重试一次，别反复 |
| sync 报 `S05 单向指配` | 表侧 K 列数据问题：两边要互指且满足 `^0x8000`，人工修表后重跑 |
| 链接修完又漂 | 表里插/删了行 → 正常，`sync` 就是干这个的；改表优先填缓冲空行 |
| sync 报 `[MERGE]` 合并不全 | 服务块 A~D 未整块合并（块内每行重复显示服务名/id/描述/命名空间）；非 dry-run 会自动按块 unmerge+merge 重做 |
| 页面出现「48 行起又是 power」 | 同上：合并区没覆盖到块尾；`sync` 一次修好，`--dry-run` 只报不改 |
| `模板渲染不确定` | gen 自检失败即中止，查模板是否用了 `now()`/随机类调用 |
| PE 枚举名解析成多组 | A 列合并单元格只在首行带值，检查表里合并是否被破坏 |
| `sync` 报 `[RUL] 规则表有 N 条规则未被任何检查项覆盖` | 规则表新增了判据但检查器还没跟上：属流程约束可先忽略；要落地就在 `scripts/rules/basic.py` 写 Rule 并 `register()`，再 `sync --freeze-rules` |
| `sync` 报 `[RUL] 规则正文已变更` | 规则表 C 列被改过，确认检查器判据仍匹配后 `sync --freeze-rules` 刷新快照 |
| `预检有 N 项错误，拒绝落表` | `edit apply` 被 `rules/precheck.py` 拦下：按提示改 edit_request（如 ≥2 标量参数要改成一个 `struct:名`）；确要强写加 `--force` |
