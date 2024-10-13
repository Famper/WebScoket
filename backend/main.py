#!/usr/bin/env python

import asyncio

from websockets.asyncio.server import serve

from modules.own_handler import handler
from modules.set_logging import *


async def main():
    async with serve(handler, get_environment('HOST'), int(get_environment('PORT'))):
        logger.debug('\n[SYSTEM]: Все переменные окружения подключены!\n')
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    set_logging()
    asyncio.run(main())
