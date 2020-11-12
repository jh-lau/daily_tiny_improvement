"""
  @Author       : liujianhan
  @Date         : 2020/11/10 18:52
  @Project      : DailyTinyImprovement
  @FileName     : demo3_实例属性的寻找顺序.py
  @Description  : Placeholder
"""


class Student:
    age = 10
    name = 'joey'

    def __init__(self, age, name):
        self.age = age
        self.name = name


if __name__ == '__main__':
    s = Student(123, 'chandler')
    print(s.name)
    print(s.__dict__)
    print(s.age)
    print(Student.name)
    print(Student.age)
    print(Student.__dict__)
    Student.name = 'seeker'
    Student.age = 100
    print(s.name)
    print(s.age)
