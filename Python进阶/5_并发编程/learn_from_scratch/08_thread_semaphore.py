"""
  @Author       : liujianhan
  @Date         : 21/1/28 23:09
  @Project      : DailyTinyImprovement
  @FileName     : 08_thread_semaphore.py
  @Description  : 用于控制进入数量的锁
"""
import time
from threading import Thread, Semaphore


class HtmlSpider(Thread):
    def __init__(self, url, sem):
        super().__init__()
        self.url = url
        self.sem = sem

    def run(self) -> None:
        time.sleep(2)
        print('Got html content successfully')
        # 2.注意释放的锁的位置
        self.sem.release()


class UrlProducer(Thread):
    def __init__(self, sem):
        super().__init__()
        self.sem = sem

    def run(self) -> None:
        for i in range(20):
            # 1.控制线程的数量
            self.sem.acquire()
            html_thread = HtmlSpider('www.baidu.com', self.sem)
            html_thread.start()


if __name__ == '__main__':
    sem = Semaphore(3)  # 控制同时运行线程的数量3
    url_producer = UrlProducer(sem)
    url_producer.start()
