# THMY auxiliary-code optimization report

- rounds: 700
- seed: 20260632
- candidate_limit: 96
- char_limit: all
- best_round: 641
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
| 1 | 641 | 7356.727 | 7423 | 79 | 4 | 0 | 2109 | `quick=4 slot=3001 overflow=57735 phrase=125 key_load=0.00657308 finger_load=9.1133e-06 hand_load=1.84627e-05` |
| 2 | 1 | 7359.608 | 7425 | 77 | 4 | 0 | 2036 | `quick=4 slot=2967 overflow=35507 phrase=513 key_load=0.00531709 finger_load=0.000155066 hand_load=4.3388e-05` |
| 3 | 600 | 7364.713 | 7421 | 81 | 4 | 0 | 2102 | `quick=4 slot=3128 overflow=64187 phrase=141 key_load=0.0066233 finger_load=9.22131e-06 hand_load=1.86911e-05` |
| 4 | 651 | 7365.064 | 7421 | 81 | 4 | 0 | 2103 | `quick=4 slot=3101 overflow=66599 phrase=109 key_load=0.00643195 finger_load=9.51222e-06 hand_load=1.90617e-05` |
| 5 | 696 | 7366.811 | 7422 | 80 | 4 | 0 | 2104 | `quick=4 slot=3242 overflow=60564 phrase=130 key_load=0.00709392 finger_load=9.3561e-06 hand_load=1.98861e-05` |
| 6 | 647 | 7368.375 | 7423 | 79 | 4 | 0 | 2105 | `quick=4 slot=3181 overflow=62508 phrase=102 key_load=0.00739262 finger_load=9.85911e-06 hand_load=1.92391e-05` |
| 7 | 597 | 7370.197 | 7423 | 79 | 4 | 0 | 2111 | `quick=4 slot=3060 overflow=59915 phrase=163 key_load=0.00676722 finger_load=9.12422e-06 hand_load=2.00927e-05` |
| 8 | 676 | 7370.448 | 7421 | 81 | 4 | 0 | 2100 | `quick=4 slot=3097 overflow=62091 phrase=111 key_load=0.00641429 finger_load=9.26681e-06 hand_load=1.91381e-05` |
| 9 | 666 | 7374.246 | 7423 | 79 | 4 | 0 | 2106 | `quick=4 slot=3121 overflow=59916 phrase=116 key_load=0.00726387 finger_load=9.86796e-06 hand_load=2.0032e-05` |
| 10 | 614 | 7379.242 | 7423 | 79 | 4 | 0 | 2104 | `quick=4 slot=3146 overflow=63726 phrase=163 key_load=0.00697373 finger_load=1.0202e-05 hand_load=2.12476e-05` |

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
