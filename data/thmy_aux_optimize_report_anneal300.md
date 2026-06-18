# THMY auxiliary-code optimization report

- rounds: 300
- seed: 20260621
- candidate_limit: 96
- char_limit: all
- best_round: 284
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
| 1 | 284 | 7484.232 | 7424 | 78 | 4 | 0 | 2034 | `quick=4 slot=2567 overflow=40319 phrase=421 key_load=0.00295394 finger_load=8.87198e-05 hand_load=9.37727e-05` |
| 2 | 256 | 7493.733 | 7424 | 78 | 4 | 0 | 2035 | `quick=4 slot=2537 overflow=38846 phrase=422 key_load=0.00296676 finger_load=8.99811e-05 hand_load=9.52564e-05` |
| 3 | 281 | 7493.869 | 7425 | 77 | 4 | 0 | 2062 | `quick=4 slot=2480 overflow=38271 phrase=438 key_load=0.0030444 finger_load=8.47759e-05 hand_load=8.96528e-05` |
| 4 | 280 | 7496.891 | 7424 | 78 | 4 | 0 | 2035 | `quick=4 slot=2621 overflow=37979 phrase=434 key_load=0.00308099 finger_load=8.88772e-05 hand_load=9.87034e-05` |
| 5 | 254 | 7498.449 | 7425 | 77 | 4 | 0 | 2037 | `quick=4 slot=2583 overflow=36882 phrase=410 key_load=0.00310158 finger_load=8.80237e-05 hand_load=9.46707e-05` |
| 6 | 290 | 7504.050 | 7424 | 78 | 4 | 0 | 2035 | `quick=4 slot=2551 overflow=40894 phrase=412 key_load=0.00298374 finger_load=8.91971e-05 hand_load=8.87694e-05` |
| 7 | 295 | 7504.375 | 7424 | 78 | 4 | 0 | 2035 | `quick=4 slot=2543 overflow=38646 phrase=421 key_load=0.00294083 finger_load=8.79694e-05 hand_load=9.37602e-05` |
| 8 | 253 | 7508.916 | 7424 | 78 | 4 | 0 | 2039 | `quick=4 slot=2494 overflow=37859 phrase=421 key_load=0.00292296 finger_load=8.80413e-05 hand_load=8.95247e-05` |
| 9 | 274 | 7509.097 | 7425 | 77 | 4 | 0 | 2059 | `quick=4 slot=2485 overflow=37100 phrase=396 key_load=0.00299897 finger_load=9.01615e-05 hand_load=9.31657e-05` |
| 10 | 300 | 7511.860 | 7425 | 77 | 4 | 0 | 2072 | `quick=4 slot=2466 overflow=39136 phrase=417 key_load=0.00308501 finger_load=8.72631e-05 hand_load=9.08839e-05` |

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
