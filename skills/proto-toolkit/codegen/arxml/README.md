# ARXML 后端（AUTOSAR DataType + Interface）

`protocol.json` → 标准 AUTOSAR ARXML，供 DaVinci Developer / ISOLAR / EB tresos 导入。
**v1 只生成应用数据类型、实现数据类型、接口和数据类型映射集**，不生成 SWC/Port/COM。

## 配置

所有可调项都在 [config/codegen_config.json](config/codegen_config.json)：

| 配置 | 说明 |
|---|---|
| `arxml.version` | `4.2.2` / `4.4` / `R21-11` / `R22-11` |
| `arxml.namespace` | Classic 4.x 通常 `http://autosar.org/schema/r4.0` |
| `arxml.schema_location` | 与版本对应的 XSD，如 `AUTOSAR_4-2-2.xsd` |
| `arxml.package_prefix` | 生成包前缀，如 `/CDC7255` |
| `arxml.platform_types_package` | 平台类型包，默认 `/AUTOSAR_Platform` |
| `arxml.tool_profile` | `generic` / `davinci` / `isolar` / `tresos`（v1 保留） |
| `scope.datatypes` / `scope.interfaces` | v1 必须为 `true` |
| `scope.swc` / `scope.com` | v1 必须为 `false`（后续版本实现） |
| `naming.*` | 包名、实现类型后缀、数组后缀、开放数组上限 |
| `behaviour.emit_bit_representation` | 单字节位成员是否生成 `SW-BIT-REPRESENTATION` |
| `behaviour.reference_check` | 生成前检查引用闭合（默认开） |

改版本只改 `version` + `schema_location` + `schema_attribute`（必要时 `namespace`），生成器逻辑不动。

## 生成

```bash
cd <repo>/.claude/skills/proto-toolkit
utils/.venv/Scripts/python.exe scripts/cli.py gen --lang arxml
# 或解析 + 生成
utils/.venv/Scripts/python.exe scripts/cli.py parse --lang arxml
```

产物：`codegen/arxml/generated/CDC7255_Protocol.arxml`

## 生成内容

- 基础类型：`uint8/sint8/uint16/sint16/uint32/sint32` 的 Application/Implementation 类型；
- 枚举：`ApplicationPrimitiveDataType` + `CompuMethod(TEXTTABLE)`；
- struct：`ApplicationRecordDataType` + `ImplementationDataType(STRUCTURE)`；
- 开放尾/数组：`ApplicationArrayDataType` + `ImplementationDataType(ARRAY)`；
- 接口：`event` → `SenderReceiverInterface`；`method(rr)` → `ClientServerInterface`；
- `DataTypeMappingSet`：应用类型 → 实现类型。

`msg_id / pair_id / direction / transport / qos` 写在 `DESC` 里（AUTOSAR 基础 S/R、C/S 接口没有通用消息 ID 字段）。

## 已知边界

- **平台类型**引用 `/AUTOSAR_Platform/BaseTypes/*`，目标工具工程里必须有该包（DaVinci 默认有）。
- **字节偏移/位域**：位成员生成 `SW-BIT-REPRESENTATION`，字节偏移写在 `DESC`；没有生成 `SwRecordLayout`，所以 ARXML 不保证 C 结构体的物理字节布局与协议表逐字节一致。需要精确布局时，以 C 生成器的 `Proto_Types.h` 为准。
- **无 SWC/Port/COM**：需要 SWC 或 CAN COM 映射时，后续版本再加。
- 生成后建议用 Vector SchemaCheck 或目标工具的 ARXML 导入检查；本仓库没有内置 XSD 校验。
