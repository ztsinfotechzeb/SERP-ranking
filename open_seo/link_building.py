"""Link-building prospecting, contact discovery, outreach drafting, and
backlink verification for off-page SEO.

This module deliberately stops short of submitting or posting anything
anywhere. Google's link-spam guidance treats mass, unreviewed link
placement (auto-submitted directories, comment spam, PBNs) as manipulative
and a manual-action risk, so every prospect and outreach draft here is
meant for a human to review before it's sent or acted on.
"""

import re

import requests

from open_seo.serpapi_client import search_web

OPPORTUNITY_QUERIES = {
    "guest_post": '"{niche}" ("write for us" OR "guest post guidelines" OR "contribute to us")',
    "resource_page": '"{niche}" ("resources" OR "useful links") intitle:resources',
    "directory": '"{niche}" ("submit your site" OR "add a listing" OR "submit a resource")',
    "roundup": '"{niche}" ("best tools" OR "best blogs") intitle:best',
}

EMAIL_RE = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
MAILTO_RE = re.compile(r"mailto:([\w.+-]+@[\w-]+\.[\w.-]+)", re.I)

REQUEST_HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; OpenSEO-LinkResearch/1.0)"}


def find_link_prospects(niche, opportunity_types=None, num_results=10, location="United States"):
    """Search for real, human-reviewable link-building opportunities for a niche."""
    types = opportunity_types or list(OPPORTUNITY_QUERIES)
    unknown = [t for t in types if t not in OPPORTUNITY_QUERIES]
    if unknown:
        raise ValueError(f"Unknown opportunity type(s): {', '.join(unknown)}")

    prospects = []
    seen_urls = set()
    for opp_type in types:
        query = OPPORTUNITY_QUERIES[opp_type].format(niche=niche)
        for result in search_web(query, location=location, num_results=num_results):
            url = result["url"]
            if not url or url in seen_urls:
                continue
            seen_urls.add(url)
            prospects.append({**result, "opportunity_type": opp_type})

    return prospects


def scrape_contact_info(url, timeout=15):
    """Fetch a prospect page and pull out an email address / contact-form signal.

    This is a plain HTTP GET, not a JS-rendering browser, so sites that only
    expose contact details via client-side scripts won't be caught.
    """
    try:
        response = requests.get(url, timeout=timeout, headers=REQUEST_HEADERS)
        response.raise_for_status()
    except requests.RequestException as exc:
        return {"url": url, "emails": [], "has_contact_form": None, "error": str(exc)}

    html = response.text
    emails = sorted(set(MAILTO_RE.findall(html)) | set(EMAIL_RE.findall(html)))
    has_contact_form = "<form" in html.lower()

    return {"url": url, "emails": emails, "has_contact_form": has_contact_form}


def link_exists_on_page(url, target_domain, timeout=15):
    """Check whether a live page currently links to target_domain — used to
    verify a placed backlink actually went live."""
    try:
        response = requests.get(url, timeout=timeout, headers=REQUEST_HEADERS)
        response.raise_for_status()
    except requests.RequestException as exc:
        return {"url": url, "linked": False, "error": str(exc)}

    return {"url": url, "linked": target_domain.lower() in response.text.lower()}


OUTREACH_TEMPLATES = {
    "guest_post": {
        "subject": "Guest post idea for {site_name}",
        "body": (
            "Hi{contact_first_name_part},\n\n"
            "I came across {site_name} while researching {niche} content and enjoyed "
            "your work. I write about {niche} for {client_name} ({client_domain}) and "
            "would love to contribute a guest post your readers would find useful.\n\n"
            "A few angles I could write on:\n"
            "- [Topic idea 1]\n"
            "- [Topic idea 2]\n"
            "- [Topic idea 3]\n\n"
            "Happy to follow whatever guidelines you have — let me know if any of "
            "these would be a fit.\n\n"
            "Thanks,\n{sender_name}"
        ),
    },
    "resource_page": {
        "subject": "Suggestion for your {niche} resources page",
        "body": (
            "Hi{contact_first_name_part},\n\n"
            "I was looking through the resources page on {site_name} and thought your "
            "readers might also benefit from {client_domain}, a {niche} resource from "
            "{client_name}.\n\n"
            "No pressure at all, but if it looks like a fit, I'd appreciate a mention "
            "alongside the other links there.\n\n"
            "Thanks for putting the list together,\n{sender_name}"
        ),
    },
    "directory": {
        "subject": "Listing submission: {client_name}",
        "body": (
            "Hi{contact_first_name_part},\n\n"
            "I'd like to submit {client_name} ({client_domain}) for listing on "
            "{site_name}. Let me know if you need any further details to complete "
            "the listing.\n\n"
            "Thanks,\n{sender_name}"
        ),
    },
    "roundup": {
        "subject": "{client_name} for your {niche} roundup",
        "body": (
            "Hi{contact_first_name_part},\n\n"
            "I enjoyed your {niche} roundup on {site_name}. {client_name} "
            "({client_domain}) covers {niche} as well, and I think it could be a "
            "solid addition if you ever update the list.\n\n"
            "Thanks for considering it,\n{sender_name}"
        ),
    },
}


def draft_outreach_email(
    site_name,
    niche,
    client_name,
    client_domain,
    sender_name,
    opportunity_type="guest_post",
    contact_first_name=None,
):
    """Draft a professional, personalized outreach email for a link prospect.

    Returns a subject/body pair for human review; nothing is sent from here.
    """
    template = OUTREACH_TEMPLATES.get(opportunity_type)
    if template is None:
        raise ValueError(f"Unknown opportunity type: {opportunity_type}")

    fields = {
        "site_name": site_name,
        "niche": niche,
        "client_name": client_name,
        "client_domain": client_domain,
        "sender_name": sender_name,
        "contact_first_name_part": f" {contact_first_name}" if contact_first_name else "",
    }
    return {
        "subject": template["subject"].format(**fields),
        "body": template["body"].format(**fields),
    }
