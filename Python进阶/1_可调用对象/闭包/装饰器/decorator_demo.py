"""
  @Author       : Liujianhan
  @Date         : 20/8/11 21:29
  @FileName     : decorator_demo.py
  @ProjectName  : DailyTinyImprovement
  @Description  : 装饰器的特性：
  1.将被装饰函数变成另一个函数
  2.在被装饰的函数定义之后立即运行
 """
from functools import wraps
from functools import singledispatch


def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"{func.__name__}({args}, {kwargs}) -> {result}")
        return result

    return wrapper


def say_hello(country):
    def wrapper(func):
        @wraps(func)
        def deco(*args, **kwargs):
            if country == 'china':
                print('你好')
            if country == 'america':
                print('Hello')
            else:
                return
            func(*args, **kwargs)

        return deco

    return wrapper


@trace
def fibonacci(n):
    if n in (0, 1):
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


@say_hello('china')
def xiaoming():
    pass


@say_hello('america')
def joey():
    pass


if __name__ == '__main__':
    fibonacci(4)
    xiaoming()
    joey()
    # 相当于下面的写法
    say_hello('china')(xiaoming)()
    say_hello('america')(joey)()
