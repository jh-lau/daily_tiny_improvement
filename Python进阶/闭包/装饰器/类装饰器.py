"""
  @Author       : liujianhan
  @Date         : 2020/10/9 15:17
  @Project      : DailyTinyImprovement
  @FileName     : 类装饰器.py
  @Description  : Placeholder
"""


class Logger:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"[INFO]: the function {self.func.__name__}() is running...")
        return self.func(*args, **kwargs)


class LoggerNew:
    def __init__(self, level="INFO"):
        self.level = level

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print(f"[{self.level}]: the function {func.__name__}() is running...")
            func(*args, **kwargs)
        return wrapper


@LoggerNew(level='WARNING')
def say(something):
    print(f"say {something}!")


if __name__ == '__main__':
    say('hello world')
