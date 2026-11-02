# L4_Services(平台服务层:板级电源/IO 管理与通信协议服务,上承 L1/L2,下接 L5_EcuAL 硬件抽象)

## Architecture
```
L4_Services/
  Service_Board/    # 引脚索引宏(PIN_IDX_*)/ADC 通道映射/上下电时序/SOC 复位与供电/待机保持 RAM
  Service_Canbus/
    Service_CanComm/   # CAN 交互层:il 配置表驱动收发、周期/事件消息、BusOff 统计;ccl tick
    Service_CanAsrNm/  # 网络管理:AUTOSAR 风格 CanNm/Nm 栈(Can_AsrNM,Lcfg/PBcfg 分离)
    Service_CanUds/    # 诊断:自研轻量 UDS 栈 DcmSrv(固定 15 服务表)+ Adapter 适配
  Service_Power/    # HSM 电源状态机(RESET/RUN/STANDBY/SLEEP 等 10 态)+ 事件路由 PowerEvRouter
  Service_SocComm/  # MCU↔SoC 通信:CommTp 传输层(SF/FF/CF 分段重组)+ PduR 路由 + 握手机制
  Service_LinComm/  # LIN master:调度表驱动(p_LinCfgTable)
  Service_Memory/   # EEPROM 块同步读写 + PFlash 扇区擦写
  Service_Key/      # ADC 按键(采样阈值判键,3 组×5 键)
  Service_Debug/    # xprintf 调试打印
```

## Interface Convention
- 每个服务三件套:`Service_X.c/h`(业务)+ `Service_XLowInf.c/h`(下行走 L5:调 `EcuAL_*_UpInf` 函数指针结构,ISR 回调经 Init 参数结构注册,如 `sCanEcuALInitParams`)+ `Service_XUpInf.c/h`(上行走 L1/L2:`STRUCT_SERVICE_*_UPINF` 函数指针结构)
- 部分服务用 impl 注入:`Service_Power_Impl`、`Service_Key_Impl`(Init/Deinit/MainFunction 函数指针,由实现方注册)
- 功能开关宏:`SERVICE_CANCOMM_LOWINF_EN` / `SERVICE_CAN_ASRNM_LOWINF_EN` / `FUNC_IVI_ADC_KEY_EN` 等控制整块功能
- RX 分发:Service_CanComm 的 CAN ISR 回调按 CanId extern 直呼 `Service_AsrNmLowInf_CanRecvMsg` / `Service_CanUds_RxMsg`(编译期符号耦合,非函数指针)

## Key Files
- `Service_Board.h` - 全板引脚索引宏与 ADC 通道映射的唯一权威来源
- `Service_Canbus/Service_CanComm/Service_CanComm_il.h` - CAN 报文配置表(ilTxTable/ilRxTable),新增报文在此定义
- `Service_Canbus/Service_CanUds/CanSrv_UdsStack/DcmSrv_Api.h` - UDS 栈入口(Api_DcmSrv_Init/FrameHandle、会话与安全访问)
- `Service_Power/Service_PowerEventRouter.h` - 电源 HSM 事件表(HSM_PWR_SSD_*_TABLE)
- `Service_SocComm/Service_CommTp.h` - SoC 传输层(SF/FF/CF PCI、队列与 SN 重组)

## Gotchas
- 板型宏 `PROJECT_WEIQIAO_YB103` / `WY113` / `WB101` 决定差异:SocComm 通道数 2 vs 3(见 `Service_SocComm_PduR_Cfg.h`);Service_Board.h 中 WB101 引脚复用(如 `PIN_IDX_PWR_EN_AMBIENT` 与 `PIN_IDX_MCU2SEATBELT_B1_DET` 同为 PORTB18),改引脚前先搜同值宏
- 全部上/下行接口是函数指针结构:调用前必须完成对应 Init 注册,否则 NULL 解引用;开关宏关闭时调用被静默吞掉(仅返回 FALSE)
- 定时以 5ms 为 tick:如 `CANNME_FORCE_RELEASE_TIMEOUT (720000/5)`,新超时常量按 毫秒/5 折算
- include 大量使用反斜杠相对路径(`..\..\L5_EcuAL\...`、`.\Can_AsrNm\...`),移动文件必断,且仅 Windows 工具链可编译
- `StandbyRamData`(`__STBY_RAM` 保留段,Service_Board.h)跨睡眠保持,增删字段会改变布局,必须同步预留字段
- 新增 CAN 报文:改 Service_CanComm_il.c 的 ilTxTable/ilRxTable 配置表与状态缓冲,勿绕过 Service_CanComm 直接调 EcuAL 发送;UDS 服务表 `CAN_DCMSRV_Group` 固定 15 项,扩项需同步表定义
