"""
  @Author       : liujianhan
  @Date         : 2020/11/11 9:54
  @Project      : DailyTinyImprovement
  @FileName     : test1.py
  @Description  : Placeholder
"""


class Student:
    def __init__(self, age: int, name: str):
        self.age = age
        self.name = name


if __name__ == '__main__':
    s: Student = Student(31, 'joey')
    t: int = 12
    f: float = 123.
    print(s.age, s.name)
    print(t)
    print(f)