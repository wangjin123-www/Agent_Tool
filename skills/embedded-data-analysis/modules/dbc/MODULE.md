# 模块：DBC / CAN 数据库分析

> embedded-data-analysis（嵌入式数据分析）的 DBC 模块。基于 **cantools**（Python 生态最主流的 DBC/车载数据库库，pip 直装）。确定性解析全在脚本 `scripts/dbc_tools.py`，AI 只做解释。

## 依赖

```bash
python -m pip install cantools        # 本机已装 45.1.0
# 国内网慢: python -m pip install cantools -i https://pypi.tuna.tsinghua.edu.cn/simple
```

- 脚本自检缺库会给装法（exit 3）。
- **环境坑（已修复，2026-10-26 复盘）**：本机 python（`C:\Users\Lenovo\python-sdk\python3.13.2`）曾因 grpcio-tools/setuptools dist-info 的 `entry_points.txt/top_level.txt` 共 4 个文件是**加密态**（公司加密按扩展名管 .txt；2026-03-12 一次不受信进程上下文里的 pip 安装所致）导致 `import cantools` 炸 UnicodeDecodeError——初判"GBK 编码"是错的，密文无钥不可解。**修复 = 删 4 个密文文件 + `pip install --force-reinstall --no-deps grpcio-tools==1.78.0 setuptools==82.0.1`**（密文存在时 pip 卸载/重装都会撞密文崩，先删再装才通；缺文件=跳过、密文=炸）。已验证三绿：密文归零 / 裸 import 干净 / dbc_tools 无环境提示。脚本内的 entry_points 容错补丁**保留**（防同类事件复发；再遇密文元数据时只是打一行提示不影响功能）。

## 工具速查

```bash
DBC_TOOLS="$(git rev-parse --show-toplevel)/.claude/skills/embedded-data-analysis/modules/dbc/scripts/dbc_tools.py"
python "$DBC_TOOLS" <子命令> ...    # --help 看全量
```

| 子命令 | 用途 |
|---|---|
| `info <dbc>` | 总览：节点/报文/信号数、周期报文占比、发报 Top3 节点 |
| `messages <dbc> [--id 0x1A0 \| --msg 子串 \| --node N \| --rx-node N]` | 报文清单（ID hex/dec、DLC、周期、发送者，带 Mux 标记） |
| `signals <dbc> --msg 名字或ID` | 信号明细：bit 起/长、字节序、缩放/偏移、单位、范围、**值表**、接收者 |
| `decode <dbc> --msg X --data "01 AB ..."` | 原始字节→物理值（符号翻译 + raw 双口径） |
| `encode <dbc> --msg X --set "Sig=v1,Sig2=On" [--loose]` | 物理值→原始字节（带回读校验） |
| `dump <dbc> --format table\|json\|csv [--out F]` | 全量导出（csv 带 BOM，Excel 直开） |
| `c-code <dbc> [--out DIR] [--no-float] [--use-float] [--node N]` | 生成 MCU 端 C 解析代码（.h/.c） |
| `scan [--dir D]` | 扫描目录找 .dbc（按修改时间倒序） |

## 典型工作流

### 1. 拿到一个陌生 DBC，先看懂它

```bash
python "$DBC_TOOLS" scan --dir "D:\项目目录"        # 找到有哪些 DBC(含版本演进的多个)
python "$DBC_TOOLS" info "<dbc>"                     # 总览: 谁在发报、多少报文/信号
python "$DBC_TOOLS" messages "<dbc>" --node CCU      # 按节点过滤报文清单
python "$DBC_TOOLS" signals "<dbc>" --msg 0x1A5      # 深挖某条报文的信号布局
```

### 2. 解一帧实车/日志里抓到的数据

```bash
python "$DBC_TOOLS" decode "<dbc>" --msg 0x1A5 --data "40 03 00 00 00 00 00 00"
```

输出物理值 + 符号含义 + raw 值。数据字节数必须等于 DLC，否则报错。

### 3. 构造一帧要发送/要灌的数据

```bash
# 严格模式(默认): 必须给全所有信号
python "$DBC_TOOLS" encode "<dbc>" --msg X --set "A=1,B=2.5,C=On"
# 宽松模式: 没给的信号按 initial/min/0 预填(多路复用报文必须用它或给全)
python "$DBC_TOOLS" encode "<dbc>" --msg X --set "A=1" --loose
```

值可以写数字（`2`、`0x1A`、`2.5`）或值表里的符号名（`ON`、`Remote start mode`）。输出 hex 字节 + 回读校验（按物理数值比对，符号翻译不误报）。

### 4. 生成 MCU 端 C 解析代码

```bash
python "$DBC_TOOLS" c-code "<dbc>" --out 输出目录 [--no-float] [--node CCU]
```

- 纯 C、无动态内存，可直接拷入 MCU 工程（本工程 S32K3 也适用）。
- 默认 double 缩放；无 FPU 用 `--no-float`（定点），要 float 用 `--use-float`。
- 大矩阵产物很大（实测 V837 全库 .h 2.4MB），建议 `--node` 只生成本节点收发的报文。

### 5. 导出给评审/Excel

```bash
python "$DBC_TOOLS" dump "<dbc>" --format csv --out 输出.csv
```

## 平台哲学在本模块的落法

- **结论必须落到出处**：说"车速信号在哪"，要给出 `报文名 ID=0xXXX 信号名 bit起/长 字节序 缩放/偏移`——`signals` 子命令的输出就是出处格式。
- **数值不手算**：decode/encode 全走脚本，AI 不做位运算心算。
- **不确定就明说**：DBC 里没有的信号/找不到的 ID，脚本报"找不到"，AI 不猜。

## 坑（实测）

- **国产 DBC 是 GBK 编码**（JMC 系全中招）：脚本自动嗅探（字节非合法 UTF-8 → 按 GBK 读），值表里的中文（如"上高压/下高压"）正常显示；可用 `--encoding` 强制覆盖。
- **多路复用报文 encode**：mux 选择信号缺失会 KeyError——默认严格模式要求给全信号；`--loose` 预填缺省（mux 信号也预填 0，注意选中的分支）。
- **滚动计数/校验和信号**（`XXX_RollingCounter`/`XXX_Checksum`）在 JMC DBC 里是普通信号，encode 不会自动算——构造完整合法帧要自己填对。
- cantools 也支持 .arxml/.kcd，本工具主打 .dbc；J1939 库的 PGN 语义未特化处理（`info` 会报 PGN 报文数）。
- 实测样例库：`D:\wnagjin\Compay_Project\JMC\dbc_file\`（V837 车身矩阵，120 报文/1052 信号，全多路复用）。

## 与其他模块的关系

- 自包含模块，不依赖 serial-log；未来若要做"CAN 总线日志(BLF/ASC) + DBC 解码"的新模块，把日志解析放新模块、复用本模块的 `load_db`/decode 思路，按 [../../SKILL.md](../../SKILL.md) 扩展规范落位。
