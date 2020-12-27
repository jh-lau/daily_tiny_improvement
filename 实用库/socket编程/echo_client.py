"""
  @Author       : liujianhan
  @Date         : 20/12/27 21:21
  @Project      : DailyTinyImprovement
  @FileName     : echo_client.py
  @Description  : Placeholder
"""
import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello world')
    data = s.recv(1024)

print('Received', repr(data))