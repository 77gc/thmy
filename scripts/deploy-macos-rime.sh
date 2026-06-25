#!/bin/sh

set -eu

ROOT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
RIME_DIR="${RIME_DIR:-$HOME/Library/Rime}"
SQUIRREL_DIR="${SQUIRREL_DIR:-/Library/Input Methods/Squirrel.app/Contents}"
SHARED_DIR="${SHARED_DIR:-$SQUIRREL_DIR/SharedSupport}"
DEPLOYER="${DEPLOYER:-$SQUIRREL_DIR/MacOS/rime_deployer}"
THMY_DEPLOY_VERBOSE="${THMY_DEPLOY_VERBOSE:-0}"
THMY_WITH_JJ="${THMY_WITH_JJ:-0}"
SQUIRREL_CANDIDATE_FORMAT='[label]- [candidate] [comment]'

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
  mkdir -p "$RIME_DIR/lua"
  cp "$ROOT_DIR/rime/thmy.dict.yaml" "$RIME_DIR/thmy.dict.yaml"
  cp "$ROOT_DIR/rime/thmy.schema.yaml" "$RIME_DIR/thmy.schema.yaml"
  cp "$ROOT_DIR/rime/thmy_code_lookup.tsv" "$RIME_DIR/thmy_code_lookup.tsv"
  cp "$ROOT_DIR/rime/rime.lua" "$RIME_DIR/rime.lua"
  cp "$ROOT_DIR/rime/lua/thmy_code_lookup.lua" "$RIME_DIR/lua/thmy_code_lookup.lua"
  cp "$ROOT_DIR/rime/default.custom.yaml" "$RIME_DIR/default.custom.yaml"

  if [ "$THMY_WITH_JJ" = "1" ]; then
    cp "$ROOT_DIR/rime/thmy_jj.dict.yaml" "$RIME_DIR/thmy_jj.dict.yaml"
    cp "$ROOT_DIR/rime/thmy_jj.schema.yaml" "$RIME_DIR/thmy_jj.schema.yaml"
    cp "$ROOT_DIR/rime/thmy_jj_code_lookup.tsv" "$RIME_DIR/thmy_jj_code_lookup.tsv"
  fi
}

patch_squirrel_candidate_format() {
  python3 - "$RIME_DIR/squirrel.custom.yaml" "$SQUIRREL_CANDIDATE_FORMAT" <<'PY'
from pathlib import Path
import sys

path = Path(sys.argv[1])
candidate_format = sys.argv[2]
target = f'  style/candidate_format: "{candidate_format}"'
lines = path.read_text(encoding="utf-8").splitlines() if path.exists() else []

if not lines:
    lines = ["patch:", target]
else:
    replaced = False
    output = []
    for line in lines:
        if line.lstrip().startswith("style/candidate_format:"):
            output.append(target)
            replaced = True
        else:
            output.append(line)
    lines = output

    patch_index = next((index for index, line in enumerate(lines) if line.strip() == "patch:"), None)
    if patch_index is None:
        lines = ["patch:", target, *lines]
    elif not replaced:
        lines.insert(patch_index + 1, target)

path.write_text("\n".join(lines) + "\n", encoding="utf-8")
PY

  if [ -f "$RIME_DIR/build/squirrel.yaml" ]; then
    python3 - "$RIME_DIR/build/squirrel.yaml" "$SQUIRREL_CANDIDATE_FORMAT" <<'PY'
from pathlib import Path
import sys

path = Path(sys.argv[1])
candidate_format = sys.argv[2]
target = f'  candidate_format: "{candidate_format}"'
lines = path.read_text(encoding="utf-8").splitlines()
output = []
in_style = False
replaced = False

for line in lines:
    if line == "style:":
        in_style = True
        output.append(line)
        continue

    if in_style and line and not line.startswith(" "):
        if not replaced:
            output.append(target)
        in_style = False

    if in_style and line.startswith("  candidate_format:"):
        output.append(target)
        replaced = True
        continue

    output.append(line)

if in_style and not replaced:
    output.append(target)

if not any(line == "style:" for line in lines):
    output.extend(["style:", target])

path.write_text("\n".join(output) + "\n", encoding="utf-8")
PY
  fi
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
run_step "更新鼠须管候选提示格式" patch_squirrel_candidate_format
run_step "编译团码-ym" "$DEPLOYER" --compile "$RIME_DIR/thmy.schema.yaml" "$RIME_DIR" "$SHARED_DIR" "$RIME_DIR/build"
if [ "$THMY_WITH_JJ" = "1" ]; then
  run_step "编译团码-jj" "$DEPLOYER" --compile "$RIME_DIR/thmy_jj.schema.yaml" "$RIME_DIR" "$SHARED_DIR" "$RIME_DIR/build"
fi

step "完成"
if [ "$THMY_WITH_JJ" = "1" ]; then
  echo "已部署团码-ym 和团码-jj 到 ${RIME_DIR}"
else
  echo "已部署团码-ym 到 ${RIME_DIR}；团码-jj 已跳过"
fi
