"""
  @Author       : liujianhan
  @Date         : 21/1/26 22:39
  @Project      : DailyTinyImprovement
  @FileName     : 01_GIL.py
  @Description  : 一个时刻只有一个线程在一个cpu上运行，无法将多个线程映射到多个cpu
  GIL释放规则：运行一定字节码行数或者时间片、系统中断（IO操作等）等
"""
import dis
import threading


def add(a):
    a = a + 1
    return a


def plus():
    global total
    for i in range(count):
        total += 1


def sub():
    global total
    for i in range(count):
        total -= 1


if __name__ == '__main__':
    # print(dis.dis(add))
    count = 1000000
    total = 0
    t1 = threading.Thread(target=plus)
    t2 = threading.Thread(target=sub)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print(total)
