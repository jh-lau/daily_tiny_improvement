"""
  @Author       : liujianhan
  @Date         : 2020/7/30 上午9:28
  @Project      : DailyTinyImprovement
  @FileName     : student.py
  @Description  : 避免写这种过于臃肿的代码
"""


class Student:
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        if isinstance(name, str):
            self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age: int):
        if isinstance(age, int) and age > 0:
            self.__age = age


if __name__ == '__main__':
    st = Student('liujianhan', 12)
    st.name = 123
    st.age = -1
    print(st.name)
    print(st.age)
