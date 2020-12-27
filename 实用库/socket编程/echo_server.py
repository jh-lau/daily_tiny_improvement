"""
  @Author       : liujianhan
  @Date         : 20/12/27 21:14
  @Project      : DailyTinyImprovement
  @FileName     : echo_server.py
  @Description  : https://keelii.com/2018/09/24/socket-programming-in-python/
"""
import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by: ', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
