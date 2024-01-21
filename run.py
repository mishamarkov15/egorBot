import asyncio
import logging
import handlers

from loader import dp, bot


async def main() -> None:
    """Initializing bot.

    :return:
    """
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
