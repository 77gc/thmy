#!/usr/bin/env python3

from __future__ import annotations

import argparse
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from build_thmy import (
    DVORAK_FINGERS,
    DVORAK_POSITIONS,
    dvorak_distance,
    dvorak_hand,
    iter_custom_entries,
    iter_phrase_reading_overrides,
    iter_source_entries,
    phrase_char_codes,
    phrase_code,
    primary_sound_codes,
    substantial_sound_codes,
)
from char_frequency import CharFrequency, ReadingFrequency


LETTERS = "abcdefghijklmnopqrstuvwxyz"
SINGLE_AUX_CODES = list(LETTERS)
DOUBLE_AUX_CODES = [left + right for left in LETTERS for right in LETTERS]
ALL_AUX_CODES = SINGLE_AUX_CODES + DOUBLE_AUX_CODES
UNRANKED_RANK_OFFSET = 50_000
AUX_KEY_LOAD_WEIGHT = 0.00657308
AUX_FINGER_LOAD_WEIGHT = 0.0000091133
AUX_HAND_LOAD_WEIGHT = 0.0000184627
AUX_QUICK_SELECT_CANDIDATES = 4
AUX_SAME_CODE_SLOT_WEIGHT = 3_001
AUX_SAME_CODE_OVERFLOW_WEIGHT = 57_735
AUX_PHRASE_CODE_COLLISION_WEIGHT = 125


@dataclass(frozen=True)
class CodeMetrics:
    big_same_finger: int
    same_finger: int
    repeat_key: int
    same_hand: int
    hand_imbalance: int
    distance: int
    length: int


@dataclass
class AuxAssignment:
    char: str
    aux_code: str
    score: float


def is_same_finger_stretch(
    left: str,
    right: str,
    pair_distance: int | None = None,
) -> bool:
    if left == right:
        return False
    if DVORAK_FINGERS[left] != DVORAK_FINGERS[right]:
        return False
    left_row, _left_col = DVORAK_POSITIONS[left]
    right_row, _right_col = DVORAK_POSITIONS[right]
    return abs(left_row - right_row) >= 2


def code_metrics(sound_code: str, aux_code: str) -> CodeMetrics:
    code = sound_code + aux_code
    hand_counts = Counter(dvorak_hand(key) for key in code)
    big_same_finger = 0
    same_finger = 0
    repeat_key = 0
    same_hand = 0
    distance = 0

    for left, right in zip(code, code[1:]):
        pair_distance = dvorak_distance(left, right)
        distance += pair_distance
        if dvorak_hand(left) == dvorak_hand(right):
            same_hand += 1
        if DVORAK_FINGERS[left] == DVORAK_FINGERS[right]:
            same_finger += 1
            if is_same_finger_stretch(left, right, pair_distance):
                big_same_finger += 1
        if left == right:
            repeat_key += 1

    return CodeMetrics(
        big_same_finger=big_same_finger,
        same_finger=same_finger,
        repeat_key=repeat_key,
        same_hand=same_hand,
        hand_imbalance=abs(hand_counts["L"] - hand_counts["R"]),
        distance=distance,
        length=len(aux_code),
    )


def aux_transition_metrics(sound_code: str, aux_code: str) -> CodeMetrics:
    code = sound_code + aux_code
    hand_counts = Counter(dvorak_hand(key) for key in aux_code)
    big_same_finger = 0
    same_finger = 0
    repeat_key = 0
    same_hand = 0
    distance = 0
    first_aux_pair_index = max(len(sound_code) - 1, 0)

    for index, (left, right) in enumerate(zip(code, code[1:])):
        if index < first_aux_pair_index:
            continue
        pair_distance = dvorak_distance(left, right)
        distance += pair_distance
        if dvorak_hand(left) == dvorak_hand(right):
            same_hand += 1
        if DVORAK_FINGERS[left] == DVORAK_FINGERS[right]:
            same_finger += 1
            if is_same_finger_stretch(left, right, pair_distance):
                big_same_finger += 1
        if left == right:
            repeat_key += 1

    return CodeMetrics(
        big_same_finger=big_same_finger,
        same_finger=same_finger,
        repeat_key=repeat_key,
        same_hand=same_hand,
        hand_imbalance=abs(hand_counts["L"] - hand_counts["R"]),
        distance=distance,
        length=len(aux_code),
    )


def metric_score(metrics: CodeMetrics) -> int:
    return (
        metrics.big_same_finger * 30_000
        + metrics.same_finger * 8_000
        + metrics.repeat_key * 5_000
        + metrics.length * 2_500
        + metrics.hand_imbalance * 900
        + metrics.same_hand * 700
        + metrics.distance * 45
    )


def aux_transition_score(metrics: CodeMetrics) -> int:
    return (
        metrics.big_same_finger * 50_000
        + metrics.same_finger * 12_000
        + metrics.repeat_key * 10_000
    )


def sound_weights_for_char(
    char: str,
    sound_codes: Iterable[str],
    reading_frequency: ReadingFrequency,
) -> dict[str, int]:
    weights: dict[str, int] = {}
    for sound_code in sound_codes:
        weights[sound_code] = reading_frequency.sound_weight(char, sound_code) or 1
    return weights


def weighted_metric_score(
    char: str,
    aux_code: str,
    char_sound_weights: dict[str, dict[str, int]],
) -> float:
    sound_weights = char_sound_weights[char]
    total_weight = sum(sound_weights.values()) or 1
    weighted_score = 0
    for sound_code, weight in sound_weights.items():
        weighted_score += metric_score(code_metrics(sound_code, aux_code)) * weight
    return weighted_score / total_weight


def weighted_aux_transition_score(
    char: str,
    aux_code: str,
    char_sound_weights: dict[str, dict[str, int]],
) -> float:
    sound_weights = char_sound_weights[char]
    total_weight = sum(sound_weights.values()) or 1
    weighted_score = 0
    for sound_code, weight in sound_weights.items():
        weighted_score += (
            aux_transition_score(aux_transition_metrics(sound_code, aux_code)) * weight
        )
    return weighted_score / total_weight


def char_priority(
    char: str,
    char_frequency: CharFrequency,
    char_sound_weights: dict[str, dict[str, int]],
) -> tuple[object, ...]:
    rank = char_frequency.ranks.get(char, char_frequency.max_rank + UNRANKED_RANK_OFFSET)
    best_reading_weight = max(char_sound_weights[char].values(), default=0)
    reading_count = len(char_sound_weights[char])
    return (rank, -best_reading_weight, -reading_count, char)


def phrase_code_loads(
    phrase_source: Path,
    custom_entries: list[Path],
    primary_codes: dict[str, str],
    phrase_reading_overrides: dict[str, dict[str, str]],
) -> Counter[str]:
    code_loads: Counter[str] = Counter()

    for _source_code, text in iter_source_entries(phrase_source):
        if len(text) <= 1:
            continue
        full_codes = phrase_char_codes(text, primary_codes, phrase_reading_overrides)
        if full_codes is None:
            continue
        code = phrase_code(full_codes)
        if code is not None and len(code) in (3, 4):
            code_loads[code] += 1

    for custom_path in custom_entries:
        for code, text in iter_custom_entries(custom_path):
            if len(text) > 1 and len(code) in (3, 4):
                code_loads[code] += 1

    return code_loads


def available_aux_codes() -> Iterable[str]:
    yield from ALL_AUX_CODES


def load_char_sound_weights(
    reading_frequency: ReadingFrequency,
) -> dict[str, dict[str, int]]:
    single_char_codes = substantial_sound_codes(reading_frequency)
    return {
        char: sound_weights_for_char(char, sound_codes, reading_frequency)
        for char, sound_codes in single_char_codes.items()
        if sound_codes
    }


def soft_collision_score(
    char: str,
    aux_code: str,
    char_sound_weights: dict[str, dict[str, int]],
    assigned_by_sound: dict[str, Counter[str]],
    phrase_code_counts: Counter[str],
) -> float:
    sound_weights = char_sound_weights[char]
    total_weight = sum(sound_weights.values()) or 1
    weighted_score = 0.0

    for sound_code, weight in sound_weights.items():
        existing_count = assigned_by_sound[sound_code][aux_code]
        overflow_count = max(
            0,
            existing_count + 1 - AUX_QUICK_SELECT_CANDIDATES,
        )
        score = (
            existing_count * AUX_SAME_CODE_SLOT_WEIGHT
            + overflow_count * overflow_count * AUX_SAME_CODE_OVERFLOW_WEIGHT
            + phrase_code_counts[sound_code + aux_code]
            * AUX_PHRASE_CODE_COLLISION_WEIGHT
        )
        weighted_score += score * weight

    return weighted_score / total_weight


def choose_aux_code(
    char: str,
    assigned_by_sound: dict[str, Counter[str]],
    char_sound_weights: dict[str, dict[str, int]],
    phrase_code_counts: Counter[str],
    aux_key_load: Counter[str],
    aux_finger_load: Counter[str],
    aux_hand_load: Counter[str],
) -> AuxAssignment:
    best_assignment: AuxAssignment | None = None
    char_weight = max(char_sound_weights[char].values(), default=1)

    for aux_code in available_aux_codes():
        score = weighted_metric_score(
            char,
            aux_code,
            char_sound_weights,
        ) + weighted_aux_transition_score(
            char,
            aux_code,
            char_sound_weights,
        ) + soft_collision_score(
            char=char,
            aux_code=aux_code,
            char_sound_weights=char_sound_weights,
            assigned_by_sound=assigned_by_sound,
            phrase_code_counts=phrase_code_counts,
        )
        for key in aux_code:
            score += aux_key_load[key] * AUX_KEY_LOAD_WEIGHT
            score += aux_finger_load[DVORAK_FINGERS[key]] * AUX_FINGER_LOAD_WEIGHT
            score += aux_hand_load[dvorak_hand(key)] * AUX_HAND_LOAD_WEIGHT
        assignment = AuxAssignment(char=char, aux_code=aux_code, score=score)
        if best_assignment is None:
            best_assignment = assignment
            continue
        if (assignment.score, len(aux_code), aux_code) < (
            best_assignment.score,
            len(best_assignment.aux_code),
            best_assignment.aux_code,
        ):
            best_assignment = assignment

    if best_assignment is None:
        raise RuntimeError(f"no auxiliary code available for {char}")

    for sound_code in char_sound_weights[char]:
        assigned_by_sound[sound_code][best_assignment.aux_code] += 1
    for key in best_assignment.aux_code:
        aux_key_load[key] += char_weight
        aux_finger_load[DVORAK_FINGERS[key]] += char_weight
        aux_hand_load[dvorak_hand(key)] += char_weight
    return best_assignment


def generate_assignments(
    char_frequency: CharFrequency,
    reading_frequency: ReadingFrequency,
    phrase_source: Path,
    custom_entries: list[Path],
    phrase_reading_overrides: dict[str, dict[str, str]],
) -> list[AuxAssignment]:
    primary_codes = primary_sound_codes(reading_frequency)
    char_sound_weights = load_char_sound_weights(reading_frequency)
    phrase_code_counts = phrase_code_loads(
        phrase_source=phrase_source,
        custom_entries=custom_entries,
        primary_codes=primary_codes,
        phrase_reading_overrides=phrase_reading_overrides,
    )
    chars = sorted(
        char_sound_weights,
        key=lambda char: char_priority(
            char,
            char_frequency,
            char_sound_weights,
        ),
    )
    assigned_by_sound: dict[str, Counter[str]] = defaultdict(Counter)
    aux_key_load: Counter[str] = Counter()
    aux_finger_load: Counter[str] = Counter()
    aux_hand_load: Counter[str] = Counter()
    assignments: list[AuxAssignment] = []

    for char in chars:
        assignments.append(
            choose_aux_code(
                char=char,
                assigned_by_sound=assigned_by_sound,
                char_sound_weights=char_sound_weights,
                phrase_code_counts=phrase_code_counts,
                aux_key_load=aux_key_load,
                aux_finger_load=aux_finger_load,
                aux_hand_load=aux_hand_load,
            )
        )

    return assignments


def assignment_report(
    assignments: list[AuxAssignment],
    reading_frequency: ReadingFrequency,
) -> str:
    char_sound_weights = load_char_sound_weights(reading_frequency)
    length_counts = Counter(len(assignment.aux_code) for assignment in assignments)
    metric_totals = Counter()
    weighted_metric_totals = Counter()
    added_metric_totals = Counter()
    weighted_added_metric_totals = Counter()
    reading_count = 0
    total_weight = 0
    assigned_by_sound: dict[str, set[str]] = defaultdict(set)
    collisions = 0

    for assignment in assignments:
        for sound_code, weight in char_sound_weights[assignment.char].items():
            full_code = sound_code + assignment.aux_code
            if full_code in assigned_by_sound[sound_code]:
                collisions += 1
            assigned_by_sound[sound_code].add(full_code)
            metrics = code_metrics(sound_code, assignment.aux_code)
            added_metrics = aux_transition_metrics(sound_code, assignment.aux_code)
            reading_count += 1
            total_weight += weight
            for field in (
                "big_same_finger",
                "same_finger",
                "repeat_key",
                "same_hand",
                "hand_imbalance",
                "distance",
            ):
                value = getattr(metrics, field)
                metric_totals[field] += value
                weighted_metric_totals[field] += value * weight
                added_value = getattr(added_metrics, field)
                added_metric_totals[field] += added_value
                weighted_added_metric_totals[field] += added_value * weight

    average = {
        field: metric_totals[field] / max(reading_count, 1)
        for field in metric_totals
    }
    weighted_average = {
        field: weighted_metric_totals[field] / max(total_weight, 1)
        for field in weighted_metric_totals
    }
    weighted_added_average = {
        field: weighted_added_metric_totals[field] / max(total_weight, 1)
        for field in weighted_added_metric_totals
    }
    return "\n".join(
        [
            "generate_thmy_aux:",
            f"  chars={len(assignments)}",
            f"  one_letter={length_counts[1]}",
            f"  two_letter={length_counts[2]}",
            f"  readings={reading_count}",
            f"  collisions={collisions}",
            "  average="
            + " ".join(f"{key}={value:.3f}" for key, value in sorted(average.items())),
            "  weighted_average="
            + " ".join(
                f"{key}={value:.3f}" for key, value in sorted(weighted_average.items())
            ),
            "  weighted_aux_added="
            + " ".join(
                f"{key}={value:.3f}"
                for key, value in sorted(weighted_added_average.items())
            ),
        ]
    )


def write_aux_table(output: Path, assignments: list[AuxAssignment]) -> None:
    lines = [
        "# THMY native auxiliary codes.",
        "# Generated by scripts/generate_thmy_aux.py; do not edit by hand.",
        "# Columns: character<TAB>aux_code",
        "#",
        "# Codes are arbitrary comfort-first disambiguators. They are assigned",
        "# against each character's sound-code context, with Dvorak same-finger,",
        "# same-hand, large-stretch, distance, and load-balance metrics.",
    ]
    lines.extend(f"{assignment.char}\t{assignment.aux_code}" for assignment in assignments)
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("output")
    parser.add_argument("--char-frequency", required=True)
    parser.add_argument("--reading-frequency", required=True)
    parser.add_argument("--phrase-source", required=True)
    parser.add_argument(
        "--phrase-reading-overrides",
        action="append",
        default=[],
        help="TSV file with text<TAB>char:pinyin phrase reading overrides",
    )
    parser.add_argument(
        "--custom-entries",
        action="append",
        default=[],
        help="TSV file with code<TAB>text entries to avoid for 3/4-code phrases",
    )
    parser.add_argument("--report", action="store_true")
    args = parser.parse_args()

    char_frequency = CharFrequency.load(args.char_frequency)
    reading_frequency = ReadingFrequency.load(args.reading_frequency)
    phrase_reading_overrides: dict[str, dict[str, str]] = {}
    for override_path in args.phrase_reading_overrides:
        phrase_reading_overrides.update(
            iter_phrase_reading_overrides(Path(override_path))
        )
    assignments = generate_assignments(
        char_frequency=char_frequency,
        reading_frequency=reading_frequency,
        phrase_source=Path(args.phrase_source),
        custom_entries=[Path(path) for path in args.custom_entries],
        phrase_reading_overrides=phrase_reading_overrides,
    )
    write_aux_table(Path(args.output), assignments)
    if args.report:
        print(assignment_report(assignments, reading_frequency), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
