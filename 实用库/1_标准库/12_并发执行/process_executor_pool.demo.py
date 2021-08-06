"""
  @Author       : liujianhan
  @Date         : 2021/7/12 9:04
  @Project      : DailyTinyImprovement
  @FileName     : process_executor_pool.end_to_end_MLM_with_BERT.py
  @Description  : Placeholder
"""
import multiprocessing as mp
from concurrent.futures import ProcessPoolExecutor

import pandas as pd


def worker():
    pass


# method 1
# def main():
#     with open(target, encoding='utf8') as file:
#         print('starting working...')
#         with ProcessPoolExecutor(max_workers=mp.cpu_count()//2) as pool:
#             rs = pool.map(worker, file)
#             for res in rs:
#                 with open(result, 'a+') as writer:
#                     writer.writelines(f"{res}\n")

# method 2
def main():
    columns = ['name', 'age', 'gender']
    df = pd.read_csv(target, names=columns, chunksize=1000)
    print('starting working...')
    with ProcessPoolExecutor(max_workers=mp.cpu_count() // 2) as pool:
        pool.map(worker, df)


if __name__ == '__main__':
    target = 'demo_target.txt'
    main()
