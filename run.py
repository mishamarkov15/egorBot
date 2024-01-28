import asyncio
import logging
import handlers
from config import BOT_COMMANDS

from loader import dp, bot


async def main() -> None:
    """Initializing bot.

    :return:
    """
    await bot.set_my_commands(BOT_COMMANDS)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
