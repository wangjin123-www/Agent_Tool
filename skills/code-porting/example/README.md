# example：示例输入与成品输出

## 输入（Phase 0 三参数）

| 参数 | 值 |
|---|---|
| 源工程 | `D:\wnagjin\Compay_Project\CDC_7255\6125\FreeRTOS_S32K312`（WB101 代码基） |
| 目标工程 | `D:\wnagjin\Compay_Project\CDC_7255\cdc_7255`（7255 平台 POC） |
| 移植范围 | 电源管理模块（高低压保护/状态机/上下电时序/STR/休眠唤醒 + 连带 App_HwFault） |

## 成品输出

`6125To7255电源管理移植.md` — 实际交付过的移植方案，`references/plan-template.md` 八段式模板的实测出处。
写方案前通读它，对齐：决策表的粒度、红线表的"源 vs 目标"两栏写法、修改清单的行数量化
（文件数/行数/file:line）、11 步每步带验证列、§六防漏细节的"不做就会错"密度、§八红线条目化。
