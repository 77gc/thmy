# THMY auxiliary-code optimization report

- rounds: 700
- seed: 20260635
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
| 2 | 700 | 7407.146 | 7421 | 81 | 4 | 0 | 2117 | `quick=4 slot=3049 overflow=124558 phrase=202 key_load=0.00626758 finger_load=9.94726e-06 hand_load=2.13822e-05` |
| 3 | 697 | 7407.195 | 7421 | 81 | 4 | 0 | 2089 | `quick=4 slot=2925 overflow=125840 phrase=213 key_load=0.00607993 finger_load=1.05718e-05 hand_load=2.20026e-05` |
| 4 | 498 | 7420.818 | 7421 | 81 | 4 | 0 | 2089 | `quick=4 slot=3013 overflow=104525 phrase=183 key_load=0.00592153 finger_load=1.32057e-05 hand_load=1.95673e-05` |
| 5 | 645 | 7421.422 | 7421 | 81 | 4 | 0 | 2092 | `quick=4 slot=2728 overflow=133604 phrase=212 key_load=0.00575504 finger_load=1.05413e-05 hand_load=2.2628e-05` |
| 6 | 371 | 7422.967 | 7423 | 79 | 4 | 0 | 2109 | `quick=4 slot=3523 overflow=47799 phrase=87 key_load=0.0088165 finger_load=1.46568e-05 hand_load=1.4965e-05` |
| 7 | 485 | 7424.654 | 7420 | 82 | 4 | 0 | 2090 | `quick=4 slot=2663 overflow=93791 phrase=229 key_load=0.00492182 finger_load=1.40566e-05 hand_load=2.22443e-05` |
| 8 | 679 | 7424.898 | 7420 | 82 | 4 | 0 | 2088 | `quick=4 slot=2908 overflow=137874 phrase=192 key_load=0.00557812 finger_load=1.04224e-05 hand_load=2.16447e-05` |
| 9 | 502 | 7424.991 | 7421 | 81 | 4 | 0 | 2097 | `quick=4 slot=2783 overflow=124219 phrase=242 key_load=0.0053266 finger_load=1.00154e-05 hand_load=2.6667e-05` |
| 10 | 671 | 7427.339 | 7421 | 81 | 4 | 0 | 2096 | `quick=4 slot=2706 overflow=141092 phrase=254 key_load=0.00572333 finger_load=1.23675e-05 hand_load=2.24817e-05` |

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
