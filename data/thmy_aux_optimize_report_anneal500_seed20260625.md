# THMY auxiliary-code optimization report

- rounds: 500
- seed: 20260625
- candidate_limit: 96
- char_limit: all
- best_round: 437
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
| 1 | 437 | 7359.608 | 7425 | 77 | 4 | 0 | 2036 | `quick=4 slot=2967 overflow=35507 phrase=513 key_load=0.00531709 finger_load=0.000155066 hand_load=4.3388e-05` |
| 2 | 450 | 7366.777 | 7424 | 78 | 4 | 0 | 2036 | `quick=4 slot=2996 overflow=37325 phrase=520 key_load=0.00531709 finger_load=0.000155066 hand_load=4.2713e-05` |
| 3 | 411 | 7366.924 | 7425 | 77 | 4 | 0 | 2035 | `quick=4 slot=2987 overflow=36536 phrase=524 key_load=0.00531709 finger_load=0.000155202 hand_load=4.52572e-05` |
| 4 | 481 | 7367.876 | 7425 | 77 | 4 | 0 | 2041 | `quick=4 slot=2922 overflow=34547 phrase=485 key_load=0.00531709 finger_load=0.000155568 hand_load=4.39531e-05` |
| 5 | 484 | 7371.578 | 7425 | 77 | 4 | 0 | 2043 | `quick=4 slot=2954 overflow=36561 phrase=508 key_load=0.00525519 finger_load=0.000153701 hand_load=4.27192e-05` |
| 6 | 396 | 7376.009 | 7423 | 79 | 4 | 0 | 2034 | `quick=4 slot=3075 overflow=36884 phrase=517 key_load=0.00531709 finger_load=0.000155573 hand_load=4.54812e-05` |
| 7 | 470 | 7377.306 | 7425 | 77 | 4 | 0 | 2037 | `quick=4 slot=2981 overflow=33759 phrase=508 key_load=0.00531709 finger_load=0.000154742 hand_load=4.32161e-05` |
| 8 | 330 | 7379.150 | 7425 | 77 | 4 | 0 | 2041 | `quick=4 slot=2906 overflow=35200 phrase=515 key_load=0.00531709 finger_load=0.000154827 hand_load=4.66842e-05` |
| 9 | 490 | 7380.669 | 7425 | 77 | 4 | 0 | 2043 | `quick=4 slot=2868 overflow=35013 phrase=498 key_load=0.00531709 finger_load=0.000155633 hand_load=4.32232e-05` |
| 10 | 494 | 7383.959 | 7425 | 77 | 4 | 0 | 2044 | `quick=4 slot=2937 overflow=35480 phrase=556 key_load=0.00531709 finger_load=0.000156379 hand_load=4.41942e-05` |

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
