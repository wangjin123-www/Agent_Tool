/*************************************************************************************************
 * @file    Proto_Enums.h
 * @brief   7255 MCU&SOC 协议参数枚举（由 proto-toolkit 从协议表生成，禁止手改）
 * @copyright Copyright (c) 2026, cviauto.com. All rights reserved.
 *
 * 源: 7255 MCU&SOC 通信协议表 rev.1270
 ************************************************************************************************/
#ifndef PROTO_PROTO_ENUMS_H
#define PROTO_PROTO_ENUMS_H

#include <stdint.h>

/* ===== MPU_REQ_DATA_SYNC ===== */
typedef enum
{
    REQUEST = 0x00,     /* 请求 */
    NO_REQUEST = 0x01,     /* 无请求 */
}Proto_MPU_REQ_DATA_SYNC;

/* ===== RESET_TYPE ===== */
typedef enum
{
    RESET_MPU = 0x00,     /* 复位 MPU */
    RESET_MCU = 0x01,     /* 复位 MCU */
    RESET_TOUCH_KEY = 0x02,     /* 复位 TOUCH KEY */
    RESET_FACTORY = 0x03,     /* 恢复出厂设置复位 */
}Proto_RESET_TYPE;

/* ===== HEARTBEAT_SET ===== */
typedef enum
{
    HB_SET_COMM_ON = 0x00,     /* 开启 Comm UART 心跳功能 */
    HB_SET_COMM_OFF = 0x01,     /* 关闭 Comm UART 心跳功能 */
    HB_SET_FAST_ON = 0x02,     /* 开启 Fast UART 心跳功能 */
    HB_SET_FAST_OFF = 0x03,     /* 关闭 Fast UART 心跳功能 */
}Proto_HEARTBEAT_SET;

/* ===== HEARTBEAT_STATE ===== */
typedef enum
{
    HEARTBEAT_OK = 0x00,     /* 正常 */
    HEARTBEAT_TIMEOUT = 0x01,     /* 接收 MCU 心跳反馈超时 10 秒 */
}Proto_HEARTBEAT_STATE;

/* ===== POWER_MGMT_REQ ===== */
typedef enum
{
    PWR_PREPARE_SLEEP_READY = 0x00,     /* 准备休眠就绪 */
    PWR_EXIT_DELAY_WORK = 0x01,     /* 退出延时工作 */
    PWR_BATT_TOO_HIGH_READY = 0x02,     /* 电池电压过高就绪 */
    PWR_BATT_TOO_LOW_READY = 0x03,     /* 电池电压过低就绪 */
    PWR_ENTRY_STANDBY = 0x04,     /* 进入待机 */
    PWR_EXIT_STANDBY = 0x05,     /* 退出待机 */
    PWR_ENTRY_CLOCK_MODE = 0x06,     /* 进入时钟模式 */
    PWR_EXIT_CLOCK_MODE = 0x07,     /* 退出时钟模式 */
    PWR_ENTRY_HALF_RUN = 0x08,     /* 进入半运行（预留） */
    PWR_EXIT_HALF_RUN = 0x09,     /* 退出半运行 */
    PWR_REQ_INVALID = 0xFF,     /* 无效值 */
}Proto_POWER_MGMT_REQ;

/* ===== STR_STATE ===== */
typedef enum
{
    STR_NOT_IN_STR = 0x00,     /* 不处于 STR 状态 */
    STR_PREPARE_ENTRY = 0x01,     /* 准备进入 STR 状态 */
}Proto_STR_STATE;

/* ===== STR_DEBUG ===== */
typedef enum
{
    STR_DEBUG_OFF = 0x00,     /* 关闭 */
    STR_DEBUG_1MIN = 0x01,     /* 1 分钟 */
    STR_DEBUG_5MIN = 0x02,     /* 5 分钟 */
    STR_DEBUG_30MIN = 0x03,     /* 30 分钟 */
}Proto_STR_DEBUG;

/* ===== IC_POWER_STATE ===== */
typedef enum
{
    IC_PWR_INIT = 0x00,     /* INIT 初始（上电） */
    IC_PWR_RUN = 0x01,     /* RUN 运行（KL15 ON） */
    IC_PWR_STANDBY1 = 0x02,     /* STANDBY1 待机模式1（ACC OFF 10 分钟且无报警、无设防） */
    IC_PWR_STANDBY2 = 0x03,     /* STANDBY2 待机模式2（ACC ON 但未完全进入 RUN，或报警/门等特殊场景后恢复） */
    IC_PWR_STANDBY3 = 0x04,     /* STANDBY3 待机模式3（KL15 OFF，但带部分显示/控制） */
    IC_PWR_STANDBY4 = 0x05,     /* STANDBY4 待机模式4（有报警信息） */
    IC_PWR_STR = 0x06,     /* STR 系统休眠（等待网络信号 MCU 触发唤醒） */
    IC_PWR_STR_PREPARE = 0x07,     /* STR_PREPARE 休眠准备 */
    IC_PWR_STR_ENTER = 0x08,     /* STR_ENTER 进入中 */
    IC_PWR_STR_FAILED = 0x09,     /* STR_FAILED 休眠失败 */
    IC_PWR_REMOTE_CTRL = 0x0A,     /* REMOTE_CTRL 远程控制模式 */
    IC_PWR_UPDATE = 0x0B,     /* UPDATE 软件升级中 */
}Proto_IC_POWER_STATE;

/* ===== HEARTBEAT_STATUS ===== */
typedef enum
{
    HB_STS_COMM_ON = 0x00,     /* 开启 Comm UART 心跳功能 */
    HB_STS_COMM_OFF = 0x01,     /* 关闭 Comm UART 心跳功能 */
    HB_STS_FAST_ON = 0x02,     /* 开启 Fast UART 心跳功能 */
    HB_STS_FAST_OFF = 0x03,     /* 关闭 Fast UART 心跳功能 */
}Proto_HEARTBEAT_STATUS;

/* ===== POWER_MGMT_STATUS ===== */
typedef enum
{
    PWR_ST_UNKNOWN = 0x00,     /* 未知 */
    PWR_ST_HALF_RUN = 0x01,     /* 半运行 */
    PWR_ST_RUNNING = 0x02,     /* 运行中 */
    PWR_ST_EXTEND_RUN = 0x03,     /* 延长运行 */
    PWR_ST_STANDBY = 0x04,     /* 待机 */
    PWR_ST_PRE_SLEEP = 0x05,     /* 休眠前 */
    PWR_ST_SLEEP = 0x06,     /* 休眠 */
    PWR_ST_DEEP_SLEEP = 0x07,     /* 深度休眠 */
    PWR_ST_BATT_HIGH = 0x08,     /* 电池电压高 */
    PWR_ST_BATT_LOW = 0x09,     /* 电池电压低 */
    PWR_ST_STR = 0x0A,     /* STR */
}Proto_POWER_MGMT_STATUS;

/* ===== ACC_STATUS ===== */
typedef enum
{
    ACC_OFF = 0x00,     /* ACC 关 */
    ACC_ON = 0x01,     /* ACC 开 */
    IGN_ON = 0x02,     /* IGN 开 */
    ACC_START = 0x03,     /* 启动 */
}Proto_ACC_STATUS;

/* ===== BATTERY_STATUS ===== */
typedef enum
{
    BATTERY_NORMAL = 0x00,     /* 正常电压 */
    BATTERY_HIGH = 0x01,     /* 高电压 */
    BATTERY_LOW = 0x02,     /* 低电压 */
    BATTERY_OVER = 0x03,     /* 超高电压 */
    BATTERY_UNDER = 0x04,     /* 超低电压 */
    BATTERY_INVALID = 0x05,     /* 无效 */
}Proto_BATTERY_STATUS;

/* ===== AUTOSAR_NM_MODE ===== */
typedef enum
{
    NM_MODE_BUS_SLEEP = 0x00,     /* 总线睡眠模式 */
    NM_MODE_PREPARE_BUS_SLEEP = 0x01,     /* 准备总线睡眠模式 */
    NM_MODE_SYNCHRONIZED = 0x02,     /* 同步模式 */
    NM_MODE_NETWORK = 0x03,     /* 网络模式 */
}Proto_AUTOSAR_NM_MODE;

/* ===== AUTOSAR_NM_STATE ===== */
typedef enum
{
    NM_STATE_UNINITIALIZED = 0x00,     /* 未初始化状态 */
    NM_STATE_BUS_SLEEP = 0x01,     /* 总线睡眠状态 */
    NM_STATE_PREPARE_BUS_SLEEP = 0x02,     /* 准备总线睡眠状态 */
    NM_STATE_READY_SLEEP = 0x03,     /* 就绪睡眠状态 */
    NM_STATE_NORMAL_OPERATION = 0x04,     /* 正常运行状态 */
    NM_STATE_REPEAT_MESSAGE = 0x05,     /* 重复消息状态 */
    NM_STATE_SYNCHRONIZED = 0x06,     /* 同步状态 */
    NM_STATE_WAIT_CHECK_ACTIVATION = 0x07,     /* 等待检查激活 */
    NM_STATE_WAIT_NETWORK_STARTUP = 0x08,     /* 等待网络启动 */
}Proto_AUTOSAR_NM_STATE;

/* ===== VEHICLE_ANTI_THEFT_STS ===== */
typedef enum
{
    ANTI_DISALARMED = 0x00,     /* 已撤防 */
    ANTI_PRE_ALARMED = 0x01,     /* 预警状态 */
    ANTI_FULL_ALARMED = 0x02,     /* 全报警状态 */
    ANTI_ALARMED = 0x03,     /* 报警状态 */
}Proto_VEHICLE_ANTI_THEFT_STS;

/* ===== REMOTE_CTRL_ST ===== */
typedef enum
{
    REMOTE_CTRL_NONE = 0x00,     /* 非远程控制模式 */
    REMOTE_CTRL_ACTIVE = 0x01,     /* 远程控制模式 */
}Proto_REMOTE_CTRL_ST;

/* ===== OTA_REQ_STS ===== */
typedef enum
{
    OTA_REQ_NONE = 0x00,     /* 无升级（预留） */
    OTA_REQ_FLAG_SAVED = 0x01,     /* 升级请求（MCU 收到后存储升级标志位） */
    OTA_REQ_START = 0x02,     /* 升级开始 */
    OTA_REQ_DONE_REBOOT = 0x03,     /* 升级完成，请求重启 */
    OTA_REQ_CANCEL = 0x04,     /* 取消升级（SOC 主动中止升级） */
}Proto_OTA_REQ_STS;

/* ===== OTA_UPGRADE_STS ===== */
typedef enum
{
    OTA_STS_NONE = 0x00,     /* 无升级 */
    OTA_STS_FLAG_SAVED = 0x01,     /* 升级标志位已存储，准备重启进入升级 */
    OTA_STS_READY = 0x02,     /* 升级就绪 */
    OTA_STS_COND_UNSAT = 0x03,     /* 当前条件不满足升级条件，退出升级 */
    OTA_STS_FILE_DONE = 0x04,     /* 当前文件校验结束，申请切换分区进行升级 */
    OTA_STS_REQ_TIMEOUT = 0x05,     /* 数据请求次数超时，退出升级 */
    OTA_STS_ERASE_FAIL = 0x06,     /* MCU 擦除 flash 失败，退出升级 */
    OTA_STS_WRITE_FAIL = 0x07,     /* MCU 写 flash 失败，退出升级 */
    OTA_STS_SIGN_FAIL = 0x08,     /* 签名校验失败，退出升级 */
    OTA_STS_HASH_FAIL = 0x09,     /* 升级文件 hash 校验失败，退出升级 */
    OTA_STS_CANCEL = 0x0A,     /* 收到 SOC 取消升级请求，已中断升级 */
}Proto_OTA_UPGRADE_STS;

/* ===== POWER_REQ_CMD ===== */
typedef enum
{
    PWR_REQ_STR = 0x00,     /* 请求 STR */
    PWR_REQ_SHUTDOWN = 0x01,     /* 请求关机 */
    PWR_REQ_RESTART = 0x02,     /* 请求重启 */
}Proto_POWER_REQ_CMD;

/* ===== TEMPERATURE_STATUS ===== */
typedef enum
{
    TEMP_UNDER = 0x00,     /* 超低温 */
    TEMP_LOW = 0x01,     /* 低温 */
    TEMP_NORMAL = 0x02,     /* 正常 */
    TEMP_HIGH = 0x03,     /* 高温 */
    TEMP_OVER = 0x04,     /* 超高温 */
}Proto_TEMPERATURE_STATUS;

/* ===== VOLTAGE_STATUS ===== */
typedef enum
{
    VOLTAGE_UNDER = 0x00,     /* 超低压 */
    VOLTAGE_LOW = 0x01,     /* 低压 */
    VOLTAGE_NORMAL = 0x02,     /* 正常 */
    VOLTAGE_HIGH = 0x03,     /* 高压 */
    VOLTAGE_OVER = 0x04,     /* 超高压 */
    VOLTAGE_DISCONNECT = 0x05,     /* 断开 */
}Proto_VOLTAGE_STATUS;

/* ===== RESTART_TYPE ===== */
typedef enum
{
    RESTART_POWER_ON = 0x00,     /* power on reset */
    RESTART_WAKE_UP = 0x01,     /* wake up */
}Proto_RESTART_TYPE;

#endif /* PROTO_PROTO_ENUMS_H */
/*************************************************************************************************
 * End of File
 ************************************************************************************************/
