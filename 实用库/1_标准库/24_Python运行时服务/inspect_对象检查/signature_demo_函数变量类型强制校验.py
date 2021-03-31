"""
  @Author       : liujianhan
  @Date         : 2019/12/28 下午2:46
  @Project      : DailyTinyImprovement
  @FileName     : signature_demo_函数变量类型强制校验.py
  @Description  : 强制参数校验
"""
from functools import wraps
from inspect import signature


def type_checker(func):
    annotations = func.__annotations__
    sig = signature(func)

    @wraps(func)
    def wrapper(*args, **kwargs):
        bound = sig.bind(*args, **kwargs)
        for k, v in bound.arguments.items():
            if k in annotations:
                assert isinstance(v, annotations[k]), f"Type Error Expected {annotations[k]}"
        return func(*args, **kwargs)

    return wrapper


def type_assert(*ty_args, **ty_kwargs):
    def decorate(func):
        # If in optimized mode, disable type checking
        if not __debug__:
            return func

        # Map function argument names to supplied types
        sig = signature(func)
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)
            # Enforce type assertions across supplied arguments
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError(
                            'Argument {} must be {}'.format(name, bound_types[name])
                        )
            return func(*args, **kwargs)

        return wrapper

    return decorate


if __name__ == '__main__':
    @type_assert(int, int)
    def add(a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a


    print(add(23, 2))
    print(add(2,34))
