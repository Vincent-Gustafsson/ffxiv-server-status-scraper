import os, json

import pika

def send_message(message):
    conn_params = pika.ConnectionParameters(host=os.getenv("CLOUDAQMP_URL"))
    connection = pika.BlockingConnection(conn_params)
    channel = connection.channel()

    channel.queue_declare(queue='scraping-results')

    channel.basic_publish(exchange='', routing_key='scraping', body=json.dumps(message))
    print(" [x] Sent Message")
    connection.close()
