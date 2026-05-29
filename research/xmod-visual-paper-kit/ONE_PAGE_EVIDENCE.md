# X-MoD One-Page Evidence

## Core Idea

X-MoD treats explainability as a routing property, not only as a post-hoc explanation. A router assigns weights to explicit drives, and each expert reads the partial state relevant to its drive.

The four drives are:

- Safety
- Legality
- Comfort
- Efficiency

## What Was Tested

The central test asks whether the safety gate activates on safety-relevant events and stays low on non-events. This makes the explainability claim falsifiable: a gate that does not align with event labels should not be treated as semantically grounded.

## Main Result

| Metric | Value |
| --- | ---: |
| Samples | 11,500 |
| Primary run | `ce_align_safety_all` |
| Safety gate/event correlation | 0.8035 |
| Safety gate mean on event | 0.6541 |
| Safety gate mean on non-event | 0.0367 |
| Router accuracy | 0.7616 |
| Mean latency | 1.5435 ms |

Visuals:

- [Safety Gate Alignment](assets/gate_alignment.svg)
- [Negative-Control Comparison](assets/negative_control_comparison.svg)
- [Primary Run Drive Weights](assets/drive_weight_summary.svg)

## Why The Negative Controls Matter

The controls show that low action error or low latency alone does not prove explainable routing. In the primary comparison:

- `ce_align_all` has low action MSE but safety correlation is near zero.
- `bce_all` has weak positive safety correlation and worse action MSE.
- `ce_align_safety_all` produces strong safety alignment while keeping low latency.

This supports the narrower claim: under the included offline protocol, the safety-aware setting produces a gate that is quantitatively aligned with safety events.

## Regeneration Boundary

The plots are regenerated from a sanitized aggregate CSV included in this kit.
They do not require the raw CARLA workspace, local logs, checkpoints, or private
notes.

## Current Boundary

This is research evidence for explainable routing under the included protocol. It is not a real-world deployment claim, not external benchmark dominance, and not proof that all four drives are equally validated.
