# THMY auxiliary-code optimization report

- rounds: 500
- seed: 20260627
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
| 2 | 490 | 7362.804 | 7423 | 79 | 4 | 0 | 2034 | `quick=4 slot=3004 overflow=193639 phrase=747 key_load=0.00507932 finger_load=0.000102786 hand_load=4.37832e-05` |
| 3 | 452 | 7365.629 | 7423 | 79 | 4 | 0 | 2033 | `quick=4 slot=3024 overflow=186642 phrase=755 key_load=0.00513177 finger_load=0.000101053 hand_load=4.46398e-05` |
| 4 | 483 | 7366.770 | 7421 | 81 | 4 | 0 | 2032 | `quick=4 slot=3088 overflow=184741 phrase=755 key_load=0.0051136 finger_load=0.0001001 hand_load=4.35658e-05` |
| 5 | 469 | 7367.379 | 7423 | 79 | 4 | 0 | 2037 | `quick=4 slot=2986 overflow=183388 phrase=749 key_load=0.00519357 finger_load=0.000104479 hand_load=4.22632e-05` |
| 6 | 416 | 7371.800 | 7423 | 79 | 4 | 0 | 2043 | `quick=4 slot=3154 overflow=200000 phrase=805 key_load=0.00557141 finger_load=0.000110405 hand_load=4.43659e-05` |
| 7 | 478 | 7372.612 | 7422 | 80 | 4 | 0 | 2034 | `quick=4 slot=3080 overflow=192984 phrase=744 key_load=0.00512881 finger_load=0.00010295 hand_load=4.41108e-05` |
| 8 | 488 | 7373.337 | 7423 | 79 | 4 | 0 | 2039 | `quick=4 slot=2900 overflow=184719 phrase=767 key_load=0.00506638 finger_load=0.000103382 hand_load=4.19259e-05` |
| 9 | 484 | 7373.669 | 7423 | 79 | 4 | 0 | 2036 | `quick=4 slot=2953 overflow=184635 phrase=754 key_load=0.00502809 finger_load=0.000104494 hand_load=4.23355e-05` |
| 10 | 441 | 7374.539 | 7423 | 79 | 4 | 0 | 2049 | `quick=4 slot=2931 overflow=200000 phrase=763 key_load=0.00511378 finger_load=0.000101746 hand_load=4.11448e-05` |

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
