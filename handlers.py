from aiogram.types import ContentType, ChatMember
import settings
from aiogram import Bot, Dispatcher, executor, types
from buttons import start, map_paint
import map_logic
from loguru import logger
from objects.channel import Channel
import aio_pika


class Handlers:
    def __init__(self, dp, bot):
        self.bot = bot
        self.dp = dp
        self.channels = dict()


    def register(self):
        self.dp.register_message_handler(self.start, commands='start')
        self.dp.register_callback_query_handler(self.new_game, start.start_cb.filter(new_game='new_game'))
        self.dp.register_callback_query_handler(self.open_but, map_paint.val_cb.filter(action='open_but'))

    async def new_game(self, query: types.CallbackQuery, callback_data: dict):
        self.channels[query.message.chat.id].opened.clear()
        self.channels[query.message.chat.id].set_pole(map_logic.mapa())
        await query.bot.edit_message_reply_markup(query.message.chat.id, message_id=query.message.message_id,
                    reply_markup=map_paint.map_paint(self.channels[query.message.chat.id].pole, self.channels[query.message.chat.id].opened))



    async def open_but(self, query: types.CallbackQuery, callback_data: dict):
        if callback_data['value']=="*":
            await query.bot.edit_message_reply_markup(query.message.chat.id, message_id=query.message.message_id, reply_markup=None)
            await query.bot.send_message(query.message.chat.id, text=settings.game_over,
                                        parse_mode = 'Markdown', reply_markup=start.start())
        else:
            logger.info(self.channels[query.message.chat.id].opened)
            logger.info(int(callback_data['y']))
            self.channels[query.message.chat.id].add_open_but([int(callback_data['y']), int(callback_data['x'])])
            logger.info(self.channels[query.message.chat.id].opened)
            await query.bot.edit_message_reply_markup(query.message.chat.id, message_id=query.message.message_id,
                    reply_markup=map_paint.map_paint(self.channels[query.message.chat.id].pole, self.channels[query.message.chat.id].opened))


    async def start(self, message: types.Message):
        logger.info(message.chat.id)
        if not message.chat.id in self.channels.keys():
            self.channels[message.chat.id] = Channel(message.chat.id)
            logger.info(self.channels)
        await self.bot.send_message(message.chat.id, text=settings.start_text,
                                    parse_mode = 'Markdown', reply_markup=start.start())
