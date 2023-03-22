import logging

from aiogram.utils.executor import start_polling

from app.handlers import *


def main():
    logging.basicConfig(
        level=logging.INFO,
        filename="app_log.log",
        filemode="a"
    )

    start_polling(dp, skip_updates=True)


if __name__ == '__main__':
    main()
