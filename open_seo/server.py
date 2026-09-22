"""Open SEO MCP server.

Exposes SERP rank-tracking as MCP tools so Claude can manage SEO keyword
projects, run rank checks, and export reports directly.

Run with:
    python -m open_seo.server

Requires SERPAPI_API_KEY to be set to the company's SerpApi account key.
"""

import time

from mcp.server.fastmcp import FastMCP

from open_seo import link_building, storage
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


PROSPECT_STATUSES = {"found", "contacted", "replied", "published", "declined"}


def _project_domain(project_name):
    data = storage.load_data()
    if project_name not in data:
        raise ValueError(f"Project '{project_name}' not found")
    return data[project_name]["domain"]


def _get_prospect(project_name, prospect_url):
    prospects = storage.load_prospects()
    project_prospects = prospects.get(project_name, {})
    if prospect_url not in project_prospects:
        raise ValueError(f"Prospect '{prospect_url}' not found for project '{project_name}'")
    return prospects, project_prospects


@mcp.tool()
def find_link_opportunities(
    project_name: str,
    niche: str,
    opportunity_types: list[str] | None = None,
    num_results: int = 10,
    location: str = "United States",
) -> list[dict]:
    """Search for guest-post, resource-page, directory, and roundup link-building
    opportunities for a niche, and save new ones as prospects under a project.
    Nothing is contacted or submitted automatically — the results are for
    human review before any outreach.
    """
    _project_domain(project_name)  # validates the project exists

    found = link_building.find_link_prospects(
        niche, opportunity_types=opportunity_types, num_results=num_results, location=location
    )

    prospects = storage.load_prospects()
    project_prospects = prospects.setdefault(project_name, {})
    for p in found:
        if p["url"] not in project_prospects:
            project_prospects[p["url"]] = {
                **p,
                "status": "found",
                "emails": [],
                "has_contact_form": None,
                "notes": "",
                "found_at": storage.now_iso(),
            }
    storage.save_prospects(prospects)

    return list(project_prospects.values())


@mcp.tool()
def get_link_prospects(project_name: str, status: str | None = None) -> list[dict]:
    """List saved link-building prospects for a project, optionally filtered by status."""
    rows = list(storage.load_prospects().get(project_name, {}).values())
    if status:
        rows = [r for r in rows if r.get("status") == status]
    return rows


@mcp.tool()
def research_link_prospect_contact(project_name: str, prospect_url: str) -> dict:
    """Fetch a saved prospect's page and look for an email address or contact form."""
    prospects, project_prospects = _get_prospect(project_name, prospect_url)

    info = link_building.scrape_contact_info(prospect_url)
    project_prospects[prospect_url]["emails"] = info["emails"]
    project_prospects[prospect_url]["has_contact_form"] = info["has_contact_form"]
    storage.save_prospects(prospects)
    return project_prospects[prospect_url]


@mcp.tool()
def draft_link_outreach_email(
    project_name: str,
    prospect_url: str,
    client_name: str,
    sender_name: str,
    niche: str,
    contact_first_name: str | None = None,
) -> dict:
    """Draft a professional outreach email for a saved link prospect. Returns
    a subject/body pair for human review — nothing is sent from here."""
    client_domain = _project_domain(project_name)
    _, project_prospects = _get_prospect(project_name, prospect_url)
    prospect = project_prospects[prospect_url]

    return link_building.draft_outreach_email(
        site_name=prospect.get("title") or prospect_url,
        niche=niche,
        client_name=client_name,
        client_domain=client_domain,
        sender_name=sender_name,
        opportunity_type=prospect.get("opportunity_type", "guest_post"),
        contact_first_name=contact_first_name,
    )


@mcp.tool()
def update_link_prospect_status(
    project_name: str, prospect_url: str, status: str, notes: str = ""
) -> dict:
    """Update a link prospect's status (found, contacted, replied, published, declined)."""
    if status not in PROSPECT_STATUSES:
        raise ValueError(f"status must be one of {sorted(PROSPECT_STATUSES)}")

    prospects, project_prospects = _get_prospect(project_name, prospect_url)
    project_prospects[prospect_url]["status"] = status
    project_prospects[prospect_url]["notes"] = notes
    project_prospects[prospect_url][f"{status}_at"] = storage.now_iso()
    storage.save_prospects(prospects)
    return project_prospects[prospect_url]


@mcp.tool()
def verify_link_placement(project_name: str, prospect_url: str) -> dict:
    """Check whether a prospect page now actually links back to the project's
    domain, to verify a placed backlink went live. Marks the prospect
    'published' if found."""
    domain = _project_domain(project_name)
    prospects, project_prospects = _get_prospect(project_name, prospect_url)

    result = link_building.link_exists_on_page(prospect_url, domain)
    if result.get("linked"):
        project_prospects[prospect_url]["status"] = "published"
        project_prospects[prospect_url]["published_at"] = storage.now_iso()
        storage.save_prospects(prospects)

    return {**project_prospects[prospect_url], "live_check": result}


def main():
    mcp.run()


if __name__ == "__main__":
    main()
