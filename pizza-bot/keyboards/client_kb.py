from aiogram.types import ReplyKeyboardMarkup, KeyboardButton  # , ReplyKeyboardRemove

b1 = KeyboardButton('/Schedule')
b2 = KeyboardButton('/Location')
b3 = KeyboardButton('/Menu')
# b4 = KeyboardButton('Share number', request_contact=True)
# b5 = KeyboardButton('Send my coord', request_location=True)
kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1).add(b2).insert(b3)  # .row(b4, b5)
