from aiogram.types import ReplyKeyboardRemove, \
ReplyKeyboardMarkup, InlineKeyboardMarkup, \
InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

val_cb = CallbackData('val_cb', 'value', 'x', 'y', 'action')

def map_paint(l , opened):
    markup = InlineKeyboardMarkup()
    listbut = list()
    print(opened)
    for i in range(0,len(l)):
        listbut.clear()
        for j in range(0,len(l[i])):
            if [i,j] in opened:
                listbut.append(InlineKeyboardButton(l[i][j], callback_data=val_cb.new(value = l[i][j], x=int(j), y=int(i), action = "open_but")))
            else:
                listbut.append(InlineKeyboardButton(" ", callback_data=val_cb.new(value = l[i][j], x=int(j), y=int(i), action = "open_but")))
        markup.row(*listbut)
    return markup
