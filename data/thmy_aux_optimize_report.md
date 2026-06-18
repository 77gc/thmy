# THMY auxiliary-code optimization report

- rounds: 100
- seed: 20260618
- candidate_limit: 96
- char_limit: all
- best_round: 67
- best_score: 7975.486

## Best parameters

| Parameter | Value |
| --- | ---: |
| quick_select_candidates | 4 |
| same_code_slot_weight | 3661 |
| same_code_overflow_weight | 50578 |
| phrase_code_collision_weight | 1274 |
| key_load_weight | 0.00171194 |
| finger_load_weight | 0.00016031 |
| hand_load_weight | 0.00057448 |

## Best metrics

- one_letter: 7425
- two_letter: 77
- collisions: 1999
- phrase_collisions: 13
- same_finger_stretches: 15
- weighted_same_finger_stretches: 0.001240
- max_candidates: 4
- groups_over_quick: 0
- overflow_candidates: 0
- weighted_average: `big_same_finger=0.001 distance=8.165 hand_imbalance=1.033 repeat_key=0.020 same_finger=0.032 same_hand=0.394`
- weighted_aux_added: `big_same_finger=0.000 distance=4.234 hand_imbalance=1.000 repeat_key=0.000 same_finger=0.000 same_hand=0.185`

## Candidate group distribution

| Candidate count | Groups |
| ---: | ---: |
| 1 | 4144 |
| 2 | 1076 |
| 3 | 190 |
| 4 | 181 |

## Top trials

| Rank | Round | Score | One-letter | Two-letter | Max candidates | Groups > quick | Collisions | Parameters |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | 67 | 7975.486 | 7425 | 77 | 4 | 0 | 1999 | `quick=4 slot=3661 overflow=50578 phrase=1274 key_load=0.00171194 finger_load=0.000160311 hand_load=0.000574478` |
| 2 | 25 | 8055.959 | 7439 | 63 | 4 | 0 | 2131 | `quick=4 slot=3148 overflow=36637 phrase=25 key_load=0.000506325 finger_load=0.000309617 hand_load=0.000555412` |
| 3 | 14 | 8071.709 | 7437 | 65 | 4 | 0 | 2084 | `quick=4 slot=3058 overflow=135367 phrase=848 key_load=0.000357208 finger_load=0.000221137 hand_load=0.000393317` |
| 4 | 65 | 8085.673 | 7434 | 68 | 4 | 0 | 2082 | `quick=4 slot=3181 overflow=177634 phrase=740 key_load=0.000503906 finger_load=0.000176214 hand_load=0.000397468` |
| 5 | 5 | 8183.296 | 7433 | 69 | 4 | 0 | 2127 | `quick=4 slot=2990 overflow=52701 phrase=1352 key_load=0.000729964 finger_load=0.000322962 hand_load=0.000448677` |
| 6 | 31 | 8302.061 | 7433 | 69 | 4 | 0 | 2279 | `quick=4 slot=2640 overflow=26352 phrase=1353 key_load=0.000815795 finger_load=0.000283895 hand_load=0.000476809` |
| 7 | 51 | 8335.917 | 7425 | 77 | 4 | 0 | 2503 | `quick=4 slot=1262 overflow=18073 phrase=280 key_load=0.00058235 finger_load=0.000187603 hand_load=9.60197e-05` |
| 8 | 49 | 8341.814 | 7441 | 61 | 4 | 0 | 2446 | `quick=4 slot=1429 overflow=79785 phrase=939 key_load=0.000762497 finger_load=0.000189876 hand_load=0.000539091` |
| 9 | 56 | 8365.962 | 7425 | 77 | 4 | 0 | 2463 | `quick=4 slot=1338 overflow=102892 phrase=1156 key_load=0.00197423 finger_load=0.000291338 hand_load=0.000244319` |
| 10 | 29 | 8407.857 | 7425 | 77 | 4 | 0 | 2540 | `quick=4 slot=1110 overflow=149435 phrase=35 key_load=0.00195002 finger_load=0.000163102 hand_load=0.000317817` |

## Largest candidate groups

| Code | Chars | Weights |
| --- | --- | --- |
| `fja` | 伏俯趺滏 | `697, 126, 12, 5` |
| `fjb` | 服俘馥赙 | `3361, 170, 24, 4` |
| `fjc` | 拂腐玞鲋 | `244, 218, 20, 5` |
| `fjg` | 附斧芣涪 | `4846, 538, 43, 42` |
| `fjh` | 负凫脯簠 | `4145, 61, 48, 20` |
| `fjk` | 芙妇呋韨 | `594, 211, 7, 1` |
| `fjl` | 幅孵跗榑 | `657, 77, 13, 7` |
| `fjm` | 复赴茀匐 | `1786, 1308, 11, 8` |
| `fjn` | 福甫幞讣 | `1378, 319, 3, 1` |
| `fjo` | 弗敷绋蚨 | `799, 587, 2, 1` |
| `fjp` | 扶孚麸琈 | `833, 77, 23, 1` |
| `fjq` | 副祓苻咐 | `3013, 52, 28, 2` |
| `fjr` | 符缚鄜郛 | `675, 233, 40, 24` |
| `fjs` | 付辐稃茯 | `2603, 83, 10, 8` |
| `fjt` | 富袱菔艴 | `1296, 7, 5, 2` |
| `fju` | 浮蝠罘洑 | `375, 56, 8, 7` |
| `fjv` | 府傅桴蝮 | `1107, 443, 31, 11` |
| `fjw` | 夫辅黻宓 | `1472, 375, 29, 14` |
| `fjx` | 腹阜怫垺 | `542, 50, 7, 1` |
| `fjz` | 父覆绂驸 | `868, 290, 16, 10` |

## Same-Finger Stretch Pairs

Same-finger stretches count only different-key same-finger pairs with a Dvorak row gap >= 2. Repeated keys such as `uuu` and adjacent or diagonal-neighbor same-finger keys such as `ik`, `pi`, and `ki` are ignored.

| Pair | Count | Weighted average | Examples |
| --- | ---: | ---: | --- |
| `px` | 8 | 0.000861 | 派:pxz 排:pxm 拍:pxw 牌:pxv 徘:pxb 湃:pxn 俳:pxs 哌:pxr |
| `ky` | 6 | 0.000379 | 卡:kyg 咖:kyr 喀:kyc 咯:kyl 咔:kyw 胩:kys |
| `kp` | 1 | 0.000001 | 剋:kpr |
