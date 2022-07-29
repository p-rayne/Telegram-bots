from aiogram import types, Dispatcher
from create_bot import dp


# @dp.message_handler()
async def echo_send(message: types.Message):
    if message.text.lower() == 'hi':
        await message.answer('hello to you too')


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(echo_send)
