from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Union


MIN_SUBSTANTIAL_READING_WEIGHT = 1000

PINYIN_INITIAL_TO_YEHE = {
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
    "zh": "v",
    "ch": "i",
    "sh": "u",
}
PINYIN_FINAL_TO_YEHE = {
    "a": "a",
    "ai": "d",
    "an": "j",
    "ang": "h",
    "ao": "c",
    "e": "e",
    "ei": "w",
    "en": "f",
    "eng": "g",
    "er": "r",
    "i": "i",
    "ia": "x",
    "ian": "m",
    "iang": "l",
    "iao": "n",
    "ie": "p",
    "in": "b",
    "ing": "k",
    "iong": "s",
    "iu": "q",
    "o": "o",
    "ong": "s",
    "ou": "z",
    "u": "u",
    "ua": "x",
    "uai": "k",
    "uan": "r",
    "uang": "l",
    "ue": "t",
    "ui": "v",
    "un": "y",
    "uo": "o",
    "v": "v",
    "ve": "t",
}
ZERO_INITIAL_PINYIN_TO_YEHE = {
    "a": "aa",
    "ai": "ai",
    "an": "an",
    "ang": "ah",
    "ao": "ao",
    "e": "ee",
    "ei": "ei",
    "en": "en",
    "eng": "eg",
    "er": "er",
    "o": "oo",
    "ou": "ou",
}


def pinyin_to_yehe_sound_code(pinyin: str) -> Optional[str]:
    normalized = pinyin.lower().replace("ü", "v")
    if normalized in ZERO_INITIAL_PINYIN_TO_YEHE:
        return ZERO_INITIAL_PINYIN_TO_YEHE[normalized]

    for initial in ("zh", "ch", "sh"):
        if normalized.startswith(initial):
            final = normalized[len(initial) :]
            break
    else:
        initial = normalized[:1]
        final = normalized[1:]

    initial_code = PINYIN_INITIAL_TO_YEHE.get(initial)
    final_code = PINYIN_FINAL_TO_YEHE.get(final)
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

        # No word-frequency corpus is bundled. Keep phrase order stable and
        # below single characters so a same-code high-frequency character is
        # not displaced by an unrelated phrase.
        return 1_000_000 + total_entries - index


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
            char, key, weight_text, *rest = line.split("\t")
            if len(char) != 1 or len(key) != 1:
                continue
            weight = int(weight_text)
            identity = (char, key)
            weights[identity] = max(weight, weights.get(identity, 0))
            max_weights[char] = max(weight, max_weights.get(char, 0))
            if rest:
                pinyin = rest[0].strip()
                if pinyin:
                    pinyin_identity = (char, pinyin)
                    pinyin_weights[pinyin_identity] = max(
                        weight, pinyin_weights.get(pinyin_identity, 0)
                    )
                    sound_code = pinyin_to_yehe_sound_code(pinyin)
                    if sound_code is not None:
                        sound_identity = (char, sound_code)
                        sound_weights[sound_identity] = max(
                            weight, sound_weights.get(sound_identity, 0)
                        )
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
    reading_key: Optional[str] = None,
    reading_sound_code: Optional[str] = None,
) -> tuple[object, ...]:
    normalized_code = code.replace(";", "-")
    text_kind = 0 if len(text) == 1 else 1
    if char_frequency is None or len(text) != 1:
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
        if reading_weight is None:
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
