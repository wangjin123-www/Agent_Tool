# 模块：原理图 / 网络表分析

> embedded-data-analysis（嵌入式数据分析）的 schematic 模块。两条腿：
> - **native 侧**（有 EDA 源文件，精确）：基于开源工具 [universal-netlist](https://github.com/IntelligentElectron/universal-netlist)（Apache-2.0，v1.12.2，本机已装）直接读 Cadence/Altium/KiCad 源文件，无需装 EDA、无需 license；桥接脚本 `scripts/native/unl_bridge.py`。
> - **PDF 侧**（只有导出 PDF，启发式）：基于 PyMuPDF 提取文本层（位号/网络标号/器件值），脚本 `scripts/pdf/sch_pdf_tools.py`。**不含连线连通性**——要精确网络表必须有 EDA 源文件走 native 侧。

## 支持格式

| 入口 | 格式 | 侧 | 能拿到什么 |
|---|---|---|---|
| Cadence OrCAD/CIS | `.DSN`（含带密码款，读环境变量） | native | 精确网络表：器件/引脚/网络/DNS 不贴装/CIS 变体 |
| Altium Designer | `.PrjPcb`（自动聚合多页 `.SchDoc`，经端口/图纸入口/总线拼接；支持装配变体） | native | 同上 |
| KiCad | `.kicad_pro` / 根 `.kicad_sch`（优先读旁边的 `.net` 导出；没有则调 kicad-cli 现导，`KICAD_CLI_PATH` 可指路径） | native | 同上 |
| 通用网络表快照 | `.netlist.json`（universal-netlist schema，带 SHA-256 自校验） | native | 同上，可入库 diff |
| 原理图 PDF | `.pdf`（EDA 导出、带文本层；扫描图不行） | PDF | 位号清单+值(启发式)、网络标号、简易 BOM、文本定位；**无连通性** |

不直接支持但可中转：立创 EDA/AD 老版本等可先导出上述格式之一；KiCad 也能把 OrCAD/Altium 工程导入后再走本模块（kicad-cli netlist 导出另有 kicadxml/cadstar/orcadpcb2/spice 等格式，本模块不用）。

## 依赖

```bash
# native 侧(已装, 版本 v1.12.2)
npm install -g @intelligentelectron/universal-netlist     # 需 Node 20+；本机 node 就位
# 公司网走不了外网时: npm config set registry https://registry.npmmirror.com 后再装, 或用官方 PowerShell 安装器
# 二进制不在 PATH 可设 UNL_BIN 环境变量

# PDF 侧(已装)
python -m pip install pymupdf
```

脚本缺依赖自报装法（exit 3）。

## 工具速查

```bash
SCH="$(git rev-parse --show-toplevel)/.claude/skills/embedded-data-analysis/modules/schematic"
UNL="$SCH/scripts/native/unl_bridge.py"      # native 侧(EDA 源文件, 精确)
PDF="$SCH/scripts/pdf/sch_pdf_tools.py"      # PDF 侧(导出 PDF, 启发式)
```

### native 侧 `unl_bridge.py`（design = .DSN/.PrjPcb/.kicad_pro/.netlist.json）

| 子命令 | 用途 |
|---|---|
| `info <design>` | 总览：来源格式/器件数/网络数/前缀分布/DNS 不贴装清单 |
| `comps <design> [--type U] [--ref U1] [--mpn PAT]` | 器件清单：位号/值/MPN/描述/DNS |
| `pins <design> --ref U1` | 某器件引脚表：脚号/脚名/所在网络 |
| `nets <design> [--match PAT] [--net NAME]` | 网络清单；`--net` 列成员（位号.脚） |
| `xnet <design> --net NAME [--skip C,L]` | 扩展网络：穿过串阻/串容/磁珠追到驱动与负载端 |
| `export <design> [--out F]` | 导出 `.netlist.json`（可入库/可 diff 的网络表快照） |

### PDF 侧 `sch_pdf_tools.py`

| 子命令 | 用途 |
|---|---|
| `info <pdf>` | 总览：每页位号/网络/值统计；无文本层（扫描图）告警 |
| `comps <pdf> [--page N] [--type R] [--ref R14] [--out csv]` | 位号清单（含阅读顺序关联的值） |
| `nets <pdf> [--match PAT] [--page N]` | 网络标号清单（跨页聚合，含电源名） |
| `find <pdf> <关键字> [--all]` | 定位任意文本：页码+坐标（"这条网络在哪页"） |
| `bom <pdf> [--out csv]` | 按值聚合的简易 BOM（启发式，评审用） |
| `scan [--dir D]` | 扫目录找 PDF |

## 典型工作流

### 1. 软件排障要查硬件连接（最常用）

```bash
# 例: 查 MCU 的 CAN 收发器 STB 脚挂哪个网络、串阻多大 —— 有 .DSN/.PrjPcb 时:
python "$UNL" nets  "D:\硬件\G.EQC1601.DSN" --match CAN_STB
python "$UNL" xnet  "D:\硬件\G.EQC1601.DSN" --net CAN0_STB_N
python "$UNL" pins  "D:\硬件\G.EQC1601.DSN" --ref U3

# 只有 PDF 时(如本仓库 resource/原理图/):
python "$PDF" nets "…B26296.pdf" --match CAN
python "$PDF" find "…B26296.pdf" CAN0_STB_N     # 定位到第几页
python "$PDF" comps "…B26296.pdf" --page 4 --ref R   # 该页电阻+值
```

### 2. 网络表快照入库、跨版本 diff

```bash
python "$UNL" export "D:\硬件\G.EQC1601.DSN" --out doc/hardware/netlist_snapshot.netlist.json
# 改版后重新导出, 两份 .netlist.json 直接文本 diff(带 SHA-256 完整性)
```

### 3. 评审一颗电源/一个接口电路

```bash
python "$UNL" xnet "…PrjPcb" --net PP3V3 --skip C   # 电源轨追网, 跳过电容看主链路
python "$UNL" comps "…PrjPcb" --type U --mpn TPS    # 全板用了哪些 TI 电源片
```

## 平台哲学在本模块的落法

- **结论必须落到出处**：说"STB 脚在哪"，native 侧给 `位号.脚号 → 网络名`；PDF 侧给 `页码(坐标)`。
- **数值不手算**：连通性/成员全走脚本；PDF 侧不假装知道连通性（能力边界明说）。
- **不确定就明说**：PDF 侧一切输出都是启发式（位号/值关联/网络标号都可能含误报或漏报），最终以 EDA 源文件为准。

## 坑（实测）

- **PDF 侧值关联靠"阅读顺序"不是几何**：OrCAD 层次图导出 PDF 里，值文本与位号几何上相距 50~70pt 且与邻居交叉，几何就近关联几乎全错；但 PDF 文本块写出顺序里"位号→值"严格相邻，按 (block,line,word) 顺序配对才可靠（B26296.pdf 实测：R14→390kohm，与分压注释 13.5V/(390K+33K) 吻合）。
- **PDF 侧中文值 vs 中文注释**：国产库值行（"厚膜电阻,1/16W,390kohm,±1%,0402,SMD"）有 ASCII 数字+半角逗号；图纸注释（"此处静态电流I"）通常没有——据此区分，仍可能误报。
- **PDF 侧位号含交叉引用标签**：层次图导出会带 COR14/PIR1401 这类出现标签和 A1 这类跨页链接标签，都被当位号收进来（comps 会列出）；BOM 已把"未关联到值"的单独报数量不计入表。
- **扫描图 PDF 不可用**：info 会按页文本量告警；确认是扫描图就别硬跑。
- **universal-netlist 的 KiCad 路径**：优先读工程旁已导出的 `.net`；没有时要 kicad-cli（可 `KICAD_CLI_PATH` 指定）。KiCad 10 变体信息由解析器自己套用（kicad-cli 导出不带变体）。
- **本桥 xnet 与官方 MCP query_xnet 有差**：电源/地停止网的判定是本脚本的简化正则，官方 MCP server 有更完整的 power-rail 语义；重要结论交叉核对（或直接给 MCP 挂官方 server）。
- **密码保护的 OrCAD**：密码从环境变量读，见官方 docs/password-protected-designs.md。

## 环境实测记录（2026-10-27）

- universal-netlist v1.12.2 经 npm 全局安装于本机（node 在 D:\node.exe）；KiCad 最小样例（.kicad_pro+.net）`export-json` 通过，schema v2 解析正确。
- B26296.pdf（34 页 OrCAD 层次图，G.EQC1601.MB.1 车身控制器）全量验证：位号 15868（含交叉引用标签）、值关联成功 2849、网络标号 2183；BOM 头部 271×0.1uF/189×0Ω/177×10k 与车身控制器规模吻合。

## 与其他模块的关系

- 自包含模块，不依赖 serial-log/dbc。
- 硬件连接查完后常与 serial-log（引脚配置与日志行为对不上时）或 dbc（CAN 通道对应关系）联动，按 [../../SKILL.md](../../SKILL.md) 规则分两次执行。
