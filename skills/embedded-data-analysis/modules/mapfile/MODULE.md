# 模块：链接 map 文件分析

> embedded-data-analysis（嵌入式数据分析）的 mapfile 模块。基于 GitHub 开源库 [mapfile-parser](https://github.com/Decompals/mapfile-parser)（MIT，Rust 后端，pip 直装），在其上做嵌入式常用查询：存储区占用 / 符号定位 / 模块体积排行 / 两版 map 对比。确定性解析全在库+脚本 `scripts/map/map_tools.py`，AI 只做解释。

## 为什么不按芯片分类（决策记录）

**不需要，未加芯片分类。** 依据：
1. map 文件格式由**工具链**决定（GNU ld / clang lld / Metrowerks ld / IAR ilinkarm / ARM armlink 各一套语法），与芯片无关，库按文件特征自动识别——分类维度应该是工具链，而工具链恰好都能自动判。
2. 地址→含义的映射 map 文件**自包含**：GNU ld map 的 `Memory Configuration` 块自带 region 名/origin/length（本工程 S32K312 的 map 里 `int_pflash 0x00400000 0x1D4000`、`int_dtcm 0x20000000` 等一应俱全），不需要外部芯片知识库来解释。
3. 若未来加芯片层（如"0x20410000 是 shareable 区、CAN RAM 在 0x40400000"这类外设语义），那属于查芯片手册（RM/DS）的活，与 map 解析解耦，不进本模块。

首个实测目标：S32K312 + S32DS ARM GCC 10.2（GNU ld map，本仓库 `Debug_FLASH/test_prj.map`）。

## 支持格式

| map 来源 | 支持 | 说明 |
|---|---|---|
| GNU ld（GCC/binutils，含 S32DS） | ✅ | 实测主路径 |
| clang lld | ✅ | 库声称支持 |
| Metrowerks ld（老 CodeWarrior） | ✅ | 库声称支持 |
| IAR ilinkarm | ❌ | `info` 会报"不支持"；要支持需换库（如 iemap，未集成） |
| ARM armlink/armclang | ❌ | 同上 |

## 依赖

```bash
python -m pip install mapfile-parser        # 本机已装 2.13.2
# 国内镜像: python -m pip install mapfile-parser -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## 工具速查

```bash
MAP_TOOLS="$(git rev-parse --show-toplevel)/.claude/skills/embedded-data-analysis/modules/mapfile/scripts/map/map_tools.py"
python "$MAP_TOOLS" <子命令> <map> ...    # --help 看全量
```

| 子命令 | 用途 |
|---|---|
| `info <map>` | 总览：工具链识别 / Memory Configuration 存储区表 / 段布局 / 符号总数 |
| `regions <map>` | 存储区占用率：region 已用/剩余/百分比条（Flash 够不够一眼看） |
| `symbols <map> --match xTask` / `--exact xTaskCreate` | 符号查询：地址/大小/段/所在 .o（"这个变量/函数在哪、多大"） |
| `largest <map> [--top N] [--ram]` | 最大的输入节（哪块代码最吃 Flash；`--ram` 只看 .bss/.data） |
| `objects <map> [--top N] [--match PAT]` | 按 .o 文件聚合体积（哪个模块最占） |
| `diff <mapA> <mapB> [--top N]` | 两版 map 对比：新增/删除/变大/变小 TopN（优化前后对比） |
| `scan [--dir D]` | 扫描目录找 .map（按修改时间倒序） |

## 典型工作流

### 1. 新版本固件 Flash/RAM 涨了多少，涨在哪

```bash
python "$MAP_TOOLS" diff Debug_FLASH/test_prj_old.map Debug_FLASH/test_prj.map --top 15
python "$MAP_TOOLS" regions Debug_FLASH/test_prj.map
```

### 2. 排查符号位置（HardFault 地址反查 / 变量在哪个区）

```bash
python "$MAP_TOOLS" symbols Debug_FLASH/test_prj.map --exact uxBaselo   # 看地址落在哪个区
python "$MAP_TOOLS" symbols Debug_FLASH/test_prj.map --match Standby
```

### 3. 裁剪体积

```bash
python "$MAP_TOOLS" objects Debug_FLASH/test_prj.map --top 20           # 谁最占(本工程 main.o 21.3K 居首)
python "$MAP_TOOLS" largest Debug_FLASH/test_prj.map --ram              # RAM 大头(实测 EcuAL_Spi .bss 2.0K)
```

## 平台哲学在本模块的落法

- **结论必须落到出处**：说"某个函数多大"，给 `符号名 地址 大小 所在 .o`（symbols 输出格式）；说"Flash 用了多少"，给 regions 表。
- **数值不手算**：占用率/聚合/对比全走脚本。
- **不确定就明说**：`info` 识别不了工具链（IAR/armlink）直接说不可用，不硬解析。

## 坑（实测）

- **region 使用率是输入节累加**，排除 fill/调试节，与链接器汇报的精确值有少量对齐差额（本工程 int_pflash 8.6% vs segment 合计 169.9K/1872K，量级一致）。
- **符号 size 大多数有值但非全部**：GNU ld map 的符号行带 size（如 xTaskCreate=92），个别为 0（对齐/汇编符号），输出如实展示。
- **库会生成 `$_static_symbol_*` 合成名**（decomp 用途的占位符号），本脚本所有查询已过滤。
- **`*default*` region**（length=0xFFFFFFFF）是 GNU ld 兜底区，占用恒 0，正常现象。
- **diff 的键是 (符号名, .o 路径)**：同名符号在不同 .o 里算不同条目；静态函数重名跨文件时会分别列出。
- **map 路径里混合 `/` 和 `\`**（S32DS 产物，libc_nano.a 行是反斜杠），脚本已归一化。

## 与其他模块的关系

- 自包含模块，不依赖 serial-log/dbc/schematic。
- 与 schematic 模块天然互补：原理图查"板上有什么"，map 查"镜像里有什么"（如 FreeRTOS 堆大小 ↔ 原理图 RAM 选型）。
- HardFault 地址反查：先 `symbols --match` 或按地址对段定位（.int_vector/.pflash 范围见 `info`），再结合 serial-log 抓的现场日志分析。
