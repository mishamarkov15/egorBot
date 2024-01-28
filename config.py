from environs import Env
from aiogram import types

env = Env()
env.read_env()


BOT_TOKEN = env.str('TELEGRAM_TOKEN')


bot_cmd = {
    'start': 'Начать работу',
    'help': 'Помощь'
}

BOT_COMMANDS = [types.BotCommand(command=k, description=v) for k, v in bot_cmd.items()]
