"""
  @Author       : liujianhan
  @Date         : 21/4/1 15:05
  @Project      : DailyTinyImprovement
  @FileName     : 1_why_descriptor.py
  @Description  : 属性校验、类型检查
"""


class T:
    """
    可行，但是过于臃肿和逻辑混乱。
    """
    name = None

    @classmethod
    def get_name(cls):
        return cls.name

    @classmethod
    def set_name(cls, val):
        if isinstance(val, str):
            cls.name = val
        else:
            raise TypeError("Name must be a string")


class NameDes:
    def __init__(self, name):
        self.__name = name

    def __get__(self, instance, owner):
        print(f'call __get__ in {NameDes.__name__}')
        return self.__name

    def __set__(self, instance, value):
        print(f'call __set__ in {NameDes.__name__}')
        if isinstance(value, str):
            self.__name = value
        else:
            raise TypeError("Name must be a string")


class NewT:
    name = NameDes('joey')

    def __init__(self, name):
        # self.name = name
        pass


if __name__ == '__main__':
    t = NewT('amanda')
    print(t.name, '\n')
    t.name = 'ross'
