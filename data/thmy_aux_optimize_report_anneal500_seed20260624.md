# THMY auxiliary-code optimization report

- rounds: 500
- seed: 20260624
- candidate_limit: 96
- char_limit: all
- best_round: 1
- best_score: 7484.232

## Best parameters

| Parameter | Value |
| --- | ---: |
| quick_select_candidates | 4 |
| same_code_slot_weight | 2567 |
| same_code_overflow_weight | 40319 |
| phrase_code_collision_weight | 421 |
| key_load_weight | 0.00295394 |
| finger_load_weight | 0.00008872 |
| hand_load_weight | 0.00009377 |

## Best metrics

- one_letter: 7424
- two_letter: 78
- collisions: 2034
- phrase_collisions: 18
- same_finger_stretches: 15
- weighted_same_finger_stretches: 0.001240
- max_candidates: 4
- groups_over_quick: 0
- overflow_candidates: 0
- weighted_average: `big_same_finger=0.001 distance=8.135 hand_imbalance=1.003 repeat_key=0.020 same_finger=0.032 same_hand=0.309`
- weighted_aux_added: `big_same_finger=0.000 distance=4.205 hand_imbalance=1.000 repeat_key=0.000 same_finger=0.000 same_hand=0.100`

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
| 1 | 1 | 7484.232 | 7424 | 78 | 4 | 0 | 2034 | `quick=4 slot=2567 overflow=40319 phrase=421 key_load=0.00295394 finger_load=8.87198e-05 hand_load=9.37727e-05` |
| 2 | 384 | 7501.293 | 7423 | 79 | 4 | 0 | 2029 | `quick=4 slot=3314 overflow=14509 phrase=385 key_load=0.00469406 finger_load=0.000105569 hand_load=0.000113927` |
| 3 | 340 | 7505.781 | 7423 | 79 | 4 | 0 | 2026 | `quick=4 slot=3291 overflow=13301 phrase=403 key_load=0.00470194 finger_load=0.000105935 hand_load=0.000111416` |
| 4 | 409 | 7508.094 | 7423 | 79 | 4 | 0 | 2027 | `quick=4 slot=3395 overflow=14646 phrase=357 key_load=0.00462292 finger_load=0.000104227 hand_load=0.000108631` |
| 5 | 421 | 7510.078 | 7423 | 79 | 4 | 0 | 2030 | `quick=4 slot=3294 overflow=14540 phrase=378 key_load=0.00449895 finger_load=0.000101759 hand_load=0.000105562` |
| 6 | 368 | 7517.593 | 7425 | 77 | 4 | 0 | 2046 | `quick=4 slot=3085 overflow=13201 phrase=392 key_load=0.00464839 finger_load=0.000106173 hand_load=0.000111332` |
| 7 | 247 | 7519.912 | 7423 | 79 | 4 | 0 | 2028 | `quick=4 slot=3471 overflow=12695 phrase=471 key_load=0.0050468 finger_load=0.000103454 hand_load=0.000114036` |
| 8 | 346 | 7519.988 | 7423 | 79 | 4 | 0 | 2026 | `quick=4 slot=3302 overflow=14783 phrase=445 key_load=0.00475309 finger_load=0.000106583 hand_load=0.000111964` |
| 9 | 341 | 7520.101 | 7424 | 78 | 4 | 0 | 2030 | `quick=4 slot=3186 overflow=13071 phrase=406 key_load=0.00463891 finger_load=0.000106279 hand_load=0.000115691` |
| 10 | 401 | 7521.448 | 7423 | 79 | 4 | 0 | 2026 | `quick=4 slot=3345 overflow=13443 phrase=404 key_load=0.00483235 finger_load=0.00010371 hand_load=0.000116054` |

## Largest candidate groups

| Code | Chars | Weights |
| --- | --- | --- |
| `fja` | 幅脯芣鲋 | `657, 48, 43, 5` |
| `fjb` | 福俘祓匐 | `1378, 170, 52, 8` |
| `fjc` | 符斧凫艴 | `675, 538, 61, 2` |
| `fjf` | 复甫幞讣 | `1786, 319, 3, 1` |
| `fjg` | 芙妇呋韨 | `594, 211, 7, 1` |
| `fjh` | 副辐馥赙 | `3013, 83, 24, 4` |
| `fji` | 扶孚麸琈 | `833, 77, 23, 1` |
| `fjk` | 浮蝠玞跗 | `375, 56, 20, 13` |
| `fjl` | 付缚鄜郛 | `2603, 233, 40, 24` |
| `fjm` | 赴父苻茀 | `1308, 868, 28, 11` |
| `fjo` | 伏孵榑菔 | `697, 77, 7, 5` |
| `fjp` | 腐罘袱洑 | `218, 8, 7, 7` |
| `fjq` | 弗敷涪簠 | `799, 587, 42, 20` |
| `fjr` | 附俯茯绋 | `4846, 126, 8, 2` |
| `fjs` | 负趺滏咐 | `4145, 12, 5, 2` |
| `fjt` | 富拂稃蚨 | `1296, 244, 10, 1` |
| `fjv` | 服覆黻蝮 | `3361, 290, 29, 11` |
| `fjw` | 夫辅绂宓 | `1472, 375, 16, 14` |
| `fjx` | 腹阜怫垺 | `542, 50, 7, 1` |
| `fjz` | 府傅桴驸 | `1107, 443, 31, 10` |

## Same-Finger Stretch Pairs

Same-finger stretches count only different-key same-finger pairs with a Dvorak row gap >= 2. Repeated keys such as `uuu` and adjacent or diagonal-neighbor same-finger keys such as `ik`, `pi`, and `ki` are ignored.

| Pair | Count | Weighted average | Examples |
| --- | ---: | ---: | --- |
| `px` | 8 | 0.000861 | 派:pxw 排:pxv 拍:pxm 牌:pxb 徘:pxz 湃:pxs 俳:pxf 哌:pxh |
| `ky` | 6 | 0.000379 | 卡:kyh 咖:kyf 喀:kyr 咯:kyv 咔:kyl 胩:kyg |
| `kp` | 1 | 0.000001 | 剋:kpf |
