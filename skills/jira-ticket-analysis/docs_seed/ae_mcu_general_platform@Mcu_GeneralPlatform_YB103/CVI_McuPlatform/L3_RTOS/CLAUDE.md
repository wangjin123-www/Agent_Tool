# L3_RTOS(RTOS 层:FreeRTOS V10.6.0 内核 + 项目自研 OS 包装抽象,附无 OS 协作调度备选)

## Commands
| Command | Description |
|---------|-------------|
| (无模块级命令) | 本模块随仓库根 S32DS Eclipse 工程(`.cproject`/`.project`)整体构建,无独立脚本;OS 配置由 `generate/include/FreeRTOSConfig.h` 提供(`configTICK_RATE_HZ=1000`,tick 即 ms) |

## Architecture
```
CVI_McuPlatform/L3_RTOS/
  OS1_FreeRTOS/
    Source/                      # FreeRTOS V10.6.0 上游内核(tasks/queue/timers/list/event_groups/stream_buffer)
      portable/GCC/ARM_CM7/r0p1/ # Cortex-M7 port(S32K312)
      portable/MemMang/heap_4.c  # heap_4 内存管理(唯一堆)
    Os1_UpInf/                   # 项目自研 FreeRTOS 包装:Os1If_UpInf 函数指针表 + OsIf_* 实现
  OS2_TmrSched/
    Sched_Impl/                  # BareTask 无 OS 协作式调度器(轮询 READY 状态机)
    Os2_UpInf/                   # 与 Os1 同构的 Os2If_UpInf 函数指针表(能力子集)
```
- 上层(L2_Tasks)只依赖 `Os1If_UpInf`/`Os2If_UpInf` 两个函数指针表实现 OS 切换;E_TASK_OS 任务枚举与消息结构定义在 `CVI_McuPlatform/L6_Public/Public_TypeDef/Os_TypeDef.h`。

## Key Files
- `OS1_FreeRTOS/Os1_UpInf/Os1If_UpInf.c` - Os1 唯一上层入口;`Os1If_CreateTask` = xTaskCreate + 自动创建并启动同 id 周期软件定时器(回调转调传入的 pTimerCallback)
- `OS1_FreeRTOS/Os1_UpInf/OsIf_Task.h/.c` - task_id→名称/栈/优先级表 `TaskInfo_Group`;优先级枚举(TASK9=IDLE+1 最低 → PWR=IDLE+10 最高);栈深宏单位是 word(已 ÷4)
- `OS1_FreeRTOS/Os1_UpInf/OsIf_Msg.h/.c` - 每任务一个队列:深度 8 × `STRUCT_TASK_BASE_MSG`(msg_id/msg_addr/msg_len);收发等待时间宏均为 0(不阻塞)
- `OS1_FreeRTOS/Os1_UpInf/OsIf_Lock.c` - 全部锁共用一个全局 EventGroup(LOCK_BITS_MAX=10 位,位=1 空闲;WaitLock 先 0-tick 轮询再 portMAX_DELAY 死等)
- `OS1_FreeRTOS/Os1_UpInf/OsIf_SwTimer.c` - Task0..9 定时器回调桥接表;任务主函数周期由软件定时器驱动(周期表 `TASKx_TIMER_PERIOD` 在 L6_Public)
- `OS1_FreeRTOS/Os1_UpInf/OsIf_Queue.c` - 通用队列包装(句柄直传,与 Msg 的按 id 队列并存)
- `OS2_TmrSched/Sched_Impl/BareTask.c` - 协作调度核心:`BareTask_TickHandle()`(外部周期调用)递减计数置 READY,`StartScheduler` = while(1) 轮询 Main/Evt/Msg 三路;周期表内嵌本文件(Pwr 5/Can 5/Soc 10/Mem 10/Misc 50ms,其余 Reserved 不跑)

## Gotchas
- 换 OS 时任务表错位:同一 task_id 在 `TaskInfo_Group`(Os1:3=Ip1,4=Ip2,5=Mem,6=Misc)与 `BareTask_MainSchedCfg`(Os2:3=Mem,4=Misc,5..9=Reserved)语义不同,两表必须一起改。
- Os2 能力是子集:Lock 接口全为 NULL;`Os2If_DelayMs` 是双层空循环忙等;`Os2If_MsgIsEmpty` 恒返回 TRUE;`BareTask_CopyDataInTaskMutex` 注释称关中断但实际未关,ISR 并发拷贝不安全。
- heap 预算紧:`configTOTAL_HEAP_SIZE=20KB`,10 个任务栈合计 15KB(Pwr/Misc/LIN/Task8/9 各 1K,其余各 2K),队列/定时器/TCB 也从堆出,加资源前先算余量。
- 已知实现缺陷,复用前先核对:`OsTask_DeleteAllTasks` 把 handle 当 task_id 用且与声明 `OsTaskk_DeleteAllTasks` 拼写不一致(勿调用);Ip1/Ip2 优先级误用 `APP_SOC_TASK_PRIORITY`(专用的 `APP_CLUSTER*_TASK_PRIORITY` 闲置);`BareTask_MsgSchedulerRun` 重装周期错用 Evt 表(现配置两者相等故无感);`Os1If_SendMsg` 用 static 中转,多任务/ISR 并发发送有竞态。
- Os1 事件用 Task Notification 位图(`1<<evt`,非 FreeRTOS EventGroup),Recv 为 portMAX_DELAY 死等;FROM_ISR 临界区状态存单个 static,ISR 临界区不可嵌套。
- 相对路径陷阱:`Os1_UpInf`/`Os2_UpInf` 各 .c 用两层 `..\..\L6_Public\...`(按目录直连不成立)、.h 用三层,依赖工程 include 路径兜底;移动文件需同步 `.cproject`。
- `Source/` 为上游内核源码,勿手改;补丁应落在 `Os1_UpInf` 包装层。
