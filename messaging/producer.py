import os, json, time

import pika

EXCHANGE = "scraping.results.fx"

def send_message(message):
    conn_params = pika.URLParameters(os.environ.get("CLOUDAMQP_URL"))
    
    connection = pika.BlockingConnection(conn_params)
    channel = connection.channel()

    # channel.queue_declare(queue="")

    # TODO TEMPORARY
    final_message = {
        "timestamp": time.time(),
        "data": message
    }

    channel.basic_publish(exchange=EXCHANGE, routing_key='', body=json.dumps(final_message))
    connection.close()
