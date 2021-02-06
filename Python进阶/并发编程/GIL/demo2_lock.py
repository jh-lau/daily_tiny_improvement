"""
  @Author       : liujianhan
  @Date         : 20/9/30 21:13
  @Project      : DailyTinyImprovement
  @FileName     : demo2_lock.py
  @Description  : Placeholder
"""
from multiprocessing import Process, Value, Lock

import time


def deposit(money, lock):
    for i in range(100):
        time.sleep(.01)
        lock.acquire()
        money.value += 1
        lock.release()


def withdraw(money, lock):
    for i in range(100):
        time.sleep(.01)
        lock.acquire()
        money.value -= 1
        lock.release()


if __name__ == '__main__':
    money = Value('i', 2000)
    lock = Lock()
    print(money.value)

    d = Process(target=deposit, args=(money, lock))
    w = Process(target=withdraw, args=(money, lock))
    d.start()
    w.start()

    d.join()
    w.join()
    print(money.value)
