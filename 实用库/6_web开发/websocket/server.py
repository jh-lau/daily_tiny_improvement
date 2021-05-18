"""
  @Author       : liujianhan
  @Date         : 21/5/12 11:23
  @Project      : DailyTinyImprovement
  @FileName     : server.py
  @Description  : Placeholder
"""
import asyncio
import json

import websockets

response1 = {"intent": "setup", "count": 0,"module": "env_sdk.gfootball_sdk","sdk": "GfootballSDK"}


async def echo(websocket, path):
    async for message in websocket:
        print(f"Receiving: {message}")
        # response['count'] += 1
        response = input('->')
        print(json.dumps(response))
        await websocket.send(json.dumps(response))


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(websockets.serve(echo, 'localhost', 8765))
    asyncio.get_event_loop().run_forever()
