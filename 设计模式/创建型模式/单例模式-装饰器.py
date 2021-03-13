"""
  @Author       : liujianhan
  @Date         : 21/1/1 18:07
  @Project      : DailyTinyImprovement
  @FileName     : 单例模式-装饰器.py
  @Description  : Placeholder
"""
import threading
from functools import wraps


def singleton(cls):
    """
    单例模式装饰器,新加入线程锁，更牢固的单例模式，主要解决多线程如100线程同时实例化情况下可能会出现三例四例的情况,实测。
    """
    _instance = {}
    singleton.__lock = threading.Lock()  # 这里直接演示了线程安全版单例模式

    @wraps(cls)
    def _singleton(*args, **kwargs):
        with singleton.__lock:
            if cls not in _instance:
                _instance[cls] = cls(*args, **kwargs)
            return _instance[cls]

    return _singleton


@singleton
class A:
    def __init__(self, identity):
        self.identity = identity

    def eat(self):
        print(f'{self.identity} 吃饭')


if __name__ == '__main__':
    a1 = A('001')
    a2 = A('001')
    print(a1 == a2)
    a1.eat()
    a2.eat()
    a3 = A('003')
    print(a1 == a3)
    a3.eat()
