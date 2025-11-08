import os
import asyncio
import aiohttp
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the bot token
TOKEN = os.getenv("BOT_TOKEN")

# -------------------------------
# Command: /start
# -------------------------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Welcome! Type /price to get BTC price from Delta Exchange.")

# -------------------------------
# Command: /price
# -------------------------------
async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = "https://api.delta.exchange/v2/tickers/BTCUSDT"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, ssl=False) as response:
                if response.status == 200:
                    data = await response.json()
                    price = data["result"]["mark_price"]
                    await update.message.reply_text(f"💰 BTC Price: ${price}")
                else:
                    await update.message.reply_text("❌ Error fetching price!")
    except Exception as e:
        await update.message.reply_text(f"⚠️ Error: {e}")

# -------------------------------
# Main Function
# -------------------------------
async def main():
    print("🤖 Bot is starting...")

    # Safety check for token
    if not TOKEN:
        raise ValueError("❌ BOT_TOKEN not found! Please set it correctly in .env file.")

    app = ApplicationBuilder().token(TOKEN).build()

    # Add commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("price", price))

    print("✅ Bot is live and polling Telegram updates...")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
