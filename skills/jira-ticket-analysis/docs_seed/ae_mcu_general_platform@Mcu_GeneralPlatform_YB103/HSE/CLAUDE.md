# HSE(NXP 硬件安全引擎的 Host 侧驱动与安全安装器示例,S32K3/HSE-B)

通过 MU(Message Unit)向 HSE 固件(v2.40.0)发起服务请求的 host 驱动,外加一套生命周期/密钥/安全引导的安装器示例。全部源码在 `HSE_SRC/` 单层目录(37 .c + 79 .h),随根工程整体编译,本目录无独立构建命令。

## Architecture
```
HSE/HSE_SRC/          # 唯一子目录,按文件名前缀分四类:
  hse_host_*          # Host 驱动层:hse_host.c/h 是核心(HSE_Send/HSE_GetFreeChannel),
                      # 其余 hse_host_<svc>.c/h 为逐服务封装(mac/hash/cipher/ecc/sign/rng/kdf/key...)
  hse_srv_*           # 各服务组的请求/响应类型定义(填充 hseSrvDescriptor_t 联合体成员用)
  hse_*config*        # 平台与特性裁剪:hse_target.h(平台=S32K3X2)、hse_platform.h(S32K3→HSE_B)、
                      # hse_b_config.h(HSE-B 特性集:2 MU×4 通道、SMR/密钥库尺寸上限)
  无前缀 .c           # 安装器/示例层:demo_app_services.h 是入口声明(HSE_Config/HSE_Crypto/
                      # SecureBoot/生命周期/ADKP);host_flash.c+utest.c 负责闪存与 UTEST DCF 写入
```

## Key Files
- `HSE_SRC/hse_host.h` - 对外总入口:HSE_Send、HSE_GetFreeChannel、状态查询、GPI 回调注册
- `HSE_SRC/hse_interface.h` - hseSrvDescriptor_t 与全部服务 ID/请求类型(服务调用的依据)
- `HSE_SRC/hse_b_config.h` - S32K3(HSE_B)生效的特性裁剪:MU/通道数、密钥库与 SMR 容量
- `HSE_SRC/hse_target.h` - 平台选择(HSE_S32K3X2)与 HSE 固件版本(2.40.0),升级固件需同步
- `HSE_SRC/demo_app_services.h` - 安装器示例 API + IVT/UTEST/Flash 块地址常量(BLOCK0 从 0x00400000)
- `HSE_SRC/hse_status_and_errors.h` - HSE_SRV_RSP_* 错误码(判断各服务返回值)

## Gotchas
- 服务描述符必须放 DTCM:hse_host.c 将 hseSrvDescMu0/1 放入链接段 `._HseSrvDesc`(HSE_USE_DTCM=1),
  HSE_Send 对地址做 +0x1000000 平移(HSE_DTCM_ADDR);链接脚本须保留该段,勿随意改 HSE_USE_DTCM。
- 本目录的外部依赖不在本目录:代码 include 的 `Hse_Ip.h`(RTD HSE 驱动,HSE_Send 最终调
  Hse_Ip_ServiceRequest)、`Mcal.h`、`Crypto_MemMap.h`(约 24 处 MemMap 分段宏)、`OsIf_Cfg.h`
  均由根工程 RTD/ 提供包含路径;OsIf.h 是 RTD(S32K3_RTD_1_0_0_HF02)的拷贝,勿两处同时修改。
- 头注释里的 @file 不可信(复制粘贴残留):hse_boot_auth.c、hse_advance_LC.c、hse_debug_key.c、
  hse_debug_auth_mode.c、hse_extend_cust_security_policy.c 的 @file 都写成 hse_fuses.c;以文件名为准。
- 通道 0 为管理服务保留,HSE_GetFreeChannel 只返回 1..4(每 MU 4 通道,S32K3 共 2 个 MU 实例)。
- 生命周期/熔丝/ADKP 流程(hse_advance_LC.c、hse_boot_auth.c、hse_debug_key.c 等)会烧写 UTEST DCF
  记录且不可逆;LOCKSTEP_EN(demo_app_services.h,默认 1)决定 DCF 数据字的核模式。
