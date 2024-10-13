#!/usr/bin/env python

import json
import logging

from websockets import ConnectionClosedOK, ConnectionClosedError, ConnectionClosed
from .handlers.authorization import authorization_handler

logger = logging.getLogger('websockets')


async def handler(websocket: any) -> any:
    """
    Основной handler для работы с сообщениями

    :param websocket: Объект websocket'а
    :return:
    """
    try:
        async for message in websocket:
            data = json.loads(message)

            if data.get('event') == 'auth':
                response = authorization_handler(data)
            else:
                response = {'data': {'code': 403, 'text': 'Not access'}}

            await websocket.send(json.dumps(response))
    except (ConnectionClosedOK, ConnectionClosedError, ConnectionClosed):
        logger.debug("\n[SYSTEM]: Один из connect'ов закрыт.\n")
