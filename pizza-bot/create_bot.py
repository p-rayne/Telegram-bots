from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from dotenv import load_dotenv
import os
load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
