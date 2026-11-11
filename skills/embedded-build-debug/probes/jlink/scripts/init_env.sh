#!/bin/bash
# J-Link 探针环境初始化 - 所有命令必须先 source 此文件
# 按脚本自身位置定位探针目录(<skill>/probes/jlink), 不依赖技能目录名
SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export SKILL_DIR
CONF="$SKILL_DIR/config/config.conf"

# config.conf 不存在时从 config.conf.example 拷贝生成（config.conf 不入库）
[ -f "$CONF" ] || cp "$SKILL_DIR/config/config.conf.example" "$CONF"
source "$CONF"

# 工具路径不存在时：先扫常见安装目录，再扫磁盘，仍找不到问用户输入，最终值写回 config.conf
set_tool() { # $1=变量名 $2=路径；更新内存变量并写回配置（删旧行追加新行，保留注释）
  local var="$1" val="$2" tmp
  printf -v "$var" '%s' "$val"
  tmp="$(mktemp)"
  grep -vE "^${var}=" "$CONF" > "$tmp"
  echo "${var}=\"${val}\"" >> "$tmp"
  mv "$tmp" "$CONF"
  echo "$var -> $val"
}

resolve_jlink() {
  local cur="$JLINK" root cand
  [ -f "$cur" ] && return 0
  # Keil 自带 Segger + SEGGER 官方安装目录
  for root in /c/Keil_v5/ARM/Segger /d/Keil_v5/ARM/Segger /c/keil/ARM/Segger /d/keil/ARM/Segger \
              "/c/Program Files/SEGGER/JLink" "/d/Program Files/SEGGER/JLink" \
              "/c/Program Files (x86)/SEGGER/JLink" "/d/Program Files (x86)/SEGGER/JLink"; do
    if [ -f "$root/JLink.exe" ]; then
      set_tool JLINK "$(cygpath -m "$root/JLink.exe")"
      return 0
    fi
  done
  echo "JLINK 不存在，扫描磁盘查找 JLink.exe ..."
  cand="$(find /c /d -maxdepth 4 -iname "JLink.exe" 2>/dev/null | head -1)"
  if [ -n "$cand" ]; then
    set_tool JLINK "$(cygpath -m "$cand")"
    return 0
  fi
  read -r -p "未能自动定位 JLink.exe，请输入完整路径: " cand
  set_tool JLINK "$cand"
}

resolve_jlink

PROJECT_ROOT="$(git rev-parse --show-toplevel)"
PYTHON="python"

# 镜像/链接脚本路径（config 中相对仓库根，这里转绝对；已绝对则原样）
case "$HEX_PATH" in /*|[A-Za-z]:*) ;; *) HEX_PATH="$PROJECT_ROOT/$HEX_PATH";; esac
case "$BIN_PATH" in /*|[A-Za-z]:*) ;; *) BIN_PATH="$PROJECT_ROOT/$BIN_PATH";; esac
case "$LINKER_SCRIPT" in /*|[A-Za-z]:*) ;; *) LINKER_SCRIPT="$PROJECT_ROOT/$LINKER_SCRIPT";; esac
