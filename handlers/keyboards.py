from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

cancel_button = KeyboardButton("CANCEL")
cancel_markup = ReplyKeyboardMarkup(resize_keyboard=False, one_time_keyboard=True)

help_button = KeyboardButton('HELP')
help_markup = ReplyKeyboardMarkup(resize_keyboard=False, one_time_keyboard=True)

cancel_markup.add(cancel_button)
help_markup.add(help_button)