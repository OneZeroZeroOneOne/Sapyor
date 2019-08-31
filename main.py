from loguru import logger
import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher.webhook import get_new_configured_app, configure_app
from handlers import Handlers
import settings
from aiohttp import web


if __name__=="__main__":
    loop = asyncio.get_event_loop()
    bot = Bot(token=settings.token, loop=loop, parse_mode=types.ParseMode.HTML)
    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)
    dp.middleware.setup(LoggingMiddleware())
    app = web.Application()
    loop.run_until_complete(bot.set_webhook(settings.BOT_WEBHOOK_URL))
    configure_app(dispatcher = dp, app = app, path = settings.BOT_WEBHOOK_PATH)
