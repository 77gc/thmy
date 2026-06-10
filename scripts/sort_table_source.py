#!/usr/bin/env python3

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from char_frequency import CharFrequency, ReadingFrequency, table_sort_key


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("output")
    parser.add_argument(
        "--char-frequency",
        help="TSV file with rank<TAB>character for sorting single-character candidates",
    )
    parser.add_argument(
        "--dedupe",
        action="store_true",
        help="drop exact duplicate code/text entries while keeping the first occurrence",
    )
    parser.add_argument(
        "--reading-frequency",
        help="TSV file with character<TAB>key<TAB>weight for suppressing rare polyphonic readings",
    )
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)
    char_frequency = CharFrequency.load(args.char_frequency) if args.char_frequency else None
    reading_frequency = (
        ReadingFrequency.load(args.reading_frequency) if args.reading_frequency else None
    )

    lines = input_path.read_text(encoding="utf-8").splitlines()

    try:
        data_index = lines.index("[Data]")
    except ValueError:
        print("missing [Data] section", file=sys.stderr)
        return 1

    header = lines[: data_index + 1]
    data_lines = lines[data_index + 1 :]
    entries: list[tuple[tuple[object, ...], str]] = []
    seen_entries: set[tuple[str, str]] = set()

    for index, line in enumerate(data_lines):
        if not line.strip():
            continue
        if "\t" not in line:
            print(f"invalid data line: {line}", file=sys.stderr)
            return 1
        code, text = line.split("\t", 1)
        identity = (code.replace(";", "-"), text)
        if args.dedupe:
            if identity in seen_entries:
                continue
            seen_entries.add(identity)
        reading_key = code[0] if code else None
        reading_sound_code = code[:2] if len(text) == 1 and len(code) >= 2 else None
        entries.append(
            (
                table_sort_key(
                    code=code,
                    text=text,
                    index=index,
                    char_frequency=char_frequency,
                    reading_frequency=reading_frequency,
                    reading_key=reading_key,
                    reading_sound_code=reading_sound_code,
                ),
                line,
            )
        )

    # Sort by code, but keep single-character entries ahead of multi-character
    # entries for the same code. If a frequency table is supplied, same-code
    # single-character candidates are ordered by rank; phrases remain stable.
    entries.sort(key=lambda item: item[0])
    output_data = [line for _sort_key, line in entries]

    output_path.write_text(
        "\n".join(header + output_data) + "\n",
        encoding="utf-8",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
