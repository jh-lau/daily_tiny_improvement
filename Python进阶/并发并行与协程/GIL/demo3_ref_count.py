"""
  @Author       : liujianhan
  @Date         : 20/10/2 20:07
  @Project      : DailyTinyImprovement
  @FileName     : demo3_ref_count.py
  @Description  : GIL解决了python中引用计数加锁的问题
"""
import sys

if __name__ == '__main__':
    a = [1, 1, 2]
    b = a
    print(sys.getrefcount(a) - 1)
    print(sys.getrefcount(b) - 1)
    print(sys.getrefcount([1, 1, 2]) - 1)
