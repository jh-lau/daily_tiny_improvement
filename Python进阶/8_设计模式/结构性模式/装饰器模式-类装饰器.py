"""
  @Author       : liujianhan
  @Date         : 21/1/1 18:42
  @Project      : DailyTinyImprovement
  @FileName     : 装饰器模式-类装饰器.py
  @Description  : Placeholder
"""
import types
from functools import wraps


class Profiled:
    def __init__(self, func):
        wraps(func)(self)
        self.ncalls = 0

    def __call__(self, *args, **kwargs):
        self.ncalls += 1
        return self.__wrapped__(*args, **kwargs)

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)


@Profiled
def add(x, y):
    return x + y


class Spam:
    @Profiled
    def bar(self, x):
        print(self, x)


if __name__ == '__main__':
    add(2, 3)
    add(4, 5)
    print(add.ncalls)

    s = Spam()
    s.bar(1)
    s.bar(2)
    s.bar(3)
    print(Spam.bar.ncalls)
