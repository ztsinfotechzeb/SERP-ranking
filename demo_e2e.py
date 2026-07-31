#!/usr/bin/env python3
"""End-to-end demo for SERP Rank Tracker (uses mocked SerpAPI responses)."""

import json
import os
import shutil
import sys
from unittest.mock import MagicMock, patch

# Use isolated data folder for demo
DEMO_DATA = "tracking_data_demo"
os.environ.setdefault("DEMO_MODE", "1")

# Load app from README.md (the repo's single source file)
import types
from pathlib import Path

app = types.ModuleType("serp_app")
exec(compile(Path("README.md").read_text(), "README.md", "exec"), app.__dict__)

app.DATA_FOLDER = DEMO_DATA
app.RESULTS_FILE = f"{DEMO_DATA}/rankings.json"
app.CSV_FILE = f"{DEMO_DATA}/rankings.csv"


def mock_serp_response(keyword, domain):
    """Return a fake SerpAPI organic_results payload."""
    return {
        "organic_results": [
            {"link": "https://competitor.com/page", "title": "Competitor"},
            {"link": f"https://www.{domain}/blog/{keyword.replace(' ', '-')}", "title": domain},
            {"link": "https://another-site.org/", "title": "Other"},
        ]
    }


def run_demo():
    if os.path.exists(DEMO_DATA):
        shutil.rmtree(DEMO_DATA)

    mock_response = MagicMock()
    mock_response.json.return_value = mock_serp_response("python tutorial", "example.com")

    with patch.object(app.requests, "get", return_value=mock_response):
        app.create_data_folder()
        data = {}

        # Add project
        data["Acme SEO"] = {
            "domain": "example.com",
            "keywords": [
                {"keyword": "python tutorial", "current_rank": None},
                {"keyword": "web development", "current_rank": None},
            ],
            "created_at": "2026-07-31T08:00:00",
        }
        app.save_data(data)

        # Track rankings (core feature)
        project = data["Acme SEO"]
        for kw_data in project["keywords"]:
            rank, url = app.search_keyword(kw_data["keyword"], project["domain"])
            kw_data["current_rank"] = rank
            kw_data["url"] = url
        app.save_data(data)

        # Export CSV
        import csv

        with open(app.CSV_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Project", "Keyword", "Rank", "Status"])
            for project_name, proj in data.items():
                for kw in proj["keywords"]:
                    rank = kw.get("current_rank", "Not Ranked")
                    status = "TOP 10" if isinstance(rank, int) and rank <= 10 else "Other"
                    writer.writerow([project_name, kw["keyword"], rank, status])

    # Verify outputs
    with open(app.RESULTS_FILE) as f:
        saved = json.load(f)

    assert "Acme SEO" in saved
    assert saved["Acme SEO"]["keywords"][0]["current_rank"] == 2
    assert os.path.exists(app.CSV_FILE)

    print("E2E demo passed!")
    print(f"  Project: Acme SEO")
    print(f"  Domain: example.com")
    print(f"  Keyword 'python tutorial' rank: #{saved['Acme SEO']['keywords'][0]['current_rank']}")
    print(f"  JSON: {app.RESULTS_FILE}")
    print(f"  CSV:  {app.CSV_FILE}")
    return 0


if __name__ == "__main__":
    sys.exit(run_demo())
