"""
  @Author       : liujianhan
  @Date         : 21/2/24 11:34
  @Project      : DailyTinyImprovement
  @FileName     : 捕获顺序.py
  @Description  : Placeholder
"""


class NameError(Exception):
    pass


if __name__ == '__main__':
    try:
        raise NameError("name error")
    except NameError:
        print('name error')
    except Exception as e:
        print('other error', e)
