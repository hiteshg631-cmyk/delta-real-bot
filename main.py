import os
import time
import logging
import requests

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Read environment variables from Render (you will set these in Environment tab)
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
    logger.error("Missing TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID in environment")
    raise SystemExit("Set environment variables and redeploy")

def send_telegram(text: str):
    """Send a message to Telegram chat"""
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": text}
    try:
        resp = requests.post(url, data=payload, timeout=10)
        logger.info("Telegram response: %s", resp.text)
    except Exception as e:
        logger.exception("Failed to send telegram message: %s", e)

def main():
    logger.info("Bot starting...")
    send_telegram("✅ Delta bot started on Render (test message).")

    while True:
        logger.info("Bot is alive - heartbeat")
        time.sleep(60)

if __name__ == "__main__":
    main()
