import config

import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = config.API_TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm TestBot!\nPowered by aiogram.")