"""
  @Author       : liujianhan
  @Date         : 2020/10/13 11:33
  @Project      : DailyTinyImprovement
  @FileName     : demo7_获取协程返回值.py
  @Description  : python3.3之前协程不可以有返回值return句法，否则会报句法错
  yield from结构会在内部自动捕获StopIteration异常，并将异常的属性值返回
"""
from collections import namedtuple

Result = namedtuple('Result', 'count average')


def co_averager():
    total = 0.
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total / count
    return Result(count, average)


if __name__ == '__main__':
    s = co_averager()
    s.send(None)
    s.send(10)
    s.send(11)
    s.send(12)
    s.send(13)
    try:
        s.send(None)
    except StopIteration as exe:
        result = exe.value
        print(result.count)
        print(result.average)
