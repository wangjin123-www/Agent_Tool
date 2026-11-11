---
version: 4.4.0
author: wangjin0115
company: cviauto
name: proto-toolkit
description: 通信协议工具链（数据源为飞书多维表格 Bitable），按平台宏路由。读取理解（read/query/show）、拉取快照（pull → base_raw.json 唯一提交物，解析在内存完成，自带检测统计）、代码生成（gen → C / AUTOSAR ARXML）、兜底修复（fix）。Use when user wants to 看懂/查询协议、接口/结构体/枚举/错误码/服务及其关联闭包，or mentions 协议表、protocol、查协议、接口详情、消息id、参数、struct 成员、enum 取值，or says 拉协议/导出json/base_raw/生成代码/生成 .h .c/生成 arxml/自动修复/修复表/协议变更了拉下来看差异/检测不通过。表结构维护与 Base 治理（字段转单选、检测公式、删视图、建表/迁数据、文档块）走 references/base-maintenance.md 的受控写 SOP。校验与日常格式修复在多维表格（检测公式 + 建议列 + 自动回填 workflow）；能多维表格实现的就在多维表格实现，skill 做表格实现不了的（raw 快照 + 内存解析 + 模板生成 + 批量兜底修复）。新增协议内容：对话里问清服务/结构/枚举等语义后直接写正式表（检测公式与自动回填把关），无需中间问答表。所有交互命令行传参，无 AI 问答。
---

# proto-toolkit

通信协议工具链：从飞书多维表格读取协议、导出可 diff 的 JSON 快照、自动修复表数据、生成 C / ARXML 代码。

## 表结构（2026-11-09 表优化定稿，5 张表）

表 id 与字段名见 `config/proto_config.json`（本文不重复抄写，避免文档与配置分叉）。表职责：

| 表 | 表 id | 说明 |
|---|---|---|
| 服务接口 | tbl1YV1OxMxG3kLm | **纯接口表**：每行一个接口，`服务名`/`命名空间`/`服务id`/`服务描述` 是普通列（不是 link）。主字段=`接口名`（保证 link 字段引用时显示接口名而非服务名）。无接口的预留服务也保留行，接口字段留空待补 |
| 数据结构 | tblsDjXiMxUOPGCx | 结构体与枚举合并，`种类`=结构体/枚举；`子项` link 指向子项表 |
| 数据结构子项 | tblxbsN0Al9ad3o6 | 成员变量与枚举值合并，`子项类型`=枚举值 的为枚举值，其余为结构体成员。字段分组：`字节序号(B)` / `位宽(bit)` / `长度`（变量长度：标量=1、`[n]` 数组=1024/64，非枚举值行必填）/ `Bit范围`（公式，闭区间 `字节×8 ~ 字节×8+位宽×长度-1`） |
| 错误码 | tbl858ZfyLwPOMvj | 独立表，接口用 `引用错误码组` 关联 |

（原「自动修改协议」问答表已退役删除，2026-11-09：新增协议内容改为对话确认语义后直接写正式表。）

服务接口表共 79 行 = 71 条接口行（`接口名` 非空）+ 8 条只有服务信息的预留行（BacklightSrv/AdasSrv/BodySrv/HvacSrv/SeatSrv/SafetySrv/DiagSrv/VehicleSignalSrv，接口字段全空待补）。reader 按 `接口名` 是否为空分流，服务由全部行的 `服务名` 去重聚合，`interface_names` 按行归属统计。

结构体/子项表按 `种类`/`子项类型` 分流回 structs / enums / members / enum_values，对外模型与合并前一致。

## 核心链路（v4.2）

```
                        ①pull（API）
多维表格 ─────────────────────▶ base_raw.json   ← 唯一提交物（git）
                                      │
                                      └─ ②内存解析 ──▶ protocol.json 形态的 dict
                                                        ├─ check  判定 ❌/⚠️
                                                        ├─ ③gen  → codegen/<lang>/generated/
                                                        └─ fix / read / query / show
```

**只有一份 JSON**：`base_raw.json` 是唯一落盘产物与唯一真源；解析在内存里完成，不落中间文件。

- `base_raw.json` = API 原始记录（record_id、link id、检测公式原文），稳定排序，提交 git。
- 协议表改了 → 重新 `pull` → `git diff base_raw.json` 直接看到表里改了什么。
- 解析逻辑（[pull.transform](scripts/pull.py)）只此一处，gen/check/fix 共用，不会各写一遍。
- 需要人工 review 解析结果时才 `pull --model` 额外导出 `protocol.json`（默认不落，不入 git）。

**检测约定**：每个实体带 `check` 字段（多维表格「XX正常性检测」公式原文）——`❌`=违规（阻断 gen）、`⚠️`=警告、`✅`/空=通过。业务性缺失（服务暂未定义接口、结构体暂未被引用）自动降级为警告，不阻断。表里加检测列 pull 自动带上。

## 铁律：表坐标与字段名只从 config 取，禁止硬编码

**任何脚本（含一次性诊断脚本）禁止硬编码 `tbl`/`vew`/`fld` 开头的 id，也禁止硬编码表内字段名。** 坐标走 `conf.tables()` / `conf.table(role)` / `conf.platform_cfg()`；字段名走 `schema.from_records()` / `schema.declared()` 拿到的语义键。

理由（2026-11-09 两次事故）：
- Base 重建「服务接口」表后 id 从 `tblHdNLTj7tfascd` 变成 `tbl1YV1OxMxG3kLm`，一次性脚本硬编码旧 id，lark-cli 只回 `not_found`；
- 表里字段从 `数组长度` 改名 `长度` 后，reader 硬编码旧名，**静默读到空**——`upgradeData`(1024) / `verArray`(64) 的数组长度全部丢失，且不报错。

### 字段语义映射（config `tables.<role>.fields`）

脚本里只写语义键（`msg_id` / `arr_len` / `interface_name` …），真实字段名声明在 config：

```json
"fields": {
  "msg_id":  ["消息id(16进制)", "消息id"],   // 候选名，按顺序兜底
  "arr_len": ["长度", "数组长度"]
}
```

两层保护：
1. **运行时**：[schema.from_records()](scripts/common/schema.py) 按 raw 记录里实际出现的键就地解析语义键 → 真实字段名。字段改名只要命中任一候选，就不会读成空；表为空等极端情况退回首选名。
2. **体检时**：`doctor` 拿线上 `+field-list` 核对声明；声明的名字全都不存在时按命名包含关系唯一推断，`doctor --fix` 回写 config（新名提首选、旧名留候选）。

`label_key` / `split.field` 的值是**语义键**不是字段名；`links` 声明「link 字段语义键 → 目标表 role」，doctor 会核对该 link 字段线上确实指向目标表。

### 降级规则（config `check_rules.degraded`）

「业务尚未定义、不阻断 gen」的 ❌ 项按表角色声明匹配串（如 `data_structure: ["引用接口为空", "子项为空"]`）。这些串匹配的是多维表格检测公式的**输出文本**，公式一改写就会静默失效（gen 突然被阻断，且报错看起来像协议问题），所以 `doctor` 会校验每个串仍能在该表的 formula 字段表达式里找到，找不到直接报 ERROR。

**动手前先体检：**

```powershell
python scripts/cli.py doctor          # 表 id / 字段语义 / link 目标 / split / 降级规则
python scripts/cli.py doctor --fix    # 回写失效表 id 与被改名的字段，改完 git diff 确认
```

`pull` 联网读表失败时会自动提示改用 `doctor --fix`。

### 不随表漂移、因此刻意保留在代码里的

- 基础类型位宽：`uint8=8 / uint16=16 / uint32=32`（协议常识，不是表数据）
- 语言类型映射：`uint8 → uint8_t`（C 语言知识）
- ❌/⚠️/✅ 的阻断语义、msg_id bit15 方向判定、C 命名规范（业务约定，表里无对应数据）

这些搬进 config 只是挪常量，不降低风险；真正会漂移的是字段名、表 id、split 选项，已全部配置化。

## 用法

```powershell
cd .claude/skills/proto-toolkit

# 理解协议（联网）
python scripts/cli.py read                     # 概览
python scripts/cli.py query <关键词>           # 搜索（含关联闭包）
python scripts/cli.py show interface <接口名>  # 定向：interface|struct|enum|error|service

# 离线（读 base_raw.json，不联网）
python scripts/cli.py read --from-raw output/base_raw.json

# 主体链路
python scripts/cli.py doctor                   # 先体检：config 表坐标 vs 线上 Base
python scripts/cli.py doctor --fix             # 表 id 失效则按表名自动重解析
python scripts/cli.py pull                     # 表 → base_raw.json（唯一提交物，自带 ❌/⚠️ 统计）
python scripts/cli.py pull --from-raw output/base_raw.json   # 用已有 raw 重跑（不联网）
python scripts/cli.py pull --model             # 额外导出 protocol.json 供人工 review
python scripts/cli.py fix                      # 预览自动修复计划（兜底：批量/点名场景，默认 dry-run）
python scripts/cli.py fix --apply              # 真正写表修复
python scripts/cli.py langs                    # 列出语言与状态
python scripts/cli.py gen --lang c             # raw → 内存解析 → C 代码
python scripts/cli.py gen --lang arxml         # → AUTOSAR ARXML
python scripts/cli.py gen --lang all           # 全部 ready 语言
```

`gen` 的路径参数接受 `base_raw.json` 或 `protocol.json`（自动识别形态）；缺省读 `output/base_raw.json`。检测统计已并入 `pull` 输出（原 `check` 命令退役）。**`gen` 缺省读本地快照、不联网**，会打印快照文件修改时间并提示先 `pull`；要生成前确保用最新数据，用 `gen --fresh`（先 `pull` 再 `gen`）或先手动 `pull`。

依赖：`lark-cli`（`--as user` 登录）、`python` + `jinja2`（C 生成用；`python -m pip install jinja2`）。

## 表内自动化（多维表格承担，2026-11-09 第十一批）

格式类修复已下沉到多维表格，skill 不再是日常修复入口：

| 表 | 建议列（formula） | 回填自动化（workflow，enabled） |
|---|---|---|
| 服务接口 | `消息id建议`（fldyCBkNNe，`0x%04X`） | `消息id格式自动回填` wkfo9S9hIasLUeUj |
| 数据结构子项 | `枚举值建议`（fldj1xDyDG，`0x%02X`） | `枚举值格式自动回填` wkfR0LFGuPAlRl7B |

机制：`ChangeRecordTrigger`（检测字段 isNotEmpty）→ `IfElseBranch`（原值 ≠ 建议值才写，防同值死循环）→ `SetRecordAction`（ref_info 引用触发记录，把建议列计算结果写回原字段）。回填后公式重算、检测转绿，链路自然终止。实测：注入 `102` → 30s 内自动修回 `0x0801`；注入 `0` → 自动修回 `0x00`；19 条常驻命名违规在场时零意外写入。

**已知边界**：已经非空的检测不会因公式更新/同值写入自动再触发（无变更事件）——改检测公式产生的存量问题需要一次真编辑才触发回填，平时靠 A2 每日体检兜底展示。

子项表检测公式同批补了「❌ 枚举值须0x开头十六进制」项（REGEXMATCH `^0[xX][0-9A-Fa-f]{1,2}$`），是子项表回填的触发源。

## 自动修复（fix）

**定位：兜底**——批量修复、用户点名修复、表内自动化覆盖不到的表。日常格式修复由上面的表内自动化接管。

只修**能确定性推导**的问题（语义类只报告，不猜）：

| 项 | 修复内容 |
|---|---|
| R1 消息id 规范化 | `801` / `0x801` → `0x0801`（4 位大写十六进制） |
| R2 枚举值规范化 | `1` / `0x1` → `0x01`（2 位大写十六进制） |
| R3 select 选项缺失 | 记录值不在字段选项内 → 补选项（**用 `+field-search-options` 取全量基集，绝不用会截断的 field-get options**，避免误删选项清空数据） |
| R4 类型别名规范化 | `uint8_t` / `int8` → `uint8` / `sint8` |

流程：`pull`（落 raw）→ `fix`（基于 raw 算差异，默认只预览）→ `fix --apply`（写表）→ 再 `pull` 复核。修复幂等，修完再跑 diff 为空。

> 表合并后「接口列表 / 所属服务」双向字段已取消（改为服务接口表内单向自关联 `归属服务`），故原 R5 双向回填不再适用。

## 代码生成（gen）

与 v2 完全一致：**jinja2 模板 + 语言注册表 + 插件化生成器**，模板零逻辑、StrictUndefined、两次渲染 md5 自检（确定性）。

- 语言注册表：`codegen/config/languages.json`（c=ready / arxml=ready / java=todo）
- 每种语言：`codegen/<lang>/{config,templates,generated}` + `scripts/gen/lang_<lang>.py` + 注册表一条
- C 产物：`Proto_Types.h`（结构体+位域访问器+Pack/Unpack 原型）、`Proto_Enums.h`、`Proto_CmdTable.c`（RX/TX 登记表，方向真源=msg_id bit15）、`Proto_CmdStub.c`
- ARXML 产物：`codegen/arxml/generated/CDC7255_Protocol.arxml`（AUTOSAR 4.2.2，DataType + Interface）
- 新增语言三步：建 `codegen/<lang>/` + 写 `scripts/gen/lang_<lang>.py`（签名 `generate(data, gcfg)`）+ 注册表加一条，不改 cli

`scripts/gen/object_view.py` 把扁平 protocol.json 包装成 v2 对象接口，供 arxml 等按对象属性访问的生成器复用。

### C 命名规范（2026-11-09 定案，方案 A）

表内名字即 C 名字，生成器**不再叠加类型前缀**；只有函数名保留 `Proto_` 辅助前缀：

| 对象 | 表内写法 | 生成物 |
|---|---|---|
| 结构体类型 | `PowerOffReqResult_t` | `typedef struct {...} PowerOffReqResult_t;` |
| 枚举类型 | `AccStatus_E` | `typedef enum {...} AccStatus_E;` |
| 枚举值 | `AccStatus_ACC_OFF`（枚举名去 `_E` + `_` + 值名） | `AccStatus_ACC_OFF = 0x00,` |
| 结构体成员 / 接口参数 | `powerOffReqResult`（lowerCamelCase） | 同名成员/参数 |
| Pack/Unpack、位域访问器 | — | `Proto_PowerOffReqResult_Pack(...)`（`helper_prefix`） |
| 命令 id 枚举 | — | `PROTO_CMD_<接口名>`（`cmd_enum_prefix`） |

配置项（`codegen/c/config/codegen_config.json`）：`struct_prefix` 已置空（类型名直接用表内名），新增 `helper_prefix: "Proto_"` 只作用于函数名。

**为什么必须这样**：C 的 typedef 名与变量名同属一个普通标识符命名空间。若结构体类型与其成员/参数同名（如参数 `PowerOffReqResult` 引用结构体 `PowerOffReqResult`），生成 `X X;` 后类型名被遮蔽，后续声明直接编译失败（MISRA C 2012 Rule 5.3）。类型名加 `_t`/`_E`、成员与参数用小驼峰即可从形态上根本区分。

表内三条命名检测公式（数据结构 / 服务接口 / 数据结构子项）负责守门，`pull` 会把结果带进 `check`，违规即阻断 `gen`。

## Base 表维护（写操作）

**改结构（字段 / 公式 / 视图 / 自动化）必须先在飞书「沙箱」里验证，不许直接改正式表**——沙箱是 Base 右上角 `···` 菜单里的隔离副本，验证通过一键更新线上，同步后立刻 `pull` + `gen` 复核。（`fix --apply` 改的是数据行，不受此限。）

字段类型改造（text→单选）、检测公式增删、删视图、建表/迁数据、文档块写入等结构性变更，**先读 [references/base-maintenance.md](references/base-maintenance.md)** 按受控流程执行。检测公式产出必须遵守 ❌/⚠️/✅ 语义（gen/fix 只认这个约定）。

## 平台宏机制

`config/proto_config.json` 的 `platform` 指定活动平台，实现按 `scripts/platforms/<module>/` 匹配。换平台 = 改配置 + 在新平台 reader 实现 `read_raw()` / `assemble_raw()` / `read()`。pull/fix/gen 是平台无关通用层。

新增平台三步：① `platforms` 下加一项声明 `module` 与数据源/表坐标；② 新建 `platform_<id>/reader.py`（实现 `read()`/`read_raw()`/`assemble_raw()`，实体带 `check`）；③ `platforms/__init__.py` 的 `_REGISTRY` 登记。

## 与历史版本的关系

v2（电子表格全生命周期 sync/edit/parse/gen/console/check）备份于 `.claude/skills-backup/proto-toolkit_20261108/`；其 protocol.json 契约（保序、双 id、无时间戳、可 diff）、C/ARXML 生成器（jinja2、模板零逻辑、确定性渲染、位域访问器）在 v4 完整继承。
v3 起数据源迁到多维表格；v4.0 建 pull/check/gen 链路；v4.1 三处对齐 v2（pull 拆出 raw 层、代码生成恢复 jinja2 + languages.json + arxml、新增 fix 自动修复改表）；**v4.2 去掉 protocol.json 中转**——raw 是唯一提交物，解析在内存完成直接喂 gen/check/fix，`--model` 才导出解析视图（已实测 5 个生成物与改造前逐字节一致）。校验规则仍由多维表格检测字段承担，skill 只判定与阻断。
