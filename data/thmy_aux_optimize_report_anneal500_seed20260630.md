# THMY auxiliary-code optimization report

- rounds: 500
- seed: 20260630
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
| 2 | 82 | 7430.121 | 7415 | 87 | 4 | 0 | 2026 | `quick=4 slot=2960 overflow=30855 phrase=854 key_load=0.00455416 finger_load=9.42319e-05 hand_load=4.04468e-05` |
| 3 | 323 | 7437.007 | 7424 | 78 | 4 | 0 | 2101 | `quick=4 slot=3043 overflow=28704 phrase=377 key_load=0.00678024 finger_load=3.87665e-05 hand_load=3.12794e-05` |
| 4 | 85 | 7440.075 | 7418 | 84 | 4 | 0 | 2029 | `quick=4 slot=2880 overflow=32346 phrase=791 key_load=0.00459907 finger_load=9.172e-05 hand_load=4.17467e-05` |
| 5 | 338 | 7441.366 | 7424 | 78 | 4 | 0 | 2098 | `quick=4 slot=3052 overflow=26954 phrase=347 key_load=0.00657699 finger_load=5.05738e-05 hand_load=3.12922e-05` |
| 6 | 251 | 7446.576 | 7424 | 78 | 4 | 0 | 2100 | `quick=4 slot=3149 overflow=49627 phrase=168 key_load=0.00739687 finger_load=5.89622e-05 hand_load=2.68504e-05` |
| 7 | 199 | 7449.345 | 7423 | 79 | 4 | 0 | 2109 | `quick=4 slot=3151 overflow=31632 phrase=118 key_load=0.00602625 finger_load=5.7753e-05 hand_load=4.11769e-05` |
| 8 | 396 | 7452.814 | 7424 | 78 | 4 | 0 | 2092 | `quick=4 slot=3114 overflow=22925 phrase=292 key_load=0.00714526 finger_load=5.80191e-05 hand_load=2.08508e-05` |
| 9 | 441 | 7453.474 | 7424 | 78 | 4 | 0 | 2087 | `quick=4 slot=3077 overflow=21293 phrase=250 key_load=0.00677751 finger_load=5.85632e-05 hand_load=2.10392e-05` |
| 10 | 472 | 7453.483 | 7424 | 78 | 4 | 0 | 2088 | `quick=4 slot=3106 overflow=20767 phrase=241 key_load=0.00702094 finger_load=5.90913e-05 hand_load=2.04256e-05` |

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
