#!/usr/bin/env python3
"""
to-planner.py — Convert dependency-mapper markdown task table to CSV

Reads a tab-separated or pipe-delimited markdown task table from stdin (or a file)
and outputs a Microsoft Project-compatible CSV to stdout.

Usage:
    python to-planner.py input.md > tasks.csv
    cat input.md | python to-planner.py > tasks.csv

Expected input format (markdown table):
    | ID | Task | Phase | Duration | Predecessors | Resource | Notes |
    |----|------|-------|----------|-------------|----------|-------|
    | 1  | Kick-off | Planning | 1d | | Delivery Lead | |

Output: Microsoft Project CSV with columns:
    ID, Name, Outline Level, Duration, Predecessors, Resource Names, Notes, Milestone
"""

import sys
import csv
import re
import io


PHASE_OUTLINE_LEVEL = 1
TASK_OUTLINE_LEVEL = 2
SUBTASK_OUTLINE_LEVEL = 3


def parse_markdown_table(lines):
    """Parse a markdown pipe table and return list of dicts."""
    rows = []
    headers = []

    for line in lines:
        line = line.strip()
        if not line.startswith("|"):
            continue
        # Skip separator rows (---|---|---)
        if re.match(r"^\|[\s\-:|]+\|", line):
            continue

        cells = [c.strip() for c in line.strip("|").split("|")]

        if not headers:
            headers = [h.lower().replace(" ", "_") for h in cells]
            continue

        if len(cells) < len(headers):
            cells.extend([""] * (len(headers) - len(cells)))

        rows.append(dict(zip(headers, cells)))

    return rows


def detect_phase_changes(rows):
    """
    Assign outline levels: rows with no predecessors and no duration
    that appear to be phase headers get level 1; others get level 2.
    If a 'phase' column exists, group by phase and emit phase rows.
    """
    result = []
    current_phase = None

    for row in rows:
        phase = row.get("phase", "").strip()
        task_id = row.get("id", "").strip()
        name = row.get("task", row.get("name", "")).strip()
        duration = row.get("duration", "").strip()
        predecessors = row.get("predecessors", "").strip()
        resource = row.get("resource", row.get("resource_names", "")).strip()
        notes = row.get("notes", "").strip()
        milestone = "Yes" if (not duration or duration == "0d") and predecessors else "No"

        # Emit a phase header row when the phase changes
        if phase and phase != current_phase:
            current_phase = phase
            result.append({
                "id": "",
                "name": phase,
                "outline_level": PHASE_OUTLINE_LEVEL,
                "duration": "",
                "predecessors": "",
                "resource_names": "",
                "notes": "",
                "milestone": "No",
            })

        result.append({
            "id": task_id,
            "name": name,
            "outline_level": TASK_OUTLINE_LEVEL,
            "duration": duration or "1d",
            "predecessors": predecessors,
            "resource_names": resource,
            "notes": notes,
            "milestone": milestone,
        })

    return result


def write_project_csv(rows, output):
    """Write Microsoft Project-compatible CSV."""
    fieldnames = [
        "ID", "Name", "Outline Level", "Duration",
        "Predecessors", "Resource Names", "Notes", "Milestone"
    ]
    writer = csv.DictWriter(output, fieldnames=fieldnames, lineterminator="\n")
    writer.writeheader()

    for row in rows:
        writer.writerow({
            "ID": row.get("id", ""),
            "Name": row.get("name", ""),
            "Outline Level": row.get("outline_level", TASK_OUTLINE_LEVEL),
            "Duration": row.get("duration", ""),
            "Predecessors": row.get("predecessors", ""),
            "Resource Names": row.get("resource_names", ""),
            "Notes": row.get("notes", ""),
            "Milestone": row.get("milestone", "No"),
        })


def main():
    # Read from file argument or stdin
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            lines = f.readlines()
    else:
        lines = sys.stdin.readlines()

    rows = parse_markdown_table(lines)

    if not rows:
        print("Error: No markdown table found in input.", file=sys.stderr)
        print("Expected a pipe-delimited table with a header row.", file=sys.stderr)
        sys.exit(1)

    enriched = detect_phase_changes(rows)

    output = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="")
    write_project_csv(enriched, output)
    output.flush()


if __name__ == "__main__":
    main()
