#!/usr/bin/env python3

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Optional

from char_frequency import (
    CharFrequency,
    ReadingFrequency,
    pinyin_to_sound_code,
)


MAX_PURE_PHRASE_CODE_LENGTH = 32
HEADER = """;fcitx Version 0x03 Table file
KeyCode=abcdefghijklmnopqrstuvwxyz
Length=32
Pinyin=@
PinyinLength=32
Prompt=&
ConstructPhrase=^
[Rule]
e2=p11+p12+p21+p22
e3=p11+p21+p31+p32
a4=p11+p21+p31+n11
[Data]"""


def iter_source_entries(path: Path) -> list[tuple[str, str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    try:
        data_index = lines.index("[Data]")
    except ValueError:
        raise ValueError(f"missing [Data] section: {path}") from None

    entries: list[tuple[str, str]] = []
    for line in lines[data_index + 1 :]:
        if not line.strip() or "\t" not in line:
            continue
        code, text = line.split("\t", 1)
        entries.append((code, text))
    return entries


def iter_custom_entries(path: Path) -> list[tuple[str, str]]:
    entries: list[tuple[str, str]] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "\t" not in line:
            raise ValueError(f"missing tab in custom entry {path}:{line_number}")
        code, text = line.split("\t", 1)
        code = code.strip().lower()
        text = text.strip()
        if not code or not text:
            raise ValueError(f"empty custom entry field {path}:{line_number}")
        if not code.isascii() or not code.isalpha():
            raise ValueError(f"invalid custom entry code {path}:{line_number}: {code}")
        entries.append((code, text))
    return entries


def iter_phrase_reading_overrides(path: Path) -> dict[str, dict[str, str]]:
    overrides: dict[str, dict[str, str]] = {}
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        fields = line.split("\t")
        text = fields[0].strip()
        if not text:
            raise ValueError(f"empty override text {path}:{line_number}")
        text_overrides: dict[str, str] = {}
        for field in fields[1:]:
            if ":" not in field:
                raise ValueError(f"invalid override {path}:{line_number}: {field}")
            char, pinyin = field.split(":", 1)
            char = char.strip()
            pinyin = pinyin.strip()
            if len(char) != 1 or not pinyin:
                raise ValueError(f"invalid override {path}:{line_number}: {field}")
            sound_code = pinyin_to_sound_code(pinyin)
            if sound_code is None:
                raise ValueError(f"unsupported pinyin {path}:{line_number}: {pinyin}")
            text_overrides[char] = sound_code
        overrides[text] = text_overrides
    return overrides


def primary_sound_codes(reading_frequency: ReadingFrequency) -> dict[str, str]:
    candidates: dict[str, list[tuple[tuple[object, ...], str]]] = {}
    for (text, pinyin), weight in reading_frequency.pinyin_weights.items():
        sound_code = pinyin_to_sound_code(pinyin)
        if sound_code is None:
            continue
        sort_key: tuple[object, ...] = (
            0 if reading_frequency.is_substantial_sound(text, sound_code) else 1,
            -weight,
            sound_code,
        )
        candidates.setdefault(text, []).append((sort_key, sound_code))

    primary_codes: dict[str, str] = {}
    for text, text_candidates in candidates.items():
        text_candidates.sort(key=lambda item: item[0])
        primary_codes[text] = text_candidates[0][1]
    return primary_codes


def phrase_char_codes(
    text: str,
    char_codes: dict[str, str],
    phrase_reading_overrides: dict[str, dict[str, str]],
) -> Optional[list[str]]:
    overrides = phrase_reading_overrides.get(text, {})
    codes = [overrides.get(char, char_codes.get(char)) for char in text]
    if any(code is None for code in codes):
        return None
    return [code for code in codes if code is not None]


def phrase_code(full_codes: list[str]) -> Optional[str]:
    if len(full_codes) == 2:
        return full_codes[0][:2] + full_codes[1][:2]
    if len(full_codes) == 3:
        return full_codes[0][0] + full_codes[1][0] + full_codes[2][:2]
    if len(full_codes) >= 4:
        return full_codes[0][0] + full_codes[1][0] + full_codes[2][0] + full_codes[-1][0]
    return None


def pure_phrase_code(full_codes: list[str]) -> Optional[str]:
    raw_code = "".join(code[:2] for code in full_codes)
    if len(raw_code) > MAX_PURE_PHRASE_CODE_LENGTH:
        return None
    return raw_code


def one_key_abbrevs(
    char_codes: dict[str, str],
    char_frequency: CharFrequency,
    reading_frequency: ReadingFrequency,
    overrides: dict[str, str] | None = None,
) -> dict[str, tuple[str, str]]:
    candidates: dict[str, list[tuple[tuple[object, ...], str, str]]] = {}

    for index, (text, code) in enumerate(char_codes.items()):
        key = code[0]
        reading_weight = reading_frequency.sound_weight(text, code)
        if reading_weight is None:
            sort_key: tuple[object, ...] = (
                2,
                char_frequency.single_char_sort_rank(text, index),
                index,
                text,
            )
        else:
            reading_priority = (
                0 if reading_frequency.is_substantial_sound(text, code) else 1
            )
            sort_key = (
                reading_priority,
                char_frequency.single_char_sort_rank(text, index),
                -reading_weight,
                index,
                text,
            )
        candidates.setdefault(key, []).append((sort_key, code, text))

    for key_candidates in candidates.values():
        key_candidates.sort(key=lambda item: item[0])

    selected: dict[str, tuple[str, str]] = {}
    used_text: set[str] = set()
    remaining_keys = set(candidates)

    while remaining_keys:
        best_choice: tuple[tuple[object, ...], str, str, str] | None = None
        empty_keys: set[str] = set()
        for key in sorted(remaining_keys):
            available = next(
                (
                    (sort_key, code, text)
                    for sort_key, code, text in candidates[key]
                    if text not in used_text
                ),
                None,
            )
            if available is None:
                empty_keys.add(key)
                continue
            sort_key, code, text = available
            choice = (sort_key, key, code, text)
            if best_choice is None or choice < best_choice:
                best_choice = choice

        remaining_keys -= empty_keys
        if best_choice is None:
            break

        _sort_key, key, code, text = best_choice
        selected[key] = (code, text)
        used_text.add(text)
        remaining_keys.remove(key)

    if overrides:
        for key, text in overrides.items():
            for _sort_key, code, cand_text in candidates.get(key, []):
                if cand_text == text:
                    selected[key] = (code, text)
                    break
    return selected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("phrase_source")
    parser.add_argument("output")
    parser.add_argument(
        "--char-frequency",
        required=True,
        help="TSV file with rank<TAB>character for one-key abbreviations",
    )
    parser.add_argument(
        "--reading-frequency",
        required=True,
        help="TSV file with character<TAB>key<TAB>weight<TAB>pinyin readings",
    )
    parser.add_argument(
        "--custom-entries",
        action="append",
        default=[],
        help="TSV file with code<TAB>text entries to merge into the table",
    )
    parser.add_argument(
        "--phrase-reading-overrides",
        action="append",
        default=[],
        help="TSV file with text<TAB>char:pinyin phrase reading overrides",
    )
    args = parser.parse_args()

    source_entries = iter_source_entries(Path(args.phrase_source))
    char_frequency = CharFrequency.load(args.char_frequency)
    reading_frequency = ReadingFrequency.load(args.reading_frequency)
    primary_codes = primary_sound_codes(reading_frequency)
    phrase_reading_overrides: dict[str, dict[str, str]] = {}
    for override_path in args.phrase_reading_overrides:
        phrase_reading_overrides.update(
            iter_phrase_reading_overrides(Path(override_path))
        )

    output: list[str] = HEADER.splitlines()
    seen_output: set[tuple[str, str]] = set()
    one_key_count = 0
    char_sound_count = 0
    custom_count = 0

    one_keys = one_key_abbrevs(
        primary_codes,
        char_frequency,
        reading_frequency,
        overrides={"m": "没", "o": "喔"},
    )
    for key, (_full_code, text) in sorted(one_keys.items()):
        item = (key, text)
        if item in seen_output:
            continue
        seen_output.add(item)
        output.append(f"{key}\t{text}")
        one_key_count += 1

    for text, code in primary_codes.items():
        item = (code, text)
        if item in seen_output:
            continue
        seen_output.add(item)
        output.append(f"{code}\t{text}")
        char_sound_count += 1

    for custom_entries in args.custom_entries:
        for code, text in iter_custom_entries(Path(custom_entries)):
            item = (code, text)
            if item in seen_output:
                continue
            seen_output.add(item)
            output.append(f"{code}\t{text}")
            custom_count += 1

    phrase_count = 0
    pure_phrase_count = 0
    skipped_count = 0
    seen_phrases: set[str] = set()

    for _source_code, text in source_entries:
        if len(text) <= 1 or text in seen_phrases:
            continue
        seen_phrases.add(text)

        full_codes = phrase_char_codes(text, primary_codes, phrase_reading_overrides)
        if full_codes is None:
            skipped_count += 1
            continue
        code = phrase_code(full_codes)
        if code is None:
            skipped_count += 1
            continue
        phrase_count += 1

        phrase_items = [(code, text)]
        pure_code = pure_phrase_code(full_codes)
        if pure_code is not None:
            phrase_items.append((pure_code, text))

        for item in phrase_items:
            if item in seen_output:
                continue
            seen_output.add(item)
            output.append(f"{item[0]}\t{item[1]}")
            if item[0] != code:
                pure_phrase_count += 1

    Path(args.output).write_text("\n".join(output) + "\n", encoding="utf-8")
    print(
        "build_thmy:",
        f"chars={len(primary_codes)}",
        f"one_key_abbrevs={one_key_count}",
        f"char_sound_codes={char_sound_count}",
        f"custom_entries={custom_count}",
        f"phrases={phrase_count}",
        f"pure_phrases={pure_phrase_count}",
        f"skipped_phrases={skipped_count}",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
