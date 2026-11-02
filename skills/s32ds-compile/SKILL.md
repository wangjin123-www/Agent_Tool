---
name: s32ds-compile
description: "NXP S32DS (S32K3) 工程命令行编译验证工具。工作流:python scripts/s32ds_compile.py <check|full|quick|parse|clean> — check 按 config/build_mode.conf 的 mode 决定行为:compile=仅并行编译验证(-c,产物 .o 落 output/obj),full=完整构建(make -n 计划 + python 回放命令,生成 Debug_FLASH 下 .elf/.map/.hex/.bin);quick <file> 只编译单个文件;parse 从 .cproject 解析编译选项;clean 清理 output/。utils/build.bat 交互选 1(编译)/2(完整构建)。Use when the user asks 编译检查 / 编译验证 / 语法检查 / 有没有编译错误 / 验证某文件能否编译 / 全量编译检查 / 链接出 elf/hex/bin / 出固件 / compile check / verify build for this S32K3 project. DO NOT use for: 烧录(需 S32DS GUI)、改 .cproject 本身、非 NXP S32DS 工程。"
tools: Read, Glob, Grep, Bash, Edit, Write
---

# s32ds-compile — S32K3 工程命令行编译验证 + 完整构建

## 目标

在不打开 S32 Design Studio GUI 的前提下,用 `arm-none-eabi-gcc` 按工程 `Debug_FLASH` 配置做两种事:

- **compile 模式(默认)**:`-c` 只编译不链接,产物 .o 落 `output/obj`,逐文件验证语法/类型错误,产出 `output/summary.json`
- **full 模式**:完整构建,产出 `Debug_FLASH/` 下 `.elf/.map/.hex` + 追加 `.bin`——与 GUI 构建产物同路径同内容

两种模式由 `config/build_mode.conf`(`mode = compile|full`)决定,命令行 `--mode` 可临时覆盖。

## 适用 / 不适用

- ✅ 改完 C 代码后快速验证「有没有编译错误」;误删 include、改错头文件、类型不匹配等
- ✅ 单个文件快速验证:`quick <相对路径>`
- ✅ 命令行出固件(.elf/.map/.hex/.bin):full 模式或双击 `utils/build.bat` 选 2
- ✅ 交互式构建入口:`utils/build.bat`,选 1=编译检查 / 2=完整构建,打印结果与退出码
- ❌ 烧录(仍需 S32DS GUI + `Project_Settings/Debugger/` launch)
- ❌ 改引脚/时钟/外设后未跑 Config Tools 重新生成 `generate/` 的场景(生成物过期,编译错是预期)
- ❌ full 模式前提:`Debug_FLASH/` 下须有 S32DS 生成的 makefile/subdir.mk/*.args(GUI 构建过一次即有)

## 调用方式

```
python <本skill目录>/scripts/s32ds_compile.py <command> [args]
<本skill目录>/utils/build.bat          (交互选 1/2)
```

| 命令 | 作用 |
|---|---|
| `check` | 按 config/build_mode.conf 的 mode 执行(默认 compile=全量并行编译,写 `output/summary.json`);`--mode full` 可覆盖 |
| `full` | 显式完整构建:make -n 算增量计划 → python 逐条回放命令(DLP 安全)→ objcopy 补 .bin → size;完整日志 `output/build_full.log`;退出码 0=BUILD OK,1=失败,3=DLP 阻塞 |
| `quick <file>` | 只编译单文件(相对仓库根的路径),快速验证一处修改;退出码 3=DLP 阻塞 |
| `parse` | 从 `.cproject` Debug_FLASH 配置解析选项,打印解析出的 gcc 命令行 + include 目录存在性 + 源码清单;报出未映射的 superClass |
| `clean` | 删除 `output/` 全部编译产物 |

**先跑 `parse` 确认选项映射完整、include 目录无 `[MISS]`,再跑 `check`。** 否则工具链版本/优化等级对不上时,误报的编译错会浪费排查时间。

## 关键背景知识(规则 | 原因)

| 规则 | 原因 |
|---|---|
| compile 模式只做 `-c` 编译(产物在 output/obj);full 模式才链接(产物在 Debug_FLASH/,与 GUI 同路径) | 编译验证快且无副作用;full 复用 S32DS 生成的 makefile,产物与 GUI 完全一致 |
| **full 模式绝不直接执行 make,只用 `make -n` 拿计划、python 逐条回放命令** | DLP 白名单按进程链放行:python→gcc 读明文(quick 已验证),make→gcc 读密文(实测 exit 3);回放保证命令与 GUI 逐字一致 |
| full 模式 `.bin` 是脚本追加的 objcopy -O binary | S32DS makefile 只产 .hex/.siz,无 .bin 目标 |
| 选项来源是 `.cproject` 的 Debug_FLASH 配置,不是拍脑袋 | 保证与 IDE 构建一致;`parse` 负责兜底未映射项 |
| 工具链/SDK 自动探测,支持 `config/sdk_paths.conf` 显式覆盖;make 探测 build_tools/msys32/usr/bin/make.exe | 各机器安装路径不同;探测失败时脚本会打印线索 |
| 已知良性告警不当作失败 | PlatformTypes.h 与 standtype.h 的 typedef 重定义、未用参数、`-Wextra` 噪音等,见 `reference/platform-notes.md` 清单 |
| Windows 下脚本强制 UTF-8 | cp936 会炸中文;已内置 reconfigure |
| 只把带 `error:` 的行记入失败 | 告警多≠失败;告警数只进 summary.json 的 `warnings` 字段 |

## 流程

**`parse`(首次或怀疑选项对不上时):**

```
python .../s32ds_compile.py parse
```

读 `.cproject` Debug_FLASH 配置 → 解析 BOOL/ENUM/STRING 三类选项 → 打印解析结果。若 `unmapped` 清单非空,把新 superClass 补进脚本的 `BOOL_FLAGS`/`ENUM_SUPERCLASSES`/`STRING_FLAGS`,再重跑。

**`check`(日常验证):**

```
python .../s32ds_compile.py check [--jobs 4]
```

跑完看 `output/summary.json`:

```json
{ "config": "Debug_FLASH", "total": 112, "fail": 0, "warn_files": 32,
  "failed": [], "warnings": { "src/.../xxx.c": 2 } }
```

`failed` 数组为空即全过。失败时看 `output/obj/<文件>.err` 拿完整错误。

**`quick`(单文件快速验证):**

```
python .../s32ds_compile.py quick src/App/App_Power.c
```

**`clean`(清产物):**

```
python .../s32ds_compile.py clean
```

## 失败处理表(场景 | 处置)

| 场景 | 处置 |
|---|---|
| 退出码 3,打印 `DLP TRANSPARENT ENCRYPTION BLOCKS gcc` | 公司 DLP 透明加密:gcc 读项目文件是 `%TSD-Header` 密文。把 `arm-none-eabi-gcc.exe` 加进 DLP 白名单(或对该路径关加密)后重跑;Python/Read/Edit/IDE 不受影响 |
| summary.json 里 `fail` 且错误文本是头文件里的 `#error` | 先查 `generate/include/modules.h` 的 `USE_*_MODULE` 开关与 RTD 版本基线,别当普通语法错修 |
| 错误都指向一个 `*_Cfg.h` / 某个生成物 | 该生成物过期:去 S32 Config Tools 重新生成 `generate/`,别手改生成物 |
| 错误是 `unknown type name` 且指向 SDK 转发头 | 检查对应类型的真头文件是否缺失或版本不匹配(PlatformTypes.h 被转发头引用,见 platform-notes.md) |
| 所有文件 `FILE VERSION CHECKS` 类 `#error` | RTD/include、RTD/src、generate 三处版本基线不一致,需统一回同一 RTD 版本 |
| `parse` 里 `[MISS]` 的 include 目录 | 先看是 `${...}` 未解析(SDK 路径探测失败)还是真缺目录;前者在 `config/sdk_paths.conf` 显式指定 |
| 想全部通过但有一堆重复 typedef 告警 | 良性,记录在 platform-notes.md,不必处理 |

## 常见自我合理化(Excuse | Reality)

| Excuse | Reality |
|---|---|
| "IDE 里反正能编译,不用跑脚本" | IDE 每改一次全量构建几分钟;脚本 1–2 分钟且直接给到错误行,迭代快得多 |
| "我只改了 .h,编译会跟着过" | 头文件改动影响所有 include 它的 .c;`check` 全量跑才能兜住 |
| "告警多,估计全过不了" | 告警≠失败;脚本只把带 error 的行记入失败,告警行在 platform-notes.md 里已判定良性 |
| "链接错没抓到,等于没用" | 链接阶段交给 S32DS;脚本定位的是语法/类型/头文件类错误,那是改代码时 95% 的坑 |
