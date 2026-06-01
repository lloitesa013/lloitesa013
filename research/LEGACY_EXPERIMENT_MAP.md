# Legacy Experiment Map

The original CARLA workspace contains many numbered run scripts. They are
private provenance, not the public reproduction interface.

## How To Read The Legacy Line

| Private lineage | Public meaning |
| --- | --- |
| Early `run_v4` - `run_v9` scripts | development and signal-search history |
| `run_v10_sequence.ps1` | `ped_surprise/v10` frozen anchor |
| `run_v11_sequence.ps1` | `merge_cutin/v11` frozen anchor |
| `run_v12` - `run_v14` pedestrian variants | failure analysis and protocol-extension context |
| `run_v15` - `run_v16` merge variants | merge-signal refinement context |
| boost/sweep scripts | private research acceleration, not public claims |

## Public Interface

Use the public validators and aggregate packets instead of the raw scripts:

```powershell
python research\xmod-visual-paper-kit\scripts\validate_drive_alignment.py
python research\angelos-reproducibility-kit\scripts\verify_protocol_packet.py
```

## Non-Claim

This map does not claim that the private script sequence is clean, reusable, or
complete. It only explains how the public research kits relate to the private
experiment history.
