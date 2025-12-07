"""
СЕРВИСНЫЙ ФАЙЛ С ВСПОМОГАТЕЛЬНЫМИ ФУНКЦИЯМИ
здесь может быть написана логика и работа с базой данных
Сейчас содержит одну функцию для демонстрации архитектуры
"""
from datetime import datetime
from dateutil.relativedelta import relativedelta

# ВСПОМОГАТЕЛЬНАЯ ФУНКЦИЯ ДЛЯ ПРОВЕРКИ СТАТУСА
def get_subscription_status(user_id: int, subscriptions: dict) -> str:
    info = subscriptions.get(user_id)
    # ПОДПИСКА АКТИВНА: возвращаем детали
    if info:
        username = info["username"]
        end_date = info["end_date"].strftime("%d.%m.%Y")
        return f"Пользователь: @{username}\nСтатус: Активирована\nДата окончания: {end_date}"

     # ПОДПИСКИ НЕТ: стандартное сообщение
    return "Статус: Не активирована"
