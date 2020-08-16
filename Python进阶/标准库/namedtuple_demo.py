"""
  @Author       : Liujianhan
  @Date         : 20/8/9 23:25
  @FileName     : namedtuple_demo.py
  @ProjectName  : DailyTinyImprovement
  @Description  : 定义精简而不可变的数据类型
 """
from collections import namedtuple
from pprint import pprint as print

grade = namedtuple('student', ('score', 'weight'))

if __name__ == '__main__':
   g1 = grade([100, 12, 123, 123], .23)
   g2 = grade(80, .34)
   print(g1.score)
   print(g1.weight)
   print(g1.score.count(123))