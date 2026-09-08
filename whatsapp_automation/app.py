"""
Generic WhatsApp auto-responder built on the Meta WhatsApp Cloud API.

Reusable as-is:
  - webhook verification (GET /webhook)
  - inbound message parsing + optional request-signature check (POST /webhook)
  - sending replies (see whatsapp_client.py)

Adapt for your use case:
  - generate_reply() — plug in your own logic (FAQ lookup, database query,
    LLM call, ticket creation, etc.)
"""
import hashlib
import hmac
import logging
import os
from typing import Optional

from flask import Flask, request, jsonify

from whatsapp_client import send_text_message

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

VERIFY_TOKEN = os.environ["WHATSAPP_VERIFY_TOKEN"]
APP_SECRET = os.environ.get("WHATSAPP_APP_SECRET")  # optional, enables signature checks


@app.route("/webhook", methods=["GET"])
def verify_webhook():
    """Meta calls this once when you set the webhook URL in the app dashboard."""
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return challenge, 200
    return "Verification failed", 403


@app.route("/webhook", methods=["POST"])
def receive_message():
    if APP_SECRET and not _signature_is_valid(request):
        logger.warning("Rejected webhook call with invalid signature")
        return "Invalid signature", 403

    payload = request.get_json(silent=True) or {}

    for entry in payload.get("entry", []):
        for change in entry.get("changes", []):
            for message in change.get("value", {}).get("messages", []):
                handle_incoming_message(message)

    # Respond quickly with 200 so Meta doesn't retry/backoff the webhook.
    return jsonify(status="received"), 200


def _signature_is_valid(req) -> bool:
    signature_header = req.headers.get("X-Hub-Signature-256", "")
    if not signature_header.startswith("sha256="):
        return False

    expected = hmac.new(APP_SECRET.encode(), req.get_data(), hashlib.sha256).hexdigest()
    provided = signature_header.removeprefix("sha256=")
    return hmac.compare_digest(expected, provided)


def handle_incoming_message(message: dict) -> None:
    sender = message.get("from")
    msg_type = message.get("type")

    if msg_type != "text":
        logger.info("Ignoring non-text message type: %s", msg_type)
        return

    text = message["text"]["body"]
    logger.info("Message from %s: %s", sender, text)

    reply = generate_reply(text)
    if reply:
        send_text_message(sender, reply)


def generate_reply(incoming_text: str) -> Optional[str]:
    """Decide what to send back. Replace this with your own business logic."""
    text = incoming_text.strip().lower()

    keyword_responses = {
        "hi": "Hello! Thanks for reaching out. How can we help you today?",
        "hello": "Hi there! How can we help you today?",
        "hours": "We're open Monday-Friday, 9am-6pm.",
        "help": "Send 'hours' for business hours, or ask us anything and a team member will follow up.",
    }

    for keyword, response in keyword_responses.items():
        if keyword in text:
            return response

    return "Thanks for your message! A team member will get back to you shortly."


if __name__ == "__main__":
    app.run(port=int(os.environ.get("PORT", 5000)))
