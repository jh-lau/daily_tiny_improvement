"""
  @Author       : liujianhan
  @Date         : 2020/10/13 19:28
  @Project      : DailyTinyImprovement
  @FileName     : demo3_进程池下载国旗.py
  @Description  : Placeholder
"""
from concurrent import futures
import os
from demo1_顺序下载国旗 import save_flag, get_flag, show, main


def download_one(cc):
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    return cc


def download_many(cc_list):
    workers = min(os.cpu_count(), len(cc_list))
    with futures.ProcessPoolExecutor(workers) as executor:
        res = executor.map(download_one, sorted(cc_list))

    return len(list(res))


if __name__ == '__main__':
    main(download_many)
