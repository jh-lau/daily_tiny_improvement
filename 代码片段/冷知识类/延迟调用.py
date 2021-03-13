"""
  @Author       : liujianhan
  @Date         : 2020/10/9 11:21
  @Project      : DailyTinyImprovement
  @FileName     : 延迟调用.py
  @Description  : Placeholder
"""
cont = __import__('contextlib')


def callback():
    print('B')


if __name__ == '__main__':
    with cont.ExitStack() as stack:
        stack.callback(callback)
        print('C')
        print('A')
