from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def get_start_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Активировать подписку", callback_data="activate")],
        [InlineKeyboardButton(text="Продлить подписку", callback_data="extend")],
        [InlineKeyboardButton(text="Статус подписки", callback_data="status")],
        [InlineKeyboardButton(text="VLESS ключ", callback_data="vless")]
    ])

def get_tariff_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="1 месяц", callback_data="plan_1"),
            InlineKeyboardButton(text="2 месяца", callback_data="plan_2"),
            InlineKeyboardButton(text="3 месяца", callback_data="plan_3"),
        ],
        [InlineKeyboardButton(text="В главное меню", callback_data="main_menu")]
    ])

def get_confirm_keyboard(months: str):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Подтвердить", callback_data=f"test_{months}")],
        [InlineKeyboardButton(text="Вернуться к тарифам", callback_data="activate")],
        [InlineKeyboardButton(text="В главное меню", callback_data="main_menu")]
    ])

def get_status_button():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="VLESS ключ", callback_data="vless")],
        [InlineKeyboardButton(text="В главное меню", callback_data="main_menu")]
    ])

def get_vless_button():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="В главное меню", callback_data="main_menu")]
    ])

def get_extend_keyboard(callback_data_yes: str):
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Да", callback_data=callback_data_yes),
            InlineKeyboardButton(text="Нет", callback_data="main_menu")
        ]
    ])