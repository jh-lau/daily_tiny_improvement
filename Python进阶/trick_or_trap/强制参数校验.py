"""
  @Author       : liujianhan
  @Date         : 2020/10/10 12:04
  @Project      : DailyTinyImprovement
  @FileName     : 强制参数校验.py
  @Description  : Placeholder
"""
import inspect
from functools import wraps


def type_check(func):
    print('running immediately....')
    ann = func.__annotations__
    sig = inspect.signature(func)

    @wraps(func)
    def wrapper(*args, **kwargs):
        bound = sig.bind(*args, **kwargs)
        for k, v in bound.arguments.items():
            if k in ann:
                assert isinstance(v, ann[k]), f'Type Error Expected {ann[k]}'
        return func(*args, **kwargs)

    return wrapper


@type_check
def test(a: int, b: 'int > 0' = 80) -> int:
    return a + b


if __name__ == '__main__':
    pass
    # print(test(1))
    # from dis import dis
    # print(dis(type_check))
    # print(test('1', '3'))
