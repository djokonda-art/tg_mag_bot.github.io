from aiogram.types import WebAppInfo
from aiogram import types

web_app = WebAppInfo(url='https://djokonda-art.github.io/tg_mag_bot.github.io/')

keyboard = types.ReplyKeyboardMarkup(
    keyboard=[
        [types.KeyboardButton(text='Site', web_app=web_app)]
    ],
    resize_keyboard=True
)
