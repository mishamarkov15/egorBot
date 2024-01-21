import logging
import sys
from logging.handlers import RotatingFileHandler

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from config import BOT_TOKEN

bot = Bot(BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()


def init_logging() -> None:
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter(
        fmt='[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
        datefmt='%d.%m.%Y %H:%M:%S'
    )

    stdout = logging.StreamHandler(sys.stdout)
    stdout.setFormatter(formatter)
    stdout.setLevel(logging.INFO)

    fout = RotatingFileHandler(filename='logs/app.log', maxBytes=10*1024*1024, backupCount=10)
    fout.setFormatter(formatter)
    fout.setLevel(logging.INFO)

    logger.addHandler(stdout)
    logger.addHandler(fout)


init_logging()
