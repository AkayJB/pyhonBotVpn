import asyncio
from aiogram import Bot, Dispatcher
from bot import handlers
from bot.config import BOT_TOKEN
import logging
logging.basicConfig(level=logging.INFO)

async def main():
    bot = Bot(token='7770468932:AAGsw4xBLvAQMfkbkTk_ByO17Cn0onkke7U')
    dp = Dispatcher()

    handlers.register(dp)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())