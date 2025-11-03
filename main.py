import os
import asyncio
from telegram import Bot

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=TOKEN)

async def main():
    await bot.send_message(chat_id=CHAT_ID, text="✅ Bot started successfully on Render!")

if __name__ == "__main__":
    asyncio.run(main())
