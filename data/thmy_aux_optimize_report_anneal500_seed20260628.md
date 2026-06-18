# THMY auxiliary-code optimization report

- rounds: 500
- seed: 20260628
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
| 2 | 414 | 7389.151 | 7421 | 81 | 4 | 0 | 2023 | `quick=4 slot=4017 overflow=41618 phrase=130 key_load=0.0066612 finger_load=0.000141716 hand_load=4.32822e-05` |
| 3 | 413 | 7390.773 | 7421 | 81 | 4 | 0 | 2024 | `quick=4 slot=3973 overflow=45737 phrase=107 key_load=0.00677178 finger_load=0.000133441 hand_load=4.45618e-05` |
| 4 | 430 | 7391.775 | 7422 | 80 | 4 | 0 | 2033 | `quick=4 slot=3920 overflow=41176 phrase=144 key_load=0.00684491 finger_load=0.000145617 hand_load=4.28848e-05` |
| 5 | 412 | 7392.995 | 7421 | 81 | 4 | 0 | 2026 | `quick=4 slot=4208 overflow=46109 phrase=89 key_load=0.00704106 finger_load=0.000136877 hand_load=4.63589e-05` |
| 6 | 469 | 7395.373 | 7423 | 79 | 4 | 0 | 2043 | `quick=4 slot=3875 overflow=39863 phrase=139 key_load=0.00700638 finger_load=0.000140484 hand_load=4.29919e-05` |
| 7 | 458 | 7395.958 | 7421 | 81 | 4 | 0 | 2024 | `quick=4 slot=4165 overflow=41957 phrase=141 key_load=0.00717205 finger_load=0.00014747 hand_load=4.41741e-05` |
| 8 | 492 | 7397.584 | 7421 | 81 | 4 | 0 | 2024 | `quick=4 slot=4002 overflow=40647 phrase=141 key_load=0.00703483 finger_load=0.000141711 hand_load=4.43104e-05` |
| 9 | 432 | 7397.929 | 7422 | 80 | 4 | 0 | 2027 | `quick=4 slot=3902 overflow=41004 phrase=156 key_load=0.00683953 finger_load=0.000151195 hand_load=4.4342e-05` |
| 10 | 500 | 7401.746 | 7423 | 79 | 4 | 0 | 2045 | `quick=4 slot=3891 overflow=39435 phrase=128 key_load=0.00702548 finger_load=0.000145918 hand_load=4.15657e-05` |

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
