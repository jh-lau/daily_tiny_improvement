"""
  @Author       : liujianhan
  @Date         : 21/3/27 9:05
  @Project      : DailyTinyImprovement
  @FileName     : 动态调用函数.py
  @Description  : 通过字符串动态调用函数的3种方式
"""


class Temp:
    @staticmethod
    def parse_info():
        print("This is info message")

    @staticmethod
    def parse_warning():
        print("This is warning message")

    @staticmethod
    def parse_error():
        print("This is error message")

    def func_invoker(self, func_name: str):
        func_name = f"parse_{func_name}"
        try:
            getattr(self, func_name)()  # method 3
        except AttributeError:
            print(f"No func with name: {func_name}")


def parse_info():
    print("This is info message")


def parse_warning():
    print("This is warning message")


def parse_error():
    print("This is error message")


def func_invoker(func_name: str):
    func_name = f"parse_{func_name}"
    # eval(func_name)()  # method 1
    globals()[func_name]()  # method 2


if __name__ == '__main__':
    # func_invoker('error')

    t = Temp()
    t.func_invoker('error')
