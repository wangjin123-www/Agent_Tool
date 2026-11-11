# Base 表维护 SOP（写操作）

对协议 Base（坐标见 `config/proto_config.json` 的 `source.base_token` 与 `tables`）做**结构维护**的受控写流程：字段 text→单选、检测公式补空值/重复项、问题清单视图核对、可逆注入验证。核心读取命令（platform/read/query/show/pull/check/gen）仍只读；本 SOP 是唯一允许写表的路径。

## 结构变更必须先在沙箱验证（2026-11-09 用户裁定，硬约束）

**凡是要改字段 / 公式 / 视图 / 自动化这类「结构」，先去沙箱试，不许直接改正式表。**

| 属于「结构」（走沙箱） | 不属于「结构」（可直接改正式表） |
|---|---|
| 字段类型改造（text→单选）、新增/删除/改名字段 | 修单条记录的错误值（msg_id 格式、游离 select 值） |
| 改检测公式表达式 | `fix --apply` 的 R1~R5 数据修复 |
| 增删改视图、调整视图筛选/分组/字段顺序 | 对话确认语义后 `record-batch-create` 直写正式表新增记录 |
| 改自动化（workflow）步骤、触发器、通知对象 | 补记录之间的 link 关联 |

**沙箱操作**（飞书 Web UI，非 CLI）：
1. 打开 Base → 右上角 `···` → **沙箱**；沙箱是当前 Base 配置的隔离副本，改动不落地线上。
2. 在沙箱里做完结构变更，配一条记录试跑，确认：检测公式判定符合 ❌/⚠️/✅ 约定、视图筛选正确、自动化不误触发。
3. 验证通过 → 沙箱里**一键更新到线上**。
4. 同步到正式 Base 后，立刻 `python scripts/cli.py pull` + `check` + `gen`，确认代码链路未被结构变更破坏。

**为什么**：结构变更影响面是全表/所有协作者/所有自动化，改错会在秒级污染线上；`fix` 那套 dry-run 只覆盖数据行，管不了结构。沙箱是飞书提供的产品级预演层，比脚本自造副本可靠。

**注意**：拿不到沙箱权限（租户版本限制）时，不得退化成「直接改正式表」——必须先向用户报告受阻原因，由用户决定。

## 检测语义约定（v4 起硬约束）

检测公式的产出必须遵守 proto-toolkit 的判定约定——**pull 把检测字段原文带进 protocol.json，fix/gen 只按此判定**：

- `❌ xxx`：违规（gen 阻断，须修复后重新 pull）
- `⚠️ xxx`：警告（提示不阻断）
- `✅` / 空串：通过

业务性缺失（`归属服务为空`、`引用接口为空`、`子项为空`）在 `pull.check_issues` 里自动降级为 ⚠️ 警告、不阻断 gen——这类是「尚未定义」而非数据损坏（判据：生成物里只是没有对应条目，C/ARXML 依然合法）。若要真正阻断，改 `pull._DEGRADED_PATTERNS`。

新加检测项时：问题消息以 `❌` 前缀拼接（沿用 `ARRAYJOIN(LIST(...).FILTER(CurrentValue!=""),"；")` 骨架）；非问题态输出空串或 `✅`（勿输出其他文字，会被当成告警噪声）。

### 自动修复（`cli.py fix`）与检测的关系

能确定性修复的问题交给 `fix`（不规范格式、选项缺失、双向回填），**语义类问题（如服务该归属哪些接口）fix 只报告不猜**。检测公式发现问题后：
1. 先跑 `python scripts/cli.py fix`（预览）看能否自动修；
2. 能修就 `fix --apply`，再 `pull` 复核；
3. 修不了的（语义判断）去表里手动改。

检测公式本身不因 fix 而改变——fix 改的是数据，检测继续作为回归闸门。

## 触发场景

用户说「XX 字段不要文本，改成单选」「检测要加空值/重复」「XX 只能关联一个/允许关联多个」「检测视图要能看到问题」「改完表要通知」等。

## 通用约定

- 所有 lark-cli 命令带 `--as user`；cwd 设为临时目录，`--json '@file.json'` 参数**必须加单引号**（PowerShell 会把 `@` 当 splatting，内联 JSON 也会被引号规则破坏）。
- JSON 体一律 Python `json.dump(ensure_ascii=False)` 生成文件，不手拼字符串。
- `+field-update` 是**全量 PUT**：改前先 `+field-get` 读完整定义，提交目标态完整 JSON。
- 同表写操作串行执行（并发触发 1254291 冲突）；表内更新走异步链路，写入成功即认可，验收统一最后读回。
- Python 读 PowerShell 落盘文件用 `encoding='utf-8-sig'`（BOM）。

## 步骤

### 1. 勘察

```powershell
lark-cli base +field-list  --base-token <bt> --table-id <tbl> --as user   # 字段类型/公式现状
lark-cli base +view-list   --base-token <bt> --table-id <tbl> --as user   # 找「XX正常性检测 问题清单」视图
lark-cli base +view-get-filter --base-token <bt> --table-id <tbl> --view-id <vew> --as user
lark-cli base +record-list --base-token <bt> --table-id <tbl> --field-id <f1> --field-id <f2> `
  --output .\t.ndjson --overwrite --as user                                # 本地分析用
```

问题清单视图的筛选应为（一般已配好，核对即可）：

```json
{"logic":"and","conditions":[["<检测字段名>","non_empty",null]]}
```

### 2. 字段 text → 单选（不丢数据的关键）

text→select 在 CLI 白名单内，但**只有与选项名完全匹配的值才保留**。因此选项必须从现有记录值生成：

1. Python 读 ndjson，收集该字段唯一非空值（**保持原值，不 strip**；strip 后近重复会生成相似选项，需报告）；
2. 生成 `{"name":"<字段名>","type":"select","multiple":false,"options":[{"name":<原值>,"hue":<循环11色>,"lightness":"Lighter"}]}`；
3. `lark-cli base +field-update --base-token <bt> --table-id <tbl> --field-id <fid> --json '@f.json' --yes --as user`
4. 重导出验证：该列 `empty_count=0`、各记录值仍在。跨记录同名（不同结构体共用成员名等）共享选项，正常。
- 主字段可以转 select；link 字段类型**不能**改；数字字段转 select 同理需值精确匹配。

### 3. 检测公式（「XX正常性检测」formula 字段）

统一骨架：`ARRAYJOIN(LIST(<检测项…>).FILTER(CurrentValue!=""),"；")`，多问题「；」连接，消息加 `❌` 前缀。改公式前须读 lark-base skill 的 `lark-base-field-formula.md` 指南，更新命令带 `--i-have-read-guide --yes`。

常用检测项（按需拼装，**保留表内原有检测逻辑**，只增删目标项）：

```text
空值:   IF(ISBLANK([字段]),"❌ <字段>为空","")            # link 空列表=空；数字 0 / FALSE 不算空
单表重复: IF(AND(NOT(ISBLANK([字段])),[表名].COUNTIF(CurrentValue.[字段]=[字段])>1),"❌ <字段>重复","")
关联上限: IF(COUNTA([link字段])>1,"❌ <字段>只能关联一个","")  # 放开多关联=删掉该项；条件放开=加类型判断
link集合重复(同一目标被多条记录关联):
  IF(AND(NOT(ISBLANK([link])),[表名].[link].[目标label].LISTCOMBINE().FILTER(CONTAIN([link].[目标label],CurrentValue)).COUNTA()>COUNTA([link])),"❌ <link>重复","")
跨表占用(如消息id被别的接口占用):
  IF(AND(NOT(ISBLANK([字段])),COUNTA([本表].FILTER(AND(CurrentValue.[字段]=[字段],CurrentValue.[排除自字段]!=[排除自字段])))>0),"❌ <消息>","")
```

表名/字段名必须与 `+table-get` 返回的完全一致。硬约束：FILTER/MAP/COUNTIF 互不嵌套（链式可以）；字符串只能双引号；等号 `=` 不等 `!=`。

### 4. 验证

1. 重导出（公式异步，必要时导两次）：无 `#ERROR`；空值/重复按预期报出；不该报的为空串；
2. **可逆注入测试**（确认检测真的会触发，而非恰好无数据）：
   - `+record-batch-update --json '@inject.json'` 临时制造一条违规（如把某记录字段改成与另一条重复）；
   - 重导出确认检测字段出现对应「❌ …」；
   - `--json '@revert.json'` 还原，再导出确认干净；
3. 大批量空值告警（如可选关联字段 35/38 为空）先报告影响，用户可改条件检测或删除该项。

### 5. 维护完成：写变更履历（B 流程）

**通知由多维表格自动化发，skill 不发消息。** skill 只往「变更履历」表（`tbljY1BMMetDRjEa`）**新增一条记录**，Base 的 `AddRecordTrigger` 自动把内容发给王锦。

```powershell
lark-cli base +record-batch-create --base-token Mj3gbU3NqagG4WsPcQgc0YhSnac --table-id tbljY1BMMetDRjEa --json '@changelog_rec.json' --as user
```

记录字段（**必须如实标注 AI 身份**）：

| 字段 | 填写要求 |
|---|---|
| 变更摘要 | `【AI结构维护】<一句话概括>`，同时作为通知标题 |
| 变更类型 | 固定 `["AI结构维护"]`（人工改动才用「人工维护」，协议升级用「协议版本升级」） |
| 涉及表 | 列出改动的表名（新建表也写） |
| 变更内容 | 具体做了什么：字段类型、公式增删项、视图/表/记录变更 |
| 验证结果 | 实测结论，如「N/N 值保留，0 #ERROR，注入测试已还原」 |
| 执行者 | 固定 `AI（proto-toolkit skill）` |

变更时间由 `created_at` 自动填，无需写入。**一条记录只记一次维护动作**，不要按表拆成多条刷屏。

## 通知体系（2026-11-09 建，勿重复建）

**全部由多维表格原生自动化（Base Workflow）实现，skill 不发任何消息**——skill 只负责改表、写检测公式、写变更履历记录；通知一律由 Base 自己触发。

| workflow_id | 作用 | 触发/数据源 | 接收人 |
|---|---|---|---|
| wkfzDLiYGSNAHwIW | A1 服务接口实时告警 | ChangeRecordTrigger：服务接口.服务接口正常性检测 isNotEmpty | 王锦 |
| wkfOkYAQKE0ukzOe | A1 数据结构子项实时告警 | 同上（数据结构子项.数据结构子项正常性检测） | 王锦 |
| wkf0AKBDaLLmAPpR | A2 每日体检日报 | TimerTrigger 每天 09:00 → FindRecordAction×4（服务行/接口行/数据结构/子项）→ 引用 recordNum 汇总 | 王锦 |
| wkf3PHBpZvCatkPY | B 结构变更通知 | AddRecordTrigger：变更履历新增记录 → 引用记录字段 | 王锦 |
| wkfQNuaoNHjwuPUN | （已停用）A1 服务清单实时告警 | 指向已删除的「服务清单」表，**已 disable，遗留项** | — |
| wkfo9S9hIasLUeUj | 消息id格式自动回填 | ChangeRecordTrigger：服务接口.检测非空 → IfElseBranch ≠建议 → SetRecordAction 写回消息id | （写表，无通知） |
| wkfR0LFGuPAlRl7B | 枚举值格式自动回填 | 同构（数据结构子项，直连版无分支） | （写表，无通知） |

- 检测公式改动（❌ 前缀语义）同时驱动三处联动：问题清单视图、A1 实时告警、A2 每日体检——改检测公式无需动 workflow
- **新表接入告警**：照抄任一 A1 的 steps（ChangeRecordTrigger + LarkMessageAction），改 `table_name`、检测字段名（condition 用字段名）、消息里的 label fieldId；建后 `+workflow-enable`（创建即 disabled）
- workflow 的 `table_name`/条件用**真实表名**（曾用名报 800004006 not found）；消息 `ref` 一律 fieldId（如 `$.trig.fldykA53Ik`）
- **改检测字段必须同步 workflow 的 fieldId**：检测字段删除重建会换 id，旧 id 报 `800004006 'fldxxx' not found in table`，需 `+workflow-get` 取回 steps、替换 ref 后再 `+workflow-update` 整体提交
- 触发器内置输出可直接进消息：`recordLink`（记录跳转按钮）、`recordModifiedUser`、`recordModifiedTime`
- **注入测试会真发消息给王锦**（E2E 已验证：SafetySrv 告警卡片、变更履历通知卡片格式均正确）——测试前告知用户去飞书确认
- A2 无问题也发（体检日报语义）；要停用 `+workflow-disable`，勿删


## 本 Base 已落地基线（2026-11-09 表优化定稿）

**5 张协议表**（全部平铺在 Base 根目录，无文件夹）：

| 表 | id | 分流方式 | 检测公式 |
|---|---|---|---|
| 服务接口 | tbl1YV1OxMxG3kLm | 纯接口表；`接口名` 为空的是预留服务行；主字段=`接口名` | 服务名/命名空间/服务id/服务描述空值（所有行）；同服务名下 服务id/命名空间 一致性；接口行 6 项（消息id/方向/类型空值、接口名重复、消息id占用、参数名重复）；引用互斥 9 项；单关联上限 4 项；引用类型语义 2 项；命名规范 4 项（大驼峰/Mtd/Evt/16进制） |
| 数据结构 | tblsDjXiMxUOPGCx | `种类`=结构体/枚举 | 数据结构名/种类/子项/引用接口空值；结构体额外要求描述；名称唯一；子项异常聚合（重叠/重名）；种类与子项类型一致；枚举值唯一 |
| 数据结构子项 | tblxbsN0Al9ad3o6 | `子项类型`=枚举值 为枚举值，其余为成员 | 4 通用空值；成员：字节序号/位宽/**长度为空即报错**/枚举类成员缺枚举/基础类挂枚举/不应有值；枚举值：缺值/**须0x开头十六进制**/不应有字节序号/位宽/长度/枚举；父级种类匹配；同结构体内子项名重复；**Bit 区间重叠**（闭区间 `字节*8 ~ 字节*8+位宽*长度-1`） |
| 错误码 | tbl858ZfyLwPOMvj | — | 未做（按本 SOP 对齐） |

三张主表均配「XX正常性检测 问题清单」视图（筛选：检测字段 non_empty，logic=and）。

**服务接口表结构（79 行）**
- 71 条接口行：接口字段 + 服务属性（服务名/命名空间/服务id/服务描述，普通 select/text 列，不是 link）
- 8 条预留服务行：只有服务属性，接口字段全空，待后续补接口
- **无 `记录类型`、无 `归属服务`**：服务归属靠 `服务名` 列直接表达，一行自解释

**服务接口表字段顺序（2026-11-09 定稿）**

接口名（主字段，不可移动）→ 服务名 → 服务id → 服务描述 → 命名空间 → 接口描述 → 接口类型 → 发送类型 → 消息方向 → 消息id(16进制) → 关联接口 → 传输层协议 → 服务质量 → 参数名 → 参数类型 → 参数描述 → 参数方向 → 引用结构体 → 引用枚举 → 引用错误码组 → 服务接口正常性检测

> 主字段必须=接口名：link 字段（数据结构/错误码的「引用接口」、接口表自关联「关联接口」）显示的是目标表主字段，主字段为服务名时引用处只能看到服务名、无法区分接口。
>
> `消息id(16进制)` 带后缀、`关联接口` 不带——二者由用户命名规范决定。字段名若再变，改 `proto_config.json` 的 `field_aliases` 即可，skill 的 reader/fix 会按别名兜底读取并按实际命中的名字写回，无需改代码。

**命名规范（检测公式强制）**
- 接口名大驼峰（首字母大写、无下划线）
- 接口类型 = `method(rr)` → 名字须以 `Mtd` 结尾
- 接口类型 = `event` → 名字须以 `Evt` 结尾
- 消息id 必须是 `0x` 开头的十六进制
- 参数方向选项：`IN（入参）` / `OUT（出参）` / `NONE（无参）`

**数据结构 / 子项表字段要点**
- 数据结构：`子项` 双向 link → 数据结构子项.`所属数据结构`
- 数据结构子项：`所属数据结构` 双向 link；`引用枚举` 单向 link 指向数据结构表（仅成员用）
- 服务接口：`引用结构体`/`引用枚举` 均为**单向** link 指向数据结构表，靠 `种类` 区分语义

**子项表数组字段（2026-11-09 第十批）**

| 字段 | 类型 | 说明 |
|---|---|---|
| `字节序号(B)` | number | 起始字节 |
| `位宽(bit)` | number | 单个元素的位宽 |
| `长度` | number | 变量长度：`uint8` 等标量=1、`uint8[n]` 数组=1024/64 等；非枚举值行必填（检测报错） |
| `Bit范围` | formula（只读，闭区间 `~`） | `IF(OR(ISBLANK([字节序号(B)]),ISBLANK([位宽(bit)])),"",IF(OR(ISBLANK([长度]),[长度]=0),"",TEXT([字节序号(B)]*8)&" ~ "&TEXT([字节序号(B)]*8+[位宽(bit)]*[长度]-1)))` |

> 语义：闭区间 `首bit = 字节*8`、`末bit = 字节*8 + 位宽*长度 - 1`。例 `upgrade_data`（`uint8[n]`，字节6、位宽8、长度1024）→ Bit范围 `48 ~ 8239`。

**规范化建议列 + 自动回填（2026-11-09 第十一批，格式修复下沉表内）**

| 表 | 建议列（formula，只读） | 回填 workflow（enabled） |
|---|---|---|
| 服务接口 | `消息id建议` fldyCBkNNe：空→空；否则 `"0x"&UPPER(RIGHT("0000"&SUBSTITUTE(UPPER(TRIM(值)),"0X",""),4))` | `消息id格式自动回填` wkfo9S9hIasLUeUj |
| 数据结构子项 | `枚举值建议` fldj1xDyDG：仅 `子项类型=枚举值` 行，`"0x"&UPPER(RIGHT("00"&…,2))` | `枚举值格式自动回填` wkfR0LFGuPAlRl7B |

回填链路：`ChangeRecordTrigger`（检测字段 isNotEmpty）→ `IfElseBranch`（原值 ≠ 建议值才写，**防同值死循环**；子项表直连版无分支，因该表无常驻违规）→ `SetRecordAction`（`ref_info` 引用触发记录 + ref `$.trig.<fld建议列>` 取公式计算结果写回原字段）。回填后检测转绿自然终止。

- 实测：注入 `102`→30s 内自动 `0x0102`；注入 `0`→自动 `0x00`；19 条常驻命名违规在场零意外写入
- **已知边界**：已非空的检测不会因公式更新/同值写入再触发（无变更事件）——改检测公式产生的存量问题需一次真编辑才触发，靠 A2 日报兜底展示
- 同批补子项表检测项「❌ 枚举值须0x开头十六进制」（REGEXMATCH `^0[xX][0-9A-Fa-f]{1,2}$`），是子项表回填的触发源；field-update 原地更新 id 不变，workflow 引用不受影响

非协议数据块（2026-11-09 自旧电子表格迁入）：

| 块 | 坐标 | 内容 |
|---|---|---|
| 表「规则」 | tblfiDPnlBqaMMO5 | 5 text 字段（类别/规则项/取值定义/说明/来源章节），11 条（帧格式 5/命令字 1/时序 5） |
| 表「版本履历」 | tbllAU7BZQ4ulJF4 | 5 text 字段（版本/日期/变更人/变更说明/依据），空表待填 |
| 表「变更履历」 | tbljY1BMMetDRjEa | 7 字段（变更摘要/变更类型 select〔AI结构维护·人工维护·协议版本升级〕/涉及表/变更内容/验证结果/执行者/变更时间 created_at）；**B 通知的数据入口，只增不改** |
| 文档块「概述」 | docx PcqCd345boE8WWxnydFcFN3VnWz（block ldxNZDKmD13DAeS6） | 文档目的/范围（覆盖/边界/不覆盖）/读者/参考文档 5 条/术语表 15 条 |

## Bit 区间重叠公式（子项表，2026-11-09 第十批改用 Bit 半开区间）

```
本行:  start = 字节序号*8
       end   = 字节序号*8 + 位宽*IF(ISBLANK(数组长度),1,数组长度)
重叠 ⟺ OTHER.start < 本.end && OTHER.end > 本.start        ← 半开区间，相邻不算冲突
同结构体匹配：CONTAIN(CurrentValue.[所属数据结构].[数据结构名], FIRST([所属数据结构].[数据结构名]))
```

半开区间是关键：`32→48` 与 `48→8240` 相邻不重叠；若用闭区间 `<=`/`>=` 会把所有首尾相接的成员全判成冲突（旧版按字节闭区间就有这个隐患）。

实测（2026-11-09）：把 `UpgradeDataPkg.data_len` 由字节 4 临时改到 7（bit 56..72，落进 `upgrade_data` 的 48..8240）→ 两行同时报 `❌ Bit区间重叠`；还原回字节 4 后两行都变空。

## 字节区间重叠公式（旧版，2026-11-08，已被上面 Bit 版取代）

```
区间 = [序号, 序号 + CEILING(IF(ISBLANK([位宽(bit)]),8,[位宽(bit)])/8,1) - 1]
重叠 ⟺ OTHER.序号 <= 本.末 && OTHER.末 >= 本.序号
同结构体匹配：CONTAIN(CurrentValue.[所属结构体].[结构体类型], FIRST([所属结构体].[结构体类型]))
```

**跨表聚合防污染**（结构体表聚合成员检测结果时）：必须 `CONTAINTEXT(CurrentValue,"重叠")` 精确匹配目标问题，**勿用 `CurrentValue!=""` 非空判断**——成员表后续新增的其他检测项（如引用枚举为空）会被整列吸进聚合方造成全表误报。

## 公式引擎撞名坑（表名优先，必读）

**公式里裸 `[X]` 的解析：表名优先于字段名。** 2026-11-08 两次实战踩坑（枚举值表、结构体类型表）：

| 场景 | 症状 | 规避 |
|---|---|---|
| link 字段名 = 目标表表名（字段「成员变量」vs 表「成员变量」） | `[字段].[列]` 解析成整表整列 → **全行误报** | 改**目标表表名**消歧（`+table-update`）；API 改不了 link 字段名（unsafe_operation_blocked） |
| 普通字段名 = 本表表名（字段「结构体类型」vs 表「结构体类型」） | `[字段]=值` / `ISBLANK([字段])` 整列**静默 error**（全空，公式其他正常项也消失） | 经 link 间接取：`FIRST([link].[对端link].[本字段])` 再判空 |

- 表改名后公式内表引用**自动重写**，无需手动同步
- 消歧改名选语义等价名（「成员变量」→「成员变量定义」），link 字段名不动，UI 无感
- **公式 error 特征**：整列全 null。定位用**探针字段**二分：临时建几个最小公式字段各测一种写法，读值对比，测完全删
- 零参函数不能链式（`CurrentValue.RECORD_ID()` 非法），FILTER 迭代行拿不到 record_id，别往这方向设计公式

## 其他实战坑

- **⚠️ field-get 选项截断（2026-11-09 实际事故，最高优先级）**：`+field-get` 对 select 字段**只返回前 50 个选项**（`truncated=true`, `remaining_options_count>0`）。若拿它做全量 PUT（field-update 是 override 语义），**未返回的选项会被删除，同时使用这些选项的记录值被清空**。本次事故：接口名 71 选项砍到 50、21 条接口记录名被清空；枚举名 122 选项同理清空 72 条。
  - **正确做法**：增选项必须用 `+field-search-options --limit 200` 取全量选项，作为 PUT 基集（参考 `bitable.ensure_select_options`）
  - **恢复办法**：`output/protocol.json` 快照是可靠基线——接口按 msg_id 反查名称，枚举值按（所属枚举 + 归一化 hex 值）反查 c_name；恢复前先补选项再回填记录
- **record 写入不会自动创建 select 新选项**：写不在选项内的值会报 `800030005 not_found ... v1-style wrapper ... use create_records`（错误信息严重误导，真实原因是选项不存在）。必须先补选项再写记录
- **select 值必须传数组**：`{"接口名": ["名"]}`，传裸字符串 `"名"` 同样报上述误导性错误
- **重算延迟**：公式级联异步（秒级）。改公式/记录后立即读回可能见旧值——等 1~2 秒重读再下结论；跨表聚合（结构体表←成员表）延迟更长，必要时读两次
- **formula JSON 结构**：`expression` 与 `name`/`type` **同级**，包进 `property` 报 invalid_request
- **text→select 后游离值**：已有值不在选项内会保留游离文本，顺手 `+record-batch-update` 修成合法选项（实战：uint8[]→uint8[n]）
- **ndjson 值形态**：select（含单选）→ `["选项"]` 数组取首元素；link → `[{"id":"recXxx"}]`；number → 数字；formula → 计算文本或 null。`+record-list --output` 会伴随生成 `.manifest.json`，清理时一起删
- **临时文件**：JSON/ndjson 全部放 `%TEMP%`，任务结束统一删
- **`--json '@file'` 各命令支持不一致（2026-11-09 实测）**：`+field-update` 支持；`+record-batch-create` **不支持**（报 `positional arguments are not supported`）。后者改用 PowerShell 变量传值并转义内层双引号：`$esc = $json -replace '"', '\"'` 再 `--json $esc`（值内无 `\"` 字面量时安全）
- **PowerShell 5 `Out-File -Encoding UTF8` 带 BOM** → lark-cli 报 `invalid JSON object near byte 1 (invalid character 'ï')`；给 CLI 的 JSON/XML 文件用 `[IO.File]::WriteAllText($p, $s, (New-Object Text.UTF8Encoding($false)))` 或 Python `json.dump` 生成
- **`--format ndjson` 与 `-q/--jq` 不兼容**（会报错提示）：ndjson 导出去掉 `--jq`，落盘后本地分析
- **`+table-create` 重名报 `validation_error(800010102)`**：先 `+table-list` 核对——表很可能已建成功（首次调用输出解析失败误判"未建"而重跑撞名的典型事故）；成功输出表 id 在 `.data.table_id`
- **text→select 提交时选项可只写 `{"name":...}`**：hue/lightness 可省略，系统自动循环配色

## 视图与 Block 管理（2026-11-09 实战）

**删视图**：`+view-list` 确认 view_id → `lark-cli base +view-delete --base-token <bt> --table-id <tbl> --view-id <vew> --yes --as user`；每表至少保留一个视图（如「表格」）。

**建表**：`lark-cli base +table-create --base-token <bt> --name <表名> --fields '@f.json' --as user`；fields 为数组、**第一个字段是主字段**，字段形状同 `+field-create`。表名用中文与 Base 现有命名对齐。

**表改名**：`lark-cli base +base-block-rename --base-token <bt> --block-id <tbl> --name <新名> --as user`；名字 Base 内唯一（实战：Rule→规则、History→版本履历）。

**建文档块**：`lark-cli base +base-block-create --base-token <bt> --type docx --name <名> --as user` → 返回 `data.block.docx_token`；正文 `lark-cli docs +update --doc <docx_token> --command overwrite --content <XML>`（新空文档 overwrite 无损失；XML 传参同样需双引号转义）。XML 规范见 lark-doc skill 的 `lark-doc-xml.md`：`<title>` 开头、标题 `seq="auto"` 自动编号、文本 `&`→`&amp;`、表格 `<table><thead><tr><th><p>`。写完 `docs +fetch --scope outline --max-depth 2` 验证章节结构。

**批量写记录**：`+record-batch-create --json '{"create_records":[{字段:值,…},…]}'`，单批 ≤200 条，同表串行；text 字段值直接给字符串。

**从旧电子表格迁数据**：`lark-cli sheets +csv-get --spreadsheet-token <sht> --sheet-id <id> --range <A1> --as user` 读 `annotated_csv`（每行带 `[row=N]` 前缀，转记录时剥掉）；`current_region` 遇空行截断、可能小于真实范围——以 `+workbook-info` 的 `row_count` 为上界分窗探底确认末行（实战：History 表头下全空、Rule 到 12 行）。

## 变更史（2026-11-08 电子表格→多维表格迁移后）

**结构体类型表**（tblsDjXiMxUOPGCx，曾用名：数据结构名→结构体→结构体类型）
- 删字段：从属服务、命名空间、关联错误码组（含清空值）、数据结构类型
- 改名：数据结构名→结构体类型、数据结构描述→结构体描述
- 新增：检测公式 + 问题清单视图

**成员变量定义表**（tblxbsN0Al9ad3o6，曾用名：成员变量→成员变量定义〔为消除撞名〕）
- 类型改造：成员变量类型/成员变量名→select、字节序号(B)/位宽(bit)→number；数据修正 uint8[]→uint8[n]
- 新增：检测公式 + 问题清单视图

**枚举类型表**（tblSpPDtrDVmFVXL）：删字段「关联消息id」
**服务接口表**（tblHdNLTj7tfascd）：视图字段顺序调整（关联接口倒数第二、所属服务最后）

**设计原则**：结构体的服务归属经「引用接口→所属服务」推导，不在结构体层写死；枚举经「引用接口→消息id」推导，不直接挂消息；实体名字段一律 select，消息id 保持 text（防 16 进制转 10 进制）

## 新增协议内容（对话直录，问答表已退役）

「自动修改协议」问答表（tblSLnhcPri8tat7）已于 2026-11-09 **退役删除**：AI 在对话里问清服务/结构/枚举等语义后直接写正式表即可，中间问答表是绕路（表单视图 vewx8Y6Gd3、skill `intake` 命令、`intake.py` 一并删除）。表内自动化「协议问答·自动创建」wkfZRnR6z5NBOlQw 因失去目标表已 disable（遗留项，同 wkfQNuaoNHjwuPUN）。

现状：用户说「加一个接口/结构体/枚举值」→ AI 逐项确认语义（服务归属、消息id、类型、参数……）→ `+record-batch-create` 直写正式表 → 检测公式与建议列自动回填接管质量 → `pull + gen` 同步代码。

**经验存档**（曾用于问答表自动化 wkfZRnR6z5NBOlQw，以后建类似录入自动化仍适用）：
- `AddRecordAction` 用 `ref` 能写 link 关联字段；写 select 字段时**能自动创建新选项**（API 做不到）
- `服务` 用单选（服务名）而非 link——合并后服务接口表无独立服务记录可 link
- 限制：不能拆多值字符串（一次录一条）；无重名校验（靠检测公式事后发现）；新实体间关联需分多行

## 变更史（2026-11-09 第二批：枚举值表治理 + sheets→Base 收尾迁移）

- **通用枚举值表** tbl6IBHqygBWp5VI：删「按枚举看板」「画册」视图（仅留「表格」）；「枚举名」fld8bB0fRa text→select（122 选项=现有枚举值名全量，转后 empty_count=0、122 distinct 全保留）
- **新增表「规则」** tblfiDPnlBqaMMO5：5 text 字段（类别/规则项/取值定义/说明/来源章节），11 条记录（源 sheets Rule 6DFi3T）
- **新增表「版本履历」** tbllAU7BZQ4ulJF4：5 text 字段（版本/日期/变更人/变更说明/依据），空表（源 sheets History jDRRgz 仅表头无数据）
- **新增文档块「概述」** docx PcqCd345boE8WWxnydFcFN3VnWz：title+文档目的/范围/读者/参考文档/术语表 15 条（源 sheets Overview JJWLVm 25 行）
- 旧电子表格 YrK8sncCThe8UstV0yBcvkjQnMR 至此仅剩协议数据 sheet（Service Interface / Data Structure / Control Item / Signal / Parameter Enum / 错误码 / AI修订规则）待迁

## 变更史（2026-11-09 第三批：表合并 / 表优化）

**目标**：服务清单 + 服务接口 → 一张「服务接口」；结构体类型 + 成员变量定义 + 通用枚举类型 + 通用枚举值 → 「数据结构」+「数据结构子项」。全部平铺根目录，不用文件夹。

**做法（顺序即安全顺序）**
1. 服务接口表加 `记录类型`/`服务名`/`命名空间`/`服务id`/`服务描述` 5 个字段
2. 服务清单 13 条记录原样迁入为 `记录类型=服务` 行；71 条接口行回填 `记录类型=接口` + `归属服务`（自关联）
3. 结构体类型表：删除检测公式（重建）、`结构体类型`→`数据结构名`（15+23=38 选项）、`结构体描述`→`描述`、新增 `种类`；迁入 23 条枚举类型为 `种类=枚举`
4. 成员变量定义表：删除检测公式与旧 `引用枚举`；`成员变量名`→`子项名`（33+122=155 选项）、`成员变量类型`→`子项类型`（+`枚举值`）、`成员变量描述`→`描述`、新增 `值`、`所属结构体`→`所属数据结构`；迁入 122 条枚举值为 `子项类型=枚举值`
5. 重建三处引用链：服务接口.`引用结构体`/`引用枚举`、子项.`引用枚举`，全部单向指向「数据结构」表
6. 删除 服务清单 / 通用枚举类型 / 通用枚举值 三张旧表
7. 三表改名 + 移到根目录；删除 结构体 / 通用枚举 / 通用接口 三个空文件夹

**踩坑记录（务必记住）**
- **双向 link 不能改目标表**：`field-update` 换 `link_table` 报 `unsafe_operation_blocked: Updating a link field type, bidirectional setting, or duplex target table is not supported`。必须 `field-delete` + `field-create` 重建，数据从备份回填。
- **删除双向 link 会连带删除对端反向字段**：删 `结构体.引用接口` 时对端 `服务接口.引用结构体` 一并消失；删 `成员.引用枚举` 时对端 `枚举类型.引用成员变量` 消失。**删前必须先快照 link 值**（`{record_id: link_ids}` 存 JSON），删后重建字段再按快照回填。
- **双向自关联字段在公式里裸引用读不到**：`COUNTA([归属服务])` 恒 0、`ISBLANK([归属服务])` 恒 blank，但 `COUNTA([归属服务].[记录类型])` 和 `FIRST([归属服务].[记录类型])` 正常。最终改为**单向自关联**，公式统一走链式访问（`FIRST([归属服务].[记录类型])`）。
- **link 字段改名可以，但必须传完整 body**：只传 `{"name":"新名"}` 报 `800010701 invalid_request: Invalid discriminator value`；要传 `{"name","type":"link","link_table","bidirectional"}`。
- **枚举/结构体合并后必须靠 `种类` 分流**：迁枚举类型进「数据结构」表时，若对端 link 是双向的，会自动把枚举记录写进接口的 `引用结构体`。判据：`FIRST([引用结构体].[种类])!="结构体"` 即为污染，需清洗后再把枚举移到 `引用枚举`。
- **删除一张表后，指向它的 workflow 不会自动失效报错，但会静默不工作**：必须 `+workflow-disable` 或改 `table_name`。
- **公式字段删除重建会换 fieldId**：所有引用它的 workflow 都要跟着改 ref（`$.trig.fldXXX`），否则 `+workflow-update` 报 `800004006 'fldxxx' not found`。
- **`+view-set-filter` 的 JSON 是 `{"logic":"and","conditions":[["字段名","non_empty",null]]}`**（不是 `{"conditions":[{"field_name",...}],"conjunction"}`，后者静默报 False）；且该命令**不接受 `--yes`**。

## 变更史（2026-11-09 第四批：服务表改扁平）

**用户裁定**：不要用「记录类型」区分服务/接口，服务直接做成接口行上的一列；无接口的服务先只写服务信息，接口字段留空，后续补。

**做法**
1. 71 条接口行回填 `服务名`/`命名空间`/`服务id`/`服务描述`（值取自对应服务行）
2. 删除 `记录类型`、`归属服务` 两个字段（删前先删检测公式，否则公式引用报错）
3. 删除 5 条冗余服务行（PowerMgr/SelfCtrlSrv/OtaSrv/SysSrv/VersionSrv —— 已有接口行承载），保留 8 条无接口服务行（只有服务属性，接口字段全空）
4. 重建检测公式：服务字段空值 + 同服务名下 服务id/命名空间 一致性（替代原「服务名重复/服务id重复」）+ 接口字段原 22 项
5. 视图字段顺序改为「服务 4 列 → 接口列 → 检测」
6. 问答表 `服务` 字段 link→select（13 个服务名）——link 不能直接改类型，需删后重建；表当时 0 记录无风险
7. 自动化：A1 服务接口告警换检测字段 ID；A2 每日体检由 4 查改回 3 查；问答 add_si 分支去掉 `记录类型`/`归属服务`，加 `服务名`（ref 指向问答表 `服务` 字段）

**结果**：79 行 = 71 接口 + 8 预留服务；服务 13 / 接口 71 / 结构体 15 / 枚举 23 / 枚举值 122 / 成员 38 / 错误码 8 全对。

**踩坑**
- **workflow 的 field_values 里 `field_name` 存的是字段 ID**（不是字段名），删字段后残留 ID 会让 `+workflow-update` 报 `'fldXXX' not found in table`
- **通知消息 content 里的 `ref` 也存旧字段 ID**（`$.trig.fldXXX`），改字段后必须一并替换，否则报 `path "fldXXX" does not exist in the output path tree`
- **问答表服务字段是 select 时，自动化写 `服务名` 只能写值**，命名空间/服务id/服务描述需要问答表有对应列才能写入

## 变更史（2026-11-09 第五批：问答表补齐服务属性输入）

**目的**：解决「问答自动创建的接口行，服务属性只有服务名、其余三项为空」的缺口。

**做法**
1. 问答表新增 3 个字段：`命名空间`（select，13 个）、`服务id`（text）、`服务描述`（text）
2. 自动化 `add_si` 分支补 3 条 field_values（ref 指向问答表对应字段）
3. `add_si_notify` 通知内容补 3 行展示
4. skill `intake.py`：服务属性优先取问答表填的值，未填则从同服务已有行补齐（intake 已于同日退役，此条为历史记录）

**E2E 验证**：问答表填全 4 项 → 自动化建出的接口行 服务名/命名空间/服务id/服务描述 全部写入，检测字段为空（通过），测试数据已清理。

**注意**：新增字段后 workflow 的 `field_values` 用的是**字段 ID**（`$.trig.fldcZnWLIM` 等），不是字段名。

## 变更史（2026-11-09 第六批：服务接口表字段顺序 + 参数方向 + 命名规范）

**做法**
1. 视图字段顺序改为用户指定顺序（服务名→服务id→服务描述→命名空间→接口名→接口描述→接口类型→发送类型→消息方向→消息id→关联接口→传输层协议→服务质量→参数名→参数类型→参数描述→参数方向→三个引用 link→检测）
2. `参数方向` 选项 `IN`/`OUT`/`NONE` → `IN（入参）`/`OUT（出参）`/`NONE（无参）`，并迁移 60 条记录值
3. 检测公式新增 4 项命名规范：大驼峰、method→Mtd 结尾、event→Evt 结尾、消息id 十六进制

**⚠️ 事故与恢复（重要教训）**
- **改 select 选项名会立刻清空所有使用旧选项的记录值**：`field-update` 用新选项全量 PUT 后，原 `IN`/`OUT`/`NONE` 值全部变空（79 条里 60 条受影响）
- **恢复办法**：`output/base_raw.json` 是唯一可靠快照（改前 pull 过），按 record_id 取旧值 → 映射成新选项名 → `record-batch-update` 回填，恢复后计数与改前完全一致（OUT 39 / IN 20 / NONE 1）
- **正确顺序应是**：先 pull 备份 → 改选项 → 立即按快照回填（而不是改完再想办法找值）
- `+field-update` 改 select 选项时**必须带 hue/lightness**，只写 `{"name":...}` 报 `800010701 Request validation failed with 3 issues`

**检测结果**：新增 17 条命名违规（14 条 method 用了 Evt 结尾、3 条 event 用了 Mtd 结尾），数据本身未改，等人工确认后重命名。

## 变更史（2026-11-09 第七批：服务接口表重建，主字段换服务名）

**动机**：用户要求第一列是「服务名」，但飞书**主字段永远固定在第一列**，`view-set-visible-fields` 无法把它挪走。旧表主字段是「接口名」，只能重建。

**做法（顺序即安全顺序）**
1. 全量备份：79 条记录 + 表定义（字段/视图/主字段）存本地 JSON
2. `+table-create --name 服务接口新 --fields @f.json`（`--fields` 是独立参数，**不是** `--json`；数组第一项即主字段 → 建成「服务名」）
3. 建自关联 `关联接口`（自关联需建表后补，因为要引用自己的 table_id）
4. 建检测公式（30 项，含 4 项命名规范）
5. 按备份迁移 79 条记录 → 保存 旧record_id→新record_id 映射
6. 用映射回填 `关联接口`（58 条自关联）
7. 重建外部引用：`数据结构.引用接口`(31 条) 与 `错误码.引用接口`(14 条) → 指向新表（双向 link 不能改目标表，只能删后重建+回填）
8. 配视图：字段顺序 + 排序 + 问题清单筛选
9. 旧表改名「服务接口旧待删」腾出名称 → 新表改名「服务接口」→ 删旧表
10. 自动化全部切到新表 + 新字段 ID

**踩坑（这次全中）**
- **`+table-create` 的字段数组用 `--fields`，不是 `--json`**；用 `--json` 报 `positional arguments are not supported`
- **表名未腾出前改不了名**：新表必须先叫临时名，等旧表改名/删除后才能改成「服务接口」，否则重名报错
- **自动化里的表引用存的是 table_id**：旧表删掉后 workflow 会显示 `table= tblHdNLTj7tfascd`（裸 ID），必须在删除**前**改掉，否则 `+workflow-update` 报 `'tblXXX' not found`
- **workflow 的字段引用同时存在「字段 ID」和「字段名」两种形态**：`field_values[].field_name` 存 ID，`condition_list[].field_name` 存字段名；两者都要按新表重建
- **ChangeRecordTrigger 的输出树只暴露 condition 里列的字段**：通知消息引用未在 condition 出现的字段会报 `path "fldXXX" does not exist in the output path tree`。要把「问题详情」放通知里，检测字段必须出现在 trigger condition 中
- 重试期间遇到 `800004014 request timeout`（服务端抖动），直接重跑即可

**验证**：79 行（71 接口 + 8 预留服务）；服务13/接口71/结构体15/枚举23/枚举值122/成员38/错误码8 全对；关联接口 58、引用结构体 19、引用枚举 17、引用错误码组 14 与旧表一致；检测结果与旧表逐项相同；问答自动化注入测试已建接口行并写全 4 个服务属性，测试数据已清理；skill read/pull/show 全链路通过。

## 变更史（2026-11-09 第八批：主字段改回接口名，再次重建）

**动机（用户原话）**：「我突然感觉还是有必要接口名作为第一列，比如图中这种引用接口我看到的是服务名，看不到接口名了」。**根因：link 字段的显示值 = 目标表的主字段**——第七批把主字段改成服务名后，数据结构/错误码的「引用接口」与接口表自关联「关联接口」全部只显示服务名，同一服务下多条接口无法区分。

**做法**：与第七批同一套流程（备份 → `+table-create` 第一项=`接口名` → 自关联 → 30 项检测公式 → 迁 79 行 → 回填 58 关联接口 → 重定向 数据结构/错误码 引用接口并回填 31/14 → 视图字段顺序 → 审批/问答自动化换表换字段 ID → 旧表改名腾位 → 新表改名）。

| 项 | 第七批（旧，已废） | 第八批（现行） |
|---|---|---|
| 表 id | tblUABcgXD3qwfXr（已删除） | **tbl1YV1OxMxG3kLm** |
| 主字段 | 服务名 | **接口名 `fldRFL8mxV`** |
| 检测字段 | — | `fldhGGC4lC` |
| 问题清单视图 | — | `vew7sgP7hc` |

**新踩坑（第七批没遇到）**
- **改名后 workflow 里残留旧表名**：`+workflow-get` 取回的 steps 里 `table_name` 仍是「服务接口旧待删」（第七批 c9 只改了 A1）。旧表被删前必须**逐个 workflow 全量扫** `table_name` 字段——QA 自动化（`wkfZRnR6z5NBOlQw` step2）与 A2 日报（`wkf0AKBDaLLmAPpR` step1）各有一处，改完再删表。
- **旧表实际已被删除**（`+table-get` 返回 `800030104 not_found`，`+table-list` 共 11 张表无该表），复查时无需再删。
- **`+view-set-visible-fields` 不移动主字段**：即使传了含「接口名」在首位的顺序，主字段永远在最左；查询顺序要用 `+view-get-visible-fields` 复核。
- **`+workflow-list` 的返回键是 `data.items`**（不是 `data.workflows`），按 `workflows` 取会得到空列表。
- **检测公式里的裸表名会随改名自动重写**：公式内引用的是旧临时名「服务接口重建」，表改名后飞书自动改写为「服务接口」，无需手工重写公式。

**验证**：79 行 / 71 接口名非空 / 服务 13 / 结构体 15 / 枚举 23 / 成员 38 / 枚举值 122 / 错误码 8；关联接口 58、引用结构体 19、引用枚举 17、引用错误码组 14 —— 与第七批逐项一致；8 个 workflow 无任何旧表 ID/旧表名残留；`pull` 输出与 `read` 统计一致；`show service PowerMgr` / `query PowerMgr` 正常。

**遗留（检测报 19 条 ❌，等人工决定）**：17 条命名后缀与接口类型不符（14 条 method 用 Evt 结尾、3 条 event 用 Mtd 结尾）+ 2 条消息id 冲突（`0x0801` 被 PowerOffReqMtd 与 SocFanQueryMtd 共用，合并前既有）。

## 变更史（2026-11-09 第九批：删旧表 + 字段名还原 + skill 别名适配）

**删表（tblUABcgXD3qwfXr「服务接口旧待删」）**——删除前四项核验全过：
1. 全表 link 字段的目标表：指向旧表的 0 个（数据结构/错误码的「引用接口」、问答表 link 均指新表 `tbl1YV1OxMxG3kLm`，其中接口表自关联也已指新表）
2. 公式 / 视图筛选 / 8 个 workflow / dashboard 全扫：旧表 ID 与旧表名 0 处残留
3. 79 行内容比对：按**目标名**解析 link 后逐行对比（不是比 id，id 重建后本就不同），新表独有 0 行、旧表独有 0 行
4. 删除后回归：11 张表行数正常，pull/read/fix 全通
`+table-delete --table-id <id> --yes` 返回 `deleted: true`。

**字段名还原**：新表字段被误改成 `关联接口(16进制)`，已还原为 `关联接口`。
- **link 字段改名的坑**：`+field-get` 取回完整定义后必须 PUT `{name, type:"link", link_table, bidirectional, description}` —— 只传 `{"name":"新名"}` 报 `800010701 invalid_request: Invalid discriminator value`（缺 type 判别字段）；只传 name+type 也仍会因缺 link_table 失败。
- `消息id(16进制)` **保留**（符合用户命名规范「消息id(16进制)」）。

**skill 侧字段别名机制**（字段改名不再打断 skill）：
- `proto_config.json` 的 table 定义可加 `field_aliases: { 规范名: [候选名...] }`，当前只有 `service_interface` 的 `消息id` 一项
- `common/bitable.py` 新增 `pick(record, names)`（按候选顺序取首个非空）/ `pick_name(record, names)`（返回实际命中的字段名，用于写回）
- `reader.py` 在 `__init__` 收拢全部 table 的 aliases，`_get()` 统一兜底取消息id
- `fix.py` 查重/写回都用别名：读用 `pick`，写用 `pick_name`，保证写回落到表里真实存在的那个字段名
- **别名列表要去重**：config 里写 `["消息id(16进制)", "消息id"]`，代码再追加一次 `消息id` 会得到重复项，`+record-list --field-id` 直接报 `duplicate field id` —— 拼接后必须去重

## 变更史（2026-11-09 第十批：子项表加数组长度 + Bit 范围 + Bit 区间重叠）

**需求（用户原话）**：「子项类型是 uint[n] 时需要有字段定义数组长度……子域分组要有 字节序号 位宽 长度，那么这个数据的 bit 范围就是 字节序号*8 → 字节序号*8 + 位宽*长度……加字段用于显示这个算出来的 Bit 范围。然后检测也要检测属于同一数据结构的子项范围是否有冲突」。

**表结构变更（数据结构子项 tblxbsN0Al9ad3o6）**

| 新增字段 | 类型 | id |
|---|---|---|
| 数组长度 | number | `fldU4z6X1D` |
| Bit范围 | formula | `fldOMRQW2c` |

视图字段顺序：子项名 → 子项类型 → 字节序号(B) → 位宽(bit) → **数组长度 → Bit范围** → 描述 → 所属数据结构 → 值 → 引用枚举 → 检测。两个视图（`vewiJpfkS7` 表格、`vewuMY8AgI` 问题清单）都已同步。

**检测公式新增 4 项**（`fldO5DvIHT`，总长 2056 字符）
1. `数组类型缺数组长度`：`uint8[n]/uint16[n]/uint32[n]` 但 `数组长度` 为空
2. `非数组类型不应填数组长度`
3. `枚举值子项不应有数组长度`
4. 重叠判定由「字节闭区间」改为「**Bit 半开区间**」：`OTHER.start < 本.end && OTHER.end > 本.start`，提示文案改为 `❌ Bit区间重叠`

**数据**：`UpgradeDataPkg.upgrade_data` 填 `数组长度=1024` → Bit范围 `48 → 8240`。`VersionInfo.ver_array` 暂未定长度，检测正确报 `❌ 数组类型缺数组长度`（等业务确认）。

**skill 侧同步**
- `reader.py`：成员模型加 `len` / `bit_range` 两个字段（对应表里 `数组长度` / `Bit范围`）
- `pull.py` `_transform_member`：新增 `array_len`，`[n]` 且有长度时 `nbytes = 单元素字节 × 长度`、`byte_end` 按实际算出（不再是 `None` 的 open）；无长度仍按 open 处理
- `gen/object_view.py`：`Member` 加 `array_len` 透传，生成器可用
- 实测解析：`upgrade_data` → `byte 6..1029, nbytes=1024, array_len=1024`；`ver_array` → `byte 2..None, nbytes=None`（未定长）

**踩坑**：`+field-create` **没有 `--yes` 参数**（`+field-update` 才有），传了报 `unknown flag`；公式字段仍要 `--i-have-read-guide`。
