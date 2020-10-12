"""
  @Author       : liujianhan
  @Date         : 2020/10/12 17:03
  @Project      : DailyTinyImprovement
  @FileName     : yield_from_demo.py
  @Description  : Placeholder
"""
from itertools import *


def new_chain(*iterable):
    for it in iterable:
        for i in it:
            yield i


def yield_chain(*iterable):
    for it in iterable:
        yield from it


if __name__ == '__main__':
    a = 'abc'
    b = range(3)
    # 自行实现的chain
    print(list(new_chain(a, b)))
    # 标准库的chain
    print(list(chain(a, b)))
    # yield from的用法
    print(list(yield_chain(a, b)))
