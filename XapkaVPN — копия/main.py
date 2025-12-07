"""
ГЛАВНЫЙ ФАЙЛ ПРОЕКТА - ТОЧКА ВХОДА
Отвечает за запуск Telegram бота
"""
import asyncio
from aiogram import Bot, Dispatcher
from bot import handlers
from bot.config import BOT_TOKEN
import logging
logging.basicConfig(level=logging.INFO)

async def main():
    bot = Bot(token='')
    dp = Dispatcher()

    handlers.register(dp)

    await dp.start_polling(bot)

if __name__ == "__main__":

    asyncio.run(main())
