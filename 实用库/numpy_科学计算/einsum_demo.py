"""
  @Author       : liujianhan
  @Date         : 2021/1/26 10:14
  @Project      : DailyTinyImprovement
  @FileName     : einsum_demo.py
  @Description  : https://zhuanlan.zhihu.com/p/71639781
"""
import numpy as np


if __name__ == '__main__':
    a = np.random.randint(1, 10, (3, 3, 3))
    print(a)
    print(np.einsum('ijk->jk', a))