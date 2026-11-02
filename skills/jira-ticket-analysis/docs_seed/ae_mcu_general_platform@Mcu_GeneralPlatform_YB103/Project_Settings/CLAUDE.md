# Project_Settings — 启动代码与镜像签名(NXP RTD 样例 startup + HSE 应用签名流水线)

## Commands
| Command | Description |
|---------|-------------|
| `cd Project_Settings/mcu_signature_YB103 && sh signature.sh` | 签名流水线:mcu_s.bin → BL 填充 700K → boot.pem 签名 → sw.pem 签头 → hse_app_signed.bin;必须在 mcu_signature_YB103/ 内执行 |
| `py make_header_file.py -type MCU -file hse_app.bin -VID 1 -ver <版本串> -out hse_app_header -offset 1024` | 生成 68 字节 CVIA 头(含 SHA-256);signature.sh 内部即用此命令 |

## Architecture
```
Project_Settings/
  Startup_Code/         # NXP RTD 3.0.0 官方样例启动代码(S32K3/CM7),随主工程编译进镜像
  mcu_signature_YB103/  # 离线签名工具(openssl + python),不参与固件编译
```

## Key Files
- `Startup_Code/startup_cm7.s` - Reset_Handler 全流程 + .boot_header(SBAF 标记 0x5AA55AA5、各核使能位与 VTOR)+ .init_table/.zero_table(拷贝/清零表)
- `Startup_Code/Vector_Table.s` - ROM 中断向量表(.intc_vector):16 项内核异常 + 242 项 IRQ(全部默认 undefined_handler)
- `Startup_Code/exceptions.c` - 异常默认实现(weak 死循环);定义 MCAL_ENABLE_USER_MODE_SUPPORT 时 SVC_Handler 用汇编实现用户/管理模式切换(svc 0-3)
- `Startup_Code/startup.c` - init_data_bss():按 __INIT_TABLE 拷 .data、按 __ZERO_TABLE 清 .bss;init_data_bss_core2() 从 __INDEX_COPY_CORE2 起拷(副核)
- `Startup_Code/system.c` - SystemInit():MSCM 中断路由、FPU 使能、MPU 15 区域(属性按衍生型号条件编译)、Cache 使能;sys_m7_standbysram_init() 按复位原因决定是否清 standby SRAM
- `Startup_Code/nvic.c` - NVIC 封装:使能/禁用 IRQ、设优先级(4 位)
- `mcu_signature_YB103/make_header_file.py` - CVIA 头:magic 0x41495643、swType(MCU=1)、大小/offset/VID/版本串 + SHA-256;只写头不拷贝负载
- `mcu_signature_YB103/signature.sh` - 完整签名链:dd 填充 → openssl 签名 → 头+签名拼接,产出 hse_app_signed.bin(702K)

## Gotchas
- 向量表运行期在 RAM:启动后 VTOR 指向 __RAM_INTERRUPT_START,ROM 表经 init_table 拷入;新增中断要接 RAM 表/IntController 配置,只改 Vector_Table.s 默认项不一定生效
- 默认异常处理全是 while(TRUE) 死循环(HardFault/SysTick/PendSV…),相应驱动或 RTOS 接管前触发即挂死
- 非上电复位(POR)时 SRAM 从 __BSS_SRAM_START 起清,standby 区保留;sys_m7_standbysram_init 对软复位/HSE SWT 复位也跳过清零
- 仅主核关 SWT0 看门狗(0xC520/0xD928 解锁后写 0xFF000040);SWT1 不在此关(其时钟上电即关);副核(CORE1/2/3)跳过 MSCM 时钟初始化
- Cortex-M7 投机访问约束:MPU 必须先于 Cache 使能;-DDISABLE_DEBUGGER_TRAP 可去掉复位后等调试器挂接的 100 次延时循环
- signature.sh 依赖当前目录下的 mcu_s.bin、boot.pem、sw.pem(相对路径),只能在 mcu_signature_YB103/ 内跑;Windows 依赖 py 启动器
- 头文件版本串最长 15 字符,超长直接退出;向量表中 Reset_Handler/SVC_Handler 入口带 +1(Thumb 位)
