"""
  @Author       : liujianhan
  @Date         : 20/10/27 23:28
  @Project      : DailyTinyImprovement
  @FileName     : module_1.py
  @Description  : 参数类型校验
"""
from operator import sub


class Test:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def adder(a, b):
    return sum([a, b])


def substracter(a: int, b: int) -> int:
    return sub(a, b)


if __name__ == '__main__':
    print(adder(1.2, 1.2))
    print(substracter(1.2, 1.2))
