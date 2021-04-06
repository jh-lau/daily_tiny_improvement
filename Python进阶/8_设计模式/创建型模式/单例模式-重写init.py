"""
  @Author       : liujianhan
  @Date         : 21/1/1 18:07
  @Project      : DailyTinyImprovement
  @FileName     : 单例模式-重写init.py
  @Description  : Placeholder
"""


class A:
    """
    这种方式重写new实现的单例模式要注意，虽然生成的对象都是同一个，但init会每次都被自动调用。py2这种写法实现的单例模式，
    init不会自动被调用，py3会被自动调用。
    要是init里面成本很大，不希望被自动调用，可以改成另外的方式，参考其他方式的单例模式。
    修改上面这个缺点的重写new方式
    """
    _inst = None

    def __new__(cls, *args, **kwargs):
        if not cls._inst:
            cls._inst = object.__new__(cls)
            cls._inst.__custom_init__(*args, **kwargs)  # 重点在这里。
        return cls._inst

    def __custom_init__(self, identity):  # 这行也是是重点。去掉了__init__方法，init会被自动调用，改成在new里面主动调用。
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
