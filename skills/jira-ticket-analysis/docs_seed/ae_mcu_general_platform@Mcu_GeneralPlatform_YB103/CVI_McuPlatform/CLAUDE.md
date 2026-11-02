# CVI_McuPlatform(整车主控 MCU 平台代码,按 L1~L6 分层;本文件为平台总览 + L6 公共类型层文档)

## Architecture(上层依赖下层,禁止反向依赖)
```
CVI_McuPlatform/
  L1_Applications/   # 应用层:仪表显示/CAN 通信/诊断/按键/电源等业务,按项目分 WB101/WY113/YB103 子目录
  L2_Tasks/          # 任务层:FreeRTOS 任务封装(Task_*),统一入口 Tasks_LowInf
  L3_RTOS/           # OS 层:OS1_FreeRTOS 内核 + OS2_TmrSched 备用调度器(二选一)
  L4_Services/       # 服务层:CAN 总线/UDS/存储/电源等中间服务(Service_*)
  L5_EcuAL/          # MCU 抽象层:封装 RTD 驱动(Adc/Can/Fls/Pwm/Port/Lin...)
  L6_Public/         # 平台级公共类型与项目配置(全局头之一;用户侧公共头在仓库根 inc/)
```
- 每层模块统一三段式:`<Xxx>UpInf`(对上层暴露的接口)/`<Xxx>`(核心逻辑)/`<Xxx>LowInf`(对下层的封装);跨层调用只经 UpInf/LowInf 接口头文件。
- 各层子目录详情见各自 CLAUDE.md(L1_Applications/、L2_Tasks/、L3_RTOS/、L4_Services/、L5_EcuAL/)。

## Key Files
- `L6_Public/Public_TypeDef/Proj_Cfg.h` - 车型总开关:注释/放开 `PROJECT_WEIQIAO_WB101/WY113/YB103` 三行宏选项目(当前 WB101)
- `L6_Public/Public_TypeDef/Proj_Cfg_WB101.h`(及 _WY113/_YB103) - 各车型配置与版本号 `WB101_MCU_VERSION`;三个文件始终被包含,内容靠车型宏守卫
- `L6_Public/Public_TypeDef/Proj_Includes.h` - 公共类型 + 项目配置的标准入口 include
- `L6_Public/Public_TypeDef/Public_StdTypes.h` / `Public_DataTypes.h` / `Public_DrvTypes.h` / `Public_CanDataTypes.h` - 全平台基础类型(`uint8/sint*` 前缀、`boolean`)
- `L6_Public/Public_TypeDef/Os_TypeDef.h` - 任务函数指针类型、调度器选择宏 `MCU_SCHED_TYPE`(当前 FreeRTOS)、基础节拍 `TASK0_TIMER_PERIOD`(5ms)

## Gotchas
- 切换车型只改 `Proj_Cfg.h`;但选 YB103 时还有二级子项目宏(`WY115/WY110/YB103_PROJECT`,在 `Proj_Cfg.h` 内切换),漏改会带着错误配置编译通过。
- 跨层 include 全部用相对路径(`..\..\L4_Services\...`),且正/反斜杠混用——移动或重命名目录会静默断链;新增跨层引用时沿用同风格的相对路径。
- 新增公共类型必须收敛到 `L6_Public` 并经 `Proj_Includes.h` 引出,不要在业务层自造全局类型定义。
- 版本号字符串 `WB101_MCU_VERSION`(格式 `项目号_版本号_发布日期`,如 `WB101_V1.0.16.0.0_20260831`)发布前必须手工更新;`extern MCU_VERSION` 供诊断读取,`FUEL_/HYBRID_MCU_VERSION` 是它的别名。
