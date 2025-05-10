
def filter_by_state(list_dict: list[dict], state: str = 'EXECUTED'):
    """
    Принимает список словарей и опционально значение ключа,
    возвращает новый список словарей,
    у которых ключ state соответствует указанному значению
    """

    new_list_dict: list[dict] = []
    for item in list_dict:
        if state in item.values():
            new_list_dict.append(item)

    return new_list_dict