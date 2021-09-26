"""
  @Author       : liujianhan
  @Date         : 2020/10/29 11:14
  @Project      : DailyTinyImprovement
  @FileName     : 是否可哈希.py
  @Description  :
"""
from typing import Any


def hashable(obj: Any) -> bool:
    try:
        hash(obj)
        return True
    except TypeError as e:
        return False


if __name__ == '__main__':
    print(hashable([1, 23, 3]))
    print(hashable((1, 2, 3, 4)))
    print(hashable((1, 2, 3, 4, [12, 3])))
    print(hashable((1, 2, 3, 4, {123, 2, 3})))
    print([1, 2, 3] == [1, 2, 3])
