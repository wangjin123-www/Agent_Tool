/*************************************************************************************************
 * @file    Proto_CmdStub.c
 * @brief   7255 MCU&SOC 协议命令处理桩 + Pack/Unpack 实现（由 proto-toolkit 生成，禁止手改）
 * @copyright Copyright (c) 2026, cviauto.com. All rights reserved.
 *
 * 源: 7255 MCU&SOC 通信协议表 rev.1144
 * 集成: 参考实现落点。真实现接入后，用 <名>_Fun 同名函数替换桩体即可（表不用改）。
 ************************************************************************************************/
#include "Proto_Types.h"
#include <string.h>

/* UpgradeFileInfo: 升级文件信息（0x0C02） 大端 Pack（返回写入字节数） */
uint16_t Proto_UpgradeFileInfo_Pack(const Proto_UpgradeFileInfo *p, uint8_t *buf)
{
    uint16_t i = 0u;
    buf[i] = (uint8_t)(p->file_size >> 24); i++;
    buf[i] = (uint8_t)(p->file_size >> 16); i++;
    buf[i] = (uint8_t)(p->file_size >> 8); i++;
    buf[i] = (uint8_t)(p->file_size); i++;
    buf[i] = (uint8_t)(p->frame_upgrade_data_len >> 8); i++;
    buf[i] = (uint8_t)(p->frame_upgrade_data_len); i++;
    buf[i] = (uint8_t)(p->total_pkg_num >> 24); i++;
    buf[i] = (uint8_t)(p->total_pkg_num >> 16); i++;
    buf[i] = (uint8_t)(p->total_pkg_num >> 8); i++;
    buf[i] = (uint8_t)(p->total_pkg_num); i++;
    return i;
}

void Proto_UpgradeFileInfo_Unpack(Proto_UpgradeFileInfo *p, const uint8_t *buf)
{
    uint16_t i = 0u;
    p->file_size = ((uint32_t)buf[i] << 24) | ((uint32_t)buf[i + 1u] << 16) \
                    | ((uint32_t)buf[i + 2u] << 8) | buf[i + 3u]; i += 4u;
    p->frame_upgrade_data_len = (uint16_t)(((uint16_t)buf[i] << 8) | buf[i + 1u]); i += 2u;
    p->total_pkg_num = ((uint32_t)buf[i] << 24) | ((uint32_t)buf[i + 1u] << 16) \
                    | ((uint32_t)buf[i + 2u] << 8) | buf[i + 3u]; i += 4u;
}

/* UpgradeDataPkg: 升级包数据（0x0C03） 大端 Pack（返回写入字节数） */
uint16_t Proto_UpgradeDataPkg_Pack(const Proto_UpgradeDataPkg *p, uint8_t *buf)
{
    uint16_t i = 0u;
    buf[i] = (uint8_t)(p->pkg_seq >> 24); i++;
    buf[i] = (uint8_t)(p->pkg_seq >> 16); i++;
    buf[i] = (uint8_t)(p->pkg_seq >> 8); i++;
    buf[i] = (uint8_t)(p->pkg_seq); i++;
    /* upgrade_data: 开放尾由调用方追加，此处不写 */
    return i;
}

void Proto_UpgradeDataPkg_Unpack(Proto_UpgradeDataPkg *p, const uint8_t *buf)
{
    uint16_t i = 0u;
    p->pkg_seq = ((uint32_t)buf[i] << 24) | ((uint32_t)buf[i + 1u] << 16) \
                    | ((uint32_t)buf[i + 2u] << 8) | buf[i + 3u]; i += 4u;
    /* upgrade_data: 开放尾由调用方按帧长拷贝 */
}

/* 0x0100 PowerOnHandshakeMtd MPURequestsDataSynchronization:uint8 NONE */
void Proto_PowerOnHandshakeMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x0101 PowerOffReqMtd PowerReqCmd:uint8 IN */
void Proto_PowerOffReqMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x0102 HeartbeatSetMtd HeartbeatSet:uint8 IN */
void Proto_HeartbeatSetMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x0103 HeartbeatReqMtd HeartbeatState:uint8 IN */
void Proto_HeartbeatReqMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x0105 PowerMgmtReqMtd */
void Proto_PowerMgmtReqMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x0106 StrStateFbMtd STRState:uint8 IN */
void Proto_StrStateFbMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x011E StrDebugSetMtd StrMaxDuration:struct IN */
void Proto_StrDebugSetMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x0108 PowerStateSetMtd powerState:uint8 IN */
void Proto_PowerStateSetMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x011F PowerOffReqAckEvt result:uint8 OUT */
void Proto_PowerOffReqAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x0107 BatteryStatusAckEvt result:uint8 OUT */
void Proto_BatteryStatusAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x010D EnterStrAckEvt result:uint8 OUT */
void Proto_EnterStrAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x010E WakeSocAckEvt result:uint8 OUT */
void Proto_WakeSocAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x010F McuRestartReqMtd restartType:uint8 IN */
void Proto_McuRestartReqMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x0110 KeyRestartAckEvt keyResult:uint8 OUT */
void Proto_KeyRestartAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x0111 RtcRestartAckEvt restartResult:uint8 OUT */
void Proto_RtcRestartAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x0112 SocPowerCtrlAckEvt PeripheralPowerAck:struct OUT */
void Proto_SocPowerCtrlAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x0113 McuPowerCtrlReqMtd McuPowerReq:struct IN */
void Proto_McuPowerCtrlReqMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x0114 RtcTimeSetMtd DateTime:struct IN */
void Proto_RtcTimeSetMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x0115 TimeZoneSetMtd TimeZoneInfo:struct IN */
void Proto_TimeZoneSetMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x0116 SentryModeSetMtd enable:uint8 IN */
void Proto_SentryModeSetMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x0117 PetModeSetMtd enable:uint8 IN */
void Proto_PetModeSetMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x0118 BatteryVoltageAckEvt result:uint8 OUT */
void Proto_BatteryVoltageAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x0119 VehicleSignalAckEvt result:uint8 OUT */
void Proto_VehicleSignalAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x011A HeartbeatLostAckEvt result:uint8 OUT */
void Proto_HeartbeatLostAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x011B HeartbeatRecoveredAckEvt result:uint8 OUT */
void Proto_HeartbeatRecoveredAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x011C TemperatureAbnormalAckEvt result:uint8 OUT */
void Proto_TemperatureAbnormalAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x0801 SocFanQueryMtd */
void Proto_SocFanQueryMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x0802 SocFanCtrlMtd pwm:uint8 IN */
void Proto_SocFanCtrlMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x0C00 UpgradeCmdEvt UpgradeReqStatus:uint8 IN */
void Proto_UpgradeCmdEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x0C02 UpgradeFileInfoRspEvt UpgradeFileInfo:struct IN */
void Proto_UpgradeFileInfoRspEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x0C03 UpgradeDataRspEvt UpgradeDataPkg:struct IN */
void Proto_UpgradeDataRspEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x8100 HandshakeAckEvt */
void Proto_HandshakeAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x811F PowerOffReqEvt */
void Proto_PowerOffReqEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x8102 HeartbeatSetStatusEvt HeartbeatStatus:uint8 OUT */
void Proto_HeartbeatSetStatusEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x8103 HeartbeatFeedbackEvt */
void Proto_HeartbeatFeedbackEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x8105 PowerMgmtStatusEvt PowerManageStatus:uint8 OUT */
void Proto_PowerMgmtStatusEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x8106 AccStatusEvt ACC_Status:uint8 OUT */
void Proto_AccStatusEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x8107 BatteryStatusEvt batteryStatus:uint8 OUT */
void Proto_BatteryStatusEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x811D ResetReasonEvt ResetReason:uint8 OUT */
void Proto_ResetReasonEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x810A AutosarNmModeEvt AutosarNmStatus:struct OUT */
void Proto_AutosarNmModeEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x810B VehicleAntiTheftEvt VehicleAntiCurrentSts:uint8 OUT */
void Proto_VehicleAntiTheftEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x810C RemoteControlModeEvt RemoteControlSt:uint8 OUT */
void Proto_RemoteControlModeEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x8101 PowerOffReqStatusEvt PowerOffReqResult:struct OUT */
void Proto_PowerOffReqStatusEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x8108 PowerStateSetStatusEvt PowerStateSyncResult:struct OUT */
void Proto_PowerStateSetStatusEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x811E StrDebugSetStatusEvt StrMaxDuration:struct OUT */
void Proto_StrDebugSetStatusEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
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
/* 0x810F McuRestartAckEvt result:uint8 OUT */
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
/* 0x8112 SocPowerCtrlReqEvt PeripheralPowerReq:struct IN */
void Proto_SocPowerCtrlReqEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x8113 McuPowerCtrlAckEvt McuPowerAck:struct OUT */
void Proto_McuPowerCtrlAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x8114 RtcTimeSetAckEvt result:uint8 OUT */
void Proto_RtcTimeSetAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x8115 TimeZoneSetAckEvt result:uint8 OUT */
void Proto_TimeZoneSetAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x8116 SentryModeAckEvt result:uint8 OUT */
void Proto_SentryModeAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x8117 PetModeAckEvt result:uint8 OUT */
void Proto_PetModeAckEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x8118 BatteryVoltageEvt voltage:uint16 OUT */
void Proto_BatteryVoltageEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x8119 VehicleSignalEvt VehicleSignalStatus:struct OUT */
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
/* 0x811C TemperatureAbnormalEvt temperatureStatus:uint8 OUT */
void Proto_TemperatureAbnormalEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x8802 SocFanSpeedEvt speed:uint16 OUT */
void Proto_SocFanSpeedEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x8C01 UpgradeStatusEvt MCUUpgradeStatus:uint8 OUT */
void Proto_UpgradeStatusEvt_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x8C02 UpgradeFileInfoReqMtd */
void Proto_UpgradeFileInfoReqMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/* 0x8C03 UpgradeDataReqMtd PkgSeq:uint32 OUT */
void Proto_UpgradeDataReqMtd_Fun(uint8_t channel, const uint8_t *pdata, uint16_t len)
{
    (void)channel; (void)pdata; (void)len;    /* TODO: 接入真实现 */
}
/*************************************************************************************************
 * End of File
 ************************************************************************************************/
