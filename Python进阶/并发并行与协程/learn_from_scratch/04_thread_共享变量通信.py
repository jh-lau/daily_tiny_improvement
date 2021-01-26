"""
  @Author       : liujianhan
  @Date         : 21/1/26 23:00
  @Project      : DailyTinyImprovement
  @FileName     : 04_thread_共享变量通信.py
  @Description  : 线程间通信方式
  1. 共享变量（不推荐，需要加锁）
"""
import time
from threading import Thread

detail_url_list = []  # list不是线程安全的


def get_html(detail_url_list):
    """获取文章详情页"""
    while True:
        if detail_url_list:
            url = detail_url_list.pop()
            print(f'get detail {url} started')
            time.sleep(2)
            print(f'get detail {url} ended.')


def get_url(detail_url_list):
    """获取文章列表"""
    print('get detail url started')
    time.sleep(4)
    for i in range(20):
        detail_url_list.append(f'http://baidu.com/{i}')
    print('get detail url ended.')


if __name__ == '__main__':
    thread_detail_url = Thread(target=get_url, args=(detail_url_list, ))
    thread_detail_url.start()
    for i in range(10):
        html_thread = Thread(target=get_html, args=(detail_url_list, ))
        html_thread.start()
