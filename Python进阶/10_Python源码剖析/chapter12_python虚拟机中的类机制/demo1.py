"""
  @Author       : liujianhan
  @Date         : 20/10/3 17:40
  @Project      : DailyTinyImprovement
  @FileName     : client.py
  @Description  : Placeholder
"""


class A:
    pass


if __name__ == '__main__':
    a = A()
    # is-kind-of:基类与子类的关系--类之间
    print(A.__bases__)
    print(issubclass(A, object))
    # is-instance-of:实例和类的关系
    print(a.__class__)
    print(type(a))
    print(isinstance(a, A))
