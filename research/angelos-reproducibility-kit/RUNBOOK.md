# Angelos Public Packet Runbook

This runbook explains how to use the public reproducibility kit without exposing the mixed raw CARLA workspace.

## Quick Verification

Run the public packet validator:

```powershell
python research\angelos-reproducibility-kit\scripts\verify_protocol_packet.py
```

Expected result:

```json
{
  "packet_id": "angelos-public-reproducibility-kit-v1",
  "scenario_count": 2,
  "row_count": 6,
  "status": "PASS"
}
```

## What The Validator Checks

- Frozen anchors are fixed to `ped_surprise/v10` and `merge_cutin/v11`.
- Each frozen anchor has 40 seeds.
- Required metric columns are present and numeric.
- Each scenario includes an `SC` row.
- Claim boundary text is present for deployment, universal-claim, and CARLA-scope limits.
- Scenario schematics referenced by the manifest exist and are sanitized SVG files.

## What This Does Not Do

- It does not run CARLA.
- It does not run private scenario scripts.
- It does not read raw logs, videos, caches, checkpoints, or local environment folders.
- It does not turn local CARLA evidence into road-deployment evidence.

## Full Reproduction Requirements

A future standalone reproduction package should add sanitized scenario scripts, seed lists, metric definitions, environment setup, validation logs, and failure-analysis records. Until then, this public kit should be read as protocol-frozen evidence plus a packet consistency check.
