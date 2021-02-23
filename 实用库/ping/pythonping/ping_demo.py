"""
  @Author       : liujianhan
  @Date         : 21/2/23 11:38
  @Project      : DailyTinyImprovement
  @FileName     : ping_demo.py
  @Description  : Placeholder
"""
from pythonping import ping
import sys


if __name__ == '__main__':
    url = '192.168.3.102'
    try:
        ping(url, verbose=False, timeout=.4)
        print(sys.stdout.readlines())
    except Exception as e:
        print('time out')