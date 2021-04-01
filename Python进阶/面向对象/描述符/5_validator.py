"""
  @Author       : liujianhan
  @Date         : 21/4/1 16:31
  @Project      : DailyTinyImprovement
  @FileName     : 5_validator.py
  @Description  : Placeholder
"""
from abc import ABC, abstractmethod


class Validator(ABC):
    def __set_name__(self, owner, name):
        self.private_name = f"_{name}"

    def __get__(self, instance, owner):
        return getattr(instance, self.private_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.private_name, value)

    @abstractmethod
    def validate(self, value):
        pass


class OneOf(Validator):
    def __init__(self, *options):
        self.options = set(options)

    def validate(self, value):
        if value not in self.options:
            raise ValueError(f"Expected {value!r} to be one of {self.options!r}")


class Number(Validator):
    def __init__(self, min_value=None, max_value=None):
        self.min_value = min_value
        self.max_value = max_value

    def validate(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f"Expected {value!r} to be an int or float")
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f"Expected {value!r} to be at least {self.min_value}")
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f"Expected {value!r} to be no more than {self.max_value}")


class String(Validator):
    def __init__(self, min_size=None, max_size=None, predicate=None):
        self.min_size = min_size
        self.max_size = max_size
        self.predicate = predicate

    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError(f"Expected {value!r} to be an str")
        if self.min_size is not None and len(value) < self.min_size:
            raise ValueError(f"Expected {value!r} to be no smaller than {self.min_size}")
        if self.max_size is not None and len(value) > self.max_size:
            raise ValueError(f"Expected {value!r} to be no bigger than {self.max_size}")
        if self.predicate is not None and not self.predicate(value):
            raise ValueError(f"Expected {self.predicate} to be true for {value}")


class Component:
    name = String(min_size=3, max_size=10, predicate=str.isupper)
    kind = OneOf('wood', 'metal', 'plastic')
    quantity = Number(min_value=0)

    def __init__(self, name, kind, quantity):
        self.name = name
        self.kind = kind
        self.quantity = quantity


if __name__ == '__main__':
    # Component('Widget', 'metal', 5)
    # Component("WIDGET", 'metle', 5)
    # Component('WIDGET', 'metal', -5)
    # Component('WIDGET', 'metal', 'V')
    c = Component('WIDGET', 'metal', 5)

