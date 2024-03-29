"""
  @Author       : Liujianhan
  @Date         : 20/8/2 12:13
  @FileName     : logger_demo_日志设置.py
  @ProjectName  : DailyTinyImprovement
  @Description  : Placeholder
 """
import logging
import os
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler


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


def get_logger_rotation(log_path: str,
                        log_name: str,
                        file_level: int = logging.INFO,
                        console_level: int = logging.INFO,
                        when: str = 'D',
                        interval: int = 3,
                        backup_count: int = 1,
                        to_screen: bool = False):
    os.makedirs(log_path, exist_ok=True)
    log_file_path = f'{log_path}/{log_name}.log'
    logger = logging.getLogger(log_file_path)
    logger.setLevel(file_level)
    handler = TimedRotatingFileHandler(log_file_path, when=when,
                                       interval=interval,
                                       backupCount=backup_count,
                                       encoding='utf-8')
    formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    if to_screen:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(console_level)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger


if __name__ == '__main__':
    f = datetime.now().strftime(f'%m%d-%H%M-red')
    for i in range(10):
        logger1 = get_logger_rotation('./logger', f'test_logger_1110_{i}')
        logger1.info('this is test log11')
        logger1.info('this is test log21')
        logger1.info('this is test log31')
        logger1.warning('this is test log31')
    # logger2 = get_logger('logger2', file_level=logging.INFO, console_level=logging.INFO, to_screen=False)
    # logger2.info('this is test log1 in logger2')
    # logger2.info('this is test log2')
    # logger2.info('this is test log3')
    # logger2.debug('debug info')
    # logger2.warning('this is test log3')
