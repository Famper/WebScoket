import logging

from .parameters import get_environment

logger = logging.getLogger('websockets')


def set_logging() -> None:
    """
    Задаем уровень логирования

    :return: None
    """
    is_debug = str(get_environment('DEBUG'))

    if is_debug.lower() == 'true':
        logger.setLevel(logging.DEBUG)
        logger.addHandler(logging.StreamHandler())
    else:
        logger.setLevel(logging.INFO)
        logger.addHandler(logging.StreamHandler())