"""
  @Author       : liujianhan
  @Date         : 21/2/19 11:26
  @Project      : DailyTinyImprovement
  @FileName     : custom_catcher.py
  @Description  : Placeholder
"""
import contextlib
import functools


def decorate_check_error(error_enum: int = 1):
    def decorator(func):
        @functools.wraps(func)
        def _check_error(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except TypeError:
                print('type error')
            except ZeroDivisionError:
                print('zero error')

        return _check_error

    return decorator


class Temp:
    @contextlib.contextmanager
    def catch_websocket_connection_errors(self):
        try:
            yield
        except TypeError:
            self.reset()
        except ZeroDivisionError:
            self.restart()

    def division_zero(self):
        with self.catch_websocket_connection_errors():
            raise ZeroDivisionError

    def type_error(self):
        with self.catch_websocket_connection_errors():
            raise TypeError

    def reset(self):
        print('reseting...')

    def restart(self):
        print('restarting...')


if __name__ == '__main__':
    t = Temp()
    t.division_zero()
    t.type_error()
