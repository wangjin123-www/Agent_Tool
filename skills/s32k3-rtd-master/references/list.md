# list 参考文档

> 本文件是 SKILL.md 中 `list` 命令的**次选**路由。确定性操作请走首选脚本
> `python scripts/cmd/cmd_list.py [关键词]`。

## 何时读这份文档

- 需要了解"工程目录 → 教学文档"的映射规则（关键词优先级）
- 脚本输出与预期不符需要人工判断原因
- 训练库新增工程后需要确认是否被索引

## 映射规则（core.py 的 TOPIC_RULES，按序首个命中）

| 关键词（出现在工程目录名中） | 教学文档 |
|------|------|
| wkup / wakeup | wkup.md |
| can | can.md |
| emios | emios.md |
| c40 / fls / fee | flash.md |
| adc / bctu | adc.md |
| lpspi / flexiospi | spi.md |
| iic / lpi2c | iic.md |
| lin | lin.md |
| uart | uart.md |
| rtc | rtc.md |
| intctrl / siul2_icu / pit_stm / osif | timing.md |
| edma / dma | dma.md |
| crc / trgmux / lcu / swt | misc1.md |
| sent / flexio / hse / gmac / sai | misc2.md |

注意：lpspi/flexiospi 规则在 dma 之前（`S32K344_LPSPI_WithDMA` 含 "dma"，应归 spi.md）。

## 索引口径

- 工程判定：训练库根路径（`config/config.conf` 的 `[paths].training_root`）下**直接子目录且含 `.cproject`** 的目录
- 当前库：S32K344，RTD 0.9.0，S32DS v3.4，共 29 个工程

## 常见异常与处置

| 现象 | 处置 |
|------|------|
| `未配置训练库路径` | 检查 `config/config.conf` 是否存在 `[paths]` 段及 `training_root` 键 |
| `训练库路径不存在` | 路径写错/移动，用 `cmd_lookup.py` 也会失败，先修 config |
| 工程未标教学文档（显示 `-`） | 目录名不含任何映射关键词，人工确认后往 TOPIC_RULES 加规则 |
