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

response = {
    "intent": "setup",
    "type": "sdk",
    "count": 0,
    "class": {
        "package": "gfootball.env",
        "method": {
            "name": "create_environment",
            "kwargs": {
                "env_name": "academy_empty_goal_close",
                "render": False,
                "representation": "simple115"
            }
        }
    }
}


async def echo(websocket, path):
    async for message in websocket:
        print(f"Receiving: {message}")
        response['count'] += 1
        await websocket.send(json.dumps(response))


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(websockets.serve(echo, 'localhost', 8765))
    asyncio.get_event_loop().run_forever()
