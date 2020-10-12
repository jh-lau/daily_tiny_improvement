"""
  @Author       : liujianhan
  @Date         : 2020/10/12 18:02
  @Project      : DailyTinyImprovement
  @FileName     : 协程的状态与预激.py
  @Description  : Placeholder
"""
from inspect import getgeneratorstate as ggs
from functools import wraps


def coroutine(func):
    """
    避免忘记预激协程的装饰器
    :param func:
    :return:
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        gen = func(*args, **kwargs)
        gen.send(None)
        return gen

    return wrapper


@coroutine
def sim_coroutine(a):
    print(f"-> started: a = {a}")
    b = yield a
    print(f"-> Received: b = {b}")
    c = yield a + b
    print(f"-> Received: c = {c}")


if __name__ == '__main__':
    my_cor = sim_coroutine(14)
    try:
        print(ggs(my_cor))
        # print(next(my_cor))
        print(ggs(my_cor))
        print(my_cor.send(14))
        print(ggs(my_cor))
        print(my_cor.send(99))
    except StopIteration:
        print(ggs(my_cor))
