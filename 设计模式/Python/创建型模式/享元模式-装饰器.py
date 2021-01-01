"""
  @Author       : liujianhan
  @Date         : 21/1/1 18:11
  @Project      : DailyTinyImprovement
  @FileName     : 享元模式-装饰器.py
  @Description  : Placeholder
"""
from functools import wraps


def flyweight(cls):
    _instance = {}

    def _make_arguments_to_key(args, kwds):
        key = args
        if kwds:
            sorted_items = sorted(kwds.items())
            for item in sorted_items:
                key += item
        return key

    @wraps(cls)
    def _flyweight(*args, **kwargs):
        cache_key = f'{cls}_{_make_arguments_to_key(args, kwargs)}'
        if cache_key not in _instance:
            _instance[cache_key] = cls(*args, **kwargs)
        return _instance[cache_key]

    return _flyweight


@flyweight
class A:
    def __init__(self, identity):
        self.identity = identity

    def eat(self):
        print(f'{self.identity} 吃饭')


if __name__ == '__main__':
    a1 = A('001')
    a2 = A('001')
    print(a1 == a2)
    a1.eat()
    a2.eat()
    a3 = A('003')
    print(a1 == a3)
    a3.eat()
