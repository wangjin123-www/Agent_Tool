#!/bin/bash
# J-Link 探针调度入口（烧录/调试域）
# 用法: bash jlink_entry.sh <command> [args...]
# 命令: download|full_download|erase|verify|reset|jlink|dump_cortex
# 接口固定 SWD @ 4000kHz（与原 keil-debug 行为一致）

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
source "$SCRIPT_DIR/init_env.sh"

cmd=$1; shift

case "$cmd" in
  download)
    # 默认 Slot A 模式: 从 0x8000 编程应用区; --file <路径> 可覆盖默认镜像
    $PYTHON "$SCRIPT_DIR/flash_loader.py" --jlink "$JLINK" --device $DEVICE --file "$HEX_PATH" --slot-a "$@"
    ;;

  full_download)
    # 擦除 -> 下载 -> 运行（镜像类型非交互时默认 HEX）
    $PYTHON "$SCRIPT_DIR/flash_loader.py" --jlink "$JLINK" --device $DEVICE --config "$SKILL_DIR/config/config.conf" --linker "$LINKER_SCRIPT" --full "$@"
    ;;

  erase)
    $PYTHON "$SCRIPT_DIR/jlink_ops.py" erase --jlink "$JLINK" --device $DEVICE --linker "$LINKER_SCRIPT" "$@"
    ;;

  verify)
    $PYTHON "$SCRIPT_DIR/jlink_ops.py" verify --jlink "$JLINK" --device $DEVICE --file "$HEX_PATH" --linker "$LINKER_SCRIPT" "$@"
    ;;

  reset)
    $PYTHON "$SCRIPT_DIR/jlink_ops.py" reset --jlink "$JLINK" --device $DEVICE "$@"
    ;;

  jlink)
    # 通用操作: --command halt|go|regs|reset|step|read_mem|write_mem|bp|read_reg
    $PYTHON "$SCRIPT_DIR/jlink_cmd.py" --jlink "$JLINK" --device $DEVICE "$@"
    ;;

  probe)
    # 通用探针操作入口(与 pemicro 对齐): probe halt --address 等转发到 jlink_cmd
    $PYTHON "$SCRIPT_DIR/jlink_cmd.py" --jlink "$JLINK" --device $DEVICE "$@"
    ;;

  dump_cortex)
    # HardFault 现场导出 + CFSR/HFSR 分析
    $PYTHON "$SCRIPT_DIR/dump_cortex.py" --jlink "$JLINK" --device $DEVICE "$@"
    ;;

  *)
    echo "用法: bash jlink_entry.sh <command> [args...]"
    echo "命令: download|full_download|erase|verify|reset|jlink|dump_cortex"
    exit 1
    ;;
esac
