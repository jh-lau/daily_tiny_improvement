"""
  @Author       : Liujianhan
  @Date         : 20/8/2 12:13
  @FileName     : logger_demo_日志设置.py
  @ProjectName  : DailyTinyImprovement
  @Description  : Placeholder
 """
import logging
import os


def set_logger(logger_name: str, save_file: str, logging_level: str = 'INFO'):
    logger = logging.getLogger(logger_name)
    logging.basicConfig(
        format='%(asctime)s '
               '%(levelname)s '
               '[%(filename)s:%(lineno)d] '
               ':  %(message)s',
        filename=save_file,
        filemode='w',
    )
    logger.setLevel(logging_level)

    return logger


def get_logger(log_name, file_level=logging.FATAL, console_level=logging.FATAL, filemode="w"):  # a,追加, w,覆蓋
    dest_dir = os.path.join(os.path.dirname(__file__)) + "/logs"
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)  # 定义要创建的目录

    log_name = 'logs/' + log_name
    logger = logging.getLogger(log_name)
    logger.setLevel(file_level)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    fileHandler = logging.FileHandler(os.path.join(os.path.dirname(__file__), log_name + '.log'), encoding="utf-8",
                                      mode=filemode)
    fileHandler.setLevel(file_level)
    fileHandler.setFormatter(formatter)

    consoleHandler = logging.StreamHandler()
    consoleHandler.setLevel(console_level)
    consoleHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)
    logger.addHandler(consoleHandler)

    return logger


if __name__ == '__main__':
    logger1 = get_logger('logger1', file_level=logging.INFO, console_level=logging.INFO)
    logger1.info('this is test log1')
    logger1.info('this is test log2')
    logger1.info('this is test log3')
    logger1.warning('this is test log3')
    logger2 = get_logger('logger2', file_level=logging.INFO, console_level=logging.INFO)
    logger2.info('this is test log1 in logger2')
    logger2.info('this is test log2')
    logger2.info('this is test log3')
    logger2.warning('this is test log3')
