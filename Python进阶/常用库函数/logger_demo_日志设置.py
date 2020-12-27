"""
  @Author       : Liujianhan
  @Date         : 20/8/2 12:13
  @FileName     : logger_demo_日志设置.py
  @ProjectName  : DailyTinyImprovement
  @Description  : Placeholder
 """
import logging


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


if __name__ == '__main__':
    logger1 = set_logger('logger1', 'test11.log')
    logger1.info('this is test log1')
    logger1.info('this is test log2')
    logger1.info('this is test log3')
    logger1.warning('this is test log3')
    logger2 = set_logger('logger2', 'test2.log')
    logger2.info('this is test log1 in logger2')
    logger2.info('this is test log2')
    logger2.info('this is test log3')
    logger2.warning('this is test log3')