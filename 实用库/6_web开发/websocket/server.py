"""
  @Author       : liujianhan
  @Date         : 21/5/12 11:23
  @Project      : DailyTinyImprovement
  @FileName     : server.py
  @Description  :
"""
import asyncio
import json

import websockets

intent1 = {"intent": "setup", "module": "env_sdk.gfootball_sdk","sdk": "GfootballSDK"}
intent2 = {"intent": "launch"}
intent3 = {"intent": "step"}
intent4 = {"intent": "close"}


async def echo(websocket, path):
    async for message in websocket:
        print(f"Receiving: {message}")
        response = eval(input('->'))
        await websocket.send(json.dumps(response))


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(websockets.serve(echo, '0.0.0.0', 8765))
    asyncio.get_event_loop().run_forever()
