"""
  @Author       : liujianhan
  @Date         : 2020/10/12 17:16
  @Project      : DailyTinyImprovement
  @FileName     : iter的额外用法.py
  @Description  : iter的额外用法：
    iter(iterable) -> iterator
    iter(callable, sentinel) -> iterator
    出现哨符后停止，哨符不会被返回，相当于stopiteration的触发条件
"""
from random import randint


def d6():
    return randint(1, 6)


if __name__ == '__main__':
    d6_iter = iter(d6, 1)
    for index, s in enumerate(d6_iter, start=1):
        print(f"第 {index} 次掷骰子: {s}")
