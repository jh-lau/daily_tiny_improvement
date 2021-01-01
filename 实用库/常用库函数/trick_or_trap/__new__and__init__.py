"""
  @Author       : liujianhan
  @Date         : 20/10/11 22:43
  @Project      : DailyTinyImprovement
  @FileName     : __new__and__init__.py
  @Description  : Placeholder
"""


class User:
    def __new__(cls, *args, **kwargs):
        print('here new function')
        return super().__new__(cls)

    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == '__main__':
    user = User('joey', 123)
    print(user.name)
    print(user.age)