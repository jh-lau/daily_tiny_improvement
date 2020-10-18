"""
  @Author       : liujianhan
  @Date         : 2020/10/17 16:27
  @Project      : DailyTinyImprovement
  @FileName     : demo2_frozen_json.py
  @Description  : Placeholder
"""
from demo1_download import load
from collections import abc


class FrozenJSON:
    def __init__(self, mapping):
        self.__data = dict(mapping)

    def __getattr__(self, item):
        if hasattr(self.__data, item):
            print(f"hello, {item}")
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


if __name__ == '__main__':
    raw_feed = load()
    feed = FrozenJSON(raw_feed)
    print(feed.Schedule.speakers[-1].name)
    pass
