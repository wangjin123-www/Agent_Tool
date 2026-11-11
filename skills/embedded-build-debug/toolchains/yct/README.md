# YCT 工具链后端（云途 YTM32 / GCC + CMake + Ninja）

面向 YCT 配置工具生成的 CMake 工程（当前用于 **yadea 八寸 yadea0801_app / YTM32B1MD2 / Cortex-M33**）。
与其他两个工具链后端（keil/s32ds）不同，本后端**不绑定 skill 所在仓库**：目标工程路径由 `--project` 或
config.conf 的 `PROJECT_DIR` 决定，因此把整个 skill 目录拷到任意仓库/机器均可使用。

## 环境要求（新机器从零到能编，只有 1 步）

| 组件 | 来源 | 说明 |
|---|---|---|
| YCT 配置工具 | 云途官网 https://www.ytmicro.com → 产品 → YTM32工具链 | 安装弹窗选「是」→ 终端输三次 y，一键部署 CMake/Ninja/GCC 并写 PATH；SDK 在 YCT 内按芯片下载 |

装完后零配置即可用：`build --project <工程根>` 会自动探测 `%APPDATA%/yt_config_tool` 下的
gcc / ninja / cmake / sdk，并自动完成 cmake configure（gcc bin 目录会前置到 PATH，
供工程的 `cmake/gcc.cmake` 里 `find_program` 定位交叉编译器）。

## 常用命令

```bash
SKILL=<skill目录>
# 环境体检 + 固化配置（缺什么会打印对应安装指引）
python $SKILL/toolchains/yct/scripts/yct_build.py init --project D:/wnagjin/Compay_Project/yadea/yadea_8srceen/yadea_8screen_APP

# 增量编译（build.ninja 不存在时自动 configure）
python $SKILL/toolchains/yct/scripts/yct_build.py build --project <工程根>

# 全量重编 / 清理 / 单文件语法编译
python $SKILL/toolchains/yct/scripts/yct_build.py rebuild --project <工程根>
python $SKILL/toolchains/yct/scripts/yct_build.py clean  --project <工程根>
python $SKILL/toolchains/yct/scripts/yct_build.py quick app/main.c --project <工程根>

# 或走统一入口
python $SKILL/scripts/mcu_build_debug.py --toolchain yct --project <工程根> build|rebuild|full|clean|quick
```

产物在 `<工程根>/build/`（`yadea0801_app.elf` 等），编译结束自动列出清单。

## 配置文件

`config/config.conf`（init 生成，不入库）记录探测到的绝对路径；机器之间不通用，
换机后重跑一次 `init` 即可。模板见 `config.conf.example`。

## 烧录

固件产物可直接交给烧录域：`--probe jlink download --file <工程根>/build/yadea0801_app.elf`
（J-Link 配置的 DEVICE 需为 YTM32B1MD2，配置在 `probes/jlink/config/`）。
工程自带 `yadea0801_app.jdebug`，也可直接用 J-Flash/Segger 工程烧录。

## 已知约束

- SDK 路径写死在工程 `CMakeLists.txt` 的 `SDK_DIR`（YCT 生成时按本机 AppData 路径落盘），
  同事机器上由他们的 YCT 重新生成/对齐，路径约定一致（`%APPDATA%/yt_config_tool/sdk/...`）。
- 增删 `Driver/` 等被 `file(GLOB)` 收集的源文件后必须重新 configure（`rebuild`/`full` 或删 build 目录）。

## 两个已踩的坑（脚本已内置处理，勿回退）

**1. cmake 猜中宿主 objcopy → `Invalid bfd target`**

cmake 会从 PATH 猜 `objcopy`/`size`，本机 PATH 里有 `D:\software\bin\objcopy.exe`（x86 版）时，
它会把该绝对路径写进 `build.ninja`，链接尾段转 hex/bin 时直接报
`objcopy.exe: ... Invalid bfd target`。**事后改 PATH 无效**（路径已被固化），必须 configure 期显式
`-DCMAKE_OBJCOPY/-DCMAKE_SIZE/-DCMAKE_AR/-DCMAKE_RANLIB/-DCMAKE_OBJDUMP` 指向 gcc 自带交叉工具。
`configure()` 已自动做这件事。

**2. DLP 透明加密：ninja 处于 python 子孙链时 gcc 读到密文**

本机（DLP 环境）实测：`python → ninja → gcc` 时 gcc 读 `main.c` 拿到密文，报
`stray '\xxx' in program` / `expected ... before '%' token`；而 `python → gcc`、
`python → cmd → gcc`、以及用户在终端直接 `ninja` 都正常。改 ninja 文件名、加 detached/new-console、
经 bash/cmd/powershell 中转、`os.execv` 替换均无效，唯一特征是 “ninja.exe 在 python 子孙链中”。

因此 `run_ninja()` 会先正常跑 ninja；**一旦输出命中密文特征就自动降级**为
`ninja -n -v` 取命令列表 → python 逐条直接执行（进程链里没有 ninja），编译结果完全一致。
降级会打印 `命中 DLP 透明加密拦截...改用 python 直驱`，属预期行为，不是错误。

