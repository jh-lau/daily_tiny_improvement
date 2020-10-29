"""
  @Author       : liujianhan
  @Date         : 2020/10/29 10:51
  @Project      : DailyTinyImprovement
  @FileName     : 判断是否在字典内的效率对比.py
  @Description  : Placeholder
"""
from random import choice
from time import time

dic = {choice(range(20000)): k for k in range(1000)}

if __name__ == '__main__':
    key = choice(range(20000))
    num = int(1e7)
    t1 = time()
    for _ in range(num):
        if key in dic:
            pass
    print(f"elapsed time: {time() - t1: .3f} s")

    t2 = time()
    for _ in range(num):
        if key in dic.keys():
            pass
    print(f"elapsed time: {time() - t2: .3f} s")

    t3 = time()
    keys = dic.keys()
    for _ in range(num):
        if key in keys:
            pass
    print(f"elapsed time: {time() - t3: .3f} s")

    t4 = time()
    keys = set(dic.keys())
    for _ in range(num):
        if keys & {key}:
            pass
    print(f"elapsed time: {time() - t4: .3f} s")
