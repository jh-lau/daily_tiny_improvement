"""
  @Author       : liujianhan
  @Date         : 2020/10/13 19:28
  @Project      : DailyTinyImprovement
  @FileName     : demo2.0_多线程下载国旗1.py
  @Description  : 多线程
"""
from concurrent import futures
from demo1_顺序下载国旗 import save_flag, get_flag, show, main

max_workers = 20


def download_one(cc):
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    return cc


def download_many(cc_list):
    workers = min(max_workers, len(cc_list))
    with futures.ThreadPoolExecutor(workers) as executor:
        res = executor.map(download_one, sorted(cc_list))

    return len(list(res))


if __name__ == '__main__':
    main(download_many)
