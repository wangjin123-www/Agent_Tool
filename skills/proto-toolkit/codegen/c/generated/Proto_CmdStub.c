/*************************************************************************************************
 * @file    Proto_CmdStub.c
 * @brief   7255 MCU&SOC 协议命令处理桩 + Pack/Unpack 实现（由 proto-toolkit 生成，禁止手改）
 * @copyright Copyright (c) 2026, cviauto.com. All rights reserved.
 *
 * 源: 7255 MCU&SOC 通信协议（Bitable Mj3gbU3NqagG4WsPcQgc0YhSnac） rev.4.0.0
 * 命名: 类型名直接用表内名（Xxx_t / Xxx_E），函数名带 Proto_ 前缀。
 * 集成: 参考实现落点。真实现接入后，用 <名>_Fun 同名函数替换桩体即可（表不用改）。
 ************************************************************************************************/
#include "Proto_Types.h"
#include <string.h>

/* AutosarNmStatus_t: Autosar 网络管理模式与状态（0x810A） 大端 Pack（返回写入字节数） */
uint16_t Proto_AutosarNmStatus_Pack(const AutosarNmStatus_t *p, uint8_t *buf)
{
    uint16_t i = 0u;
    buf[i] = p->nmMode; i++;
    buf[i] = p->nmState; i++;
    return i;
}

void Proto_AutosarNmStatus_Unpack(AutosarNmStatus_t *p, const uint8_t *buf)
{
    uint16_t i = 0u;
    p->nmMode = buf[i]; i++;
    p->nmState = buf[i]; i++;
}

/* DateTime_t: 时间同步（0x0D 0x01/0x02、0x8D 0x02） 大端 Pack（返回写入字节数） */
uint16_t Proto_DateTime_Pack(const DateTime_t *p, uint8_t *buf)
{
    uint16_t i = 0u;
    buf[i] = p->year; i++;
    buf[i] = p->month; i++;
    buf[i] = p->day; i++;
    buf[i] = p->hour; i++;
    buf[i] = p->minute; i++;
    buf[i] = p->second; i++;
    return i;
}

void Proto_DateTime_Unpack(DateTime_t *p, const uint8_t *buf)
{
    uint16_t i = 0u;
    p->year = buf[i]; i++;
    p->month = buf[i]; i++;
    p->day = buf[i]; i++;
    p->hour = buf[i]; i++;
    p->minute = buf[i]; i++;
    p->second = buf[i]; i++;
}

/* McuPowerAck_t: MCU 电源控制应答载荷（0x8113） 大端 Pack（返回写入字节数） */
uint16_t Proto_McuPowerAck_Pack(const McuPowerAck_t *p, uint8_t *buf)
{
    uint16_t i = 0u;
    buf[i] = p->ctrlType; i++;
    buf[i] = p->result; i++;
    return i;
}

void Proto_McuPowerAck_Unpack(McuPowerAck_t *p, const uint8_t *buf)
{
    uint16_t i = 0u;
    p->ctrlType = buf[i]; i++;
    p->result = buf[i]; i++;
}

/* McuPowerReq_t: MCU 电源控制请求载荷（0x0113） 大端 Pack（返回写入字节数） */
uint16_t Proto_McuPowerReq_Pack(const McuPowerReq_t *p, uint8_t *buf)
{
    uint16_t i = 0u;
    buf[i] = p->ctrlType; i++;
    buf[i] = p->ctrlCmd; i++;
    return i;
}

void Proto_McuPowerReq_Unpack(McuPowerReq_t *p, const uint8_t *buf)
{
    uint16_t i = 0u;
    p->ctrlType = buf[i]; i++;
    p->ctrlCmd = buf[i]; i++;
}

/* PeripheralPowerAck_t: 外设电源控制应答载荷（0x0112） 大端 Pack（返回写入字节数） */
uint16_t Proto_PeripheralPowerAck_Pack(const PeripheralPowerAck_t *p, uint8_t *buf)
{
    uint16_t i = 0u;
    buf[i] = p->powerType; i++;
    buf[i] = p->result; i++;
    return i;
}

void Proto_PeripheralPowerAck_Unpack(PeripheralPowerAck_t *p, const uint8_t *buf)
{
    uint16_t i = 0u;
    p->powerType = buf[i]; i++;
    p->result = buf[i]; i++;
}

/* PeripheralPowerReq_t: 外设电源控制请求载荷（0x8112） 大端 Pack（返回写入字节数） */
uint16_t Proto_PeripheralPowerReq_Pack(const PeripheralPowerReq_t *p, uint8_t *buf)
{
    uint16_t i = 0u;
    buf[i] = p->powerType; i++;
    buf[i] = p->onOff; i++;
    return i;
}

void Proto_PeripheralPowerReq_Unpack(PeripheralPowerReq_t *p, const uint8_t *buf)
{
    uint16_t i = 0u;
    p->powerType = buf[i]; i++;
    p->onOff = buf[i]; i++;
}

/* PeripheralStatus_t: 外设工作状态（0x8D 0x04） 大端 Pack（返回写入字节数） */
uint16_t Proto_PeripheralStatus_Pack(const PeripheralStatus_t *p, uint8_t *buf)
{
    uint16_t i = 0u;
    buf[i] = p->can1; i++;
    buf[i] = p->can2; i++;
    buf[i] = p->other; i++;
    return i;
}

void Proto_PeripheralStatus_Unpack(PeripheralStatus_t *p, const uint8_t *buf)
{
    uint16_t i = 0u;
    p->can1 = buf[i]; i++;
    p->can2 = buf[i]; i++;
    p->other = buf[i]; i++;
}

/* PowerOffReqResult_t: SoC 睡眠/关机请求的响应（MD 4） 大端 Pack（返回写入字节数） */
uint16_t Proto_PowerOffReqResult_Pack(const PowerOffReqResult_t *p, uint8_t *buf)
{
    uint16_t i = 0u;
    buf[i] = p->powerReqCmd; i++;
    buf[i] = p->result; i++;
    return i;
}

void Proto_PowerOffReqResult_Unpack(PowerOffReqResult_t *p, const uint8_t *buf)
{
    uint16_t i = 0u;
    p->powerReqCmd = buf[i]; i++;
    p->result = buf[i]; i++;
}

/* PowerStateSyncResult_t: SoC 电源状态同步的响应（MD 10） 大端 Pack（返回写入字节数） */
uint16_t Proto_PowerStateSyncResult_Pack(const PowerStateSyncResult_t *p, uint8_t *buf)
{
    uint16_t i = 0u;
    buf[i] = p->powerState; i++;
    buf[i] = p->result; i++;
    return i;
}

void Proto_PowerStateSyncResult_Unpack(PowerStateSyncResult_t *p, const uint8_t *buf)
{
    uint16_t i = 0u;
    p->powerState = buf[i]; i++;
    p->result = buf[i]; i++;
}

/* StrMaxDuration_t: STR 最大维持时长（MD 14） 大端 Pack（返回写入字节数） */
uint16_t Proto_StrMaxDuration_Pack(const StrMaxDuration_t *p, uint8_t *buf)
{
    uint16_t i = 0u;
    buf[i] = p->function; i++;
    buf[i] = p->hours; i++;
    return i;
}

void Proto_StrMaxDuration_Unpack(StrMaxDuration_t *p, const uint8_t *buf)
{
    uint16_t i = 0u;
    p->function = buf[i]; i++;
    p->hours = buf[i]; i++;
}

/* TimeZoneInfo_t: 时区偏移信息（0x0115） 大端 Pack（返回写入字节数） */
uint16_t Proto_TimeZoneInfo_Pack(const TimeZoneInfo_t *p, uint8_t *buf)
{
    uint16_t i = 0u;
    buf[i] = p->sign; i++;
    buf[i] = (uint8_t)(p->offsetSeconds >> 8); i++;
    buf[i] = (uint8_t)(p->offsetSeconds); i++;
    return i;
}

void Proto_TimeZoneInfo_Unpack(TimeZoneInfo_t *p, const uint8_t *buf)
{
    uint16_t i = 0u;
    p->sign = buf[i]; i++;
    p->offsetSeconds = (uint16_t)(((uint16_t)buf[i] << 8) | buf[i + 1u]); i += 2u;
}

/* UpgradeDataPkg_t: 升级包数据（0x0C03） 大端 Pack（返回写入字节数） */
uint16_t Proto_UpgradeDataPkg_Pack(const UpgradeDataPkg_t *p, uint8_t *buf)
{
    uint16_t i = 0u;
    buf[i] = (uint8_t)(p->pkgSeq >> 24); i++;
    buf[i] = (uint8_t)(p->pkgSeq >> 16); i++;
    buf[i] = (uint8_t)(p->pkgSeq >> 8); i++;
    buf[i] = (uint8_t)(p->pkgSeq); i++;
    buf[i] = (uint8_t)(p->dataLen >> 8); i++;
    buf[i] = (uint8_t)(p->dataLen); i++;
    /* upgradeData: 开放尾由调用方追加，此处不写 */
    return i;
}

void Proto_UpgradeDataPkg_Unpack(UpgradeDataPkg_t *p, const uint8_t *buf)
{
    uint16_t i = 0u;
    p->pkgSeq = ((uint32_t)buf[i] << 24) | ((uint32_t)buf[i + 1u] << 16) \
                    | ((uint32_t)buf[i + 2u] << 8) | buf[i + 3u]; i += 4u;
    p->dataLen = (uint16_t)(((uint16_t)buf[i] << 8) | buf[i + 1u]); i += 2u;
    /* upgradeData: 开放尾由调用方按帧长拷贝 */
}

/* UpgradeFileInfo_t: 升级文件信息（0x0C02） 大端 Pack（返回写入字节数） */
uint16_t Proto_UpgradeFileInfo_Pack(const UpgradeFileInfo_t *p, uint8_t *buf)
{
    uint16_t i = 0u;
    buf[i] = (uint8_t)(p->fileSize >> 24); i++;
    buf[i] = (uint8_t)(p->fileSize >> 16); i++;
    buf[i] = (uint8_t)(p->fileSize >> 8); i++;
    buf[i] = (uint8_t)(p->fileSize); i++;
    buf[i] = (uint8_t)(p->frameUpgradeDataLen >> 8); i++;
    buf[i] = (uint8_t)(p->frameUpgradeDataLen); i++;
    buf[i] = (uint8_t)(p->totalPkgNum >> 24); i++;
    buf[i] = (uint8_t)(p->totalPkgNum >> 16); i++;
    buf[i] = (uint8_t)(p->totalPkgNum >> 8); i++;
    buf[i] = (uint8_t)(p->totalPkgNum); i++;
    return i;
}

void Proto_UpgradeFileInfo_Unpack(UpgradeFileInfo_t *p, const uint8_t *buf)
{
    uint16_t i = 0u;
    p->fileSize = ((uint32_t)buf[i] << 24) | ((uint32_t)buf[i + 1u] << 16) \
                    | ((uint32_t)buf[i + 2u] << 8) | buf[i + 3u]; i += 4u;
    p->frameUpgradeDataLen = (uint16_t)(((uint16_t)buf[i] << 8) | buf[i + 1u]); i += 2u;
    p->totalPkgNum = ((uint32_t)buf[i] << 24) | ((uint32_t)buf[i + 1u] << 16) \
                    | ((uint32_t)buf[i + 2u] << 8) | buf[i + 3u]; i += 4u;
}

/* VehicleSignalStatus_t: 车身信号状态（MD 18） 大端 Pack（返回写入字节数） */
uint16_t Proto_VehicleSignalStatus_Pack(const VehicleSignalStatus_t *p, uint8_t *buf)
{
    uint16_t i = 0u;
    buf[i] = p->ignState; i++;
    buf[i] = p->vehicleIgnState; i++;
    return i;
}

void Proto_VehicleSignalStatus_Unpack(VehicleSignalStatus_t *p, const uint8_t *buf)
{
    uint16_t i = 0u;
    p->ignState = buf[i]; i++;
    p->vehicleIgnState = buf[i]; i++;
}

/* VersionInfo_t: 版本查询回复载荷（0x8E01） 大端 Pack（返回写入字节数） */
uint16_t Proto_VersionInfo_Pack(const VersionInfo_t *p, uint8_t *buf)
{
    uint16_t i = 0u;
    buf[i] = p->module; i++;
    buf[i] = p->len; i++;
    /* verArray: 开放尾由调用方追加，此处不写 */
    return i;
}

void Proto_VersionInfo_Unpack(VersionInfo_t *p, const uint8_t *buf)
{
    uint16_t i = 0u;
    p->module = buf[i]; i++;
    p->len = buf[i]; i++;
    /* verArray: 开放尾由调用方按帧长拷贝 */
}

/* 0x0100 PowerOnHandshakeMtd mpuRequestsDataSynchronization:uint8(枚举) NONE（无参） */
void Proto_PowerOnHandshakeMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x0102 HeartbeatSetMtd heartbeatSet:uint8(枚举) IN（入参） */
void Proto_HeartbeatSetMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x0103 HeartbeatReqMtd heartbeatState:uint8(枚举) IN（入参） */
void Proto_HeartbeatReqMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x0105 PowerMgmtReqMtd */
void Proto_PowerMgmtReqMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x0106 StrStateFbMtd strState:uint8(枚举) IN（入参） */
void Proto_StrStateFbMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x0107 BatteryStatusAckEvt result:uint8(枚举) OUT（出参） */
void Proto_BatteryStatusAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x0108 PowerStateSetMtd powerState:uint8(枚举) IN（入参） */
void Proto_PowerStateSetMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x010D EnterStrAckEvt result:uint8(枚举) OUT（出参） */
void Proto_EnterStrAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x010E WakeSocAckEvt result:uint8(枚举) OUT（出参） */
void Proto_WakeSocAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x010F McuRestartReqMtd restartType:uint8(枚举) IN（入参） */
void Proto_McuRestartReqMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x0110 KeyRestartAckEvt keyResult:uint8 OUT（出参） */
void Proto_KeyRestartAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x0111 RtcRestartAckEvt restartResult:uint8 OUT（出参） */
void Proto_RtcRestartAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x0112 SocPowerCtrlAckEvt peripheralPowerAck:struct OUT（出参） */
void Proto_SocPowerCtrlAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x0113 McuPowerCtrlReqMtd mcuPowerReq:struct IN（入参） */
void Proto_McuPowerCtrlReqMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x0114 RtcTimeSetMtd dateTime:struct IN（入参） */
void Proto_RtcTimeSetMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x0115 TimeZoneSetMtd timeZoneInfo:struct IN（入参） */
void Proto_TimeZoneSetMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x0116 SentryModeSetMtd enable:uint8 IN（入参） */
void Proto_SentryModeSetMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x0117 PetModeSetMtd enable:uint8 IN（入参） */
void Proto_PetModeSetMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x0118 BatteryVoltageAckEvt result:uint8(枚举) OUT（出参） */
void Proto_BatteryVoltageAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x0119 VehicleSignalAckEvt result:uint8(枚举) OUT（出参） */
void Proto_VehicleSignalAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x011A HeartbeatLostAckEvt result:uint8(枚举) OUT（出参） */
void Proto_HeartbeatLostAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x011B HeartbeatRecoveredAckEvt result:uint8(枚举) OUT（出参） */
void Proto_HeartbeatRecoveredAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x011C TemperatureAbnormalAckEvt result:uint8(枚举) OUT（出参） */
void Proto_TemperatureAbnormalAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x011E StrDebugSetMtd strMaxDuration:struct IN（入参） */
void Proto_StrDebugSetMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x011F PowerOffReqAckEvt result:uint8(枚举) OUT（出参） */
void Proto_PowerOffReqAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x0801 PowerOffReqMtd powerReqCmd:uint8(枚举) IN（入参） */
void Proto_PowerOffReqMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x0801 SocFanQueryMtd */
void Proto_SocFanQueryMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x0802 SocFanCtrlMtd pwm:uint8 IN（入参） */
void Proto_SocFanCtrlMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x0C00 UpgradeCmdEvt upgradeReqStatus:uint8(枚举) IN（入参） */
void Proto_UpgradeCmdEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x0C02 UpgradeFileInfoRspEvt upgradeFileInfo:struct IN（入参） */
void Proto_UpgradeFileInfoRspEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x0C03 UpgradeDataRspEvt upgradeDataPkg:struct IN（入参） */
void Proto_UpgradeDataRspEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x0D01 TimeQueryMtd dateTime:struct IN（入参） */
void Proto_TimeQueryMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x0D02 TimeSetEvt dateTime:struct IN（入参） */
void Proto_TimeSetEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x0E01 VersionQueryMtd module:uint8(枚举) IN（入参） */
void Proto_VersionQueryMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x8100 HandshakeAckEvt */
void Proto_HandshakeAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x8101 PowerOffReqStatusEvt powerOffReqResult:struct OUT（出参） */
void Proto_PowerOffReqStatusEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x8102 HeartbeatSetStatusEvt heartbeatStatus:uint8(枚举) OUT（出参） */
void Proto_HeartbeatSetStatusEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x8103 HeartbeatFeedbackEvt */
void Proto_HeartbeatFeedbackEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x8105 PowerMgmtStatusEvt powerManageStatus:uint8(枚举) OUT（出参） */
void Proto_PowerMgmtStatusEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x8106 AccStatusEvt accStatus:uint8(枚举) OUT（出参） */
void Proto_AccStatusEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x8107 BatteryStatusEvt batteryStatus:uint8(枚举) OUT（出参） */
void Proto_BatteryStatusEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x8108 PowerStateSetStatusEvt powerStateSyncResult:struct OUT（出参） */
void Proto_PowerStateSetStatusEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x810A AutosarNmModeEvt autosarNmStatus:struct OUT（出参） */
void Proto_AutosarNmModeEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x810B VehicleAntiTheftEvt vehicleAntiTheftSts:uint8(枚举) OUT（出参） */
void Proto_VehicleAntiTheftEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x810C RemoteControlModeEvt remoteControlSt:uint8(枚举) OUT（出参） */
void Proto_RemoteControlModeEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x810D EnterStrEvt */
void Proto_EnterStrEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x810E WakeSocEvt */
void Proto_WakeSocEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x810F McuRestartAckEvt result:uint8(枚举) OUT（出参） */
void Proto_McuRestartAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x8110 KeyRestartReqEvt */
void Proto_KeyRestartReqEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x8111 RtcRestartReqEvt */
void Proto_RtcRestartReqEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x8112 SocPowerCtrlReqEvt peripheralPowerReq:struct IN（入参） */
void Proto_SocPowerCtrlReqEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x8113 McuPowerCtrlAckEvt mcuPowerAck:struct OUT（出参） */
void Proto_McuPowerCtrlAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x8114 RtcTimeSetAckEvt result:uint8(枚举) OUT（出参） */
void Proto_RtcTimeSetAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x8115 TimeZoneSetAckEvt result:uint8(枚举) OUT（出参） */
void Proto_TimeZoneSetAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x8116 SentryModeAckEvt result:uint8(枚举) OUT（出参） */
void Proto_SentryModeAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x8117 PetModeAckEvt result:uint8(枚举) OUT（出参） */
void Proto_PetModeAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x8118 BatteryVoltageEvt voltage:uint16 OUT（出参） */
void Proto_BatteryVoltageEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x8119 VehicleSignalEvt vehicleSignalStatus:struct OUT（出参） */
void Proto_VehicleSignalEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x811A HeartbeatLostEvt */
void Proto_HeartbeatLostEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x811B HeartbeatRecoveredEvt */
void Proto_HeartbeatRecoveredEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x811C TemperatureAbnormalEvt temperatureStatus:uint8(枚举) OUT（出参） */
void Proto_TemperatureAbnormalEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x811D ResetReasonEvt resetReason:uint8 OUT（出参） */
void Proto_ResetReasonEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x811E StrDebugSetStatusEvt strMaxDuration:struct OUT（出参） */
void Proto_StrDebugSetStatusEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x811F PowerOffReqEvt */
void Proto_PowerOffReqEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x8802 SocFanSpeedEvt speed:uint16 OUT（出参） */
void Proto_SocFanSpeedEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x8C01 UpgradeStatusEvt mcuUpgradeStatus:uint8(枚举) OUT（出参） */
void Proto_UpgradeStatusEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x8C02 UpgradeFileInfoReqMtd frameUpgradeDataLen:uint16 OUT（出参） */
void Proto_UpgradeFileInfoReqMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x8C03 UpgradeDataReqMtd pkgSeq:uint32 OUT（出参） */
void Proto_UpgradeDataReqMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x8D01 TimeQueryAckEvt dateTime:struct OUT（出参） */
void Proto_TimeQueryAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x8D02 TimeUploadEvt dateTime:struct OUT（出参） */
void Proto_TimeUploadEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x8E01 VersionQueryAckEvt versionInfo:struct OUT（出参） */
void Proto_VersionQueryAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/*************************************************************************************************
 * End of File
 ************************************************************************************************/
