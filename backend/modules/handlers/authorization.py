def authorization_handler(data: dict) -> dict:
    """
    Метод установление связи

    :param data: Данные от клиента
    :return: dict
    """
    return {'data': {'code': 200, 'success': True, **data}}