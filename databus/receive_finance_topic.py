import time

import pika
import sys


def consume_finance():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='finance', exchange_type='topic')

    result = channel.queue_declare('', exclusive=True)
    queue_name = result.method.queue

    # server_id = sys.argv[2]
    server_id = "alpha"
    print(f'server id is: {server_id}')

    # binding_keys = sys.argv[1:]
    binding_keys = "coin.price"
    if not binding_keys:
        sys.stderr.write("Usage: %s [binding_key]...\n" % sys.argv[0])
        sys.exit(1)

    for binding_key in binding_keys:
        channel.queue_bind(
            exchange='finance', queue=queue_name, routing_key='coin')

    print(' [*] Waiting for data. To exit press CTRL+C')

    def callback(ch, method, properties, body):
        time.sleep(1)
        print("<--%r [x] %r:%r \n" % (server_id, method.routing_key, body))

    # how to return data more than once? a return statement will stop the function
    channel.basic_consume(
        queue=queue_name, on_message_callback=callback, auto_ack=True)

    channel.start_consuming()


# consume_finance()
