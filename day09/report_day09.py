# ...existing code...
"""
Generate submission report from day09/subjects.txt

- Parses plain text (tab-separated) lines like:
  id<TAB>state<TAB>title<TAB><TAB>timestamp
- Extracts assignment and student from "... by <student>" titles.
- Optionally accepts a CSV of deadlines (assignment,deadline) to flag late submissions.
- Prints missing / late lists and a per-assignment summary, and saves CSVs to day09/.
"""
from __future__ import annotations

import argparse
import os
import re
from pathlib import Path
from typing import Dict, Optional, Union

import pandas as pd


# Resolve paths relative to this script's directory
SCRIPT_DIR = Path(__file__).resolve().parent

ISO_TS_RE = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z")


def resolve_path(p: Union[str, Path]) -> Path:
    """Resolve a path relative to the script directory when not absolute."""
    p = Path(p)
    return p if p.is_absolute() else (SCRIPT_DIR / p)


def read_subjects_txt(path: Union[str, Path]) -> pd.DataFrame:
    """
    Read plain text subjects file and return a DataFrame with columns:
    post_id, state, title, submission_raw (may be empty).
    """
    path = resolve_path(path)
    rows = []
    with open(path, "r", encoding="utf-8") as fh:
        for raw in fh:
            line = raw.rstrip("\n")
            if not line.strip():
                continue
            parts = line.split("\t")
            # remove empty columns produced by double tabs while preserving content words
            parts = [p for p in parts if p != ""]
            if len(parts) < 3:
                continue
            post_id = parts[0].strip()
            state = parts[1].strip()
            # if last part looks like ISO timestamp, treat it as submission_raw
            submission_raw = None
            if ISO_TS_RE.match(parts[-1].strip()):
                submission_raw = parts[-1].strip()
                title_parts = parts[2:-1]
            else:
                title_parts = parts[2:]
            title = "\t".join(title_parts).strip()
            rows.append({"post_id": post_id, "state": state, "title": title, "submission_raw": submission_raw})
    return pd.DataFrame(rows)


def split_title(title: str) -> Dict[str, Optional[str]]:
    """
    Split a title like "Day08 by Shoshana Sernik" into {'assignment': 'Day08', 'student': 'Shoshana Sernik'}.
    If no 'by' found, assignment=title and student is None.
    """
    m = re.match(r"^(?P<assignment>.+?)\s+by\s+(?P<student>.+)$", title, flags=re.I)
    if m:
        return {"assignment": m.group("assignment").strip(), "student": m.group("student").strip()}
    return {"assignment": title.strip(), "student": None}


def parse_submissions(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add parsed columns: assignment, student, submission_ts (pd.Timestamp or NaT).
    """
    df2 = df.copy()
    split = df2["title"].apply(split_title).apply(pd.Series)
    df2 = pd.concat([df2, split], axis=1)
    df2["submission_ts"] = pd.to_datetime(df2["submission_raw"], errors="coerce")
    return df2


def load_deadlines_csv(path: Union[str, Path]) -> pd.DataFrame:
    """
    Load deadlines CSV with columns: assignment,deadline (ISO format).
    Returns DataFrame with assignment and deadline_ts.
    """
    path = resolve_path(path)
    d = pd.read_csv(path)
    if "assignment" not in d.columns or "deadline" not in d.columns:
        raise ValueError("Deadlines CSV must contain 'assignment' and 'deadline' columns")
    d = d[["assignment", "deadline"]].copy()
    d["deadline_ts"] = pd.to_datetime(d["deadline"], errors="coerce")
    return d[["assignment", "deadline_ts"]]


def attach_deadlines(df: pd.DataFrame, deadlines: Optional[pd.DataFrame]) -> pd.DataFrame:
    """
    Merge per-assignment deadlines (if provided) into df as deadline_ts.
    """
    df2 = df.copy()
    if deadlines is None:
        df2["deadline_ts"] = pd.NaT
        return df2
    merged = df2.merge(deadlines, on="assignment", how="left")
    merged["deadline_ts"] = merged["deadline_ts"].fillna(pd.NaT)
    return merged


def compute_status(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute status column:
      - 'missing' if no submission_ts
      - 'submitted (deadline unknown)' if submission exists but no deadline
      - 'on-time' if submission_ts <= deadline_ts
      - 'late' if submission_ts > deadline_ts
    """
    df2 = df.copy()

    def _status(row):
        if pd.isna(row["submission_ts"]):
            return "missing"
        if pd.isna(row["deadline_ts"]):
            return "submitted (deadline unknown)"
        return "on-time" if row["submission_ts"] <= row["deadline_ts"] else "late"

    df2["status"] = df2.apply(_status, axis=1)
    return df2


def find_missing_submissions(df: pd.DataFrame) -> pd.DataFrame:
    return df[df["status"] == "missing"].copy()


def find_late_submissions(df: pd.DataFrame) -> pd.DataFrame:
    return df[df["status"] == "late"].copy()


def submission_summary(df: pd.DataFrame) -> pd.DataFrame:
    summary = df.groupby(["assignment", "status"]).size().unstack(fill_value=0).reset_index()
    return summary


def save_csv(df: pd.DataFrame, outpath: Union[str, Path]) -> None:
    outp = resolve_path(outpath)
    outp.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(outp, index=False)


def print_table(df: pd.DataFrame, title: Optional[str] = None, max_rows: int = 50) -> None:
    if title:
        print(f"\n=== {title} ===")
    if df.empty:
        print(" (no rows)")
        return
    print(df.head(max_rows).to_string(index=False))


def generate_report(
    txt_path: str = "day09/subjects.txt",
    deadlines_csv: Optional[str] = None,
    save_csvs: bool = True,
) -> None:
    """
    Orchestrate reading, parsing, status computation, printing and saving CSVs.
    """
    txt_path_resolved = resolve_path(txt_path)
    print(f"Reading subjects from: {txt_path_resolved}")
    df0 = read_subjects_txt(txt_path_resolved)
    print("\nDetected columns (parsed):")
    print(" - post_id\n - state\n - title\n - submission_raw")

    df_parsed = parse_submissions(df0)

    deadlines_df = None
    if deadlines_csv:
        deadlines_path_resolved = resolve_path(deadlines_csv)
        print(f"\nLoading deadlines from: {deadlines_path_resolved}")
        deadlines_df = load_deadlines_csv(deadlines_path_resolved)

    df_with_deadlines = attach_deadlines(df_parsed, deadlines_df)
    df_final = compute_status(df_with_deadlines)

    missing = find_missing_submissions(df_final)
    late = find_late_submissions(df_final)
    summary = submission_summary(df_final)

    print_table(missing[["post_id", "student", "assignment", "state"]], "Missing Submissions")
    print_table(late[["post_id", "student", "assignment", "submission_ts", "deadline_ts"]], "Late Submissions")
    print_table(summary, "Submission Summary (counts)")

    if save_csvs:
        base = SCRIPT_DIR 
        save_csv(df_final, base / "submissions_parsed.csv")
        save_csv(missing, base / "missing_submissions.csv")
        save_csv(late, base / "late_submissions.csv")
        save_csv(summary, base / "submission_summary.csv")
        print(f"\nCSV reports saved to {base}/")


def main() -> None:
    p = argparse.ArgumentParser(description="Generate submission report from subjects.txt")
    p.add_argument("--txt", "-i", default="day09/subjects.txt", help="Input text file")
    p.add_argument("--deadlines", "-d", default=None, help="Optional CSV of deadlines (assignment,deadline)")
    p.add_argument("--no-save", dest="save", action="store_false", help="Do not write CSVs")
    args = p.parse_args()
    generate_report(txt_path=args.txt, deadlines_csv=args.deadlines, save_csvs=args.save)


if __name__ == "__main__":
    main()
