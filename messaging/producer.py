import os

import pika

def send_message(queue, message):
    print("messaging")
    print(os.environ)
    print(os.environ.items())
"""     conn_params = pika.ConnectionParameters(host=os.getenv())
    connection = pika.BlockingConnection(conn_params)
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
    print(" [x] Sent 'Hello World!'")
    connection.close() """
