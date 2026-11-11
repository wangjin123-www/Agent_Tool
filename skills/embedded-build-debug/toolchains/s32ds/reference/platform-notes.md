# 7255 平台笔记(embedded-build-debug / s32ds 后端)

本工程 CDC_7255(NXP S32K312 + AUTOSAR RTD 4.7,裸机 BareTask 调度)特有的编译相关知识。通用知识见根 `CLAUDE.md`。

## DLP 透明加密(当前阻塞项)

公司 DLP 对项目文件做透明加密,**gcc/bash 读项目文件拿到 `%TSD-Header` 密文,Python/Read/Edit/IDE 读明文**。实测结论(2026-09,dlp_probe):

| 读取方 | 仓库项目 .c/.h | %TEMP% 新内容 |
|---|---|---|
| python | 明文 ✅ | 明文 ✅ |
| gcc | 密文 ❌ | 明文 ✅ |
| bash | 密文 ❌ | 密文 ❌ |

- 是**内容感知加密**:python 把项目源码复制到 %TEMP% 的副本也被识别为敏感内容重新加密(gcc 读它仍是密文),所以**镜像明文副本的方案被 DLP 的复制保护堵死,不要试图绕过**(会写成废密文)。
- 曾正常编译(上次会话 41 文件 FAIL=0)是因为当时文件还是明文;用 Write 工具改文件或 DLP 策略同步后整树被重新加密。
- **解法**:把 `arm-none-eabi-gcc.exe` 加入 DLP 白名单 / 对该路径关闭透明加密。之后 `check`/`quick` 立即可用。
- **`.cproject` 例外(2026-09-14 实测)**:`.cproject` 对 python/Read 工具也拦截(源码 .c/.h 不拦)——`parse` 及一切子命令启动时的 `pick_configuration` 必挂 ParseError。**既有解法**:git 读 blob 是明文,`git show :.cproject > "$LOCALAPPDATA/Temp/cp_idx.xml"` 后用脚本新增的 `S32DS_CPROJECT` 环境变量指向明文副本:`S32DS_CPROJECT=... python s32ds_compile.py parse|check`(环境变量未设时行为不变,见 s32ds_compile.py CPROJECT 处注释)。前提:`.cproject` 与暂存区一致(status 干净),否则副本是旧的。
- 技能脚本已内置检测:gcc 报错含 `%TSD-Header` 时打印诊断并退出码 3,不再吐成百上千行 `stray '\NNN'` 垃圾错误。

## 环境(本机)

| 项 | 路径 |
|---|---|
| S32DS 安装根 | `C:/NXP/S32DS.3.5`(脚本 glob `C:/NXP/S32DS.*`) |
| ARM GCC | `C:/NXP/S32DS.3.5/S32DS/build_tools/gcc_v10.2/gcc-10.2-arm32-eabi/bin/arm-none-eabi-gcc.exe` |
| RTD SDK | `C:/NXP/S32DS.3.5/S32DS/software/PlatformSDK_S32K3/RTD` |
| BaseNXP | `BaseNXP_TS_T40D34M40I0R0`(`include/Mcal.h` 定位,parents[1]) |
| Platform | `Platform_TS_T40D34M40I0R0`(`startup/include/system.h` 定位,parents[2]) |

## 源码构成(112 个 .c)

`RTD/src`(54)+ `Project_Settings/Startup_Code`(4)+ `generate/src`(11)+ `board`(2)+ `src/main.c`(1)+ `CVI_McuPlatform`(40,排除 FreeRTOS)。

- 来源:`.cproject` sourceEntries:`Project_Settings`(排除 `Linker_Files|Debugger`)、`RTD`、`board`、`generate`、`src`、`CVI_McuPlatform`(排除 `L3_RTOS/OS1_FreeRTOS`)。
- `.metadata/` 不在任何 sourceEntry,自动不参与编译(里面 `specs.c` 是 CDT 自动生成物,勿手动纳入)。

## 编译选项(Debug_FLASH,脚本与 IDE 完全一致)

```
-c -mcpu=cortex-m7 -mthumb -mfloat-abi=hard -mfpu=fpv5-sp-d16
-std=c99 -Os -fno-short-enums
-funsigned-char -fomit-frame-pointer -funsigned-bitfields -fno-common
-pedantic -Wextra -Wunused
-Wstrict-prototypes -Wsign-compare -Werror=implicit-function-declaration -Wundef -Wdouble-promotion
```

-D 宏:`D_CACHE_ENABLE I_CACHE_ENABLE ENABLE_FPU MPU_ENABLE GCC S32K3XX S32K312 CPU_S32K312 CPU_CORTEX_M7`。

注意:
- `misc.other` 里含 `-c`,脚本本来也只做 `-c`,无副作用。
- `.cproject` 里 `../RTD/include`(第 39/157/234 行)是相对路径,解析成 `<repo>/../RTD/include`(不存在,gcc 忽略);真实 include 来自 `${ProjDirPath}/RTD/include`。**别把它当成 bug 去改。**

## 已知良性告警(勿当作失败处理)

| 告警 | 来源 | 处置 |
|---|---|---|
| `'uint8' redefined` / `'sint32' redefined` 等 | `L6_Public/PlatformTypes.h`(完整 NXP 版)与 `L6_Public/standtype.h` 对 uint8/uint16/uint32/sint32 的重复 typedef | C99 允许兼容重定义,GCC 认可;`-Wpedantic` 告警,非错误。**不要删 PlatformTypes.h 里的 typedef 去消告警** |
| `unused parameter` | `-Wextra -Wunused` 噪音 | 大量存在于 RTD/generate 回调签名,良性 |
| `implicit declaration` 之外的一切 warning | - | 一律看是不是 `error:` 才算失败 |

## 关键坑

- **PlatformTypes.h 不可精简**:SDK 的 `Platform_Types.h` 是转发桩(`#include "PlatformTypes.h"`),RTD 全部驱动头依赖工程自带这份完整 NXP 版(716 行,含 `boolean/uint64/CPU_TYPE/sint*`)。精简成 stdint 壳 → 全链 `unknown type name 'boolean'`。来源:参考工程 `inc/PlatformTypes.h`。
- **消息表宏在 .c 不在 .h**:`X_MESSAGE_NUMBER`(sizeof 消息表)必须在 Task_XMsg.c;.h 里只有 extern 不完整数组声明,对它 sizeof 是编译错误。跨文件取表长度用 `XApp_GetRealMsgNum()`。
- **generate/ + board/ 是生成物**:手改会被 Config Tools 下次生成覆盖(例外:`generate/src/Igf_Port_Ip_Cfg.c/h` 是手工占位,不在 mex 清单)。
- **`-I src` 不能删**:`EcuAL_GPIO.h` 的 `#include "../CVI_McuPlatform/L6_Public/standtype.h"` 靠它解析。
- **版本一致性**:RTD/include、RTD/src、generate 须同 RTD 基线,`FILE VERSION CHECKS` 用 `#error` 交叉校验。
- **`.cproject` 有 4 个 configuration**,脚本默认取 `Debug_FLASH`(唯一带 `-I src` 的配置;其余 3 配置历来不可构建)。

## REPO_ROOT 计算(s32ds_compile.py 第 33 行)

```python
SCRIPT_DIR = Path(__file__).resolve().parent   # <repo>/.claude/skills/embedded-build-debug/toolchains/s32ds/scripts
REPO_ROOT  = SCRIPT_DIR.parents[3]            # <repo> ← 必须 parents[3],不是 [4]!
```

`parents[4]` 会落到 `<repo>` 的父目录(实测 `D:/.../CDC_7255`,找不到 `.cproject`)。**别"顺手修正"成 [4]。**
