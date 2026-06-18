# THMY auxiliary-code optimization report

- rounds: 500
- seed: 20260623
- candidate_limit: 96
- char_limit: all
- best_round: 78
- best_score: 7369.794

## Best parameters

| Parameter | Value |
| --- | ---: |
| quick_select_candidates | 4 |
| same_code_slot_weight | 3133 |
| same_code_overflow_weight | 15853 |
| phrase_code_collision_weight | 1500 |
| key_load_weight | 0.00531709 |
| finger_load_weight | 0.00010439 |
| hand_load_weight | 0.00004220 |

## Best metrics

- one_letter: 7422
- two_letter: 80
- collisions: 2034
- phrase_collisions: 18
- same_finger_stretches: 15
- weighted_same_finger_stretches: 0.001240
- max_candidates: 4
- groups_over_quick: 0
- overflow_candidates: 0
- weighted_average: `big_same_finger=0.001 distance=8.230 hand_imbalance=1.003 repeat_key=0.020 same_finger=0.032 same_hand=0.271`
- weighted_aux_added: `big_same_finger=0.000 distance=4.299 hand_imbalance=1.000 repeat_key=0.000 same_finger=0.000 same_hand=0.063`

## Candidate group distribution

| Candidate count | Groups |
| ---: | ---: |
| 1 | 4081 |
| 2 | 1097 |
| 3 | 197 |
| 4 | 181 |

## Top trials

| Rank | Round | Score | One-letter | Two-letter | Max candidates | Groups > quick | Collisions | Parameters |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | 78 | 7369.794 | 7422 | 80 | 4 | 0 | 2034 | `quick=4 slot=3133 overflow=15853 phrase=1500 key_load=0.00531709 finger_load=0.000104386 hand_load=4.21977e-05` |
| 2 | 76 | 7384.324 | 7418 | 84 | 4 | 0 | 2033 | `quick=4 slot=3042 overflow=19362 phrase=1438 key_load=0.00484165 finger_load=9.86845e-05 hand_load=4.36495e-05` |
| 3 | 85 | 7388.951 | 7418 | 84 | 4 | 0 | 2028 | `quick=4 slot=2960 overflow=13964 phrase=1402 key_load=0.00475596 finger_load=9.54981e-05 hand_load=4.2672e-05` |
| 4 | 79 | 7389.091 | 7423 | 79 | 4 | 0 | 2035 | `quick=4 slot=3067 overflow=14640 phrase=1319 key_load=0.00531709 finger_load=0.000117986 hand_load=4.56675e-05` |
| 5 | 91 | 7412.003 | 7423 | 79 | 4 | 0 | 2051 | `quick=4 slot=2948 overflow=23104 phrase=1251 key_load=0.00531709 finger_load=0.000116814 hand_load=4.21977e-05` |
| 6 | 80 | 7422.176 | 7422 | 80 | 4 | 0 | 2060 | `quick=4 slot=3036 overflow=16211 phrase=1355 key_load=0.00517476 finger_load=8.81233e-05 hand_load=4.21977e-05` |
| 7 | 90 | 7437.288 | 7415 | 87 | 4 | 0 | 2026 | `quick=4 slot=3068 overflow=15929 phrase=1500 key_load=0.00455124 finger_load=0.000106179 hand_load=4.21977e-05` |
| 8 | 484 | 7479.155 | 7424 | 78 | 4 | 0 | 2048 | `quick=4 slot=2624 overflow=14901 phrase=1292 key_load=0.00352654 finger_load=5.16099e-05 hand_load=8.59028e-05` |
| 9 | 1 | 7484.232 | 7424 | 78 | 4 | 0 | 2034 | `quick=4 slot=2567 overflow=40319 phrase=421 key_load=0.00295394 finger_load=8.87198e-05 hand_load=9.37727e-05` |
| 10 | 457 | 7488.870 | 7424 | 78 | 4 | 0 | 2039 | `quick=4 slot=2658 overflow=14483 phrase=1262 key_load=0.00358731 finger_load=5.15693e-05 hand_load=8.5181e-05` |

## Largest candidate groups

| Code | Chars | Weights |
| --- | --- | --- |
| `bnq` | 币蓖萆馝 | `2666, 13, 6, 1` |
| `fja` | 伏敷芣鲋 | `697, 587, 43, 5` |
| `fjb` | 福赴桴驸 | `1378, 1308, 31, 10` |
| `fjc` | 付甫鄜郛 | `2603, 319, 40, 24` |
| `fjf` | 副傅馥赙 | `3013, 443, 24, 4` |
| `fjg` | 负俘趺幞 | `4145, 170, 12, 3` |
| `fjh` | 服斧呋韨 | `3361, 538, 7, 1` |
| `fji` | 腐阜怫垺 | `218, 50, 7, 1` |
| `fjk` | 妇脯玞跗 | `211, 48, 20, 13` |
| `fjl` | 扶孵涪簠 | `833, 77, 42, 20` |
| `fjm` | 父覆黻苻 | `868, 290, 29, 28` |
| `fjn` | 弗俯稃蚨 | `799, 126, 10, 1` |
| `fjp` | 浮袱榑菔 | `375, 7, 7, 5` |
| `fjq` | 附芙凫艴 | `4846, 594, 61, 2` |
| `fjr` | 夫拂茯滏 | `1472, 244, 8, 5` |
| `fjs` | 富辐绋讣 | `1296, 83, 2, 1` |
| `fjv` | 府绂匐咐 | `1107, 16, 8, 2` |
| `fjw` | 符辅宓茀 | `675, 375, 14, 11` |
| `fjx` | 幅蝠罘洑 | `657, 56, 8, 7` |
| `fjy` | 腹孚麸琈 | `542, 77, 23, 1` |

## Same-Finger Stretch Pairs

Same-finger stretches count only different-key same-finger pairs with a Dvorak row gap >= 2. Repeated keys such as `uuu` and adjacent or diagonal-neighbor same-finger keys such as `ik`, `pi`, and `ki` are ignored.

| Pair | Count | Weighted average | Examples |
| --- | ---: | ---: | --- |
| `px` | 8 | 0.000861 | 派:pxb 排:pxz 拍:pxv 牌:pxm 徘:pxw 湃:pxs 俳:pxf 哌:pxg |
| `ky` | 6 | 0.000379 | 卡:kyg 咖:kyf 喀:kyr 咯:kyl 咔:kyc 胩:kyb |
| `kp` | 1 | 0.000001 | 剋:kpf |
