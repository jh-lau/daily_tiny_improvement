"""
  @Author       : liujianhan
  @Date         : 20/10/18 22:14
  @Project      : DailyTinyImprovement
  @FileName     : demo10_condition.py
  @Description  : Placeholder
"""
from threading import Thread, Condition
import time
from collections import deque

items = deque(maxlen=10)
condition = Condition()


class Consumer(Thread):
    def __init__(self):
        super().__init__()

    @staticmethod
    def consume():
        global items, condition
        condition.acquire()
        if not items:
            condition.wait()
            print('Consumer notify: no item to consume')
        items.pop()
        print(f'Consumer notify: consumed 1 item, left: {len(items)}')
        condition.notify()
        condition.release()

    def run(self):
        for i in range(20):
            time.sleep(2)
            self.consume()


class Producer(Thread):
    def __init__(self):
        super().__init__()

    @staticmethod
    def produce():
        global items, condition
        condition.acquire()
        if len(items) == 10:
            condition.wait()
            print(f"Producer notify: reach max cap, stop producing.")
        items.appendleft(1)
        print(f"Producer notify: current producer cap: {len(items)}")
        condition.notify()
        condition.release()

    def run(self):
        for i in range(20):
            time.sleep(1)
            self.produce()


if __name__ == '__main__':
    producer = Producer()
    consumer = Consumer()
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()
