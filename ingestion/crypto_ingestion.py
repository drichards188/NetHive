import json

import requests


def get_coin_price(coin_id):
    bitcoin_price = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd")

    if bitcoin_price:
        coin_json = json.loads(bitcoin_price.content)
        for coin in coin_json:
            price = coin_json[coin]
            for currency in coin_json[coin]:
                print(f'{coin} is at {price[currency]} {currency}')
                return {"price": {"price": price[currency], "currency": currency}}
