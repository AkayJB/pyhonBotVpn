"""
ГЛАВНЫЙ ФАЙЛ С ЛОГИКОЙ БОТА
Содержит обработчики для всех команд и callback-запросов
"""
from aiogram import Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from datetime import datetime
from dateutil.relativedelta import relativedelta
from bot import messages
from bot import keyboards

# Хендлер для команды /start — показываем главное меню
async def start_cmd(message: types.Message):
    await message.answer(
        messages.WELCOME_MSG,
        reply_markup=keyboards.get_start_keyboard()
    )

# Словарь для хранения подписок: user_id -> dict с info
user_subscriptions = {}

# Хендлер для активации подписки
async def activate_subscription(callback: types.CallbackQuery):
    await callback.message.edit_text(
        messages.TARIFF_INFO,
        reply_markup=keyboards.get_tariff_keyboard()
    )
    await callback.answer()

# Хендлер для продления подписки
async def extend_subscription(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    info = user_subscriptions.get(user_id)
    
    if info and info["end_date"] > datetime.now():
        text = messages.SUBSCRIPTION_ACTIVE
        callback_data_yes = "extend_confirm"
    else:
        text = messages.SUBSCRIPTION_INACTIVE
        callback_data_yes = "activate"
    
    await callback.message.edit_text(
        text,
        reply_markup=keyboards.get_extend_keyboard(callback_data_yes)
    )
    await callback.answer()

# Хендлер подтверждения выбора тарифа
async def confirm_plan(callback: types.CallbackQuery):
    months = int(callback.data.split("_")[1])
    if months == 1:
        month_word = "месяц"
    elif months in [2, 3, 4]:
        month_word = "месяца"
    else:
        month_word = "месяцев"
    await callback.message.edit_text(
        messages.CONFIRM_MSG.format(f"{months} {month_word}"),
        reply_markup=keyboards.get_confirm_keyboard(months)
    )
    await callback.answer()

# Хендлер имитации оплаты
async def fake_payment(callback: types.CallbackQuery):
    months = int(callback.data.split("_")[1])
    user_id = callback.from_user.id
    username = callback.from_user.username or f"user_{user_id}"
    
    start_date = datetime.now()
    end_date = start_date + relativedelta(months=months)
    
    # Сохраняем в словарь
    user_subscriptions[user_id] = {
        "username": username,
        "start_date": start_date,
        "end_date": end_date,
        "months": months
    }
    
    # Определяем правильное склонение слова "месяц"
    if months == 1:
        month_word = "месяц"
    elif months in [2, 3, 4]:
        month_word = "месяца"
    else:
        month_word = "месяцев"
    
    simulated_output = f"Подписка активирована: {months} {month_word}, до {end_date.strftime('%d.%m.%Y')}"
    
    await callback.message.edit_text(
        simulated_output,
        reply_markup=keyboards.get_vless_button()
    )
    await callback.answer()

# Хендлер статуса подписки
async def subscription_status(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    info = user_subscriptions.get(user_id)
    
    if info:
        username = info["username"]
        end_date = info["end_date"].strftime("%d.%m.%Y")
        status = "Активирована"
        text = (
            f"Пользователь: @{username}\n"
            f"Статус: {status}\n"
            f"Дата окончания: {end_date}"
        )
    else:
        text = messages.NO_SUBSCRIPTION
    
    await callback.message.edit_text(
        text,
        reply_markup=keyboards.get_status_button()
    )
    await callback.answer()

# Хендлер для показа VLESS ключа
async def show_vless_key(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    info = user_subscriptions.get(user_id)
    
    if info:
        username = info["username"]
        vless_key = f"vless://{username}"
        text = vless_key
    else:
        text = "У вас нет активной подписки."
    
    await callback.message.edit_text(
        text,
        reply_markup=keyboards.get_vless_button()
    )
    await callback.answer()

# Хендлер для возврата в главное меню
async def main_menu(callback: types.CallbackQuery):
    await callback.message.edit_text(
        messages.WELCOME_MSG,
        reply_markup=keyboards.get_start_keyboard()
    )
    await callback.answer()

# Функция для регистрации всех хендлеров
def register(dp: Dispatcher):
    dp.message.register(start_cmd, Command(commands=["start"]))
    dp.callback_query.register(activate_subscription, F.data == "activate")
    dp.callback_query.register(extend_subscription, F.data == "extend")
    dp.callback_query.register(confirm_plan, F.data.startswith("plan_"))
    dp.callback_query.register(fake_payment, F.data.startswith("test_"))
    dp.callback_query.register(subscription_status, F.data == "status")
    dp.callback_query.register(show_vless_key, F.data == "vless")
    dp.callback_query.register(main_menu, F.data == "main_menu")

    dp.callback_query.register(activate_subscription, F.data == "extend_confirm")
