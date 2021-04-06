"""
  @Author       : liujianhan
  @Date         : 21/1/1 17:55
  @Project      : DailyTinyImprovement
  @FileName     : 单例模式.py
  @Description  : Placeholder
"""


class A:
    """
    # 这种方式重写new实现的单例模式要注意，虽然生成的对象都是同一个，但init会每次都被自动调用。py2这种写法实现的单例模式，init不会自动被调用，py3会被自动调用。
    要是init里面成本很大，不希望每次都被自动调用，可以改成另外的方式，参考其他方式的单例模式。
    """
    _inst = None

    def __new__(cls, identity):
        if not cls._inst:
            cls._inst = object.__new__(cls)
        return cls._inst

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
