"""
  @Author       : Liujianhan
  @Date         : 20/8/11 22:53
  @FileName     : socket_client.py
  @ProjectName  : DailyTinyImprovement
  @Description  : Placeholder
 """


import socket

if __name__ == '__main__':
    client = socket.socket()
    client.connect(('127.0.0.1', 8000))
    while True:
        input_data = input('客户端发送：')
        client.send(input_data.encode())
        data = client.recv(1024)
        print('客户端接收：', data.decode())
    # client.send('hello python.'.encode('utf8'))
    # data = client.recv(1024)
    # print(data.decode('utf8'))
    # client.close()
