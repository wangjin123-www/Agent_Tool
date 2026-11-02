# 固件端串口日志：level 输出 / drop counter / 移植指南

三种场景：

1. [DAB_BOX 现有代码加 level 前缀（最小改动）](#1-dab_box-现有代码加-level-前缀)
2. [drop counter（DAB_BOX 现有代码最小改动）](#2-drop-counter)
3. [移植到其他项目：Service_Log 常驻服务（完整模块）](#3-移植到其他项目-servicelog-常驻服务)

统一输出格式（serial-log skill 固定格式解析依据）：

```text
[timestamp][level][file:line] [module] message
```

level 全称（不用缩写）：`DEBUG` / `INFO` / `WARN` / `ERROR`。

---

## 1. DAB_BOX 现有代码加 level 前缀

位置：`L3_Service/Service_USB_Debug/Service_USB_Debug.c` 串口输出段
（`Service_USB_LogDiagInternal` 内 `#ifdef PROJECT_DEBUG_USART_ENABLE` 部分，约 L139 起）。

在 `[timestamp]` 拼装完成之后、`[file:line]` 拼装之前插入：

```c
        // [level] 全称: DEBUG/INFO/WARN/ERROR, 枚举值 1~4, 越界记 "?"
        {
            static const char *const lvl_name[] = {
                "?", "DEBUG", "INFO", "WARN", "ERROR"
            };
            const char *s = (level <= DiagLogLevel_DIAG_LOG_LEVEL_ERROR)
                            ? lvl_name[level] : "?";
            if (pos < cap - 1) buf_p[pos++] = '[';
            while (*s && pos < cap - 1) { buf_p[pos++] = *s++; }
            if (pos < cap - 1) buf_p[pos++] = ']';
        }
```

说明：

- `DiagLogLevel` 枚举值 0~4（UNKNOWN/DEBUG/INFO/WARN/ERROR），见 `Service_Com.pb.h` L76。
- `level` 参数已在函数入参中，无需改动函数签名。
- 旧固件日志（无 level 字段）skill 解析脚本自动兼容。

输出效果：

```text
[12345678][INFO][Service_Com.c:277] [COM] SendWithAck success count=5
[12345679][ERROR][Service_Com.c:1059] [COM] COM_Resp_Handshake send failed: ret=0x00000016
```

## 2. drop counter

DAB_BOX 现有代码有三个丢弃点，都在 `Service_USB_LogDiagInternal` 里：

| 丢弃点 | 位置 | 原因 |
|--------|------|------|
| 中断上下文 | `LOG_MUTEX_LOCK` 宏 L26-28 | 中断不能拿互斥锁 |
| 互斥锁拿不到 | `LOG_MUTEX_LOCK` 宏 L29-31 | 其他任务正在打日志（超时 0） |
| UART 发送失败 | `MCAL_Uart_Trans` 返回后 | 串口忙等超时 `LOG_UART_TIMEOUT` |

最小改动（文件顶部定义 + 丢弃点自增 + 查询函数）：

```c
/* Service_USB_Debug.c 顶部 */
static volatile uint32_t g_log_drop_cnt = 0;

/* LOG_MUTEX_LOCK 宏的两个 return 前加 */
g_log_drop_cnt++;

/* UART 发送判断: MCAL_Uart_Trans 无返回值, 可通过 USART_GetStatus 检查,
 * 或改为移植版 Service_Log(见第3节)自带返回值统计 */

/* 查询函数, 加入 Service_USB_Debug.h */
uint32_t Service_USB_DebugGetDropCnt(void)
{
    return g_log_drop_cnt;
}
```

上报方式（任选）：

- 周期上报：任一低频任务里每 10s 检查，变化则 `LOG_WARN(LOG_MOD_COM, "drop_cnt=%u", ...)`，注意 level 用 `W`，脚本会自动归类到 drop counter 章节。
- 命令查询：挂到现有调试命令分发，收到查询指令时打印。

drop_cnt=0 说明日志系统健康；非 0 说明互斥锁竞争激烈或波特率不够（921600 下 DEBUG 级别刷太多时先 `LOG_SET_LEVEL(DiagLogLevel_DIAG_LOG_LEVEL_INFO)`）。

## 3. 移植到其他项目：ServiceLog 常驻服务

设计：**业务调用只写 ring buffer（微秒级，不阻塞业务），低优先级常驻任务慢慢发串口**。
与 DAB_BOX 现有实现的差别：DAB_BOX 在调用者上下文里直接发串口（持锁忙等）；移植版把发送挪到独立任务，业务侧永不阻塞。

### ServiceLog.h

```c
#ifndef __SERVICE_LOG_H__
#define __SERVICE_LOG_H__

#include <stdint.h>

typedef enum {
    LOG_LEVEL_DEBUG = 0,
    LOG_LEVEL_INFO  = 1,
    LOG_LEVEL_WARN  = 2,
    LOG_LEVEL_ERROR = 3,
} LogLevel_t;

void     ServiceLog_Init(void);            /* 调度器启动前调用 */
void     ServiceLog_SetLevel(LogLevel_t l);
LogLevel_t ServiceLog_GetLevel(void);
uint32_t ServiceLog_GetDropCnt(void);

/* 任务和中断都可调用; 中断里不要打 DEBUG 级别长日志 */
void ServiceLog_Output(LogLevel_t lvl, const char *file, int line,
                       const char *module, const char *fmt, ...);

#define LOGD(mod, fmt, ...)  ServiceLog_Output(LOG_LEVEL_DEBUG, __FILE__, __LINE__, mod, fmt, ##__VA_ARGS__)
#define LOGI(mod, fmt, ...)  ServiceLog_Output(LOG_LEVEL_INFO,  __FILE__, __LINE__, mod, fmt, ##__VA_ARGS__)
#define LOGW(mod, fmt, ...)  ServiceLog_Output(LOG_LEVEL_WARN,  __FILE__, __LINE__, mod, fmt, ##__VA_ARGS__)
#define LOGE(mod, fmt, ...)  ServiceLog_Output(LOG_LEVEL_ERROR, __FILE__, __LINE__, mod, fmt, ##__VA_ARGS__)

#endif
```

### ServiceLog.c

```c
#include "ServiceLog.h"
#include <stdio.h>
#include <stdarg.h>
#include <string.h>
#include "FreeRTOS.h"
#include "task.h"
#include "semphr.h"

#define LOG_RING_SIZE   4096U              /* 环形缓冲字节 */
#define LOG_LINE_MAX    192U               /* 单条日志上限 */
#define LOG_TASK_STACK  512U
#define LOG_TASK_PRIO   1U                 /* 最低优先级, 不抢业务 */
#define DROP_REPORT_MS  10000U             /* drop 变化上报周期 */

static uint8_t  s_ring[LOG_RING_SIZE];
static volatile uint16_t s_w = 0, s_r = 0; /* 读指针追赶写指针 */
static volatile uint32_t s_drop_cnt = 0;
static volatile uint32_t s_drop_reported = 0;
static volatile LogLevel_t s_level = LOG_LEVEL_DEBUG;
static SemaphoreHandle_t s_sem;

static inline uint16_t ring_used(void)
{
    return (uint16_t)((s_w - s_r) & (LOG_RING_SIZE - 1));  /* LOG_RING_SIZE 必须 2 的幂 */
}

/* 关中断保护, 任务/中断通用; 放不下整条就整条丢弃并计数, 不产生截断日志 */
static void ring_write(const char *data, uint16_t len)
{
    UBaseType_t uxSaved = portSET_INTERRUPT_MASK_FROM_ISR();
    if (ring_used() + len > LOG_RING_SIZE - 1) {
        s_drop_cnt++;
        portCLEAR_INTERRUPT_MASK_FROM_ISR(uxSaved);
        return;
    }
    for (uint16_t i = 0; i < len; i++) {
        s_ring[s_w] = (uint8_t)data[i];
        s_w = (uint16_t)((s_w + 1) & (LOG_RING_SIZE - 1));
    }
    portCLEAR_INTERRUPT_MASK_FROM_ISR(uxSaved);
}

/* 弱符号: 移植到不同 MCU 时在别处重定义为自己的串口发送 */
__weak int32_t Log_UartSend(const uint8_t *buf, uint16_t len)
{
    (void)buf; (void)len;
    return -1;  /* 未实现, 日志会积压并计入 drop */
}

static char s_line[LOG_LINE_MAX];

void ServiceLog_Output(LogLevel_t lvl, const char *file, int line,
                       const char *module, const char *fmt, ...)
{
    if (lvl < s_level) {
        return;
    }
    static const char tag[] = {'D', 'I', 'W', 'E'};
    const char *fname = strrchr(file, '/');
    const char *bslash = strrchr(file, '\\');
    if (bslash > fname) fname = bslash;
    fname = fname ? fname + 1 : file;

    int n = snprintf(s_line, LOG_LINE_MAX, "[%lu][%c][%s:%d] [%s] ",
                     (unsigned long)xTaskGetTickCount(),
                     tag[lvl & 3], fname, line, module);
    if (n < 0) return;
    if (n > (int)LOG_LINE_MAX - 3) n = (int)LOG_LINE_MAX - 3;

    va_list ap;
    va_start(ap, fmt);
    int m = vsnprintf(s_line + n, (size_t)(LOG_LINE_MAX - n - 2), fmt, ap);
    va_end(ap);
    if (m < 0) m = 0;
    if (m > (int)LOG_LINE_MAX - n - 2) m = (int)LOG_LINE_MAX - n - 2;
    n += m;
    s_line[n++] = '\r';
    s_line[n++] = '\n';

    ring_write(s_line, (uint16_t)n);

    BaseType_t woken = pdFALSE;
    if ((SCB->ICSR & SCB_ICSR_VECTACTIVE_Msk) != 0U) {
        xSemaphoreGiveFromISR(s_sem, &woken);
        portYIELD_FROM_ISR(woken);
    } else {
        xSemaphoreGive(s_sem);
    }
}

static void LogTask(void *arg)
{
    (void)arg;
    uint8_t chunk[64];
    TickType_t last_drop_check = xTaskGetTickCount();
    for (;;) {
        xSemaphoreTake(s_sem, pdMS_TO_TICKS(DROP_REPORT_MS));
        while (s_r != s_w) {
            uint16_t n = 0;
            while (n < sizeof(chunk) && s_r != s_w) {
                chunk[n++] = s_ring[s_r];
                s_r = (uint16_t)((s_r + 1) & (LOG_RING_SIZE - 1));
            }
            (void)Log_UartSend(chunk, n);   /* 发失败由 ring 满计数兜底 */
        }
        /* drop 变化上报 */
        if (s_drop_cnt != s_drop_reported &&
            (xTaskGetTickCount() - last_drop_check) >= pdMS_TO_TICKS(DROP_REPORT_MS)) {
            uint32_t d = s_drop_cnt;
            ServiceLog_Output(LOG_LEVEL_WARN, "ServiceLog.c", 0, "LOG",
                              "drop_cnt=%u (total)", (unsigned)d);
            s_drop_reported = d;
            last_drop_check = xTaskGetTickCount();
        }
    }
}

void ServiceLog_Init(void)
{
    s_sem = xSemaphoreCreateBinary();
    xTaskCreate(LogTask, "Log", LOG_TASK_STACK / sizeof(StackType_t),
                NULL, LOG_TASK_PRIO, NULL);
}

void ServiceLog_SetLevel(LogLevel_t l) { s_level = l; }
LogLevel_t ServiceLog_GetLevel(void)    { return s_level; }
uint32_t ServiceLog_GetDropCnt(void)    { return s_drop_cnt; }
```

### 移植 checklist

1. 拷贝 `ServiceLog.c/.h` 到新项目 service 层（如 `L3_Service/Service_Log/`）
2. 实现 `Log_UartSend`：绑定目标 MCU 的串口发送（DAB_BOX 上对应 `MCAL_Uart_Trans`，HC32F460 为 USART3 PE2/PE3，921600）
3. `main` 里调度器启动前调用 `ServiceLog_Init()`
4. 全局搜索替换旧 `printf` 调用为 `LOGD/LOGI/LOGW/LOGE`
5. 量产/压测时 `ServiceLog_SetLevel(LOG_LEVEL_WARN)` 降噪
6. 采日志：`python .claude/skills/serial-log/scripts/capture/capture_serial.py --port COMx --baud 921600`

### 纯串口配置（不带 USB 输出）

DAB_BOX 固件里日志走 USB（`COM_SendMessage` EP3）+ 串口双通道。只要串口时：

```c
/* Public_Project.h 或编译宏 */
#undef  PROJECT_DEBUG_USB_ENABLE     /* 关 USB 日志通道 */
#define PROJECT_DEBUG_USART_ENABLE  1 /* 只留串口 */
```

`Service_USB_LogDiagInternal` 内两个 `#ifdef` 分支自动只剩串口路径，无需改代码。

### 已知限制

- `s_line` 是单缓冲，并发调用时后到的会覆盖先到的：DAB_BOX 原实现用互斥锁串行化解决了这个问题，代价是拿不到锁就丢。移植版保持同样取舍（丢 > 卡）。如果业务侧高频并发打日志，把 `s_line` 改为两块交替缓冲可缓解。
- 乱码/丢字符：检查波特率两端一致、`LOG_RING_SIZE` 是否够（压测日志量大时升到 8192）。
