# THMY auxiliary-code optimization report

- rounds: 500
- seed: 20260622
- candidate_limit: 96
- char_limit: all
- best_round: 479
- best_score: 7478.323

## Best parameters

| Parameter | Value |
| --- | ---: |
| quick_select_candidates | 4 |
| same_code_slot_weight | 2558 |
| same_code_overflow_weight | 20421 |
| phrase_code_collision_weight | 275 |
| key_load_weight | 0.00340577 |
| finger_load_weight | 0.00005668 |
| hand_load_weight | 0.00008626 |

## Best metrics

- one_letter: 7425
- two_letter: 77
- collisions: 2043
- phrase_collisions: 19
- same_finger_stretches: 15
- weighted_same_finger_stretches: 0.001240
- max_candidates: 4
- groups_over_quick: 0
- overflow_candidates: 0
- weighted_average: `big_same_finger=0.001 distance=8.097 hand_imbalance=1.003 repeat_key=0.020 same_finger=0.032 same_hand=0.314`
- weighted_aux_added: `big_same_finger=0.000 distance=4.167 hand_imbalance=1.000 repeat_key=0.000 same_finger=0.000 same_hand=0.105`

## Candidate group distribution

| Candidate count | Groups |
| ---: | ---: |
| 1 | 4069 |
| 2 | 1096 |
| 3 | 199 |
| 4 | 183 |

## Top trials

| Rank | Round | Score | One-letter | Two-letter | Max candidates | Groups > quick | Collisions | Parameters |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | 479 | 7478.323 | 7425 | 77 | 4 | 0 | 2043 | `quick=4 slot=2558 overflow=20421 phrase=275 key_load=0.00340577 finger_load=5.66826e-05 hand_load=8.62618e-05` |
| 2 | 469 | 7482.328 | 7424 | 78 | 4 | 0 | 2041 | `quick=4 slot=2584 overflow=20793 phrase=274 key_load=0.00347198 finger_load=5.57265e-05 hand_load=8.82663e-05` |
| 3 | 483 | 7483.021 | 7425 | 77 | 4 | 0 | 2042 | `quick=4 slot=2557 overflow=20146 phrase=272 key_load=0.00346214 finger_load=5.69216e-05 hand_load=8.65951e-05` |
| 4 | 366 | 7483.420 | 7424 | 78 | 4 | 0 | 2040 | `quick=4 slot=2684 overflow=19924 phrase=302 key_load=0.00356296 finger_load=5.5088e-05 hand_load=8.79841e-05` |
| 5 | 430 | 7483.713 | 7425 | 77 | 4 | 0 | 2041 | `quick=4 slot=2675 overflow=20573 phrase=296 key_load=0.00351233 finger_load=5.71796e-05 hand_load=9.47209e-05` |
| 6 | 1 | 7484.232 | 7424 | 78 | 4 | 0 | 2034 | `quick=4 slot=2567 overflow=40319 phrase=421 key_load=0.00295394 finger_load=8.87198e-05 hand_load=9.37727e-05` |
| 7 | 460 | 7486.957 | 7424 | 78 | 4 | 0 | 2040 | `quick=4 slot=2688 overflow=19789 phrase=293 key_load=0.0034986 finger_load=5.66848e-05 hand_load=9.27948e-05` |
| 8 | 475 | 7487.178 | 7425 | 77 | 4 | 0 | 2049 | `quick=4 slot=2563 overflow=20555 phrase=269 key_load=0.00348476 finger_load=5.55707e-05 hand_load=8.55308e-05` |
| 9 | 400 | 7489.295 | 7424 | 78 | 4 | 0 | 2041 | `quick=4 slot=2631 overflow=20741 phrase=291 key_load=0.00345026 finger_load=5.65996e-05 hand_load=8.8582e-05` |
| 10 | 488 | 7491.351 | 7424 | 78 | 4 | 0 | 2041 | `quick=4 slot=2647 overflow=20294 phrase=264 key_load=0.00346789 finger_load=5.51703e-05 hand_load=8.88326e-05` |

## Largest candidate groups

| Code | Chars | Weights |
| --- | --- | --- |
| `fja` | 伏孵芣鲋 | `697, 77, 43, 5` |
| `fjb` | 复傅祓蝮 | `1786, 443, 52, 11` |
| `fjc` | 富趺幞咐 | `1296, 12, 3, 2` |
| `fjf` | 芙妇呋韨 | `594, 211, 7, 1` |
| `fjg` | 付拂鄜郛 | `2603, 244, 40, 24` |
| `fjh` | 福缚茯绋 | `1378, 233, 8, 2` |
| `fjk` | 幅脯玞跗 | `657, 48, 20, 13` |
| `fjl` | 副辐稃蚨 | `3013, 83, 10, 1` |
| `fjm` | 赴府绂匐 | `1308, 1107, 16, 8` |
| `fjo` | 腹蝠榑菔 | `542, 56, 7, 5` |
| `fjp` | 浮袱怫垺 | `375, 7, 7, 1` |
| `fjq` | 弗敷涪簠 | `799, 587, 42, 20` |
| `fjr` | 符斧凫艴 | `675, 538, 61, 2` |
| `fjs` | 负甫馥滏 | `4145, 319, 24, 5` |
| `fjt` | 附俘赙讣 | `4846, 170, 4, 1` |
| `fjv` | 父肤桴驸 | `868, 69, 31, 10` |
| `fjw` | 服辅黻宓 | `3361, 375, 29, 14` |
| `fjx` | 腐阜罘洑 | `218, 50, 8, 7` |
| `fjy` | 扶孚麸琈 | `833, 77, 23, 1` |
| `fjz` | 夫覆苻茀 | `1472, 290, 28, 11` |

## Same-Finger Stretch Pairs

Same-finger stretches count only different-key same-finger pairs with a Dvorak row gap >= 2. Repeated keys such as `uuu` and adjacent or diagonal-neighbor same-finger keys such as `ik`, `pi`, and `ki` are ignored.

| Pair | Count | Weighted average | Examples |
| --- | ---: | ---: | --- |
| `px` | 8 | 0.000861 | 派:pxm 排:pxv 拍:pxw 牌:pxb 徘:pxz 湃:pxs 俳:pxt 哌:pxc |
| `ky` | 6 | 0.000379 | 卡:kyb 咖:kyc 喀:kyg 咯:kyl 咔:kyv 胩:kyf |
| `kp` | 1 | 0.000001 | 剋:kpc |
