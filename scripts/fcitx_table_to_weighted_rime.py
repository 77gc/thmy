#!/usr/bin/env python3

from __future__ import annotations

import argparse
from pathlib import Path

from char_frequency import CharFrequency, ReadingFrequency
from derive_thmy_table import (
    source_initial_for_remapped_key,
    source_sound_for_remapped_code,
)


def read_entries(path: Path) -> list[tuple[str, str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    entries: list[tuple[str, str]] = []
    in_data = False

    for line in lines:
        if line == "[Data]":
            in_data = True
            continue
        if not in_data or not line.strip():
            continue
        if "\t" not in line:
            raise ValueError(f"invalid data line: {line}")
        code, text = line.split("\t", 1)
        code = code.replace(";", "-")
        if code and text:
            entries.append((text, code))

    return entries


def write_rime_dict(
    entries: list[tuple[str, str]],
    output_path: Path,
    name: str,
    version: str,
    char_frequency: CharFrequency,
    reading_frequency: ReadingFrequency | None,
) -> None:
    total_entries = len(entries)
    output: list[str] = [
        "---",
        f"name: {name}",
        f'version: "{version}"',
        "sort: by_weight",
        "use_preset_vocabulary: false",
        "columns:",
        "  - text",
        "  - code",
        "  - weight",
        "...",
    ]

    for index, (text, code) in enumerate(entries):
        weight = char_frequency.rime_weight(text, index, total_entries)
        if len(text) == 1 and code and reading_frequency is not None:
            reading_sound_code = source_sound_for_remapped_code(code)
            if reading_sound_code is not None:
                reading_weight = reading_frequency.sound_weight(text, reading_sound_code)
                is_substantial = reading_frequency.is_substantial_sound(
                    text, reading_sound_code
                )
            else:
                reading_key = source_initial_for_remapped_key(code[0])
                reading_weight = reading_frequency.weight(text, reading_key)
                is_substantial = reading_frequency.is_substantial(text, reading_key)

            if reading_weight is None or not is_substantial:
                weight = 100 + (reading_weight or 0)
        output.append(f"{text}\t{code}\t{weight}")

    output_path.write_text("\n".join(output) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("output")
    parser.add_argument("--name", required=True)
    parser.add_argument("--version", required=True)
    parser.add_argument("--char-frequency", required=True)
    parser.add_argument("--reading-frequency")
    args = parser.parse_args()

    char_frequency = CharFrequency.load(args.char_frequency)
    reading_frequency = (
        ReadingFrequency.load(args.reading_frequency) if args.reading_frequency else None
    )
    entries = read_entries(Path(args.input))
    write_rime_dict(
        entries=entries,
        output_path=Path(args.output),
        name=args.name,
        version=args.version,
        char_frequency=char_frequency,
        reading_frequency=reading_frequency,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
