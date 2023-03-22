from aiogram import types

from app.dispatcher import dp


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply(
        f'Я бот. Приятно познакомиться, {message.from_user.first_name}'
    )


@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def text_reply(message: types.Message):
    if message.text.lower() == 'привет':
        await message.answer('Привет!')
    else:
        await message.answer('Не понимаю, что это значит...')
