"""
  @Author       : Liujianhan
  @Date         : 20/8/2 12:13
  @FileName     : get_logger.py
  @ProjectName  : DailyTinyImprovement
  @Description  : Placeholder
 """
import logging


def set_logger(save_file: str, logging_level: str = 'INFO'):
    logger = logging.getLogger(__name__)
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
    logger = set_logger('test.log')
    logger.info('this is test log1')
    logger.info('this is test log2')
    logger.info('this is test log3')
    logger.warning('this is test log3')