# THMY auxiliary-code optimization report

- rounds: 700
- seed: 20260636
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
| 2 | 679 | 7374.202 | 7423 | 79 | 4 | 0 | 2103 | `quick=4 slot=3237 overflow=191876 phrase=1227 key_load=0.00784429 finger_load=8.70715e-06 hand_load=2.81924e-06` |
| 3 | 560 | 7383.904 | 7423 | 79 | 4 | 0 | 2118 | `quick=4 slot=3224 overflow=181327 phrase=1235 key_load=0.00772157 finger_load=8.3678e-06 hand_load=4.08311e-06` |
| 4 | 448 | 7384.298 | 7423 | 79 | 4 | 0 | 2116 | `quick=4 slot=3261 overflow=162816 phrase=1434 key_load=0.00795071 finger_load=8.75432e-06 hand_load=3.2912e-06` |
| 5 | 491 | 7385.395 | 7421 | 81 | 4 | 0 | 2101 | `quick=4 slot=3455 overflow=167432 phrase=1394 key_load=0.00773636 finger_load=8.66114e-06 hand_load=2.54653e-06` |
| 6 | 635 | 7386.135 | 7423 | 79 | 4 | 0 | 2113 | `quick=4 slot=3236 overflow=192808 phrase=1248 key_load=0.00768147 finger_load=8.74073e-06 hand_load=3.34397e-06` |
| 7 | 608 | 7386.934 | 7421 | 81 | 4 | 0 | 2100 | `quick=4 slot=3520 overflow=193570 phrase=1272 key_load=0.00782871 finger_load=8.70883e-06 hand_load=2.86757e-06` |
| 8 | 610 | 7387.585 | 7421 | 81 | 4 | 0 | 2101 | `quick=4 slot=3499 overflow=200000 phrase=1250 key_load=0.00746664 finger_load=8.7137e-06 hand_load=3.15024e-06` |
| 9 | 556 | 7389.081 | 7421 | 81 | 4 | 0 | 2099 | `quick=4 slot=3387 overflow=176925 phrase=1248 key_load=0.00722316 finger_load=8.53508e-06 hand_load=4.59857e-06` |
| 10 | 601 | 7389.476 | 7421 | 81 | 4 | 0 | 2100 | `quick=4 slot=3529 overflow=187225 phrase=1277 key_load=0.00774216 finger_load=8.26261e-06 hand_load=3.48316e-06` |

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
