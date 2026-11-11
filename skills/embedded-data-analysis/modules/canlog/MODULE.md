# 模块：CAN 总线日志（BLF/ASC）分析

> embedded-data-analysis（嵌入式数据分析）的 canlog 模块。读=**python-can**（GitHub hardbyte/python-can，Vector BLF 的标准 Python 实现，兼 ASC/TRC/CSV/candump）；解码=**cantools**；**波形=cantools 自带 `cantools plot`**（matplotlib 引擎，`-o` 存 PNG，支持子图/双纵轴/通配符/样式——波形图由该工具本身绘制，本模块只负责把日志转成 candump 流喂给它）；**表格=stdout 表格 + CSV/XLSX 导出**（openpyxl）。确定性解析全在库+脚本 `scripts/canlog/canlog_tools.py`，AI 只做解释。

## 支持格式

| 格式 | 读 | 写/转 | 说明 |
|---|---|---|---|
| `.blf`（Vector 二进制） | ✅ | ✅ | 主路径，CANoe/CANalyzer/CANlog 原生格式 |
| `.asc`（Vector 文本） | ✅ | ✅ | 跨工具通用文本格式 |
| `.trc`（PEAK） | ✅ | - | python-can TRCReader |
| `.csv` / candump(`.log/.canlog`) | ✅ | ✅(csv) | Linux candump 流、python-can CSV |

## 依赖

```bash
python -m pip install python-can cantools matplotlib    # 前两者已装(4.6.1 / 45.1.0), matplotlib 3.11.2 已补装
python -m pip install openpyxl                          # xlsx 导出用, 已装
# 国内镜像加 -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## 工具速查

```bash
CLT="$(git rev-parse --show-toplevel)/.claude/skills/embedded-data-analysis/modules/canlog/scripts/canlog/canlog_tools.py"
python "$CLT" <子命令> <log> ...      # --help 看全量
```

| 子命令 | 用途 |
|---|---|
| `info <log>` | 总览：帧数/时长/平均负载/通道/错误帧/ID 分布（Top15+估算周期+11/29bit） |
| `frames <log> [--id 0x1A5] [--ch N] [--limit N]` | 原始帧清单（时间/通道/ID/DLC/数据 hex） |
| `decode <log> --dbc X.dbc [--id] [--signals a,b] [--limit]` | 物理值解码表（缩放+值表符号翻译，含中文值） |
| `export <log> --dbc X.dbc [--format csv\|xlsx] [--layout long\|wide] [--out F]` | 全量信号导出：long=透视友好一行一信号，wide=一帧一行 |
| `plot <log> --dbc X.dbc --signals "a,b[:fmt] - c" [--out F.png]` | **波形图（cantools plot 引擎）**：`-o` 存文件；`-` 分子图 `,` 分纵轴 `*?` 通配 |
| `convert <log> --to asc\|blf\|csv [--out F]` | 格式互转 |
| `scan [--dir D]` | 扫描目录找 .blf/.asc/.trc/.canlog |

## 典型工作流

### 1. 拿到实车 BLF，先看懂里面有什么

```bash
python "$CLT" scan --dir "D:\问题车数据"          # 找日志
python "$CLT" info 路径/x.blf                     # 哪些 ID、周期对不对、有没有错误帧
python "$CLT" frames x.blf --id 0x1A5 --limit 5   # 看原始字节
```

### 2. 结账问题定位：把信号解码出来看时序

```bash
python "$CLT" decode x.blf --dbc V837.dbc --id 0x1A5 --signals PEPS_StartrequestValid,PEPS_RollingCounter_0x1A5
python "$CLT" plot x.blf --dbc V837.dbc --signals "PEPS_StartrequestValid - PEPS_RollingCounter_0x1A5" --out wave.png
```

### 3. 给评审/Excel 出表

```bash
python "$CLT" export x.blf --dbc V837.dbc --format xlsx --layout long --out 信号表.xlsx
# long 布局直接在 Excel 里做透视表(报文/信号为维度); wide 布局适合按行扫
```

## 平台哲学在本模块的落法

- **结论必须落到出处**：说"信号什么时候变"，给 `时间 报文 信号=值`（decode 输出）或波形 PNG；说"丢帧"，给 info 的 ID 帧数/周期 vs DBC 周期。
- **数值不手算**：解码/统计全走脚本。
- **不确定就明说**：ID 与 DBC 不匹配时 decode 报 0 帧可解码并提示对照 info。

## 坑（实测）

- **cantools 解码的值表值是 NamedSignalValue 对象**不是 str：导 xlsx 必须转（脚本已处理），自己写代码要注意。
- **BLF 时间戳是相对 log 起点的秒数**（python-can 行为）：脚本输出统一转为相对首帧的秒；绝对时刻要看 BLF 文件头的日志起始时间（info 首帧时间戳）。
- **`cantools plot` 无 BLF 直读能力**（只吃 candump 文本）：本模块靠 BLF→candump 流桥接；信号语法是 cantools 自己的（`Msg.sig[:fmt]`，`-` 子图、`,` 纵轴、`*?` 通配），详见 `python -m cantools plot --help`。
- **plot 存文件时**脚本强制 `MPLBACKEND=Agg`（无窗口）；不给 `--out` 则开交互窗口，需本地图形环境。
- **估算周期 = 时长/帧数**：丢帧/突发时偏乐观，精确周期用 frames 两帧差。
- **GBK 编码 ASC**：国产工具导的 ASC 可能 GBK，python-can 自动处理；DBC 侧沿用 dbc 模块的编码嗅探。
- 大 BLF（几百 MB）全量 list 进内存：info/frames 够快，export 全量解码会慢，先用 `--id/--signals` 收窄。

## 环境实测记录（2026-10-27）

- 用真实 JMC V837 DBC（V3.4）+ python-can BLFWriter 合成 45 帧 BLF（0x1A5 30 帧 + 0x310 15 帧）全链路验证：
  - info：ID 分布 0x1A5/10ms、0x310/19ms ✓
  - decode：中文值表（上高压/下高压）正常翻译 ✓
  - plot：cantools 引擎输出 wave.png（双子图+自定义线型）✓
  - export：xlsx long 735 行 / wide 45 行×40 列 ✓；convert BLF→ASC ✓
- python-can 4.6 属性名为 `is_extended_id`（老教程写 `is_extended_frame` 会 AttributeError）。

## 与其他模块的关系

- **与 dbc 模块**：dbc 管"矩阵本身"（报文/信号布局、单帧手工 decode/encode、生成 C 代码），本模块管"日志流"（成千上万帧的解码/波形/导出）；DBC 检索/造帧走 dbc 模块，看实车/台架日志走本模块。
- 与 serial-log 模块：CAN 日志 + 串口日志同一问题交叉分析时，分两次执行（平台路由规则）。
