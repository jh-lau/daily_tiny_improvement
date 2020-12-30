"""
  @Author       : Liujianhan
  @Date         : 20/8/11 22:54
  @FileName     : socket_server.py
  @ProjectName  : DailyTinyImprovement
  @Description  : Placeholder
 """

import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8000))
server.listen()


def handle_sock(sock, addr):
    data = sock.recv(1024)
    print('服务端接收：', data.decode('utf8'))
    input_data = input('服务端发送：')
    sock.send(input_data.encode('utf8'))


while True:
    sock, addr = server.accept()
    client_thread = threading.Thread(target=handle_sock, args=(sock, addr))
    client_thread.start()

    # sock.send(f'hello {data}'.encode('utf8'))
    # server.close()
    # sock.close()
