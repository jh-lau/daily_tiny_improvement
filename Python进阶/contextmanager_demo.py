"""
  @Author       : liujianhan
  @Date         : 2020/8/11 上午9:59
  @Project      : DailyTinyImprovement
  @FileName     : contextmanager_demo.py
  @Description  : Placeholder
"""
import logging
from contextlib import contextmanager


def my_function():
    logging.debug('some debug data')
    logging.error('error log here')
    logging.debug('more debug data')


@contextmanager
def debug_logging(level):
    logger = logging.getLogger()
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield
    finally:
        logger.setLevel(old_level)


@contextmanager
def log_level(level, name):
    logger = logging.getLogger(name)
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield logger
    finally:
        logger.setLevel(old_level)


if __name__ == '__main__':
    # my_function()

    # with debug_logging(logging.DEBUG):
    #     print('Inside:')
    #     my_function()
    # print('After:')
    # my_function()

    with log_level(logging.DEBUG, 'my-log') as logger:
        logger.debug('This is my message!')
        logging.debug('This will not print')

