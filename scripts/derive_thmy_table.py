#!/usr/bin/env python3

from __future__ import annotations

import sys
from pathlib import Path


SIT_EXCLUDED_PUNCT_TEXTS = {"。", "，", "；", "：", "、"}
# Keep most Yehe initials visible, but swap zh/ch: Yehe uses v=zh and i=ch.
# On Dvorak, zh is much more frequent than ch, so put zh on the stronger i key.
SIT_INITIAL_REMAP_TABLE = {
    **{key: key for key in "abcdefghijklmnopqrstuvwxyz"},
    "i": "v",
    "v": "i",
}
SIT_INITIAL_REMAP = str.maketrans(SIT_INITIAL_REMAP_TABLE)
SIT_INITIAL_REVERSE_REMAP = {
    target: source for source, target in SIT_INITIAL_REMAP_TABLE.items()
}
# The final layer is a hand-feel map. Yehe's second sound position is already
# a code group rather than plain pinyin, so it can move independently.
SIT_FINAL_REMAP_TABLE = {
    "a": "y",
    "b": "m",
    "c": "a",
    "d": "x",
    "e": "e",
    "f": "z",
    "g": "i",
    "h": "s",
    "i": "n",
    "j": "o",
    "k": "l",
    "l": "g",
    "m": "c",
    "n": "r",
    "o": "u",
    "p": "v",
    "q": "b",
    "r": "h",
    "s": "q",
    "t": "f",
    "u": "j",
    "v": "k",
    "w": "p",
    "x": "w",
    "y": "d",
    "z": "t",
}
SIT_FINAL_REMAP = str.maketrans(SIT_FINAL_REMAP_TABLE)
SIT_FINAL_REVERSE_REMAP = {
    target: source for source, target in SIT_FINAL_REMAP_TABLE.items()
}
SIT_SHAPE_REMAP = str.maketrans(
    {
        ",": "w",
        ".": "v",
        ";": "z",
        "a": "m",
        "b": "l",
        "f": "q",
        "g": "o",
        "h": "a",
        "i": "t",
        "j": "f",
        "k": "j",
        "l": "b",
        "m": "i",
        "o": "r",
        "p": "g",
        "q": "u",
        "r": "x",
        "s": "h",
        "t": "w",
        "u": "v",
        "v": "p",
        "w": "y",
        "x": "s",
        "y": "k",
    }
)


def phrase_sound_roles(text: str, code_len: int) -> list[str]:
    if len(text) <= 1:
        roles = ["I", "F"]
    elif len(text) == 2:
        roles = ["I", "F", "I", "F"]
    elif len(text) == 3:
        roles = ["I", "I", "I", "F"]
    else:
        roles = ["I", "I", "I", "I"]
    return roles[:code_len]


def remap_sound_code_by_roles(code: str, roles: list[str]) -> str:
    output: list[str] = []
    for char, role in zip(code, roles):
        if role == "F":
            output.append(char.translate(SIT_FINAL_REMAP))
        else:
            output.append(char.translate(SIT_INITIAL_REMAP))
    return "".join(output)


def source_initial_for_remapped_key(key: str) -> str:
    return SIT_INITIAL_REVERSE_REMAP.get(key, key)


def source_final_for_remapped_key(key: str) -> str:
    return SIT_FINAL_REVERSE_REMAP.get(key, key)


def source_sound_for_remapped_code(code: str) -> str | None:
    if len(code) < 2:
        return None
    return source_initial_for_remapped_key(code[0]) + source_final_for_remapped_key(
        code[1]
    )


def remap_phrase_sound_code(code: str, text: str) -> str:
    return remap_sound_code_by_roles(code, phrase_sound_roles(text, len(code)))


def remap_pure_phrase_sound_code(code: str) -> str:
    roles = ["I" if index % 2 == 0 else "F" for index in range(len(code))]
    return remap_sound_code_by_roles(code, roles)


def remap_sound_shape_code(code: str) -> str:
    if len(code) <= 2:
        return remap_sound_code_by_roles(code, ["I", "F"][: len(code)])

    return remap_sound_code_by_roles(code[:2], ["I", "F"]) + code[2:].translate(
        SIT_SHAPE_REMAP
    )


def remap_code(code: str) -> str:
    return remap_sound_shape_code(code)


def remap_code_for_text(code: str, text: str) -> str:
    if len(text) > 1:
        return remap_phrase_sound_code(code, text)
    return remap_sound_shape_code(code)


def remap_keycode(line: str) -> str:
    prefix = "KeyCode="
    if not line.startswith(prefix):
        return line
    return prefix + "abcdefghijklmnopqrstuvwxyz"


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: derive_thmy_table.py INPUT.txt OUTPUT.txt", file=sys.stderr)
        return 1

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])

    lines = input_path.read_text(encoding="utf-8").splitlines()
    output: list[str] = []
    in_data = False

    for line in lines:
        if not in_data:
            if line == "[Data]":
                in_data = True
                output.append(line)
                continue
            output.append(remap_keycode(line))
            continue

        if not line.strip():
            continue
        if "\t" not in line:
            output.append(line)
            continue

        code, text = line.split("\t", 1)
        if text in SIT_EXCLUDED_PUNCT_TEXTS:
            continue
        output.append(f"{remap_code_for_text(code, text)}\t{text}")

    output_path.write_text("\n".join(output) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
