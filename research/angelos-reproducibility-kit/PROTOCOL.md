# Angelos Protocol Summary

Angelos Protocol is a local CARLA closed-loop benchmark framing for top-level judgment layers. It is designed to separate raw route completion from pedestrian-priority behavior, legality, contact severity, and final judgment latency.

## Scenario 1: `ped_surprise`

Anchor: `v10`, 40 matched seeds.

Interpretation: pedestrian-priority behavior.

Primary metrics:

- collision count
- intervention rate
- near-miss rate
- critical-event rate
- red-light violation rate
- latency mean
- route distance
- pedestrian-priority stop/brake indicators

Reading rule: a conservative pedestrian response may sacrifice progress, but it must be separated from accidental mobility freeze. Route distance is interpreted together with contact severity and pedestrian-priority indicators.

## Scenario 2: `merge_cutin`

Anchor: `v11`, 40 matched seeds.

Interpretation: mobility-preserving scenario behavior.

Primary metrics:

- collision count
- red-light violation rate
- intervention rate
- near-miss rate
- critical-event rate
- latency mean
- route distance

Reading rule: route-completion parity is required. A system cannot claim success in this scenario by freezing or giving up progress.

## Protocol Freeze Rule

The public evidence anchor is fixed to `v10` for pedestrian surprise and `v11` for merge/cut-in. Later runs such as `v12`, `v13`, `v14`, `v16ped`, and `v16` are used only to expose failure modes or protocol extensions.

