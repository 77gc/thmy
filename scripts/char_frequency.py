from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Union


MIN_SUBSTANTIAL_READING_WEIGHT = 1000
PHRASE_LENGTH_BASE_WEIGHTS = {
    2: 700_000,
    3: 520_000,
    4: 300_000,
    5: 220_000,
}
MAX_FALLBACK_PHRASE_WEIGHT = 999_999

PINYIN_INITIAL_TO_THMY = {
    "b": "b",
    "p": "p",
    "m": "m",
    "f": "f",
    "d": "d",
    "t": "t",
    "n": "n",
    "l": "l",
    "g": "g",
    "k": "k",
    "h": "h",
    "j": "j",
    "q": "q",
    "x": "x",
    "r": "r",
    "z": "z",
    "c": "c",
    "s": "s",
    "y": "y",
    "w": "w",
    "zh": "i",
    "ch": "v",
    "sh": "u",
}
PINYIN_FINAL_TO_THMY = {
    "a": "y",
    "ai": "x",
    "an": "o",
    "ang": "s",
    "ao": "a",
    "e": "e",
    "ei": "p",
    "en": "z",
    "eng": "i",
    "er": "h",
    "i": "n",
    "ia": "w",
    "ian": "c",
    "iang": "g",
    "iao": "r",
    "ie": "v",
    "in": "m",
    "ing": "l",
    "iong": "q",
    "iu": "b",
    "o": "u",
    "ong": "q",
    "ou": "t",
    "u": "j",
    "ua": "w",
    "uai": "l",
    "uan": "h",
    "uang": "g",
    "ue": "f",
    "ui": "k",
    "un": "d",
    "uo": "u",
    "v": "k",
    "ve": "f",
}
ZERO_INITIAL_PINYIN_TO_THMY = {
    "a": "ay",
    "ai": "an",
    "an": "ar",
    "ang": "as",
    "ao": "au",
    "e": "ee",
    "ei": "en",
    "en": "er",
    "eng": "ai",
    "er": "ah",
    "o": "ou",
    "ou": "oj",
}


def pinyin_to_sound_code(pinyin: str) -> Optional[str]:
    normalized = pinyin.lower().replace("ü", "v")
    if normalized in ZERO_INITIAL_PINYIN_TO_THMY:
        return ZERO_INITIAL_PINYIN_TO_THMY[normalized]

    for initial in ("zh", "ch", "sh"):
        if normalized.startswith(initial):
            final = normalized[len(initial) :]
            break
    else:
        initial = normalized[:1]
        final = normalized[1:]

    initial_code = PINYIN_INITIAL_TO_THMY.get(initial)
    final_code = PINYIN_FINAL_TO_THMY.get(final)
    if initial_code is None or final_code is None:
        return None
    return initial_code + final_code


@dataclass(frozen=True)
class CharFrequency:
    ranks: dict[str, int]
    max_rank: int

    @classmethod
    def load(cls, path: Union[str, Path]) -> "CharFrequency":
        ranks: dict[str, int] = {}
        for line in Path(path).read_text(encoding="utf-8").splitlines():
            if not line or line.startswith("#"):
                continue
            rank_text, char, *_rest = line.split("\t")
            char = char.strip()
            if not char:
                continue
            ranks[char] = int(rank_text)
        return cls(ranks=ranks, max_rank=max(ranks.values(), default=0))

    def single_char_sort_rank(self, text: str, index: int) -> int:
        if len(text) != 1:
            return self.max_rank + 1 + index
        return self.ranks.get(text, self.max_rank + 1 + index)

    def rime_weight(self, text: str, index: int, total_entries: int) -> int:
        if len(text) == 1:
            rank = self.ranks.get(text)
            if rank is not None:
                return 20_000_000 + self.max_rank + 1 - rank
            return 10_000_000 - min(index, 9_000_000)

        # Fallback phrase weights stay below explicit PhraseFrequency weights
        # while avoiding raw source order for same-code phrase collisions.
        return 1_000_000 + self.phrase_fallback_weight(text, index)

    def phrase_fallback_weight(self, text: str, index: int) -> int:
        if len(text) <= 1:
            return 0

        length_base = PHRASE_LENGTH_BASE_WEIGHTS.get(
            len(text),
            max(80_000, PHRASE_LENGTH_BASE_WEIGHTS[5] - (len(text) - 5) * 25_000),
        )
        unknown_rank = self.max_rank + 1
        ranks = [self.ranks.get(char, unknown_rank) for char in text]
        rank_ceiling = max(self.max_rank, 1)
        average_rank = sum(ranks) / len(ranks)
        best_rank = min(ranks)
        average_score = int(
            max(0.0, 1.0 - (average_rank - 1) / rank_ceiling) * 200_000
        )
        best_score = int(max(0.0, 1.0 - (best_rank - 1) / rank_ceiling) * 70_000)
        source_score = max(0, 20_000 - min(index, 20_000))
        return min(
            MAX_FALLBACK_PHRASE_WEIGHT,
            length_base + average_score + best_score + source_score,
        )


@dataclass(frozen=True)
class PhraseFrequency:
    weights: dict[str, int]

    @classmethod
    def load(cls, path: Union[str, Path]) -> "PhraseFrequency":
        weights: dict[str, int] = {}
        for line_number, line in enumerate(
            Path(path).read_text(encoding="utf-8").splitlines(),
            1,
        ):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "\t" not in line:
                raise ValueError(f"missing tab in phrase frequency {path}:{line_number}")
            text, weight_text = line.split("\t", 1)
            text = text.strip()
            weight = int(weight_text.strip())
            if not text:
                raise ValueError(f"empty phrase frequency text {path}:{line_number}")
            if len(text) <= 1:
                raise ValueError(
                    f"single character in phrase frequency {path}:{line_number}"
                )
            if weight <= 0:
                raise ValueError(f"non-positive phrase frequency {path}:{line_number}")
            weights[text] = max(weight, weights.get(text, 0))
        return cls(weights=weights)

    def weight(self, text: str) -> Optional[int]:
        return self.weights.get(text)

    def rime_weight(
        self,
        text: str,
        index: int,
        total_entries: int,
        custom_rank: Optional[int] = None,
    ) -> Optional[int]:
        if len(text) <= 1:
            return None
        if custom_rank is not None:
            return 5_000_000 - custom_rank
        weight = self.weight(text)
        if weight is None:
            return None
        return 2_000_000 + weight


@dataclass(frozen=True)
class ReadingFrequency:
    weights: dict[tuple[str, str], int]
    max_weights: dict[str, int]
    pinyin_weights: dict[tuple[str, str], int]
    sound_weights: dict[tuple[str, str], int]

    @classmethod
    def load(cls, path: Union[str, Path]) -> "ReadingFrequency":
        weights: dict[tuple[str, str], int] = {}
        max_weights: dict[str, int] = {}
        pinyin_weights: dict[tuple[str, str], int] = {}
        sound_weights: dict[tuple[str, str], int] = {}
        for line in Path(path).read_text(encoding="utf-8").splitlines():
            if not line or line.startswith("#"):
                continue
            char, source_key, weight_text, *rest = line.split("\t")
            if len(char) != 1:
                continue
            weight = int(weight_text)
            if rest:
                pinyin = rest[0].strip()
                if pinyin:
                    pinyin_identity = (char, pinyin)
                    pinyin_weights[pinyin_identity] = max(
                        weight, pinyin_weights.get(pinyin_identity, 0)
                    )
                    sound_code = pinyin_to_sound_code(pinyin)
                    if sound_code is not None:
                        identity = (char, sound_code[0])
                        weights[identity] = max(weight, weights.get(identity, 0))
                        sound_identity = (char, sound_code)
                        sound_weights[sound_identity] = max(
                            weight, sound_weights.get(sound_identity, 0)
                        )
            elif len(source_key) == 1:
                identity = (char, source_key)
                weights[identity] = max(weight, weights.get(identity, 0))
            max_weights[char] = max(weight, max_weights.get(char, 0))
        return cls(
            weights=weights,
            max_weights=max_weights,
            pinyin_weights=pinyin_weights,
            sound_weights=sound_weights,
        )

    def weight(self, text: str, key: str) -> Optional[int]:
        return self.weights.get((text, key))

    def is_substantial(self, text: str, key: str) -> bool:
        weight = self.weight(text, key)
        if weight is None:
            return False
        if weight <= 0:
            return False
        max_weight = self.max_weights.get(text, 0)
        if max_weight <= 0:
            return False
        return weight >= MIN_SUBSTANTIAL_READING_WEIGHT or weight / max_weight >= 0.2

    def pinyin_weight(self, text: str, pinyin: str) -> Optional[int]:
        return self.pinyin_weights.get((text, pinyin))

    def sound_weight(self, text: str, sound_code: str) -> Optional[int]:
        return self.sound_weights.get((text, sound_code))

    def is_substantial_sound(self, text: str, sound_code: str) -> bool:
        weight = self.sound_weight(text, sound_code)
        if weight is None:
            return False
        if weight <= 0:
            return False
        max_weight = self.max_weights.get(text, 0)
        if max_weight <= 0:
            return False
        return weight >= MIN_SUBSTANTIAL_READING_WEIGHT or weight / max_weight >= 0.2


def table_sort_key(
    code: str,
    text: str,
    index: int,
    char_frequency: Optional[CharFrequency] = None,
    reading_frequency: Optional[ReadingFrequency] = None,
    phrase_frequency: Optional[PhraseFrequency] = None,
    custom_rank: Optional[int] = None,
    reading_key: Optional[str] = None,
    reading_sound_code: Optional[str] = None,
) -> tuple[object, ...]:
    normalized_code = code.replace(";", "-")
    text_kind = 0 if len(text) == 1 else 1
    if len(text) != 1:
        phrase_weight = (
            phrase_frequency.weight(text) if phrase_frequency is not None else None
        )
        fallback_weight = (
            char_frequency.phrase_fallback_weight(text, index)
            if char_frequency is not None
            else 0
        )
        return (
            normalized_code,
            text_kind,
            custom_rank is None,
            custom_rank if custom_rank is not None else 0,
            phrase_weight is None,
            -(phrase_weight if phrase_weight is not None else fallback_weight),
            index,
        )
    if char_frequency is None:
        return (normalized_code, text_kind, index)
    reading_priority: int | None = None
    reading_weight_sort = 0
    if reading_frequency is not None and (
        reading_sound_code is not None or reading_key is not None
    ):
        if reading_sound_code is not None:
            reading_weight = reading_frequency.sound_weight(text, reading_sound_code)
            is_substantial = reading_frequency.is_substantial_sound(
                text, reading_sound_code
            )
        elif reading_key is not None:
            reading_weight = reading_frequency.weight(text, reading_key)
            is_substantial = reading_frequency.is_substantial(text, reading_key)
        else:
            reading_weight = None
            is_substantial = False
        if reading_weight is None and len(code) == 1:
            reading_priority = 0
            reading_weight_sort = -reading_frequency.max_weights.get(text, 0)
        elif reading_weight is None:
            reading_priority = 2
        else:
            reading_priority = 0 if is_substantial else 1
            reading_weight_sort = -reading_weight
    return (
        normalized_code,
        text_kind,
        *( () if reading_priority is None else (reading_priority,) ),
        char_frequency.single_char_sort_rank(text, index),
        reading_weight_sort,
        index,
    )
