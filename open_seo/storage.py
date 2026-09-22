"""Persistence for tracked SEO projects and keyword rankings."""

import csv
import json
import os
from datetime import datetime, timezone

DATA_FOLDER = os.environ.get("OPEN_SEO_DATA_DIR", "tracking_data")
RESULTS_FILE = os.path.join(DATA_FOLDER, "rankings.json")
CSV_FILE = os.path.join(DATA_FOLDER, "rankings.csv")
PROSPECTS_FILE = os.path.join(DATA_FOLDER, "link_prospects.json")


def _ensure_data_folder():
    os.makedirs(DATA_FOLDER, exist_ok=True)


def load_data():
    _ensure_data_folder()
    if os.path.exists(RESULTS_FILE):
        with open(RESULTS_FILE, "r") as f:
            return json.load(f)
    return {}


def save_data(data):
    _ensure_data_folder()
    with open(RESULTS_FILE, "w") as f:
        json.dump(data, f, indent=2)


def now_iso():
    return datetime.now(timezone.utc).isoformat()


def load_prospects():
    """Load link-building prospects, keyed by project name then prospect URL."""
    _ensure_data_folder()
    if os.path.exists(PROSPECTS_FILE):
        with open(PROSPECTS_FILE, "r") as f:
            return json.load(f)
    return {}


def save_prospects(data):
    _ensure_data_folder()
    with open(PROSPECTS_FILE, "w") as f:
        json.dump(data, f, indent=2)


def export_csv(data, project_name=None):
    """Write rankings to CSV_FILE, optionally restricted to one project."""
    _ensure_data_folder()
    projects = {project_name: data[project_name]} if project_name else data

    with open(CSV_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Project", "Keyword", "Rank", "Status", "URL"])
        for name, project in projects.items():
            for kw in project["keywords"]:
                rank = kw.get("current_rank", "Not Ranked")
                status = "TOP 10" if isinstance(rank, int) and rank <= 10 else "Other"
                writer.writerow([name, kw["keyword"], rank, status, kw.get("url", "")])

    return CSV_FILE
