# coding: utf-8

import asyncio
import websockets

from flask import Flask, request

app = Flask(__name__)

async def hello(name):
    uri = "ws://heyling_websocket:8765"
    async with websockets.connect(uri) as websocket:

        await websocket.send(name)

@app.route('/')
def server():
    name = request.args.get("name", "World")
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    asyncio.get_event_loop().run_until_complete(hello(name))
    with open('recieve.log', 'r') as f:
        res = f.read()
    return f'Hello, {res}!'
