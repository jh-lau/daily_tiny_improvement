"""
  @Author       : liujianhan
  @Date         : 20/9/30 21:13
  @Project      : DailyTinyImprovement
  @FileName     : demo9_多进程多线程加锁区别.py
  @Description  : Placeholder
"""
from multiprocessing import Process, Value, Lock
from threading import Thread

import time


def deposit(num, money, lock=None, mode=1):
    if lock:
        if mode == 1:
            for i in range(num):
                lock.acquire()
                money.value += 1
                lock.release()
        else:
            tmp = 0
            for i in range(num):
                tmp += i
            lock.acquire()
            money.value += tmp
            lock.release()
    else:
        for i in range(num):
            # time.sleep(.01)
            money.value += 1


def withdraw(num, money, lock=None, mode=1):
    if lock:
        if mode == 1:
            for i in range(num):
                lock.acquire()
                money.value -= 1
                lock.release()
        else:
            tmp = 0
            for i in range(num):
                tmp += i
            lock.acquire()
            money.value -= tmp
            lock.release()
    else:
        for i in range(num):
            # time.sleep(.01)
            money.value -= 1


if __name__ == '__main__':
    for option in range(1, 8):
        money = Value('i', 2000)
        num = 1000_000
        lock = Lock()
        print(money.value)
        # option = 5
        if option == 1:
            t1 = time.time()
            deposit(num, money)
            withdraw(num, money)
            print(f"Time costs in sequential: {time.time() - t1:.2f}s, result: {money.value}")

        elif option == 2:
            t1 = time.time()
            d = Thread(target=deposit, args=(num, money,))
            w = Thread(target=withdraw, args=(num, money,))
            d.start()
            w.start()

            d.join()
            w.join()
            print(f"Time costs without lock[Multi-thread]: {time.time() - t1:.2f}s, result: {money.value}")

        elif option == 3:
            t1 = time.time()
            d = Process(target=deposit, args=(num, money,))
            w = Process(target=withdraw, args=(num, money,))
            d.start()
            w.start()

            d.join()
            w.join()
            print(f"Time costs without lock[Multi-process]: {time.time() - t1:.2f}s, result: {money.value}")

        elif option == 4:
            t1 = time.time()
            d = Process(target=deposit, args=(num, money, lock))
            w = Process(target=withdraw, args=(num, money, lock))
            d.start()
            w.start()

            d.join()
            w.join()
            print(f"Time costs with lock inside for loop[Multi-process]: {time.time() - t1:.2f}s, result: {money.value}")

        elif option == 5:
            t1 = time.time()
            d = Process(target=deposit, args=(num, money, lock, 0))
            w = Process(target=withdraw, args=(num, money, lock, 0))
            d.start()
            w.start()

            d.join()
            w.join()
            print(f"Time costs with lock outside for loop[Multi-process]: {time.time() - t1:.2f}s, result: {money.value}")

        elif option == 6:
            t1 = time.time()
            d = Thread(target=deposit, args=(num, money, lock))
            w = Thread(target=withdraw, args=(num, money, lock))
            d.start()
            w.start()

            d.join()
            w.join()
            print(f"Time costs with lock outside for loop[Multi-thread]: {time.time() - t1:.2f}s, result: {money.value}")

        elif option == 7:
            t1 = time.time()
            d = Thread(target=deposit, args=(num, money, lock, 0))
            w = Thread(target=withdraw, args=(num, money, lock, 0))
            d.start()
            w.start()

            d.join()
            w.join()
            print(f"Time costs with lock outside for loop[Multi-thread]: {time.time() - t1:.2f}s, result: {money.value}")