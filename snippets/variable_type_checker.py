"""
  @Author       : liujianhan
  @Date         : 2019/12/28 下午2:46
  @Project      : DailyTinyImprovement
  @FileName     : variable_type_checker.py
  @Description  : Placeholder
"""
import inspect
from functools import wraps


def type_checker(func):
    annotations = func.__annotations__
    sig = inspect.signature(func)

    @wraps(func)
    def wrapper(*args, **kwargs):
        bound = sig.bind(*args, **kwargs)
        for k, v in bound.arguments.items():
            if k in annotations:
                assert isinstance(v, annotations[k]), f"Type Error Expected {annotations[k]}"
        return func(*args, **kwargs)

    return wrapper


if __name__ == '__main__':
    @type_checker
    def add(a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a

    print(add(23.3, 2))
