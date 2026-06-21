# THMY auxiliary-code optimization report

- rounds: 800
- seed: 20260643
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
| 2 | 516 | 7393.811 | 7425 | 77 | 4 | 0 | 2109 | `quick=4 slot=2677 overflow=40520 phrase=1087 key_load=0.00605075 finger_load=3.51326e-06 hand_load=2.41447e-05` |
| 3 | 565 | 7398.863 | 7421 | 81 | 4 | 0 | 2092 | `quick=4 slot=2911 overflow=40572 phrase=1055 key_load=0.00565352 finger_load=3.77831e-06 hand_load=2.41595e-05` |
| 4 | 93 | 7400.152 | 7423 | 79 | 4 | 0 | 2103 | `quick=4 slot=3423 overflow=43201 phrase=330 key_load=0.00798804 finger_load=1.39511e-05 hand_load=1.04396e-05` |
| 5 | 502 | 7400.182 | 7422 | 80 | 4 | 0 | 2091 | `quick=4 slot=2866 overflow=43481 phrase=1094 key_load=0.00586364 finger_load=3.24775e-06 hand_load=2.53038e-05` |
| 6 | 426 | 7400.785 | 7422 | 80 | 4 | 0 | 2092 | `quick=4 slot=2798 overflow=60469 phrase=1282 key_load=0.00576477 finger_load=3.7022e-06 hand_load=2.52683e-05` |
| 7 | 556 | 7401.379 | 7421 | 81 | 4 | 0 | 2089 | `quick=4 slot=2804 overflow=43068 phrase=1053 key_load=0.00539593 finger_load=3.59337e-06 hand_load=2.47509e-05` |
| 8 | 431 | 7404.110 | 7425 | 77 | 4 | 0 | 2122 | `quick=4 slot=2657 overflow=61620 phrase=1250 key_load=0.0061026 finger_load=3.71614e-06 hand_load=2.48114e-05` |
| 9 | 485 | 7404.208 | 7424 | 78 | 4 | 0 | 2100 | `quick=4 slot=2789 overflow=43473 phrase=1131 key_load=0.00620415 finger_load=3.20653e-06 hand_load=2.49126e-05` |
| 10 | 416 | 7404.297 | 7423 | 79 | 4 | 0 | 2126 | `quick=4 slot=3051 overflow=56327 phrase=1351 key_load=0.00667567 finger_load=3.83598e-06 hand_load=2.17969e-05` |

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
