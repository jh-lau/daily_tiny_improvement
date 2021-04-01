"""
  @Author       : liujianhan
  @Date         : 21/4/1 15:42
  @Project      : DailyTinyImprovement
  @FileName     : 2_dynamic_lookup.py
  @Description  : Placeholder
"""
import os


class DirectorySize:
    def __get__(self, instance, owner):
        return len(os.listdir(instance.dirname))


class Directory:
    size = DirectorySize()

    def __init__(self, dirname):
        self.dirname = dirname


if __name__ == '__main__':
    s = Directory(r'C:\Users\dataexa\Desktop\projects\DailyTinyImprovement\Python进阶\面向对象')
    g = Directory(r'C:\Users\dataexa\Desktop\projects\DailyTinyImprovement\Python进阶\闭包')
    print(s.size)
    print(g.size)
