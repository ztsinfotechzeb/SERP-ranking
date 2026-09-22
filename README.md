# Open SEO — Automating SEO Tasks with Claude MCP

Open SEO turns SERP (Search Engine Results Page) rank tracking into a set of
[MCP](https://modelcontextprotocol.io) tools, so Claude can create SEO
projects, check keyword rankings, and export reports on request — no manual
script running required.

Rankings are fetched from [SerpApi](https://serpapi.com), using the
**company's own SerpApi account only**. Never hardcode a key in source or use
a personal account key.

## Setup

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Configure the company SerpApi key as an environment variable (never in
   code, never committed):

   ```bash
   cp .env.example .env
   # edit .env and set SERPAPI_API_KEY to the company account key
   ```

3. Run the MCP server directly to verify it starts:

   ```bash
   python -m open_seo.server
   ```

## Connecting to Claude

### Claude Code

```bash
claude mcp add open-seo -- python -m open_seo.server
```

Set `SERPAPI_API_KEY` in the environment Claude Code runs in (e.g. export it
in your shell profile, or add it under `env` for the server in
`.claude/settings.json` / `.mcp.json`), pointing at the company account key.

### Claude Desktop

Add to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "open-seo": {
      "command": "python",
      "args": ["-m", "open_seo.server"],
      "env": {
        "SERPAPI_API_KEY": "<company account key>"
      }
    }
  }
}
```

## Available tools

| Tool | Description |
| --- | --- |
| `add_project(name, domain, keywords)` | Create a new SEO tracking project for a domain with a starting keyword list. |
| `list_projects()` | List all tracked projects with domain and keyword count. |
| `track_rankings(project_name, location="United States")` | Query current Google rankings for every keyword in a project via SerpApi. |
| `get_rankings(project_name)` | Return the last-known rankings for a project without re-querying SerpApi. |
| `export_rankings_csv(project_name=None)` | Export rankings to CSV (all projects, or one). Returns the file path. |
| `delete_project(project_name)` | Delete a project and its ranking history. |

### Link building

These tools help research and manage off-page link-building outreach for a
project. They **only research, draft, and track** — nothing is submitted,
posted, or emailed automatically. Mass, unreviewed link placement (auto
directory submissions, comment spam, PBNs) violates Google's link-spam
policy and risks a manual action, so every prospect and draft is meant for a
human to review before acting on it.

| Tool | Description |
| --- | --- |
| `find_link_opportunities(project_name, niche, opportunity_types=None, num_results=10, location="United States")` | Search for guest-post, resource-page, directory, and roundup opportunities for a niche via SerpApi, and save new ones as prospects. |
| `get_link_prospects(project_name, status=None)` | List saved prospects for a project, optionally filtered by status. |
| `research_link_prospect_contact(project_name, prospect_url)` | Fetch a prospect's page and look for a contact email or contact form. |
| `draft_link_outreach_email(project_name, prospect_url, client_name, sender_name, niche, contact_first_name=None)` | Draft a professional outreach email (subject + body) for a prospect, for human review. |
| `update_link_prospect_status(project_name, prospect_url, status, notes="")` | Update a prospect's status: `found`, `contacted`, `replied`, `published`, or `declined`. |
| `verify_link_placement(project_name, prospect_url)` | Fetch the prospect page and check whether it now actually links to the project's domain; marks it `published` if found. |

## Data storage

Project, ranking, and link-prospect data is stored locally as JSON/CSV under
`tracking_data/` (configurable via `OPEN_SEO_DATA_DIR`). This directory is
gitignored — it holds client keyword and outreach data, not code.

## Project layout

```
open_seo/
  server.py          # MCP server + tool definitions
  serpapi_client.py  # SerpApi request wrapper (company key via env var)
  storage.py          # JSON/CSV persistence for projects, rankings, and link prospects
  link_building.py    # Link prospecting, contact discovery, outreach drafting, verification
```
