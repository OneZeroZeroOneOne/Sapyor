from loguru import logger
import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher.webhook import get_new_configured_app, configure_app
from handlers import Handlers
import settings
from aiohttp import web
from MyBot import MyBot
import config
from MyBot import create_bot



if __name__=="__main__":
    loop = asyncio.get_event_loop()
    logger.info("!!!!!!!!!!!!!!!")
    bot = bot = create_bot(config.rmq_channel, config.rmq_connection_string, token=config.bot_token)
    logger.info("!!!!!!!!!!!!!!!")
    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)
    dp.middleware.setup(LoggingMiddleware())
    handler = Handlers(dp, bot)
    handler.register()
    #app = web.Application()
    #loop.run_until_complete(bot.set_webhook(settings.BOT_WEBHOOK_URL))
    #configure_app(dispatcher = dp, app = app, path = settings.BOT_WEBHOOK_PATH)
    #web.run_app(app, host= "0.0.0.0", port=443)
    executor.start_polling(dp, loop=loop, skip_updates=True)
