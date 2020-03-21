# coding: utf-8

import pika

def callback(ch, method, properties, body):
    body = body[::-1]
    with open('recieve.log', 'w') as f:
        f.write(body.decode('utf-8'))
    print(" [x] Received %r" % body)

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='heyling_rabbit', port=5672))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_consume(
    queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
connection.close()
