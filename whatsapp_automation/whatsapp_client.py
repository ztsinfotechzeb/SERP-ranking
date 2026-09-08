"""Thin wrapper around the Meta WhatsApp Cloud API for sending messages."""
import os

import requests

GRAPH_API_VERSION = "v20.0"
BASE_URL = "https://graph.facebook.com/{version}/{phone_number_id}/messages"


def _config():
    return {
        "access_token": os.environ["WHATSAPP_ACCESS_TOKEN"],
        "phone_number_id": os.environ["WHATSAPP_PHONE_NUMBER_ID"],
    }


def send_text_message(to: str, body: str) -> dict:
    """Send a plain-text WhatsApp message to `to` (E.164 phone number, no '+')."""
    config = _config()
    url = BASE_URL.format(version=GRAPH_API_VERSION, phone_number_id=config["phone_number_id"])
    headers = {
        "Authorization": f"Bearer {config['access_token']}",
        "Content-Type": "application/json",
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {"body": body},
    }

    response = requests.post(url, headers=headers, json=payload, timeout=10)
    response.raise_for_status()
    return response.json()
