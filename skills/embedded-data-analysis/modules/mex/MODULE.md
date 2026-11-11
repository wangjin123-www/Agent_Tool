# 模块：NXP Config Tools `.mex` 配置分析

> embedded-data-analysis（嵌入式数据分析）的 mex 模块。`.mex` 是 NXP MCUXpresso Config Tools（S32DS 内置）的工程配置源，本质是分层 XML。本模块做只读分析：芯片/工具总览、引脚标签与功能路由、时钟配置、外设实例与参数、生成文件清单、两版配置对比。确定性解析全在 `scripts/mex/mex_tools.py`（**仅 Python 标准库**），AI 只做解释。

## 参考实现（GitHub）

| 项目 | 关系 | 说明 |
|---|---|---|
| [zephyrproject-rtos/hal_nxp · `mex_utils.py`](https://github.com/zephyrproject-rtos/hal_nxp/blob/master/mcux/scripts/pinctrl/shared/mex_utils.py) | **主要参考** | `NxpMexUtil` 用 `xml.etree.ElementTree` + 命名空间映射读取 `.mex`，取 board/processor/pins 版本；仅适配 `mex_configuration_14`，且只服务 i.MX RT/Kinetis/LPC 的 pinctrl 生成 |
| [wavenumber-eng/nxp_monkey](https://github.com/wavenumber-eng/nxp_monkey)（MIT，`pip install nxp-monkey`） | 参考 | 抓取/索引 NXP KEX 芯片数据（寄存器/信号/封装），**不解析工程 `.mex`**，故未集成 |
| NXP Config Tools | 数据来源 | `.mex` 的 schema 由工具定义，无公开稳定 API；本工具按 XML 结构直接读取 |

本模块自行实现解析器：**命名空间无关**（`mex_configuration_14/15` 及后续版本按本地标签名匹配），覆盖 `pins/clocks/periphs` 全量配置，而非只取版本号。

## 支持范围

| 项 | 支持 | 说明 |
|---|---|---|
| S32DS / S32K3 工程 `.mex` | ✅ | 实测 `test_prj.mex`（`mex_configuration_15`，Config Tools Pins 15.0 / Clocks 13.0 / Peripherals 14.0） |
| `mex_configuration_14` | ✅ | 用最小样例验证过命名空间兼容 |
| 其他 NXP 系列（i.MX RT/LPC/Kinetis/MCX） | ⚠️ | 同为 Config Tools 输出，结构一致即可读；未逐一家族实测 |
| 非 Config Tools 的 XML/文本 | ❌ | 根元素不是 `<configuration>` 会直接报错 |

## 依赖

无。只用 Python 3 标准库（`xml.etree.ElementTree`），不需要 pip 安装。

## 工具速查

```bash
MEX="$(git rev-parse --show-toplevel)/.claude/skills/embedded-data-analysis/modules/mex/scripts/mex/mex_tools.py"
python "$MEX" <子命令> <mex> ...      # --help 看全量
```

| 子命令 | 用途 |
|---|---|
| `info <mex>` | 总览：处理器/封装/内核/XML 模型、各工具版本与启用状态、配置对象计数、依赖规则计数 |
| `pins <mex> [--match PAT]` | 引脚标签表：`pin_num / pin_signal / label / identifier`（网络名反查物理引脚） |
| `routes <mex> [--peripheral P] [--match PAT]` | 功能引脚路由：初始化函数 → 外设信号 → 物理引脚 + 方向/标识 |
| `clocks <mex> [--config NAME] [--match PAT]` | 时钟配置：默认概览（时钟源 + 关键输出频率）；`--config` 打印全量源/输出/分频设置 |
| `instances <mex> [--match PAT] [--enabled-only]` | 外设实例清单：group/instance/type/mode/enabled/comment（comment 常含移植备注） |
| `config <mex> --instance NAME [--match PAT]` | 展开某实例的完整 `config_set`，路径形如 `Wkpu.IcuConfigSet.IcuChannel[0].IcuChannelId` |
| `settings <mex> --match PAT [--instance NAME] [--limit N]` | 全局搜索外设设置（路径或值正则，默认最多 200 条） |
| `files <mex> [--tool pins\|clocks\|periphs]` | 各工具声明的生成文件清单（`generated_project_files`） |
| `problems <mex> [--level N]` | Config Tools 记录的依赖/校验规则（`problem_level`，**规则不是当前报错清单**） |
| `diff <mexA> <mexB> [--top N]` | 两版 `.mex` 对比：引脚标签/路由/时钟/外设设置/生成文件的新增、删除、修改 |
| `scan [--dir D]` | 扫描目录找 `.mex`（按修改时间倒序） |

## 典型工作流

### 1. 接手工程，先看配置全貌

```bash
python "$MEX" info test_prj.mex
python "$MEX" instances test_prj.mex
python "$MEX" files test_prj.mex
```

`info` 给出芯片/封装/内核、三个配置工具的版本与启用状态、引脚标签/时钟配置/外设实例/设置项计数。`instances` 的 `comment` 列是工程师留下的移植备注（本工程 ADC 实例上就有 6125 通道映射说明）。

### 2. 查某个网络/引脚配置

```bash
python "$MEX" pins test_prj.mex --match PTE2          # 网络名 -> pin_signal/pin_num
python "$MEX" pins test_prj.mex --match ACC           # 模糊查
python "$MEX" routes test_prj.mex --match PTE2        # 功能路由 + 方向
```

注意 `.mex` 的 `pin_labels` 只记录**打过标签的信号**；未打标签但已路由的引脚只在 `routes`（functions_list）里出现。

### 3. 查外设参数（串口波特率 / PWM 周期 / ADC 通道 / WKPU 通道）

```bash
python "$MEX" config test_prj.mex --instance Lpuart_Uart --match "Baud|Parity|Stop"
python "$MEX" config test_prj.mex --instance Emios_Pwm --match "Period|Duty"
python "$MEX" config test_prj.mex --instance Adc_Sar_Ip --match "Channel|HwUnit"
python "$MEX" settings test_prj.mex --match "IcuWkpuChannel"   # 跨实例搜
```

### 4. 看时钟树

```bash
python "$MEX" clocks test_prj.mex                              # 两套配置概览
python "$MEX" clocks test_prj.mex --config ClockConfig1        # STANDBY 全量
python "$MEX" clocks test_prj.mex --match "PLL|FXOSC"          # 按 id/频率过滤
```

### 5. 改配置前后对比（评审/回归）

```bash
python "$MEX" diff test_prj.mex test_prj_new.mex --top 30
```

输出按 `pin_label[...] / route[...] / clock[...] / periph[...] / file[...]` 分类列出新增/删除/修改，修改项并列 A/B 值。

### 6. 确认生成面（哪些文件由 mex 生成）

```bash
python "$MEX" files test_prj.mex --tool pins     # board/Siul2_Port_Ip_Cfg.{c,h} 等
python "$MEX" files test_prj.mex --tool periphs  # generate/ 下 PBcfg 等 98 个
```

生成文件清单是「mex ↔ 代码」的同步边界；见下方坑位。

## 配置树结构（读懂输出的前提）

```
configuration
├─ common          processor / package / mcu_data / cores / description
└─ tools
   ├─ pins         pins_profile/pin_labels/pin_label      (pin_num,pin_signal,label,identifier)
   │               functions_list/function/pins/pin       (peripheral,signal,pin_num,pin_signal)
   │                 └─ pin_features/pin_feature          (name,value: direction/identifier/…)
   ├─ clocks       clock_configurations/clock_configuration
   │                 ├─ clock_sources/clock_source        (id,value,enabled)
   │                 ├─ clock_outputs/clock_output        (id,value)
   │                 ├─ clock_settings/setting            (id,value)
   │                 └─ dependencies/dependency           (problem_level,…)
   └─ periphs      functional_groups/functional_group/instances/instance
                     │  (name,type_id,mode,enabled,comment)
                     └─ config_set
                          setting  (name,value)
                          struct   (name)   -> 可嵌套
                          array    (name)   -> struct name=0,1,2… 表示下标
```

`config_set` 用 `struct/array/setting` 混合嵌套，**没有扁平键**；本工具按 `数组名[下标].字段` 展开，这也是 `config/settings/diff` 的键格式。

## 平台哲学在本模块的落法

- **结论落到出处**：说「PTE2 是 ACC 检测」，给 `pins --match PTE2` 的 `pin_num/pin_signal/label`；说「串口 115200」，给 `config` 里的具体设置路径与值。定位不到就明说「`.mex` 中未找到」。
- **数值不手算**：计数、展开、对比全部由脚本完成。
- **只读**：本模块不修改 `.mex`。要改配置走 Config Tools GUI 或按项目规范手改（并同步 `test_prj.mex`），见坑位。

## 坑（实测）

- **`problem_level` 是规则等级，不是当前错误列表**。`dependencies` 存的是 Config Tools 的校验规则（如「组件未找到则代码不会被编译」），规则是否满足要看 `feature` 里的期望值；GUI 的 Problems 视图才是求值后的结果。本工程 45 条规则中 level1=25 / level2=20，不能直接当成 45 个错误。
- **`identifier` 可含多个网络名**，用 `;` 分隔（如 `SER781_1V8_SW_EN;MCU2AVAS_STANDBY_N`）；`label` 只是其中一个。分析网络名时两个字段都要看。
- **`pin_labels` ≠ 全部已配置引脚**。只有人工打了标签的信号才进 `pin_labels`；其余路由在 `functions_list`。查引脚要 `pins` + `routes` 交叉看。
- **生成文件清单是同步边界**：本工程 `pins` 生成 `board/Siul2_Port_Ip_Cfg.*`，`periphs` 生成 `generate/` 下 98 个文件。只改 `board/` 或 `generate/` 而不同步 `test_prj.mex`，Config Tools 重新生成会回退（项目 CLAUDE.md 有 2026-11-05 心跳链回退实例）。
- **Config Tools 打开工程时手改 `.mex` 无效**：工具保存/Generate 会用内存模型重写文件。手改前先关闭 S32DS 工程/Config Tools（2026-11-05 实测）。
- **`.mex` 处于 DLP 透明加密目录时**：bash `grep/cat` 可能读到密文，Python 读是明文。本脚本用 Python 的 `ET.parse` 读，不受影响；手工取证也别用 `sed/echo`。
- **XML 命名空间版本随工具升级**：Pins 15.0 对应 `mex_configuration_15`。脚本按本地标签名匹配，不硬编码版本号；新增未知标签会被安全忽略（只影响该标签的展示，不影响已支持部分）。
- **`clocks` 的 `setting` 用 `id` 属性，`periphs` 的 `setting` 用 `name` 属性**；脚本已兼容两者。
- **空数组很常见**（如 `IcuSignalMeasurement`），展开时自然跳过，不代表配置丢失。

## 与其他模块的关系

- 自包含，不依赖其他模块。
- 与 **schematic** 互补：原理图查「板上有哪些网络/器件」，`.mex` 查「芯片引脚被配成什么功能」。
- 与 **mapfile** 互补：`.mex` 是编译前的配置真相，map 是编译后的镜像真相。
- 与 **embedded-build-debug** 配合：改完 `.mex` → Config Tools 重新生成 → 用 embedded-build-debug 验证编译。
- 与 **serial-log** 配合：配置侧（`.mex`）与运行侧（串口日志）对照，可快速定位「配置没生效 vs 代码没用上」。
