"""
  @Author       : Liujianhan
  @Date         : 20/8/11 21:29
  @FileName     : closure_demo.py
  @ProjectName  : DailyTinyImprovement
  @Description  : 闭包
  1. 嵌套函数
  2. 闭包引用外部变量
  3. 闭包返回
 """
from dis import dis


def outside(x):
    def closure(y):
        result = (x - y) / (x + y)
        return result

    return closure


def make_average():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return averager


if __name__ == '__main__':
    s = outside(10)
    print(s(5))
    avg = make_average()
    print(avg(10))
    print(avg(11))
    print(avg(12))
    # __code__：编译后的定义体
    for s in dir(avg.__code__):
        if not s.startswith('__'):
            print(f"{s}: {getattr(avg.__code__, s)}")
    print(avg.__closure__)
    print(avg.__closure__[0].cell_contents)