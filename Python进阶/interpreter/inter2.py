"""
  @Author       : liujianhan
  @Date         : 20/10/2 0:12
  @Project      : DailyTinyImprovement
  @FileName     : inter2.py
  @Description  : Placeholder
"""


def cond():
    x = 3
    if x < 5:
        return 'yes'
    else:
        return 'no'


if __name__ == '__main__':
    print(cond.__code__.co_code)
    print(list(bytearray(cond.__code__.co_code)))
