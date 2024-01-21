from aiogram import types


def start_keyboard() -> types.InlineKeyboardMarkup:
    """Creating keyboard for /start command.

    :return:
    """
    buttons = [
        [types.InlineKeyboardButton(text='Расписание', callback_data='schedule')],
        [types.InlineKeyboardButton(text='Помощь', callback_data='help')],
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)
