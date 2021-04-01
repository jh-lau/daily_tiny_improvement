"""
  @Author       : liujianhan
  @Date         : 2020/11/11 18:44
  @Project      : DailyTinyImprovement
  @FileName     : contain_demo.py
  @Description  : Placeholder
"""


class Company:
    def __init__(self, name):
        self.name = name
        self.employee = [name]

    def __contains__(self, item):
        return True if item in self.employee else False


if __name__ == '__main__':
    s = Company('joey')
    print('joe1y' in s)
