# THMY auxiliary-code optimization report

- rounds: 500
- seed: 20260620
- candidate_limit: 96
- char_limit: all
- best_round: 400
- best_score: 7549.997

## Best parameters

| Parameter | Value |
| --- | ---: |
| quick_select_candidates | 4 |
| same_code_slot_weight | 2516 |
| same_code_overflow_weight | 30064 |
| phrase_code_collision_weight | 1362 |
| key_load_weight | 0.00352828 |
| finger_load_weight | 0.00011541 |
| hand_load_weight | 0.00010164 |

## Best metrics

- one_letter: 7425
- two_letter: 77
- collisions: 2045
- phrase_collisions: 16
- same_finger_stretches: 15
- weighted_same_finger_stretches: 0.001240
- max_candidates: 4
- groups_over_quick: 0
- overflow_candidates: 0
- weighted_average: `big_same_finger=0.001 distance=8.205 hand_imbalance=1.003 repeat_key=0.020 same_finger=0.032 same_hand=0.308`
- weighted_aux_added: `big_same_finger=0.000 distance=4.274 hand_imbalance=1.000 repeat_key=0.000 same_finger=0.000 same_hand=0.099`

## Candidate group distribution

| Candidate count | Groups |
| ---: | ---: |
| 1 | 4066 |
| 2 | 1099 |
| 3 | 194 |
| 4 | 186 |

## Top trials

| Rank | Round | Score | One-letter | Two-letter | Max candidates | Groups > quick | Collisions | Parameters |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | 400 | 7549.997 | 7425 | 77 | 4 | 0 | 2045 | `quick=4 slot=2516 overflow=30064 phrase=1362 key_load=0.00352828 finger_load=0.000115411 hand_load=0.000101642` |
| 2 | 382 | 7585.514 | 7423 | 79 | 4 | 0 | 2038 | `quick=4 slot=3398 overflow=18734 phrase=542 key_load=0.00526758 finger_load=0.000103244 hand_load=8.98682e-05` |
| 3 | 70 | 7589.151 | 7423 | 79 | 4 | 0 | 2020 | `quick=4 slot=3471 overflow=11723 phrase=554 key_load=0.00494975 finger_load=0.000110417 hand_load=0.000104967` |
| 4 | 181 | 7603.737 | 7425 | 77 | 4 | 0 | 2010 | `quick=4 slot=3392 overflow=36412 phrase=401 key_load=0.00481796 finger_load=0.000133133 hand_load=0.000147056` |
| 5 | 106 | 7607.293 | 7424 | 78 | 4 | 0 | 2023 | `quick=4 slot=2975 overflow=31612 phrase=700 key_load=0.00441688 finger_load=0.000124874 hand_load=8.0516e-05` |
| 6 | 126 | 7607.882 | 7425 | 77 | 4 | 0 | 2111 | `quick=4 slot=2393 overflow=21377 phrase=752 key_load=0.00296873 finger_load=9.72274e-05 hand_load=9.54618e-05` |
| 7 | 243 | 7615.359 | 7424 | 78 | 4 | 0 | 2007 | `quick=4 slot=4115 overflow=24996 phrase=1296 key_load=0.00495076 finger_load=0.000142346 hand_load=0.000154889` |
| 8 | 178 | 7633.492 | 7424 | 78 | 4 | 0 | 2025 | `quick=4 slot=2650 overflow=35153 phrase=501 key_load=0.00308815 finger_load=0.00012853 hand_load=0.000104899` |
| 9 | 435 | 7634.566 | 7421 | 81 | 4 | 0 | 2009 | `quick=4 slot=3828 overflow=19183 phrase=558 key_load=0.00542903 finger_load=0.000155649 hand_load=8.53319e-05` |
| 10 | 440 | 7637.141 | 7424 | 78 | 4 | 0 | 2023 | `quick=4 slot=3136 overflow=17145 phrase=745 key_load=0.00496397 finger_load=0.000108289 hand_load=7.83249e-05` |

## Largest candidate groups

| Code | Chars | Weights |
| --- | --- | --- |
| `bnj` | 闭愎佖秕 | `312, 10, 3, 2` |
| `bno` | 彼蓖荜馝 | `909, 13, 5, 1` |
| `fja` | 伏脯芣鲋 | `697, 48, 43, 5` |
| `fjb` | 复覆祓苻 | `1786, 290, 52, 28` |
| `fjc` | 附缚宓幞 | `4846, 233, 14, 3` |
| `fjf` | 副傅茀讣 | `3013, 443, 11, 1` |
| `fjg` | 富斧凫簠 | `1296, 538, 61, 20` |
| `fjh` | 福芙呋韨 | `1378, 594, 7, 1` |
| `fji` | 抚腑麸琈 | `249, 103, 23, 1` |
| `fjk` | 浮孵榑菔 | `375, 77, 7, 5` |
| `fjl` | 付拂郛稃 | `2603, 244, 24, 10` |
| `fjm` | 夫赴绂蝮 | `1472, 1308, 16, 11` |
| `fjn` | 符茯咐绋 | `675, 8, 2, 2` |
| `fjo` | 幅蝠玞跗 | `657, 56, 20, 13` |
| `fjp` | 腐阜怫垺 | `218, 50, 7, 1` |
| `fjq` | 弗敷涪艴 | `799, 587, 42, 2` |
| `fjr` | 妇俘鄜蚨 | `211, 170, 40, 1` |
| `fjt` | 负俯趺赙 | `4145, 126, 12, 4` |
| `fjv` | 父辅黻驸 | `868, 375, 29, 10` |
| `fjw` | 府辐馥滏 | `1107, 83, 24, 5` |

## Same-Finger Stretch Pairs

Same-finger stretches count only different-key same-finger pairs with a Dvorak row gap >= 2. Repeated keys such as `uuu` and adjacent or diagonal-neighbor same-finger keys such as `ik`, `pi`, and `ki` are ignored.

| Pair | Count | Weighted average | Examples |
| --- | ---: | ---: | --- |
| `px` | 8 | 0.000861 | 派:pxv 排:pxm 拍:pxb 牌:pxf 徘:pxz 湃:pxw 俳:pxt 哌:pxc |
| `ky` | 6 | 0.000379 | 卡:kyl 咖:kyf 喀:kyc 咯:kyv 咔:kyr 胩:kyt |
| `kp` | 1 | 0.000001 | 剋:kpf |
