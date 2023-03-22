from aiogram import Bot, Dispatcher

from app.config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
