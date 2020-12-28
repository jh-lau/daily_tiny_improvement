"""
  @Author       : liujianhan
  @Date         : 2020/12/28 14:51
  @Project      : DailyTinyImprovement
  @FileName     : signal_demo.py
  @Description  : https://juejin.cn/post/6844903733466251272
"""
import os
import signal
import sys
import time


def handle_int(sig, frame):
    print("get signal: %s, I will quit" % sig)
    sys.exit(0)


def handle_hup(sig, frame):
    print("get signal: %s" % sig)


if __name__ == "__main__":
    signal.signal(2, handle_int)
    signal.signal(1, handle_hup)
    print("My pid is %s" % os.getpid())
    while True:
        time.sleep(3)
