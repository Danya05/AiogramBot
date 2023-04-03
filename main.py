import config

import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = config.API_TOKEN

logging.basicConfig(level=logging.DEBUG)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm TestBot!\nPowered by aiogram.")

'''
Если нужно ответить на сообщение - reply
Если просто отправить - answer
'''


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
