import json

import requests

from databus.emit_log_topic import get_pika_channel
from ingestion.coin_list import coingecko_coin_list


def get_coin_price(coin_id):
    bitcoin_price = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd")

    if bitcoin_price:
        coin_json = json.loads(bitcoin_price.content)
        for coin in coin_json:
            price = coin_json[coin]
            for currency in coin_json[coin]:
                print(f'{coin} is at {price[currency]} {currency}')
                return {"price": {"price": price[currency], "currency": currency}}

# i = 0
# coin_data = {}
# while i < 10:
#     target_coin = coingecko_coin_list[i]["id"]
#     result = get_coin_price(target_coin)
#     if result:
#         coin_data[target_coin] = result
#     else:
#         print(f'--> no result for {target_coin}')
#     i += 1
# print(f"--> coin data is {len(coin_data)} long")
#
# message = bytes(json.dumps(coin_data), 'utf-8')
#
# try:
#     channel = get_pika_channel()
#     channel.basic_publish(exchange='finance', routing_key='coin', body=message)
#
#     channel.close()
# except Exception as e:
#     print(f'--> error: {e}')
