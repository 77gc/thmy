#!/bin/sh

set -eu

ROOT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
RIME_DIR="${RIME_DIR:-$HOME/Library/Rime}"
SQUIRREL_DIR="${SQUIRREL_DIR:-/Library/Input Methods/Squirrel.app/Contents}"
SHARED_DIR="${SHARED_DIR:-$SQUIRREL_DIR/SharedSupport}"
DEPLOYER="${DEPLOYER:-$SQUIRREL_DIR/MacOS/rime_deployer}"

if [ ! -x "$DEPLOYER" ]; then
  echo "missing rime_deployer: $DEPLOYER" >&2
  exit 1
fi

mkdir -p "$RIME_DIR"

sh "$ROOT_DIR/scripts/build.sh"

cp "$ROOT_DIR/rime/thmy.dict.yaml" "$RIME_DIR/thmy.dict.yaml"
cp "$ROOT_DIR/rime/thmy.schema.yaml" "$RIME_DIR/thmy.schema.yaml"

"$DEPLOYER" --compile "$RIME_DIR/thmy.schema.yaml" "$RIME_DIR" "$SHARED_DIR" "$RIME_DIR/build"

echo "Deployed thmy to $RIME_DIR"
