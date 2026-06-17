#!/usr/bin/env python3

from __future__ import annotations

import argparse
from collections import defaultdict
from pathlib import Path

from build_thmy import primary_sound_codes, substantial_sound_codes
from char_frequency import CharFrequency, ReadingFrequency


def load_aux_codes(path: Path) -> dict[str, str]:
    aux_codes: dict[str, str] = {}
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line or line.startswith("#"):
            continue
        if "\t" not in line:
            raise ValueError(f"missing tab in aux entry {path}:{line_number}")
        char, aux_code = line.split("\t", 1)
        aux_codes[char] = aux_code
    return aux_codes


def write_reference(
    output: Path,
    aux_codes: dict[str, str],
    char_frequency: CharFrequency,
    reading_frequency: ReadingFrequency,
    limit: int,
) -> None:
    primary_codes = primary_sound_codes(reading_frequency)
    substantial_codes = substantial_sound_codes(reading_frequency)
    rows: list[tuple[int, str, str, str, int]] = []

    for char, aux_code in aux_codes.items():
        rank = char_frequency.ranks.get(char, char_frequency.max_rank + 1)
        sound_codes = substantial_codes.get(char) or [primary_codes[char]]
        for sound_code in sound_codes:
            weight = reading_frequency.sound_weight(char, sound_code) or 0
            rows.append((rank, char, sound_code, aux_code, weight))

    rows.sort(key=lambda item: (item[0], item[1], -item[4], item[2]))
    visible_rows = rows[:limit]
    grouped: dict[str, list[tuple[int, str, str, str, int]]] = defaultdict(list)
    for row in visible_rows:
        grouped[row[2][0]].append(row)

    lines = [
        "# THMY 辅助码打法参照表",
        "",
        "本表由 `data/thmy_aux.tsv` 汇总，按字频从高到低排列。",
        "",
        "- `打法` 是实际码表中的连续输入形式，例如 `ded`。",
        "- `分号打法` 是 Rime 派生出的可读输入形式，例如 `de;d`。",
        "- 一字多音时会出现多行，辅码相同，音码不同。",
        "",
        f"## 高频 {len(visible_rows)} 条",
        "",
        "| 排名 | 字 | 音码 | 辅码 | 打法 | 分号打法 |",
        "| ---: | --- | --- | --- | --- | --- |",
    ]

    for rank, char, sound_code, aux_code, _weight in visible_rows:
        lines.append(
            f"| {rank} | {char} | `{sound_code}` | `{aux_code}` | "
            f"`{sound_code}{aux_code}` | `{sound_code};{aux_code}` |"
        )

    lines.extend(["", "## 按首码分组", ""])
    for initial in "abcdefghijklmnopqrstuvwxyz":
        initial_rows = grouped.get(initial, [])
        if not initial_rows:
            continue
        lines.extend(
            [
                f"### `{initial}`",
                "",
                "| 排名 | 字 | 音码 | 辅码 | 打法 | 分号打法 |",
                "| ---: | --- | --- | --- | --- | --- |",
            ]
        )
        for rank, char, sound_code, aux_code, _weight in initial_rows:
            lines.append(
                f"| {rank} | {char} | `{sound_code}` | `{aux_code}` | "
                f"`{sound_code}{aux_code}` | `{sound_code};{aux_code}` |"
            )
        lines.append("")

    output.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_tsv(
    output: Path,
    aux_codes: dict[str, str],
    char_frequency: CharFrequency,
    reading_frequency: ReadingFrequency,
) -> None:
    primary_codes = primary_sound_codes(reading_frequency)
    substantial_codes = substantial_sound_codes(reading_frequency)
    rows: list[tuple[int, str, str, str, int]] = []
    for char, aux_code in aux_codes.items():
        rank = char_frequency.ranks.get(char, char_frequency.max_rank + 1)
        sound_codes = substantial_codes.get(char) or [primary_codes[char]]
        for sound_code in sound_codes:
            weight = reading_frequency.sound_weight(char, sound_code) or 0
            rows.append((rank, char, sound_code, aux_code, weight))
    rows.sort(key=lambda item: (item[0], item[1], -item[4], item[2]))

    lines = ["rank\tchar\tsound_code\taux_code\tinput_code\tdelimited_input\tweight"]
    for rank, char, sound_code, aux_code, weight in rows:
        lines.append(
            "\t".join(
                [
                    str(rank),
                    char,
                    sound_code,
                    aux_code,
                    sound_code + aux_code,
                    sound_code + ";" + aux_code,
                    str(weight),
                ]
            )
        )
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_keymap(
    output: Path,
    aux_codes: dict[str, str],
    char_frequency: CharFrequency,
) -> None:
    single_by_key: dict[str, list[tuple[int, str]]] = defaultdict(list)
    double_initial_counts: dict[str, int] = defaultdict(int)

    for char, aux_code in aux_codes.items():
        rank = char_frequency.ranks.get(char, char_frequency.max_rank + 1)
        if len(aux_code) == 1:
            single_by_key[aux_code].append((rank, char))
        elif len(aux_code) == 2:
            double_initial_counts[aux_code[0]] += 1

    lines = [
        "# THMY 辅助码各键对应表",
        "",
        "本表由 `data/thmy_aux.tsv` 汇总。",
        "",
        "- “单键”表示该字可直接用 `音码 + 该键` 输入。",
        "- “两键首键数”表示完整两键辅码中，以该键开头的字数。",
        "- 辅码是手感优先的无理码，不表达字形。",
        "",
        "| 键 | 单键数 | 两键首键数 | 合计 |",
        "| --- | ---: | ---: | ---: |",
    ]

    for key in "abcdefghijklmnopqrstuvwxyz":
        single_count = len(single_by_key.get(key, []))
        double_count = double_initial_counts.get(key, 0)
        lines.append(f"| `{key}` | {single_count} | {double_count} | {single_count + double_count} |")

    lines.extend(
        [
            "",
            "## 单键对应字",
            "",
            "| 键 | 单键对应字 |",
            "| --- | --- |",
        ]
    )
    for key in "abcdefghijklmnopqrstuvwxyz":
        chars = "".join(
            char for _rank, char in sorted(single_by_key.get(key, []))
        )
        lines.append(f"| `{key}` | {chars} |")

    output.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--aux-codes", required=True)
    parser.add_argument("--char-frequency", required=True)
    parser.add_argument("--reading-frequency", required=True)
    parser.add_argument("--markdown-output", required=True)
    parser.add_argument("--tsv-output", required=True)
    parser.add_argument("--keymap-output")
    parser.add_argument("--limit", type=int, default=1000)
    args = parser.parse_args()

    aux_codes = load_aux_codes(Path(args.aux_codes))
    char_frequency = CharFrequency.load(args.char_frequency)
    reading_frequency = ReadingFrequency.load(args.reading_frequency)
    write_reference(
        output=Path(args.markdown_output),
        aux_codes=aux_codes,
        char_frequency=char_frequency,
        reading_frequency=reading_frequency,
        limit=args.limit,
    )
    write_tsv(
        output=Path(args.tsv_output),
        aux_codes=aux_codes,
        char_frequency=char_frequency,
        reading_frequency=reading_frequency,
    )
    if args.keymap_output:
        write_keymap(
            output=Path(args.keymap_output),
            aux_codes=aux_codes,
            char_frequency=char_frequency,
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
