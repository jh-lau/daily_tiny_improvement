"""
  @Author       : liujianhan
  @Date         : 21/1/1 18:42
  @Project      : DailyTinyImprovement
  @FileName     : 装饰器模式-函数装饰器.py
  @Description  : Placeholder
"""
import time
from functools import wraps


def time_this(func):
    """
    Decorator that reports the execution time.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result

    return wrapper


@time_this
def fun():
    time.sleep(3)
    return 1


if __name__ == '__main__':
    fun()
