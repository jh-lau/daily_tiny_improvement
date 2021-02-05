"""
  @Author       : liujianhan
  @Date         : 21/1/16 23:48
  @Project      : DailyTinyImprovement
  @FileName     : contextmanager_优雅的异常捕获.py
  @Description  : Placeholder
"""
import contextlib
from typing import Union, Callable
from functools import wraps


class ExternalServiceError:
    pass


def log_error(name, raises):
    pass


class ExternalService:
    def call(self):
        pass


def APIError(error):
    return


@contextlib.contextmanager
def catches(*exceptions, raises: Union[BaseException, Callable[[Exception], BaseException]], log=False):
    exceptions = exceptions or (Exception,)
    try:
        yield
    except exceptions as ex:
        if callable(raises):
            raises = raises(ex)
        if log:
            log_error(__name__, raises)
        raise raises from ex


@catches(ExternalServiceError, raises=APIError('Error calling external service'), log=True)
def service_call():
    external_service = ExternalService()
    external_service.call()


def exception_dec(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            print(e.__class__)
            print(f"something wrong: {e}")

    return decorator


@exception_dec
def exception_handle2():
    try:
        assert 0, f"No valid op"
    except Exception as e:
        raise IndexError('wrong index') from e


@exception_dec
def exception_handle1():
    try:
        raise ValueError
    except Exception as e:
        raise IndexError


@exception_dec
def simple_func():
    # raise TypeError('Wrong type')
    assert 0, f"wrong number"


if __name__ == '__main__':
    # exception_handle2()
    # exception_handle1()
    simple_func()
