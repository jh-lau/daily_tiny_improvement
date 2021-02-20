"""
  @Author       : liujianhan
  @Date         : 21/2/19 11:26
  @Project      : DailyTinyImprovement
  @FileName     : custom_catcher.py
  @Description  : Placeholder
"""
import contextlib
import functools


# 正确写法1
def decorate_check_error(error_enum: int = 1):
    def decorator(func):
        @functools.wraps(func)
        def _check_error(self, *args, **kwargs):
            try:
                func(self, *args, **kwargs)
            except TypeError:
                self.reset()
            except ZeroDivisionError:
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
    def catch_websocket_connection_errors(self):
        try:
            yield
        except TypeError:
            self.reset()
        except ZeroDivisionError:
            self.restart()

    def division_zero(self):
        # 正确写法2的用法
        with self.catch_websocket_connection_errors():
            raise ZeroDivisionError

    def type_error(self):
        with self.catch_websocket_connection_errors():
            raise TypeError

    # @decorate_check_error()
    @catch_websocket_connection_errors()
    def get_info(self):
        raise TypeError

    def reset(self):
        print('reseting...')

    def restart(self):
        print('restarting...')


if __name__ == '__main__':
    t = Temp()
    t.get_info()
