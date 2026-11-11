#!/bin/bash
# Keil 工具链调度入口（编译域）
# 用法: bash keil_build.sh <command> [args...]
# 命令: build|rebuild|parse|flash_check|diff|report
# 烧录/调试走 probes/jlink（统一入口 mcu_build_debug.py build_and_download 会自动串联）

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
source "$SCRIPT_DIR/init_env.sh"

cmd=$1; shift

case "$cmd" in
  build)
    cd "$MDK_DIR" && { "$UV4" -r "$UVPROJX" -t "$UV4_TARGET" -o build.log; BUILD_RC=$?; [ $BUILD_RC -le 1 ] && "$FROMELF" --bin --output "./$OUTPUT_SUBDIR/$TARGET_NAME.bin" "./$OUTPUT_SUBDIR/$TARGET_NAME.axf"; }
    if [ $? -eq 0 ]; then
      cp "$MDK_DIR/build.log" "$OUTPUT_DIR/build_log.txt"
      $PYTHON "$SCRIPTS_DIR/parse_build_log.py" "$MDK_DIR/build.log" > "$OUTPUT_DIR/build_summary.json"
      $PYTHON "$SCRIPTS_DIR/log_history.py" "$MDK_DIR/build.log" "$OUTPUT_DIR/history.json"
      $PYTHON "$SCRIPTS_DIR/generate_html_report.py" "$OUTPUT_DIR"
      cat "$OUTPUT_DIR/build_summary.json"
    else
      cp "$MDK_DIR/build.log" "$OUTPUT_DIR/build_log.txt"
      $PYTHON "$SCRIPTS_DIR/parse_build_log.py" "$MDK_DIR/build.log" > "$OUTPUT_DIR/build_summary.json"
      $PYTHON "$SCRIPTS_DIR/generate_html_report.py" "$OUTPUT_DIR"
      cat "$OUTPUT_DIR/build_summary.json"
      exit 1
    fi
    ;;

  rebuild)
    cd "$MDK_DIR" && rm -f $OUTPUT_SUBDIR/*.o $OUTPUT_SUBDIR/*.d $OUTPUT_SUBDIR/*.crf $OUTPUT_SUBDIR/*.axf $OUTPUT_SUBDIR/*.htm $OUTPUT_SUBDIR/*.map
    cd "$MDK_DIR" && { "$UV4" -r "$UVPROJX" -t "$UV4_TARGET" -o build.log; BUILD_RC=$?; [ $BUILD_RC -le 1 ] && "$FROMELF" --bin --output "./$OUTPUT_SUBDIR/$TARGET_NAME.bin" "./$OUTPUT_SUBDIR/$TARGET_NAME.axf"; }
    if [ $? -eq 0 ]; then
      cp "$MDK_DIR/build.log" "$OUTPUT_DIR/build_log.txt"
      $PYTHON "$SCRIPTS_DIR/parse_build_log.py" "$MDK_DIR/build.log" > "$OUTPUT_DIR/build_summary.json"
      $PYTHON "$SCRIPTS_DIR/log_history.py" "$MDK_DIR/build.log" "$OUTPUT_DIR/history.json"
      $PYTHON "$SCRIPTS_DIR/generate_html_report.py" "$OUTPUT_DIR"
      cat "$OUTPUT_DIR/build_summary.json"
    else
      cp "$MDK_DIR/build.log" "$OUTPUT_DIR/build_log.txt"
      $PYTHON "$SCRIPTS_DIR/parse_build_log.py" "$MDK_DIR/build.log" > "$OUTPUT_DIR/build_summary.json"
      $PYTHON "$SCRIPTS_DIR/generate_html_report.py" "$OUTPUT_DIR"
      cat "$OUTPUT_DIR/build_summary.json"
      exit 1
    fi
    ;;

  parse)
    cp "$MDK_DIR/build.log" "$OUTPUT_DIR/build_log.txt"
    $PYTHON "$SCRIPTS_DIR/parse_build_log.py" "$MDK_DIR/build.log" > "$OUTPUT_DIR/build_summary.json"
    cat "$OUTPUT_DIR/build_summary.json"
    ;;

  flash_check)
    $PYTHON "$SCRIPTS_DIR/check_flash_usage.py" "$MDK_DIR/$OUTPUT_SUBDIR/$TARGET_NAME.map" "$@"
    ;;

  diff)
    $PYTHON "$SCRIPTS_DIR/diff_build.py" "$@"
    ;;

  report)
    $PYTHON "$SCRIPTS_DIR/generate_report.py" "$OUTPUT_DIR"
    ;;

  *)
    echo "用法: bash keil_build.sh <command> [args...]"
    echo "命令: build|rebuild|parse|flash_check|diff|report"
    exit 1
    ;;
esac
