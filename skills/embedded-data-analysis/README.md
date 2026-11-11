# embedded-data-analysis（嵌入式数据分析）

嵌入式领域多数据形态分析平台（Claude Code skill）。一种数据形态一个模块，模块自包含、可独立扩展。

## 模块

| 模块 | 目录 | 一句话 |
|---|---|---|
| 串口日志 | `modules/serial-log/` | 串口采集（Web 实时/后台写文件）→ 分析（固定/自由格式，结论反查工程源码）→ HTML 报告 → 邮件。原独立 skill `serial-log`，2026-10-26 并入 |
| DBC | `modules/dbc/` | CAN 数据库解析（cantools）：报文/信号检索、原始帧 decode/encode、导出、生成 C 解析代码 |
| 原理图 | `modules/schematic/` | EDA 源文件（OrCAD .DSN / Altium .PrjPcb / KiCad，基于 universal-netlist）精确查器件/引脚/网络/追网；原理图 PDF 文本层启发式分析（位号/值/BOM/网络标号定位），2026-10-27 新增 |
| 链接map | `modules/mapfile/` | map 文件分析（基于 mapfile-parser，GNU ld/lld/Metrowerks）：存储区占用率/符号查询/模块体积排行/两版 map 对比；不按芯片分类（map 自包含存储区语义），2026-10-27 新增 |
| CAN日志 | `modules/canlog/` | CAN 总线日志 .blf/.asc（python-can 读 + cantools 解码）：帧统计/ID 分布/物理值解码/cantools plot 原生波形(PNG)/CSV·XLSX 表格导出/格式互转，2026-10-27 新增 |
| Config Tools配置 | `modules/mex/` | NXP Config Tools `.mex`（标准库 XML 解析，无依赖）：芯片/工具总览/引脚标签与功能路由/时钟配置/外设实例与参数/生成文件清单/两版配置对比，2026-11-06 新增 |

用法入口见 [SKILL.md](SKILL.md)（路由层）；各模块详细文档见其目录内 `MODULE.md`。

## 分层

```
SKILL.md            路由层：意图识别 → 模块分发 + 平台规范（唯一 skill 入口）
modules/<形态>/      模块层：MODULE.md（工作流）+ scripts/（确定性工具）+ references/ + config/
```

加新数据形态的规范（目录约定、脚本自定位、何时上提共享配置）见 [SKILL.md](SKILL.md) 的「扩展规范」。
