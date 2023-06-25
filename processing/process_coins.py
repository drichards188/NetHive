import json


def process_coin_batch(data: bytes):
    coin_batch = json.loads(data.decode('utf-8'))
    for coin in coin_batch:
        print(f'--> coin is {coin} & price is {coin_batch[coin]["price"]}')
