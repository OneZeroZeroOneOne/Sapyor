from aiogram.types import ContentType, ChatMember
import settings
from aiogram import Bot, Dispatcher, executor, types
from buttons.start import start
from loguru import logger

class Handlers:
    def __init__(self, dp, bot):
        self.bot = bot
        self.dp = dp

    def register(self):
        self.dp.register_message_handler(self.start, commands='start')
        self.dp.register_callback_query_handler(self.query_skip, skip.skip_cb.filter(ng='new_game'))

    async def new_game(self, query: types.CallbackQuery, callback_data: dict):
        await query.bot.send_message(query.message.chat.id,"preiom")



    async def start(self, message: types.Message):
        logger.info(message.chat.id)
        await self.bot.send_message(message.chat.id, text=settings.start_text,
                                    parse_mode = 'Markdown', reply_markup=start())
