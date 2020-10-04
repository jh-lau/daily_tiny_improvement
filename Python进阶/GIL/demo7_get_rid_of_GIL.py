"""
  @Author       : liujianhan
  @Date         : 20/10/4 23:07
  @Project      : DailyTinyImprovement
  @FileName     : demo7_get_rid_of_GIL.py
  @Description  : 用c重写创建线程
    gcc deadLock.c -shared -o deadLock.so
"""
import threading
from ctypes import *


def f():
    while True:
        pass


if __name__ == '__main__':
    lib = cdll.LoadLibrary('deadLock.so')
    t = threading.Thread(target=lib.DLoop)
    t.start()

    while True:
        pass
