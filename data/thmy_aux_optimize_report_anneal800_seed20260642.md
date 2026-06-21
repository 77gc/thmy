# THMY auxiliary-code optimization report

- rounds: 800
- seed: 20260642
- candidate_limit: 96
- char_limit: all
- best_round: 637
- best_score: 7351.872

## Best parameters

| Parameter | Value |
| --- | ---: |
| quick_select_candidates | 4 |
| same_code_slot_weight | 3091 |
| same_code_overflow_weight | 118229 |
| phrase_code_collision_weight | 1348 |
| key_load_weight | 0.00713805 |
| finger_load_weight | 0.00001184 |
| hand_load_weight | 0.00001364 |

## Best metrics

- one_letter: 7423
- two_letter: 79
- collisions: 2102
- phrase_collisions: 27
- same_finger_stretches: 15
- weighted_same_finger_stretches: 0.001240
- max_candidates: 4
- groups_over_quick: 0
- overflow_candidates: 0
- weighted_average: `big_same_finger=0.001 distance=8.303 hand_imbalance=1.004 repeat_key=0.020 same_finger=0.032 same_hand=0.245`
- weighted_aux_added: `big_same_finger=0.000 distance=4.372 hand_imbalance=1.000 repeat_key=0.000 same_finger=0.000 same_hand=0.036`

## Candidate group distribution

| Candidate count | Groups |
| ---: | ---: |
| 1 | 3960 |
| 2 | 1143 |
| 3 | 196 |
| 4 | 189 |

## Top trials

| Rank | Round | Score | One-letter | Two-letter | Max candidates | Groups > quick | Collisions | Parameters |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | 637 | 7351.872 | 7423 | 79 | 4 | 0 | 2102 | `quick=4 slot=3091 overflow=118229 phrase=1348 key_load=0.00713805 finger_load=1.18365e-05 hand_load=1.36433e-05` |
| 2 | 758 | 7353.361 | 7423 | 79 | 4 | 0 | 2111 | `quick=4 slot=3127 overflow=128562 phrase=1316 key_load=0.0077943 finger_load=1.18249e-05 hand_load=1.311e-05` |
| 3 | 664 | 7354.133 | 7423 | 79 | 4 | 0 | 2105 | `quick=4 slot=3197 overflow=122979 phrase=1335 key_load=0.00767695 finger_load=1.18399e-05 hand_load=1.39446e-05` |
| 4 | 624 | 7355.231 | 7423 | 79 | 4 | 0 | 2119 | `quick=4 slot=3013 overflow=116863 phrase=1366 key_load=0.00688682 finger_load=1.18159e-05 hand_load=1.39795e-05` |
| 5 | 652 | 7355.299 | 7423 | 79 | 4 | 0 | 2103 | `quick=4 slot=3243 overflow=114286 phrase=1329 key_load=0.00744356 finger_load=1.18796e-05 hand_load=1.41356e-05` |
| 6 | 691 | 7356.539 | 7423 | 79 | 4 | 0 | 2108 | `quick=4 slot=3103 overflow=120699 phrase=1327 key_load=0.00780156 finger_load=1.191e-05 hand_load=1.35967e-05` |
| 7 | 1 | 7356.727 | 7423 | 79 | 4 | 0 | 2109 | `quick=4 slot=3001 overflow=57735 phrase=125 key_load=0.00657308 finger_load=9.1133e-06 hand_load=1.84627e-05` |
| 8 | 593 | 7359.439 | 7423 | 79 | 4 | 0 | 2106 | `quick=4 slot=3052 overflow=122304 phrase=1389 key_load=0.00689666 finger_load=1.1535e-05 hand_load=1.26921e-05` |
| 9 | 744 | 7361.319 | 7423 | 79 | 4 | 0 | 2105 | `quick=4 slot=3179 overflow=116987 phrase=1320 key_load=0.00782822 finger_load=1.19001e-05 hand_load=1.30123e-05` |
| 10 | 674 | 7362.188 | 7423 | 79 | 4 | 0 | 2105 | `quick=4 slot=3303 overflow=115323 phrase=1331 key_load=0.0076643 finger_load=1.19294e-05 hand_load=1.39263e-05` |

## Largest candidate groups

| Code | Chars | Weights |
| --- | --- | --- |
| `bne` | 毕璧妣珌 | `690, 258, 30, 4` |
| `bno` | 必裨荜馝 | `3672, 11, 5, 1` |
| `bny` | 币俾佖秕 | `2666, 110, 3, 2` |
| `fja` | 妇俘馥滏 | `211, 170, 24, 5` |
| `fjb` | 服俯黻苻 | `3361, 126, 29, 28` |
| `fjc` | 扶孵跗艴 | `833, 77, 13, 2` |
| `fjf` | 附甫茯绋 | `4846, 319, 8, 2` |
| `fjg` | 府缚蚨韨 | `1107, 233, 1, 1` |
| `fji` | 浮蝠怫垺 | `375, 56, 7, 1` |
| `fjk` | 符辐赙讣 | `675, 83, 4, 1` |
| `fjl` | 付拂郛稃 | `2603, 244, 24, 10` |
| `fjm` | 福傅绂匐 | `1378, 443, 16, 8` |
| `fjn` | 富袱榑菔 | `1296, 7, 7, 5` |
| `fjo` | 弗趺幞咐 | `799, 12, 3, 2` |
| `fjp` | 斧腐玞鲋 | `538, 218, 20, 5` |
| `fjq` | 副釜肤黼 | `3013, 598, 69, 41` |
| `fjr` | 父芙凫鄜 | `868, 594, 61, 40` |
| `fjs` | 负敷簠呋 | `4145, 587, 20, 7` |
| `fjv` | 幅辅蝮茀 | `657, 375, 11, 11` |
| `fjw` | 复赴祓宓 | `1786, 1308, 52, 14` |

## Same-Finger Stretch Pairs

Same-finger stretches count only different-key same-finger pairs with a Dvorak row gap >= 2. Repeated keys such as `uuu` and adjacent or diagonal-neighbor same-finger keys such as `ik`, `pi`, and `ki` are ignored.

| Pair | Count | Weighted average | Examples |
| --- | ---: | ---: | --- |
| `px` | 8 | 0.000861 | 派:pxz 排:pxw 拍:pxb 牌:pxm 徘:pxv 湃:pxf 俳:pxg 哌:pxl |
| `ky` | 6 | 0.000379 | 卡:kyf 咖:kyl 喀:kyg 咯:kyw 咔:kyr 胩:kyz |
| `kp` | 1 | 0.000001 | 剋:kpf |
