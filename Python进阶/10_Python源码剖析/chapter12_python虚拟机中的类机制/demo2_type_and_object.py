"""
  @Author       : liujianhan
  @Date         : 20/10/3 17:47
  @Project      : DailyTinyImprovement
  @FileName     : demo2_type_and_object.py
  @Description  :
"""


def factorial(n, a: int = 8, *, m: int = 8, x: float = 9.):
    """returns n!"""
    return 1 if n < 2 else n * factorial(n - 1)


if __name__ == '__main__':
    print(factorial.__doc__)
    # 函数直接赋予属性，不常见
    factorial.short_description = 'fac'
    print(dir(factorial))
    for p in dir(factorial):
        print(p, '-->', getattr(factorial, p))
    print(type(factorial))
    print('object is instance of:', object.__class__)
    print(type(object))
    print('type is instance of:', type.__class__)
    print('type is kind of:', type.__bases__)
    print('int is instance of:', int.__class__)
    print('int is instance of:', type(int))
    print('int is kind of:', int.__bases__)
    print('dict is instance of:', dict.__class__)
    print('dict is kind of:', dict.__bases__)
