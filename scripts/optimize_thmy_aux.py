#!/usr/bin/env python3

from __future__ import annotations

import argparse
import math
import random
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path

import generate_thmy_aux as auxgen
from build_thmy import (
    DVORAK_FINGERS,
    dvorak_hand,
    iter_phrase_reading_overrides,
    primary_sound_codes,
)
from char_frequency import CharFrequency, ReadingFrequency


@dataclass(frozen=True)
class AuxParams:
    quick_select_candidates: int
    same_code_slot_weight: int
    same_code_overflow_weight: int
    phrase_code_collision_weight: int
    key_load_weight: float
    finger_load_weight: float
    hand_load_weight: float


@dataclass(frozen=True)
class ScoreWeights:
    big_same_finger: float
    same_finger: float
    repeat_key: float
    same_hand: float
    distance: float
    two_letter: float
    groups_over_quick: float
    overflow_candidates: float
    max_candidate_overflow: float
    collision: float
    phrase_collision: float
    same_finger_stretch: float


@dataclass
class TrialResult:
    round_number: int
    score: float
    params: AuxParams
    length_counts: Counter[int]
    group_size_counts: Counter[int]
    average: dict[str, float]
    weighted_average: dict[str, float]
    weighted_aux_added: dict[str, float]
    collisions: int
    phrase_collisions: int
    same_finger_stretches: int
    weighted_same_finger_stretches: float
    max_candidates: int
    groups_over_quick: int
    overflow_candidates: int
    example_groups: list[tuple[str, str, list[int]]]
    same_finger_stretch_pairs: list[tuple[str, int, float, str]]


def resolve_path(root: Path, value: str | Path) -> Path:
    path = Path(value)
    if path.is_absolute():
        return path
    return root / path


def parse_int_range(value: str) -> tuple[int, int]:
    left, sep, right = value.partition(":")
    if not sep:
        number = int(value)
        return number, number
    low = int(left)
    high = int(right)
    if low > high:
        raise argparse.ArgumentTypeError(f"invalid range: {value}")
    return low, high


def parse_float_range(value: str) -> tuple[float, float]:
    left, sep, right = value.partition(":")
    if not sep:
        number = float(value)
        return number, number
    low = float(left)
    high = float(right)
    if low > high:
        raise argparse.ArgumentTypeError(f"invalid range: {value}")
    return low, high


def sample_log_int(rng: random.Random, bounds: tuple[int, int]) -> int:
    low, high = bounds
    if low == high:
        return low
    if low <= 0:
        return rng.randint(low, high)
    value = math.exp(rng.uniform(math.log(low), math.log(high)))
    return max(low, min(high, round(value)))


def sample_log_float(rng: random.Random, bounds: tuple[float, float]) -> float:
    low, high = bounds
    if low == high:
        return low
    if low <= 0:
        return rng.uniform(low, high)
    return math.exp(rng.uniform(math.log(low), math.log(high)))


def load_phrase_reading_overrides(paths: list[Path]) -> dict[str, dict[str, str]]:
    overrides: dict[str, dict[str, str]] = {}
    for path in paths:
        overrides.update(iter_phrase_reading_overrides(path))
    return overrides


def current_params(quick_select_candidates: int | None = None) -> AuxParams:
    return AuxParams(
        quick_select_candidates=(
            quick_select_candidates or auxgen.AUX_QUICK_SELECT_CANDIDATES
        ),
        same_code_slot_weight=auxgen.AUX_SAME_CODE_SLOT_WEIGHT,
        same_code_overflow_weight=auxgen.AUX_SAME_CODE_OVERFLOW_WEIGHT,
        phrase_code_collision_weight=auxgen.AUX_PHRASE_CODE_COLLISION_WEIGHT,
        key_load_weight=auxgen.AUX_KEY_LOAD_WEIGHT,
        finger_load_weight=auxgen.AUX_FINGER_LOAD_WEIGHT,
        hand_load_weight=auxgen.AUX_HAND_LOAD_WEIGHT,
    )


def random_params(
    rng: random.Random,
    quick_select_candidates: int,
    slot_weight_range: tuple[int, int],
    overflow_weight_range: tuple[int, int],
    phrase_weight_range: tuple[int, int],
    key_load_multiplier_range: tuple[float, float],
    finger_load_multiplier_range: tuple[float, float],
    hand_load_multiplier_range: tuple[float, float],
) -> AuxParams:
    return AuxParams(
        quick_select_candidates=quick_select_candidates,
        same_code_slot_weight=sample_log_int(rng, slot_weight_range),
        same_code_overflow_weight=sample_log_int(rng, overflow_weight_range),
        phrase_code_collision_weight=sample_log_int(rng, phrase_weight_range),
        key_load_weight=auxgen.AUX_KEY_LOAD_WEIGHT
        * sample_log_float(rng, key_load_multiplier_range),
        finger_load_weight=auxgen.AUX_FINGER_LOAD_WEIGHT
        * sample_log_float(rng, finger_load_multiplier_range),
        hand_load_weight=auxgen.AUX_HAND_LOAD_WEIGHT
        * sample_log_float(rng, hand_load_multiplier_range),
    )


def seed_params(quick_select_candidates: int) -> list[AuxParams]:
    baseline = current_params(quick_select_candidates)
    seeds = [
        baseline,
        AuxParams(
            quick_select_candidates=quick_select_candidates,
            same_code_slot_weight=700,
            same_code_overflow_weight=24_000,
            phrase_code_collision_weight=350,
            key_load_weight=baseline.key_load_weight,
            finger_load_weight=baseline.finger_load_weight,
            hand_load_weight=baseline.hand_load_weight,
        ),
        AuxParams(
            quick_select_candidates=quick_select_candidates,
            same_code_slot_weight=1_500,
            same_code_overflow_weight=80_000,
            phrase_code_collision_weight=500,
            key_load_weight=baseline.key_load_weight,
            finger_load_weight=baseline.finger_load_weight,
            hand_load_weight=baseline.hand_load_weight,
        ),
        AuxParams(
            quick_select_candidates=quick_select_candidates,
            same_code_slot_weight=2_500,
            same_code_overflow_weight=120_000,
            phrase_code_collision_weight=700,
            key_load_weight=baseline.key_load_weight,
            finger_load_weight=baseline.finger_load_weight,
            hand_load_weight=baseline.hand_load_weight,
        ),
    ]
    unique: dict[AuxParams, None] = {}
    for params in seeds:
        unique[params] = None
    return list(unique)


def precompute_candidates(
    chars: list[str],
    char_sound_weights: dict[str, dict[str, int]],
    candidate_limit: int,
    quiet: bool,
) -> dict[str, list[tuple[float, int, str]]]:
    candidates_by_char: dict[str, list[tuple[float, int, str]]] = {}
    total = len(chars)

    for index, char in enumerate(chars, 1):
        candidates: list[tuple[float, int, str]] = []
        for aux_code in auxgen.ALL_AUX_CODES:
            base_score = auxgen.weighted_metric_score(
                char,
                aux_code,
                char_sound_weights,
            ) + auxgen.weighted_aux_transition_score(
                char,
                aux_code,
                char_sound_weights,
            )
            candidates.append((base_score, len(aux_code), aux_code))
        candidates.sort(key=lambda item: (item[0], item[1], item[2]))
        if candidate_limit > 0:
            candidates = candidates[:candidate_limit]
        candidates_by_char[char] = candidates

        if not quiet and (index == total or index % 500 == 0):
            print(
                f"precompute candidates: {index}/{total}",
                file=sys.stderr,
                flush=True,
            )

    return candidates_by_char


def soft_collision_score(
    char: str,
    aux_code: str,
    params: AuxParams,
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
            existing_count + 1 - params.quick_select_candidates,
        )
        score = (
            existing_count * params.same_code_slot_weight
            + overflow_count
            * overflow_count
            * params.same_code_overflow_weight
            + phrase_code_counts[sound_code + aux_code]
            * params.phrase_code_collision_weight
        )
        weighted_score += score * weight

    return weighted_score / total_weight


def generate_assignments(
    params: AuxParams,
    chars: list[str],
    char_sound_weights: dict[str, dict[str, int]],
    candidates_by_char: dict[str, list[tuple[float, int, str]]],
    phrase_code_counts: Counter[str],
) -> list[auxgen.AuxAssignment]:
    assigned_by_sound: dict[str, Counter[str]] = defaultdict(Counter)
    aux_key_load: Counter[str] = Counter()
    aux_finger_load: Counter[str] = Counter()
    aux_hand_load: Counter[str] = Counter()
    assignments: list[auxgen.AuxAssignment] = []

    for char in chars:
        best_assignment: auxgen.AuxAssignment | None = None
        char_weight = max(char_sound_weights[char].values(), default=1)

        for base_score, _length, aux_code in candidates_by_char[char]:
            score = base_score + soft_collision_score(
                char=char,
                aux_code=aux_code,
                params=params,
                char_sound_weights=char_sound_weights,
                assigned_by_sound=assigned_by_sound,
                phrase_code_counts=phrase_code_counts,
            )
            for key in aux_code:
                score += aux_key_load[key] * params.key_load_weight
                score += aux_finger_load[DVORAK_FINGERS[key]] * params.finger_load_weight
                score += aux_hand_load[dvorak_hand(key)] * params.hand_load_weight

            assignment = auxgen.AuxAssignment(
                char=char,
                aux_code=aux_code,
                score=score,
            )
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
        assignments.append(best_assignment)

    return assignments


def average_from_totals(totals: Counter[str], divisor: int | float) -> dict[str, float]:
    return {
        field: totals[field] / max(divisor, 1)
        for field in (
            "big_same_finger",
            "same_finger",
            "repeat_key",
            "same_hand",
            "hand_imbalance",
            "distance",
        )
    }


def evaluate_assignments(
    round_number: int,
    params: AuxParams,
    assignments: list[auxgen.AuxAssignment],
    char_sound_weights: dict[str, dict[str, int]],
    phrase_code_counts: Counter[str],
    score_weights: ScoreWeights,
) -> TrialResult:
    length_counts = Counter(len(assignment.aux_code) for assignment in assignments)
    metric_totals: Counter[str] = Counter()
    weighted_metric_totals: Counter[str] = Counter()
    added_metric_totals: Counter[str] = Counter()
    weighted_added_metric_totals: Counter[str] = Counter()
    groups: dict[str, list[tuple[str, int]]] = defaultdict(list)
    same_finger_stretch_pairs: Counter[str] = Counter()
    weighted_same_finger_stretch_pairs: Counter[str] = Counter()
    same_finger_stretch_examples: dict[str, list[str]] = defaultdict(list)
    reading_count = 0
    total_weight = 0

    for assignment in assignments:
        for sound_code, weight in char_sound_weights[assignment.char].items():
            full_code = sound_code + assignment.aux_code
            groups[full_code].append((assignment.char, weight))
            for left, right in zip(full_code, full_code[1:]):
                if auxgen.is_same_finger_stretch(left, right):
                    pair = left + right
                    same_finger_stretch_pairs[pair] += 1
                    weighted_same_finger_stretch_pairs[pair] += weight
                    examples = same_finger_stretch_examples[pair]
                    if len(examples) < 8:
                        examples.append(f"{assignment.char}:{full_code}")
            metrics = auxgen.code_metrics(sound_code, assignment.aux_code)
            added_metrics = auxgen.aux_transition_metrics(
                sound_code,
                assignment.aux_code,
            )
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

    group_size_counts = Counter(len(group) for group in groups.values())
    max_candidates = max(group_size_counts, default=0)
    collisions = sum(len(group) - 1 for group in groups.values() if len(group) > 1)
    groups_over_quick = sum(
        1 for group in groups.values() if len(group) > params.quick_select_candidates
    )
    overflow_candidates = sum(
        max(0, len(group) - params.quick_select_candidates)
        for group in groups.values()
    )
    phrase_collisions = sum(
        phrase_code_counts[code] * len(group)
        for code, group in groups.items()
        if phrase_code_counts[code]
    )
    same_finger_stretches = sum(same_finger_stretch_pairs.values())
    weighted_same_finger_stretches = (
        sum(weighted_same_finger_stretch_pairs.values()) / max(total_weight, 1)
    )

    weighted_aux_added = average_from_totals(weighted_added_metric_totals, total_weight)
    average = average_from_totals(metric_totals, reading_count)
    weighted_average = average_from_totals(weighted_metric_totals, total_weight)
    max_candidate_overflow = max(0, max_candidates - params.quick_select_candidates)

    score = (
        weighted_aux_added["big_same_finger"] * score_weights.big_same_finger
        + weighted_aux_added["same_finger"] * score_weights.same_finger
        + weighted_aux_added["repeat_key"] * score_weights.repeat_key
        + weighted_aux_added["same_hand"] * score_weights.same_hand
        + weighted_aux_added["distance"] * score_weights.distance
        + length_counts[2] * score_weights.two_letter
        + groups_over_quick * score_weights.groups_over_quick
        + overflow_candidates * score_weights.overflow_candidates
        + max_candidate_overflow * score_weights.max_candidate_overflow
        + collisions * score_weights.collision
        + phrase_collisions * score_weights.phrase_collision
        + weighted_same_finger_stretches * score_weights.same_finger_stretch
    )

    example_groups: list[tuple[str, str, list[int]]] = []
    for code, group in sorted(
        groups.items(),
        key=lambda item: (-len(item[1]), item[0]),
    )[:20]:
        sorted_group = sorted(group, key=lambda item: -item[1])
        example_groups.append(
            (
                code,
                "".join(char for char, _weight in sorted_group),
                [weight for _char, weight in sorted_group],
            )
        )

    same_finger_stretch_pair_rows: list[tuple[str, int, float, str]] = []
    for pair, count in sorted(
        same_finger_stretch_pairs.items(),
        key=lambda item: (-weighted_same_finger_stretch_pairs[item[0]], item[0]),
    )[:20]:
        pair_weighted_average = (
            weighted_same_finger_stretch_pairs[pair] / max(total_weight, 1)
        )
        same_finger_stretch_pair_rows.append(
            (
                pair,
                count,
                pair_weighted_average,
                " ".join(same_finger_stretch_examples[pair]),
            )
        )

    return TrialResult(
        round_number=round_number,
        score=score,
        params=params,
        length_counts=length_counts,
        group_size_counts=group_size_counts,
        average=average,
        weighted_average=weighted_average,
        weighted_aux_added=weighted_aux_added,
        collisions=collisions,
        phrase_collisions=phrase_collisions,
        same_finger_stretches=same_finger_stretches,
        weighted_same_finger_stretches=weighted_same_finger_stretches,
        max_candidates=max_candidates,
        groups_over_quick=groups_over_quick,
        overflow_candidates=overflow_candidates,
        example_groups=example_groups,
        same_finger_stretch_pairs=same_finger_stretch_pair_rows,
    )


def format_params(params: AuxParams) -> str:
    return (
        f"quick={params.quick_select_candidates} "
        f"slot={params.same_code_slot_weight} "
        f"overflow={params.same_code_overflow_weight} "
        f"phrase={params.phrase_code_collision_weight} "
        f"key_load={params.key_load_weight:.6g} "
        f"finger_load={params.finger_load_weight:.6g} "
        f"hand_load={params.hand_load_weight:.6g}"
    )


def metric_line(metrics: dict[str, float]) -> str:
    return " ".join(f"{key}={value:.3f}" for key, value in sorted(metrics.items()))


def write_report(
    output: Path,
    results: list[TrialResult],
    best: TrialResult,
    rounds: int,
    candidate_limit: int,
    seed: int,
    char_limit: int | None,
) -> None:
    top_results = sorted(results, key=lambda result: result.score)[:10]
    lines = [
        "# THMY auxiliary-code optimization report",
        "",
        f"- rounds: {rounds}",
        f"- seed: {seed}",
        f"- candidate_limit: {candidate_limit}",
        f"- char_limit: {char_limit or 'all'}",
        f"- best_round: {best.round_number}",
        f"- best_score: {best.score:.3f}",
        "",
        "## Best parameters",
        "",
        "| Parameter | Value |",
        "| --- | ---: |",
        f"| quick_select_candidates | {best.params.quick_select_candidates} |",
        f"| same_code_slot_weight | {best.params.same_code_slot_weight} |",
        f"| same_code_overflow_weight | {best.params.same_code_overflow_weight} |",
        f"| phrase_code_collision_weight | {best.params.phrase_code_collision_weight} |",
        f"| key_load_weight | {best.params.key_load_weight:.8f} |",
        f"| finger_load_weight | {best.params.finger_load_weight:.8f} |",
        f"| hand_load_weight | {best.params.hand_load_weight:.8f} |",
        "",
        "## Best metrics",
        "",
        f"- one_letter: {best.length_counts[1]}",
        f"- two_letter: {best.length_counts[2]}",
        f"- collisions: {best.collisions}",
        f"- phrase_collisions: {best.phrase_collisions}",
        f"- same_finger_stretches: {best.same_finger_stretches}",
        f"- weighted_same_finger_stretches: {best.weighted_same_finger_stretches:.6f}",
        f"- max_candidates: {best.max_candidates}",
        f"- groups_over_quick: {best.groups_over_quick}",
        f"- overflow_candidates: {best.overflow_candidates}",
        f"- weighted_average: `{metric_line(best.weighted_average)}`",
        f"- weighted_aux_added: `{metric_line(best.weighted_aux_added)}`",
        "",
        "## Candidate group distribution",
        "",
        "| Candidate count | Groups |",
        "| ---: | ---: |",
    ]

    for size, count in sorted(best.group_size_counts.items()):
        lines.append(f"| {size} | {count} |")

    lines.extend(
        [
            "",
            "## Top trials",
            "",
            "| Rank | Round | Score | One-letter | Two-letter | Max candidates | "
            "Groups > quick | Collisions | Parameters |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for rank, result in enumerate(top_results, 1):
        lines.append(
            f"| {rank} | {result.round_number} | {result.score:.3f} | "
            f"{result.length_counts[1]} | {result.length_counts[2]} | "
            f"{result.max_candidates} | {result.groups_over_quick} | "
            f"{result.collisions} | `{format_params(result.params)}` |"
        )

    lines.extend(
        [
            "",
            "## Largest candidate groups",
            "",
            "| Code | Chars | Weights |",
            "| --- | --- | --- |",
        ]
    )
    for code, chars, weights in best.example_groups:
        lines.append(
            f"| `{code}` | {chars} | "
            f"`{', '.join(str(weight) for weight in weights)}` |"
        )

    lines.extend(
        [
            "",
            "## Same-Finger Stretch Pairs",
            "",
            "Same-finger stretches count only different-key same-finger pairs with "
            "a Dvorak row gap >= 2. Repeated keys such as `uuu` and adjacent "
            "or diagonal-neighbor same-finger keys such as `ik`, `pi`, and `ki` "
            "are ignored.",
            "",
            "| Pair | Count | Weighted average | Examples |",
            "| --- | ---: | ---: | --- |",
        ]
    )
    if best.same_finger_stretch_pairs:
        for pair, count, weighted_average, examples in best.same_finger_stretch_pairs:
            lines.append(
                f"| `{pair}` | {count} | {weighted_average:.6f} | {examples} |"
            )
    else:
        lines.append("| - | 0 | 0.000000 | - |")

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    root = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser(
        description="Search comfort/collision parameters for THMY auxiliary codes.",
    )
    parser.set_defaults(root=root)
    parser.add_argument("--rounds", type=int, default=20)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--quick-select-candidates", type=int, default=4)
    parser.add_argument("--candidate-limit", type=int, default=96)
    parser.add_argument(
        "--char-limit",
        type=int,
        help="Only optimize the first N priority characters; for smoke tests.",
    )
    parser.add_argument(
        "--char-frequency",
        default="data/hanzi_frequency_junda.tsv",
    )
    parser.add_argument(
        "--reading-frequency",
        default="data/hanzi_reading_frequency_baishuang_8105.tsv",
    )
    parser.add_argument("--phrase-source", default="data/phrase_source.txt")
    parser.add_argument("--custom-entries", action="append")
    parser.add_argument("--phrase-reading-overrides", action="append")
    parser.add_argument("--output", help="Write the best auxiliary table.")
    parser.add_argument("--report", help="Write a Markdown optimization report.")
    parser.add_argument("--quiet", action="store_true")

    parser.add_argument("--slot-weight-range", type=parse_int_range, default=(250, 5_000))
    parser.add_argument(
        "--overflow-weight-range",
        type=parse_int_range,
        default=(10_000, 200_000),
    )
    parser.add_argument("--phrase-weight-range", type=parse_int_range, default=(0, 1_500))
    parser.add_argument(
        "--key-load-multiplier-range",
        type=parse_float_range,
        default=(0.25, 2.0),
    )
    parser.add_argument(
        "--finger-load-multiplier-range",
        type=parse_float_range,
        default=(0.25, 2.0),
    )
    parser.add_argument(
        "--hand-load-multiplier-range",
        type=parse_float_range,
        default=(0.25, 2.0),
    )

    parser.add_argument("--score-big-same-finger", type=float, default=100_000)
    parser.add_argument("--score-same-finger", type=float, default=50_000)
    parser.add_argument("--score-repeat-key", type=float, default=40_000)
    parser.add_argument("--score-same-hand", type=float, default=6_000)
    parser.add_argument("--score-distance", type=float, default=1_000)
    parser.add_argument("--score-two-letter", type=float, default=8)
    parser.add_argument("--score-groups-over-quick", type=float, default=100_000)
    parser.add_argument("--score-overflow-candidates", type=float, default=25_000)
    parser.add_argument("--score-max-candidate-overflow", type=float, default=100_000)
    parser.add_argument("--score-collision", type=float, default=1)
    parser.add_argument("--score-phrase-collision", type=float, default=1)
    parser.add_argument("--score-same-finger-stretch", type=float, default=2_000)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    if args.rounds < 1:
        parser.error("--rounds must be at least 1")
    if args.candidate_limit < 0:
        parser.error("--candidate-limit cannot be negative")
    if args.quick_select_candidates < 1:
        parser.error("--quick-select-candidates must be at least 1")
    if args.char_limit is not None and args.char_limit < 1:
        parser.error("--char-limit must be at least 1")

    root: Path = args.root
    char_frequency = CharFrequency.load(resolve_path(root, args.char_frequency))
    reading_frequency = ReadingFrequency.load(resolve_path(root, args.reading_frequency))
    phrase_source = resolve_path(root, args.phrase_source)
    custom_entries = [
        resolve_path(root, path)
        for path in (args.custom_entries or ["data/thmy_custom.tsv"])
    ]
    phrase_reading_override_paths = [
        resolve_path(root, path)
        for path in (
            args.phrase_reading_overrides
            or ["data/phrase_reading_overrides.tsv"]
        )
    ]
    phrase_reading_overrides = load_phrase_reading_overrides(
        phrase_reading_override_paths,
    )
    primary_codes = primary_sound_codes(reading_frequency)
    char_sound_weights = auxgen.load_char_sound_weights(reading_frequency)
    phrase_code_counts = auxgen.phrase_code_loads(
        phrase_source=phrase_source,
        custom_entries=custom_entries,
        primary_codes=primary_codes,
        phrase_reading_overrides=phrase_reading_overrides,
    )
    chars = sorted(
        char_sound_weights,
        key=lambda char: auxgen.char_priority(
            char,
            char_frequency,
            char_sound_weights,
        ),
    )
    if args.char_limit is not None:
        chars = chars[: args.char_limit]
        char_sound_weights = {char: char_sound_weights[char] for char in chars}

    if not args.quiet:
        print(
            f"optimize_thmy_aux: chars={len(chars)} rounds={args.rounds} "
            f"candidate_limit={args.candidate_limit}",
            file=sys.stderr,
        )

    candidates_by_char = precompute_candidates(
        chars=chars,
        char_sound_weights=char_sound_weights,
        candidate_limit=args.candidate_limit,
        quiet=args.quiet,
    )
    score_weights = ScoreWeights(
        big_same_finger=args.score_big_same_finger,
        same_finger=args.score_same_finger,
        repeat_key=args.score_repeat_key,
        same_hand=args.score_same_hand,
        distance=args.score_distance,
        two_letter=args.score_two_letter,
        groups_over_quick=args.score_groups_over_quick,
        overflow_candidates=args.score_overflow_candidates,
        max_candidate_overflow=args.score_max_candidate_overflow,
        collision=args.score_collision,
        phrase_collision=args.score_phrase_collision,
        same_finger_stretch=args.score_same_finger_stretch,
    )
    rng = random.Random(args.seed)
    queued_params = seed_params(args.quick_select_candidates)
    results: list[TrialResult] = []
    best_result: TrialResult | None = None
    best_assignments: list[auxgen.AuxAssignment] | None = None

    for round_number in range(1, args.rounds + 1):
        if queued_params:
            params = queued_params.pop(0)
        else:
            params = random_params(
                rng=rng,
                quick_select_candidates=args.quick_select_candidates,
                slot_weight_range=args.slot_weight_range,
                overflow_weight_range=args.overflow_weight_range,
                phrase_weight_range=args.phrase_weight_range,
                key_load_multiplier_range=args.key_load_multiplier_range,
                finger_load_multiplier_range=args.finger_load_multiplier_range,
                hand_load_multiplier_range=args.hand_load_multiplier_range,
            )

        assignments = generate_assignments(
            params=params,
            chars=chars,
            char_sound_weights=char_sound_weights,
            candidates_by_char=candidates_by_char,
            phrase_code_counts=phrase_code_counts,
        )
        result = evaluate_assignments(
            round_number=round_number,
            params=params,
            assignments=assignments,
            char_sound_weights=char_sound_weights,
            phrase_code_counts=phrase_code_counts,
            score_weights=score_weights,
        )
        results.append(result)

        if best_result is None or result.score < best_result.score:
            best_result = result
            best_assignments = assignments

        if not args.quiet:
            best_score = best_result.score if best_result else result.score
            print(
                f"round {round_number}/{args.rounds}: "
                f"score={result.score:.3f} best={best_score:.3f} "
                f"one={result.length_counts[1]} two={result.length_counts[2]} "
                f"max={result.max_candidates} "
                f"over={result.groups_over_quick} "
                f"params=({format_params(params)})",
                file=sys.stderr,
                flush=True,
            )

    if best_result is None or best_assignments is None:
        raise RuntimeError("no optimization result generated")

    if args.output:
        output = resolve_path(root, args.output)
        if args.char_limit is not None:
            print(
                "warning: --char-limit is set; writing a partial auxiliary table",
                file=sys.stderr,
            )
        output.parent.mkdir(parents=True, exist_ok=True)
        auxgen.write_aux_table(output, best_assignments)

    if args.report:
        write_report(
            output=resolve_path(root, args.report),
            results=results,
            best=best_result,
            rounds=args.rounds,
            candidate_limit=args.candidate_limit,
            seed=args.seed,
            char_limit=args.char_limit,
        )

    print("best_score", f"{best_result.score:.3f}")
    print("best_params", format_params(best_result.params))
    print(
        "best_metrics",
        f"one_letter={best_result.length_counts[1]}",
        f"two_letter={best_result.length_counts[2]}",
        f"collisions={best_result.collisions}",
        f"same_finger_stretches={best_result.same_finger_stretches}",
        f"max_candidates={best_result.max_candidates}",
        f"groups_over_quick={best_result.groups_over_quick}",
        "weighted_aux_added=" + metric_line(best_result.weighted_aux_added),
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
