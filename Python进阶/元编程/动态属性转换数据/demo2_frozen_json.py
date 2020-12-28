"""
  @Author       : liujianhan
  @Date         : 2020/10/17 16:27
  @Project      : DailyTinyImprovement
  @FileName     : demo2_frozen_json.py
  @Description  : Placeholder
"""
from demo1_download import load
from collections import abc, UserDict
import keyword as ky


class NewDict(UserDict):
    def __missing__(self, key):
        return f'No such key: {key}'


class FrozenJSON:
    def __init__(self, mapping):
        self.__data = NewDict()
        for key, value in mapping.items():
            if key.isidentifier():
                if ky.iskeyword(key):
                    key += '_'
                self.__data[key] = value
            else:
                raise KeyError(f'Invalid identifier: {key}')

    def __getattr__(self, item):
        if hasattr(self.__data, item):
            return getattr(self.__data, item)
        else:
            return FrozenJSON.build(self.__data[item])

    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj


class NewFrozenJSON:
    def __new__(cls, args):
        if isinstance(args, abc.Mapping):
            return super().__new__(cls)
        elif isinstance(args, abc.MutableSequence):
            return [cls(item) for item in args]
        else:
            return args

    def __init__(self, mapping):
        self.__data = NewDict()
        for key, value in mapping.items():
            if key.isidentifier():
                if ky.iskeyword(key):
                    key += '_'
                self.__data[key] = value
            else:
                raise KeyError(f'Invalid identifier: {key}')

    def __getattr__(self, item):
        if hasattr(self.__data, item):
            return getattr(self.__data, item)
        else:
            return NewFrozenJSON(self.__data[item])


if __name__ == '__main__':
    raw_feed = load()
    raw_feed = {'name': 'jimbo', 'class': 19293, 'a2be': 'or not', 'stick': {'a': 1, 'b': 2}}
    # feed = FrozenJSON(raw_feed)
    feed = NewFrozenJSON(raw_feed)
    print(feed.class_)
    print(feed.a2be)
    print(feed.name)
    print(feed.stick.a)
    print(feed.stick.b)
    print(feed.class__)
    # print(feed.Schedule.speakers[-1].name)
    pass
