#!/usr/bin/env python

import logging

from websockets import ConnectionClosedOK, ConnectionClosedError, ConnectionClosed


async def handler(websocket: any) -> any:
    """
    Основной handler для работы с сообщениями

    :param websocket: Объект websocket'а
    :return:
    """
    try:
        async for message in websocket:
            response = f"Echo: {message}"

            await websocket.send(response)
    except (ConnectionClosedOK, ConnectionClosedError, ConnectionClosed):
        logger = logging.getLogger('websockets')
        logger.debug("\n[SYSTEM]: Один из connect'ов закрыт.\n")
