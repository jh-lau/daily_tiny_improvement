"""
  @Author       : liujianhan
  @Date         : 2020/7/30 下午2:41
  @Project      : DailyTinyImprovement
  @FileName     : partial_demo.py
  @Description  : Placeholder
"""
from functools import partial


def add(a, b, c, d):
    return sum([a, b, c, d])


if __name__ == '__main__':
    print(add(1, 2, 3, 4))
    add_100 = partial(add, 100)
    print(add_100(2, 3, 4))
    base_16 = partial(int, base=16)
    print(base_16('123'))
