from aiogram.types import ReplyKeyboardRemove, \
ReplyKeyboardMarkup, InlineKeyboardMarkup, \
InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from loguru import logger


start_cb = CallbackData('skip','start')

def start():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("НАЧАТЬ", callback_data=start_cb.new(start = 'start')))
    return markup
