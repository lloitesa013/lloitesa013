"""Validate the public X-MoD drive-alignment boundary matrix."""

from __future__ import annotations

import csv
import json
from pathlib import Path


KIT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = KIT_ROOT / "data" / "drive_alignment_status.csv"
REQUIRED_DRIVES = {"Safety", "Legality", "Comfort", "Efficiency"}


def load_rows():
    with DATA_PATH.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def require(condition, message):
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def validate():
    rows = load_rows()
    require(rows, "drive_alignment_status.csv is empty")
    by_drive = {row["drive"]: row for row in rows}
    require(set(by_drive) == REQUIRED_DRIVES, f"drive set mismatch: {sorted(by_drive)}")

    safety = by_drive["Safety"]
    require(safety["status"] == "measured", "Safety must be marked measured")
    require(
        "gate_safety_event_corr" in safety["current_metric"],
        "Safety row must name the measured correlation metric",
    )
    require(
        "included offline protocol" in safety["public_claim_boundary"],
        "Safety row must keep the public boundary scoped",
    )

    pending = ["Legality", "Comfort", "Efficiency"]
    for drive in pending:
        row = by_drive[drive]
        require(row["status"] == "pending", f"{drive} must remain pending")
        require(
            "descriptive router weight only" == row["evidence_type"],
            f"{drive} must not be framed as event-aligned yet",
        )
        require(
            row["public_claim_boundary"].lower().startswith("no "),
            f"{drive} must state a non-claim boundary",
        )

    return {
        "status": "PASS",
        "measured_drives": ["Safety"],
        "pending_drives": pending,
        "row_count": len(rows),
    }


def main():
    print(json.dumps(validate(), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
