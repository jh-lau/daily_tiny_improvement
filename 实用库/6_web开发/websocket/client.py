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
    sock = websocket.create_connection('ws://localhost:8765')
    while True:
        sock.send('start')
        print(sock.recv())
