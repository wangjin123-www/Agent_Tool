# s32ds-compile

S32K3 工程命令行编译验证 skill。不打开 S32 Design Studio GUI,用 `arm-none-eabi-gcc` 按工程 `Debug_FLASH` 配置只做 `-c` 编译,快速定位语法/类型/头文件错误。

## 快速开始

```bash
# 1. 解析 .cproject,确认选项映射与 include 路径
python .claude/skills/s32ds-compile/scripts/s32ds_compile.py parse

# 2. 全量编译检查(112 个 .c,约 1-2 分钟)
python .claude/skills/s32ds-compile/scripts/s32ds_compile.py check

# 3. 单文件快速验证
python .claude/skills/s32ds-compile/scripts/s32ds_compile.py quick src/App/App_Power.c
```

## 目录结构

```
s32ds-compile/
├── SKILL.md                       # 主技能说明(调用方式/失败处理)
├── scripts/
│   └── s32ds_compile.py           # 唯一入口脚本(parse/check/quick/clean)
├── reference/
│   └── platform-notes.md          # 7255 平台坑与良性告警清单
├── config/
│   └── sdk_paths.conf.example     # 覆盖自动探测的配置模板
├── output/                        # 编译产物(已 gitignore,勿提交)
└── readme.md
```

## 注意事项

- **DLP 前提**:若 `check`/`quick` 退出码 3 提示 DLP 加密阻塞,需先把 `arm-none-eabi-gcc.exe` 加进 DLP 白名单(公司 DLP 让 gcc 读项目文件拿到密文;Python/Read/Edit/IDE 不受影响)。详见 `reference/platform-notes.md`。
- **只做编译,不做链接/烧录**:链接出 elf 走 S32DS GUI 的 managed build。
- **`output/` 不要提交**:全是编译中间物。
- 自动探测到本机 S32DS.3.5 / GCC 10.2 / RTD SDK;换机器路径变了就在 `config/sdk_paths.conf` 显式指定(复制 example 改名)。
- 更多平台细节(良性告警、PlatformTypes.h 等)见 `reference/platform-notes.md`。
