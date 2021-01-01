"""
  @Author       : Liujianhan
  @Date         : 20/8/9 20:44
  @FileName     : zip_demo.py
  @ProjectName  : DailyTinyImprovement
  @Description  : Placeholder
 """
from pprint import pprint as print
from itertools import zip_longest

s = range(10)
t = 'abcdefghijklmnopqrst'
r = '!@$#%&^%&*(*&(())_'

a = {'flower', 'flow', 'floool'}
common_prefix_length = len([s for s in zip(*a) if len(set(s)) == 1])

if __name__ == '__main__':
    # print(list(zip(t, r, s)))
    # print(list(zip_longest(t, r, s)))
    print(common_prefix_length)
