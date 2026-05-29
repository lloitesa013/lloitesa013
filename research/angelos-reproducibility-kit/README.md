# Angelos Reproducibility Kit

Status: public research kit v1.

Angelos OS / SynOptic Core is a top-level judgment layer above autonomous-driving policies. The layer separates policy output from final action by adding candidate evaluation, value arbitration, gating, and traceable explanation.

This kit is not the raw CARLA workspace. It is a scoped reproducibility packet for the protocol-frozen evidence anchors described in the paper draft.

## What To Read First

1. [Protocol Summary](PROTOCOL.md)
2. [Frozen-Anchor Results](RESULTS_TABLE.md)
3. [Limitations And Non-Claims](LIMITATIONS_AND_NON_CLAIMS.md)
4. [Pipeline Diagram](assets/angelos_pipeline.svg)
5. [Pedestrian Surprise Schematic](assets/scenario_ped_surprise.svg)
6. [Merge/Cut-In Schematic](assets/scenario_merge_cutin.svg)
7. [Reproduction Boundary](REPRODUCTION_BOUNDARY.md)
8. [Public Packet Runbook](RUNBOOK.md)

## Frozen Anchors

| Scenario | Anchor | Seeds | Reading |
| --- | --- | ---: | --- |
| `ped_surprise` | `v10` | 40 | pedestrian-priority behavior with mobility and legality caveats |
| `merge_cutin` | `v11` | 40 | mobility-preserving scenario behavior and route-completion parity |

Later variants are failure-analysis or protocol-extension evidence, not replacements for the frozen anchors.

## Source Boundary

Original PDFs, local scripts, CARLA logs, generated files, and private notes remain outside this public kit. This folder only contains sanitized protocol summaries, diagrams, result excerpts, and limitations.

## Minimal Runnable Check

This kit includes a public packet validator. It checks the sanitized manifest and
frozen-anchor result table without running CARLA or reading private local files.

```powershell
python research\angelos-reproducibility-kit\scripts\verify_protocol_packet.py
```

## Completion Signal

This kit is complete when a reviewer can understand the protocol, the two frozen scenario anchors, the primary result table, and the limitations without seeing the mixed raw CARLA workspace.
