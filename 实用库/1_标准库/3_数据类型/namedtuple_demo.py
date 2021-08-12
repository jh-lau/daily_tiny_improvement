"""
  @Author       : Liujianhan
  @Date         : 20/8/9 23:25
  @FileName     : namedtuple_demo.py
  @ProjectName  : DailyTinyImprovement
  @Description  : 定义精简而不可变的数据类型
 """
from collections import namedtuple

grade = namedtuple('grade', ('score', 'weight', 'info'))
scripts = namedtuple('info_level_api', 'exception method task')
level_s = scripts('hello', 'yes', 'task')
print(level_s.exception, level_s.method, level_s.task)


class Person(
    namedtuple('Person', 'id age gender city')
):
    pass


if __name__ == '__main__':
    # g1 = grade([100, 12, 123, 123], .23, 'math')
    # g2 = grade(80, .34, 'physics')
    # print(g1.score)
    # print(g1.weight)

    # print(g1.score.count(123))
    # print(g2.count(.34))

    p = Person(1, 18, 'male', 'Fujian')
    print(p.id, p.age, p.gender, p.city)
