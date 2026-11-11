/*************************************************************************************************
 * @file    Proto_CmdTable.c
 * @brief   7255 MCU&SOC 协议命令登记表（由 proto-toolkit 从协议表生成，禁止手改）
 * @copyright Copyright (c) 2026, cviauto.com. All rights reserved.
 *
 * 源: 7255 MCU&SOC 通信协议（Bitable Mj3gbU3NqagG4WsPcQgc0YhSnac） rev.4.0.0
 * 统计: RX(SOC→MCU) 34 条 / TX(MCU→SOC) 37 条
 * 说明: 生成表是协议表的机器视图，供比对 App_SocComSysCmd.h 手写清单差异；
 *       仍以手写 X-macro 清单为编译期真源（见 SKILL.md 约束）。
 ************************************************************************************************/
#include "Proto_Types.h"

/* 命令 id 枚举（与 Proto_Enums.h 分离，只含消息 id） */
typedef enum
{
    PROTO_CMD_PowerOnHandshakeMtd = 0x0100,     /* PowerOnHandshakeMtd event event */
    PROTO_CMD_HeartbeatSetMtd = 0x0102,     /* HeartbeatSetMtd method(rr) event */
    PROTO_CMD_HeartbeatReqMtd = 0x0103,     /* HeartbeatReqMtd event Cycle(1000ms) */
    PROTO_CMD_PowerMgmtReqMtd = 0x0105,     /* PowerMgmtReqMtd method(rr) event */
    PROTO_CMD_StrStateFbMtd = 0x0106,     /* StrStateFbMtd event event */
    PROTO_CMD_BatteryStatusAckEvt = 0x0107,     /* BatteryStatusAckEvt event event */
    PROTO_CMD_PowerStateSetMtd = 0x0108,     /* PowerStateSetMtd method(rr) event */
    PROTO_CMD_EnterStrAckEvt = 0x010D,     /* EnterStrAckEvt event event */
    PROTO_CMD_WakeSocAckEvt = 0x010E,     /* WakeSocAckEvt event event */
    PROTO_CMD_McuRestartReqMtd = 0x010F,     /* McuRestartReqMtd method(rr) event */
    PROTO_CMD_KeyRestartAckEvt = 0x0110,     /* KeyRestartAckEvt event event */
    PROTO_CMD_RtcRestartAckEvt = 0x0111,     /* RtcRestartAckEvt event event */
    PROTO_CMD_SocPowerCtrlAckEvt = 0x0112,     /* SocPowerCtrlAckEvt event event */
    PROTO_CMD_McuPowerCtrlReqMtd = 0x0113,     /* McuPowerCtrlReqMtd method(rr) event */
    PROTO_CMD_RtcTimeSetMtd = 0x0114,     /* RtcTimeSetMtd method(rr) event */
    PROTO_CMD_TimeZoneSetMtd = 0x0115,     /* TimeZoneSetMtd method(rr) event */
    PROTO_CMD_SentryModeSetMtd = 0x0116,     /* SentryModeSetMtd method(rr) event */
    PROTO_CMD_PetModeSetMtd = 0x0117,     /* PetModeSetMtd method(rr) event */
    PROTO_CMD_BatteryVoltageAckEvt = 0x0118,     /* BatteryVoltageAckEvt event event */
    PROTO_CMD_VehicleSignalAckEvt = 0x0119,     /* VehicleSignalAckEvt event event */
    PROTO_CMD_HeartbeatLostAckEvt = 0x011A,     /* HeartbeatLostAckEvt event event */
    PROTO_CMD_HeartbeatRecoveredAckEvt = 0x011B,     /* HeartbeatRecoveredAckEvt event event */
    PROTO_CMD_TemperatureAbnormalAckEvt = 0x011C,     /* TemperatureAbnormalAckEvt event event */
    PROTO_CMD_StrDebugSetMtd = 0x011E,     /* StrDebugSetMtd method(rr) event */
    PROTO_CMD_PowerOffReqAckEvt = 0x011F,     /* PowerOffReqAckEvt event event */
    PROTO_CMD_PowerOffReqMtd = 0x0801,     /* PowerOffReqMtd method(rr) event */
    PROTO_CMD_SocFanQueryMtd = 0x0801,     /* SocFanQueryMtd method(rr) event */
    PROTO_CMD_SocFanCtrlMtd = 0x0802,     /* SocFanCtrlMtd method(rr) event */
    PROTO_CMD_UpgradeCmdEvt = 0x0C00,     /* UpgradeCmdEvt event event */
    PROTO_CMD_UpgradeFileInfoRspEvt = 0x0C02,     /* UpgradeFileInfoRspEvt event event */
    PROTO_CMD_UpgradeDataRspEvt = 0x0C03,     /* UpgradeDataRspEvt event event */
    PROTO_CMD_TimeQueryMtd = 0x0D01,     /* TimeQueryMtd method(rr) event */
    PROTO_CMD_TimeSetEvt = 0x0D02,     /* TimeSetEvt event event */
    PROTO_CMD_VersionQueryMtd = 0x0E01,     /* VersionQueryMtd method(rr) event */
    PROTO_CMD_HandshakeAckEvt = 0x8100,     /* HandshakeAckEvt event event */
    PROTO_CMD_PowerOffReqStatusEvt = 0x8101,     /* PowerOffReqStatusEvt event event */
    PROTO_CMD_HeartbeatSetStatusEvt = 0x8102,     /* HeartbeatSetStatusEvt method(rr) event */
    PROTO_CMD_HeartbeatFeedbackEvt = 0x8103,     /* HeartbeatFeedbackEvt event event */
    PROTO_CMD_PowerMgmtStatusEvt = 0x8105,     /* PowerMgmtStatusEvt method(rr) event */
    PROTO_CMD_AccStatusEvt = 0x8106,     /* AccStatusEvt event event */
    PROTO_CMD_BatteryStatusEvt = 0x8107,     /* BatteryStatusEvt method(rr) event */
    PROTO_CMD_PowerStateSetStatusEvt = 0x8108,     /* PowerStateSetStatusEvt event event */
    PROTO_CMD_AutosarNmModeEvt = 0x810A,     /* AutosarNmModeEvt event event */
    PROTO_CMD_VehicleAntiTheftEvt = 0x810B,     /* VehicleAntiTheftEvt event event */
    PROTO_CMD_RemoteControlModeEvt = 0x810C,     /* RemoteControlModeEvt event event */
    PROTO_CMD_EnterStrEvt = 0x810D,     /* EnterStrEvt method(rr) event */
    PROTO_CMD_WakeSocEvt = 0x810E,     /* WakeSocEvt method(rr) event */
    PROTO_CMD_McuRestartAckEvt = 0x810F,     /* McuRestartAckEvt event event */
    PROTO_CMD_KeyRestartReqEvt = 0x8110,     /* KeyRestartReqEvt method(rr) event */
    PROTO_CMD_RtcRestartReqEvt = 0x8111,     /* RtcRestartReqEvt method(rr) event */
    PROTO_CMD_SocPowerCtrlReqEvt = 0x8112,     /* SocPowerCtrlReqEvt method(rr) event */
    PROTO_CMD_McuPowerCtrlAckEvt = 0x8113,     /* McuPowerCtrlAckEvt event event */
    PROTO_CMD_RtcTimeSetAckEvt = 0x8114,     /* RtcTimeSetAckEvt event event */
    PROTO_CMD_TimeZoneSetAckEvt = 0x8115,     /* TimeZoneSetAckEvt event event */
    PROTO_CMD_SentryModeAckEvt = 0x8116,     /* SentryModeAckEvt event event */
    PROTO_CMD_PetModeAckEvt = 0x8117,     /* PetModeAckEvt event event */
    PROTO_CMD_BatteryVoltageEvt = 0x8118,     /* BatteryVoltageEvt method(rr) event */
    PROTO_CMD_VehicleSignalEvt = 0x8119,     /* VehicleSignalEvt method(rr) event */
    PROTO_CMD_HeartbeatLostEvt = 0x811A,     /* HeartbeatLostEvt method(rr) event */
    PROTO_CMD_HeartbeatRecoveredEvt = 0x811B,     /* HeartbeatRecoveredEvt method(rr) event */
    PROTO_CMD_TemperatureAbnormalEvt = 0x811C,     /* TemperatureAbnormalEvt method(rr) event */
    PROTO_CMD_ResetReasonEvt = 0x811D,     /* ResetReasonEvt event event */
    PROTO_CMD_StrDebugSetStatusEvt = 0x811E,     /* StrDebugSetStatusEvt event event */
    PROTO_CMD_PowerOffReqEvt = 0x811F,     /* PowerOffReqEvt method(rr) event */
    PROTO_CMD_SocFanSpeedEvt = 0x8802,     /* SocFanSpeedEvt event event */
    PROTO_CMD_UpgradeStatusEvt = 0x8C01,     /* UpgradeStatusEvt event event */
    PROTO_CMD_UpgradeFileInfoReqMtd = 0x8C02,     /* UpgradeFileInfoReqMtd method(rr) event */
    PROTO_CMD_UpgradeDataReqMtd = 0x8C03,     /* UpgradeDataReqMtd method(rr) event */
    PROTO_CMD_TimeQueryAckEvt = 0x8D01,     /* TimeQueryAckEvt event event */
    PROTO_CMD_TimeUploadEvt = 0x8D02,     /* TimeUploadEvt event Cycle(60000ms) */
    PROTO_CMD_VersionQueryAckEvt = 0x8E01,     /* VersionQueryAckEvt event event */
}PROTO_CMD_Id_t;

typedef struct
{
    uint16_t cmd;
    void (*handler)(uint8_t channel, const uint8_t *pdata, uint16_t len);
}Proto_CmdEntry_t;

/* RX：SOC → MCU 下发/请求 */
const Proto_CmdEntry_t Proto_RxCmdTable[] =
{
    { 0x0100u, Proto_PowerOnHandshakeMtd_Fun },      /* PowerOnHandshakeMtd */
    { 0x0102u, Proto_HeartbeatSetMtd_Fun },      /* HeartbeatSetMtd */
    { 0x0103u, Proto_HeartbeatReqMtd_Fun },      /* HeartbeatReqMtd */
    { 0x0105u, Proto_PowerMgmtReqMtd_Fun },      /* PowerMgmtReqMtd */
    { 0x0106u, Proto_StrStateFbMtd_Fun },      /* StrStateFbMtd */
    { 0x0107u, Proto_BatteryStatusAckEvt_Fun },      /* BatteryStatusAckEvt */
    { 0x0108u, Proto_PowerStateSetMtd_Fun },      /* PowerStateSetMtd */
    { 0x010Du, Proto_EnterStrAckEvt_Fun },      /* EnterStrAckEvt */
    { 0x010Eu, Proto_WakeSocAckEvt_Fun },      /* WakeSocAckEvt */
    { 0x010Fu, Proto_McuRestartReqMtd_Fun },      /* McuRestartReqMtd */
    { 0x0110u, Proto_KeyRestartAckEvt_Fun },      /* KeyRestartAckEvt */
    { 0x0111u, Proto_RtcRestartAckEvt_Fun },      /* RtcRestartAckEvt */
    { 0x0112u, Proto_SocPowerCtrlAckEvt_Fun },      /* SocPowerCtrlAckEvt */
    { 0x0113u, Proto_McuPowerCtrlReqMtd_Fun },      /* McuPowerCtrlReqMtd */
    { 0x0114u, Proto_RtcTimeSetMtd_Fun },      /* RtcTimeSetMtd */
    { 0x0115u, Proto_TimeZoneSetMtd_Fun },      /* TimeZoneSetMtd */
    { 0x0116u, Proto_SentryModeSetMtd_Fun },      /* SentryModeSetMtd */
    { 0x0117u, Proto_PetModeSetMtd_Fun },      /* PetModeSetMtd */
    { 0x0118u, Proto_BatteryVoltageAckEvt_Fun },      /* BatteryVoltageAckEvt */
    { 0x0119u, Proto_VehicleSignalAckEvt_Fun },      /* VehicleSignalAckEvt */
    { 0x011Au, Proto_HeartbeatLostAckEvt_Fun },      /* HeartbeatLostAckEvt */
    { 0x011Bu, Proto_HeartbeatRecoveredAckEvt_Fun },      /* HeartbeatRecoveredAckEvt */
    { 0x011Cu, Proto_TemperatureAbnormalAckEvt_Fun },      /* TemperatureAbnormalAckEvt */
    { 0x011Eu, Proto_StrDebugSetMtd_Fun },      /* StrDebugSetMtd */
    { 0x011Fu, Proto_PowerOffReqAckEvt_Fun },      /* PowerOffReqAckEvt */
    { 0x0801u, Proto_PowerOffReqMtd_Fun },      /* PowerOffReqMtd */
    { 0x0801u, Proto_SocFanQueryMtd_Fun },      /* SocFanQueryMtd */
    { 0x0802u, Proto_SocFanCtrlMtd_Fun },      /* SocFanCtrlMtd */
    { 0x0C00u, Proto_UpgradeCmdEvt_Fun },      /* UpgradeCmdEvt */
    { 0x0C02u, Proto_UpgradeFileInfoRspEvt_Fun },      /* UpgradeFileInfoRspEvt */
    { 0x0C03u, Proto_UpgradeDataRspEvt_Fun },      /* UpgradeDataRspEvt */
    { 0x0D01u, Proto_TimeQueryMtd_Fun },      /* TimeQueryMtd */
    { 0x0D02u, Proto_TimeSetEvt_Fun },      /* TimeSetEvt */
    { 0x0E01u, Proto_VersionQueryMtd_Fun },      /* VersionQueryMtd */
    { 0xFFFFu, NULL }
};

/* TX：MCU → SOC 上报/应答 */
const Proto_CmdEntry_t Proto_TxCmdTable[] =
{
    { 0x8100u, Proto_HandshakeAckEvt_Fun },      /* HandshakeAckEvt */
    { 0x8101u, Proto_PowerOffReqStatusEvt_Fun },      /* PowerOffReqStatusEvt */
    { 0x8102u, Proto_HeartbeatSetStatusEvt_Fun },      /* HeartbeatSetStatusEvt */
    { 0x8103u, Proto_HeartbeatFeedbackEvt_Fun },      /* HeartbeatFeedbackEvt */
    { 0x8105u, Proto_PowerMgmtStatusEvt_Fun },      /* PowerMgmtStatusEvt */
    { 0x8106u, Proto_AccStatusEvt_Fun },      /* AccStatusEvt */
    { 0x8107u, Proto_BatteryStatusEvt_Fun },      /* BatteryStatusEvt */
    { 0x8108u, Proto_PowerStateSetStatusEvt_Fun },      /* PowerStateSetStatusEvt */
    { 0x810Au, Proto_AutosarNmModeEvt_Fun },      /* AutosarNmModeEvt */
    { 0x810Bu, Proto_VehicleAntiTheftEvt_Fun },      /* VehicleAntiTheftEvt */
    { 0x810Cu, Proto_RemoteControlModeEvt_Fun },      /* RemoteControlModeEvt */
    { 0x810Du, Proto_EnterStrEvt_Fun },      /* EnterStrEvt */
    { 0x810Eu, Proto_WakeSocEvt_Fun },      /* WakeSocEvt */
    { 0x810Fu, Proto_McuRestartAckEvt_Fun },      /* McuRestartAckEvt */
    { 0x8110u, Proto_KeyRestartReqEvt_Fun },      /* KeyRestartReqEvt */
    { 0x8111u, Proto_RtcRestartReqEvt_Fun },      /* RtcRestartReqEvt */
    { 0x8112u, Proto_SocPowerCtrlReqEvt_Fun },      /* SocPowerCtrlReqEvt */
    { 0x8113u, Proto_McuPowerCtrlAckEvt_Fun },      /* McuPowerCtrlAckEvt */
    { 0x8114u, Proto_RtcTimeSetAckEvt_Fun },      /* RtcTimeSetAckEvt */
    { 0x8115u, Proto_TimeZoneSetAckEvt_Fun },      /* TimeZoneSetAckEvt */
    { 0x8116u, Proto_SentryModeAckEvt_Fun },      /* SentryModeAckEvt */
    { 0x8117u, Proto_PetModeAckEvt_Fun },      /* PetModeAckEvt */
    { 0x8118u, Proto_BatteryVoltageEvt_Fun },      /* BatteryVoltageEvt */
    { 0x8119u, Proto_VehicleSignalEvt_Fun },      /* VehicleSignalEvt */
    { 0x811Au, Proto_HeartbeatLostEvt_Fun },      /* HeartbeatLostEvt */
    { 0x811Bu, Proto_HeartbeatRecoveredEvt_Fun },      /* HeartbeatRecoveredEvt */
    { 0x811Cu, Proto_TemperatureAbnormalEvt_Fun },      /* TemperatureAbnormalEvt */
    { 0x811Du, Proto_ResetReasonEvt_Fun },      /* ResetReasonEvt */
    { 0x811Eu, Proto_StrDebugSetStatusEvt_Fun },      /* StrDebugSetStatusEvt */
    { 0x811Fu, Proto_PowerOffReqEvt_Fun },      /* PowerOffReqEvt */
    { 0x8802u, Proto_SocFanSpeedEvt_Fun },      /* SocFanSpeedEvt */
    { 0x8C01u, Proto_UpgradeStatusEvt_Fun },      /* UpgradeStatusEvt */
    { 0x8C02u, Proto_UpgradeFileInfoReqMtd_Fun },      /* UpgradeFileInfoReqMtd */
    { 0x8C03u, Proto_UpgradeDataReqMtd_Fun },      /* UpgradeDataReqMtd */
    { 0x8D01u, Proto_TimeQueryAckEvt_Fun },      /* TimeQueryAckEvt */
    { 0x8D02u, Proto_TimeUploadEvt_Fun },      /* TimeUploadEvt */
    { 0x8E01u, Proto_VersionQueryAckEvt_Fun },      /* VersionQueryAckEvt */
    { 0xFFFFu, NULL }
};
/*************************************************************************************************
 * End of File
 ************************************************************************************************/
