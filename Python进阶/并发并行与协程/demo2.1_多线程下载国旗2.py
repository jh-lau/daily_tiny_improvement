"""
  @Author       : liujianhan
  @Date         : 2020/10/13 19:28
  @Project      : DailyTinyImprovement
  @FileName     : demo2.0_多线程下载国旗1.py
  @Description  : Placeholder
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
    cc_list = cc_list[:5]
    with futures.ThreadPoolExecutor(max_workers=3) as executor:
        to_do = []
        for cc in sorted(cc_list):
            # 创建Future实例
            future = executor.submit(download_one, cc)
            to_do.append(future)
            print(f'Scheduled for {cc}: {future}')

        results = []
        for future in futures.as_completed(to_do):
            res = future.result()
            print(f"{future} result: {res}")
            results.append(res)

    return len(results)


if __name__ == '__main__':
    main(download_many)
