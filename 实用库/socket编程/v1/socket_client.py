"""
  @Author       : Liujianhan
  @Date         : 20/8/11 22:53
  @FileName     : socket_client.py
  @ProjectName  : DailyTinyImprovement
  @Description  : Placeholder
 """


import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8000))
while True:
    input_data = input('客户端发送：')
    client.send(input_data.encode('utf8'))
    data = client.recv(1024)
    print('客户端接收：', data.decode('utf8'))
# client.send('hello python.'.encode('utf8'))
# data = client.recv(1024)
# print(data.decode('utf8'))
# client.close()
