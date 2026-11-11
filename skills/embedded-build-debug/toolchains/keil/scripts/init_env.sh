#!/bin/bash
# Keil 工具链环境初始化 - 所有命令必须先 source 此文件
# 按脚本自身位置定位工具链目录(<skill>/toolchains/keil), 不依赖技能目录名
# 烧录/调试工具(JLink)在 probes/jlink 层, 这里只管编译域(UV4/fromelf)
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

resolve_tool() { # $1=变量名 $2=Keil根目录下的相对路径 $3=可执行文件名
  local var="$1" rel="$2" exe="$3"
  local cur="${!var}" root cand
  [ -f "$cur" ] && return 0
  for root in /c/Keil_v5 /d/Keil_v5 /c/keil /d/keil "/c/Program Files/Keil_v5" "/d/Program Files/Keil_v5"; do
    if [ -f "$root/$rel" ]; then
      set_tool "$var" "$(cygpath -m "$root/$rel")"
      return 0
    fi
  done
  echo "$var 不存在，扫描磁盘查找 $exe ..."
  cand="$(find /c /d -maxdepth 5 -iname "$exe" 2>/dev/null | head -1)"
  if [ -n "$cand" ]; then
    set_tool "$var" "$(cygpath -m "$cand")"
    return 0
  fi
  read -r -p "未能自动定位 $exe，请输入完整路径: " cand
  set_tool "$var" "$cand"
}

resolve_tool UV4 "UV4/UV4.exe" "UV4.exe"
resolve_tool FROMELF "ARM/ARMCC/bin/fromelf.exe" "fromelf.exe"

PROJECT_ROOT="$(git rev-parse --show-toplevel)"
MDK_DIR="$PROJECT_ROOT/$MDK_DIR"
SCRIPTS_DIR="$SKILL_DIR/scripts"
OUTPUT_DIR="$SKILL_DIR/output"
PYTHON="python"
