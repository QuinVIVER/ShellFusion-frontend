# encoding:utf-8
import asyncio
import websockets
import json

async def echo(websocket,path):
    async for message in websocket:
        with open("./static/data.json","r",encoding="utf-8") as f:
            # data = json.load(f)
            data = f.read()
        await websocket.send(str(data))

asyncio.get_event_loop().run_until_complete(websockets.serve(echo, 'localhost', 8088))
asyncio.get_event_loop().run_forever()
