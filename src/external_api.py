import json
import os
import requests
from dotenv import load_dotenv


def get_transaction_amount_in_rub(transaction: dict) -> float | None:
    """ Принимает на вход транзакцию и
    возвращает сумму транзакции в рублях """

    if transaction['operationAmount']['currency']['code'] == 'RUB':
        return float(transaction['operationAmount']['amount'])


    load_dotenv()
    api_key = os.getenv('API_KEY')
    headers = {
        "apikey": api_key
    }
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={transaction['operationAmount']['currency']['code']}&amount={transaction['operationAmount']['amount']}"

    response = (requests.request("GET", url, headers = headers)).json()

    return response['result']




operation = {
    "id": 142264268,
    "state": "EXECUTED",
    "date": "2019-04-04T23:20:05.206878",
    "operationAmount": {
      "amount": "79114.93",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод со счета на счет",
    "from": "Счет 19708645243227258542",
    "to": "Счет 75651667383060284188"
  }
print(get_transaction_amount_in_rub(operation))