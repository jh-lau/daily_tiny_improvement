"""
  @Author       : liujianhan
  @Date         : 2021/1/6 16:02
  @Project      : DailyTinyImprovement
  @FileName     : client.py
  @Description  : Placeholder
"""
from websocket import create_connection


if __name__ == '__main__':
    url = 'ws://10.20.20.37:8090/combat'
    url = 'ws://10.20.20.24:9903/combat'
    sc = create_connection(url)
    print('we')
    print(sc)
    pass
