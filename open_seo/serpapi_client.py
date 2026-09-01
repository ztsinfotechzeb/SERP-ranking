"""Thin client around SerpApi's Google search endpoint.

Credentials always come from the SERPAPI_API_KEY environment variable, which
must be set to the company's own SerpApi account key. No key is ever
hardcoded in source, and personal/individual keys should not be used here.
"""

import os

import requests

SERPAPI_URL = "https://serpapi.com/search"


class SerpApiKeyMissing(RuntimeError):
    pass


def _api_key():
    key = os.environ.get("SERPAPI_API_KEY", "").strip()
    if not key:
        raise SerpApiKeyMissing(
            "SERPAPI_API_KEY is not set. Configure the company SerpApi "
            "account key as an environment variable before running Open SEO "
            "(see README.md). Do not hardcode or use a personal key."
        )
    return key


def search_keyword(keyword, domain, location="United States", num_results=100):
    """Return (rank, url) for the first result whose link contains `domain`,
    or (None, None) if the domain isn't found in the top `num_results`.
    """
    params = {
        "q": keyword,
        "location": location,
        "api_key": _api_key(),
        "num": num_results,
    }
    response = requests.get(SERPAPI_URL, params=params, timeout=30)
    response.raise_for_status()
    results = response.json().get("organic_results", [])

    for idx, result in enumerate(results, 1):
        if domain.lower() in result.get("link", "").lower():
            return idx, result["link"]

    return None, None
