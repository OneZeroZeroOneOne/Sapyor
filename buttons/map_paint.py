from aiogram.types import ReplyKeyboardRemove, \
ReplyKeyboardMarkup, InlineKeyboardMarkup, \
InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

val_cb = CallbackData('val_cb', 'value', 'x', 'y')
def map_paint(l , opened, x, y):
    markup = InlineKeyboardMarkup()
    listbut = list()
    for i in range(0,len(l)+1):
        listbut.clear()
        for j in range(0,len(l[i])+1):
            if [i,j] in opened:
                listbut.append(InlineKeyboardButton(l[i][j], callback_data=val_cb.new(value = l[i][j], x=j, y=i)))
            else:
                listbut.append(InlineKeyboardButton(" ", callback_data=val_cb.new(value = l[i][j], x=j, y=i)))
        markup.row(*listbut)
    return markup
