# CVI_McuPlatform/L2_Tasks(任务适配层:用统一四件套框架把 L1 应用挂到调度器上)

每个任务一个目录,固定四件套:`Task_X.c/h` 生命周期与主循环、`Task_XEvent.c/h` 事件位分发、`Task_XMsg.c/h` 消息分发、`Task_XInf.h` 对外入口。`Tasks_LowInf/` 是 OS 抽象层。

## Architecture
```
L2_Tasks/
  Tasks_LowInf/  # OS 抽象:STRUCT_TASKS_LOWINF 函数指针表,按 MCU_SCHED_TYPE 路由到 OS1_FreeRTOS / OS2_TmrSched
  Task_Power/    # 电源任务 → App_Power_UpInf(AppCycProc 直调 MainFunction)
  Task_Canbus/   # CAN+诊断任务 → App_Can_UpInf + CanApp_DcmMain(DCM)
  Task_Soc/      # SOC 任务 → App_SocComInf + Energy_Mainfunction(独立 EnergyCycProc)
  Task_Cluster1/ # 仪表1 → App_Cluster_UpInf(20/50/100ms 主功能挂在事件表)
  Task_Cluster2/ # 仪表2 → IcApp_Trip / IcApp_OneDrive(经事件表)
  Task_Lin/      # LIN 任务 → App_Lin_UpInf
  Task_Misc/     # 杂项 → App_Key + APP_HWFAULT + App_AutoTest
```

## Key Files
- `Tasks_LowInf/Tasks_LowInf.h` - 任务 ID(E_TASK_*)、消息组(TASK_MSGID_GROUP_*)、OsIf_* 接口定义;新增任务第一步改这里
- `Task_Canbus/Task_Can.c` - 四件套标准模板:CreateInit 注册任务/事件/消息,App() 死循环泵事件+消息
- `Task_Canbus/Task_CanEvent.c` - 事件表模式:`EvtIdTable[E_X_EVT_ID_MAX]` 按事件位索引派发

## 任务框架模式(7 个任务同构)
- `Task_XCreateInit()`:Os_CreateTask + Os_CreateEvent + Os_CreateMessage;对外仅暴露 CreateInit/App(见 Task_XInf.h),由模块外装配调用
- FreeRTOS 下 `Task_XApp()` 先 AppInit 一次再 while(1) 泵事件/消息;`TimerCallback` 发基础节拍事件(5ms 或 10ms),慢周期用静态计数器分频
- 加事件 = Event.h 枚举 + Event.c 表 + 发送处三处同步;加消息 = Msg.h 枚举 + Msg.c 表同步

## Gotchas
- 全部 7 个 Event.c 的表槽 18 都错填 `XxxApp_EvtID17_Function`(复制粘贴),ID18 处理函数成孤儿;启用事件前先核对表项
- Soc/Misc/Cluster1/Cluster2 的 CreateInit 无真正的 TMRSCHED `#if` 分支(仅注释),TmrSched 下会把死循环 Task_XApp 注册成周期函数;CAN/Lin/Power 有正确分支
- `Tasks_LowInf/Tasks_LowInf.h` 已定义 E_TASK_MEM/TASK_MSGID_GROUP_MEM,但本层无 Task_Mem 目录(ID 预留)
- Cluster1 枚举 ID06_CYC100MS 排在 ID07_CYC50MS 之前,ID 号与周期长短不对应,别按数字猜周期
- 分频计数 `>N`(实为 N+1 拍)与 `>=N`(N 拍)混用:Cluster1 的 50/100ms 实际 60/110ms;复制分频代码先看清比较符
- `Task_PowerAppIpcProc`/`Task_SocAppIpcProc` 仅在 Inf.h 声明、无定义,勿调用
- `Task_CanAppCycProc` 里 "for test" 发事件代码未屏蔽(每 101 拍发 EVT_ID05);Power 同类测试代码已 `#if 0`
- `Task_Cluster2AppInit()` 是空壳,Cluster2 业务全在事件表里
