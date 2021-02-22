"""
  @Author       : liujianhan
  @Date         : 2020/10/9 14:56
  @Project      : DailyTinyImprovement
  @FileName     : 异常退出时执行清理程序.py
  @Description  : Placeholder
"""
import atexit


@atexit.register
def clean():
    print('清理相关环境代码')


def test():
    example = {'a': 1, 'b': 2}
    print(example['c'])


if __name__ == '__main__':
    test()
