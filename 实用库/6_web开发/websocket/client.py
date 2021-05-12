"""
  @Author       : liujianhan
  @Date         : 21/5/12 10:59
  @Project      : DailyTinyImprovement
  @FileName     : client.py
  @Description  : Placeholder
"""
import websocket


def on_message(wsapp, message):
    print(message)


if __name__ == '__main__':
    ws = websocket.WebSocket()
    ws.connect("ws://echo.websocket.org")
    ws.send("Hello, Servera")
    print(ws.recv())
    ws.close()
