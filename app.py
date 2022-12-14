import asyncio

from aiohttp import web

from loader import dp, context
from web_server import app, setup_app
from conf import WEBHOOK_URL_PATH, WEBHOOK_URL_BASE, WEBHOOK_SSL_CERT, WEBHOOK_PORT, WEBHOOK_LISTEN
from utils import set_default_commands

import handlers


async def on_startup(dispatcher):
    await set_default_commands(dispatcher)
    await dp.bot.delete_webhook()
    await dp.bot.set_webhook(
        url=f'{WEBHOOK_URL_BASE}{WEBHOOK_URL_PATH}',
        certificate=open(WEBHOOK_SSL_CERT, 'r'),
        drop_pending_updates=True
    )


loop = asyncio.new_event_loop()
loop.create_task(on_startup(dp))

if __name__ == '__main__':
    setup_app(app)
    web.run_app(
        app,
        host=WEBHOOK_LISTEN,
        port=WEBHOOK_PORT,
        ssl_context=context,
        loop=loop
    )
