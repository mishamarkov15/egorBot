from aiogram import types, F
from aiogram.enums import ChatAction
from aiogram.filters import CommandStart

from keyboard.base import start_keyboard, schedule_keyboard
from loader import dp, bot


@dp.message(CommandStart())
async def start(message: types.Message) -> None:
    """Answering for command /start.

    :param message:
    :return:
    """
    await bot.send_chat_action(message.chat.id, action=ChatAction.TYPING)
    await message.answer(f"Привет, {message.chat.full_name}!", reply_markup=start_keyboard())


@dp.callback_query(F.data=='start')
async def start(callback: types.CallbackQuery) -> None:
    """Answering for command /start.

    :param callback:
    :return:
    """
    await bot.send_chat_action(callback.message.chat.id, action=ChatAction.TYPING)
    await callback.message.edit_text(f"Привет, {callback.message.chat.full_name}!", reply_markup=start_keyboard())


@dp.callback_query(F.data == "schedule")
async def schedule(callback: types.CallbackQuery) -> None:
    """schedule callback

    :param callback:
    :return:
    """
    await bot.send_chat_action(callback.message.chat.id, action=ChatAction.TYPING)
    await callback.message.edit_text("Тут Ваше расписание!", reply_markup=schedule_keyboard())
