"""
  @Author       : liujianhan
  @Date         : 2020/7/30 上午10:45
  @Project      : DailyTinyImprovement
  @FileName     : student2.py
  @Description  : 避免重复(如student)的属性方法
"""
from functools import partial


def type_property(name, expected_type):
    storage_name = '_' + name

    @property
    def prop(self):
        return getattr(self, storage_name)

    @prop.setter
    def prop(self, value):
        if not isinstance(value, expected_type):
            raise TypeError(f"{name} must be a {expected_type}.")
        setattr(self, storage_name, value)

    return prop


class Student:
    # name = type_property('name', str)
    # age = type_property('age', int)
    Integer = partial(type_property, expected_type=int)
    String = partial(type_property, expected_type=str)
    name = String('name')
    age = Integer('age')

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Score:
    def __init__(self, subject):
        self.name = subject

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if 0 <= value <= 100:
            instance.__dict__[self.name] = value
        else:
            raise ValueError


class Student2:
    # 降低代码重复率，把描述符直接当做代理，本身不存储值，否则出现多个实例共享某个属性值的情况
    math = Score("math")
    chinese = Score("chinese")
    english = Score("english")

    def __init__(self, math, chinese, english):
        self.math = math
        self.chinese = chinese
        self.english = english

    def __repr__(self):
        return "<Student math:{}, chinese:{}, english:{}>".format(self.math, self.chinese, self.english)


if __name__ == '__main__':
    st = Student('joey', 20)
    st.name = 'chandler'
    print(st.name)
    print(st.age)
    s2 = Student2(90, 90, 90)
    print(hasattr(s2, 'math'))
    print(hasattr(s2, 'chinese'))
    print(hasattr(s2, 'english'))
