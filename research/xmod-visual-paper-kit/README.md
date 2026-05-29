# X-MoD Visual Paper Kit

Status: public research kit v1.

X-MoD is an explainable routing architecture for autonomous-driving decisions. It routes candidate action behavior through four explicit drives: safety, legality, comfort, and efficiency.

This kit is not the full raw CARLA workspace. It is a reviewer-facing visual packet that explains the core architecture, the primary gate-event alignment result, the negative-control pattern, and the current limitations.

## What To Read First

1. [One-Page Evidence](ONE_PAGE_EVIDENCE.md)
2. [Four-Drive Routing Diagram](assets/xmod_architecture.svg)
3. [Gate Alignment Plot](assets/gate_alignment.svg)
4. [Limitations And Non-Claims](LIMITATIONS_AND_NON_CLAIMS.md)

## Primary Evidence Snapshot

| Run | Samples | Action MSE | Router Acc | Latency ms | Safety Corr |
| --- | ---: | ---: | ---: | ---: | ---: |
| `ce_align_all` | 11,500 | 0.0205 | 0.7698 | 1.6240 | -0.0301 |
| `bce_all` | 11,500 | 0.2908 | 0.5642 | 1.5708 | 0.2392 |
| `ce_align_safety_all` | 11,500 | 0.0379 | 0.7616 | 1.5435 | 0.8035 |

Primary result: `ce_align_safety_all` is the H3 evidence run. Safety gate activation separates event and non-event regions: 0.6541 vs 0.0367.

## Source Boundary

Original PDFs, local scripts, CARLA logs, generated files, and private notes remain outside this public kit. This folder only contains sanitized summaries, diagrams, and result excerpts.

## Completion Signal

This kit is complete when a reviewer can understand the four-drive routing idea, the safety gate alignment evidence, the negative-control meaning, and the public claim boundary without opening the raw workspace.

