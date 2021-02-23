"""
  @Author       : liujianhan
  @Date         : 21/2/19 11:26
  @Project      : DailyTinyImprovement
  @FileName     : custom_catcher.py
  @Description  : Placeholder
"""
import contextlib
import functools


class NeedResetError(Exception):
    pass


class NeedFullRestartError(Exception):
    pass


# 正确写法1
def decorate_catch_error(error_enum: int = 1):
    def decorator(func):
        @functools.wraps(func)
        def _check_error(self, *args, **kwargs):
            try:
                return func(self, *args, **kwargs)
            except TypeError as e:
                raise NeedResetError("需要重置") from e
            except ZeroDivisionError as e:
                raise NeedFullRestartError("需要重启") from e

        return _check_error

    return decorator


def decorate_deal_error(error_enum: int = 1):
    def decorator(func):
        @functools.wraps(func)
        def _check_error(self, *args, **kwargs):
            try:
                return func(self, *args, **kwargs)
            except NeedResetError:
                self.reset()
            except NeedFullRestartError:
                self.restart()

        return _check_error

    return decorator


# 待修改写法
@contextlib.contextmanager
def catcher_outside(self):
    try:
        yield
    except TypeError:
        self.reset()
    except ZeroDivisionError:
        self.restart()


class Temp:
    # 正确写法2
    @contextlib.contextmanager
    def deal_runtime_error(self):
        try:
            yield
        except NeedResetError:
            self.reset()
        except NeedFullRestartError:
            self.restart()

    @contextlib.contextmanager
    def catch_runtime_error(self):
        try:
            yield
        except TypeError as e:
            raise NeedResetError("需要重置") from e
        except ZeroDivisionError as e:
            raise NeedFullRestartError("需要重启") from e

    def division_zero(self):
        # 正确写法2的单独用法
        with self.catch_runtime_error():
            raise ZeroDivisionError

    def type_error(self):
        with self.catch_runtime_error():
            raise TypeError

    # 多重异常捕获写法1
    def get_info(self):
        with self.deal_runtime_error():
            with self.catch_runtime_error():
                raise TypeError

    # 多重异常捕获写法2
    @decorate_deal_error()
    @decorate_catch_error()
    def get_name(self):
        raise ZeroDivisionError

    @staticmethod
    def reset():
        print('resetting...')

    @staticmethod
    def restart():
        print('restarting...')


if __name__ == '__main__':
    t = Temp()
    t.get_info()
    t.get_name()
