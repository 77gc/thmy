# THMY auxiliary-code optimization report

- rounds: 500
- seed: 20260626
- candidate_limit: 96
- char_limit: all
- best_round: 294
- best_score: 7373.052

## Best parameters

| Parameter | Value |
| --- | ---: |
| quick_select_candidates | 4 |
| same_code_slot_weight | 2957 |
| same_code_overflow_weight | 19103 |
| phrase_code_collision_weight | 432 |
| key_load_weight | 0.00531709 |
| finger_load_weight | 0.00014317 |
| hand_load_weight | 0.00004619 |

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
- weighted_average: `big_same_finger=0.001 distance=8.237 hand_imbalance=1.003 repeat_key=0.020 same_finger=0.032 same_hand=0.273`
- weighted_aux_added: `big_same_finger=0.000 distance=4.307 hand_imbalance=1.000 repeat_key=0.000 same_finger=0.000 same_hand=0.065`

## Candidate group distribution

| Candidate count | Groups |
| ---: | ---: |
| 1 | 4080 |
| 2 | 1096 |
| 3 | 194 |
| 4 | 184 |

## Top trials

| Rank | Round | Score | One-letter | Two-letter | Max candidates | Groups > quick | Collisions | Parameters |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | 294 | 7373.052 | 7425 | 77 | 4 | 0 | 2036 | `quick=4 slot=2957 overflow=19103 phrase=432 key_load=0.00531709 finger_load=0.000143168 hand_load=4.61899e-05` |
| 2 | 441 | 7377.902 | 7425 | 77 | 4 | 0 | 2037 | `quick=4 slot=2981 overflow=18329 phrase=418 key_load=0.00531709 finger_load=0.00014581 hand_load=4.79925e-05` |
| 3 | 471 | 7378.285 | 7425 | 77 | 4 | 0 | 2041 | `quick=4 slot=2928 overflow=19470 phrase=435 key_load=0.00531709 finger_load=0.000141801 hand_load=4.68182e-05` |
| 4 | 432 | 7379.982 | 7425 | 77 | 4 | 0 | 2036 | `quick=4 slot=2969 overflow=18676 phrase=425 key_load=0.00531709 finger_load=0.000145935 hand_load=4.77557e-05` |
| 5 | 413 | 7380.494 | 7424 | 78 | 4 | 0 | 2036 | `quick=4 slot=2991 overflow=19802 phrase=434 key_load=0.00529938 finger_load=0.00014142 hand_load=4.74765e-05` |
| 6 | 405 | 7384.380 | 7424 | 78 | 4 | 0 | 2036 | `quick=4 slot=2932 overflow=19576 phrase=450 key_load=0.00521838 finger_load=0.000136497 hand_load=4.52059e-05` |
| 7 | 208 | 7385.427 | 7424 | 78 | 4 | 0 | 2035 | `quick=4 slot=2963 overflow=13725 phrase=524 key_load=0.00531709 finger_load=0.000146014 hand_load=4.21977e-05` |
| 8 | 493 | 7385.583 | 7425 | 77 | 4 | 0 | 2057 | `quick=4 slot=2883 overflow=19496 phrase=437 key_load=0.00531709 finger_load=0.000137192 hand_load=4.60324e-05` |
| 9 | 478 | 7386.838 | 7423 | 79 | 4 | 0 | 2035 | `quick=4 slot=2991 overflow=18273 phrase=419 key_load=0.00531709 finger_load=0.000139901 hand_load=4.62027e-05` |
| 10 | 487 | 7386.995 | 7423 | 79 | 4 | 0 | 2034 | `quick=4 slot=3005 overflow=19158 phrase=450 key_load=0.00531709 finger_load=0.000141841 hand_load=4.72891e-05` |

## Largest candidate groups

| Code | Chars | Weights |
| --- | --- | --- |
| `bne` | 笔敝萆馝 | `6838, 167, 6, 1` |
| `fja` | 伏敷涪艴 | `697, 587, 42, 2` |
| `fjb` | 夫肤黻苻 | `1472, 69, 29, 28` |
| `fjc` | 扶孵玞跗 | `833, 77, 20, 13` |
| `fjf` | 付甫稃蚨 | `2603, 319, 10, 1` |
| `fjg` | 附郛滏咐 | `4846, 24, 5, 2` |
| `fjh` | 复辅幞讣 | `1786, 375, 3, 1` |
| `fji` | 腐阜麸垺 | `218, 50, 23, 1` |
| `fjk` | 弗脯芣鲋 | `799, 48, 43, 5` |
| `fjl` | 服芙凫鄜 | `3361, 594, 61, 40` |
| `fjm` | 负俘宓茀 | `4145, 170, 14, 11` |
| `fjn` | 富拂茯绋 | `1296, 244, 8, 2` |
| `fjp` | 幅蝠榑菔 | `657, 56, 7, 5` |
| `fjq` | 妇辐馥赙 | `211, 83, 24, 4` |
| `fjr` | 府俯趺韨 | `1107, 126, 12, 1` |
| `fjs` | 副斧簠呋 | `3013, 538, 20, 7` |
| `fjv` | 福赴绂蝮 | `1378, 1308, 16, 11` |
| `fjw` | 符傅桴驸 | `675, 443, 31, 10` |
| `fjx` | 浮罘袱洑 | `375, 8, 7, 7` |
| `fjy` | 腹孚怫琈 | `542, 77, 7, 1` |

## Same-Finger Stretch Pairs

Same-finger stretches count only different-key same-finger pairs with a Dvorak row gap >= 2. Repeated keys such as `uuu` and adjacent or diagonal-neighbor same-finger keys such as `ik`, `pi`, and `ki` are ignored.

| Pair | Count | Weighted average | Examples |
| --- | ---: | ---: | --- |
| `px` | 8 | 0.000861 | 派:pxv 排:pxz 拍:pxb 牌:pxm 徘:pxw 湃:pxh 俳:pxg 哌:pxn |
| `ky` | 6 | 0.000379 | 卡:kys 咖:kyr 喀:kyf 咯:kyq 咔:kyl 胩:kyg |
| `kp` | 1 | 0.000001 | 剋:kpg |
