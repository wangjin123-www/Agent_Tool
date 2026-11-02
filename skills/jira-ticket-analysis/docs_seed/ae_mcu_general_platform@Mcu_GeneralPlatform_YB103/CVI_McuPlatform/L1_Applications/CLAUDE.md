# L1_Applications —— 应用层(仪表业务实现:电源/CAN/LIN/诊断/仪表显示/SOC 串口通信)

由 L2_Tasks 创建任务并按周期调度;向下经 `LowInf` 调 L5_EcuAL,经 `Service_*_UpInf` 调 L4_Services。

## Commands
| Command | Description |
|---------|-------------|
| (无独立构建) | 纯源码目录,随根工程一起编译(见仓库根 CLAUDE.md / Project_Settings) |

## Architecture
```
L1_Applications/
  AppsStart.c        # 应用层入口:Mcu_AppsStart() 创建 L2 任务并启动调度器;判定油/混车型
  APP_AutoTest/      # 自动化测试支持:测试 CAN 帧(0x18FFFFF1)与状态采集
  App_Can/           # CAN 报文应用:按车型 MsgPar/MsgFunc/SignalFunc + GenerateCode(DBC 生成)
  App_Candiag/       # UDS 诊断(DCM):DcmMain 调度 + DcmApp 实现 + DcmAppCfg 配置表
  App_Cluster/       # 仪表显示:各 Mode 按车型(_WB101/_WY113/_YB103)与 Platform 公共实现
  App_Hse/           # HSE 安全应用:CMAC 生成/校验、升级包签名验证与激活
  App_HwFault/       # 硬件故障检测上报(Hw_Fault、LDO 故障)
  App_Key/           # 按键:ADC 键 / CAN 键(FUNC_IVI_*_KEY_EN 裁剪)
  App_Lin/           # LIN 应用:按车型 Include + 报文处理
  App_Mem/           # 存储应用:EE 块读写(IC/DID 块号)、能耗 NVM 累计
  App_Power/         # 电源:Batt/Acc 检测 + HSM 状态机(下电/休眠/唤醒)
  App_SocCom/        # 与 SOC(MPU) 串口通信:SysCmd/IVICmd、升级转发、心跳监测
  App_SwTimer/       # 应用层软定时器(TimerID_t 启停 + CallBack 回调)
```

## Key Files
- `AppsStart.c` - `Mcu_GetCDCCarType()` 运行时判定 FUEL/HYBRID;据此条件创建 Task_Lin
- `App_Power/App_PowerHsm.c` - 电源状态机与休眠变量管理
- `App_Can/App_CAN.c` - 报文超时/无效/首帧接收状态(CanRxTimeoutTimeTab 超时表)
- `App_Candiag/CanApp_DcmMain.c` - 诊断主调度:Service_CanUdsUpInf + DcmApp
- `App_SocCom/App_SocComUpdate.c` - 升级状态机,配 `App_SocCom/App_UpdateForward.c` 转发

## 约定
- 跨层接口统一为函数指针结构体:`<App>UpInf`(向上供 L2 调度,调用前判 NULL)、`<App>LowInf`(向下调);SocCom 例外,导出名是 `App_SocComInf`
- 周期入口按 `MainFunction20ms/50ms/100ms` 命名,由 UpInf 暴露、L2 任务定时调用;新增周期函数必须挂接到对应 L2 任务

## Gotchas
- 源文件编码混杂(GBK 与 UTF-8 共存,部分文件非法 UTF-8):编辑前先确认编码,否则中文注释会损坏
- **禁止用 `__STBY_RAM` 直接声明新变量**:休眠保持变量必须加进 `StandbyRamData` 结构体成员(App_PowerHsm.c 内有注释)
- `App_Can/App_CAN_WB101/App_CAN_WB101_GenerateCode/` 等 GenerateCode 目录是 DBC 生成代码(CanTxSigGet/Set 宏),禁止手改;改 DBC 重新生成
- WB101 固件油/混共用:车型由 EOL DID CFG_CARTYPE 运行时决定,改车型逻辑必须两条分支都验证
- 功能被宏裁剪(FUNC_IC_ENABLE、FUNC_IVI_*):代码"缺失"时先查宏定义,再怀疑实现
