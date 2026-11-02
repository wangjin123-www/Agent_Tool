# FreeRTOS_S32K312 — CVI 车载仪表主控 MCU 固件(NXP S32K312 + FreeRTOS V10.6.0,以 S32DS Eclipse 工程整体构建)

## Commands
| 命令 | 说明 |
|------|------|
| S32DS 构建 | 仓库无 Makefile/CMake;导入 `.project`/`.cproject` 到 S32 Design Studio 整体编译(arm-none-eabi-gcc),无独立脚本 |
| `cd Project_Settings/mcu_signature_YB103 && sh signature.sh` | 固件签名流水线:mcu_s.bin → boot/sw 双签名 → hse_app_signed.bin;必须在该目录内执行(依赖相对路径 pem/bin) |
| `py make_header_file.py -type MCU -file hse_app.bin -VID 1 -ver <版本串> -out hse_app_header -offset 1024` | 生成 68 字节 CVIA 头(含 SHA-256);signature.sh 内部即用此命令,同样须在 mcu_signature_YB103/ 内执行 |
| S32 Configuration Tools | 引脚配置经仓库根 `FreeRTOS_S32K312.mex` 导入后重新生成 board/(无命令行构建入口) |

## Architecture(上层依赖下层:L1→L4→L5→RTD/HSE,跨层调用只经 UpInf/LowInf 函数指针接口)
- `CVI_McuPlatform/` — 平台核心 + L6 公共层:Proj_Cfg.h 车型总开关、全局公共类型与调度配置(详见 CVI_McuPlatform/CLAUDE.md)
- `CVI_McuPlatform/L1_Applications/` — 应用层:仪表显示/CAN/LIN/UDS 诊断/按键/电源/SOC 串口,入口 AppsStart.c(详见 CVI_McuPlatform/L1_Applications/CLAUDE.md)
- `CVI_McuPlatform/L2_Tasks/` — 任务层:7 个任务"四件套"框架(Task_X),把应用挂上调度器(详见 CVI_McuPlatform/L2_Tasks/CLAUDE.md)
- `CVI_McuPlatform/L3_RTOS/` — OS 层:FreeRTOS V10.6.0 内核 + Os1/Os2 自研包装,双调度器可切换(详见 CVI_McuPlatform/L3_RTOS/CLAUDE.md)
- `CVI_McuPlatform/L4_Services/` — 服务层:CAN 交互/AUTOSAR NM/UDS 栈/电源 HSM/EEPROM/SoC 通信(详见 CVI_McuPlatform/L4_Services/CLAUDE.md)
- `CVI_McuPlatform/L5_EcuAL/` — MCU 抽象层:把 RTD IP 驱动封装成统一 EcuAL_* 三表接口(详见 CVI_McuPlatform/L5_EcuAL/CLAUDE.md)
- `RTD/include/` — NXP RTD 4.0.0 IP 驱动头文件库(原厂交付,禁止手改)(详见 RTD/include/CLAUDE.md)
- `RTD/src/` — NXP RTD 4.0.0 IP 驱动实现(原厂交付,禁止手改)(详见 RTD/src/CLAUDE.md)
- `generate/` — RTD/tresos 生成的外设配置层(*_Cfg.h/c、FreeRTOSConfig.h,含手改)(详见 generate/CLAUDE.md)
- `HSE/` — HSE 硬件安全引擎 Host 驱动与安全安装器(MU 通道对接 HSE 固件 v2.40.0)(详见 HSE/CLAUDE.md)
- `inc/` + `board/` + `src/` — 全局公共头、ConfigTools 引脚配置(.mex 产物)、main() 入口(详见 inc/CLAUDE.md)
- `Project_Settings/` — Startup_Code 启动代码/向量表/异常实现(随主工程编译进镜像)+ mcu_signature_YB103 离线签名流水线(不参与编译)(详见 Project_Settings/CLAUDE.md)

## Gotchas
- 编译 include 路径必须同时覆盖 RTD/include/、generate/include/、board/ 三处;Std_Types.h 等全仓唯一副本在 `CVI_McuPlatform/L4_Services/Service_Canbus/Service_CanAsrNm/Can_AsrNM/`,新建编译目标最易漏配
- 跨层 include 全用反斜杠相对路径(仅 Windows 工具链可编译);移动/重命名目录会静默断链,挪文件需同步 `.cproject`
- 车型只经 `CVI_McuPlatform/L6_Public/Public_TypeDef/Proj_Cfg.h` 三宏切换;WB101 固件油/混共用一个镜像,FUEL/HYBRID 由 EOL 运行时决定,改动必须两条分支都验证
- generate/ 与 board/ 是随仓提交且被手工改过的生成代码,重新生成会覆盖手改——改配置前先 git log 确认;RTD/ 升级必须整包替换 include+src(文件头版本一致性校验宏禁止混搭)
- `generate/include/FreeRTOSConfig.h` 的 configCPU_CLOCK_HZ(120MHz) 必须与 generate/src/Clock_Ip_Cfg.c 的 CORE_CLK 一致,否则 tick 漂移;tick=1ms,服务层超时常量按 毫秒/5 折算
- HSE 服务描述符放在 DTCM 链接段 ._HseSrvDesc,链接脚本必须保留该段;烧写镜像须为 Project_Settings 签名输出 hse_app_signed.bin,勿直接烧 mcu_s.bin
- 向量表启动后运行于 RAM(由 init_table 拷入):新增中断要同步 RAM 表/IntCtrl 配置,只改 `Project_Settings/Startup_Code/Vector_Table.s` 不一定生效
- 源文件编码混杂(GBK/UTF-8 共存),编辑前先确认编码;休眠保持变量必须加进 StandbyRamData 结构体,禁止直接 __STBY_RAM 声明新变量
- 公共类型收敛到 L6_Public 并经 `CVI_McuPlatform/L6_Public/Public_TypeDef/Proj_Includes.h` 引出;发布前手工更新版本串 WB101_MCU_VERSION
- catarc 安全算法实现是外部预编译库 `Libs/libsec_27func_IHU.a`,接口签名不可单边修改(同步库版本否则链接失败)
