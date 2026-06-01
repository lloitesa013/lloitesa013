# CARLA Source Boundary

The autonomous-driving research line comes from a private CARLA workspace. This
public profile does not publish that raw workspace.

## What Is Public Here

- Sanitized aggregate result tables.
- Public-safe SVG diagrams.
- Protocol summaries and frozen-anchor result excerpts.
- Validators that run only on the sanitized packet files in this repository.
- Limitations, pending evidence, and non-claims.

## What Stays Private

- Raw CARLA workspace files.
- Raw logs, generated TeX artifacts, local handoff notes, and runbooks.
- Checkpoints, datasets, and local environment folders.
- Large raw scenario videos.
- Numbered legacy execution scripts.
- Admissions or personal-context material.

## Why

The raw workspace mixes research code, generated files, private provenance, and
large local artifacts. Publishing it as-is would make the evidence harder to
review and easier to overread.

The public kits are intentionally smaller: each one should make one scoped
claim boundary, one result surface, and one reproducibility check easy to audit.

## Current Public Validators

```powershell
python research\xmod-visual-paper-kit\scripts\validate_drive_alignment.py
python research\xmod-visual-paper-kit\scripts\render_visuals.py
python research\angelos-reproducibility-kit\scripts\verify_protocol_packet.py
```

These commands do not read the private CARLA workspace.
