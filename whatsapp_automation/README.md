# WhatsApp Automated Response

A minimal, reusable scaffold for auto-replying to WhatsApp messages using
Meta's **WhatsApp Cloud API**. Everything except `generate_reply()` in
`app.py` is generic infrastructure — adapt that one function to your use
case (FAQ bot, order-status lookup, SERP-ranking updates, escalation to a
human, etc.).

## How it works

1. Someone sends a WhatsApp message to your business number.
2. Meta POSTs the message to your `/webhook` endpoint.
3. `app.py` parses it, calls `generate_reply()` to decide what to say back,
   and sends the reply via `whatsapp_client.py`.

## 1. Create a Meta app and get credentials

1. Go to [developers.facebook.com](https://developers.facebook.com/) → **My Apps** → **Create App** → choose type **Business**.
2. Add the **WhatsApp** product to the app.
3. On the WhatsApp → API Setup page, note down:
   - **Temporary access token** (valid ~24h; generate a permanent one later via a System User for production).
   - **Phone number ID** (a test number is provided free for development).
4. Under **Configuration**, you'll set up the webhook next.

## 2. Configure environment variables

```bash
cp .env.example .env
# then edit .env and fill in real values
```

- `WHATSAPP_ACCESS_TOKEN` — from step 1.
- `WHATSAPP_PHONE_NUMBER_ID` — from step 1.
- `WHATSAPP_VERIFY_TOKEN` — any secret string you make up; Meta echoes it back during webhook verification.
- `WHATSAPP_APP_SECRET` — optional, from your app's Basic Settings; enables signature verification on incoming requests (recommended once the webhook is publicly reachable).

## 3. Run it locally

```bash
pip install -r requirements.txt
export $(cat .env | xargs)   # or use python-dotenv / direnv
python app.py
```

This starts a Flask server on `http://localhost:5000`.

## 4. Expose it publicly and register the webhook

Meta needs an HTTPS URL it can reach, so for local development use a tunnel:

```bash
ngrok http 5000
```

Then in the Meta app dashboard (WhatsApp → Configuration → Webhook):

- **Callback URL**: `https://<your-ngrok-domain>/webhook`
- **Verify token**: same value as `WHATSAPP_VERIFY_TOKEN`
- Click **Verify and save** (this triggers the `GET /webhook` handshake).
- Subscribe to the **messages** field.

## 5. Test it

Send a WhatsApp message to your test number from the phone number you
registered as a tester in the Meta dashboard. You should get an automatic
reply within a couple of seconds; check the server logs for details.

## 6. Customize the logic

Edit `generate_reply()` in `app.py`. The incoming text is already extracted
for you — return `None` to skip replying, or return a string to send it
back. Examples of what to plug in:

- Keyword/intent matching (shown by default).
- A lookup against this project's rank-tracking data (`tracking_data/rankings.json`) to answer "what's my ranking for X?".
- A call to an LLM for open-ended conversation.
- Forwarding to a human/CRM ticket for anything the bot can't handle.

## 7. Going to production

- Swap the temporary access token for a permanent one issued to a System User with `whatsapp_business_messaging` permission.
- Move off the free test number to a verified business phone number.
- Run behind a real WSGI server (e.g. `gunicorn app:app`) with HTTPS, not Flask's dev server.
- Set `WHATSAPP_APP_SECRET` so `/webhook` rejects requests that aren't genuinely from Meta.
- Handle Meta's rate limits and message-template requirements if you need to message users outside a 24-hour customer-service window (that requires pre-approved message templates instead of free-form text).
