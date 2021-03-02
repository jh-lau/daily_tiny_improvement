"""
  @Author       : liujianhan
  @Date         : 21/3/1 18:55
  @Project      : DailyTinyImprovement
  @FileName     : enum_demo.py
  @Description  : Placeholder
"""
from enum import Enum


class Command(Enum):
    stop = 1
    create = 2
    close = 3


def print_enum(cmd: Enum):
    print(cmd.name)


if __name__ == '__main__':
    print_enum(Command.stop)
    print(isinstance(Command.stop, Enum))
