"""
  @Author       : liujianhan
  @Date         : 21/2/24 14:35
  @Project      : DailyTinyImprovement
  @FileName     : traceback_demo.py
  @Description  :
"""
import functools
import traceback


def watcher(fn):
    @functools.wraps(fn)
    def _watcher(*args, **kwargs):
        name = fn.__name__
        print(f"{name} started")
        try:
            return fn(*args, **kwargs)
        except Exception as e:
            print("\n".join([
                "",
                " Exception caught ".center(60, "="),
                traceback.format_exc(),
                "=" * 60,
            ]))
            print(f"Exception caught in {name}: {e}")
            # raise
        finally:
            print(f"{name} exiting")

    return _watcher


@watcher
def func3():
    try:
        func2()
    except Exception as e:
        print(f"异常栈信息：{traceback.format_exc()}")


@watcher
def func4():
    func2()


def func2():
    func1()


def func1():
    raise TypeError('type error')


if __name__ == '__main__':
    func3()
