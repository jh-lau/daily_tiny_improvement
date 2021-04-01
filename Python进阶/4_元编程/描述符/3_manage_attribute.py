"""
  @Author       : liujianhan
  @Date         : 21/4/1 15:57
  @Project      : DailyTinyImprovement
  @FileName     : 3_manage_attribute.py
  @Description  : Placeholder
"""
import logging

logging.basicConfig(level=logging.INFO)


class LoggedAgeAccess:
    def __get__(self, instance, owner):
        value = instance._age
        logging.info(f"Accessing age giving {value}")
        return value

    def __set__(self, instance, value):
        logging.info(f"Updating age to {value}")
        instance._age = value


class Person:
    age = LoggedAgeAccess()

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1


if __name__ == '__main__':
    joey = Person('joey', 30)
    ross = Person('ross', 32)
    joey.age
    joey.birthday()