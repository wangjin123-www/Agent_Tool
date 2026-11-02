# s32k3-rtd-master

S32K3（NXP S32K344，RTD 0.9.0 / S32DS v3.4）大师级专家库：把官方训练库 29 个示例工程拆成按外设分篇的教学文档（代码逐字符原样摘录），支持工程索引 / 定位 / 写码指导生成。**仅显式调用，不自动触发。**

## 使用

```
/s32k3-rtd-master list
/s32k3-rtd-master lookup wkup
/s32k3-rtd-master guide spi
```

## 操作

| 命令 | 说明 |
|------|------|
| list | 列出训练库 29 个外设示例工程索引（可带关键词过滤） |
| lookup | 按外设关键词定位训练工程路径与教学文档 |
| guide | 抽取教学文档章节 + 原样代码块，生成写码指导到 output/ |

## 目录结构

```
s32k3-rtd-master/
├── SKILL.md          # 必需：纯路由器（Entry 表 + 各命令首选脚本/次选参考行）
├── scripts/          # 固定三层，勿改层名
│   ├── cmd/          # 入口层：cmd_{list,lookup,guide}.py 薄壳
│   ├── core/         # 业务层：core.py（TOPIC_RULES 映射、索引/定位/抽取逻辑）
│   └── common/       # 公共层：conf.py 读 config.conf、log.py UTF-8 输出
├── references/       # 教学文档：wkup/can/adc/emios/flash/spi/iic/uart/lin/
│                     #   timing/rtc/dma/misc1/misc2 + list/lookup/guide
├── config/           # config.conf（训练库绝对路径，gitignored）
├── output/           # 运行时输出（gitignore）
├── README.md
├── .gitignore
└── LICENSE.txt
```

## 铁律

1. references 里的示例代码与官方源文件逐字符一致，写码沿用其写法，禁止改写。
2. 结论必须落到 `文件:行号` 或工程路径。
3. 外设问题先 `lookup` 定位，再读 references 原文，不凭记忆。
4. 训练库未覆盖的内容明确说"训练库无此内容"。
