"""
  @Author       : liujianhan
  @Date         : 2020/10/9 10:56
  @Project      : DailyTinyImprovement
  @FileName     : print_save_test.py
  @Description  : Placeholder
"""


if __name__ == '__main__':
    with open('test.log', mode='w+') as f:
        print('hello pytho123n', file=f, flush=False)
