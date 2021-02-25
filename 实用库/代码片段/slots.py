"""
  @Author       : liujianhan
  @Date         : 21/2/25 15:22
  @Project      : DailyTinyImprovement
  @FileName     : slots.py
  @Description  : Placeholder
"""


class Temp:
    __slots__ = ['name', 'age', 'gender']

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


if __name__ == '__main__':
    t = Temp('joey', 19, 'male')
    t.city = 'Fujian'
