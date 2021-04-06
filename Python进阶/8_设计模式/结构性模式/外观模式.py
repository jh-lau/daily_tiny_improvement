"""
  @Author       : liujianhan
  @Date         : 21/1/1 18:35
  @Project      : DailyTinyImprovement
  @FileName     : 外观模式.py
  @Description  : Placeholder
"""


class A:
    def run(self):
        print('A run')

    def jump(self):
        print('A jump')


class B:
    def run(self):
        print('B run')

    def jump(self):
        print('B jump')


class C:
    def run(self):
        print('C run')

    def jump(self):
        print('C jump')


class Facade:
    def __init__(self):
        self.a = A()
        self.b = B()
        self.c = C()

    def run(self):
        for item in ('a', 'b', 'c'):
            getattr(self, item).run()

    def jump(self):
        for item in ('a', 'b', 'c'):
            getattr(self, item).jump()


if __name__ == '__main__':
    facade = Facade()
    facade.run()
    facade.jump()
