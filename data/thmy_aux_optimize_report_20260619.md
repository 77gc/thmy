# THMY auxiliary-code optimization report

- rounds: 100
- seed: 20260619
- candidate_limit: 96
- char_limit: all
- best_round: 18
- best_score: 7648.501

## Best parameters

| Parameter | Value |
| --- | ---: |
| quick_select_candidates | 4 |
| same_code_slot_weight | 3200 |
| same_code_overflow_weight | 13861 |
| phrase_code_collision_weight | 913 |
| key_load_weight | 0.00332014 |
| finger_load_weight | 0.00016304 |
| hand_load_weight | 0.00016902 |

## Best metrics

- one_letter: 7425
- two_letter: 77
- collisions: 2011
- phrase_collisions: 15
- same_finger_stretches: 15
- weighted_same_finger_stretches: 0.001240
- max_candidates: 4
- groups_over_quick: 0
- overflow_candidates: 0
- weighted_average: `big_same_finger=0.001 distance=8.069 hand_imbalance=1.003 repeat_key=0.020 same_finger=0.032 same_hand=0.353`
- weighted_aux_added: `big_same_finger=0.000 distance=4.139 hand_imbalance=1.000 repeat_key=0.000 same_finger=0.000 same_hand=0.144`

## Candidate group distribution

| Candidate count | Groups |
| ---: | ---: |
| 1 | 4123 |
| 2 | 1083 |
| 3 | 191 |
| 4 | 182 |

## Top trials

| Rank | Round | Score | One-letter | Two-letter | Max candidates | Groups > quick | Collisions | Parameters |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | 18 | 7648.501 | 7425 | 77 | 4 | 0 | 2011 | `quick=4 slot=3200 overflow=13861 phrase=913 key_load=0.00332014 finger_load=0.000163041 hand_load=0.00016902` |
| 2 | 12 | 7759.996 | 7425 | 77 | 4 | 0 | 2000 | `quick=4 slot=3885 overflow=138917 phrase=266 key_load=0.00209037 finger_load=8.29195e-05 hand_load=0.000376373` |
| 3 | 90 | 7781.725 | 7425 | 77 | 4 | 0 | 1998 | `quick=4 slot=3413 overflow=115013 phrase=265 key_load=0.00238034 finger_load=5.94696e-05 hand_load=0.000837178` |
| 4 | 22 | 7884.789 | 7441 | 61 | 4 | 0 | 1997 | `quick=4 slot=4342 overflow=59895 phrase=1206 key_load=0.000493345 finger_load=7.27349e-05 hand_load=0.000926245` |
| 5 | 33 | 7893.453 | 7425 | 77 | 4 | 0 | 1999 | `quick=4 slot=4039 overflow=36139 phrase=1116 key_load=0.00304009 finger_load=0.000220394 hand_load=0.000364641` |
| 6 | 20 | 7915.947 | 7429 | 73 | 4 | 0 | 1999 | `quick=4 slot=4262 overflow=197398 phrase=135 key_load=0.000929581 finger_load=0.000107824 hand_load=0.000456016` |
| 7 | 6 | 7937.500 | 7441 | 61 | 4 | 0 | 1996 | `quick=4 slot=4123 overflow=59134 phrase=1431 key_load=0.000522353 finger_load=8.26538e-05 hand_load=0.000977378` |
| 8 | 1 | 7975.486 | 7425 | 77 | 4 | 0 | 1999 | `quick=4 slot=3661 overflow=50578 phrase=1274 key_load=0.00171194 finger_load=0.000160311 hand_load=0.000574478` |
| 9 | 27 | 8004.614 | 7441 | 61 | 4 | 0 | 2014 | `quick=4 slot=4227 overflow=97764 phrase=936 key_load=0.000884287 finger_load=0.000196078 hand_load=0.00103739` |
| 10 | 34 | 8048.744 | 7425 | 77 | 4 | 0 | 2377 | `quick=4 slot=1589 overflow=31322 phrase=1267 key_load=0.00219969 finger_load=5.03068e-05 hand_load=0.000165003` |

## Largest candidate groups

| Code | Chars | Weights |
| --- | --- | --- |
| `fja` | 幅孵玞菔 | `657, 77, 20, 5` |
| `fjb` | 服黻蝮咐 | `3361, 29, 11, 2` |
| `fjc` | 附辐芣涪 | `4846, 83, 43, 42` |
| `fjf` | 拂妇绋蚨 | `244, 211, 2, 1` |
| `fjg` | 符缚呋韨 | `675, 233, 7, 1` |
| `fjh` | 富敷鄜郛 | `1296, 587, 40, 24` |
| `fjk` | 腐罘袱洑 | `218, 8, 7, 7` |
| `fjl` | 弗斧凫簠 | `799, 538, 61, 20` |
| `fjm` | 父傅祓匐 | `868, 443, 52, 8` |
| `fjn` | 副俘苻茀 | `3013, 170, 28, 11` |
| `fjo` | 浮蝠跗榑 | `375, 56, 13, 7` |
| `fjq` | 伏脯鲋艴 | `697, 48, 5, 2` |
| `fjr` | 付甫馥赙 | `2603, 319, 24, 4` |
| `fjs` | 福俯趺滏 | `1378, 126, 12, 5` |
| `fjt` | 负辅稃讣 | `4145, 375, 10, 1` |
| `fjv` | 府芙茯幞 | `1107, 594, 8, 3` |
| `fjw` | 夫覆绂宓 | `1472, 290, 16, 14` |
| `fjx` | 腹阜怫垺 | `542, 50, 7, 1` |
| `fjy` | 扶孚麸琈 | `833, 77, 23, 1` |
| `fjz` | 复赴桴驸 | `1786, 1308, 31, 10` |

## Same-Finger Stretch Pairs

Same-finger stretches count only different-key same-finger pairs with a Dvorak row gap >= 2. Repeated keys such as `uuu` and adjacent or diagonal-neighbor same-finger keys such as `ik`, `pi`, and `ki` are ignored.

| Pair | Count | Weighted average | Examples |
| --- | ---: | ---: | --- |
| `px` | 8 | 0.000861 | 派:pxv 排:pxz 拍:pxm 牌:pxw 徘:pxb 湃:pxn 俳:pxr 哌:pxs |
| `ky` | 6 | 0.000379 | 卡:kyt 咖:kyr 喀:kyl 咯:kyw 咔:kyf 胩:kyg |
| `kp` | 1 | 0.000001 | 剋:kpr |
