"""
  @Author       : liujianhan
  @Date         : 2021/11/17 18:02
  @Project      : DailyTinyImprovement
  @FileName     : demo.py
  @Description  : Placeholder
"""
from threading import Timer
from time import sleep


def sleep_func():
    s = []
    sleep(1)
    s.append(1)
    print(f'Done: {s}')
    timer = Timer(3, sleep_func)
    timer.start()


if __name__ == '__main__':
    sleep_func()
