#!/bin/sh

set -eu

ROOT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
RIME_DIR="${RIME_DIR:-$HOME/Library/Rime}"
SQUIRREL_DIR="${SQUIRREL_DIR:-/Library/Input Methods/Squirrel.app/Contents}"
SHARED_DIR="${SHARED_DIR:-$SQUIRREL_DIR/SharedSupport}"
DEPLOYER="${DEPLOYER:-$SQUIRREL_DIR/MacOS/rime_deployer}"
THMY_DEPLOY_VERBOSE="${THMY_DEPLOY_VERBOSE:-0}"

step() {
  printf '\n==> %s\n' "$*"
}

spinner_frame() {
  case "$1" in
    0) printf '/' ;;
    1) printf '-' ;;
    2) printf '\\' ;;
    *) printf '|' ;;
  esac
}

run_step() {
  label=$1
  shift
  log_file=$(mktemp "${TMPDIR:-/tmp}/thmy-deploy.XXXXXX") || exit 1

  "$@" >"$log_file" 2>&1 &
  pid=$!
  frame=0
  while kill -0 "$pid" 2>/dev/null; do
    printf '\r==> %s %s' "$label" "$(spinner_frame "$frame")"
    frame=$(((frame + 1) % 4))
    sleep 0.1
  done

  if wait "$pid"; then
    printf '\r==> %s 完成\n' "$label"
    if [ "$THMY_DEPLOY_VERBOSE" = "1" ]; then
      sed 's/^/    /' "$log_file"
    fi
    rm -f "$log_file"
    return 0
  else
    status=$?
    printf '\r==> %s 失败\n' "$label" >&2
    sed 's/^/    /' "$log_file" >&2
    rm -f "$log_file"
    exit "$status"
  fi
}

copy_thmy_files() {
  cp "$ROOT_DIR/rime/thmy.dict.yaml" "$RIME_DIR/thmy.dict.yaml"
  cp "$ROOT_DIR/rime/thmy.schema.yaml" "$RIME_DIR/thmy.schema.yaml"
  cp "$ROOT_DIR/rime/thmy_jj.dict.yaml" "$RIME_DIR/thmy_jj.dict.yaml"
  cp "$ROOT_DIR/rime/thmy_jj.schema.yaml" "$RIME_DIR/thmy_jj.schema.yaml"
  cp "$ROOT_DIR/rime/default.custom.yaml" "$RIME_DIR/default.custom.yaml"
}

if [ ! -x "$DEPLOYER" ]; then
  echo "找不到 rime_deployer: $DEPLOYER" >&2
  exit 1
fi

step "Rime 用户目录：$RIME_DIR"
step "部署器路径：$DEPLOYER"

run_step "创建 Rime 用户目录" mkdir -p "$RIME_DIR"
run_step "构建码表和词典" sh "$ROOT_DIR/scripts/build.sh"
run_step "复制团码文件" copy_thmy_files
run_step "编译团码-ym" "$DEPLOYER" --compile "$RIME_DIR/thmy.schema.yaml" "$RIME_DIR" "$SHARED_DIR" "$RIME_DIR/build"
run_step "编译团码-jj" "$DEPLOYER" --compile "$RIME_DIR/thmy_jj.schema.yaml" "$RIME_DIR" "$SHARED_DIR" "$RIME_DIR/build"

step "完成"
echo "已部署团码-ym 和团码-jj 到 $RIME_DIR"
