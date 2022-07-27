from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import os

from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def on_startup(_):
    print('bot is running')
"""********************CLIENT********************"""


@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'You are welcome!')
        await message.delete()
    except:
        await message.reply('''Communication with the bot through private messages. 
        Write him:\nhttps://t.me/rinoket_test_bot''')


@dp.message_handler(commands=['Work_mode'])
async def pizza_open__command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Every day from 10 am to 10 pm')


@dp.message_handler(commands=['Location'])
async def pizza_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, '221b, Baker Street, London')
"""********************MAIN********************"""


@dp.message_handler()
async def echo_send(message: types.Message):
    if message.text.lower() == 'hi':
        await message.answer('hello to you too')
    # await message.reply(message.text)
    # await bot.send_message(message.from_user.id, message.text)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
