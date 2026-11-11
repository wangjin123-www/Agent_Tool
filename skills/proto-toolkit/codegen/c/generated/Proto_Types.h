/*************************************************************************************************
 * @file    Proto_Types.h
 * @brief   7255 MCU&SOC 协议数据结构（由 proto-toolkit 从协议表生成，禁止手改）
 * @copyright Copyright (c) 2026, cviauto.com. All rights reserved.
 *
 * 源: 7255 MCU&SOC 通信协议（Bitable Mj3gbU3NqagG4WsPcQgc0YhSnac） rev.4.0.0
 * 命名: 类型名直接用表内名（结构体 Xxx_t / 枚举 Xxx_E），成员名小驼峰；
 *       Pack/Unpack 与位域访问器带 Proto_ 前缀，避免与业务符号冲突。
 * 约定: 大端（BYTE0 先发，字节内 bit7 先发）；bit 成员不使用 C 位域，
 *       通过 Proto_<Struct>_Get/Set<X>() 掩码访问，保证跨编译器一致。
 ************************************************************************************************/
#ifndef PROTO_PROTO_TYPES_H
#define PROTO_PROTO_TYPES_H

#include <stdint.h>

/* ===== AutosarNmStatus_t · AutosarNmModeEvt · Autosar 网络管理模式与状态（0x810A） · Size= ===== */
typedef struct
{
    uint8_t nmMode;       /* 0B - Autosar网络管理模式 */
    uint8_t nmState;       /* 1B - Autosar网络管理状态 */
}AutosarNmStatus_t;

uint16_t Proto_AutosarNmStatus_Pack(const AutosarNmStatus_t *p, uint8_t *buf);
void Proto_AutosarNmStatus_Unpack(AutosarNmStatus_t *p, const uint8_t *buf);
/* ===== DateTime_t · TimeQueryMtd、RtcTimeSetMtd、TimeSetEvt、TimeUploadEvt、TimeQueryAckEvt · 时间同步（0x0D 0x01/0x02、0x8D 0x02） · Size= ===== */
typedef struct
{
    uint8_t year;       /* 0B - 年 */
    uint8_t month;       /* 1B - 月 */
    uint8_t day;       /* 2B - 日 */
    uint8_t hour;       /* 3B - 时 */
    uint8_t minute;       /* 4B - 分 */
    uint8_t second;       /* 5B - 秒 */
}DateTime_t;

uint16_t Proto_DateTime_Pack(const DateTime_t *p, uint8_t *buf);
void Proto_DateTime_Unpack(DateTime_t *p, const uint8_t *buf);
/* ===== McuPowerAck_t · McuPowerCtrlAckEvt · MCU 电源控制应答载荷（0x8113） · Size= ===== */
typedef struct
{
    uint8_t ctrlType;       /* 0B - 控制类型 0x00 保留 / 0x01 VBUS */
    uint8_t result;       /* 1B - 0x00 成功 / 非0 错误码 */
}McuPowerAck_t;

uint16_t Proto_McuPowerAck_Pack(const McuPowerAck_t *p, uint8_t *buf);
void Proto_McuPowerAck_Unpack(McuPowerAck_t *p, const uint8_t *buf);
/* ===== McuPowerReq_t · McuPowerCtrlReqMtd · MCU 电源控制请求载荷（0x0113） · Size= ===== */
typedef struct
{
    uint8_t ctrlType;       /* 0B - 控制类型 0x00 保留 / 0x01 请求控制 VBUS 电源 */
    uint8_t ctrlCmd;       /* 1B - 0x00 关闭 / 0x01 打开 / 0x02 重启 */
}McuPowerReq_t;

uint16_t Proto_McuPowerReq_Pack(const McuPowerReq_t *p, uint8_t *buf);
void Proto_McuPowerReq_Unpack(McuPowerReq_t *p, const uint8_t *buf);
/* ===== PeripheralPowerAck_t · SocPowerCtrlAckEvt · 外设电源控制应答载荷（0x0112） · Size= ===== */
typedef struct
{
    uint8_t powerType;       /* 0B - 外设类型 0x00 背光 / 0x01 功放 / 0x02 中控屏幕 / 0x03 仪表屏幕 */
    uint8_t result;       /* 1B - 0x00 成功 / 非0 错误码 */
}PeripheralPowerAck_t;

uint16_t Proto_PeripheralPowerAck_Pack(const PeripheralPowerAck_t *p, uint8_t *buf);
void Proto_PeripheralPowerAck_Unpack(PeripheralPowerAck_t *p, const uint8_t *buf);
/* ===== PeripheralPowerReq_t · SocPowerCtrlReqEvt · 外设电源控制请求载荷（0x8112） · Size= ===== */
typedef struct
{
    uint8_t powerType;       /* 0B - 外设类型 0x00 背光 / 0x01 功放 / 0x02 中控屏幕 / 0x03 仪表屏幕 */
    uint8_t onOff;       /* 1B - 0x00 关闭 / 0x01 打开 */
}PeripheralPowerReq_t;

uint16_t Proto_PeripheralPowerReq_Pack(const PeripheralPowerReq_t *p, uint8_t *buf);
void Proto_PeripheralPowerReq_Unpack(PeripheralPowerReq_t *p, const uint8_t *buf);
/* ===== PeripheralStatus_t ·  · 外设工作状态（0x8D 0x04） · Size= ===== */
typedef struct
{
    uint8_t can1;       /* 0B - CAN1：0=在线/1=故障 */
    uint8_t can2;       /* 1B - CAN2：0=在线/1=故障 */
    uint8_t other;       /* 2B - 其它外设状态 */
}PeripheralStatus_t;

uint16_t Proto_PeripheralStatus_Pack(const PeripheralStatus_t *p, uint8_t *buf);
void Proto_PeripheralStatus_Unpack(PeripheralStatus_t *p, const uint8_t *buf);
/* ===== PowerOffReqResult_t · PowerOffReqStatusEvt · SoC 睡眠/关机请求的响应（MD 4） · Size= ===== */
typedef struct
{
    uint8_t powerReqCmd;       /* 0B - 0 请求STR / 1 请求关机 / 2 请求重启 */
    uint8_t result;       /* 1B - 0 成功 / 非0 错误码 */
}PowerOffReqResult_t;

uint16_t Proto_PowerOffReqResult_Pack(const PowerOffReqResult_t *p, uint8_t *buf);
void Proto_PowerOffReqResult_Unpack(PowerOffReqResult_t *p, const uint8_t *buf);
/* ===== PowerStateSyncResult_t · PowerStateSetStatusEvt · SoC 电源状态同步的响应（MD 10） · Size= ===== */
typedef struct
{
    uint8_t powerState;       /* 0B - 高4bit OTA模式 / 低4bit SoC电源状态 */
    uint8_t result;       /* 1B - 0 成功 / 非0 错误码 */
}PowerStateSyncResult_t;

uint16_t Proto_PowerStateSyncResult_Pack(const PowerStateSyncResult_t *p, uint8_t *buf);
void Proto_PowerStateSyncResult_Unpack(PowerStateSyncResult_t *p, const uint8_t *buf);
/* ===== StrMaxDuration_t · StrDebugSetStatusEvt、StrDebugSetMtd · STR 最大维持时长（MD 14） · Size= ===== */
typedef struct
{
    uint8_t function;       /* 0B - 0 关闭 / 1 打开 / 2 读取状态 */
    uint8_t hours;       /* 1B - 0 - 7×24 小时 */
}StrMaxDuration_t;

uint16_t Proto_StrMaxDuration_Pack(const StrMaxDuration_t *p, uint8_t *buf);
void Proto_StrMaxDuration_Unpack(StrMaxDuration_t *p, const uint8_t *buf);
/* ===== TimeZoneInfo_t · TimeZoneSetMtd · 时区偏移信息（0x0115） · Size= ===== */
typedef struct
{
    uint8_t sign;       /* 0B - 0x00 正数 / 0x01 负数 */
    uint16_t offsetSeconds;       /* 1B-2B - 当前需要偏移的秒数 */
}TimeZoneInfo_t;

uint16_t Proto_TimeZoneInfo_Pack(const TimeZoneInfo_t *p, uint8_t *buf);
void Proto_TimeZoneInfo_Unpack(TimeZoneInfo_t *p, const uint8_t *buf);
/* ===== UpgradeDataPkg_t · UpgradeDataRspEvt · 升级包数据（0x0C03） · Size= ===== */
typedef struct
{
    uint32_t pkgSeq;       /* 0B-3B - 包序号 BYTE0-3（从 0 开始递增） */
    uint16_t dataLen;       /* 4B-5B - 本包数据长度（字节数） */
    uint8_t upgradeData[1u];      /* 开放尾 6B..N（长度随帧） - 升级包数据 BYTE6-N，末包以 0xFF 填充 */
}UpgradeDataPkg_t;

uint16_t Proto_UpgradeDataPkg_Pack(const UpgradeDataPkg_t *p, uint8_t *buf);
void Proto_UpgradeDataPkg_Unpack(UpgradeDataPkg_t *p, const uint8_t *buf);
/* ===== UpgradeFileInfo_t · UpgradeFileInfoRspEvt · 升级文件信息（0x0C02） · Size= ===== */
typedef struct
{
    uint32_t fileSize;       /* 0B-3B - 文件大小 BYTE0-3（byte3-byte0） */
    uint16_t frameUpgradeDataLen;       /* 4B-5B - 数据分包长度 BYTE4-5（byte1-byte0） */
    uint32_t totalPkgNum;       /* 6B-9B - 包序号总数 BYTE6-9（byte3-byte0） */
}UpgradeFileInfo_t;

uint16_t Proto_UpgradeFileInfo_Pack(const UpgradeFileInfo_t *p, uint8_t *buf);
void Proto_UpgradeFileInfo_Unpack(UpgradeFileInfo_t *p, const uint8_t *buf);
/* ===== VehicleSignalStatus_t · VehicleSignalEvt · 车身信号状态（MD 18） · Size= ===== */
typedef struct
{
    uint8_t ignState;       /* 0B - 0 IGN OFF / 1 IGN ON / 0xFF 无效 */
    uint8_t vehicleIgnState;       /* 1B - 0 IGN_OFF / 1 IGN_ACC / 2 IGN_ON / 3 IGN_START */
}VehicleSignalStatus_t;

uint16_t Proto_VehicleSignalStatus_Pack(const VehicleSignalStatus_t *p, uint8_t *buf);
void Proto_VehicleSignalStatus_Unpack(VehicleSignalStatus_t *p, const uint8_t *buf);
/* ===== VersionInfo_t · VersionQueryAckEvt · 版本查询回复载荷（0x8E01） · Size= ===== */
typedef struct
{
    uint8_t module;       /* 0B - 模块号：0x01 DVR / 0x02 RADAR / 0x03 HW / 0x04 诊断SW / 0x05 MCU */
    uint8_t len;       /* 1B - 版本数组长度 n（ver_array 元素个数） */
    uint8_t verArray[1u];      /* 开放尾 2B..N（长度随帧） - 版本号字符串 */
}VersionInfo_t;

uint16_t Proto_VersionInfo_Pack(const VersionInfo_t *p, uint8_t *buf);
void Proto_VersionInfo_Unpack(VersionInfo_t *p, const uint8_t *buf);
/* ===== 命令处理函数原型（stub 由 Proto_CmdStub.c 生成） ===== */
void Proto_PowerOnHandshakeMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x0100 PowerOnHandshakeMtd */
void Proto_HeartbeatSetMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x0102 HeartbeatSetMtd */
void Proto_HeartbeatReqMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x0103 HeartbeatReqMtd */
void Proto_PowerMgmtReqMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x0105 PowerMgmtReqMtd */
void Proto_StrStateFbMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x0106 StrStateFbMtd */
void Proto_BatteryStatusAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x0107 BatteryStatusAckEvt */
void Proto_PowerStateSetMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x0108 PowerStateSetMtd */
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
void Proto_StrDebugSetMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x011E StrDebugSetMtd */
void Proto_PowerOffReqAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x011F PowerOffReqAckEvt */
void Proto_PowerOffReqMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x0801 PowerOffReqMtd */
void Proto_SocFanQueryMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x0801 SocFanQueryMtd */
void Proto_SocFanCtrlMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x0802 SocFanCtrlMtd */
void Proto_UpgradeCmdEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x0C00 UpgradeCmdEvt */
void Proto_UpgradeFileInfoRspEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x0C02 UpgradeFileInfoRspEvt */
void Proto_UpgradeDataRspEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x0C03 UpgradeDataRspEvt */
void Proto_TimeQueryMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x0D01 TimeQueryMtd */
void Proto_TimeSetEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x0D02 TimeSetEvt */
void Proto_VersionQueryMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x0E01 VersionQueryMtd */
void Proto_HandshakeAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x8100 HandshakeAckEvt */
void Proto_PowerOffReqStatusEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x8101 PowerOffReqStatusEvt */
void Proto_HeartbeatSetStatusEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x8102 HeartbeatSetStatusEvt */
void Proto_HeartbeatFeedbackEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x8103 HeartbeatFeedbackEvt */
void Proto_PowerMgmtStatusEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x8105 PowerMgmtStatusEvt */
void Proto_AccStatusEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x8106 AccStatusEvt */
void Proto_BatteryStatusEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x8107 BatteryStatusEvt */
void Proto_PowerStateSetStatusEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x8108 PowerStateSetStatusEvt */
void Proto_AutosarNmModeEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x810A AutosarNmModeEvt */
void Proto_VehicleAntiTheftEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x810B VehicleAntiTheftEvt */
void Proto_RemoteControlModeEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x810C RemoteControlModeEvt */
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
void Proto_ResetReasonEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x811D ResetReasonEvt */
void Proto_StrDebugSetStatusEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x811E StrDebugSetStatusEvt */
void Proto_PowerOffReqEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x811F PowerOffReqEvt */
void Proto_SocFanSpeedEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x8802 SocFanSpeedEvt */
void Proto_UpgradeStatusEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x8C01 UpgradeStatusEvt */
void Proto_UpgradeFileInfoReqMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x8C02 UpgradeFileInfoReqMtd */
void Proto_UpgradeDataReqMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x8C03 UpgradeDataReqMtd */
void Proto_TimeQueryAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x8D01 TimeQueryAckEvt */
void Proto_TimeUploadEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x8D02 TimeUploadEvt */
void Proto_VersionQueryAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len);   /* 0x8E01 VersionQueryAckEvt */
#endif /* PROTO_PROTO_TYPES_H */
/*************************************************************************************************
 * End of File
 ************************************************************************************************/
