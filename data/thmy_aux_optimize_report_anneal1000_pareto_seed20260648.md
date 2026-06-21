# THMY auxiliary-code optimization report

- rounds: 1000
- seed: 20260648
- candidate_limit: 96
- char_limit: all
- best_round: 1
- best_score: 7351.872

## Best parameters

| Parameter | Value |
| --- | ---: |
| quick_select_candidates | 4 |
| same_code_slot_weight | 3091 |
| same_code_overflow_weight | 118229 |
| phrase_code_collision_weight | 1348 |
| key_load_weight | 0.00713805 |
| finger_load_weight | 0.00001184 |
| hand_load_weight | 0.00001364 |

## Best metrics

- one_letter: 7423
- two_letter: 79
- collisions: 2102
- phrase_collisions: 27
- same_finger_stretches: 15
- weighted_same_finger_stretches: 0.001240
- max_candidates: 4
- groups_over_quick: 0
- overflow_candidates: 0
- weighted_average: `big_same_finger=0.001 distance=8.303 hand_imbalance=1.004 repeat_key=0.020 same_finger=0.032 same_hand=0.245`
- weighted_aux_added: `big_same_finger=0.000 distance=4.372 hand_imbalance=1.000 repeat_key=0.000 same_finger=0.000 same_hand=0.036`

## Candidate group distribution

| Candidate count | Groups |
| ---: | ---: |
| 1 | 3960 |
| 2 | 1143 |
| 3 | 196 |
| 4 | 189 |

## Top trials

| Rank | Round | Score | One-letter | Two-letter | Max candidates | Groups > quick | Collisions | Parameters |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | 1 | 7351.872 | 7423 | 79 | 4 | 0 | 2102 | `quick=4 slot=3091 overflow=118229 phrase=1348 key_load=0.00713805 finger_load=1.18365e-05 hand_load=1.36433e-05` |
| 2 | 933 | 7387.726 | 7423 | 79 | 4 | 0 | 2099 | `quick=4 slot=2930 overflow=18253 phrase=212 key_load=0.00671975 finger_load=2.17029e-05 hand_load=1.65944e-05` |
| 3 | 901 | 7391.244 | 7424 | 78 | 4 | 0 | 2100 | `quick=4 slot=2866 overflow=17344 phrase=196 key_load=0.00681684 finger_load=2.1146e-05 hand_load=1.75866e-05` |
| 4 | 910 | 7392.108 | 7423 | 79 | 4 | 0 | 2098 | `quick=4 slot=3059 overflow=18896 phrase=202 key_load=0.00706028 finger_load=2.23443e-05 hand_load=1.68311e-05` |
| 5 | 824 | 7394.109 | 7424 | 78 | 4 | 0 | 2101 | `quick=4 slot=2949 overflow=16136 phrase=196 key_load=0.00689335 finger_load=2.19023e-05 hand_load=1.56421e-05` |
| 6 | 894 | 7395.282 | 7424 | 78 | 4 | 0 | 2100 | `quick=4 slot=2871 overflow=16542 phrase=210 key_load=0.00694195 finger_load=2.18469e-05 hand_load=1.62495e-05` |
| 7 | 887 | 7397.193 | 7424 | 78 | 4 | 0 | 2106 | `quick=4 slot=2939 overflow=16490 phrase=171 key_load=0.00712496 finger_load=2.21893e-05 hand_load=1.57547e-05` |
| 8 | 929 | 7397.758 | 7422 | 80 | 4 | 0 | 2095 | `quick=4 slot=3126 overflow=19385 phrase=210 key_load=0.00709095 finger_load=2.24102e-05 hand_load=1.72345e-05` |
| 9 | 888 | 7397.826 | 7424 | 78 | 4 | 0 | 2105 | `quick=4 slot=2961 overflow=16211 phrase=206 key_load=0.00707633 finger_load=2.189e-05 hand_load=1.60486e-05` |
| 10 | 899 | 7397.877 | 7423 | 79 | 4 | 0 | 2099 | `quick=4 slot=2926 overflow=16789 phrase=200 key_load=0.00660978 finger_load=2.16205e-05 hand_load=1.70003e-05` |

## Pareto Candidates

A candidate is kept when no archived candidate is no worse across quick-select overflow, two-letter count, collisions, phrase collisions, same-finger stretches, added same-hand rate, and added travel distance. Score is used only for ordering and tie-breaking.

| Rank | Round | Score | One-letter | Two-letter | Collisions | Phrase collisions | Stretches | Weighted stretches | Max candidates | Groups > quick | Overflow | Added same-hand | Added distance | Parameters |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | 1 | 7351.872 | 7423 | 79 | 2102 | 27 | 15 | 0.001240 | 4 | 0 | 0 | 0.036 | 4.372 | `quick=4 slot=3091 overflow=118229 phrase=1348 key_load=0.00713805 finger_load=1.18365e-05 hand_load=1.36433e-05` |
| 2 | 933 | 7387.726 | 7423 | 79 | 2099 | 25 | 15 | 0.001240 | 4 | 0 | 0 | 0.075 | 4.177 | `quick=4 slot=2930 overflow=18253 phrase=212 key_load=0.00671975 finger_load=2.17029e-05 hand_load=1.65944e-05` |
| 3 | 901 | 7391.244 | 7424 | 78 | 2100 | 25 | 15 | 0.001240 | 4 | 0 | 0 | 0.076 | 4.184 | `quick=4 slot=2866 overflow=17344 phrase=196 key_load=0.00681684 finger_load=2.1146e-05 hand_load=1.75866e-05` |
| 4 | 910 | 7392.108 | 7423 | 79 | 2098 | 29 | 15 | 0.001240 | 4 | 0 | 0 | 0.076 | 4.172 | `quick=4 slot=3059 overflow=18896 phrase=202 key_load=0.00706028 finger_load=2.23443e-05 hand_load=1.68311e-05` |
| 5 | 824 | 7394.109 | 7424 | 78 | 2101 | 25 | 15 | 0.001240 | 4 | 0 | 0 | 0.076 | 4.187 | `quick=4 slot=2949 overflow=16136 phrase=196 key_load=0.00689335 finger_load=2.19023e-05 hand_load=1.56421e-05` |
| 6 | 894 | 7395.282 | 7424 | 78 | 2100 | 27 | 15 | 0.001240 | 4 | 0 | 0 | 0.076 | 4.187 | `quick=4 slot=2871 overflow=16542 phrase=210 key_load=0.00694195 finger_load=2.18469e-05 hand_load=1.62495e-05` |
| 7 | 887 | 7397.193 | 7424 | 78 | 2106 | 30 | 15 | 0.001240 | 4 | 0 | 0 | 0.076 | 4.176 | `quick=4 slot=2939 overflow=16490 phrase=171 key_load=0.00712496 finger_load=2.21893e-05 hand_load=1.57547e-05` |
| 8 | 929 | 7397.758 | 7422 | 80 | 2095 | 29 | 15 | 0.001240 | 4 | 0 | 0 | 0.076 | 4.174 | `quick=4 slot=3126 overflow=19385 phrase=210 key_load=0.00709095 finger_load=2.24102e-05 hand_load=1.72345e-05` |
| 9 | 888 | 7397.826 | 7424 | 78 | 2105 | 29 | 15 | 0.001240 | 4 | 0 | 0 | 0.076 | 4.179 | `quick=4 slot=2961 overflow=16211 phrase=206 key_load=0.00707633 finger_load=2.189e-05 hand_load=1.60486e-05` |
| 10 | 853 | 7398.149 | 7424 | 78 | 2099 | 26 | 15 | 0.001240 | 4 | 0 | 0 | 0.076 | 4.192 | `quick=4 slot=2934 overflow=15999 phrase=174 key_load=0.00684119 finger_load=2.16942e-05 hand_load=1.51262e-05` |
| 11 | 859 | 7400.554 | 7424 | 78 | 2102 | 25 | 15 | 0.001240 | 4 | 0 | 0 | 0.076 | 4.193 | `quick=4 slot=2884 overflow=15488 phrase=190 key_load=0.00688916 finger_load=2.14133e-05 hand_load=1.61873e-05` |
| 12 | 982 | 7400.786 | 7424 | 78 | 2102 | 25 | 15 | 0.001240 | 4 | 0 | 0 | 0.076 | 4.194 | `quick=4 slot=2868 overflow=17890 phrase=200 key_load=0.00687879 finger_load=2.18127e-05 hand_load=1.71375e-05` |
| 13 | 644 | 7401.082 | 7421 | 81 | 2089 | 26 | 15 | 0.001240 | 4 | 0 | 0 | 0.076 | 4.180 | `quick=4 slot=3260 overflow=11164 phrase=238 key_load=0.0067595 finger_load=2.18948e-05 hand_load=1.41399e-05` |
| 14 | 972 | 7401.680 | 7424 | 78 | 2102 | 25 | 15 | 0.001240 | 4 | 0 | 0 | 0.076 | 4.195 | `quick=4 slot=2934 overflow=18778 phrase=230 key_load=0.00690081 finger_load=2.13093e-05 hand_load=1.60329e-05` |
| 15 | 941 | 7401.785 | 7424 | 78 | 2103 | 25 | 15 | 0.001240 | 4 | 0 | 0 | 0.075 | 4.195 | `quick=4 slot=2806 overflow=17828 phrase=224 key_load=0.00659689 finger_load=2.14244e-05 hand_load=1.70811e-05` |
| 16 | 960 | 7402.206 | 7424 | 78 | 2103 | 25 | 15 | 0.001240 | 4 | 0 | 0 | 0.075 | 4.196 | `quick=4 slot=2836 overflow=18005 phrase=188 key_load=0.00668602 finger_load=2.14617e-05 hand_load=1.69918e-05` |
| 17 | 999 | 7402.342 | 7424 | 78 | 2101 | 25 | 15 | 0.001240 | 4 | 0 | 0 | 0.075 | 4.198 | `quick=4 slot=2874 overflow=17712 phrase=224 key_load=0.00675036 finger_load=2.1477e-05 hand_load=1.654e-05` |
| 18 | 991 | 7403.101 | 7424 | 78 | 2101 | 25 | 15 | 0.001240 | 4 | 0 | 0 | 0.076 | 4.197 | `quick=4 slot=2908 overflow=18018 phrase=202 key_load=0.00675227 finger_load=2.14898e-05 hand_load=1.65832e-05` |
| 19 | 905 | 7403.339 | 7421 | 81 | 2093 | 26 | 15 | 0.001240 | 4 | 0 | 0 | 0.075 | 4.181 | `quick=4 slot=3066 overflow=17281 phrase=189 key_load=0.00681525 finger_load=2.1955e-05 hand_load=1.75405e-05` |
| 20 | 889 | 7403.893 | 7424 | 78 | 2102 | 26 | 15 | 0.001240 | 4 | 0 | 0 | 0.075 | 4.197 | `quick=4 slot=2929 overflow=16245 phrase=198 key_load=0.00685683 finger_load=2.12134e-05 hand_load=1.55961e-05` |
| 21 | 959 | 7404.197 | 7424 | 78 | 2102 | 25 | 15 | 0.001240 | 4 | 0 | 0 | 0.075 | 4.199 | `quick=4 slot=2864 overflow=18706 phrase=196 key_load=0.0067571 finger_load=2.15539e-05 hand_load=1.53706e-05` |
| 22 | 462 | 7404.465 | 7421 | 81 | 2099 | 28 | 15 | 0.001240 | 4 | 0 | 0 | 0.041 | 4.384 | `quick=4 slot=3557 overflow=34970 phrase=249 key_load=0.00766943 finger_load=1.32645e-05 hand_load=1.56161e-05` |
| 23 | 964 | 7406.920 | 7424 | 78 | 2104 | 29 | 15 | 0.001240 | 4 | 0 | 0 | 0.076 | 4.194 | `quick=4 slot=2870 overflow=19098 phrase=197 key_load=0.00664192 finger_load=2.09793e-05 hand_load=1.61266e-05` |
| 24 | 921 | 7408.341 | 7421 | 81 | 2095 | 29 | 15 | 0.001240 | 4 | 0 | 0 | 0.076 | 4.180 | `quick=4 slot=3094 overflow=19698 phrase=195 key_load=0.00685052 finger_load=2.19518e-05 hand_load=1.64483e-05` |
| 25 | 952 | 7409.640 | 7424 | 78 | 2114 | 29 | 15 | 0.001240 | 4 | 0 | 0 | 0.076 | 4.186 | `quick=4 slot=2843 overflow=17542 phrase=198 key_load=0.00686442 finger_load=2.15925e-05 hand_load=1.6553e-05` |
| 26 | 946 | 7410.209 | 7424 | 78 | 2120 | 29 | 15 | 0.001240 | 4 | 0 | 0 | 0.075 | 4.182 | `quick=4 slot=2774 overflow=18153 phrase=220 key_load=0.00677719 finger_load=2.17335e-05 hand_load=1.66081e-05` |
| 27 | 661 | 7410.907 | 7422 | 80 | 2095 | 25 | 15 | 0.001240 | 4 | 0 | 0 | 0.078 | 4.182 | `quick=4 slot=3424 overflow=11259 phrase=236 key_load=0.00793455 finger_load=2.4645e-05 hand_load=1.67786e-05` |
| 28 | 807 | 7411.240 | 7424 | 78 | 2116 | 25 | 15 | 0.001240 | 4 | 0 | 0 | 0.076 | 4.189 | `quick=4 slot=2678 overflow=15117 phrase=213 key_load=0.00692127 finger_load=2.20244e-05 hand_load=1.42522e-05` |
| 29 | 830 | 7411.892 | 7424 | 78 | 2112 | 29 | 15 | 0.001240 | 4 | 0 | 0 | 0.076 | 4.190 | `quick=4 slot=2828 overflow=16608 phrase=201 key_load=0.00664756 finger_load=2.25009e-05 hand_load=1.5712e-05` |
| 30 | 872 | 7411.989 | 7424 | 78 | 2099 | 25 | 15 | 0.001240 | 4 | 0 | 0 | 0.076 | 4.207 | `quick=4 slot=2952 overflow=16383 phrase=182 key_load=0.00704333 finger_load=2.26396e-05 hand_load=1.65606e-05` |
| 31 | 617 | 7413.159 | 7421 | 81 | 2094 | 25 | 15 | 0.001240 | 4 | 0 | 0 | 0.073 | 4.207 | `quick=4 slot=2756 overflow=12131 phrase=162 key_load=0.00539306 finger_load=1.52627e-05 hand_load=2.0722e-05` |
| 32 | 984 | 7413.238 | 7421 | 81 | 2097 | 25 | 15 | 0.001240 | 4 | 0 | 0 | 0.075 | 4.188 | `quick=4 slot=2953 overflow=17890 phrase=205 key_load=0.00658206 finger_load=2.15785e-05 hand_load=1.67796e-05` |
| 33 | 996 | 7413.761 | 7424 | 78 | 2101 | 25 | 15 | 0.001240 | 4 | 0 | 0 | 0.075 | 4.209 | `quick=4 slot=2926 overflow=18583 phrase=210 key_load=0.00691455 finger_load=2.16543e-05 hand_load=1.70916e-05` |
| 34 | 913 | 7414.096 | 7421 | 81 | 2094 | 25 | 15 | 0.001240 | 4 | 0 | 0 | 0.076 | 4.188 | `quick=4 slot=3172 overflow=19417 phrase=201 key_load=0.00706941 finger_load=2.19419e-05 hand_load=1.69394e-05` |
| 35 | 971 | 7414.280 | 7422 | 80 | 2098 | 26 | 15 | 0.001240 | 4 | 0 | 0 | 0.076 | 4.195 | `quick=4 slot=2971 overflow=17912 phrase=229 key_load=0.00670389 finger_load=2.13899e-05 hand_load=1.68021e-05` |
| 36 | 152 | 8003.737 | 7406 | 96 | 2716 | 7 | 15 | 0.001240 | 4 | 0 | 0 | 0.003 | 4.490 | `quick=4 slot=726 overflow=85100 phrase=808 key_load=0.00107071 finger_load=3.02868e-06 hand_load=2.04649e-06` |
| 37 | 74 | 8045.437 | 7425 | 77 | 2962 | 0 | 15 | 0.001240 | 4 | 0 | 0 | 0.020 | 4.342 | `quick=4 slot=427 overflow=30146 phrase=1303 key_load=0.00107071 finger_load=1.11135e-05 hand_load=1.50382e-05` |
| 38 | 564 | 8406.233 | 7281 | 221 | 1867 | 54 | 15 | 0.001240 | 4 | 0 | 0 | 0.107 | 4.071 | `quick=4 slot=3617 overflow=15609 phrase=191 key_load=0.00496937 finger_load=2.12614e-05 hand_load=3.80283e-05` |
| 39 | 113 | 11731.067 | 6822 | 680 | 1409 | 300 | 15 | 0.001240 | 3 | 0 | 0 | 0.058 | 4.229 | `quick=4 slot=2953 overflow=13246 phrase=0 key_load=0.00107689 finger_load=2.24648e-06 hand_load=2.5397e-05` |
| 40 | 95 | 7232320.567 | 7482 | 20 | 2326 | 16 | 15 | 0.001240 | 5 | 57 | 57 | 0.054 | 4.494 | `quick=4 slot=4327 overflow=10000 phrase=433 key_load=0.0194751 finger_load=1.77547e-06 hand_load=1.06322e-05` |

## Largest candidate groups

| Code | Chars | Weights |
| --- | --- | --- |
| `bne` | 毕璧妣珌 | `690, 258, 30, 4` |
| `bno` | 必裨荜馝 | `3672, 11, 5, 1` |
| `bny` | 币俾佖秕 | `2666, 110, 3, 2` |
| `fja` | 妇俘馥滏 | `211, 170, 24, 5` |
| `fjb` | 服俯黻苻 | `3361, 126, 29, 28` |
| `fjc` | 扶孵跗艴 | `833, 77, 13, 2` |
| `fjf` | 附甫茯绋 | `4846, 319, 8, 2` |
| `fjg` | 府缚蚨韨 | `1107, 233, 1, 1` |
| `fji` | 浮蝠怫垺 | `375, 56, 7, 1` |
| `fjk` | 符辐赙讣 | `675, 83, 4, 1` |
| `fjl` | 付拂郛稃 | `2603, 244, 24, 10` |
| `fjm` | 福傅绂匐 | `1378, 443, 16, 8` |
| `fjn` | 富袱榑菔 | `1296, 7, 7, 5` |
| `fjo` | 弗趺幞咐 | `799, 12, 3, 2` |
| `fjp` | 斧腐玞鲋 | `538, 218, 20, 5` |
| `fjq` | 副釜肤黼 | `3013, 598, 69, 41` |
| `fjr` | 父芙凫鄜 | `868, 594, 61, 40` |
| `fjs` | 负敷簠呋 | `4145, 587, 20, 7` |
| `fjv` | 幅辅蝮茀 | `657, 375, 11, 11` |
| `fjw` | 复赴祓宓 | `1786, 1308, 52, 14` |

## Same-Finger Stretch Pairs

Same-finger stretches count only different-key same-finger pairs with a Dvorak row gap >= 2. Repeated keys such as `uuu` and adjacent or diagonal-neighbor same-finger keys such as `ik`, `pi`, and `ki` are ignored.

| Pair | Count | Weighted average | Examples |
| --- | ---: | ---: | --- |
| `px` | 8 | 0.000861 | 派:pxz 排:pxw 拍:pxb 牌:pxm 徘:pxv 湃:pxf 俳:pxg 哌:pxl |
| `ky` | 6 | 0.000379 | 卡:kyf 咖:kyl 喀:kyg 咯:kyw 咔:kyr 胩:kyz |
| `kp` | 1 | 0.000001 | 剋:kpf |
