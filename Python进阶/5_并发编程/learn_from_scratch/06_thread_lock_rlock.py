"""
  @Author       : liujianhan
  @Date         : 21/1/27 22:29
  @Project      : DailyTinyImprovement
  @FileName     : 06_thread_lock_rlock.py
  @Description  :
  1. 用锁影响性能
  2. 可能产生死锁
  3. 同一个线程里面，连续调用多次acquire的锁：RLock（acquire次数 == release次数）
"""
import dis
import threading
from threading import Lock, RLock


def add(a):
    a = a + 1
    return a


def plus(lock):
    global total
    for i in range(count):
        lock.acquire()
        total += 1
        lock.release()


def sub(lock):
    global total
    for i in range(count):
        lock.acquire()
        total -= 1
        lock.release()


def plus1(_rlock):
    global total
    for i in range(count):
        _rlock.acquire()
        _rlock.acquire()
        total += 1
        _rlock.release()
        _rlock.release()


def sub1(_rlock):
    global total
    for i in range(count):
        _rlock.acquire()
        _rlock.acquire()
        total -= 1
        _rlock.release()
        _rlock.release()


if __name__ == '__main__':
    count = 10000000
    total = 0
    option = 2
    if option == 1:
        lock = Lock()
        t1 = threading.Thread(target=plus, args=(lock, ))
        t2 = threading.Thread(target=sub, args=(lock, ))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
    elif option == 2:
        rlock = RLock()
        t1 = threading.Thread(target=plus1, args=(rlock,))
        t2 = threading.Thread(target=sub1, args=(rlock,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()

    print(total)