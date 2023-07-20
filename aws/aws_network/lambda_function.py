import json

import requests

URL = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'
def lambda_handler(event, context):
    result = requests.get(URL)

    content = result.json()

    for coin in content:
        for currency in content[coin]:
            print(f'--> {coin} is ${content[coin][currency]}')

    print(result)

if __name__ == "__main__":
    event: object = {}
    context: object = {}

    lambda_handler(event, context)