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
