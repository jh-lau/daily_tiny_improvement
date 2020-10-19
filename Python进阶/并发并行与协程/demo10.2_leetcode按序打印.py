"""
  @Author       : liujianhan
  @Date         : 2020/4/1 上午11:22
  @Project      : leetcode_in_python
  @FileName     : 1114.按序打印.py
  @Description  : 我们提供了一个类：
    public class Foo {
      public void one() { print("one"); }
      public void two() { print("two"); }
      public void three() { print("three"); }
    }
    三个不同的线程将会共用一个 Foo 实例。
    线程 A 将会调用 one() 方法
    线程 B 将会调用 two() 方法
    线程 C 将会调用 three() 方法
    请设计修改程序，以确保 two() 方法在 one() 方法之后被执行，three() 方法在 two() 方法之后被执行。

    输入: [1,2,3]
    输出: "onetwothree"
    解释:有三个线程会被异步启动。输入 [1,2,3] 表示线程 A 将会调用 one() 方法，线程 B 将会调用 two() 方法，线程 C 将会调用 three() 方法。
    正确的输出是 "onetwothree"。

    输入: [1,3,2]
    输出: "onetwothree"
    解释: 输入 [1,3,2] 表示线程 A 将会调用 one() 方法，线程 B 将会调用 three() 方法，线程 C 将会调用 two() 方法。
    正确的输出是 "onetwothree"。
"""
from typing import Callable
import threading
import queue


class Foo1:
    """就相当于先用某些方法卡住执行顺序，然后不断监控目标，直到目标符合条件时才跳出当前断点继续执行后续语句。输出是正确的，
    只是因为没法像threading模块那样很好的监控线程，所以大概率会超时，其他语言或许可以用这种方法AC，但python相对较慢，大约
    只能过30/37的数据。对于单次阻塞来说，运行时间大约是threading模块时间的10-14倍这样，整个程序平均时间差距就会在15-25倍这样。"""
    # 2532ms, 13.9MB
    def __init__(self):
        self.t = 0

    def first(self, print_first: Callable[[], None]) -> None:
        print_first()
        self.t = 1

    def second(self, print_second: Callable[[], None]) -> None:
        while self.t != 1:
            pass
        print_second()
        self.t = 2

    def third(self, print_third: Callable[[], None]) -> None:
        while self.t != 2:
            pass
        print_third()


class Foo2:
    """threading模块里的Condition方法，后面五种的方法也都是调用这个模块和使用不同的方法了，方法就是启动wait_for来阻塞每个函数，
    直到指示self.t为目标值的时候才释放线程，with是配合Condition方法常用的语法糖，主要是替代try语句的。"""
    # 44ms, 13.9MB
    def __init__(self):
        self.c = threading.Condition()
        self.t = 0

    def first(self, print_first: Callable[[], None]) -> None:
        self.res(0, print_first)

    def second(self, print_second: Callable[[], None]) -> None:
        self.res(1, print_second)

    def third(self, print_third: Callable[[], None]) -> None:
        self.res(2, print_third)

    def res(self, val: int, func: Callable[[], None]) -> None:
        with self.c:
            self.c.wait_for(lambda: val == self.t)
            func()
            self.t += 1
            self.c.notify_all()


class Foo3:
    """在这题里面功能都是类似的，就是添加阻塞，然后释放线程，只是类初始化的时候不能包含有参数，所以要写一句acquire进行阻塞，
    调用其他函数的时候按顺序release释放。"""
    # 56ms, 13.9MB
    def __init__(self):
        self.l1 = threading.Lock()
        self.l1.acquire()
        self.l2 = threading.Lock()
        self.l2.acquire()

    def first(self, print_first: Callable[[], None]) -> None:
        print_first()
        self.l1.release()

    def second(self, print_second: Callable[[], None]) -> None:
        # self.l1.acquire()
        # print_second()
        # self.l2.release()

        with self.l1:
            print_second()
            self.l2.release()

    def third(self, print_third: Callable[[], None]) -> None:
        # self.l2.acquire()
        # print_third()

        with self.l2:
            print_third()


class Foo4:
    """和方法三是类似的，不过在类赋值的时候可以带有参数自带阻塞。"""
    # 48ms, 14MB
    def __init__(self):
        self.s1 = threading.Semaphore(0)
        self.s2 = threading.Semaphore(0)

    def first(self, print_first: Callable[[], None]) -> None:
        print_first()
        self.s1.release()

    def second(self, print_second: Callable[[], None]) -> None:
        self.s1.acquire()
        print_second()
        self.s2.release()

    def third(self, print_third: Callable[[], None]) -> None:
        self.s2.acquire()
        print_third()


class Foo5:
    """原理同上，用wait方法作为阻塞，用set来释放线程，默认类赋值就是阻塞的。"""
    # 48ms, 13.9MB
    def __init__(self):
        self.b1 = threading.Event()
        self.b2 = threading.Event()

    def first(self, print_first: Callable[[], None]) -> None:
        print_first()
        self.b1.set()

    def second(self, print_second: Callable[[], None]) -> None:
        self.b1.wait()
        print_second()
        self.b2.set()

    def third(self, print_third: Callable[[], None]) -> None:
        self.b2.wait()
        print_third()


class Foo6:
    """Barrier初始化的时候定义了parties = 2个等待线程，调用完了parties个wait就会释放线程。"""
    # 52ms, 13.8MB
    def __init__(self):
        self.b1 = threading.Barrier(2)
        self.b2 = threading.Barrier(2)

    def first(self, print_first: Callable[[], None]) -> None:
        print_first()
        self.b1.wait()

    def second(self, print_second: Callable[[], None]) -> None:
        self.b1.wait()
        print_second()
        self.b2.wait()

    def third(self, print_third: Callable[[], None]) -> None:
        self.b2.wait()
        print_third()


class Foo7:
    """直接使用多线程专用的阻塞队列，对于队列为空时，get方法就会自动阻塞，直到put使之非空才会释放进程。"""
    # 52ms, 14.1MB
    def __init__(self):
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()

    def first(self, print_first: Callable[[], None]) -> None:
        print_first()
        self.q1.put(0)

    def second(self, print_second: Callable[[], None]) -> None:
        self.q1.get()
        print_second()
        self.q2.put(0)

    def third(self, print_third: Callable[[], None]) -> None:
        self.q2.get()
        print_third()


class Foo8:
    """反过来，对于定容队列来说，如果队列满了，put方法也是阻塞。"""
    # 48ms, 14MB
    def __init__(self):
        self.q1 = queue.Queue(1)
        self.q1.put(0)
        self.q2 = queue.Queue(1)
        self.q2.put(0)

    def first(self, print_first: Callable[[], None]) -> None:
        print_first()
        self.q1.get()

    def second(self, print_second: Callable[[], None]) -> None:
        self.q1.put(0)
        print_second()
        self.q2.get()

    def third(self, print_third: Callable[[], None]) -> None:
        self.q2.put(0)
        print_third()


class Foo9:
    """把三个函数指针，按指定键值存入线程安全的字典，当字典长度为3时，按序输出字典。字典法现在被判不在规定的线程输出，已经不能用了。"""

    def __init__(self):
        self.d = {}

    def first(self, print_first: Callable[[], None]) -> None:
        self.d[0] = print_first
        self.res()

    def second(self, print_second: Callable[[], None]) -> None:
        self.d[1] = print_second
        self.res()

    def third(self, print_third: Callable[[], None]) -> None:
        self.d[2] = print_third
        self.res()

    def res(self) -> None:
        if len(self.d) == 3:
            self.d[0]()
            self.d[1]()
            self.d[2]()
