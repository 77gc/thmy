#!/usr/bin/env python3
"""Build a text-to-code lookup index from generated Rime dictionaries."""

from __future__ import annotations

import argparse
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class CodeEntry:
    code: str
    weight: int
    source: str
    line_number: int
    selection_rank: int | None = None


def parse_weight(raw: str | None) -> int:
    if raw is None:
        return 0
    try:
        return int(float(raw))
    except ValueError:
        return 0


def iter_rime_dict(path: Path, source: str):
    in_data = False
    with path.open("r", encoding="utf-8") as handle:
        for line_number, raw_line in enumerate(handle, 1):
            line = raw_line.rstrip("\n")
            if not in_data:
                if line.strip() == "...":
                    in_data = True
                continue
            if not line or line.startswith("#"):
                continue
            parts = line.split("\t")
            if len(parts) < 2:
                continue
            text, code = parts[0], parts[1]
            if not text or not code:
                continue
            yield text, CodeEntry(
                code=code,
                weight=parse_weight(parts[2] if len(parts) > 2 else None),
                source=source,
                line_number=line_number,
            )


def display_code(entry: CodeEntry) -> str:
    suffixes = ["", "'", ",", "."]
    suffix = ""
    if entry.selection_rank is not None:
        if 1 <= entry.selection_rank <= len(suffixes):
            suffix = suffixes[entry.selection_rank - 1]
        elif entry.selection_rank > len(suffixes):
            suffix = f"#{entry.selection_rank}"

    if entry.source == "jj":
        return f"jj:{entry.code}{suffix}"
    return f"{entry.code}{suffix}"


def sort_key(entry: CodeEntry):
    compact = entry.code.replace(" ", "").replace(";", "")
    source_rank = 0 if entry.source == "ym" else 1
    low_weight_rank = 1 if entry.weight < 1_000_000 else 0
    hard_to_select_rank = (
        1
        if len(compact) <= 2
        and entry.selection_rank is not None
        and entry.selection_rank > 4
        else 0
    )
    delimiter_rank = 1 if ";" in entry.code else 0
    space_rank = 1 if " " in entry.code else 0
    return (
        source_rank,
        low_weight_rank,
        hard_to_select_rank,
        len(compact),
        delimiter_rank,
        space_rank,
        -entry.weight,
        entry.code,
    )


def with_selection_ranks(entries: list[tuple[str, CodeEntry]]) -> list[tuple[str, CodeEntry]]:
    by_code: dict[str, list[tuple[str, CodeEntry]]] = defaultdict(list)
    for text, entry in entries:
        by_code[entry.code].append((text, entry))

    ranks_by_identity: dict[tuple[str, str, int], int] = {}
    for code_entries in by_code.values():
        ordered = sorted(
            code_entries,
            key=lambda item: (-item[1].weight, item[1].line_number, item[0]),
        )
        for rank, (text, entry) in enumerate(ordered, 1):
            ranks_by_identity[(text, entry.code, entry.line_number)] = rank

    ranked: list[tuple[str, CodeEntry]] = []
    for text, entry in entries:
        ranked.append(
            (
                text,
                CodeEntry(
                    code=entry.code,
                    weight=entry.weight,
                    source=entry.source,
                    line_number=entry.line_number,
                    selection_rank=ranks_by_identity[(text, entry.code, entry.line_number)],
                ),
            )
        )
    return ranked


def build_index(dicts: list[tuple[Path, str]], max_codes: int) -> dict[str, list[str]]:
    grouped: dict[str, list[CodeEntry]] = defaultdict(list)
    for path, source in dicts:
        entries = with_selection_ranks(list(iter_rime_dict(path, source)))
        for text, entry in entries:
            grouped[text].append(entry)

    index: dict[str, list[str]] = {}
    for text, entries in grouped.items():
        codes: list[str] = []
        seen: set[str] = set()
        for entry in sorted(entries, key=sort_key):
            code = display_code(entry)
            if code in seen:
                continue
            seen.add(code)
            codes.append(code)
            if len(codes) >= max_codes:
                break
        if codes:
            index[text] = codes
    return index


def write_index(index: dict[str, list[str]], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write("# text\tcodes\n")
        for text in sorted(index):
            if "\t" in text or "\n" in text:
                continue
            handle.write(f"{text}\t{' / '.join(index[text])}\n")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dict", dest="dicts", action="append", type=Path)
    parser.add_argument("--ym-dict", type=Path)
    parser.add_argument("--jj-dict", type=Path)
    parser.add_argument("--max-codes", type=int, default=12)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    dicts: list[tuple[Path, str]] = []
    if args.dicts:
        dicts.extend((path, "table") for path in args.dicts)
    elif args.ym_dict:
        dicts.append((args.ym_dict, "ym"))

    if args.jj_dict:
        dicts.append((args.jj_dict, "jj"))

    if not dicts:
        parser.error("at least one --dict or --ym-dict is required")

    index = build_index(dicts, max_codes=args.max_codes)
    write_index(index, args.output)
    print(f"code lookup entries={len(index)} output={args.output}")


if __name__ == "__main__":
    main()
