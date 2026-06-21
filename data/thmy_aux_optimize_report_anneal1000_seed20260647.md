# THMY auxiliary-code optimization report

- rounds: 1000
- seed: 20260647
- candidate_limit: 96
- char_limit: all
- best_round: 1
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
| 1 | 1 | 7351.872 | 7423 | 79 | 4 | 0 | 2102 | `quick=4 slot=3091 overflow=118229 phrase=1348 key_load=0.00713805 finger_load=1.18365e-05 hand_load=1.36433e-05` |
| 2 | 852 | 7352.887 | 7422 | 80 | 4 | 0 | 2101 | `quick=4 slot=3750 overflow=10000 phrase=1152 key_load=0.00851738 finger_load=7.9488e-06 hand_load=1.63899e-05` |
| 3 | 931 | 7353.107 | 7423 | 79 | 4 | 0 | 2104 | `quick=4 slot=3551 overflow=10258 phrase=1204 key_load=0.00863215 finger_load=8.04772e-06 hand_load=1.59611e-05` |
| 4 | 963 | 7355.359 | 7423 | 79 | 4 | 0 | 2106 | `quick=4 slot=3524 overflow=10153 phrase=1203 key_load=0.00857068 finger_load=8.05268e-06 hand_load=1.59604e-05` |
| 5 | 860 | 7356.265 | 7423 | 79 | 4 | 0 | 2104 | `quick=4 slot=3559 overflow=10417 phrase=1161 key_load=0.00833099 finger_load=8.06076e-06 hand_load=1.61914e-05` |
| 6 | 955 | 7357.104 | 7423 | 79 | 4 | 0 | 2101 | `quick=4 slot=3498 overflow=10321 phrase=1219 key_load=0.00839836 finger_load=7.9462e-06 hand_load=1.63853e-05` |
| 7 | 952 | 7358.506 | 7423 | 79 | 4 | 0 | 2101 | `quick=4 slot=3616 overflow=10480 phrase=1206 key_load=0.00880262 finger_load=7.89273e-06 hand_load=1.60131e-05` |
| 8 | 939 | 7360.441 | 7423 | 79 | 4 | 0 | 2117 | `quick=4 slot=3549 overflow=11116 phrase=1203 key_load=0.00889495 finger_load=8.05842e-06 hand_load=1.62424e-05` |
| 9 | 900 | 7360.768 | 7422 | 80 | 4 | 0 | 2103 | `quick=4 slot=3741 overflow=10000 phrase=1211 key_load=0.00858141 finger_load=8.03268e-06 hand_load=1.60265e-05` |
| 10 | 996 | 7361.314 | 7423 | 79 | 4 | 0 | 2104 | `quick=4 slot=3461 overflow=10093 phrase=1207 key_load=0.00851771 finger_load=7.88323e-06 hand_load=1.62121e-05` |

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
