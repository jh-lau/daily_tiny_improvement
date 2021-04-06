"""
  @Author       : liujianhan
  @Date         : 21/3/23 9:36
  @Project      : DailyTinyImprovement
  @FileName     : 展开嵌套的序列.py
  @Description  : Placeholder
"""
from collections import Iterable


def flatten(items, ignore_types=(bytes, str)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x


def flatten_for(items, ignore_types=(bytes, str)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            for i in flatten(x):
                yield i
        else:
            yield x


if __name__ == '__main__':
    item_list = [1, 2, [3, 4, [5, 6], 7], 8]
    # item_list = ['Dave', 'Paula', ['Thomas', 'Lewis']]
    print([x for x in flatten([item_list])])
    print([x for x in flatten_for([item_list])])
