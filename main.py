import os
import requests
import time
from telegram import Bot

# Telegram Bot setup
TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
bot = Bot(token=TOKEN)

# Delta Exchange API credentials
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
BASE_URL = "https://api.delta.exchange"

# Example: Check account balance
def get_balance():
    url = f"{BASE_URL}/v2/wallet/balances"
    headers = {"api-key": API_KEY, "api-secret": API_SECRET}
    response = requests.get(url, headers=headers)
    return response.json()

# Send balance to Telegram
def send_balance():
    try:
        data = get_balance()
        bot.send_message(chat_id=CHAT_ID, text=f"💰 Balance Info:\n{data}")
    except Exception as e:
        bot.send_message(chat_id=CHAT_ID, text=f"❌ Error: {e}")

# Auto run loop
if __name__ == "__main__":
    bot.send_message(chat_id=CHAT_ID, text="🤖 Bot started on Render!")
    while True:
        send_balance()
        time.sleep(60 * 5)  # हर 5 मिनट में बैलेंस भेजेगा
