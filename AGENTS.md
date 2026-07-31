# SERP Rank Tracker

## Cursor Cloud specific instructions

This repository is a **single-file Python CLI** — the application code lives in `README.md` (not documentation). There are no web servers, databases, or Docker services.

### Running the app

```bash
pip install -r requirements.txt
python3 README.md
```

### SerpAPI key (required for live rank tracking)

Set `API_KEY` on line 8 of `README.md` before using menu option **2. Track Rankings**. Without a key, add/view/export/delete still work; tracking calls SerpAPI over HTTPS and will error.

### Verification

```bash
python3 demo_e2e.py
```

This runs an automated end-to-end check with mocked SerpAPI responses (add project → track → export CSV).

### Data files

Runtime data is written to `tracking_data/` (`rankings.json`, `rankings.csv`). Safe to delete for a clean slate.

### Lint / tests

No formal linter or test suite is configured. Use `demo_e2e.py` as the smoke test.
