# THMY sound+aux optimization report

This is an experimental search report. It does not change the formal THMY sound-code tables by itself.

- rounds: 100
- seed: 20260618
- candidate_limit: 96
- char_limit: all
- baseline_score: 17557.338
- best_round: 1
- best_score: 17557.338
- score_delta: 0.000 (0.00%)

## Best sound-code changes

- changed_initials: 0
- changed_finals: 0
- changed_zero_initials: 0
- initials: `-`
- finals: `-`
- zero_initials: `-`

## Best auxiliary parameters

- quick=4 slot=3661 overflow=50578 phrase=1274 key_load=0.00171194 finger_load=0.000160311 hand_load=0.000574478

## Baseline metrics

- one_letter: 7425
- two_letter: 77
- collisions: 1999
- phrase_collisions: 13
- same_finger_stretches: 15
- max_candidates: 4
- groups_over_quick: 0
- weighted_average: `big_same_finger=0.001 distance=8.165 hand_imbalance=1.033 repeat_key=0.020 same_finger=0.032 same_hand=0.394`
- weighted_aux_added: `big_same_finger=0.000 distance=4.234 hand_imbalance=1.000 repeat_key=0.000 same_finger=0.000 same_hand=0.185`

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

## Top trials

| Rank | Round | Score | Initials | Finals | Zero | One | Two | Max | Over | Collisions | Weighted average |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | 1 | 17557.338 | 0 | 0 | 0 | 7425 | 77 | 4 | 0 | 1999 | `big_same_finger=0.001 distance=8.165 hand_imbalance=1.033 repeat_key=0.020 same_finger=0.032 same_hand=0.394` |
| 2 | 4 | 17831.461 | 0 | 0 | 0 | 7425 | 77 | 4 | 0 | 2274 | `big_same_finger=0.001 distance=8.169 hand_imbalance=1.032 repeat_key=0.020 same_finger=0.032 same_hand=0.393` |
| 3 | 3 | 17946.614 | 0 | 0 | 0 | 7425 | 77 | 4 | 0 | 2385 | `big_same_finger=0.001 distance=8.171 hand_imbalance=1.031 repeat_key=0.020 same_finger=0.032 same_hand=0.392` |
| 4 | 70 | 18429.317 | 0 | 1 | 2 | 7423 | 79 | 4 | 0 | 3024 | `big_same_finger=0.001 distance=8.290 hand_imbalance=1.000 repeat_key=0.020 same_finger=0.032 same_hand=0.358` |
| 5 | 31 | 19386.204 | 2 | 3 | 2 | 7278 | 224 | 4 | 0 | 3340 | `big_same_finger=0.004 distance=7.623 hand_imbalance=1.000 repeat_key=0.016 same_finger=0.037 same_hand=0.345` |
| 6 | 64 | 19474.814 | 4 | 3 | 1 | 7425 | 77 | 4 | 0 | 2816 | `big_same_finger=0.001 distance=7.698 hand_imbalance=1.081 repeat_key=0.020 same_finger=0.033 same_hand=0.678` |
| 7 | 11 | 19567.005 | 6 | 7 | 2 | 7420 | 82 | 4 | 0 | 2472 | `big_same_finger=0.004 distance=7.968 hand_imbalance=1.001 repeat_key=0.027 same_finger=0.055 same_hand=0.395` |
| 8 | 43 | 19710.220 | 2 | 11 | 0 | 7425 | 77 | 4 | 0 | 2496 | `big_same_finger=0.015 distance=7.150 hand_imbalance=1.003 repeat_key=0.019 same_finger=0.071 same_hand=0.352` |
| 9 | 59 | 19742.898 | 0 | 18 | 0 | 7412 | 90 | 4 | 0 | 2797 | `big_same_finger=0.005 distance=8.520 hand_imbalance=1.020 repeat_key=0.017 same_finger=0.038 same_hand=0.436` |
| 10 | 26 | 20099.286 | 2 | 8 | 0 | 7438 | 64 | 4 | 0 | 2692 | `big_same_finger=0.004 distance=8.052 hand_imbalance=1.006 repeat_key=0.028 same_finger=0.059 same_hand=0.427` |

## Candidate group distribution

| Candidate count | Groups |
| ---: | ---: |
| 1 | 4144 |
| 2 | 1076 |
| 3 | 190 |
| 4 | 181 |

## Same-Finger Stretch Pairs

| Pair | Count | Weighted average | Examples |
| --- | ---: | ---: | --- |
| `px` | 8 | 0.000861 | 派:pxz 排:pxm 拍:pxw 牌:pxv 徘:pxb 湃:pxn 俳:pxs 哌:pxr |
| `ky` | 6 | 0.000379 | 卡:kyg 咖:kyr 喀:kyc 咯:kyl 咔:kyw 胩:kys |
| `kp` | 1 | 0.000001 | 剋:kpr |
