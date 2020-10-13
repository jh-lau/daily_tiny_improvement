"""
  @Author       : Liujianhan
  @Date         : 20/7/18 23:51
  @FileName     : demo1_yield_from.py
  @ProjectName  : DailyTinyImprovement
  @Description  : Placeholder
 """
from itertools import chain

s1 = [1, 2, 3]
s2 = range(11, 15)
s3 = {'django': 1, 'joey': 2}


def my_chain(*args, **kwargs):
    for iterable in args:
        for value in iterable:
            yield value


def my_chain_v2(*args, **kwargs):
    for iterable in args:
        yield from iterable


if __name__ == '__main__':
    for value in chain(s1, s2, s3):
        print(value)

    for value in my_chain(s1, s2, s3):
        print('my chain', value)

    for value in my_chain_v2(s1, s2, s3):
        print('my chain v2', value)
