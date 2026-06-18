#!/usr/bin/env python3

from __future__ import annotations

import argparse
import random
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path

import generate_thmy_aux as auxgen
import optimize_thmy_aux as auxopt
from build_thmy import (
    dvorak_hand,
    iter_custom_entries,
    iter_source_entries,
    phrase_code,
)
from char_frequency import (
    MIN_SUBSTANTIAL_READING_WEIGHT,
    PINYIN_FINAL_TO_THMY,
    PINYIN_INITIAL_TO_THMY,
    ZERO_INITIAL_PINYIN_TO_THMY,
    CharFrequency,
    ReadingFrequency,
)


LETTERS = tuple(auxgen.LETTERS)
INITIALS = tuple(PINYIN_INITIAL_TO_THMY)
FINALS = tuple(PINYIN_FINAL_TO_THMY)
ZERO_INITIALS = tuple(ZERO_INITIAL_PINYIN_TO_THMY)


@dataclass
class SoundLayout:
    initial_map: dict[str, str]
    final_map: dict[str, str]
    zero_initial_map: dict[str, str]

    def copy(self) -> "SoundLayout":
        return SoundLayout(
            initial_map=dict(self.initial_map),
            final_map=dict(self.final_map),
            zero_initial_map=dict(self.zero_initial_map),
        )


@dataclass(frozen=True)
class SoundAuxTrial:
    round_number: int
    score: float
    layout: SoundLayout
    aux_result: auxopt.TrialResult
    changed_initials: int
    changed_finals: int
    changed_zero_initials: int
    char_count: int
    signature_count: int


def baseline_layout() -> SoundLayout:
    return SoundLayout(
        initial_map=dict(PINYIN_INITIAL_TO_THMY),
        final_map=dict(PINYIN_FINAL_TO_THMY),
        zero_initial_map=dict(ZERO_INITIAL_PINYIN_TO_THMY),
    )


def resolve_path(root: Path, value: str | Path) -> Path:
    path = Path(value)
    if path.is_absolute():
        return path
    return root / path


def is_substantial_weight(weight: int, max_weight: int) -> bool:
    if weight <= 0 or max_weight <= 0:
        return False
    return weight >= MIN_SUBSTANTIAL_READING_WEIGHT or weight / max_weight >= 0.2


def pinyin_to_sound_code(pinyin: str, layout: SoundLayout) -> str | None:
    normalized = pinyin.lower().replace("ü", "v")
    if normalized in layout.zero_initial_map:
        return layout.zero_initial_map[normalized]

    for initial in ("zh", "ch", "sh"):
        if normalized.startswith(initial):
            final = normalized[len(initial) :]
            break
    else:
        initial = normalized[:1]
        final = normalized[1:]

    initial_code = layout.initial_map.get(initial)
    final_code = layout.final_map.get(final)
    if initial_code is None or final_code is None:
        return None
    return initial_code + final_code


def mapped_readings(
    reading_frequency: ReadingFrequency,
    layout: SoundLayout,
) -> tuple[dict[str, str], dict[str, dict[str, int]]]:
    sound_weights: dict[tuple[str, str], int] = {}
    for (char, pinyin), weight in reading_frequency.pinyin_weights.items():
        sound_code = pinyin_to_sound_code(pinyin, layout)
        if sound_code is None:
            continue
        identity = (char, sound_code)
        sound_weights[identity] = max(weight, sound_weights.get(identity, 0))

    primary_candidates: dict[str, list[tuple[tuple[object, ...], str]]] = defaultdict(list)
    char_sound_weights: dict[str, dict[str, int]] = defaultdict(dict)
    for (char, sound_code), weight in sound_weights.items():
        max_weight = reading_frequency.max_weights.get(char, 0)
        is_substantial = is_substantial_weight(weight, max_weight)
        primary_candidates[char].append(
            (
                (0 if is_substantial else 1, -weight, sound_code),
                sound_code,
            )
        )
        if is_substantial:
            char_sound_weights[char][sound_code] = weight

    primary_codes: dict[str, str] = {}
    for char, candidates in primary_candidates.items():
        candidates.sort(key=lambda item: item[0])
        primary_codes[char] = candidates[0][1]

    return primary_codes, dict(char_sound_weights)


def load_phrase_reading_override_pinyins(
    paths: list[Path],
) -> dict[str, dict[str, str]]:
    overrides: dict[str, dict[str, str]] = {}
    for path in paths:
        for line_number, line in enumerate(
            path.read_text(encoding="utf-8").splitlines(),
            1,
        ):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            fields = line.split("\t")
            text = fields[0].strip()
            if not text:
                raise ValueError(f"empty override text {path}:{line_number}")
            text_overrides: dict[str, str] = {}
            for field in fields[1:]:
                if ":" not in field:
                    raise ValueError(f"invalid override {path}:{line_number}: {field}")
                char, pinyin = field.split(":", 1)
                char = char.strip()
                pinyin = pinyin.strip()
                if len(char) != 1 or not pinyin:
                    raise ValueError(f"invalid override {path}:{line_number}: {field}")
                text_overrides[char] = pinyin
            overrides[text] = text_overrides
    return overrides


def phrase_char_codes(
    text: str,
    primary_codes: dict[str, str],
    phrase_reading_overrides: dict[str, dict[str, str]],
    layout: SoundLayout,
) -> list[str] | None:
    overrides = phrase_reading_overrides.get(text, {})
    codes: list[str | None] = []
    for char in text:
        if char in overrides:
            codes.append(pinyin_to_sound_code(overrides[char], layout))
        else:
            codes.append(primary_codes.get(char))
    if any(code is None for code in codes):
        return None
    return [code for code in codes if code is not None]


def phrase_code_loads(
    phrase_source: Path,
    custom_entries: list[Path],
    primary_codes: dict[str, str],
    phrase_reading_overrides: dict[str, dict[str, str]],
    layout: SoundLayout,
) -> Counter[str]:
    code_loads: Counter[str] = Counter()

    for _source_code, text in iter_source_entries(phrase_source):
        if len(text) <= 1:
            continue
        full_codes = phrase_char_codes(
            text=text,
            primary_codes=primary_codes,
            phrase_reading_overrides=phrase_reading_overrides,
            layout=layout,
        )
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


def char_priority(
    char: str,
    char_frequency: CharFrequency,
    char_sound_weights: dict[str, dict[str, int]],
) -> tuple[object, ...]:
    rank = char_frequency.ranks.get(char, char_frequency.max_rank + 50_000)
    best_reading_weight = max(char_sound_weights[char].values(), default=0)
    reading_count = len(char_sound_weights[char])
    return (rank, -best_reading_weight, -reading_count, char)


def sound_signature(sound_weights: dict[str, int]) -> tuple[tuple[str, int], ...]:
    return tuple(sorted(sound_weights.items()))


def candidates_for_signature(
    signature: tuple[tuple[str, int], ...],
    candidate_limit: int,
) -> list[tuple[float, int, str]]:
    total_weight = sum(weight for _sound_code, weight in signature) or 1
    candidates: list[tuple[float, int, str]] = []

    for aux_code in auxgen.ALL_AUX_CODES:
        score = 0.0
        for sound_code, weight in signature:
            score += (
                auxgen.metric_score(auxgen.code_metrics(sound_code, aux_code))
                + auxgen.aux_transition_score(
                    auxgen.aux_transition_metrics(sound_code, aux_code),
                )
            ) * weight
        candidates.append((score / total_weight, len(aux_code), aux_code))

    candidates.sort(key=lambda item: (item[0], item[1], item[2]))
    if candidate_limit > 0:
        return candidates[:candidate_limit]
    return candidates


def precompute_candidates(
    chars: list[str],
    char_sound_weights: dict[str, dict[str, int]],
    candidate_limit: int,
) -> tuple[dict[str, list[tuple[float, int, str]]], int]:
    signature_cache: dict[
        tuple[tuple[str, int], ...],
        list[tuple[float, int, str]],
    ] = {}
    candidates_by_char: dict[str, list[tuple[float, int, str]]] = {}

    for char in chars:
        signature = sound_signature(char_sound_weights[char])
        if signature not in signature_cache:
            signature_cache[signature] = candidates_for_signature(
                signature,
                candidate_limit,
            )
        candidates_by_char[char] = signature_cache[signature]

    return candidates_by_char, len(signature_cache)


def random_layout(
    rng: random.Random,
    base: SoundLayout,
    max_initial_swaps: int,
    max_final_key_swaps: int,
    max_final_moves: int,
    max_zero_moves: int,
) -> SoundLayout:
    layout = base.copy()

    for _ in range(rng.randint(0, max_initial_swaps)):
        left, right = rng.sample(INITIALS, 2)
        layout.initial_map[left], layout.initial_map[right] = (
            layout.initial_map[right],
            layout.initial_map[left],
        )

    for _ in range(rng.randint(0, max_final_key_swaps)):
        left, right = rng.sample(LETTERS, 2)
        for final, key in list(layout.final_map.items()):
            if key == left:
                layout.final_map[final] = right
            elif key == right:
                layout.final_map[final] = left

    for _ in range(rng.randint(0, max_final_moves)):
        final = rng.choice(FINALS)
        layout.final_map[final] = rng.choice(LETTERS)

    for _ in range(rng.randint(0, max_zero_moves)):
        zero = rng.choice(ZERO_INITIALS)
        layout.zero_initial_map[zero] = rng.choice(LETTERS) + rng.choice(LETTERS)

    return layout


def count_changes(
    layout: SoundLayout,
    base: SoundLayout,
) -> tuple[int, int, int]:
    changed_initials = sum(
        1 for key, value in layout.initial_map.items() if base.initial_map[key] != value
    )
    changed_finals = sum(
        1 for key, value in layout.final_map.items() if base.final_map[key] != value
    )
    changed_zero_initials = sum(
        1
        for key, value in layout.zero_initial_map.items()
        if base.zero_initial_map[key] != value
    )
    return changed_initials, changed_finals, changed_zero_initials


def combined_score(
    result: auxopt.TrialResult,
    score_weights: auxopt.ScoreWeights,
    aux_transition_share: float,
) -> float:
    full = result.weighted_average
    added = result.weighted_aux_added
    full_score = (
        full["big_same_finger"] * score_weights.big_same_finger
        + full["same_finger"] * score_weights.same_finger
        + full["repeat_key"] * score_weights.repeat_key
        + full["same_hand"] * score_weights.same_hand
        + full["distance"] * score_weights.distance
    )
    aux_score = (
        added["big_same_finger"] * score_weights.big_same_finger
        + added["same_finger"] * score_weights.same_finger
        + added["repeat_key"] * score_weights.repeat_key
        + added["same_hand"] * score_weights.same_hand
        + added["distance"] * score_weights.distance
    )
    structure_score = (
        result.length_counts[2] * score_weights.two_letter
        + result.groups_over_quick * score_weights.groups_over_quick
        + result.overflow_candidates * score_weights.overflow_candidates
        + max(0, result.max_candidates - result.params.quick_select_candidates)
        * score_weights.max_candidate_overflow
        + result.collisions * score_weights.collision
        + result.phrase_collisions * score_weights.phrase_collision
        + result.weighted_same_finger_stretches
        * score_weights.same_finger_stretch
    )
    return full_score + aux_score * aux_transition_share + structure_score


def metric_line(metrics: dict[str, float]) -> str:
    return " ".join(f"{key}={value:.3f}" for key, value in sorted(metrics.items()))


def format_mapping_changes(
    current: dict[str, str],
    base: dict[str, str],
    limit: int = 80,
) -> str:
    changes = [
        f"{key}:{base[key]}->{current[key]}"
        for key in sorted(current)
        if current[key] != base[key]
    ]
    if not changes:
        return "-"
    if len(changes) > limit:
        shown = changes[:limit]
        shown.append(f"... +{len(changes) - limit}")
        return " ".join(shown)
    return " ".join(changes)


def write_report(
    output: Path,
    trials: list[SoundAuxTrial],
    baseline: SoundAuxTrial,
    best: SoundAuxTrial,
    rounds: int,
    seed: int,
    candidate_limit: int,
    char_limit: int | None,
) -> None:
    base_layout = baseline_layout()
    top_trials = sorted(trials, key=lambda item: item.score)[:10]
    delta = baseline.score - best.score
    delta_percent = delta / baseline.score * 100 if baseline.score else 0

    lines = [
        "# THMY sound+aux optimization report",
        "",
        "This is an experimental search report. It does not change the formal THMY "
        "sound-code tables by itself.",
        "",
        f"- rounds: {rounds}",
        f"- seed: {seed}",
        f"- candidate_limit: {candidate_limit}",
        f"- char_limit: {char_limit or 'all'}",
        f"- baseline_score: {baseline.score:.3f}",
        f"- best_round: {best.round_number}",
        f"- best_score: {best.score:.3f}",
        f"- score_delta: {delta:.3f} ({delta_percent:.2f}%)",
        "",
        "## Best sound-code changes",
        "",
        f"- changed_initials: {best.changed_initials}",
        f"- changed_finals: {best.changed_finals}",
        f"- changed_zero_initials: {best.changed_zero_initials}",
        f"- initials: `{format_mapping_changes(best.layout.initial_map, base_layout.initial_map)}`",
        f"- finals: `{format_mapping_changes(best.layout.final_map, base_layout.final_map)}`",
        f"- zero_initials: `{format_mapping_changes(best.layout.zero_initial_map, base_layout.zero_initial_map)}`",
        "",
        "## Best auxiliary parameters",
        "",
        f"- {auxopt.format_params(best.aux_result.params)}",
        "",
        "## Baseline metrics",
        "",
        f"- one_letter: {baseline.aux_result.length_counts[1]}",
        f"- two_letter: {baseline.aux_result.length_counts[2]}",
        f"- collisions: {baseline.aux_result.collisions}",
        f"- phrase_collisions: {baseline.aux_result.phrase_collisions}",
        f"- same_finger_stretches: {baseline.aux_result.same_finger_stretches}",
        f"- max_candidates: {baseline.aux_result.max_candidates}",
        f"- groups_over_quick: {baseline.aux_result.groups_over_quick}",
        f"- weighted_average: `{metric_line(baseline.aux_result.weighted_average)}`",
        f"- weighted_aux_added: `{metric_line(baseline.aux_result.weighted_aux_added)}`",
        "",
        "## Best metrics",
        "",
        f"- one_letter: {best.aux_result.length_counts[1]}",
        f"- two_letter: {best.aux_result.length_counts[2]}",
        f"- collisions: {best.aux_result.collisions}",
        f"- phrase_collisions: {best.aux_result.phrase_collisions}",
        f"- same_finger_stretches: {best.aux_result.same_finger_stretches}",
        f"- weighted_same_finger_stretches: {best.aux_result.weighted_same_finger_stretches:.6f}",
        f"- max_candidates: {best.aux_result.max_candidates}",
        f"- groups_over_quick: {best.aux_result.groups_over_quick}",
        f"- overflow_candidates: {best.aux_result.overflow_candidates}",
        f"- weighted_average: `{metric_line(best.aux_result.weighted_average)}`",
        f"- weighted_aux_added: `{metric_line(best.aux_result.weighted_aux_added)}`",
        "",
        "## Top trials",
        "",
        "| Rank | Round | Score | Initials | Finals | Zero | One | Two | "
        "Max | Over | Collisions | Weighted average |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]

    for rank, trial in enumerate(top_trials, 1):
        result = trial.aux_result
        lines.append(
            f"| {rank} | {trial.round_number} | {trial.score:.3f} | "
            f"{trial.changed_initials} | {trial.changed_finals} | "
            f"{trial.changed_zero_initials} | {result.length_counts[1]} | "
            f"{result.length_counts[2]} | {result.max_candidates} | "
            f"{result.groups_over_quick} | {result.collisions} | "
            f"`{metric_line(result.weighted_average)}` |"
        )

    lines.extend(
        [
            "",
            "## Candidate group distribution",
            "",
            "| Candidate count | Groups |",
            "| ---: | ---: |",
        ]
    )
    for size, count in sorted(best.aux_result.group_size_counts.items()):
        lines.append(f"| {size} | {count} |")

    lines.extend(
        [
            "",
            "## Same-Finger Stretch Pairs",
            "",
            "| Pair | Count | Weighted average | Examples |",
            "| --- | ---: | ---: | --- |",
        ]
    )
    if best.aux_result.same_finger_stretch_pairs:
        for pair, count, weighted_average, examples in best.aux_result.same_finger_stretch_pairs:
            lines.append(
                f"| `{pair}` | {count} | {weighted_average:.6f} | {examples} |"
            )
    else:
        lines.append("| - | 0 | 0.000000 | - |")

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")


def evaluate_layout(
    round_number: int,
    layout: SoundLayout,
    aux_params: auxopt.AuxParams,
    char_frequency: CharFrequency,
    reading_frequency: ReadingFrequency,
    phrase_source: Path,
    custom_entries: list[Path],
    phrase_reading_overrides: dict[str, dict[str, str]],
    candidate_limit: int,
    char_limit: int | None,
    score_weights: auxopt.ScoreWeights,
    aux_transition_share: float,
    base_layout: SoundLayout,
) -> tuple[SoundAuxTrial, list[auxgen.AuxAssignment]]:
    primary_codes, char_sound_weights = mapped_readings(reading_frequency, layout)
    chars = sorted(
        char_sound_weights,
        key=lambda char: char_priority(char, char_frequency, char_sound_weights),
    )
    if char_limit is not None:
        chars = chars[:char_limit]
        char_sound_weights = {char: char_sound_weights[char] for char in chars}

    phrase_code_counts = phrase_code_loads(
        phrase_source=phrase_source,
        custom_entries=custom_entries,
        primary_codes=primary_codes,
        phrase_reading_overrides=phrase_reading_overrides,
        layout=layout,
    )
    candidates_by_char, signature_count = precompute_candidates(
        chars=chars,
        char_sound_weights=char_sound_weights,
        candidate_limit=candidate_limit,
    )
    assignments = auxopt.generate_assignments(
        params=aux_params,
        chars=chars,
        char_sound_weights=char_sound_weights,
        candidates_by_char=candidates_by_char,
        phrase_code_counts=phrase_code_counts,
    )
    aux_result = auxopt.evaluate_assignments(
        round_number=round_number,
        params=aux_params,
        assignments=assignments,
        char_sound_weights=char_sound_weights,
        phrase_code_counts=phrase_code_counts,
        score_weights=score_weights,
    )
    score = combined_score(
        result=aux_result,
        score_weights=score_weights,
        aux_transition_share=aux_transition_share,
    )
    aux_result.score = score
    changed_initials, changed_finals, changed_zero_initials = count_changes(
        layout,
        base_layout,
    )
    trial = SoundAuxTrial(
        round_number=round_number,
        score=score,
        layout=layout,
        aux_result=aux_result,
        changed_initials=changed_initials,
        changed_finals=changed_finals,
        changed_zero_initials=changed_zero_initials,
        char_count=len(chars),
        signature_count=signature_count,
    )
    return trial, assignments


def build_parser() -> argparse.ArgumentParser:
    root = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser(
        description="Experimentally search THMY sound-code and auxiliary-code layouts.",
    )
    parser.set_defaults(root=root)
    parser.add_argument("--rounds", type=int, default=20)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--quick-select-candidates", type=int, default=4)
    parser.add_argument("--candidate-limit", type=int, default=96)
    parser.add_argument("--char-limit", type=int)
    parser.add_argument("--char-frequency", default="data/hanzi_frequency_junda.tsv")
    parser.add_argument(
        "--reading-frequency",
        default="data/hanzi_reading_frequency_baishuang_8105.tsv",
    )
    parser.add_argument("--phrase-source", default="data/phrase_source.txt")
    parser.add_argument("--custom-entries", action="append")
    parser.add_argument("--phrase-reading-overrides", action="append")
    parser.add_argument("--report", help="Write a Markdown optimization report.")
    parser.add_argument("--output-aux", help="Write the best auxiliary table.")
    parser.add_argument("--quiet", action="store_true")

    parser.add_argument("--max-initial-swaps", type=int, default=8)
    parser.add_argument("--max-final-key-swaps", type=int, default=10)
    parser.add_argument("--max-final-moves", type=int, default=10)
    parser.add_argument("--max-zero-moves", type=int, default=2)
    parser.add_argument("--aux-transition-share", type=float, default=0.35)

    parser.add_argument("--slot-weight-range", type=auxopt.parse_int_range, default=(250, 5_000))
    parser.add_argument(
        "--overflow-weight-range",
        type=auxopt.parse_int_range,
        default=(10_000, 200_000),
    )
    parser.add_argument("--phrase-weight-range", type=auxopt.parse_int_range, default=(0, 1_500))
    parser.add_argument(
        "--key-load-multiplier-range",
        type=auxopt.parse_float_range,
        default=(0.25, 2.0),
    )
    parser.add_argument(
        "--finger-load-multiplier-range",
        type=auxopt.parse_float_range,
        default=(0.25, 2.0),
    )
    parser.add_argument(
        "--hand-load-multiplier-range",
        type=auxopt.parse_float_range,
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
    phrase_reading_overrides = load_phrase_reading_override_pinyins(
        phrase_reading_override_paths,
    )
    score_weights = auxopt.ScoreWeights(
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
    base_layout = baseline_layout()
    queued_aux_params = auxopt.seed_params(args.quick_select_candidates)
    trials: list[SoundAuxTrial] = []
    best_trial: SoundAuxTrial | None = None
    best_assignments: list[auxgen.AuxAssignment] | None = None
    baseline_trial: SoundAuxTrial | None = None

    if not args.quiet:
        print(
            f"optimize_thmy_sound_aux: rounds={args.rounds} "
            f"candidate_limit={args.candidate_limit} char_limit={args.char_limit or 'all'}",
            file=sys.stderr,
        )

    for round_number in range(1, args.rounds + 1):
        if queued_aux_params:
            layout = base_layout.copy()
            aux_params = queued_aux_params.pop(0)
        else:
            layout = random_layout(
                rng=rng,
                base=base_layout,
                max_initial_swaps=args.max_initial_swaps,
                max_final_key_swaps=args.max_final_key_swaps,
                max_final_moves=args.max_final_moves,
                max_zero_moves=args.max_zero_moves,
            )
            aux_params = auxopt.random_params(
                rng=rng,
                quick_select_candidates=args.quick_select_candidates,
                slot_weight_range=args.slot_weight_range,
                overflow_weight_range=args.overflow_weight_range,
                phrase_weight_range=args.phrase_weight_range,
                key_load_multiplier_range=args.key_load_multiplier_range,
                finger_load_multiplier_range=args.finger_load_multiplier_range,
                hand_load_multiplier_range=args.hand_load_multiplier_range,
            )

        trial, assignments = evaluate_layout(
            round_number=round_number,
            layout=layout,
            aux_params=aux_params,
            char_frequency=char_frequency,
            reading_frequency=reading_frequency,
            phrase_source=phrase_source,
            custom_entries=custom_entries,
            phrase_reading_overrides=phrase_reading_overrides,
            candidate_limit=args.candidate_limit,
            char_limit=args.char_limit,
            score_weights=score_weights,
            aux_transition_share=args.aux_transition_share,
            base_layout=base_layout,
        )
        trials.append(trial)
        if baseline_trial is None:
            baseline_trial = trial
        if best_trial is None or trial.score < best_trial.score:
            best_trial = trial
            best_assignments = assignments

        if not args.quiet:
            best_score = best_trial.score if best_trial else trial.score
            print(
                f"round {round_number}/{args.rounds}: "
                f"score={trial.score:.3f} best={best_score:.3f} "
                f"init={trial.changed_initials} final={trial.changed_finals} "
                f"zero={trial.changed_zero_initials} sig={trial.signature_count} "
                f"one={trial.aux_result.length_counts[1]} "
                f"two={trial.aux_result.length_counts[2]} "
                f"collisions={trial.aux_result.collisions} "
                f"weighted_average=({metric_line(trial.aux_result.weighted_average)})",
                file=sys.stderr,
                flush=True,
            )

    if baseline_trial is None or best_trial is None or best_assignments is None:
        raise RuntimeError("no optimization result generated")

    if args.output_aux:
        output_aux = resolve_path(root, args.output_aux)
        if args.char_limit is not None:
            print(
                "warning: --char-limit is set; writing a partial auxiliary table",
                file=sys.stderr,
            )
        output_aux.parent.mkdir(parents=True, exist_ok=True)
        auxgen.write_aux_table(output_aux, best_assignments)

    if args.report:
        write_report(
            output=resolve_path(root, args.report),
            trials=trials,
            baseline=baseline_trial,
            best=best_trial,
            rounds=args.rounds,
            seed=args.seed,
            candidate_limit=args.candidate_limit,
            char_limit=args.char_limit,
        )

    print("baseline_score", f"{baseline_trial.score:.3f}")
    print("best_score", f"{best_trial.score:.3f}")
    print(
        "best_changes",
        f"initials={best_trial.changed_initials}",
        f"finals={best_trial.changed_finals}",
        f"zero_initials={best_trial.changed_zero_initials}",
    )
    print(
        "best_metrics",
        f"one_letter={best_trial.aux_result.length_counts[1]}",
        f"two_letter={best_trial.aux_result.length_counts[2]}",
        f"collisions={best_trial.aux_result.collisions}",
        f"same_finger_stretches={best_trial.aux_result.same_finger_stretches}",
        f"max_candidates={best_trial.aux_result.max_candidates}",
        f"groups_over_quick={best_trial.aux_result.groups_over_quick}",
        "weighted_average=" + metric_line(best_trial.aux_result.weighted_average),
        "weighted_aux_added=" + metric_line(best_trial.aux_result.weighted_aux_added),
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
