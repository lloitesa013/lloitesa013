"""Render X-MoD public visual kit SVGs from sanitized aggregate CSV data."""

from __future__ import annotations

import csv
from html import escape
from pathlib import Path


KIT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = KIT_ROOT / "data" / "xmod_paper_results_summary.csv"
DRIVE_STATUS_PATH = KIT_ROOT / "data" / "drive_alignment_status.csv"
ASSET_DIR = KIT_ROOT / "assets"
PRIMARY_RUN = "ce_align_safety_all"


def read_rows():
    with DATA_PATH.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    required = {"ce_align_all", "bce_all", PRIMARY_RUN}
    found = {row["run"] for row in rows}
    missing = required - found
    if missing:
        raise SystemExit(f"Missing required runs: {sorted(missing)}")
    return rows


def read_drive_status_rows():
    with DRIVE_STATUS_PATH.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    return rows


def number(row, key):
    return float(row[key])


def svg_page(title, subtitle, body, width=900, height=520):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="{title}">
  <defs>
    <style>
      .bg{{fill:#f7f9fb}}.axis{{stroke:#263238;stroke-width:2}}.grid{{stroke:#d7dde2;stroke-width:1}}.bar1{{fill:#176b87}}.bar2{{fill:#7c4d1d}}.bar3{{fill:#2f6f4e}}.ok{{fill:#176b87}}.pending{{fill:#a35b00}}.card{{fill:#fff;stroke:#d7dde2;stroke-width:1}}.txt{{font-family:Inter,Segoe UI,Arial,sans-serif;fill:#172026}}.muted{{fill:#5f6b73}}.title{{font-size:28px;font-weight:700}}.label{{font-size:15px;font-weight:700}}.small{{font-size:13px}}
    </style>
  </defs>
  <rect class="bg" width="{width}" height="{height}"/>
  <text class="txt title" x="60" y="54">{title}</text>
  <text class="txt muted small" x="60" y="82">{subtitle}</text>
{body}
</svg>
"""


def render_gate_alignment(primary):
    event = number(primary, "gate_safety_mean_event")
    non_event = number(primary, "gate_safety_mean_non_event")
    corr = number(primary, "gate_safety_event_corr")
    axis = """
  <line class="axis" x1="110" y1="420" x2="760" y2="420"/>
  <line class="axis" x1="110" y1="120" x2="110" y2="420"/>
  <line class="grid" x1="110" y1="360" x2="760" y2="360"/>
  <line class="grid" x1="110" y1="300" x2="760" y2="300"/>
  <line class="grid" x1="110" y1="240" x2="760" y2="240"/>
  <line class="grid" x1="110" y1="180" x2="760" y2="180"/>
  <text class="txt small" x="70" y="425">0.0</text>
  <text class="txt small" x="70" y="365">0.2</text>
  <text class="txt small" x="70" y="305">0.4</text>
  <text class="txt small" x="70" y="245">0.6</text>
  <text class="txt small" x="70" y="185">0.8</text>"""
    event_height = event * 300
    non_event_height = non_event * 300
    body = axis + f"""
  <rect class="bar1" x="210" y="{420 - event_height:.1f}" width="150" height="{event_height:.1f}"/>
  <rect class="bar2" x="510" y="{420 - non_event_height:.1f}" width="150" height="{non_event_height:.1f}"/>
  <text class="txt label" x="214" y="{410 - event_height:.1f}">{event:.4f}</text>
  <text class="txt label" x="518" y="{405 - non_event_height:.1f}">{non_event:.4f}</text>
  <text class="txt label" x="202" y="455">Event</text>
  <text class="txt label" x="490" y="455">Non-event</text>
  <text class="txt muted small" x="60" y="490">gate_safety_event_corr = {corr:.4f}. Scoped alignment evidence under the included offline protocol.</text>"""
    return svg_page(
        "Safety Gate Alignment",
        f"Primary run: {PRIMARY_RUN}, {int(number(primary, 'samples')):,} samples",
        body,
    )


def render_negative_controls(rows):
    max_corr = max(abs(number(row, "gate_safety_event_corr")) for row in rows)
    max_corr = max(max_corr, 0.01)
    x_positions = [150, 370, 590]
    labels = ["CE align", "BCE", "Safety align"]
    bars = []
    zero_y = 360
    max_bar_height = 220
    for index, row in enumerate(rows):
        corr = number(row, "gate_safety_event_corr")
        height = abs(corr) / max_corr * max_bar_height
        y = zero_y - height if corr >= 0 else zero_y
        klass = f"bar{index + 1}"
        bars.append(f'  <rect class="{klass}" x="{x_positions[index]}" y="{y:.1f}" width="140" height="{height:.1f}"/>')
        label_y = y - 10 if corr >= 0 else zero_y + height + 22
        if corr < 0:
            label_y = min(label_y, 412)
        bars.append(f'  <text class="txt label" x="{x_positions[index]}" y="{label_y:.1f}">{corr:.4f}</text>')
        bars.append(f'  <text class="txt label" x="{x_positions[index] - 10}" y="455">{labels[index]}</text>')
    body = """
  <line class="axis" x1="100" y1="360" x2="780" y2="360"/>
  <line class="axis" x1="100" y1="120" x2="100" y2="430"/>
  <line class="grid" x1="100" y1="250" x2="780" y2="250"/>
  <line class="grid" x1="100" y1="420" x2="780" y2="420"/>
  <text class="txt small" x="60" y="365">0.0</text>
  <text class="txt small" x="58" y="255">high</text>
  <text class="txt small" x="54" y="425">negative</text>
""" + "\n".join(bars) + """
  <text class="txt muted small" x="60" y="490">Controls show that low action error alone does not establish semantic gate-event alignment.</text>"""
    return svg_page(
        "Negative-Control Comparison",
        "Safety gate/event correlation across paper runs",
        body,
    )


def render_drive_weights(primary):
    drives = [
        ("Safety", number(primary, "gate_mean_safety"), "bar1"),
        ("Legality", number(primary, "gate_mean_legality"), "bar2"),
        ("Comfort", number(primary, "gate_mean_comfort"), "bar3"),
        ("Efficiency", number(primary, "gate_mean_efficiency"), "bar1"),
    ]
    x_positions = [130, 310, 490, 670]
    bars = []
    for index, (label, value, klass) in enumerate(drives):
        height = value * 300
        x = x_positions[index]
        bars.append(f'  <rect class="{klass}" x="{x}" y="{420 - height:.1f}" width="110" height="{height:.1f}"/>')
        bars.append(f'  <text class="txt label" x="{x}" y="{410 - height:.1f}">{value:.4f}</text>')
        bars.append(f'  <text class="txt label" x="{x - 8}" y="455">{label}</text>')
    body = """
  <line class="axis" x1="100" y1="420" x2="820" y2="420"/>
  <line class="axis" x1="100" y1="120" x2="100" y2="420"/>
  <line class="grid" x1="100" y1="320" x2="820" y2="320"/>
  <line class="grid" x1="100" y1="220" x2="820" y2="220"/>
  <text class="txt small" x="64" y="425">0.0</text>
  <text class="txt small" x="64" y="325">0.3</text>
  <text class="txt small" x="64" y="225">0.6</text>
""" + "\n".join(bars) + """
  <text class="txt muted small" x="60" y="490">Mean router weights are descriptive. Only safety has event-alignment evidence in this kit.</text>"""
    return svg_page(
        "Primary Run Drive Weights",
        f"Mean router weights for {PRIMARY_RUN}",
        body,
    )


def render_drive_alignment_status(rows):
    y_positions = [138, 218, 298, 378]
    body = """
  <rect class="card" x="60" y="105" width="780" height="330" rx="8"/>
  <text class="txt label" x="86" y="130">Drive</text>
  <text class="txt label" x="205" y="130">Status</text>
  <text class="txt label" x="330" y="130">Evidence</text>
  <text class="txt label" x="560" y="130">Current Metric</text>
  <line class="grid" x1="80" y1="148" x2="820" y2="148"/>
"""
    for index, row in enumerate(rows):
        y = y_positions[index]
        status = row["status"].lower()
        klass = "ok" if status == "measured" else "pending"
        body += f"""
  <text class="txt label" x="86" y="{y}">{escape(row['drive'])}</text>
  <rect class="{klass}" x="205" y="{y - 18}" width="88" height="26" rx="13"/>
  <text class="txt small" x="218" y="{y}">{escape(row['status'].upper())}</text>
  <text class="txt small" x="330" y="{y}">{escape(row['evidence_type'])}</text>
  <text class="txt small" x="560" y="{y}">{escape(row['current_metric'])}</text>
  <text class="txt muted small" x="330" y="{y + 22}">{escape(row['public_claim_boundary'])}</text>
  <line class="grid" x1="80" y1="{y + 38}" x2="820" y2="{y + 38}"/>
"""
    body += """
  <text class="txt muted small" x="60" y="485">Boundary: one measured drive, three pending drive-specific event protocols.</text>"""
    return svg_page(
        "Drive Alignment Status",
        "Measured vs pending evidence across X-MoD drives",
        body,
        width=900,
        height=520,
    )


def main():
    rows = read_rows()
    drive_status_rows = read_drive_status_rows()
    rows_by_name = {row["run"]: row for row in rows}
    ordered = [rows_by_name["ce_align_all"], rows_by_name["bce_all"], rows_by_name[PRIMARY_RUN]]
    ASSET_DIR.mkdir(parents=True, exist_ok=True)
    outputs = {
        "gate_alignment.svg": render_gate_alignment(rows_by_name[PRIMARY_RUN]),
        "negative_control_comparison.svg": render_negative_controls(ordered),
        "drive_weight_summary.svg": render_drive_weights(rows_by_name[PRIMARY_RUN]),
        "drive_alignment_status.svg": render_drive_alignment_status(drive_status_rows),
    }
    for filename, payload in outputs.items():
        path = ASSET_DIR / filename
        path.write_text(payload, encoding="utf-8")
        print(path.relative_to(KIT_ROOT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
