"""
КОНФИГУРАЦИОННЫЙ ФАЙЛ
Отвечает за загрузку настроек и переменных окружения
"""
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("")


