"""
  @Author       : liujianhan
  @Date         : 21/2/27 17:23
  @Project      : DailyTinyImprovement
  @FileName     : atexit_demo.py
  @Description  : Placeholder
"""
import atexit
import time


@atexit.register
def close():
    print('closing')


class Temp:
    @staticmethod
    def counting(num):
        while num:
            num -= 1
            time.sleep(1)
            # if num < 98:
            #     raise
            print(f"当前读数：{num}")


if __name__ == '__main__':
    t = Temp()
    t.counting(100)
