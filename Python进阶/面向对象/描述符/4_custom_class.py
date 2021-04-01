"""
  @Author       : liujianhan
  @Date         : 21/4/1 16:03
  @Project      : DailyTinyImprovement
  @FileName     : 4_custom_class.py
  @Description  : Placeholder
"""
import logging

logging.basicConfig(level=logging.INFO)


class LoggedAccess:
    def __set_name__(self, owner, name):
        """
        owner 是使用描述器的类，name 是分配给描述器的类变量名。
        :param owner:
        :param name:
        :return:
        """
        self.public_name = name
        self.private_name = f"_{name}"

    def __get__(self, instance, owner):
        value = getattr(instance, self.private_name)
        logging.info(f"Accessing {self.public_name} giving {value}")
        return value

    def __set__(self, instance, value):
        logging.info(f"Updating {self.public_name} to {value}")
        setattr(instance, self.private_name, value)


class Person:
    age = LoggedAccess()
    name = LoggedAccess()

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1


if __name__ == '__main__':
    ross = Person('ross', 12)
    ross.birthday()
