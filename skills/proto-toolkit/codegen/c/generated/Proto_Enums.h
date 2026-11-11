/*************************************************************************************************
 * @file    Proto_Enums.h
 * @brief   7255 MCU&SOC 协议参数枚举（由 proto-toolkit 从协议表生成，禁止手改）
 * @copyright Copyright (c) 2026, cviauto.com. All rights reserved.
 *
 * 源: 7255 MCU&SOC 通信协议（Bitable Mj3gbU3NqagG4WsPcQgc0YhSnac） rev.4.0.0
 ************************************************************************************************/
#ifndef PROTO_PROTO_ENUMS_H
#define PROTO_PROTO_ENUMS_H

#include <stdint.h>

/* ===== AccStatus_E ===== */
typedef enum
{
    AccStatus_ACC_OFF = 0x00,     /* ACC 关 */
    AccStatus_ACC_ON = 0x01,     /* ACC 开 */
    AccStatus_IGN_ON = 0x02,     /* IGN 开 */
    AccStatus_ACC_START = 0x03,     /* 启动 */
}AccStatus_E;

/* ===== AutosarNmMode_E ===== */
typedef enum
{
    AutosarNmMode_NM_MODE_BUS_SLEEP = 0x00,     /* 总线睡眠模式 */
    AutosarNmMode_NM_MODE_PREPARE_BUS_SLEEP = 0x01,     /* 准备总线睡眠模式 */
    AutosarNmMode_NM_MODE_SYNCHRONIZED = 0x02,     /* 同步模式 */
    AutosarNmMode_NM_MODE_NETWORK = 0x03,     /* 网络模式 */
}AutosarNmMode_E;

/* ===== AutosarNmState_E ===== */
typedef enum
{
    AutosarNmState_NM_STATE_UNINITIALIZED = 0x00,     /* 未初始化状态 */
    AutosarNmState_NM_STATE_BUS_SLEEP = 0x01,     /* 总线睡眠状态 */
    AutosarNmState_NM_STATE_PREPARE_BUS_SLEEP = 0x02,     /* 准备总线睡眠状态 */
    AutosarNmState_NM_STATE_READY_SLEEP = 0x03,     /* 就绪睡眠状态 */
    AutosarNmState_NM_STATE_NORMAL_OPERATION = 0x04,     /* 正常运行状态 */
    AutosarNmState_NM_STATE_REPEAT_MESSAGE = 0x05,     /* 重复消息状态 */
    AutosarNmState_NM_STATE_SYNCHRONIZED = 0x06,     /* 同步状态 */
    AutosarNmState_NM_STATE_WAIT_CHECK_ACTIVATION = 0x07,     /* 等待检查激活 */
    AutosarNmState_NM_STATE_WAIT_NETWORK_STARTUP = 0x08,     /* 等待网络启动 */
}AutosarNmState_E;

/* ===== BatteryStatus_E ===== */
typedef enum
{
    BatteryStatus_BATTERY_NORMAL = 0x00,     /* 正常电压 */
    BatteryStatus_BATTERY_HIGH = 0x01,     /* 高电压 */
    BatteryStatus_BATTERY_LOW = 0x02,     /* 低电压 */
    BatteryStatus_BATTERY_OVER = 0x03,     /* 超高电压 */
    BatteryStatus_BATTERY_UNDER = 0x04,     /* 超低电压 */
    BatteryStatus_BATTERY_INVALID = 0x05,     /* 无效 */
}BatteryStatus_E;

/* ===== HeartbeatSet_E ===== */
typedef enum
{
    HeartbeatSet_HB_SET_COMM_ON = 0x00,     /* 开启 Comm UART 心跳功能 */
    HeartbeatSet_HB_SET_COMM_OFF = 0x01,     /* 关闭 Comm UART 心跳功能 */
    HeartbeatSet_HB_SET_FAST_ON = 0x02,     /* 开启 Fast UART 心跳功能 */
    HeartbeatSet_HB_SET_FAST_OFF = 0x03,     /* 关闭 Fast UART 心跳功能 */
}HeartbeatSet_E;

/* ===== HeartbeatState_E ===== */
typedef enum
{
    HeartbeatState_HEARTBEAT_OK = 0x00,     /* 正常 */
    HeartbeatState_HEARTBEAT_TIMEOUT = 0x01,     /* 接收 MCU 心跳反馈超时 10 秒 */
}HeartbeatState_E;

/* ===== HeartbeatStatus_E ===== */
typedef enum
{
    HeartbeatStatus_HB_STS_COMM_ON = 0x00,     /* 开启 Comm UART 心跳功能 */
    HeartbeatStatus_HB_STS_COMM_OFF = 0x01,     /* 关闭 Comm UART 心跳功能 */
    HeartbeatStatus_HB_STS_FAST_ON = 0x02,     /* 开启 Fast UART 心跳功能 */
    HeartbeatStatus_HB_STS_FAST_OFF = 0x03,     /* 关闭 Fast UART 心跳功能 */
}HeartbeatStatus_E;

/* ===== IcPowerState_E ===== */
typedef enum
{
    IcPowerState_IC_PWR_INIT = 0x00,     /* INIT 初始（上电） */
    IcPowerState_IC_PWR_RUN = 0x01,     /* RUN 运行（KL15 ON） */
    IcPowerState_IC_PWR_STANDBY1 = 0x02,     /* STANDBY1 待机模式1（ACC OFF 10 分钟且无报警、无设防） */
    IcPowerState_IC_PWR_STANDBY2 = 0x03,     /* STANDBY2 待机模式2（ACC ON 但未完全进入 RUN，或报警/门等特殊场景后恢复） */
    IcPowerState_IC_PWR_STANDBY3 = 0x04,     /* STANDBY3 待机模式3（KL15 OFF，但带部分显示/控制） */
    IcPowerState_IC_PWR_STANDBY4 = 0x05,     /* STANDBY4 待机模式4（有报警信息） */
    IcPowerState_IC_PWR_STR = 0x06,     /* STR 系统休眠（等待网络信号 MCU 触发唤醒） */
    IcPowerState_IC_PWR_STR_PREPARE = 0x07,     /* STR_PREPARE 休眠准备 */
    IcPowerState_IC_PWR_STR_ENTER = 0x08,     /* STR_ENTER 进入中 */
    IcPowerState_IC_PWR_STR_FAILED = 0x09,     /* STR_FAILED 休眠失败 */
    IcPowerState_IC_PWR_REMOTE_CTRL = 0x0A,     /* REMOTE_CTRL 远程控制模式 */
    IcPowerState_IC_PWR_UPDATE = 0x0B,     /* UPDATE 软件升级中 */
}IcPowerState_E;

/* ===== MpuReqDataSync_E ===== */
typedef enum
{
    MpuReqDataSync_REQUEST = 0x00,     /* 请求 */
    MpuReqDataSync_NO_REQUEST = 0x01,     /* 无请求 */
}MpuReqDataSync_E;

/* ===== OtaReqSts_E ===== */
typedef enum
{
    OtaReqSts_OTA_REQ_NONE = 0x00,     /* 无升级（预留） */
    OtaReqSts_OTA_REQ_FLAG_SAVED = 0x01,     /* 升级请求（MCU 收到后存储升级标志位） */
    OtaReqSts_OTA_REQ_START = 0x02,     /* 升级开始 */
    OtaReqSts_OTA_REQ_DONE_REBOOT = 0x03,     /* 升级完成，请求重启 */
    OtaReqSts_OTA_REQ_CANCEL = 0x04,     /* 取消升级（SOC 主动中止升级） */
}OtaReqSts_E;

/* ===== OtaUpgradeSts_E ===== */
typedef enum
{
    OtaUpgradeSts_OTA_STS_NONE = 0x00,     /* 无升级 */
    OtaUpgradeSts_OTA_STS_FLAG_SAVED = 0x01,     /* 升级标志位已存储，准备重启进入升级 */
    OtaUpgradeSts_OTA_STS_READY = 0x02,     /* 升级就绪 */
    OtaUpgradeSts_OTA_STS_COND_UNSAT = 0x03,     /* 当前条件不满足升级条件，退出升级 */
    OtaUpgradeSts_OTA_STS_FILE_DONE = 0x04,     /* 当前文件校验结束，申请切换分区进行升级 */
    OtaUpgradeSts_OTA_STS_REQ_TIMEOUT = 0x05,     /* 数据请求次数超时，退出升级 */
    OtaUpgradeSts_OTA_STS_ERASE_FAIL = 0x06,     /* MCU 擦除 flash 失败，退出升级 */
    OtaUpgradeSts_OTA_STS_WRITE_FAIL = 0x07,     /* MCU 写 flash 失败，退出升级 */
    OtaUpgradeSts_OTA_STS_SIGN_FAIL = 0x08,     /* 签名校验失败，退出升级 */
    OtaUpgradeSts_OTA_STS_HASH_FAIL = 0x09,     /* 升级文件 hash 校验失败，退出升级 */
    OtaUpgradeSts_OTA_STS_CANCEL = 0x0A,     /* 收到 SOC 取消升级请求，已中断升级 */
}OtaUpgradeSts_E;

/* ===== PowerMgmtReq_E ===== */
typedef enum
{
    PowerMgmtReq_PWR_PREPARE_SLEEP_READY = 0x00,     /* 准备休眠就绪 */
    PowerMgmtReq_PWR_EXIT_DELAY_WORK = 0x01,     /* 退出延时工作 */
    PowerMgmtReq_PWR_BATT_TOO_HIGH_READY = 0x02,     /* 电池电压过高就绪 */
    PowerMgmtReq_PWR_BATT_TOO_LOW_READY = 0x03,     /* 电池电压过低就绪 */
    PowerMgmtReq_PWR_ENTRY_STANDBY = 0x04,     /* 进入待机 */
    PowerMgmtReq_PWR_EXIT_STANDBY = 0x05,     /* 退出待机 */
    PowerMgmtReq_PWR_ENTRY_CLOCK_MODE = 0x06,     /* 进入时钟模式 */
    PowerMgmtReq_PWR_EXIT_CLOCK_MODE = 0x07,     /* 退出时钟模式 */
    PowerMgmtReq_PWR_ENTRY_HALF_RUN = 0x08,     /* 进入半运行（预留） */
    PowerMgmtReq_PWR_EXIT_HALF_RUN = 0x09,     /* 退出半运行 */
    PowerMgmtReq_PWR_REQ_INVALID = 0xFF,     /* 无效值 */
}PowerMgmtReq_E;

/* ===== PowerMgmtStatus_E ===== */
typedef enum
{
    PowerMgmtStatus_PWR_ST_UNKNOWN = 0x00,     /* 未知 */
    PowerMgmtStatus_PWR_ST_HALF_RUN = 0x01,     /* 半运行 */
    PowerMgmtStatus_PWR_ST_RUNNING = 0x02,     /* 运行中 */
    PowerMgmtStatus_PWR_ST_EXTEND_RUN = 0x03,     /* 延长运行 */
    PowerMgmtStatus_PWR_ST_STANDBY = 0x04,     /* 待机 */
    PowerMgmtStatus_PWR_ST_PRE_SLEEP = 0x05,     /* 休眠前 */
    PowerMgmtStatus_PWR_ST_SLEEP = 0x06,     /* 休眠 */
    PowerMgmtStatus_PWR_ST_DEEP_SLEEP = 0x07,     /* 深度休眠 */
    PowerMgmtStatus_PWR_ST_BATT_HIGH = 0x08,     /* 电池电压高 */
    PowerMgmtStatus_PWR_ST_BATT_LOW = 0x09,     /* 电池电压低 */
    PowerMgmtStatus_PWR_ST_STR = 0x0A,     /* STR */
}PowerMgmtStatus_E;

/* ===== PowerReqCmd_E ===== */
typedef enum
{
    PowerReqCmd_PWR_REQ_STR = 0x00,     /* 请求 STR */
    PowerReqCmd_PWR_REQ_SHUTDOWN = 0x01,     /* 请求关机 */
    PowerReqCmd_PWR_REQ_RESTART = 0x02,     /* 请求重启 */
}PowerReqCmd_E;

/* ===== RemoteCtrlSt_E ===== */
typedef enum
{
    RemoteCtrlSt_REMOTE_CTRL_NONE = 0x00,     /* 非远程控制模式 */
    RemoteCtrlSt_REMOTE_CTRL_ACTIVE = 0x01,     /* 远程控制模式 */
}RemoteCtrlSt_E;

/* ===== ResetType_E ===== */
typedef enum
{
    ResetType_RESET_MPU = 0x00,     /* 复位 MPU */
    ResetType_RESET_MCU = 0x01,     /* 复位 MCU */
    ResetType_RESET_TOUCH_KEY = 0x02,     /* 复位 TOUCH KEY */
    ResetType_RESET_FACTORY = 0x03,     /* 恢复出厂设置复位 */
}ResetType_E;

/* ===== RestartType_E ===== */
typedef enum
{
    RestartType_RESTART_POWER_ON = 0x00,     /* power on reset */
    RestartType_RESTART_WAKE_UP = 0x01,     /* wake up */
}RestartType_E;

/* ===== StrDebug_E ===== */
typedef enum
{
    StrDebug_STR_DEBUG_OFF = 0x00,     /* 关闭 */
    StrDebug_STR_DEBUG_1MIN = 0x01,     /* 1 分钟 */
    StrDebug_STR_DEBUG_5MIN = 0x02,     /* 5 分钟 */
    StrDebug_STR_DEBUG_30MIN = 0x03,     /* 30 分钟 */
}StrDebug_E;

/* ===== StrState_E ===== */
typedef enum
{
    StrState_STR_NOT_IN_STR = 0x00,     /* 不处于 STR 状态 */
    StrState_STR_PREPARE_ENTRY = 0x01,     /* 准备进入 STR 状态 */
}StrState_E;

/* ===== TemperatureStatus_E ===== */
typedef enum
{
    TemperatureStatus_TEMP_UNDER = 0x00,     /* 超低温 */
    TemperatureStatus_TEMP_LOW = 0x01,     /* 低温 */
    TemperatureStatus_TEMP_NORMAL = 0x02,     /* 正常 */
    TemperatureStatus_TEMP_HIGH = 0x03,     /* 高温 */
    TemperatureStatus_TEMP_OVER = 0x04,     /* 超高温 */
}TemperatureStatus_E;

/* ===== VehicleAntiTheftSts_E ===== */
typedef enum
{
    VehicleAntiTheftSts_ANTI_DISALARMED = 0x00,     /* 已撤防 */
    VehicleAntiTheftSts_ANTI_PRE_ALARMED = 0x01,     /* 预警状态 */
    VehicleAntiTheftSts_ANTI_FULL_ALARMED = 0x02,     /* 全报警状态 */
    VehicleAntiTheftSts_ANTI_ALARMED = 0x03,     /* 报警状态 */
}VehicleAntiTheftSts_E;

/* ===== VersionModule_E ===== */
typedef enum
{
    VersionModule_VER_MOD_DVR = 0x01,     /* DVR 版本 */
    VersionModule_VER_MOD_RADAR = 0x02,     /* RADAR 版本（示例帧实证 0x02） */
    VersionModule_VER_MOD_HW = 0x03,     /* HW 版本 */
    VersionModule_VER_MOD_DIAG_SW = 0x04,     /* 诊断 SW 版本 */
    VersionModule_VER_MOD_MCU = 0x05,     /* MCU 软件版本 */
}VersionModule_E;

/* ===== VoltageStatus_E ===== */
typedef enum
{
    VoltageStatus_VOLTAGE_UNDER = 0x00,     /* 超低压 */
    VoltageStatus_VOLTAGE_LOW = 0x01,     /* 低压 */
    VoltageStatus_VOLTAGE_NORMAL = 0x02,     /* 正常 */
    VoltageStatus_VOLTAGE_HIGH = 0x03,     /* 高压 */
    VoltageStatus_VOLTAGE_OVER = 0x04,     /* 超高压 */
    VoltageStatus_VOLTAGE_DISCONNECT = 0x05,     /* 断开 */
}VoltageStatus_E;

#endif /* PROTO_PROTO_ENUMS_H */
/*************************************************************************************************
 * End of File
 ************************************************************************************************/
