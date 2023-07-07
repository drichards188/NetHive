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
    try:
        channel = get_pika_channel()
        i = 0
        coin_data = {}
        while i < 20:
            target_coin = coingecko_coin_list[i]["id"]
            result = get_coin_price(target_coin)
            if result:
                message = bytes(json.dumps(result), 'utf-8')
                channel.basic_publish(exchange='finance', routing_key='coin.data', body=message)
                coin_data[target_coin] = result
            else:
                print(f'--> no result for {target_coin}')
            i += 1
        print(f"--> coin data is {len(coin_data)} long")

        channel.close()
    except Exception as e:
        print(f'--> error: {e}')


def consume():
    consume_finance()


if sys.argv[1] == 'produce':
    produce()
elif sys.argv[1] == 'consume':
    consume()
