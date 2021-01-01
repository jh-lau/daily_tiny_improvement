"""
  @Author       : Liujianhan
  @Date         : 20/8/11 22:54
  @FileName     : socket_server.py
  @ProjectName  : DailyTinyImprovement
  @Description  : Placeholder
 """

import socketserver
import random


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        conn = self.request
        conn.send('hello world'.encode())
        while True:
            data = conn.recv(1024)
            if data == b'exit':
                break
            print(data.decode())
            conn.send(f"{random.randint(1, 100)}: {data.decode()}".encode())
        conn.close()


if __name__ == '__main__':
    s = socketserver.ThreadingTCPServer(('127.0.0.1', 8000), MyServer)
    s.serve_forever()
