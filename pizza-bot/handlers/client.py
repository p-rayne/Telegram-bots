from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from database import sqlite_db
# @dp.message_handler(commands=['start', 'help'])


async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'You are welcome!', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('''Communication with the bot through private messages. 
        Write him:\nhttps://t.me/rinoket_test_bot''')


# @dp.message_handler(commands=['Schedule'])
async def pizza_open__command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Every day from 10 am to 10 pm')


# @dp.message_handler(commands=['Location'])
async def pizza_place_command(message: types.Message):
    # , reply_markup=ReplyKeyboardRemove())
    await bot.send_message(message.from_user.id, '221b, Baker Street, London')


# @dp.message_handler(commands=['Menu'])
async def pizza_menu_command(message: types.Message):
    await sqlite_db.sql_read(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_open__command, commands=['Schedule'])
    dp.register_message_handler(pizza_place_command, commands=['Location'])
    dp.register_message_handler(pizza_menu_command, commands=['Menu'])
