"""
  @Author       : liujianhan
  @Date         : 2020/10/9 12:45
  @Project      : DailyTinyImprovement
  @FileName     : 单例模式.py
  @Description  : 使用锁保证多线程中的单例机制正常工作
"""
import time
import threading


def synchronized(func):
    func.__lock__ = threading.Lock()

    def lock_func(*args, **kwargs):
        with func.__lock__:
            return func(*args, **kwargs)

    return lock_func


# 使用__new__实现单例模式
class User:
    @synchronized
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            time.sleep(.1)
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, name):
        self.name = name


def task():
    u = User('chandler')
    print(u)


# 使用装饰器实现单例模式
instances = {}


def singleton(cls):
    def get_instance(*args, **kwargs):
        cls_name = cls.__name__
        if cls_name not in instances:
            instance = cls(*args, **kwargs)
            instances[cls_name] = instance
        return instances[cls_name]

    return get_instance


# 使用元类实现单例模式
class MetaSingleton(type):
    def __call__(cls, *args, **kwargs):
        print("cls:{}".format(cls.__name__))
        if not hasattr(cls, "_instance"):
            cls._instance = type.__call__(cls, *args, **kwargs)
        return cls._instance


if __name__ == '__main__':
    # print(dir(User))
    # u1 = User('liujianhan')
    # print(dir(User))
    # u1.age = 128
    # u2 = User('joey')
    # print(u1.age)
    # print(u1.name)
    # print(u2.age)
    # print(u2.name)
    # print(u1 is u2)
    # 单例线程不安全，加锁使其线程安全
    for i in range(20):
        t = threading.Thread(target=task)
        t.start()
