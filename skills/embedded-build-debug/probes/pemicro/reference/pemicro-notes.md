# PEmicro 探针调研笔记（2026-11-06）

背景：S32K312 + Multilink，S32DS launch 为 `com.pemicro.debug.gdbjtag.pne`，目标命令行化烧录/调试。

## 结论

第一版采用 **pegdbserver_console + gdb batch**（已实现于 `scripts/pemicro_ops.py`）：

- 零新增安装（S32DS 自带）、免费、Windows 原生
- headless flash / erase / reset / halt / 读写内存全具备
- 与现有探针硬件和 launch 配置完全同源
- S32K358 多核双实例命令行烧录有官方论坛实证

## 备选路径对比

| 路径 | 评估 |
|---|---|
| pegdbserver_console + gdb batch | **已采纳**。参数支持 `-flashobjectfile`、`-attachonly`、`-forcemasserase`、`-corenum`（多核）、`-configfile` |
| pyOCD + PEmicro 插件（0.36+，`pip install pyocd[pemicro]`，Apache-2.0） | 二期候选。配 S32K3 CMSIS-DFP 后 `pyocd flash -t s32k312 xxx.elf`；Zephyr MR-CANHUBK3(S32K344) 的 pyOCD runner 已实证 |
| cprog / Cyclone Control Console | 仅支持 Cyclone 独立编程器，不支持 Multilink，不适用 |
| S32 Flash Programmer | 仅 GUI，无 CLI |
| S32 Flash Tool | S32G SoC 串口/网口烧写，非探针路径 |
| J-Link 替换 | SEGGER V6.89c+ 支持 S32K3 全家族（含 S32K312），JLink.exe 无头能力最强，但需另购硬件；现有 Multilink 无法复用。长期备选（板上预留 J-Link 口时可切 `--probe jlink`） |

## Claude/LLM 生态

未发现现成的 pemicro/s32ds skill（生态刚起步），本探针层为自建。

## 来源

- [PEmicro GDB Server 命令列表](https://www.atwww.pemicro.com/learningcenter/contents.cfm?content_id=192)
- [PEmicro GDB Server 用户手册](https://www.pemicro.com/manuals/pegdbserver/getting_started/)
- [PEmicro 论坛: S32K3 命令行烧录](https://www.m.pemicro.com/forums/forum.cfm?forum_topic_id=8480)
- [PEmicro 论坛: S32K358 多核命令行烧录](https://httpswww.pemicro.com/forums/forum_topic.cfm?forum_id=9&forum_topic_id=9116)
- [DZone: GDB 批量编程（J-Link 与 P&E Multilink）](https://dzone.com/articles/batch-programming-with-gdb-segger-j-link-and-pe-mu)
- [pyOCD 安装文档（PEmicro 插件）](https://pyocd.io/docs/installing)
- [Zephyr MR-CANHUBK3 (S32K344) runners](https://docs.zephyrproject.org/latest/boards/nxp/mr_canhubk3/doc/index.html)
- [SEGGER Wiki: NXP S32K3xx 支持列表](https://wiki.segger.com/NXP_S32K3)
