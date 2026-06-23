#!/usr/bin/env python3

from __future__ import annotations

import argparse
from pathlib import Path

from char_frequency import CharFrequency, PhraseFrequency, ReadingFrequency


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
            identity = (text.strip(), code.strip().lower().replace(";", "-"))
            if identity not in ranks:
                ranks[identity] = rank
                rank += 1
    return ranks


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
    phrase_frequency: PhraseFrequency | None,
    custom_ranks: dict[tuple[str, str], int],
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
        phrase_weight = (
            phrase_frequency.rime_weight(
                text=text,
                index=index,
                total_entries=total_entries,
                custom_rank=custom_ranks.get((text, code)),
            )
            if phrase_frequency is not None
            else None
        )
        if phrase_weight is not None:
            weight = phrase_weight
        if len(text) == 1 and code and reading_frequency is not None:
            reading_sound_code = code[:2] if len(code) >= 2 else None
            if reading_sound_code is not None:
                reading_weight = reading_frequency.sound_weight(text, reading_sound_code)
                is_substantial = reading_frequency.is_substantial_sound(
                    text, reading_sound_code
                )
            else:
                reading_key = code[0]
                reading_weight = reading_frequency.weight(text, reading_key)
                is_substantial = reading_frequency.is_substantial(text, reading_key)

            if len(code) == 1 and reading_weight is None:
                weight += reading_frequency.max_weights.get(text, 0)
            elif reading_weight is None or not is_substantial:
                weight = 100 + (reading_weight or 0)
            else:
                weight += reading_weight
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
    parser.add_argument("--phrase-frequency")
    parser.add_argument("--custom-entries", action="append", default=[])
    args = parser.parse_args()

    char_frequency = CharFrequency.load(args.char_frequency)
    reading_frequency = (
        ReadingFrequency.load(args.reading_frequency) if args.reading_frequency else None
    )
    phrase_frequency = (
        PhraseFrequency.load(args.phrase_frequency) if args.phrase_frequency else None
    )
    custom_ranks = load_custom_ranks(args.custom_entries)
    entries = read_entries(Path(args.input))
    write_rime_dict(
        entries=entries,
        output_path=Path(args.output),
        name=args.name,
        version=args.version,
        char_frequency=char_frequency,
        reading_frequency=reading_frequency,
        phrase_frequency=phrase_frequency,
        custom_ranks=custom_ranks,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
