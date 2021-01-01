"""
  @Author       : liujianhan
  @Date         : 21/1/1 18:42
  @Project      : DailyTinyImprovement
  @FileName     : 装饰器模式.py
  @Description  : Placeholder
"""


class Foo:
    def f1(self):
        print("original f1")

    def f2(self):
        print("original f2")


class Foo_decorator:
    def __init__(self, decoratee):
        self._decoratee = decoratee

    def f1(self):
        print("before run f1")
        self._decoratee.f1()
        print("after run f1")

    def __getattr__(self, name):
        return getattr(self._decoratee, name)


if __name__ == '__main__':
    u = Foo()
    v = Foo_decorator(u)
    v.f1()
    v.f2()