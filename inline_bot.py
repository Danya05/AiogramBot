import config

import logging

import hashlib

from aiogram import Bot, Dispatcher, executor

from aiogram.types import InlineQuery, InputTextMessageContent, InlineQueryResultArticle

API_TOKEN = config.API_TOKEN

logging.basicConfig(level=logging.DEBUG)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.inline_handler()
async def inline_echo(inline_query: InlineQuery):
    text = inline_query.query
    input_context = InputTextMessageContent(text)
    result_id: str = hashlib.md5(text.encode()).hexdigest()
    item = InlineQueryResultArticle(
        id=result_id,
        title=f'Result {text!r}',
        input_message_content=input_context
    )
    await bot.answer_inline_query(inline_query.id, results=[item], cache_time=1)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
