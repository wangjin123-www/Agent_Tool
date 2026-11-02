# lookup 参考文档

> 本文件是 SKILL.md 中 `lookup` 命令的**次选**路由。确定性操作请走首选脚本
> `python scripts/cmd/cmd_lookup.py <关键词>`。

## 何时读这份文档

- 不确定关键词该怎么写（大小写/中英文）
- 命中结果为空需要换词
- 需要解释脚本给出的路径依据

## 匹配口径

1. **训练工程**：关键词（不区分大小写）作为子串匹配工程目录名。例：`wkup` → `S32K344_Wkup_Lab_090_34`；`spi` → 3 个 LPSPI 工程 + FlexioSpi 工程。
2. **教学文档**：两级匹配——
   - 先按文件名（stem）子串匹配：`flash` → flash.md
   - 文件名不中再读文档全文子串匹配（能命中正文里的 API 名，如 `C40_Ip`）

## 常用关键词速查

| 你想要的外设 | 推荐关键词 | 命中 |
|------|------|------|
| 低功耗唤醒/WKPU | `wkup` | S32K344_Wkup_Lab_090_34 + wkup.md |
| CAN | `can` | S32k344_CAN_Example_090_34 + can.md |
| ADC/触发转换 | `adc` 或 `bctu` | 3 个工程 + adc.md |
| Flash/NVM | `c40` / `fls` / `fee` | 4 个工程 + flash.md |
| eMIOS/PWM | `emios` | 2 个工程 + emios.md |
| SPI | `spi` | 4 个工程 + spi.md |
| 中断/ICU/PIT/STM/OSIF | `pit` 或 `osif` 或 `intctrl` | timing.md |

## 常见异常与处置

| 现象 | 处置 |
|------|------|
| 工程命中但文档为空 | 该外设无独立文档，看 list.md 的映射表找归属（misc1/misc2 合并多篇） |
| 全空 | 换更短的关键词；确认训练库路径有效（跑 `cmd_list.py`） |
