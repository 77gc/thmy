# THMY auxiliary-code optimization report

- rounds: 500
- seed: 20260631
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
| 2 | 450 | 7417.078 | 7424 | 78 | 4 | 0 | 2098 | `quick=4 slot=3109 overflow=76626 phrase=1151 key_load=0.0067294 finger_load=5.64645e-05 hand_load=3.06029e-05` |
| 3 | 470 | 7426.365 | 7424 | 78 | 4 | 0 | 2098 | `quick=4 slot=3169 overflow=72447 phrase=1145 key_load=0.0065257 finger_load=5.21112e-05 hand_load=3.11269e-05` |
| 4 | 418 | 7427.837 | 7424 | 78 | 4 | 0 | 2100 | `quick=4 slot=2938 overflow=67612 phrase=1189 key_load=0.00654422 finger_load=5.43602e-05 hand_load=3.07938e-05` |
| 5 | 238 | 7430.160 | 7420 | 82 | 4 | 0 | 2052 | `quick=4 slot=3088 overflow=66111 phrase=1498 key_load=0.00543108 finger_load=4.78077e-05 hand_load=3.78337e-05` |
| 6 | 326 | 7432.125 | 7421 | 81 | 4 | 0 | 2040 | `quick=4 slot=2811 overflow=64134 phrase=1207 key_load=0.00487469 finger_load=6.18026e-05 hand_load=3.04299e-05` |
| 7 | 357 | 7432.478 | 7421 | 81 | 4 | 0 | 2054 | `quick=4 slot=3313 overflow=64825 phrase=1206 key_load=0.00595988 finger_load=5.885e-05 hand_load=2.76802e-05` |
| 8 | 491 | 7433.050 | 7424 | 78 | 4 | 0 | 2100 | `quick=4 slot=2931 overflow=72606 phrase=1159 key_load=0.00648301 finger_load=5.46882e-05 hand_load=3.07341e-05` |
| 9 | 475 | 7433.688 | 7425 | 77 | 4 | 0 | 2099 | `quick=4 slot=3088 overflow=77865 phrase=1135 key_load=0.00640378 finger_load=5.52792e-05 hand_load=2.91361e-05` |
| 10 | 428 | 7434.605 | 7424 | 78 | 4 | 0 | 2100 | `quick=4 slot=2866 overflow=73902 phrase=1170 key_load=0.00603989 finger_load=5.48844e-05 hand_load=3.01939e-05` |

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
