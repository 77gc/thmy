# THMY auxiliary-code optimization report

- rounds: 900
- seed: 20260646
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
| 2 | 879 | 7423.330 | 7423 | 79 | 4 | 0 | 2108 | `quick=4 slot=3288 overflow=16235 phrase=501 key_load=0.0078147 finger_load=1.03042e-06 hand_load=4.69553e-06` |
| 3 | 318 | 7427.777 | 7423 | 79 | 4 | 0 | 2122 | `quick=4 slot=2796 overflow=150466 phrase=435 key_load=0.00529634 finger_load=6.0149e-07 hand_load=5.36205e-05` |
| 4 | 605 | 7432.604 | 7423 | 79 | 4 | 0 | 2108 | `quick=4 slot=3378 overflow=22009 phrase=497 key_load=0.00802529 finger_load=5.94726e-07 hand_load=5.9155e-06` |
| 5 | 890 | 7432.683 | 7423 | 79 | 4 | 0 | 2107 | `quick=4 slot=3297 overflow=15896 phrase=535 key_load=0.00794335 finger_load=1.02945e-06 hand_load=4.62429e-06` |
| 6 | 120 | 7433.468 | 7423 | 79 | 4 | 0 | 2122 | `quick=4 slot=3258 overflow=200000 phrase=1136 key_load=0.00787936 finger_load=4.55665e-07 hand_load=2.25647e-06` |
| 7 | 866 | 7434.654 | 7423 | 79 | 4 | 0 | 2108 | `quick=4 slot=3218 overflow=18217 phrase=487 key_load=0.00807481 finger_load=9.91357e-07 hand_load=4.56295e-06` |
| 8 | 638 | 7435.007 | 7423 | 79 | 4 | 0 | 2113 | `quick=4 slot=3506 overflow=19122 phrase=430 key_load=0.00912305 finger_load=7.55907e-07 hand_load=5.76155e-06` |
| 9 | 892 | 7435.319 | 7423 | 79 | 4 | 0 | 2109 | `quick=4 slot=3252 overflow=16814 phrase=512 key_load=0.00793122 finger_load=1.04995e-06 hand_load=4.90951e-06` |
| 10 | 617 | 7436.076 | 7421 | 81 | 4 | 0 | 2107 | `quick=4 slot=3522 overflow=19233 phrase=355 key_load=0.00805381 finger_load=6.0953e-07 hand_load=4.69292e-06` |

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
