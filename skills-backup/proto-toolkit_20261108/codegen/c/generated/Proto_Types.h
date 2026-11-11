/*************************************************************************************************
 * @file    Proto_Types.h
 * @brief   7255 MCU&SOC 协议数据结构（由 proto-toolkit 从协议表生成，禁止手改）
 * @copyright Copyright (c) 2026, cviauto.com. All rights reserved.
 *
 * 源: 7255 MCU&SOC 通信协议表 rev.1270
 * 约定: 大端（BYTE0 先发，字节内 bit7 先发）；bit 成员不使用 C 位域，
 *       通过 Proto_<Struct>_Get/Set<X>() 掩码访问，保证跨编译器一致。
 ************************************************************************************************/
#ifndef PROTO_PROTO_TYPES_H
#define PROTO_PROTO_TYPES_H

#include <stdint.h>

/* ===== DateTime · SysSrv · 时间同步（0x0D 0x01/0x02、0x8D 0x02） · Size=6 ===== */
/* 位域结构：按字节原样存储，成员经访问器读写 */
typedef struct
{
    uint8_t Data[6u];
}Proto_DateTime;

/* year: DateTime byte 0B bit 0-7bit (mask 0xFF) - 年 */
#define Proto_DateTime_year_MASK       (0xFFu)
#define Proto_DateTime_year_SHIFT      (0u)
static inline uint8_t Proto_DateTime_Getyear(const Proto_DateTime *p)
{
    return (uint8_t)((p->Data[0u] & Proto_DateTime_year_MASK)
                     >> Proto_DateTime_year_SHIFT);
}
static inline void Proto_DateTime_Setyear(Proto_DateTime *p, uint8_t v)
{
    p->Data[0u] = (uint8_t)((p->Data[0u]
                                              & (uint8_t)(~Proto_DateTime_year_MASK))
                                             | (uint8_t)((v << Proto_DateTime_year_SHIFT)
                                                         & Proto_DateTime_year_MASK));
}
/* month: DateTime byte 1B bit 0-7bit (mask 0xFF) - 月 */
#define Proto_DateTime_month_MASK       (0xFFu)
#define Proto_DateTime_month_SHIFT      (0u)
static inline uint8_t Proto_DateTime_Getmonth(const Proto_DateTime *p)
{
    return (uint8_t)((p->Data[1u] & Proto_DateTime_month_MASK)
                     >> Proto_DateTime_month_SHIFT);
}
static inline void Proto_DateTime_Setmonth(Proto_DateTime *p, uint8_t v)
{
    p->Data[1u] = (uint8_t)((p->Data[1u]
                                              & (uint8_t)(~Proto_DateTime_month_MASK))
                                             | (uint8_t)((v << Proto_DateTime_month_SHIFT)
                                                         & Proto_DateTime_month_MASK));
}
/* day: DateTime byte 2B bit 0-7bit (mask 0xFF) - 日 */
#define Proto_DateTime_day_MASK       (0xFFu)
#define Proto_DateTime_day_SHIFT      (0u)
static inline uint8_t Proto_DateTime_Getday(const Proto_DateTime *p)
{
    return (uint8_t)((p->Data[2u] & Proto_DateTime_day_MASK)
                     >> Proto_DateTime_day_SHIFT);
}
static inline void Proto_DateTime_Setday(Proto_DateTime *p, uint8_t v)
{
    p->Data[2u] = (uint8_t)((p->Data[2u]
                                              & (uint8_t)(~Proto_DateTime_day_MASK))
                                             | (uint8_t)((v << Proto_DateTime_day_SHIFT)
                                                         & Proto_DateTime_day_MASK));
}
/* hour: DateTime byte 3B bit 0-7bit (mask 0xFF) - 时 */
#define Proto_DateTime_hour_MASK       (0xFFu)
#define Proto_DateTime_hour_SHIFT      (0u)
static inline uint8_t Proto_DateTime_Gethour(const Proto_DateTime *p)
{
    return (uint8_t)((p->Data[3u] & Proto_DateTime_hour_MASK)
                     >> Proto_DateTime_hour_SHIFT);
}
static inline void Proto_DateTime_Sethour(Proto_DateTime *p, uint8_t v)
{
    p->Data[3u] = (uint8_t)((p->Data[3u]
                                              & (uint8_t)(~Proto_DateTime_hour_MASK))
                                             | (uint8_t)((v << Proto_DateTime_hour_SHIFT)
                                                         & Proto_DateTime_hour_MASK));
}
/* minute: DateTime byte 4B bit 0-7bit (mask 0xFF) - 分 */
#define Proto_DateTime_minute_MASK       (0xFFu)
#define Proto_DateTime_minute_SHIFT      (0u)
static inline uint8_t Proto_DateTime_Getminute(const Proto_DateTime *p)
{
    return (uint8_t)((p->Data[4u] & Proto_DateTime_minute_MASK)
                     >> Proto_DateTime_minute_SHIFT);
}
static inline void Proto_DateTime_Setminute(Proto_DateTime *p, uint8_t v)
{
    p->Data[4u] = (uint8_t)((p->Data[4u]
                                              & (uint8_t)(~Proto_DateTime_minute_MASK))
                                             | (uint8_t)((v << Proto_DateTime_minute_SHIFT)
                                                         & Proto_DateTime_minute_MASK));
}
/* second: DateTime byte 5B bit 0-7bit (mask 0xFF) - 秒 */
#define Proto_DateTime_second_MASK       (0xFFu)
#define Proto_DateTime_second_SHIFT      (0u)
static inline uint8_t Proto_DateTime_Getsecond(const Proto_DateTime *p)
{
    return (uint8_t)((p->Data[5u] & Proto_DateTime_second_MASK)
                     >> Proto_DateTime_second_SHIFT);
}
static inline void Proto_DateTime_Setsecond(Proto_DateTime *p, uint8_t v)
{
    p->Data[5u] = (uint8_t)((p->Data[5u]
                                              & (uint8_t)(~Proto_DateTime_second_MASK))
                                             | (uint8_t)((v << Proto_DateTime_second_SHIFT)
                                                         & Proto_DateTime_second_MASK));
}
/* ===== PeripheralStatus · SysSrv · 外设工作状态（0x8D 0x04） · Size=3 ===== */
/* 位域结构：按字节原样存储，成员经访问器读写 */
typedef struct
{
    uint8_t Data[3u];
}Proto_PeripheralStatus;

/* can1: PeripheralStatus byte 0B bit 0-7bit (mask 0xFF) - CAN1：0=在线/1=故障 */
#define Proto_PeripheralStatus_can1_MASK       (0xFFu)
#define Proto_PeripheralStatus_can1_SHIFT      (0u)
static inline uint8_t Proto_PeripheralStatus_Getcan1(const Proto_PeripheralStatus *p)
{
    return (uint8_t)((p->Data[0u] & Proto_PeripheralStatus_can1_MASK)
                     >> Proto_PeripheralStatus_can1_SHIFT);
}
static inline void Proto_PeripheralStatus_Setcan1(Proto_PeripheralStatus *p, uint8_t v)
{
    p->Data[0u] = (uint8_t)((p->Data[0u]
                                              & (uint8_t)(~Proto_PeripheralStatus_can1_MASK))
                                             | (uint8_t)((v << Proto_PeripheralStatus_can1_SHIFT)
                                                         & Proto_PeripheralStatus_can1_MASK));
}
/* can2: PeripheralStatus byte 1B bit 0-7bit (mask 0xFF) - CAN2：0=在线/1=故障 */
#define Proto_PeripheralStatus_can2_MASK       (0xFFu)
#define Proto_PeripheralStatus_can2_SHIFT      (0u)
static inline uint8_t Proto_PeripheralStatus_Getcan2(const Proto_PeripheralStatus *p)
{
    return (uint8_t)((p->Data[1u] & Proto_PeripheralStatus_can2_MASK)
                     >> Proto_PeripheralStatus_can2_SHIFT);
}
static inline void Proto_PeripheralStatus_Setcan2(Proto_PeripheralStatus *p, uint8_t v)
{
    p->Data[1u] = (uint8_t)((p->Data[1u]
                                              & (uint8_t)(~Proto_PeripheralStatus_can2_MASK))
                                             | (uint8_t)((v << Proto_PeripheralStatus_can2_SHIFT)
                                                         & Proto_PeripheralStatus_can2_MASK));
}
/* other: PeripheralStatus byte 2B bit 0-7bit (mask 0xFF) - 其它外设状态 */
#define Proto_PeripheralStatus_other_MASK       (0xFFu)
#define Proto_PeripheralStatus_other_SHIFT      (0u)
static inline uint8_t Proto_PeripheralStatus_Getother(const Proto_PeripheralStatus *p)
{
    return (uint8_t)((p->Data[2u] & Proto_PeripheralStatus_other_MASK)
                     >> Proto_PeripheralStatus_other_SHIFT);
}
static inline void Proto_PeripheralStatus_Setother(Proto_PeripheralStatus *p, uint8_t v)
{
    p->Data[2u] = (uint8_t)((p->Data[2u]
                                              & (uint8_t)(~Proto_PeripheralStatus_other_MASK))
                                             | (uint8_t)((v << Proto_PeripheralStatus_other_SHIFT)
                                                         & Proto_PeripheralStatus_other_MASK));
}
/* ===== AutosarNmStatus · PowerMgr · Autosar 网络管理模式与状态（0x810A） · Size=2 ===== */
/* 位域结构：按字节原样存储，成员经访问器读写 */
typedef struct
{
    uint8_t Data[2u];
}Proto_AutosarNmStatus;

/* nm_mode: AutosarNmStatus byte 0B bit 0-7bit (mask 0xFF) - Autosar网络管理模式 */
#define Proto_AutosarNmStatus_nm_mode_MASK       (0xFFu)
#define Proto_AutosarNmStatus_nm_mode_SHIFT      (0u)
static inline uint8_t Proto_AutosarNmStatus_Getnm_mode(const Proto_AutosarNmStatus *p)
{
    return (uint8_t)((p->Data[0u] & Proto_AutosarNmStatus_nm_mode_MASK)
                     >> Proto_AutosarNmStatus_nm_mode_SHIFT);
}
static inline void Proto_AutosarNmStatus_Setnm_mode(Proto_AutosarNmStatus *p, uint8_t v)
{
    p->Data[0u] = (uint8_t)((p->Data[0u]
                                              & (uint8_t)(~Proto_AutosarNmStatus_nm_mode_MASK))
                                             | (uint8_t)((v << Proto_AutosarNmStatus_nm_mode_SHIFT)
                                                         & Proto_AutosarNmStatus_nm_mode_MASK));
}
/* nm_state: AutosarNmStatus byte 1B bit 0-7bit (mask 0xFF) - Autosar网络管理状态 */
#define Proto_AutosarNmStatus_nm_state_MASK       (0xFFu)
#define Proto_AutosarNmStatus_nm_state_SHIFT      (0u)
static inline uint8_t Proto_AutosarNmStatus_Getnm_state(const Proto_AutosarNmStatus *p)
{
    return (uint8_t)((p->Data[1u] & Proto_AutosarNmStatus_nm_state_MASK)
                     >> Proto_AutosarNmStatus_nm_state_SHIFT);
}
static inline void Proto_AutosarNmStatus_Setnm_state(Proto_AutosarNmStatus *p, uint8_t v)
{
    p->Data[1u] = (uint8_t)((p->Data[1u]
                                              & (uint8_t)(~Proto_AutosarNmStatus_nm_state_MASK))
                                             | (uint8_t)((v << Proto_AutosarNmStatus_nm_state_SHIFT)
                                                         & Proto_AutosarNmStatus_nm_state_MASK));
}
/* ===== UpgradeFileInfo · OtaSrv · 升级文件信息（0x0C02） · Size=10 ===== */
typedef struct
{
uint32_t file_size;       /* 0B-3B - 文件大小 BYTE0-3（byte3-byte0） */
uint16_t frame_upgrade_data_len;       /* 4B-5B - 数据分包长度 BYTE4-5（byte1-byte0） */
uint32_t total_pkg_num;       /* 6B-9B - 包序号总数 BYTE6-9（byte3-byte0） */
}Proto_UpgradeFileInfo;

uint16_t Proto_UpgradeFileInfo_Pack(const Proto_UpgradeFileInfo *p, uint8_t *buf);
void Proto_UpgradeFileInfo_Unpack(Proto_UpgradeFileInfo *p, const uint8_t *buf);
/* ===== UpgradeDataPkg · OtaSrv · 升级包数据（0x0C03） · Size=6+N ===== */
typedef struct
{
uint32_t pkg_seq;       /* 0B-3B - 包序号 BYTE0-3（从 0 开始递增） */
uint16_t data_len;       /* 4B-5B - 本包数据长度（字节数） */
uint8_t upgrade_data[1u];      /* 开放尾 6B..N（长度随帧） - 升级包数据 BYTE6-N，末包以 0xFF 填充 */
}Proto_UpgradeDataPkg;

uint16_t Proto_UpgradeDataPkg_Pack(const Proto_UpgradeDataPkg *p, uint8_t *buf);
void Proto_UpgradeDataPkg_Unpack(Proto_UpgradeDataPkg *p, const uint8_t *buf);
/* ===== StrMaxDuration · PowerMgr · STR 最大维持时长（MD 14） · Size=2 ===== */
/* 位域结构：按字节原样存储，成员经访问器读写 */
typedef struct
{
    uint8_t Data[2u];
}Proto_StrMaxDuration;

/* function: StrMaxDuration byte 0B bit 0-7bit (mask 0xFF) - 0 关闭 / 1 打开 / 2 读取状态 */
#define Proto_StrMaxDuration_function_MASK       (0xFFu)
#define Proto_StrMaxDuration_function_SHIFT      (0u)
static inline uint8_t Proto_StrMaxDuration_Getfunction(const Proto_StrMaxDuration *p)
{
    return (uint8_t)((p->Data[0u] & Proto_StrMaxDuration_function_MASK)
                     >> Proto_StrMaxDuration_function_SHIFT);
}
static inline void Proto_StrMaxDuration_Setfunction(Proto_StrMaxDuration *p, uint8_t v)
{
    p->Data[0u] = (uint8_t)((p->Data[0u]
                                              & (uint8_t)(~Proto_StrMaxDuration_function_MASK))
                                             | (uint8_t)((v << Proto_StrMaxDuration_function_SHIFT)
                                                         & Proto_StrMaxDuration_function_MASK));
}
/* hours: StrMaxDuration byte 1B bit 0-7bit (mask 0xFF) - 0 - 7×24 小时 */
#define Proto_StrMaxDuration_hours_MASK       (0xFFu)
#define Proto_StrMaxDuration_hours_SHIFT      (0u)
static inline uint8_t Proto_StrMaxDuration_Gethours(const Proto_StrMaxDuration *p)
{
    return (uint8_t)((p->Data[1u] & Proto_StrMaxDuration_hours_MASK)
                     >> Proto_StrMaxDuration_hours_SHIFT);
}
static inline void Proto_StrMaxDuration_Sethours(Proto_StrMaxDuration *p, uint8_t v)
{
    p->Data[1u] = (uint8_t)((p->Data[1u]
                                              & (uint8_t)(~Proto_StrMaxDuration_hours_MASK))
                                             | (uint8_t)((v << Proto_StrMaxDuration_hours_SHIFT)
                                                         & Proto_StrMaxDuration_hours_MASK));
}
/* ===== VehicleSignalStatus · PowerMgr · 车身信号状态（MD 18） · Size=2 ===== */
/* 位域结构：按字节原样存储，成员经访问器读写 */
typedef struct
{
    uint8_t Data[2u];
}Proto_VehicleSignalStatus;

/* ign_state: VehicleSignalStatus byte 0B bit 0-7bit (mask 0xFF) - 0 IGN OFF / 1 IGN ON / 0xFF 无效 */
#define Proto_VehicleSignalStatus_ign_state_MASK       (0xFFu)
#define Proto_VehicleSignalStatus_ign_state_SHIFT      (0u)
static inline uint8_t Proto_VehicleSignalStatus_Getign_state(const Proto_VehicleSignalStatus *p)
{
    return (uint8_t)((p->Data[0u] & Proto_VehicleSignalStatus_ign_state_MASK)
                     >> Proto_VehicleSignalStatus_ign_state_SHIFT);
}
static inline void Proto_VehicleSignalStatus_Setign_state(Proto_VehicleSignalStatus *p, uint8_t v)
{
    p->Data[0u] = (uint8_t)((p->Data[0u]
                                              & (uint8_t)(~Proto_VehicleSignalStatus_ign_state_MASK))
                                             | (uint8_t)((v << Proto_VehicleSignalStatus_ign_state_SHIFT)
                                                         & Proto_VehicleSignalStatus_ign_state_MASK));
}
/* vehicle_ign_state: VehicleSignalStatus byte 1B bit 0-7bit (mask 0xFF) - 0 IGN_OFF / 1 IGN_ACC / 2 IGN_ON / 3 IGN_START */
#define Proto_VehicleSignalStatus_vehicle_ign_state_MASK       (0xFFu)
#define Proto_VehicleSignalStatus_vehicle_ign_state_SHIFT      (0u)
static inline uint8_t Proto_VehicleSignalStatus_Getvehicle_ign_state(const Proto_VehicleSignalStatus *p)
{
    return (uint8_t)((p->Data[1u] & Proto_VehicleSignalStatus_vehicle_ign_state_MASK)
                     >> Proto_VehicleSignalStatus_vehicle_ign_state_SHIFT);
}
static inline void Proto_VehicleSignalStatus_Setvehicle_ign_state(Proto_VehicleSignalStatus *p, uint8_t v)
{
    p->Data[1u] = (uint8_t)((p->Data[1u]
                                              & (uint8_t)(~Proto_VehicleSignalStatus_vehicle_ign_state_MASK))
                                             | (uint8_t)((v << Proto_VehicleSignalStatus_vehicle_ign_state_SHIFT)
                                                         & Proto_VehicleSignalStatus_vehicle_ign_state_MASK));
}
/* ===== PowerOffReqResult · PowerMgr · SoC 睡眠/关机请求的响应（MD 4） · Size=2 ===== */
/* 位域结构：按字节原样存储，成员经访问器读写 */
typedef struct
{
    uint8_t Data[2u];
}Proto_PowerOffReqResult;

/* powerReqCmd: PowerOffReqResult byte 0B bit 0-7bit (mask 0xFF) - 0 请求STR / 1 请求关机 / 2 请求重启 */
#define Proto_PowerOffReqResult_powerReqCmd_MASK       (0xFFu)
#define Proto_PowerOffReqResult_powerReqCmd_SHIFT      (0u)
static inline uint8_t Proto_PowerOffReqResult_GetpowerReqCmd(const Proto_PowerOffReqResult *p)
{
    return (uint8_t)((p->Data[0u] & Proto_PowerOffReqResult_powerReqCmd_MASK)
                     >> Proto_PowerOffReqResult_powerReqCmd_SHIFT);
}
static inline void Proto_PowerOffReqResult_SetpowerReqCmd(Proto_PowerOffReqResult *p, uint8_t v)
{
    p->Data[0u] = (uint8_t)((p->Data[0u]
                                              & (uint8_t)(~Proto_PowerOffReqResult_powerReqCmd_MASK))
                                             | (uint8_t)((v << Proto_PowerOffReqResult_powerReqCmd_SHIFT)
                                                         & Proto_PowerOffReqResult_powerReqCmd_MASK));
}
/* result: PowerOffReqResult byte 1B bit 0-7bit (mask 0xFF) - 0 成功 / 非0 错误码 */
#define Proto_PowerOffReqResult_result_MASK       (0xFFu)
#define Proto_PowerOffReqResult_result_SHIFT      (0u)
static inline uint8_t Proto_PowerOffReqResult_Getresult(const Proto_PowerOffReqResult *p)
{
    return (uint8_t)((p->Data[1u] & Proto_PowerOffReqResult_result_MASK)
                     >> Proto_PowerOffReqResult_result_SHIFT);
}
static inline void Proto_PowerOffReqResult_Setresult(Proto_PowerOffReqResult *p, uint8_t v)
{
    p->Data[1u] = (uint8_t)((p->Data[1u]
                                              & (uint8_t)(~Proto_PowerOffReqResult_result_MASK))
                                             | (uint8_t)((v << Proto_PowerOffReqResult_result_SHIFT)
                                                         & Proto_PowerOffReqResult_result_MASK));
}
/* ===== PowerStateSyncResult · PowerMgr · SoC 电源状态同步的响应（MD 10） · Size=2 ===== */
/* 位域结构：按字节原样存储，成员经访问器读写 */
typedef struct
{
    uint8_t Data[2u];
}Proto_PowerStateSyncResult;

/* powerState: PowerStateSyncResult byte 0B bit 0-7bit (mask 0xFF) - 高4bit OTA模式 / 低4bit SoC电源状态 */
#define Proto_PowerStateSyncResult_powerState_MASK       (0xFFu)
#define Proto_PowerStateSyncResult_powerState_SHIFT      (0u)
static inline uint8_t Proto_PowerStateSyncResult_GetpowerState(const Proto_PowerStateSyncResult *p)
{
    return (uint8_t)((p->Data[0u] & Proto_PowerStateSyncResult_powerState_MASK)
                     >> Proto_PowerStateSyncResult_powerState_SHIFT);
}
static inline void Proto_PowerStateSyncResult_SetpowerState(Proto_PowerStateSyncResult *p, uint8_t v)
{
    p->Data[0u] = (uint8_t)((p->Data[0u]
                                              & (uint8_t)(~Proto_PowerStateSyncResult_powerState_MASK))
                                             | (uint8_t)((v << Proto_PowerStateSyncResult_powerState_SHIFT)
                                                         & Proto_PowerStateSyncResult_powerState_MASK));
}
/* result: PowerStateSyncResult byte 1B bit 0-7bit (mask 0xFF) - 0 成功 / 非0 错误码 */
#define Proto_PowerStateSyncResult_result_MASK       (0xFFu)
#define Proto_PowerStateSyncResult_result_SHIFT      (0u)
static inline uint8_t Proto_PowerStateSyncResult_Getresult(const Proto_PowerStateSyncResult *p)
{
    return (uint8_t)((p->Data[1u] & Proto_PowerStateSyncResult_result_MASK)
                     >> Proto_PowerStateSyncResult_result_SHIFT);
}
static inline void Proto_PowerStateSyncResult_Setresult(Proto_PowerStateSyncResult *p, uint8_t v)
{
    p->Data[1u] = (uint8_t)((p->Data[1u]
                                              & (uint8_t)(~Proto_PowerStateSyncResult_result_MASK))
                                             | (uint8_t)((v << Proto_PowerStateSyncResult_result_SHIFT)
                                                         & Proto_PowerStateSyncResult_result_MASK));
}
/* ===== PeripheralPowerReq · PowerMgr · 外设电源控制请求载荷（0x8112） · Size=2 ===== */
/* 位域结构：按字节原样存储，成员经访问器读写 */
typedef struct
{
    uint8_t Data[2u];
}Proto_PeripheralPowerReq;

/* power_type: PeripheralPowerReq byte 0B bit 0-7bit (mask 0xFF) - 外设类型 0x00 背光 / 0x01 功放 / 0x02 中控屏幕 / 0x03 仪表屏幕 */
#define Proto_PeripheralPowerReq_power_type_MASK       (0xFFu)
#define Proto_PeripheralPowerReq_power_type_SHIFT      (0u)
static inline uint8_t Proto_PeripheralPowerReq_Getpower_type(const Proto_PeripheralPowerReq *p)
{
    return (uint8_t)((p->Data[0u] & Proto_PeripheralPowerReq_power_type_MASK)
                     >> Proto_PeripheralPowerReq_power_type_SHIFT);
}
static inline void Proto_PeripheralPowerReq_Setpower_type(Proto_PeripheralPowerReq *p, uint8_t v)
{
    p->Data[0u] = (uint8_t)((p->Data[0u]
                                              & (uint8_t)(~Proto_PeripheralPowerReq_power_type_MASK))
                                             | (uint8_t)((v << Proto_PeripheralPowerReq_power_type_SHIFT)
                                                         & Proto_PeripheralPowerReq_power_type_MASK));
}
/* on_off: PeripheralPowerReq byte 1B bit 0-7bit (mask 0xFF) - 0x00 关闭 / 0x01 打开 */
#define Proto_PeripheralPowerReq_on_off_MASK       (0xFFu)
#define Proto_PeripheralPowerReq_on_off_SHIFT      (0u)
static inline uint8_t Proto_PeripheralPowerReq_Geton_off(const Proto_PeripheralPowerReq *p)
{
    return (uint8_t)((p->Data[1u] & Proto_PeripheralPowerReq_on_off_MASK)
                     >> Proto_PeripheralPowerReq_on_off_SHIFT);
}
static inline void Proto_PeripheralPowerReq_Seton_off(Proto_PeripheralPowerReq *p, uint8_t v)
{
    p->Data[1u] = (uint8_t)((p->Data[1u]
                                              & (uint8_t)(~Proto_PeripheralPowerReq_on_off_MASK))
                                             | (uint8_t)((v << Proto_PeripheralPowerReq_on_off_SHIFT)
                                                         & Proto_PeripheralPowerReq_on_off_MASK));
}
/* ===== PeripheralPowerAck · PowerMgr · 外设电源控制应答载荷（0x0112） · Size=2 ===== */
/* 位域结构：按字节原样存储，成员经访问器读写 */
typedef struct
{
    uint8_t Data[2u];
}Proto_PeripheralPowerAck;

/* power_type: PeripheralPowerAck byte 0B bit 0-7bit (mask 0xFF) - 外设类型 0x00 背光 / 0x01 功放 / 0x02 中控屏幕 / 0x03 仪表屏幕 */
#define Proto_PeripheralPowerAck_power_type_MASK       (0xFFu)
#define Proto_PeripheralPowerAck_power_type_SHIFT      (0u)
static inline uint8_t Proto_PeripheralPowerAck_Getpower_type(const Proto_PeripheralPowerAck *p)
{
    return (uint8_t)((p->Data[0u] & Proto_PeripheralPowerAck_power_type_MASK)
                     >> Proto_PeripheralPowerAck_power_type_SHIFT);
}
static inline void Proto_PeripheralPowerAck_Setpower_type(Proto_PeripheralPowerAck *p, uint8_t v)
{
    p->Data[0u] = (uint8_t)((p->Data[0u]
                                              & (uint8_t)(~Proto_PeripheralPowerAck_power_type_MASK))
                                             | (uint8_t)((v << Proto_PeripheralPowerAck_power_type_SHIFT)
                                                         & Proto_PeripheralPowerAck_power_type_MASK));
}
/* result: PeripheralPowerAck byte 1B bit 0-7bit (mask 0xFF) - 0x00 成功 / 非0 错误码 */
#define Proto_PeripheralPowerAck_result_MASK       (0xFFu)
#define Proto_PeripheralPowerAck_result_SHIFT      (0u)
static inline uint8_t Proto_PeripheralPowerAck_Getresult(const Proto_PeripheralPowerAck *p)
{
    return (uint8_t)((p->Data[1u] & Proto_PeripheralPowerAck_result_MASK)
                     >> Proto_PeripheralPowerAck_result_SHIFT);
}
static inline void Proto_PeripheralPowerAck_Setresult(Proto_PeripheralPowerAck *p, uint8_t v)
{
    p->Data[1u] = (uint8_t)((p->Data[1u]
                                              & (uint8_t)(~Proto_PeripheralPowerAck_result_MASK))
                                             | (uint8_t)((v << Proto_PeripheralPowerAck_result_SHIFT)
                                                         & Proto_PeripheralPowerAck_result_MASK));
}
/* ===== McuPowerReq · PowerMgr · MCU 电源控制请求载荷（0x0113） · Size=2 ===== */
/* 位域结构：按字节原样存储，成员经访问器读写 */
typedef struct
{
    uint8_t Data[2u];
}Proto_McuPowerReq;

/* ctrl_type: McuPowerReq byte 0B bit 0-7bit (mask 0xFF) - 控制类型 0x00 保留 / 0x01 请求控制 VBUS 电源 */
#define Proto_McuPowerReq_ctrl_type_MASK       (0xFFu)
#define Proto_McuPowerReq_ctrl_type_SHIFT      (0u)
static inline uint8_t Proto_McuPowerReq_Getctrl_type(const Proto_McuPowerReq *p)
{
    return (uint8_t)((p->Data[0u] & Proto_McuPowerReq_ctrl_type_MASK)
                     >> Proto_McuPowerReq_ctrl_type_SHIFT);
}
static inline void Proto_McuPowerReq_Setctrl_type(Proto_McuPowerReq *p, uint8_t v)
{
    p->Data[0u] = (uint8_t)((p->Data[0u]
                                              & (uint8_t)(~Proto_McuPowerReq_ctrl_type_MASK))
                                             | (uint8_t)((v << Proto_McuPowerReq_ctrl_type_SHIFT)
                                                         & Proto_McuPowerReq_ctrl_type_MASK));
}
/* ctrl_cmd: McuPowerReq byte 1B bit 0-7bit (mask 0xFF) - 0x00 关闭 / 0x01 打开 / 0x02 重启 */
#define Proto_McuPowerReq_ctrl_cmd_MASK       (0xFFu)
#define Proto_McuPowerReq_ctrl_cmd_SHIFT      (0u)
static inline uint8_t Proto_McuPowerReq_Getctrl_cmd(const Proto_McuPowerReq *p)
{
    return (uint8_t)((p->Data[1u] & Proto_McuPowerReq_ctrl_cmd_MASK)
                     >> Proto_McuPowerReq_ctrl_cmd_SHIFT);
}
static inline void Proto_McuPowerReq_Setctrl_cmd(Proto_McuPowerReq *p, uint8_t v)
{
    p->Data[1u] = (uint8_t)((p->Data[1u]
                                              & (uint8_t)(~Proto_McuPowerReq_ctrl_cmd_MASK))
                                             | (uint8_t)((v << Proto_McuPowerReq_ctrl_cmd_SHIFT)
                                                         & Proto_McuPowerReq_ctrl_cmd_MASK));
}
/* ===== McuPowerAck · PowerMgr · MCU 电源控制应答载荷（0x8113） · Size=2 ===== */
/* 位域结构：按字节原样存储，成员经访问器读写 */
typedef struct
{
    uint8_t Data[2u];
}Proto_McuPowerAck;

/* ctrl_type: McuPowerAck byte 0B bit 0-7bit (mask 0xFF) - 控制类型 0x00 保留 / 0x01 VBUS */
#define Proto_McuPowerAck_ctrl_type_MASK       (0xFFu)
#define Proto_McuPowerAck_ctrl_type_SHIFT      (0u)
static inline uint8_t Proto_McuPowerAck_Getctrl_type(const Proto_McuPowerAck *p)
{
    return (uint8_t)((p->Data[0u] & Proto_McuPowerAck_ctrl_type_MASK)
                     >> Proto_McuPowerAck_ctrl_type_SHIFT);
}
static inline void Proto_McuPowerAck_Setctrl_type(Proto_McuPowerAck *p, uint8_t v)
{
    p->Data[0u] = (uint8_t)((p->Data[0u]
                                              & (uint8_t)(~Proto_McuPowerAck_ctrl_type_MASK))
                                             | (uint8_t)((v << Proto_McuPowerAck_ctrl_type_SHIFT)
                                                         & Proto_McuPowerAck_ctrl_type_MASK));
}
/* result: McuPowerAck byte 1B bit 0-7bit (mask 0xFF) - 0x00 成功 / 非0 错误码 */
#define Proto_McuPowerAck_result_MASK       (0xFFu)
#define Proto_McuPowerAck_result_SHIFT      (0u)
static inline uint8_t Proto_McuPowerAck_Getresult(const Proto_McuPowerAck *p)
{
    return (uint8_t)((p->Data[1u] & Proto_McuPowerAck_result_MASK)
                     >> Proto_McuPowerAck_result_SHIFT);
}
static inline void Proto_McuPowerAck_Setresult(Proto_McuPowerAck *p, uint8_t v)
{
    p->Data[1u] = (uint8_t)((p->Data[1u]
                                              & (uint8_t)(~Proto_McuPowerAck_result_MASK))
                                             | (uint8_t)((v << Proto_McuPowerAck_result_SHIFT)
                                                         & Proto_McuPowerAck_result_MASK));
}
/* ===== TimeZoneInfo · PowerMgr · 时区偏移信息（0x0115） · Size=3 ===== */
/* 位域结构：按字节原样存储，成员经访问器读写 */
typedef struct
{
    uint8_t Data[3u];
}Proto_TimeZoneInfo;

/* sign: TimeZoneInfo byte 0B bit 0-7bit (mask 0xFF) - 0x00 正数 / 0x01 负数 */
#define Proto_TimeZoneInfo_sign_MASK       (0xFFu)
#define Proto_TimeZoneInfo_sign_SHIFT      (0u)
static inline uint8_t Proto_TimeZoneInfo_Getsign(const Proto_TimeZoneInfo *p)
{
    return (uint8_t)((p->Data[0u] & Proto_TimeZoneInfo_sign_MASK)
                     >> Proto_TimeZoneInfo_sign_SHIFT);
}
static inline void Proto_TimeZoneInfo_Setsign(Proto_TimeZoneInfo *p, uint8_t v)
{
    p->Data[0u] = (uint8_t)((p->Data[0u]
                                              & (uint8_t)(~Proto_TimeZoneInfo_sign_MASK))
                                             | (uint8_t)((v << Proto_TimeZoneInfo_sign_SHIFT)
                                                         & Proto_TimeZoneInfo_sign_MASK));
}
/* ===== 命令处理函数原型（stub 由 Proto_CmdStub.c 生成） ===== */
void Proto_PowerOnHandshakeMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x0100 PowerOnHandshakeMtd */
void Proto_PowerOffReqMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x0101 PowerOffReqMtd */
void Proto_HeartbeatSetMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x0102 HeartbeatSetMtd */
void Proto_HeartbeatReqMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x0103 HeartbeatReqMtd */
void Proto_PowerMgmtReqMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x0105 PowerMgmtReqMtd */
void Proto_StrStateFbMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x0106 StrStateFbMtd */
void Proto_StrDebugSetMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x011E StrDebugSetMtd */
void Proto_PowerStateSetMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x0108 PowerStateSetMtd */
void Proto_PowerOffReqAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x011F PowerOffReqAckEvt */
void Proto_BatteryStatusAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x0107 BatteryStatusAckEvt */
void Proto_EnterStrAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x010D EnterStrAckEvt */
void Proto_WakeSocAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x010E WakeSocAckEvt */
void Proto_McuRestartReqMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x010F McuRestartReqMtd */
void Proto_KeyRestartAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x0110 KeyRestartAckEvt */
void Proto_RtcRestartAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x0111 RtcRestartAckEvt */
void Proto_SocPowerCtrlAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x0112 SocPowerCtrlAckEvt */
void Proto_McuPowerCtrlReqMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x0113 McuPowerCtrlReqMtd */
void Proto_RtcTimeSetMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x0114 RtcTimeSetMtd */
void Proto_TimeZoneSetMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x0115 TimeZoneSetMtd */
void Proto_SentryModeSetMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x0116 SentryModeSetMtd */
void Proto_PetModeSetMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x0117 PetModeSetMtd */
void Proto_BatteryVoltageAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x0118 BatteryVoltageAckEvt */
void Proto_VehicleSignalAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x0119 VehicleSignalAckEvt */
void Proto_HeartbeatLostAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x011A HeartbeatLostAckEvt */
void Proto_HeartbeatRecoveredAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x011B HeartbeatRecoveredAckEvt */
void Proto_TemperatureAbnormalAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x011C TemperatureAbnormalAckEvt */
void Proto_SocFanQueryMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x0801 SocFanQueryMtd */
void Proto_SocFanCtrlMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x0802 SocFanCtrlMtd */
void Proto_UpgradeCmdEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x0C00 UpgradeCmdEvt */
void Proto_UpgradeFileInfoRspEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x0C02 UpgradeFileInfoRspEvt */
void Proto_UpgradeDataRspEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x0C03 UpgradeDataRspEvt */
void Proto_TimeQueryMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x0D01 TimeQueryMtd */
void Proto_TimeSetEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x0D02 TimeSetEvt */
void Proto_HandshakeAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x8100 HandshakeAckEvt */
void Proto_PowerOffReqEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x811F PowerOffReqEvt */
void Proto_HeartbeatSetStatusEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x8102 HeartbeatSetStatusEvt */
void Proto_HeartbeatFeedbackEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x8103 HeartbeatFeedbackEvt */
void Proto_PowerMgmtStatusEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x8105 PowerMgmtStatusEvt */
void Proto_AccStatusEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x8106 AccStatusEvt */
void Proto_BatteryStatusEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x8107 BatteryStatusEvt */
void Proto_ResetReasonEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x811D ResetReasonEvt */
void Proto_AutosarNmModeEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x810A AutosarNmModeEvt */
void Proto_VehicleAntiTheftEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x810B VehicleAntiTheftEvt */
void Proto_RemoteControlModeEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x810C RemoteControlModeEvt */
void Proto_PowerOffReqStatusEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x8101 PowerOffReqStatusEvt */
void Proto_PowerStateSetStatusEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x8108 PowerStateSetStatusEvt */
void Proto_StrDebugSetStatusEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x811E StrDebugSetStatusEvt */
void Proto_EnterStrEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x810D EnterStrEvt */
void Proto_WakeSocEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x810E WakeSocEvt */
void Proto_McuRestartAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x810F McuRestartAckEvt */
void Proto_KeyRestartReqEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x8110 KeyRestartReqEvt */
void Proto_RtcRestartReqEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x8111 RtcRestartReqEvt */
void Proto_SocPowerCtrlReqEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x8112 SocPowerCtrlReqEvt */
void Proto_McuPowerCtrlAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x8113 McuPowerCtrlAckEvt */
void Proto_RtcTimeSetAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x8114 RtcTimeSetAckEvt */
void Proto_TimeZoneSetAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x8115 TimeZoneSetAckEvt */
void Proto_SentryModeAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x8116 SentryModeAckEvt */
void Proto_PetModeAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x8117 PetModeAckEvt */
void Proto_BatteryVoltageEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x8118 BatteryVoltageEvt */
void Proto_VehicleSignalEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x8119 VehicleSignalEvt */
void Proto_HeartbeatLostEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x811A HeartbeatLostEvt */
void Proto_HeartbeatRecoveredEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x811B HeartbeatRecoveredEvt */
void Proto_TemperatureAbnormalEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x811C TemperatureAbnormalEvt */
void Proto_SocFanSpeedEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x8802 SocFanSpeedEvt */
void Proto_UpgradeStatusEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x8C01 UpgradeStatusEvt */
void Proto_UpgradeFileInfoReqMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x8C02 UpgradeFileInfoReqMtd */
void Proto_UpgradeDataReqMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x8C03 UpgradeDataReqMtd */
void Proto_TimeQueryAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x8D01 TimeQueryAckEvt */
void Proto_TimeUploadEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x8D02 TimeUploadEvt */
#endif /* PROTO_PROTO_TYPES_H */
/*************************************************************************************************
 * End of File
 ************************************************************************************************/
