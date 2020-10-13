"""
  @Author       : liujianhan
  @Date         : 20/9/30 21:13
  @Project      : DailyTinyImprovement
  @FileName     : demo2_lock.py
  @Description  : Placeholder
"""
from threading import Thread, Lock
import time

money = 2000


def deposit(lock, with_lock=True):
    global money
    for i in range(100):
        time.sleep(.01)
        if with_lock:
            lock.acquire()
            money += 1
            lock.release()
        else:
            money += 1


def withdraw(lock, with_lock=True):
    global money
    for i in range(100):
        time.sleep(.01)
        if with_lock:
            lock.acquire()
            money -= 1
            lock.release()
        else:
            money -= 1


if __name__ == '__main__':
    for _ in range(100):
        lock = Lock()
        with_lock = False
        print(f"{_}: {money}")

        d = Thread(target=deposit, args=(lock, with_lock))
        w = Thread(target=withdraw, args=(lock, with_lock))
        d.start()
        w.start()

        d.join()
        w.join()
        print(f"{_}: {money}")
