import logging
from datetime import datetime
from pathlib import Path

from aiogram.utils.executor import start_polling

from app.handlers import *


def main():
    log_name = f'logs/{datetime.now().strftime("%Y-%m-%d")}.log'
    Path(log_name).parent.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        filename=log_name,
        filemode="a"
    )

    start_polling(dp, skip_updates=True)


if __name__ == '__main__':
    main()
