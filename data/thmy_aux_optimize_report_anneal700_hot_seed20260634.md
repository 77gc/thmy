# THMY auxiliary-code optimization report

- rounds: 700
- seed: 20260634
- candidate_limit: 96
- char_limit: all
- best_round: 1
- best_score: 7359.608

## Best parameters

| Parameter | Value |
| --- | ---: |
| quick_select_candidates | 4 |
| same_code_slot_weight | 2967 |
| same_code_overflow_weight | 35507 |
| phrase_code_collision_weight | 513 |
| key_load_weight | 0.00531709 |
| finger_load_weight | 0.00015507 |
| hand_load_weight | 0.00004339 |

## Best metrics

- one_letter: 7425
- two_letter: 77
- collisions: 2036
- phrase_collisions: 24
- same_finger_stretches: 15
- weighted_same_finger_stretches: 0.001240
- max_candidates: 4
- groups_over_quick: 0
- overflow_candidates: 0
- weighted_average: `big_same_finger=0.001 distance=8.226 hand_imbalance=1.003 repeat_key=0.020 same_finger=0.032 same_hand=0.273`
- weighted_aux_added: `big_same_finger=0.000 distance=4.296 hand_imbalance=1.000 repeat_key=0.000 same_finger=0.000 same_hand=0.064`

## Candidate group distribution

| Candidate count | Groups |
| ---: | ---: |
| 1 | 4079 |
| 2 | 1098 |
| 3 | 193 |
| 4 | 184 |

## Top trials

| Rank | Round | Score | One-letter | Two-letter | Max candidates | Groups > quick | Collisions | Parameters |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | 1 | 7359.608 | 7425 | 77 | 4 | 0 | 2036 | `quick=4 slot=2967 overflow=35507 phrase=513 key_load=0.00531709 finger_load=0.000155066 hand_load=4.3388e-05` |
| 2 | 617 | 7428.540 | 7424 | 78 | 4 | 0 | 2106 | `quick=4 slot=3646 overflow=40670 phrase=261 key_load=0.00984033 finger_load=2.88251e-05 hand_load=1.29504e-05` |
| 3 | 257 | 7429.396 | 7422 | 80 | 4 | 0 | 2106 | `quick=4 slot=5000 overflow=10000 phrase=380 key_load=0.0128627 finger_load=1.22287e-05 hand_load=1.1609e-05` |
| 4 | 655 | 7430.000 | 7424 | 78 | 4 | 0 | 2108 | `quick=4 slot=3487 overflow=37164 phrase=285 key_load=0.00952188 finger_load=2.81918e-05 hand_load=1.28654e-05` |
| 5 | 654 | 7432.312 | 7423 | 79 | 4 | 0 | 2100 | `quick=4 slot=3741 overflow=42162 phrase=275 key_load=0.00943637 finger_load=2.72559e-05 hand_load=1.2305e-05` |
| 6 | 588 | 7434.729 | 7422 | 80 | 4 | 0 | 2095 | `quick=4 slot=4235 overflow=38528 phrase=195 key_load=0.00974788 finger_load=2.74696e-05 hand_load=1.00778e-05` |
| 7 | 692 | 7434.863 | 7425 | 77 | 4 | 0 | 2119 | `quick=4 slot=3477 overflow=38294 phrase=264 key_load=0.0101569 finger_load=2.86583e-05 hand_load=1.40376e-05` |
| 8 | 623 | 7435.159 | 7424 | 78 | 4 | 0 | 2105 | `quick=4 slot=3669 overflow=39245 phrase=248 key_load=0.0095398 finger_load=2.71612e-05 hand_load=1.23863e-05` |
| 9 | 683 | 7435.801 | 7426 | 76 | 4 | 0 | 2115 | `quick=4 slot=3403 overflow=37789 phrase=258 key_load=0.00989513 finger_load=2.70366e-05 hand_load=1.33728e-05` |
| 10 | 279 | 7436.094 | 7423 | 79 | 4 | 0 | 2107 | `quick=4 slot=3082 overflow=32557 phrase=472 key_load=0.007294 finger_load=7.92279e-06 hand_load=1.10126e-05` |

## Largest candidate groups

| Code | Chars | Weights |
| --- | --- | --- |
| `bne` | 笔愎萆馝 | `6838, 10, 6, 1` |
| `fja` | 妇脯鲋艴 | `211, 48, 5, 2` |
| `fjb` | 服肤绂蝮 | `3361, 69, 16, 11` |
| `fjc` | 扶孵玞跗 | `833, 77, 20, 13` |
| `fjf` | 府辐茯绋 | `1107, 83, 8, 2` |
| `fjg` | 夫拂鄜郛 | `1472, 244, 40, 24` |
| `fjh` | 富辅馥赙 | `1296, 375, 24, 4` |
| `fji` | 腐阜怫垺 | `218, 50, 7, 1` |
| `fjk` | 弗敷芣涪 | `799, 587, 43, 42` |
| `fjl` | 幅芙凫簠 | `657, 594, 61, 20` |
| `fjm` | 负覆祓匐 | `4145, 290, 52, 8` |
| `fjn` | 副幞咐讣 | `3013, 3, 2, 1` |
| `fjp` | 伏罘袱洑 | `697, 8, 7, 7` |
| `fjq` | 符缚稃呋 | `675, 233, 10, 7` |
| `fjr` | 付斧蚨韨 | `2603, 538, 1, 1` |
| `fjs` | 复俘趺滏 | `1786, 170, 12, 5` |
| `fjv` | 福赴桴驸 | `1378, 1308, 31, 10` |
| `fjw` | 附傅宓茀 | `4846, 443, 14, 11` |
| `fjx` | 浮蝠榑菔 | `375, 56, 7, 5` |
| `fjy` | 腹孚麸琈 | `542, 77, 23, 1` |

## Same-Finger Stretch Pairs

Same-finger stretches count only different-key same-finger pairs with a Dvorak row gap >= 2. Repeated keys such as `uuu` and adjacent or diagonal-neighbor same-finger keys such as `ik`, `pi`, and `ki` are ignored.

| Pair | Count | Weighted average | Examples |
| --- | ---: | ---: | --- |
| `px` | 8 | 0.000861 | 派:pxv 排:pxm 拍:pxz 牌:pxw 徘:pxb 湃:pxh 俳:pxn 哌:pxs |
| `ky` | 6 | 0.000379 | 卡:kys 咖:kyg 喀:kyf 咯:kyq 咔:kyr 胩:kyl |
| `kp` | 1 | 0.000001 | 剋:kpf |
