"""
  @Author       : liujianhan
  @Date         : 21/3/31 14:02
  @Project      : DailyTinyImprovement
  @FileName     : iterable_and_iterator.py
  @Description  : Placeholder
"""
from collections.abc import Iterator, Iterable


class B:
    def __next__(self):
        raise StopIteration


class A:
    def __iter__(self):
        return


class C:
    def __iter__(self):
        return

    def __next__(self):
        return


class D(A, B):
    pass


# snippet from torch source code
class Torch:
    def __init__(self):
        self._modules = {}

    def __iter__(self):
        return iter(self._modules.values())

    def forward(self, _input):
        # 借鉴写法
        for module in self:
            _input = module(_input)
        return _input


if __name__ == '__main__':
    for i in [A(), B(), C(), D()]:
        print(i, 'is Iterable: ', isinstance(i, Iterable))
        print(i, 'is Iterator: ', isinstance(i, Iterator))
