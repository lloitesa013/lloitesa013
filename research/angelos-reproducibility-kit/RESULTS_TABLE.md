# Frozen-Anchor Results

Each row summarizes 40 matched seeds from the protocol-frozen paper table.

## Main Results

| Scenario | Method | Collision | Intervention | Near-miss | RLV | Latency ms | Route m |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `ped_surprise` | SC | 0.000 | 0.0175 | 0.0021 | 0.00077 | 0.0757 | 55.66 |
| `ped_surprise` | safety baseline | 0.000 | 0.0213 | 0.0034 | 0.00000 | 3.2542 | 3.64 |
| `ped_surprise` | align baseline | 0.400 | 0.0212 | 0.0028 | 0.00000 | 3.2161 | 8.55 |
| `merge_cutin` | SC | 0.000 | 0.0387 | 0.0062 | 0.00000 | 0.0702 | 145.55 |
| `merge_cutin` | safety baseline | 0.000 | 0.0405 | 0.0062 | 0.00000 | 2.1729 | 145.55 |
| `merge_cutin` | align baseline | 0.000 | 0.0368 | 0.0048 | 0.00000 | 2.2088 | 145.55 |

RLV means red-light violation rate.

## How To Read It

- Pedestrian surprise: SC preserved zero collisions and traveled farther than the stored baselines, but it still has a non-zero red-light violation rate and a minority near-zero-route issue in the validation discussion.
- Merge/cut-in: SC matched route distance with both baselines, preserved zero collision and zero red-light violation behavior, and kept much lower final-judgment latency.
- Across both anchors, the most consistent quantitative advantage is latency.

## Reproduction Boundary

The raw scripts and CARLA environment are not included in this public kit. This table is a sanitized evidence surface extracted from the private paper/source workspace.

