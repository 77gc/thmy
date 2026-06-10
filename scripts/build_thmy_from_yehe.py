#!/usr/bin/env python3

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Optional

from char_frequency import (
    CharFrequency,
    ReadingFrequency,
)
from derive_thmy_table import (
    remap_phrase_sound_code,
    remap_pure_phrase_sound_code,
    remap_sound_shape_code,
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

PINYIN_INITIAL_TO_YEHE = {
    "b": "b",
    "p": "p",
    "m": "m",
    "f": "f",
    "d": "d",
    "t": "t",
    "n": "n",
    "l": "l",
    "g": "g",
    "k": "k",
    "h": "h",
    "j": "j",
    "q": "q",
    "x": "x",
    "r": "r",
    "z": "z",
    "c": "c",
    "s": "s",
    "y": "y",
    "w": "w",
    "zh": "v",
    "ch": "i",
    "sh": "u",
}
PINYIN_FINAL_TO_YEHE = {
    "a": "a",
    "ai": "d",
    "an": "j",
    "ang": "h",
    "ao": "c",
    "e": "e",
    "ei": "w",
    "en": "f",
    "eng": "g",
    "er": "r",
    "i": "i",
    "ia": "x",
    "ian": "m",
    "iang": "l",
    "iao": "n",
    "ie": "p",
    "in": "b",
    "ing": "k",
    "iong": "s",
    "iu": "q",
    "o": "o",
    "ong": "s",
    "ou": "z",
    "u": "u",
    "ua": "x",
    "uai": "k",
    "uan": "r",
    "uang": "l",
    "ue": "t",
    "ui": "v",
    "un": "y",
    "uo": "o",
    "v": "v",
    "ve": "t",
}
ZERO_INITIAL_PINYIN_TO_YEHE = {
    "a": "aa",
    "ai": "ai",
    "an": "an",
    "ang": "ah",
    "ao": "ao",
    "e": "ee",
    "ei": "ei",
    "en": "en",
    "eng": "eg",
    "er": "er",
    "o": "oo",
    "ou": "ou",
}


def read_yehe_entries(path: Path) -> list[tuple[str, str]]:
    entries: list[tuple[str, str]] = []
    seen_entries: set[tuple[str, str]] = set()

    for line in path.read_text(encoding="utf-8").splitlines():
        if not line or line.startswith("#") or "\t" not in line:
            continue
        code, text = line.split("\t", 1)
        code = code.lower()
        if len(text) != 1 or len(code) != 4 or not code.isascii() or not code.isalpha():
            continue
        item = (code, text)
        if item in seen_entries:
            continue
        seen_entries.add(item)
        entries.append(item)

    return entries


def pinyin_to_yehe_sound_code(pinyin: str) -> Optional[str]:
    normalized = pinyin.lower().replace("ü", "v")
    if normalized in ZERO_INITIAL_PINYIN_TO_YEHE:
        return ZERO_INITIAL_PINYIN_TO_YEHE[normalized]

    for initial in ("zh", "ch", "sh"):
        if normalized.startswith(initial):
            final = normalized[len(initial) :]
            break
    else:
        initial = normalized[:1]
        final = normalized[1:]

    initial_code = PINYIN_INITIAL_TO_YEHE.get(initial)
    final_code = PINYIN_FINAL_TO_YEHE.get(final)
    if initial_code is None or final_code is None:
        return None
    return initial_code + final_code


def select_primary_codes(
    yehe_entries: list[tuple[str, str]],
    reading_frequency: ReadingFrequency,
) -> dict[str, str]:
    candidates: dict[str, list[tuple[tuple[object, ...], str]]] = {}
    sound_weights: dict[tuple[str, str], int] = {}
    for (text, pinyin), weight in reading_frequency.pinyin_weights.items():
        sound_code = pinyin_to_yehe_sound_code(pinyin)
        if sound_code is None:
            continue
        identity = (text, sound_code)
        sound_weights[identity] = max(weight, sound_weights.get(identity, 0))

    for index, (code, text) in enumerate(yehe_entries):
        pinyin_weight = sound_weights.get((text, code[:2]))
        if pinyin_weight is not None:
            sort_key: tuple[object, ...] = (0, -pinyin_weight, index)
        else:
            reading_weight = reading_frequency.weight(text, code[0])
            if reading_weight is not None:
                reading_priority = (
                    1 if reading_frequency.is_substantial(text, code[0]) else 2
                )
                sort_key = (reading_priority, -reading_weight, index)
            else:
                sort_key = (3, index)
        candidates.setdefault(text, []).append((sort_key, code))

    primary_codes: dict[str, str] = {}
    for text, text_candidates in candidates.items():
        text_candidates.sort(key=lambda item: item[0])
        primary_codes[text] = text_candidates[0][1]
    return primary_codes


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


def phrase_code(text: str, char_codes: dict[str, str]) -> Optional[str]:
    codes = [char_codes.get(char) for char in text]
    if any(code is None for code in codes):
        return None

    full_codes = [code for code in codes if code is not None]
    if len(full_codes) == 2:
        return full_codes[0][:2] + full_codes[1][:2]
    if len(full_codes) == 3:
        return full_codes[0][0] + full_codes[1][0] + full_codes[2][:2]
    if len(full_codes) >= 4:
        return full_codes[0][0] + full_codes[1][0] + full_codes[2][0] + full_codes[-1][0]
    return None


def pure_phrase_code(text: str, char_codes: dict[str, str]) -> Optional[str]:
    codes = [char_codes.get(char) for char in text]
    if any(code is None for code in codes):
        return None

    full_codes = [code for code in codes if code is not None]
    raw_code = "".join(code[:2] for code in full_codes)
    if len(raw_code) > MAX_PURE_PHRASE_CODE_LENGTH:
        return None
    return raw_code


def one_key_abbrevs(
    yehe_entries: list[tuple[str, str]],
    char_frequency: CharFrequency,
    reading_frequency: ReadingFrequency,
    overrides: dict[str, str] | None = None,
) -> dict[str, tuple[str, str]]:
    candidates: dict[str, list[tuple[tuple[object, ...], str, str]]] = {}

    for index, (code, text) in enumerate(yehe_entries):
        remapped = remap_sound_shape_code(code)
        if not remapped:
            continue
        key = remapped[0]
        reading_weight = reading_frequency.weight(text, code[0])
        if reading_weight is None:
            sort_key: tuple[object, ...] = (
                2,
                char_frequency.single_char_sort_rank(text, index),
                index,
                text,
            )
        else:
            reading_priority = (
                0 if reading_frequency.is_substantial(text, code[0]) else 1
            )
            sort_key = (
                reading_priority,
                char_frequency.single_char_sort_rank(text, index),
                -reading_weight,
                index,
                text,
            )
        candidates.setdefault(key, []).append((sort_key, remapped, text))

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
                    (sort_key, remapped, text)
                    for sort_key, remapped, text in candidates[key]
                    if text not in used_text
                ),
                None,
            )
            if available is None:
                empty_keys.add(key)
                continue
            sort_key, remapped, text = available
            choice = (sort_key, key, remapped, text)
            if best_choice is None or choice < best_choice:
                best_choice = choice

        remaining_keys -= empty_keys
        if best_choice is None:
            break

        _sort_key, key, remapped, text = best_choice
        selected[key] = (remapped, text)
        used_text.add(text)
        remaining_keys.remove(key)

    if overrides:
        for key, text in overrides.items():
            for _sort_key, remapped, cand_text in candidates.get(key, []):
                if cand_text == text:
                    selected[key] = (remapped, text)
                    break
    return selected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("yehe_sound_shape")
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
        help="TSV file with character<TAB>key<TAB>weight for one-key readings",
    )
    parser.add_argument(
        "--fallback-source-phrases",
        action="store_true",
        help="keep original phrase code when Yehe cannot encode every character",
    )
    parser.add_argument(
        "--custom-entries",
        action="append",
        default=[],
        help="TSV file with code<TAB>text entries to merge into the SIT table",
    )
    args = parser.parse_args()

    yehe_entries = read_yehe_entries(Path(args.yehe_sound_shape))
    source_entries = iter_source_entries(Path(args.phrase_source))
    char_frequency = CharFrequency.load(args.char_frequency)
    reading_frequency = ReadingFrequency.load(args.reading_frequency)
    primary_codes = select_primary_codes(yehe_entries, reading_frequency)

    output: list[str] = HEADER.splitlines()
    seen_output: set[tuple[str, str]] = set()
    one_key_count = 0
    abbrev_count = 0
    custom_count = 0

    one_keys = one_key_abbrevs(yehe_entries, char_frequency, reading_frequency, overrides={'m': '没', 'o': '喔'})
    for key, (_full_code, text) in sorted(one_keys.items()):
        item = (key, text)
        if item in seen_output:
            continue
        seen_output.add(item)
        output.append(f"{key}\t{text}")
        one_key_count += 1

    for code, text in yehe_entries:
        remapped = remap_sound_shape_code(code)
        abbrev = remapped[:2]
        for candidate_code in (abbrev, remapped):
            item = (candidate_code, text)
            if item in seen_output:
                continue
            seen_output.add(item)
            output.append(f"{candidate_code}\t{text}")
            if candidate_code == abbrev:
                abbrev_count += 1

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
    fallback_count = 0
    skipped_count = 0
    seen_phrases: set[str] = set()

    for source_code, text in source_entries:
        if len(text) <= 1 or text in seen_phrases:
            continue
        seen_phrases.add(text)

        code = phrase_code(text, primary_codes)
        if code is None:
            if args.fallback_source_phrases and source_code.isascii() and source_code.isalpha():
                remapped = remap_phrase_sound_code(source_code.lower(), text)
                fallback_count += 1
            else:
                skipped_count += 1
                continue
        else:
            remapped = remap_phrase_sound_code(code, text)
            phrase_count += 1

        phrase_items = [(remapped, text)]
        pure_code = pure_phrase_code(text, primary_codes)
        if pure_code is not None:
            pure_remapped = remap_pure_phrase_sound_code(pure_code)
            phrase_items.append((pure_remapped, text))

        for item in phrase_items:
            if item in seen_output:
                continue
            seen_output.add(item)
            output.append(f"{item[0]}\t{item[1]}")
            if item[0] != remapped:
                pure_phrase_count += 1

    Path(args.output).write_text("\n".join(output) + "\n", encoding="utf-8")
    print(
        "build_thmy_from_yehe:",
        f"chars={len(yehe_entries)}",
        f"one_key_abbrevs={one_key_count}",
        f"char_abbrevs={abbrev_count}",
        f"custom_entries={custom_count}",
        f"phrases={phrase_count}",
        f"pure_phrases={pure_phrase_count}",
        f"fallback_phrases={fallback_count}",
        f"skipped_phrases={skipped_count}",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
