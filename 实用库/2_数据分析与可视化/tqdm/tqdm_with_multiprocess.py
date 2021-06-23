"""
  @Author       : liujianhan
  @Date         : 2021/6/23 12:21
  @Project      : DailyTinyImprovement
  @FileName     : test.py
  @Description  : Placeholder
"""
import os
import io
import time
from tqdm import tqdm
from concurrent import futures


def sleep(x):
    time.sleep(.1)
    return x ** 2


if __name__ == '__main__':
    flag = 3
    if flag == 1:
        for i in tqdm(range(100), total=100):
            sleep(i)
    elif flag == 2:
        with futures.ThreadPoolExecutor(max_workers=20) as executor:
            results = list(tqdm(executor.map(sleep, range(100)), total=100))
    elif flag == 3:
        with futures.ProcessPoolExecutor(max_workers=8) as executor:
            results = list(tqdm(executor.map(sleep, range(100)), total=100))
