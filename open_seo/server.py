"""Open SEO MCP server.

Exposes SERP rank-tracking as MCP tools so Claude can manage SEO keyword
projects, run rank checks, and export reports directly.

Run with:
    python -m open_seo.server

Requires SERPAPI_API_KEY to be set to the company's SerpApi account key.
"""

import time

from mcp.server.fastmcp import FastMCP

from open_seo import storage
from open_seo.serpapi_client import search_keyword

mcp = FastMCP("open-seo")


@mcp.tool()
def add_project(name: str, domain: str, keywords: list[str]) -> dict:
    """Create a new SEO tracking project for a domain with a starting list of keywords."""
    if not name or not domain or not keywords:
        raise ValueError("name, domain, and at least one keyword are required")

    data = storage.load_data()
    if name in data:
        raise ValueError(f"Project '{name}' already exists")

    data[name] = {
        "domain": domain,
        "keywords": [{"keyword": kw, "current_rank": None} for kw in keywords],
        "created_at": storage.now_iso(),
    }
    storage.save_data(data)
    return {"project": name, "domain": domain, "keyword_count": len(keywords)}


@mcp.tool()
def list_projects() -> list[dict]:
    """List all tracked SEO projects with their domain and keyword count."""
    data = storage.load_data()
    return [
        {"project": name, "domain": p["domain"], "keyword_count": len(p["keywords"])}
        for name, p in data.items()
    ]


@mcp.tool()
def track_rankings(project_name: str, location: str = "United States") -> dict:
    """Query current SERP rankings for every keyword in a project via SerpApi."""
    data = storage.load_data()
    if project_name not in data:
        raise ValueError(f"Project '{project_name}' not found")

    project = data[project_name]
    domain = project["domain"]

    for kw_data in project["keywords"]:
        rank, url = search_keyword(kw_data["keyword"], domain, location=location)
        kw_data["previous_rank"] = kw_data.get("current_rank")
        kw_data["current_rank"] = rank
        kw_data["url"] = url
        kw_data["timestamp"] = storage.now_iso()
        time.sleep(1)  # be polite to the SerpApi rate limits

    storage.save_data(data)
    return get_rankings(project_name)


@mcp.tool()
def get_rankings(project_name: str) -> dict:
    """Return the last-known rankings for every keyword in a project."""
    data = storage.load_data()
    if project_name not in data:
        raise ValueError(f"Project '{project_name}' not found")

    project = data[project_name]
    rows = []
    for kw in project["keywords"]:
        rank = kw.get("current_rank")
        status = "TOP 10" if isinstance(rank, int) and rank <= 10 else (
            "OTHER" if isinstance(rank, int) else "NOT RANKED"
        )
        rows.append(
            {
                "keyword": kw["keyword"],
                "rank": rank,
                "previous_rank": kw.get("previous_rank"),
                "status": status,
                "url": kw.get("url"),
                "updated_at": kw.get("timestamp"),
            }
        )

    return {"project": project_name, "domain": project["domain"], "keywords": rows}


@mcp.tool()
def export_rankings_csv(project_name: str | None = None) -> str:
    """Export rankings to a CSV file and return its path. Omit project_name to export all projects."""
    data = storage.load_data()
    if project_name and project_name not in data:
        raise ValueError(f"Project '{project_name}' not found")
    return storage.export_csv(data, project_name)


@mcp.tool()
def delete_project(project_name: str) -> dict:
    """Delete a tracked SEO project and its stored ranking history."""
    data = storage.load_data()
    if project_name not in data:
        raise ValueError(f"Project '{project_name}' not found")

    del data[project_name]
    storage.save_data(data)
    return {"deleted": project_name}


def main():
    mcp.run()


if __name__ == "__main__":
    main()
