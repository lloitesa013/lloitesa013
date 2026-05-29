"""Verify the public Angelos reproducibility packet.

This wrapper validates the sanitized packet itself. It does not install CARLA,
run scenario scripts, read raw logs, or access private files.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path


KIT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = KIT_ROOT / "data"
RESULTS_PATH = DATA_DIR / "frozen_anchor_results.csv"
MANIFEST_PATH = DATA_DIR / "protocol_manifest.json"


def load_manifest():
    with MANIFEST_PATH.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def load_results():
    with RESULTS_PATH.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def require(condition, message):
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def verify():
    manifest = load_manifest()
    rows = load_results()
    require(rows, "frozen_anchor_results.csv is empty")

    required_metrics = set(manifest["required_metrics"])
    missing_columns = required_metrics - set(rows[0])
    require(not missing_columns, f"missing metric columns: {sorted(missing_columns)}")

    rows_by_scenario = {}
    for row in rows:
        rows_by_scenario.setdefault(row["scenario"], []).append(row)
        for metric in required_metrics:
            float(row[metric])

    for scenario, spec in manifest["frozen_anchors"].items():
        scenario_rows = rows_by_scenario.get(scenario, [])
        require(scenario_rows, f"missing scenario rows for {scenario}")
        anchors = {row["anchor"] for row in scenario_rows}
        seeds = {int(row["seeds"]) for row in scenario_rows}
        methods = {row["method"] for row in scenario_rows}
        require(anchors == {spec["anchor"]}, f"{scenario} anchor mismatch: {anchors}")
        require(seeds == {int(spec["seeds"])}, f"{scenario} seed mismatch: {seeds}")
        require("SC" in methods, f"{scenario} missing SC method row")

    visuals = manifest.get("scenario_visuals", {})
    require(set(visuals) == set(manifest["frozen_anchors"]), "scenario visual set mismatch")
    kit_root = KIT_ROOT.resolve()
    for scenario, relative_path in visuals.items():
        require(str(relative_path).endswith(".svg"), f"{scenario} visual must be SVG")
        visual_path = (KIT_ROOT / relative_path).resolve()
        require(
            str(visual_path).startswith(str(kit_root)),
            f"{scenario} visual path escapes kit root",
        )
        require(visual_path.exists(), f"{scenario} visual missing: {relative_path}")

    boundary_text = " ".join(manifest.get("claim_boundary", [])).lower()
    require("deployment readiness" in boundary_text, "deployment boundary missing")
    require("universal" in boundary_text, "universal-claim boundary missing")
    require("carla" in boundary_text, "CARLA scope boundary missing")

    return {
        "packet_id": manifest["packet_id"],
        "scenario_count": len(manifest["frozen_anchors"]),
        "row_count": len(rows),
        "status": "PASS",
    }


def main():
    result = verify()
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
