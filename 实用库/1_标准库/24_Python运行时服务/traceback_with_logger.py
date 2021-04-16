"""
  Author: Liujianhan
  Date: 20/1/18 16:59
  FileName: futures_demo.py
  ProjectName: DailyTinyImprovement
 """
import functools
import logging
import os
import traceback
from datetime import datetime


def get_logger(log_name: str = '',
               file_path: str = '',
               file_level=logging.INFO,
               console_level=logging.INFO,
               filemode="w",
               to_screen: bool = True):  # a,追加, w,覆蓋
    log_name = log_name or datetime.now().strftime('%Y%m%d_%H%M')
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


def exception_trace(logger):
    def watcher(fn):
        @functools.wraps(fn)
        def _watcher(*args, **kwargs):
            name = fn.__name__
            try:
                return fn(*args, **kwargs)
            except Exception as e:
                logger.info(f"Exception caught in {name}: {e}")
                logger.info("\n".join([
                    "",
                    " Exception caught ".center(60, "="),
                    traceback.format_exc(),
                    "=" * 60,
                ]))

        return _watcher

    return watcher


@exception_trace(get_logger(filemode='a'))
def inference():
    raise ZeroDivisionError


if __name__ == '__main__':
    inference()
