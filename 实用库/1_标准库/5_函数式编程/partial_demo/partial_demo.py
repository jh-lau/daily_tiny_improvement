"""
  @Author       : liujianhan
  @Date         : 2020/7/30 下午2:41
  @Project      : DailyTinyImprovement
  @FileName     : partial_demo.py
  @Description  : 偏函数
"""
from functools import partial


def add(default, *, a, b, c, d):
    return sum([default, a, b, c, d])


if __name__ == '__main__':
    print(add(1, a=1, b=2, c=3, d=4))
    add_100 = partial(add, b=100)
    print(add_100(2, c=2, a=3, d=4))
    base_16 = partial(int, base=16)
    print(base_16('123'))
