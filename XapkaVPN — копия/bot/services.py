from datetime import datetime
from dateutil.relativedelta import relativedelta

def get_subscription_status(user_id: int, subscriptions: dict) -> str:
    info = subscriptions.get(user_id)
    if info:
        username = info["username"]
        end_date = info["end_date"].strftime("%d.%m.%Y")
        return f"Пользователь: @{username}\nСтатус: Активирована\nДата окончания: {end_date}"
    return "Статус: Не активирована"