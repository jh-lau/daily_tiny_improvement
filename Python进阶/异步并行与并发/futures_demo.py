"""
  @Author       : Liujianhan
  @Date         : 20/8/9 14:16
  @FileName     : futures_demo.py
  @ProjectName  : DailyTinyImprovement
  @Description  : Placeholder
 """
import time
from concurrent import futures


def sleep_func(args):
    duration, flag = args
    time.sleep(duration)
    # print(f'Done after {duration} seconds with flag {flag}')
    return duration, flag, f'{duration} >> {flag}'


s = zip(range(10), range(11, 21))

if __name__ == '__main__':
    s1 = time.time()
    # 设定并行使用的cpu数量
    with futures.ProcessPoolExecutor(max_workers=5) as pool:
        for duration, flag, result in pool.map(sleep_func, s):
            print(f"{duration} >> {flag} || {result}")

    # for t in s:
    #     duration, flag, result = sleep_func(t)
    #     print(f"{duration} >> {flag} || {result}")

    print(f'Time cost: {time.time() - s1: .3f} seconds')
