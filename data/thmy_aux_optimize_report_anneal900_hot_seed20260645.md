# THMY auxiliary-code optimization report

- rounds: 900
- seed: 20260645
- candidate_limit: 96
- char_limit: all
- best_round: 1
- best_score: 7356.727

## Best parameters

| Parameter | Value |
| --- | ---: |
| quick_select_candidates | 4 |
| same_code_slot_weight | 3001 |
| same_code_overflow_weight | 57735 |
| phrase_code_collision_weight | 125 |
| key_load_weight | 0.00657308 |
| finger_load_weight | 0.00000911 |
| hand_load_weight | 0.00001846 |

## Best metrics

- one_letter: 7423
- two_letter: 79
- collisions: 2109
- phrase_collisions: 31
- same_finger_stretches: 15
- weighted_same_finger_stretches: 0.001240
- max_candidates: 4
- groups_over_quick: 0
- overflow_candidates: 0
- weighted_average: `big_same_finger=0.001 distance=8.289 hand_imbalance=1.004 repeat_key=0.020 same_finger=0.032 same_hand=0.246`
- weighted_aux_added: `big_same_finger=0.000 distance=4.359 hand_imbalance=1.000 repeat_key=0.000 same_finger=0.000 same_hand=0.037`

## Candidate group distribution

| Candidate count | Groups |
| ---: | ---: |
| 1 | 3943 |
| 2 | 1156 |
| 3 | 193 |
| 4 | 189 |

## Top trials

| Rank | Round | Score | One-letter | Two-letter | Max candidates | Groups > quick | Collisions | Parameters |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | 1 | 7356.727 | 7423 | 79 | 4 | 0 | 2109 | `quick=4 slot=3001 overflow=57735 phrase=125 key_load=0.00657308 finger_load=9.1133e-06 hand_load=1.84627e-05` |
| 2 | 746 | 7383.464 | 7423 | 79 | 4 | 0 | 2104 | `quick=4 slot=3192 overflow=153787 phrase=762 key_load=0.00775032 finger_load=1.09501e-05 hand_load=1.07456e-06` |
| 3 | 752 | 7383.498 | 7423 | 79 | 4 | 0 | 2111 | `quick=4 slot=3085 overflow=138986 phrase=795 key_load=0.0072612 finger_load=1.09371e-05 hand_load=1.08036e-06` |
| 4 | 780 | 7384.695 | 7423 | 79 | 4 | 0 | 2102 | `quick=4 slot=3148 overflow=153376 phrase=758 key_load=0.00745252 finger_load=1.20598e-05 hand_load=9.9821e-07` |
| 5 | 892 | 7385.385 | 7421 | 81 | 4 | 0 | 2101 | `quick=4 slot=3099 overflow=167238 phrase=671 key_load=0.00677717 finger_load=1.19823e-05 hand_load=1.0017e-06` |
| 6 | 792 | 7385.503 | 7421 | 81 | 4 | 0 | 2102 | `quick=4 slot=3311 overflow=147403 phrase=702 key_load=0.00719434 finger_load=1.20015e-05 hand_load=1.00817e-06` |
| 7 | 765 | 7385.838 | 7423 | 79 | 4 | 0 | 2118 | `quick=4 slot=3061 overflow=146396 phrase=759 key_load=0.00713875 finger_load=1.23856e-05 hand_load=9.86691e-07` |
| 8 | 810 | 7386.791 | 7421 | 81 | 4 | 0 | 2101 | `quick=4 slot=3345 overflow=152777 phrase=729 key_load=0.00737506 finger_load=1.22139e-05 hand_load=1.03018e-06` |
| 9 | 748 | 7389.808 | 7423 | 79 | 4 | 0 | 2101 | `quick=4 slot=3254 overflow=156189 phrase=739 key_load=0.00806031 finger_load=1.18655e-05 hand_load=1.08274e-06` |
| 10 | 807 | 7391.292 | 7421 | 81 | 4 | 0 | 2101 | `quick=4 slot=3167 overflow=144666 phrase=690 key_load=0.00690576 finger_load=1.22262e-05 hand_load=1.00258e-06` |

## Largest candidate groups

| Code | Chars | Weights |
| --- | --- | --- |
| `bno` | 毕俾襞馝 | `690, 110, 6, 1` |
| `bnp` | 币裨佖秕 | `2666, 11, 3, 2` |
| `bny` | 壁痹妣珌 | `761, 36, 30, 4` |
| `fja` | 附俘绋蚨 | `4846, 170, 2, 1` |
| `fjb` | 福肤黼驸 | `1378, 69, 41, 10` |
| `fjc` | 扶斧涪玞 | `833, 538, 42, 20` |
| `fjf` | 弗拂茯滏 | `799, 244, 8, 5` |
| `fjg` | 复缚郛稃 | `1786, 233, 24, 10` |
| `fji` | 腹阜怫垺 | `542, 50, 7, 1` |
| `fjk` | 妇辐鄜讣 | `211, 83, 40, 1` |
| `fjl` | 府芙凫簠 | `1107, 594, 61, 20` |
| `fjm` | 服甫绂匐 | `3361, 319, 16, 8` |
| `fjn` | 负蝠菔艴 | `4145, 56, 5, 2` |
| `fjo` | 付俯馥幞 | `2603, 126, 24, 3` |
| `fjp` | 幅孵芣鲋 | `657, 77, 43, 5` |
| `fjq` | 符釜傅桴 | `675, 598, 443, 31` |
| `fjr` | 副趺赙咐 | `3013, 12, 4, 2` |
| `fjs` | 富脯呋韨 | `1296, 48, 7, 1` |
| `fjv` | 浮辅祓苻 | `375, 375, 52, 28` |
| `fjw` | 赴父宓茀 | `1308, 868, 14, 11` |

## Same-Finger Stretch Pairs

Same-finger stretches count only different-key same-finger pairs with a Dvorak row gap >= 2. Repeated keys such as `uuu` and adjacent or diagonal-neighbor same-finger keys such as `ik`, `pi`, and `ki` are ignored.

| Pair | Count | Weighted average | Examples |
| --- | ---: | ---: | --- |
| `px` | 8 | 0.000861 | 派:pxz 排:pxb 拍:pxw 牌:pxm 徘:pxv 湃:pxr 俳:pxf 哌:pxg |
| `ky` | 6 | 0.000379 | 卡:kyz 咖:kyr 喀:kyf 咯:kyl 咔:kyg 胩:kyc |
| `kp` | 1 | 0.000001 | 剋:kpr |
