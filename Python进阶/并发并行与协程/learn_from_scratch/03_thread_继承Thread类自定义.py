"""
  @Author       : liujianhan
  @Date         : 20/10/12 23:34
  @Project      : DailyTinyImprovement
  @FileName     : 03_thread_继承Thread类自定义.py
  @Description  : Placeholder
"""
from threading import Thread
import time


class GetUrl(Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print('get detail url started')
        time.sleep(5)
        print('get detail url ended.')


class GetHtml(Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self) -> None:
        print('get detail html started')
        time.sleep(2)
        print('get detail html ended.')


if __name__ == '__main__':
    t1 = GetHtml('get detail html')
    t2 = GetUrl('get detail url')
    s1 = time.time()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(f"last time: {time.time() - s1}")
