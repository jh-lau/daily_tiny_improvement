"""
  @Author       : liujianhan
  @Date         : 21/1/26 23:14
  @Project      : DailyTinyImprovement
  @FileName     : 05_thread_queue通信.py
  @Description  : Placeholder
"""
import time
from threading import Thread
from queue import Queue  # 线程安全


def get_html(queue):
    """获取文章详情页"""
    while True:
        url = queue.get()  # 阻塞
        print(f'get detail {url} started')
        time.sleep(2)
        print(f'get detail {url} ended.')


def get_url(queue):
    """获取文章列表"""
    while True:
        print('get detail url started')
        time.sleep(4)
        for i in range(20):
            queue.put(f'http://baidu.com/{i}')
        print('get detail url ended.')


if __name__ == '__main__':
    detail_url_queue = Queue(maxsize=200)
    thread_detail_url = Thread(target=get_url, args=(detail_url_queue, ))
    thread_detail_url.start()
    for i in range(10):
        html_thread = Thread(target=get_html, args=(detail_url_queue, ))
        html_thread.start()

    detail_url_queue.task_done()
    detail_url_queue.join()