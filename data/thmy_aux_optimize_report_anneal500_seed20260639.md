# THMY auxiliary-code optimization report

- rounds: 500
- seed: 20260639
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
| 2 | 409 | 7385.726 | 7421 | 81 | 4 | 0 | 2113 | `quick=4 slot=3094 overflow=41934 phrase=684 key_load=0.00626759 finger_load=7.79945e-06 hand_load=2.54845e-05` |
| 3 | 497 | 7390.219 | 7421 | 81 | 4 | 0 | 2087 | `quick=4 slot=3035 overflow=43247 phrase=702 key_load=0.00599254 finger_load=7.66486e-06 hand_load=2.42013e-05` |
| 4 | 296 | 7393.455 | 7423 | 79 | 4 | 0 | 2104 | `quick=4 slot=3442 overflow=64477 phrase=1025 key_load=0.0079846 finger_load=8.53199e-06 hand_load=1.58074e-05` |
| 5 | 235 | 7393.556 | 7425 | 77 | 4 | 0 | 2129 | `quick=4 slot=3376 overflow=79601 phrase=583 key_load=0.00968275 finger_load=1.35456e-05 hand_load=9.50577e-06` |
| 6 | 417 | 7394.431 | 7420 | 82 | 4 | 0 | 2087 | `quick=4 slot=3178 overflow=42366 phrase=733 key_load=0.00624086 finger_load=7.03382e-06 hand_load=2.45013e-05` |
| 7 | 306 | 7394.718 | 7422 | 80 | 4 | 0 | 2107 | `quick=4 slot=3584 overflow=55682 phrase=1026 key_load=0.00819674 finger_load=7.10094e-06 hand_load=1.55902e-05` |
| 8 | 470 | 7395.204 | 7421 | 81 | 4 | 0 | 2088 | `quick=4 slot=3080 overflow=43458 phrase=668 key_load=0.00614725 finger_load=7.39071e-06 hand_load=2.48491e-05` |
| 9 | 174 | 7397.712 | 7423 | 79 | 4 | 0 | 2108 | `quick=4 slot=3147 overflow=150144 phrase=904 key_load=0.00789067 finger_load=1.60145e-05 hand_load=1.24491e-05` |
| 10 | 458 | 7399.650 | 7423 | 79 | 4 | 0 | 2107 | `quick=4 slot=3092 overflow=41131 phrase=724 key_load=0.00688353 finger_load=7.31577e-06 hand_load=2.54927e-05` |

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
