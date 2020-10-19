"""
  @Author       : liujianhan
  @Date         : 2020/10/19 11:09
  @Project      : DailyTinyImprovement
  @FileName     : demo10.1_多线程依序打印.py
  @Description  : Placeholder
"""
from concurrent.futures import ThreadPoolExecutor
from threading import Thread

current = 'c'


def print_func():
    global current
    for _ in range(10):
        if current == 'a':
            print('b')
            current = 'b'
        elif current == 'b':
            print('c')
            current = 'c'
        elif current == 'c':
            print('a')
            current = 'a'


if __name__ == '__main__':
    t_list = []
    for _ in range(3):
        t_list.append(Thread(target=print_func))
    for t in t_list:
        t.start()
    for t in t_list:
        t.join()
