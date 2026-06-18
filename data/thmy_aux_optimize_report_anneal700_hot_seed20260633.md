# THMY auxiliary-code optimization report

- rounds: 700
- seed: 20260633
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
| 2 | 693 | 7391.753 | 7424 | 78 | 4 | 0 | 2101 | `quick=4 slot=2898 overflow=25862 phrase=174 key_load=0.00674718 finger_load=2.16125e-05 hand_load=1.55416e-05` |
| 3 | 688 | 7395.172 | 7424 | 78 | 4 | 0 | 2102 | `quick=4 slot=2970 overflow=24131 phrase=168 key_load=0.00704589 finger_load=2.18319e-05 hand_load=1.53935e-05` |
| 4 | 495 | 7397.998 | 7425 | 77 | 4 | 0 | 2105 | `quick=4 slot=2936 overflow=21387 phrase=267 key_load=0.00744964 finger_load=2.17444e-05 hand_load=1.47206e-05` |
| 5 | 506 | 7405.676 | 7424 | 78 | 4 | 0 | 2103 | `quick=4 slot=2903 overflow=25334 phrase=206 key_load=0.00728539 finger_load=2.3401e-05 hand_load=1.76173e-05` |
| 6 | 633 | 7411.348 | 7424 | 78 | 4 | 0 | 2101 | `quick=4 slot=2984 overflow=26081 phrase=131 key_load=0.00736325 finger_load=2.25754e-05 hand_load=1.54115e-05` |
| 7 | 561 | 7411.790 | 7424 | 78 | 4 | 0 | 2100 | `quick=4 slot=3297 overflow=27532 phrase=194 key_load=0.00815323 finger_load=2.3591e-05 hand_load=1.67176e-05` |
| 8 | 644 | 7411.939 | 7424 | 78 | 4 | 0 | 2122 | `quick=4 slot=2766 overflow=27228 phrase=159 key_load=0.00705865 finger_load=2.23701e-05 hand_load=1.56064e-05` |
| 9 | 678 | 7415.230 | 7424 | 78 | 4 | 0 | 2102 | `quick=4 slot=3008 overflow=25373 phrase=141 key_load=0.00724736 finger_load=2.25256e-05 hand_load=1.66908e-05` |
| 10 | 558 | 7415.231 | 7424 | 78 | 4 | 0 | 2100 | `quick=4 slot=2978 overflow=25275 phrase=173 key_load=0.00746304 finger_load=2.39841e-05 hand_load=1.35726e-05` |

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
