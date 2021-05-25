"""
  @Author       : liujianhan
  @Date         : 21/5/21 16:45
  @Project      : DailyTinyImprovement
  @FileName     : 函数内部获取函数名.py
  @Description  : Placeholder
"""
import inspect


def get_fun_name():
    return inspect.stack()[1][3]


class T:
    def hello(self):
        print(get_fun_name())


def yoyo():
    print(get_fun_name())


if __name__ == '__main__':
    T().hello()
    yoyo()
