#!/usr/bin/env python

import asyncio
from websockets.asyncio.server import serve
from handlers.own_handler import handler
from environment.parameters import *


if bool(get_environment('DEBUG')):
    # Настройка логирования
    logger = logging.getLogger('websockets')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())


async def main():
    async with serve(handler, get_environment('HOST'), int(get_environment('PORT'))):
        logger.debug('\n[SYSTEM]: Все переменные окружения подключены!\n')
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
