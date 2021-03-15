"""
  @Author       : liujianhan
  @Date         : 21/3/17 15:50
  @Project      : DailyTinyImprovement
  @FileName     : abc_demo.py
  @Description  : Placeholder
"""
from abc import abstractmethod, ABC


class Base(ABC):
    @abstractmethod
    def get_name(self):
        pass


class Person(Base):
    @abstractmethod
    def get_name(self):
        print('get_name')


class Student(Person):
    def get_name(self):
        print('age')


if __name__ == '__main__':
    s = Student()
    s.get_name()
