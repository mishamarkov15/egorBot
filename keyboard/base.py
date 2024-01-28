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


def schedule_keyboard() -> types.InlineKeyboardMarkup:
    """

    :return:
    """
    buttons = [
        [types.InlineKeyboardButton(text='Расписание 👩🏻‍🏫',
                                    url='https://mgkit.ru/wp-content/uploads/2024/01/2-семестр-—-копия.xlsx')],
        [types.InlineKeyboardButton(text='« Назад', callback_data='start')]
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)
