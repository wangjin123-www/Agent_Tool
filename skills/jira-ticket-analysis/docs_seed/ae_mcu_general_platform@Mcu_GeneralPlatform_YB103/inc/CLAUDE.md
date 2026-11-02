# inc / board / src(全局公共头、板级引脚配置与程序入口)

## Architecture
```
board/   # S32 Configuration Tools 生成的 SIUL2/TSPC 引脚配置(工具产物,勿直接手改)
inc/     # 全局公共头:AUTOSAR 平台类型、公共宏、catarc 安全算法库接口、项目级配置
src/     # main.c:FreeRTOS 静态内存分配与 main() 外壳
```

## Key Files
- `board/Siul2_Port_Ip_Cfg.c/.h` - 88 引脚 SIUL2 初始 pinmux 配置数组;头部 YAML 注释块是 ConfigTools 工具输入,引脚名宏(如 `MCU2FMAM_RF_PWR_EN_PIN`)集中定义在 .h
- `board/Tspc_Port_Ip_Cfg.c/.h` - TSPC 配置占位:未配置任何 TSPC 寄存器,仅为维持工具再生结构
- `inc/PlatformTypes.h` - NXP RTD AUTOSAR 平台类型(uint8/sint32/boolean/float32 等;CPU_TYPE 固定 32 位);AUTOSAR 一致性要求禁止扩展此文件
- `inc/PubilcMarcoDefine.h` - 饱和自增/自减宏(`INC_PARA_*`/`DEC_PARA`)与浮点比较宏(`FLT_EQU` 等);文件名拼写就是 "Pubilc",被 App_Cluster 大量包含
- `inc/catarc_27func_api.h` / `inc/catarc_crypto_api.h` - catarc 安全算法库接口声明(`catarc_27func_verify`/`export_aes_key`);实现为预编译库,仓库内无源码(27func 在 `Libs/libsec_27func_IHU.a`)
- `inc/prj_config.h` - `__STBY_RAM` 宏定义处之一(空定义,见 Gotchas)
- `src/main.c` - FreeRTOS 静态内存:idle/timer task 的 TCB+栈、`ucHeap`(放入 `.dtcm_data_heap` 段);`main()` 仅调用 `Mcu_AppsStart()`(实现于 CVI_McuPlatform)

## Gotchas
- `board/` 两个 .c 头部 `/* TEXT BELOW IS USED AS SETTING FOR TOOLS */` YAML 块对应仓库根 `FreeRTOS_S32K312.mex`:手改 .c/.h 会在 ConfigTools 重新生成时被覆盖;改引脚要改 .mex 后重新生成
- RTD 版本混搭:`inc/PlatformTypes.h` 为 RTD 1.0.0(ASR 4.4, D2110),`board/*.h` 为 RTD 4.0.0(ASR 4.7, D2311);各自的版本检查宏只校验同前缀配对文件,不跨目录
- `__STBY_RAM` 定义冲突:`L6_Public/Public_TypeDef/Public_DrvTypes.h` 与 HSE `General.h` 在 `#ifndef` 下定义为 `__attribute__((section(".my_stanby_ram")))`(链接脚本 `.standby_sram_data`,上限 0x20407FFF),而 `inc/prj_config.h` 定义为空——若先包含 prj_config.h,待机保持属性会静默失效(当前无文件包含 prj_config.h)
- 待机保持数据的新增规则(Fuel_Mode.c 等处注释):不得直接 `__STBY_RAM 类型 x;` 新变量,应往 `StandbyRamData` 结构体加成员(见 `L4_Services/Service_Board`)
- 引脚运行时切换的备用 pinmux(如 `g_pin_mux_InitConfigArr_McuSocSpiResetToIO`、CAN0 Rx 的 GPIO/CAN 模式切换)不在 board/,在 `L5_EcuAL/EcuAL_Port/EcuAL_PortLowInf.c`
- catarc 接口签名不可单边修改:实现在外部预编译库,改声明需同步库版本,否则链接失败
