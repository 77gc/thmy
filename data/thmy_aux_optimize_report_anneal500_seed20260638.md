# THMY auxiliary-code optimization report

- rounds: 500
- seed: 20260638
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
| 2 | 489 | 7400.994 | 7421 | 81 | 4 | 0 | 2092 | `quick=4 slot=2773 overflow=119865 phrase=707 key_load=0.00559246 finger_load=3.66469e-06 hand_load=2.66958e-05` |
| 3 | 423 | 7401.545 | 7422 | 80 | 4 | 0 | 2090 | `quick=4 slot=2925 overflow=113516 phrase=667 key_load=0.00571469 finger_load=3.45413e-06 hand_load=2.39766e-05` |
| 4 | 427 | 7402.726 | 7421 | 81 | 4 | 0 | 2090 | `quick=4 slot=2878 overflow=116407 phrase=664 key_load=0.00560728 finger_load=3.67782e-06 hand_load=2.40874e-05` |
| 5 | 488 | 7403.480 | 7421 | 81 | 4 | 0 | 2092 | `quick=4 slot=2725 overflow=115111 phrase=708 key_load=0.00570619 finger_load=3.66936e-06 hand_load=2.68738e-05` |
| 6 | 497 | 7403.825 | 7424 | 78 | 4 | 0 | 2118 | `quick=4 slot=2590 overflow=122217 phrase=720 key_load=0.00571899 finger_load=3.67647e-06 hand_load=2.6973e-05` |
| 7 | 462 | 7405.027 | 7421 | 81 | 4 | 0 | 2090 | `quick=4 slot=2875 overflow=111054 phrase=678 key_load=0.00566484 finger_load=3.55147e-06 hand_load=2.63979e-05` |
| 8 | 458 | 7405.865 | 7423 | 79 | 4 | 0 | 2097 | `quick=4 slot=2812 overflow=109792 phrase=682 key_load=0.00615074 finger_load=3.77028e-06 hand_load=2.69117e-05` |
| 9 | 439 | 7406.053 | 7424 | 78 | 4 | 0 | 2103 | `quick=4 slot=2754 overflow=113038 phrase=680 key_load=0.00616791 finger_load=3.82226e-06 hand_load=2.44573e-05` |
| 10 | 455 | 7406.724 | 7424 | 78 | 4 | 0 | 2093 | `quick=4 slot=2804 overflow=119576 phrase=653 key_load=0.00612394 finger_load=3.5434e-06 hand_load=2.60884e-05` |

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
