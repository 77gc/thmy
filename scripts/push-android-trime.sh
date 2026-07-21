#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
SOURCE_DIR="$ROOT_DIR/android"
TRIME_DIR="${TRIME_DIR:-/sdcard/rime}"
SERIAL="${ANDROID_SERIAL:-}"
CHECK_ONLY=0

usage() {
  cat <<'EOF'
用法：
  ./scripts/push-android-trime.sh [--serial 设备序列号] [--check]

将仓库 android/ 中的 Trime 配置同步到设备的 /sdcard/rime。
默认自动选择唯一已授权设备；连接多台设备时必须用 --serial 指定。

选项：
  -s, --serial 序列号  指定目标设备，也可通过 ANDROID_SERIAL 设置
      --check          仅检查本机文件、adb 和设备连接，不写入手机
  -h, --help           显示本帮助

环境变量：
  TRIME_DIR            手机上的 Trime 用户目录，默认 /sdcard/rime

本脚本只同步文件并更新时间，绝不执行 Trime 部署。
同步后请在手机同文输入法中手动点“部署”。
EOF
}

die() {
  printf '错误：%s\n' "$*" >&2
  exit 1
}

while [ "$#" -gt 0 ]; do
  case "$1" in
    -s|--serial)
      [ "$#" -ge 2 ] || die "$1 需要设备序列号"
      SERIAL="$2"
      shift 2
      ;;
    --check)
      CHECK_ONLY=1
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      die "未知参数：$1"
      ;;
  esac
done

command -v adb >/dev/null 2>&1 || die "未找到 adb，请安装 Android Platform Tools"
[ -d "$SOURCE_DIR" ] || die "未找到 Android 配置目录：$SOURCE_DIR"

if [ -z "$SERIAL" ]; then
  DEVICES=$(adb devices | awk 'NR > 1 && $2 == "device" { print $1 }')
  DEVICE_COUNT=$(printf '%s\n' "$DEVICES" | awk 'NF { count++ } END { print count + 0 }')

  case "$DEVICE_COUNT" in
    0)
      die "未找到已授权设备。请连接手机并允许 USB 调试"
      ;;
    1)
      SERIAL=$(printf '%s\n' "$DEVICES" | awk 'NF { print; exit }')
      ;;
    *)
      printf '检测到多台已授权设备：\n%s\n' "$DEVICES" >&2
      die "请用 --serial 指定目标设备"
      ;;
  esac
fi

STATUS=$(adb devices | awk -v serial="$SERIAL" '$1 == serial { print $2; exit }')
case "$STATUS" in
  device)
    ;;
  unauthorized)
    die "设备 $SERIAL 未授权，请在手机上允许 USB 调试"
    ;;
  offline)
    die "设备 $SERIAL 离线，请重新连接"
    ;;
  *)
    die "未找到设备 $SERIAL"
    ;;
esac

ADB=(adb -s "$SERIAL")

printf '目标设备：%s\n' "$SERIAL"
printf '本地目录：%s\n' "$SOURCE_DIR"
printf '手机目录：%s\n' "$TRIME_DIR"

if [ "$CHECK_ONLY" -eq 1 ]; then
  printf '检查通过：未推送文件，未执行部署。\n'
  exit 0
fi

"${ADB[@]}" shell mkdir -p "$TRIME_DIR"
"${ADB[@]}" push "$SOURCE_DIR/." "$TRIME_DIR/"

# adb 会保留本机文件时间；更新时间可确保用户稍后手动部署时重新编译。
"${ADB[@]}" shell touch \
  "$TRIME_DIR/default.custom.yaml" \
  "$TRIME_DIR/rime.lua" \
  "$TRIME_DIR/thmy.schema.yaml" \
  "$TRIME_DIR/thmy.dict.yaml" \
  "$TRIME_DIR/thmy_code_lookup.tsv" \
  "$TRIME_DIR/thmy_jj.schema.yaml" \
  "$TRIME_DIR/thmy_jj.dict.yaml" \
  "$TRIME_DIR/thmy_jj_code_lookup.tsv" \
  "$TRIME_DIR/thmy_dvorak.trime.yaml"

printf '同步完成：未执行部署。请在手机同文输入法中手动点“部署”。\n'
