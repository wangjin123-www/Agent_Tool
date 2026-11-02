---
version: 1.0.0
author: "wangjin0115"
company: "cviauto"
name: s32k3-rtd-master
description: "S32K3 RTD 大师级专家库（NXP S32K344，RTD 0.9.0 / S32DS v3.4，29 个官方训练工程逐行教学 + S32K3xx RM/DS 手册 markdown 库）。当用户以 /s32k3-rtd-master 显式调用，或明确要求深挖 S32K3（S32K344/S32K312/S32K3xx）的 MCAL/RTD 驱动、外设配置、寄存器、初始化时序、写码问题时使用：定位训练工程路径、按外设给出逐行原样代码教学、生成写码指导；查寄存器位域/基地址/引脚复用/电气参数时走 rm 子命令查手册库。不自动触发；不处理非 S32K3 平台；不做纯硬件/原理图/PCB 问题。"
category: development
argument-hint: "list|lookup|guide|rm"
context: pull
tags: ["s32k3", "rtd", "mcal", "driver", "embedded"]
license: Complete terms in LICENSE.txt
---

# s32k3-rtd-master

S32K3（NXP S32K344 系列）RTD/MCAL 驱动的**大师级专家库**。把官方训练库 29 个示例工程拆成按外设分篇的教学文档（**代码逐字符原样摘录**），用来定位工程、讲清时序、生成写码指导。**仅在显式调用时启用**，是高强度深挖 S32K3 问题的专用武器。

## 铁律（先读）

1. **代码原样**：references 里的示例代码与官方源文件逐字符一致。给用户写码时沿用其写法，禁止"顺手美化/精简/改写"。
2. **给结论给位置**：每个结论必须落到 `文件:行号` 或工程路径，不空谈。
3. **先定位再回答**：任何外设问题先 `lookup` 拿工程路径与教学文档，再按需 `Read references/<topic>.md` 原文，不凭记忆。
4. **不确定就说不知道**：训练库未覆盖的外设（如 MCAL 配置工具链细节、非 S32K3 芯片）明确标注"训练库无此内容"。

## Entry

`$0` 为空或未匹配 → 用 AskUserQuestion 列出下表，让用户选。

| 命令 | 说明 |
|------|------|
| list | 列出训练库全部外设示例工程索引（工程目录 / 教学文档 / 绝对路径），可带关键词过滤 |
| lookup | 按外设关键词定位训练工程路径（含 main.c 行数）与对应教学文档 |
| guide | 抽取教学文档的章节标题 + 原样代码块，汇总成写码指导写入 `output/` |
| rm | 在 S32K3xx RM（119 模块文件）/DS 手册 markdown 库中定位模块文件，给页码与 Grep 建议 |

## Commands

### list

触发："有哪些工程 / 训练库有什么 / 列出 SPI 相关工程"。

首选（脚本）：

```bash
python scripts/cmd/cmd_list.py [关键词]
```

次选（参考）：`Read references/list.md`

输出：stdout 打印索引表 + references 文档清单。关键词可选（如 `spi`）。

### lookup

触发："WKPU 工程在哪 / CAN 示例路径 / 某外设对应哪个文档"。

首选（脚本）：

```bash
python scripts/cmd/cmd_lookup.py <关键词>
```

次选（参考）：`Read references/lookup.md`

输出：stdout 打印命中工程（含 main.c 绝对路径与行数）与教学文档（含行数）。

### guide

触发："按 SPI 给我写码指导 / 深挖 eMIOS / 要 Flash 的代码参考"。

首选（脚本）：

```bash
python scripts/cmd/cmd_guide.py <关键词>
```

次选（参考）：`Read references/guide.md`

输出：`output/guide_<关键词>.md`，内含来源文档引用 + 章节标题 + 原样代码块；stdout 回报命中数。

### rm

触发："WKPU 的 WIFEER 位定义 / MC_CGM 基地址 / RM 里 eMIOS 哪章 / DS 电压参数"。

首选（脚本）：

```bash
python scripts/cmd/cmd_rm.py [关键词]
```

次选（参考）：`Read references/rm-ds.md`

输出：stdout 打印命中的 RM 模块文件（含章目录 / PDF 页码范围 / 绝对路径存在性校验）+ 下一步 Grep 模式建议；关键词命中器件级参数（电压/电流/封装/ESD/去耦/热特性）时提示改查 DS 单文件。无关键词时打印 18 章概览。

**手册库分工**：训练库答"RTD 怎么写码"，手册库答"寄存器/位域/参数是什么"。查位域先 `rm` 定位文件，再在文件内 Grep `####.*\b<缩写>\b`（寄存器）、`base address`（基地址）、`^Bits `（位域）；位域答案用表格搬 picture text（`Bits/R/W/Reset`）。手册细节见 `references/rm-ds.md`（RM/DS 分工、Grep 模式、图片目录清洗规则、S32K312 特化）。

## 深挖工作流（高强度模式）

遇到复杂 S32K3 问题时，按此链闭环，不许跳步：

```mermaid
flowchart TD
    A["用户报 S32K3 问题"] --> Q{"问题类型"}
    Q --|"怎么写码/驱动/时序"| B["lookup 定位工程+文档"]
    Q --|"寄存器/位域/参数是什么"| M["rm 定位手册模块文件"]
    B --> C["Read references 下对应外设 md 读原样代码与时序"]
    M --> C2["Read references/rm-ds.md 按地图+Grep 模式查 RM/DS"]
    C --> D{"训练库是否覆盖?"}
    D --|是| E["对照源工程 main.c/驱动源文件<br/>给 文件:行号 级结论"]
    D --|否| F["明确说明训练库无此项<br/>给最接近的替代工程"]
    C2 --> E2["给 文件:行号 级结论<br/>位域用表格搬 picture text"]
    E --> G["guide 生成写码指导到 output/"]
    E2 --> G
    G --> H["按铁律②给方法+位置，落到具体 API/寄存器"]
```

## 资源路由规则

- **首选脚本**：确定性操作走 `python scripts/cmd/cmd_<verb>.py`
- **次选参考**：需背景知识/规范/schema 才读 `references/<verb>.md`
- 外设教学正文一律在 `references/<外设>.md`（wkup/can/adc/emios/flash/spi/iic/uart/lin/timing/rtc/dma/misc1/misc2）
- 手册库（RM 119 文件 + DS）地图与检索方法论在 `references/rm-ds.md`；文档实体随 skill 分发在 `docs/NXP_S32K3/`（config.conf `[paths].docs_root` 可覆盖，缺省回退工程旧位置 `doc/NXP_S32K3`）
- 路径一律相对 skill 根目录；训练库绝对路径在 `config/config.conf` 的 `[paths].training_root`
- 产物统一写 `output/`（已 gitignore）

## 输出约定

| 产物 | 位置 |
|------|------|
| 运行日志/中间产物 | `output/` |
| 用户可见结果 | stdout 直接打印 + `output/guide_<关键词>.md` |

## 脚本分层（固定，勿改层名）

```
scripts/
├── cmd/       # 入口层：一个子命令一个 cmd_<verb>.py，薄壳，只做参数解析+调 core
├── core/      # 业务层：core.py，核心逻辑，被 cmd 调用
└── common/    # 公共层：conf.py 读 config.conf、log.py 统一 UTF-8 输出
```

依赖单向 `cmd → core → common`。
