---
version: 1.0.0
author: wangjin0115
company: cviauto
name: embedded-omni
description: embedded-omni 嵌入式全能数据分析平台（可扩展的多数据形态分析 skill）。当用户提到"抓串口"、"串口日志"、"log分析"、"日志分析"、"看log"、"分析log"、"实时看串口"、"串口被占"、"发日志邮件"、"DBC"、".dbc"、"CAN 数据库"、"CAN矩阵"、"报文库"、"解析DBC"、"CAN 报文"、"报文解析"、"信号表"、"cantools"、"CAN decode/encode"、"原理图"、"网络表"、"netlist"、"看原理图"、"查引脚"、"引脚网络"、"SchDoc"、"PrjPcb"、".DSN"、"OrCAD"、"Altium 原理图"、"kicad_sch"、"kicad_pro"、"原理图PDF"、"map文件"、".map"、"链接map"、"内存占用"、"Flash占用"、"RAM占用"、"符号表"、"map对比"、"map diff"、"看map"、"BLF"、".blf"、".asc"、"CAN日志"、"CAN log"、"总线日志"、"CAN波形"、"信号波形"、"实车数据"、"台架日志"时触发。按数据形态路由到对应模块执行：串口日志 → modules/serial-log（采集/网页监视/分析/邮件一体化）、DBC/CAN 数据库 → modules/dbc（报文/信号/解码/编码/C代码生成）、原理图/网络表 → modules/schematic（EDA 源文件精确解析 + 原理图 PDF 文本层启发式分析）、链接 map → modules/mapfile（存储区占用/符号/体积排行/两版对比）、CAN 总线日志(BLF/ASC) → modules/canlog（python-can 读 + cantools 解码/波形 + CSV/XLSX 表格导出）。新数据形态按 modules/<类型>/MODULE.md 自包含模式扩展。
argument-hint: serial … | dbc … （或自然语言按数据形态路由）
allowed-tools: [Bash, Read, Edit, Grep, Glob, Write, AskUserQuestion]
tags:
   - embedded
   - serial
   - uart
   - can
   - dbc
   - analyze
   - report
---

# embedded-omni（嵌入式全能）

嵌入式领域"各种形式数据"的分析平台。**本文件只做路由与规范，不含任何模块的实现细节。**

## 第一步：路由（必做）

按用户意图 / 参数选模块，然后 **Read 对应 MODULE.md 并严格照其执行**：

| 数据形态（用户意图关键词） | 模块 | 模块文档 |
|---|---|---|
| 抓串口 / 串口日志 / log分析 / 看log / 实时看串口 / 串口被占 / 发日志邮件 | 串口日志 | [modules/serial-log/MODULE.md](modules/serial-log/MODULE.md) |
| DBC / .dbc / CAN 数据库 / CAN矩阵 / 报文库 / 报文 / 信号解析 / decode / encode / 生成C代码 | DBC | [modules/dbc/MODULE.md](modules/dbc/MODULE.md) |
| 原理图 / 网络表 / netlist / 查引脚 / 引脚网络 / .DSN / .PrjPcb / .SchDoc / .kicad_pro / .kicad_sch / 原理图PDF | 原理图 | [modules/schematic/MODULE.md](modules/schematic/MODULE.md) |
| map文件 / .map / 链接map / 内存占用 / Flash占用 / RAM占用 / 符号表 / map对比 / 看map | 链接map | [modules/mapfile/MODULE.md](modules/mapfile/MODULE.md) |
| BLF / .blf / .asc / CAN日志 / CAN log / 总线日志 / CAN波形 / 实车数据 / 台架日志 | CAN日志 | [modules/canlog/MODULE.md](modules/canlog/MODULE.md) |

路由规则：

- 用户意图明确命中一行 → 直接进该模块，不再反问。
- 意图不清（只说"分析一下这个数据"且看不出形态）→ 先看文件后缀/内容判形态；仍不清 → 问用户，禁止瞎猜模块。
- 混合需求（如 CAN 日志 + DBC 解码）→ 按**主意图**选模块执行，其余需求作为该次分析的输入上下文；两个模块都要完整流程时，分两次分别执行。
- 用户直接点名模块名（"用串口模块…"、"dbc 模块…"）→ 无视关键词，按点名路由。

## 模块清单

| 模块 | 目录 | 能力 | 依赖 |
|---|---|---|---|
| serial-log | `modules/serial-log/` | 串口采集（Web 实时/后台写文件）、固定/自由格式分析、工程关联反查源码、HTML 报告、邮件 | pyserial、lark-cli（邮件可选） |
| dbc | `modules/dbc/` | DBC 总览/报文/信号检索、原始帧 decode/encode、全量导出、生成 C 解析代码 | cantools（`python -m pip install cantools`） |
| schematic | `modules/schematic/` | EDA 源文件（OrCAD .DSN/Altium .PrjPcb/KiCad）精确解析：器件/引脚/网络/追网/网络表快照；原理图 PDF 文本层启发式分析（位号/值/BOM/网络标号） | universal-netlist（`npm i -g @intelligentelectron/universal-netlist`）、pymupdf |
| mapfile | `modules/mapfile/` | 链接 map 文件（GNU ld/lld/Metrowerks）：存储区占用率、符号查询（地址/大小/所在.o）、模块体积排行、两版 map 对比；不按芯片分类（map 自包含 MEMORY 区语义） | mapfile-parser（`python -m pip install mapfile-parser`） |
| canlog | `modules/canlog/` | CAN 总线日志（.blf/.asc/.trc/candump）：帧统计/ID 分布、DBC 物理值解码、cantools plot 原生波形（PNG/交互）、CSV/XLSX 表格导出、格式互转 | python-can + cantools + matplotlib（xlsx 另需 openpyxl） |

## 平台统一哲学（每个模块都必须遵守）

1. **脚本做确定性工作，AI 做解释**：数值统计/解析/格式转换交给模块脚本，AI 不手算、不编造。
2. **结论必须落到出处**：说一个结论就要给出它来自哪条日志/哪个报文/哪个信号/哪个 bit；定位不到就明说"未定位到"，不硬凑。
3. **输入路径与输出产物都写绝对路径或仓库相对路径**，用户要能直接找到文件。
4. **缺依赖时脚本自己报装法**（含国内镜像提示），AI 不假装跑过。

## 扩展规范：加一个新数据形态模块

新形态（BLF/ASC/CAN 报文日志、PCAP、ELF/map、寄存器 dump、CSV 遥测……）按此落位：

1. 建目录 `modules/<新类型>/`，**自包含**：
   - `MODULE.md` —— 模块完整工作流（**不带 skill frontmatter**，全平台只有顶层本文件带）
   - `scripts/` —— 确定性工具（Python，`python scripts/<x>/<tool>.py` 直接可跑）
   - `references/` —— 该模块的深度文档（模式定义/坑/移植指南，主文档只留索引）
   - `config/` —— 仅本模块的配置；`assets/`/`util/` 按需
2. **脚本自定位约定**：脚本用 `Path(__file__).resolve().parent.parent.parent` 取**模块根**（`scripts/<分类>/` 恰好三层）——模块目录整体搬移不破坏脚本；这也是模块自包含的判定标准。
3. 本文件「模块清单」「路由表」各加一行。
4. 模块间**禁止互相 import/读对方 config**；确有 ≥2 个模块需要同一份数据（如工程注册表）时，才把该数据上提到顶层 `config/` 并让两个模块同步改读取路径——不提前做投机性共享。

## 目录结构

```
embedded-omni/
├── SKILL.md          # 本文件：路由层（唯一 skill 入口）
├── README.md         # 平台总览（面向人读）
└── modules/          # 模块层：一种数据形态一个目录，自包含
    ├── serial-log/   # 串口日志（原独立 skill，2026-10-26 并入）
    ├── dbc/          # DBC / CAN 数据库
    ├── schematic/    # 原理图 / 网络表（native EDA 源文件 + 原理图 PDF，2026-10-27 新增）
    ├── mapfile/      # 链接 map 文件（基于 mapfile-parser，2026-10-27 新增）
    └── canlog/       # CAN 总线日志 BLF/ASC（python-can + cantools 波形/表格，2026-10-27 新增）
```
