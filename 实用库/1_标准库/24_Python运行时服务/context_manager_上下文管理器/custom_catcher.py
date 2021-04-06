"""
  @Author       : liujianhan
  @Date         : 21/2/19 11:26
  @Project      : DailyTinyImprovement
  @FileName     : custom_catcher.py
  @Description  : Placeholder
"""
import contextlib
import functools
import logging
import os


def get_logger(log_name: str,
               file_path: str = '',
               file_level=logging.INFO,
               console_level=logging.INFO,
               filemode="w",
               to_screen: bool = True):  # a,追加, w,覆蓋
    file_path = file_path or os.path.join(os.path.dirname(__file__))
    dest_dir = file_path + "/log"
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)  # 定义要创建的目录

    # log_name = 'log/' + log_name
    logger = logging.getLogger(log_name)
    # 此处设定等级后，后续的handler再设等级只有比此等级高才有效，否则无效，如此处为INFO，后续的DEBUG将无效
    logger.setLevel(file_level)

    formatter = logging.Formatter('%(asctime)s '
                                  '%(levelname)s '
                                  '[%(filename)s:%(lineno)d:%(funcName)s:%(threadName)s] '
                                  ': %(message)s')

    file_handler = logging.FileHandler(os.path.join(dest_dir, log_name + '.log'), encoding="utf-8",
                                       mode=filemode)
    file_handler.setLevel(file_level)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    if to_screen:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(console_level)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger


class NeedResetError(Exception):
    pass


class NeedFullRestartError(Exception):
    pass


# 正确写法1
def decorate_catch_error(logger):
    def decorator(func):
        @functools.wraps(func)
        def _check_error(self, *args, **kwargs):
            try:
                return func(self, *args, **kwargs)
            except TypeError as e:
                logger.info(f"get exception: {e}")
                raise NeedResetError("需要重置") from e
            except ZeroDivisionError as e:
                logger.info(f"get exception: {e}")
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
                return '1'
            except NeedFullRestartError:
                self.restart()
                return '12'

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
    logger = get_logger('test_logger')

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
    @decorate_catch_error(logger)
    def get_name(self, a):
        if a:
            return 'yes'
        else:
            raise ZeroDivisionError

    @staticmethod
    def reset():
        print('resetting....')

    @staticmethod
    def restart():
        print('restarting....')


class TempSub(Temp):
    def get_name(self, a):
        if a:
            return 'in sub class'
        else:
            raise ZeroDivisionError


if __name__ == '__main__':
    t = TempSub()
    print(t.get_name(''))
