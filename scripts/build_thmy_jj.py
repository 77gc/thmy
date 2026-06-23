#!/usr/bin/env python3

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from build_thmy import (
    iter_aux_codes,
    iter_custom_entries,
    iter_phrase_reading_overrides,
    phrase_char_codes,
    primary_sound_codes,
    substantial_sound_codes,
)
from char_frequency import CharFrequency, PhraseFrequency, ReadingFrequency


VERSION = "2026-05-18"
MAX_SPELLING_LENGTH = 64


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


def rime_weight(
    text: str,
    code: str,
    index: int,
    total_entries: int,
    char_frequency: CharFrequency,
    reading_frequency: ReadingFrequency,
    phrase_frequency: PhraseFrequency | None,
    custom_rank: int | None = None,
) -> int:
    weight = char_frequency.rime_weight(text, index, total_entries)
    phrase_weight = (
        phrase_frequency.rime_weight(
            text=text,
            index=index,
            total_entries=total_entries,
            custom_rank=custom_rank,
        )
        if phrase_frequency is not None
        else None
    )
    if phrase_weight is not None:
        return phrase_weight
    if len(text) != 1:
        return weight

    sound_code = code.split(";", 1)[0]
    reading_weight = reading_frequency.sound_weight(text, sound_code)
    if reading_weight is None:
        return weight
    if not reading_frequency.is_substantial_sound(text, sound_code):
        return 100 + reading_weight
    return weight + reading_weight


def add_entry(
    entries: list[tuple[str, str]],
    seen: set[tuple[str, str]],
    text: str,
    code: str,
) -> bool:
    item = (text, code)
    if item in seen:
        return False
    seen.add(item)
    entries.append(item)
    return True


def load_custom_ranks(paths: list[str]) -> dict[tuple[str, str], int]:
    ranks: dict[tuple[str, str], int] = {}
    rank = 0
    for path_text in paths:
        path = Path(path_text)
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "\t" not in line:
                raise ValueError(f"missing tab in custom entry {path}:{line_number}")
            code, text = line.split("\t", 1)
            code = code.strip().lower()
            text = text.strip()
            if len(code) != len(text) * 2:
                continue
            spelling = spelling_from_codes(
                [code[index : index + 2] for index in range(0, len(code), 2)]
            )
            if spelling is None:
                continue
            identity = (text, spelling)
            if identity not in ranks:
                ranks[identity] = rank
                rank += 1
    return ranks


def spelling_from_codes(codes: list[str]) -> str | None:
    raw_code = "".join(codes)
    if len(raw_code) > MAX_SPELLING_LENGTH:
        return None
    return " ".join(codes)


def write_rime_dict(
    output_path: Path,
    entries: list[tuple[str, str]],
    char_frequency: CharFrequency,
    reading_frequency: ReadingFrequency,
    phrase_frequency: PhraseFrequency | None,
    custom_ranks: dict[tuple[str, str], int],
) -> None:
    total_entries = len(entries)
    output = [
        "---",
        "name: thmy_jj",
        f'version: "{VERSION}"',
        "sort: by_weight",
        "use_preset_vocabulary: false",
        "columns:",
        "  - text",
        "  - code",
        "  - weight",
        "...",
    ]

    for index, (text, code) in enumerate(entries):
        weight = rime_weight(
            text=text,
            code=code,
            index=index,
            total_entries=total_entries,
            char_frequency=char_frequency,
            reading_frequency=reading_frequency,
            phrase_frequency=phrase_frequency,
            custom_rank=custom_ranks.get((text, code)),
        )
        output.append(f"{text}\t{code}\t{weight}")

    output_path.write_text("\n".join(output) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("phrase_source")
    parser.add_argument("output")
    parser.add_argument("--char-frequency", required=True)
    parser.add_argument("--reading-frequency", required=True)
    parser.add_argument("--custom-entries", action="append", default=[])
    parser.add_argument("--aux-codes", action="append", default=[])
    parser.add_argument("--phrase-reading-overrides", action="append", default=[])
    parser.add_argument("--phrase-frequency")
    args = parser.parse_args()

    source_entries = iter_source_entries(Path(args.phrase_source))
    char_frequency = CharFrequency.load(args.char_frequency)
    reading_frequency = ReadingFrequency.load(args.reading_frequency)
    phrase_frequency = (
        PhraseFrequency.load(args.phrase_frequency) if args.phrase_frequency else None
    )
    custom_ranks = load_custom_ranks(args.custom_entries)
    primary_codes = primary_sound_codes(reading_frequency)
    single_char_codes = substantial_sound_codes(reading_frequency)

    aux_codes: dict[str, list[str]] = {}
    for aux_path in args.aux_codes:
        aux_codes.update(iter_aux_codes(Path(aux_path)))

    phrase_reading_overrides: dict[str, dict[str, str]] = {}
    for override_path in args.phrase_reading_overrides:
        phrase_reading_overrides.update(
            iter_phrase_reading_overrides(Path(override_path))
        )

    entries: list[tuple[str, str]] = []
    seen: set[tuple[str, str]] = set()
    char_count = 0
    aux_count = 0
    custom_count = 0
    phrase_count = 0
    skipped_count = 0

    for text, primary_code in primary_codes.items():
        for sound_code in single_char_codes.get(text, [primary_code]):
            if add_entry(entries, seen, text, sound_code):
                char_count += 1
            for aux_code in aux_codes.get(text, []):
                if add_entry(entries, seen, text, f"{sound_code};{aux_code}"):
                    aux_count += 1

    for custom_entries in args.custom_entries:
        for code, text in iter_custom_entries(Path(custom_entries)):
            if len(code) != len(text) * 2:
                continue
            spelling = spelling_from_codes(
                [code[index : index + 2] for index in range(0, len(code), 2)]
            )
            if spelling is not None and add_entry(entries, seen, text, spelling):
                custom_count += 1

    seen_phrases: set[str] = set()
    for _source_code, text in source_entries:
        if len(text) <= 1 or text in seen_phrases:
            continue
        seen_phrases.add(text)

        full_codes = phrase_char_codes(text, primary_codes, phrase_reading_overrides)
        if full_codes is None:
            skipped_count += 1
            continue
        spelling = spelling_from_codes(full_codes)
        if spelling is None:
            skipped_count += 1
            continue
        if add_entry(entries, seen, text, spelling):
            phrase_count += 1

    write_rime_dict(
        output_path=Path(args.output),
        entries=entries,
        char_frequency=char_frequency,
        reading_frequency=reading_frequency,
        phrase_frequency=phrase_frequency,
        custom_ranks=custom_ranks,
    )
    print(
        "build_thmy_jj:",
        f"chars={char_count}",
        f"aux_codes={aux_count}",
        f"custom_entries={custom_count}",
        f"phrases={phrase_count}",
        f"skipped_phrases={skipped_count}",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
