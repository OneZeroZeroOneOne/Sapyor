from aiogram.types import ReplyKeyboardRemove, \
ReplyKeyboardMarkup, InlineKeyboardMarkup, \
InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from loguru import logger


start_cb = CallbackData('skip','new_game')

def start():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("НАЧАТЬ", callback_data=start_cb.new(new_game = 'new_game')))
    return markup
