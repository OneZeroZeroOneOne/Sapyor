from aiogram.types import ReplyKeyboardRemove, \
ReplyKeyboardMarkup, InlineKeyboardMarkup, \
InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from loguru import logger
import random


def mapa():
    bombs = 20
    l = [i*0 for i in range(0,64)]
    logger.info(l)
    while(bombs>0):
        rand = random.randint(0,63)
        logger.info(rand)
        if l[rand]==0:
            l[rand]="*"
            bombs-=1
    logger.info(l)
    x = [-9,-8,-7,-1,+1,+7,+8,+9]
    for k in range(0,64):
        b=0
        for j in x:
            if k+j >=0 and k+j<=63 and l[k]==0:
                if l[k+j]=="*":
                    b+=1
                    logger.info(b)
        l[k]=b


if __name__=="__main__":
    mapa()
