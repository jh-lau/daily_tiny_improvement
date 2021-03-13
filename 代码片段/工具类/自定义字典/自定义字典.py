"""
  @Author       : liujianhan
  @Date         : 2020/9/29 17:56
  @Project      : DailyTinyImprovement
  @FileName     : 自定义字典.py
  @Description  : Placeholder
"""
from collections import UserDict


class Str2Key(UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError
        return self[str(key)]

    def __setitem__(self, key, value):
        self.data[str(key)] = value

    def __contains__(self, item):
        return str(item) in self.data


if __name__ == '__main__':
    t = Str2Key(zip('abc', range(3)))
    t['1'] = 'abc'
    print(t[1])
