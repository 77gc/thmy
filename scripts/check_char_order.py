#!/usr/bin/env python3

from __future__ import annotations

import argparse
import sys
from collections import defaultdict
from pathlib import Path

from char_frequency import ReadingFrequency


def load_char_ranks(path: Path) -> dict[str, int]:
    ranks: dict[str, int] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line or line.startswith("#"):
            continue
        rank_text, char, *_rest = line.split("\t")
        ranks[char] = int(rank_text)
    return ranks


def load_custom_entries(paths: list[str]) -> set[tuple[str, str]]:
    custom: set[tuple[str, str]] = set()
    for path_text in paths:
        path = Path(path_text)
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "\t" not in line:
                raise ValueError(f"missing tab in custom entry {path}:{line_number}")
            code, text = line.split("\t", 1)
            custom.add((text.strip(), code.strip().lower().replace(";", "-")))
    return custom


def load_rime_chars(path: Path) -> dict[str, list[tuple[str, int, int]]]:
    entries: dict[str, list[tuple[str, int, int]]] = defaultdict(list)
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        fields = line.split("\t")
        if len(fields) < 3:
            continue
        text, code, weight_text = fields[:3]
        if len(text) != 1 or ";" in code:
            continue
        entries[code].append((text, int(weight_text), line_number))
    return entries


def actual_order(candidates: list[tuple[str, int, int]]) -> list[tuple[str, int, int]]:
    return sorted(candidates, key=lambda item: (-item[1], item[2], item[0]))


def one_key_tops(
    entries: dict[str, list[tuple[str, int, int]]],
) -> dict[str, str]:
    tops: dict[str, str] = {}
    for code, candidates in entries.items():
        if len(code) == 1 and candidates:
            tops[code] = actual_order(candidates)[0][0]
    return tops


def is_low_weight_alternate(
    text: str,
    code: str,
    reading_frequency: ReadingFrequency | None,
) -> bool:
    if reading_frequency is None or len(code) < 2:
        return False
    sound_code = code[:2]
    return (
        reading_frequency.sound_weight(text, sound_code) is not None
        and not reading_frequency.is_substantial_sound(text, sound_code)
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("dictionary", help="Rime dictionary with text/code/weight columns")
    parser.add_argument("--char-frequency", required=True)
    parser.add_argument("--reading-frequency")
    parser.add_argument("--custom-entries", action="append", default=[])
    parser.add_argument(
        "--limit",
        type=int,
        default=5,
        help="top N non-custom same-code candidates to check",
    )
    args = parser.parse_args()

    ranks = load_char_ranks(Path(args.char_frequency))
    reading_frequency = (
        ReadingFrequency.load(args.reading_frequency) if args.reading_frequency else None
    )
    entries = load_rime_chars(Path(args.dictionary))
    one_key_top = one_key_tops(entries)
    failures: list[str] = []

    for code, candidates in sorted(entries.items()):
        ordered = actual_order(candidates)
        filtered = [
            (text, weight, line_number, ranks[text])
            for text, weight, line_number in ordered
            if (
                text in ranks
                and not is_low_weight_alternate(text, code, reading_frequency)
                and not (len(code) == 2 and one_key_top.get(code[0]) == text)
            )
        ][: args.limit]
        worst_rank = -1
        worst_text = ""
        for position, (text, weight, line_number, rank) in enumerate(filtered, 1):
            if rank < worst_rank:
                failures.append(
                    f"{code}: #{position} {text}(rank={rank}, weight={weight}, "
                    f"line={line_number}) follows {worst_text}(rank={worst_rank})"
                )
                break
            if rank > worst_rank:
                worst_rank = rank
                worst_text = text

    if failures:
        for failure in failures:
            print(failure, file=sys.stderr)
        print(f"char order failures: {len(failures)}", file=sys.stderr)
        return 1

    print(f"char order check passed: top {args.limit}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
