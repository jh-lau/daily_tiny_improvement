"""
  @Author       : liujianhan
  @Date         : 20/10/12 22:38
  @Project      : DailyTinyImprovement
  @FileName     : socket_http.py
  @Description  : Placeholder
"""
import socket
from urllib.parse import urlparse


def get_url(url):
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if not path:
        path = '/'
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, 80))

    client.send(f"GET {path} HTTP/1.1\r\nHost:{host}\r\nConnection:close\r\n\r\n".encode('utf8'))
    data = b''
    while True:
        d = client.recv(1024)
        if d:
            data += d
        else:
            break
    data = data.decode('utf8')
    data = data.split('\r\n\r\n')[1]
    print(data)
    client.close()


if __name__ == '__main__':
    url = 'https://www.baidu.com'
    get_url(url)
