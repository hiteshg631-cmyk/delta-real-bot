from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# === अपना Telegram Bot Token डालो ===
TOKEN = "8236646193:AAGf-5Lybx9j5VW-DXTzL-vAifb3eMTiEiY"

# === /start command ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Bot is running successfully!")

# === Main bot app ===
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("🤖 Bot is live... now go to Telegram and type /start to test it!")
    app.run_polling()
