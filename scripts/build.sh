#!/bin/sh

set -eu
export PYTHONDONTWRITEBYTECODE=1

ROOT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
THMY_WITH_JJ="${THMY_WITH_JJ:-0}"
# rime/ 是唯一权威输出；构建后默认同步到 Android 和 Windows。
THMY_SYNC_PORTS="${THMY_SYNC_PORTS:-1}"
FREQ_FILE="$ROOT_DIR/data/hanzi_frequency_junda.tsv"
READING_FREQ_FILE="$ROOT_DIR/data/hanzi_reading_frequency_baishuang_8105.tsv"
CUSTOM_FILE="$ROOT_DIR/data/thmy_custom.tsv"
PHRASE_FREQ_FILE="$ROOT_DIR/data/phrase_frequency.tsv"
AUX_FILE="$ROOT_DIR/data/thmy_aux.tsv"
AUX_REFERENCE_FILE="$ROOT_DIR/data/thmy_aux_reference.md"
AUX_REFERENCE_TSV_FILE="$ROOT_DIR/data/thmy_aux_reference.tsv"
AUX_KEYMAP_FILE="$ROOT_DIR/data/thmy_aux_keymap.md"
PHRASE_READING_OVERRIDES_FILE="$ROOT_DIR/data/phrase_reading_overrides.tsv"
PHRASE_SOURCE_FILE="$ROOT_DIR/data/phrase_source.txt"
TMP_SOURCE=$(mktemp)
TMP_SORTED=$(mktemp)
trap 'rm -f "$TMP_SOURCE" "$TMP_SORTED"' EXIT

python3 "$ROOT_DIR/scripts/generate_thmy_aux.py" \
  --char-frequency "$FREQ_FILE" \
  --reading-frequency "$READING_FREQ_FILE" \
  --phrase-source "$PHRASE_SOURCE_FILE" \
  --custom-entries "$CUSTOM_FILE" \
  --phrase-reading-overrides "$PHRASE_READING_OVERRIDES_FILE" \
  --report \
  "$AUX_FILE"

python3 "$ROOT_DIR/scripts/generate_thmy_aux_reference.py" \
  --char-frequency "$FREQ_FILE" \
  --reading-frequency "$READING_FREQ_FILE" \
  --aux-codes "$AUX_FILE" \
  --markdown-output "$AUX_REFERENCE_FILE" \
  --tsv-output "$AUX_REFERENCE_TSV_FILE" \
  --keymap-output "$AUX_KEYMAP_FILE" \
  --limit 1000

python3 "$ROOT_DIR/scripts/build_thmy.py" \
  --char-frequency "$FREQ_FILE" \
  --reading-frequency "$READING_FREQ_FILE" \
  --custom-entries "$CUSTOM_FILE" \
  --aux-codes "$AUX_FILE" \
  --phrase-reading-overrides "$PHRASE_READING_OVERRIDES_FILE" \
  "$PHRASE_SOURCE_FILE" \
  "$TMP_SOURCE"

python3 "$ROOT_DIR/scripts/sort_table_source.py" \
  --char-frequency "$FREQ_FILE" \
  --reading-frequency "$READING_FREQ_FILE" \
  --phrase-frequency "$PHRASE_FREQ_FILE" \
  --custom-entries "$CUSTOM_FILE" \
  --dedupe \
  "$TMP_SOURCE" \
  "$ROOT_DIR/THMY.txt"

python3 "$ROOT_DIR/scripts/fcitx_table_to_weighted_rime.py" \
  --name thmy \
  --version "2026-05-18" \
  --char-frequency "$FREQ_FILE" \
  --reading-frequency "$READING_FREQ_FILE" \
  --phrase-frequency "$PHRASE_FREQ_FILE" \
  --custom-entries "$CUSTOM_FILE" \
  "$ROOT_DIR/THMY.txt" \
  "$ROOT_DIR/rime/thmy.dict.yaml"

if [ "$THMY_WITH_JJ" = "1" ]; then
  python3 "$ROOT_DIR/scripts/build_thmy_jj.py" \
    --char-frequency "$FREQ_FILE" \
    --reading-frequency "$READING_FREQ_FILE" \
    --custom-entries "$CUSTOM_FILE" \
    --aux-codes "$AUX_FILE" \
    --phrase-reading-overrides "$PHRASE_READING_OVERRIDES_FILE" \
    --phrase-frequency "$PHRASE_FREQ_FILE" \
    "$PHRASE_SOURCE_FILE" \
    "$ROOT_DIR/rime/thmy_jj.dict.yaml"
fi

python3 "$ROOT_DIR/scripts/build_code_lookup.py" \
  --dict "$ROOT_DIR/rime/thmy.dict.yaml" \
  "$ROOT_DIR/rime/thmy_code_lookup.tsv"

if [ "$THMY_WITH_JJ" = "1" ]; then
  python3 "$ROOT_DIR/scripts/build_code_lookup.py" \
    --dict "$ROOT_DIR/rime/thmy_jj.dict.yaml" \
    "$ROOT_DIR/rime/thmy_jj_code_lookup.tsv"
fi

python3 "$ROOT_DIR/scripts/check_char_order.py" \
  --char-frequency "$FREQ_FILE" \
  --reading-frequency "$READING_FREQ_FILE" \
  --custom-entries "$CUSTOM_FILE" \
  "$ROOT_DIR/rime/thmy.dict.yaml"

if [ "$THMY_SYNC_PORTS" = "1" ]; then
  mkdir -p "$ROOT_DIR/android/lua" "$ROOT_DIR/windows/lua"
  cp "$ROOT_DIR/rime/thmy.dict.yaml" "$ROOT_DIR/android/thmy.dict.yaml"
  cp "$ROOT_DIR/rime/thmy.dict.yaml" "$ROOT_DIR/windows/thmy.dict.yaml"
  cp "$ROOT_DIR/rime/thmy_code_lookup.tsv" "$ROOT_DIR/android/thmy_code_lookup.tsv"
  cp "$ROOT_DIR/rime/thmy_code_lookup.tsv" "$ROOT_DIR/windows/thmy_code_lookup.tsv"
  cp "$ROOT_DIR/rime/rime.lua" "$ROOT_DIR/android/rime.lua"
  cp "$ROOT_DIR/rime/rime.lua" "$ROOT_DIR/windows/rime.lua"
  cp "$ROOT_DIR/rime/lua/thmy_code_lookup.lua" "$ROOT_DIR/android/lua/thmy_code_lookup.lua"
  cp "$ROOT_DIR/rime/lua/thmy_code_lookup.lua" "$ROOT_DIR/windows/lua/thmy_code_lookup.lua"

  if [ "$THMY_WITH_JJ" = "1" ]; then
    cp "$ROOT_DIR/rime/thmy_jj.dict.yaml" "$ROOT_DIR/android/thmy_jj.dict.yaml"
    cp "$ROOT_DIR/rime/thmy_jj.dict.yaml" "$ROOT_DIR/windows/thmy_jj.dict.yaml"
    cp "$ROOT_DIR/rime/thmy_jj_code_lookup.tsv" "$ROOT_DIR/android/thmy_jj_code_lookup.tsv"
    cp "$ROOT_DIR/rime/thmy_jj_code_lookup.tsv" "$ROOT_DIR/windows/thmy_jj_code_lookup.tsv"
  fi
fi

echo "Built THMY table and Rime dictionaries:"
echo "  THMY.txt"
echo "  rime/thmy.dict.yaml"
echo "  rime/thmy_code_lookup.tsv"
if [ "$THMY_SYNC_PORTS" = "1" ]; then
  echo "  android/thmy.dict.yaml"
  echo "  android/thmy_code_lookup.tsv"
  echo "  windows/thmy.dict.yaml"
  echo "  windows/thmy_code_lookup.tsv"
else
  echo "  跳过 Android/Windows 同步；如需同步请设置 THMY_SYNC_PORTS=1"
fi
if [ "$THMY_WITH_JJ" = "1" ]; then
  echo "  rime/thmy_jj.dict.yaml"
  echo "  rime/thmy_jj_code_lookup.tsv"
  if [ "$THMY_SYNC_PORTS" = "1" ]; then
    echo "  android/thmy_jj.dict.yaml"
    echo "  android/thmy_jj_code_lookup.tsv"
    echo "  windows/thmy_jj.dict.yaml"
    echo "  windows/thmy_jj_code_lookup.tsv"
  fi
else
  echo "  跳过团码-jj；如需构建请设置 THMY_WITH_JJ=1"
fi
