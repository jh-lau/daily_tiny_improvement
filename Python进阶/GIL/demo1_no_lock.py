"""
  @Author       : liujianhan
  @Date         : 20/9/30 21:13
  @Project      : DailyTinyImprovement
  @FileName     : demo1_no_lock.py
  @Description  : Placeholder
"""
from multiprocessing import Process, Value

import time


def deposit(money):
    for i in range(100):
        time.sleep(.01)
        money.value += 1


def withdraw(money):
    for i in range(100):
        time.sleep(.01)
        money.value -= 1


if __name__ == '__main__':
    money = Value('i', 2000)
    print(money.value)

    d = Process(target=deposit, args=(money,))
    w = Process(target=withdraw, args=(money,))
    d.start()
    w.start()

    d.join()
    w.join()
    print(money.value)
