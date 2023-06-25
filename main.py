import json
import sys

from databus.emit_log_topic import get_pika_channel
from databus.receive_finance_topic import consume_finance
from ingestion.coin_list import coingecko_coin_list
from ingestion.crypto_ingestion import get_coin_price
from ingestion.web_scrape import WebScrape


# figure out if should be REST API. Consider GraohQL
# def main():
#     target_url = "https://runescape.wiki/"
#
#     scrape_results = WebScrape.get_page(target_url)
#     print(scrape_results)
#
# main()

def produce():
    i = 0
    coin_data = {}
    while i < 10:
        target_coin = coingecko_coin_list[i]["id"]
        result = get_coin_price(target_coin)
        if result:
            coin_data[target_coin] = result
        else:
            print(f'--> no result for {target_coin}')
        i += 1
    print(f"--> coin data is {len(coin_data)} long")

    message = bytes(json.dumps(coin_data), 'utf-8')

    try:
        channel = get_pika_channel()
        channel.basic_publish(exchange='finance', routing_key='coin.price', body=message)

        channel.close()
    except Exception as e:
        print(f'--> error: {e}')


def consume():
    consume_finance()


if sys.argv[1] == 'produce':
    produce()
elif sys.argv[1] == 'consume':
    consume()
