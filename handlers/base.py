from aiogram import types, F
from aiogram.enums import ChatAction
from aiogram.filters import CommandStart

from keyboard.base import start_keyboard
from loader import dp, bot


@dp.message(CommandStart())
async def start(message: types.Message) -> None:
    """Answering for command /start.

    :param message:
    :return:
    """
    await bot.send_chat_action(message.chat.id, action=ChatAction.TYPING)
    await message.answer(f"Привет, {message.chat.full_name}!", reply_markup=start_keyboard())


@dp.callback_query(F.data == "schedule")
async def schedule(callback: types.CallbackQuery) -> None:
    """schedule callback

    :param callback:
    :return:
    """
    await bot.send_chat_action(callback.message.chat.id, action=ChatAction.TYPING)
    await callback.message.answer("Тут Ваше расписание!")
