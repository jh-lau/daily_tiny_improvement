"""
  @Author       : liujianhan
  @Date         : 2020/12/28 14:15
  @Project      : DailyTinyImprovement
  @FileName     : client.py
  @Description  : Placeholder
"""
import socket

obj = socket.socket()
obj.connect(('127.0.0.1', 8001))

while True:
    inp = input('>>>')
    obj.sendall(bytes(inp, encoding='utf-8'))
    ret = str(obj.recv(1024),encoding='utf-8')
    print(ret)

obj.close()