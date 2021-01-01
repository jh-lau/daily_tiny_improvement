"""
  @Author       : Liujianhan
  @Date         : 20/8/11 22:54
  @FileName     : socket_server.py
  @ProjectName  : DailyTinyImprovement
  @Description  : Placeholder
 """

import socket
import threading

server = socket.socket()
server.bind(('0.0.0.0', 8000))
server.listen()


def handle_sock(sock, addr):
    data = sock.recv(1024)
    print('服务端接收：', data.decode())
    input_data = input('服务端发送：')
    sock.send(input_data.encode())


if __name__ == '__main__':
    while True:
        # todo
        sock, addr = server.accept()
        client_thread = threading.Thread(target=handle_sock, args=(sock, addr))
        client_thread.start()

        # sock.send(f'hello {data}'.encode('utf8'))
        # server.close()
        # sock.close()
