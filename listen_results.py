# coding: utf-8

import pika
import asyncio
import websockets

async def hello(websocket, path):
    name = await websocket.recv()
    print(f"< {name}")

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='heyling_rabbit', port=5672))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    channel.basic_publish(exchange='', routing_key='hello', body=name)
    print(" [x] Sent '{}'".format(name))
    connection.close()

    greeting = f"Hello {name}!"

    await websocket.send(greeting)
    print(f"> {greeting}")

start_server = websockets.serve(hello, "heyling_websocket", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
