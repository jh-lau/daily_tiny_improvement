"""
  @Author       : liujianhan
  @Date         : 21/1/1 18:11
  @Project      : DailyTinyImprovement
  @FileName     : 单例模式-元类.py
  @Description  : Placeholder
"""


class Singleton(type):
    def __init__(cls, name, bases, dict_):
        super(Singleton, cls).__init__(name, bases, dict_)
        cls.instance = None

    def __call__(cls, *args, **kw):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__call__(*args, **kw)
        return cls.instance


class A(metaclass=Singleton):
    def __init__(self, identity):
        print('执行init')
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
