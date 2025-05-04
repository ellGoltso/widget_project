import masks


def mask_account_card(card_or_account: str) -> str:
    """Принимает строку, содержащую тип и номер карты или счета и возвращает строку с замаскированным номером"""

    card_or_account_type: str = ""
    number: str = ""
    full_name_card_account: str = ""

    for ch in card_or_account:
        if ch.isalpha() or ch == " ":
            card_or_account_type += ch
        else:
            number += ch

    if len(number) == 16:
        full_name_card_account += card_or_account_type + masks.get_mask_card_number(int(number))
    else:
        full_name_card_account += card_or_account_type + masks.get_mask_account(int(number))

    return full_name_card_account


def get_date(date_time: str) -> str:
    """Получает строку даты и времени и возвращает строку с датой в формате : ДД.ММ.ГГГГ"""

    year: str = date_time[:4]
    month: str = date_time[5:7]
    day: str = date_time[8:10]

    return f"{day}.{month}.{year}"
