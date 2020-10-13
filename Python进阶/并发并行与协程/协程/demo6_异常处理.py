"""
  @Author       : liujianhan
  @Date         : 2020/10/13 11:04
  @Project      : DailyTinyImprovement
  @FileName     : demo6_异常处理.py
  @Description  : Placeholder
"""


def co_routine(a):
    while True:
        try:
            x = yield a
            if x:
                x = yield x
        except StopIteration:
            print('igonre this kind exception, continue...')
    # finally:
    #     print('hello coroutine')


if __name__ == '__main__':
    s = co_routine(1)
    s.send(None)
    print(s.send(12))
    print(s.send(13))
    print(s.throw(StopIteration))
    print(s.throw(ZeroDivisionError))
    print(s.send(14))
