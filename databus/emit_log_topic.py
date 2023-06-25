import pika
import sys

from pika.adapters.blocking_connection import BlockingChannel

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

routing_key = sys.argv[1] if len(sys.argv) > 2 else 'anonymous.info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'
channel.basic_publish(
    exchange='topic_logs', routing_key=routing_key, body=message)
print("--> [x] Sent %r:%r" % (routing_key, message))
connection.close()


def get_pika_channel() -> BlockingChannel:
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='finance', exchange_type='topic')

    routing_key = sys.argv[1] if len(sys.argv) > 2 else 'anonymous.info'

    return channel

# def open_pika_channel(msg: str, keep_open: bool):
#     connection = pika.BlockingConnection(
#         pika.ConnectionParameters(host='localhost'))
#     channel = connection.channel()
#
#     channel.exchange_declare(exchange='topic_logs', exchange_type='topic')
#
#     routing_key = sys.argv[1] if len(sys.argv) > 2 else 'anonymous.info'
#     message = ' '.join(sys.argv[2:]) or 'Hello World!'
#
#     if !keep_open:
#         channel.close()
