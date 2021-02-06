"""
  @Author       : Liujianhan
  @Date         : 20/8/10 22:59
  @FileName     : itertools_demo.py
  @ProjectName  : DailyTinyImprovement
  @Description  : Placeholder
 """
from itertools import chain, cycle, tee, repeat, zip_longest, islice, \
    takewhile, dropwhile, filterfalse, product, permutations, combinations


s1 = range(10)
s2 = range(10, 20)
s3 = range(20, 30)

if __name__ == '__main__':
    # for s in chain(s1, s2, s3):
    #     print(s)
    #
    # for s in cycle(s1):
    #     print(s)

    # for s in tee(s1, 3):
    #     print([t for t in s])

    # for s in repeat(s1, 3):
    #     print(s)

    # 当函数的值对于所有元素都为真时，返回
    print(list(takewhile(lambda x: x >= 0, s1)))
