#!/usr/bin/env python
import os

import logging


def get_environment(name: str):
    """
    Метод получения переменной окружения

    :param name: Имя переменного окружения
    :return:
    """
    environment = os.environ.get(name)

    if environment is None or environment == "":
        raise Exception(f"[SYSTEM] - переменная окружения {name} отсутствует!\n")

    return environment