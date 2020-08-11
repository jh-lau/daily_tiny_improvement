"""
  @Author       : liujianhan
  @Date         : 2020/8/11 上午10:43
  @Project      : DailyTinyImprovement
  @FileName     : getattr_demo.py
  @Description  : Placeholder
"""


class Test:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 访问的属性不存在时被调用
    def __getattr__(self, item):
        print(f'No attributes:{item} found in this class.')

    # 每次属性访问都会调用；注意调用object方法，否则会导致无限递归错误
    def __getattribute__(self, item):
        super().__getattribute__(item)
        print(f'{item} attribute is invoked')

    # 注意调用object方法，否则会导致无限递归错误
    def __setattr__(self, attr, value):
        super().__setattr__(attr, value)
        print(f'{attr} attribute has been set to {value}')


if __name__ == '__main__':
    t = Test('joey', 18)
    print(t.age)
    print(t.st)
    t.age = 89