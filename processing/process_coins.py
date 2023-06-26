import json


def process_coin_batch(data: bytes):
    coin_batch = json.loads(data.decode('utf-8'))

    highest_coin = process_high(coin_batch)

    print(f'--> highest coin is {highest_coin["highest_coin"]} & price is {highest_coin["highest_coin_price"]}')


def process_high(coin_data: dict) -> dict:
    highest_coin = ""
    highest_coin_price = 0

    try:
        for coin in coin_data:
            coin_price = coin_data[coin]["price"]["price"]
            if coin_price > highest_coin_price:
                highest_coin = coin
                highest_coin_price = coin_data[coin]["price"]["price"]
    except Exception as e:
        print(f'--> error: {e}')

    return {"highest_coin": highest_coin, "highest_coin_price": highest_coin_price}
