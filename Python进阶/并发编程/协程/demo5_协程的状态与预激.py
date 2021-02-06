"""
  @Author       : liujianhan
  @Date         : 2020/10/12 18:02
  @Project      : DailyTinyImprovement
  @FileName     : demo5_协程的状态与预激.py
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
        # print(next(my_cor))  # 有了协程装饰器之后这一步就不需要了，必须删除，否则yield执行的位置会往后一个位置
        print(ggs(my_cor))
        print(my_cor.send(14))
        print(my_cor.send(ZeroDivisionError))
        print(ggs(my_cor))
        print(my_cor.send(99))
    except StopIteration:
        print(ggs(my_cor))
    finally:
        print(ggs(my_cor))
