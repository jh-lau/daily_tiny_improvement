"""
  @Author       : liujianhan
  @Date         : 2020/10/15 15:28
  @Project      : DailyTinyImprovement
  @FileName     : demo1_spinner_thread.py
  @Description  : Placeholder
"""
import threading
import itertools, time, sys


class Signal:  # 1
    go = True


def spin(msg, signal):  # 2
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):  # 3
        status = f'{char} {msg}'
        print(f"\r{status}", end='')
        # write(status)
        # flush()
        # write('\x08' * len(status))  # 4
        time.sleep(.1)
        # 控制线程退出的条件
        if not signal.go:  # 5
            break
    # write(' ' * len(status) + '\x08' * len(status))  # 6


def slow_function():  # 7
    time.sleep(3)  # 8
    return 42


# python没有提供终止线程的api，想关闭线程，必须给线程发送消息
def supervisor():  # 9
    signal = Signal()
    # 从属线程
    spinner = threading.Thread(target=spin,
                               args=('thinking!', signal))
    print('spinner object:', spinner)  # 10
    spinner.start()  # 11
    # 运行函数，sleep会阻塞主线程
    result = slow_function()  # 12
    signal.go = False  # 13
    spinner.join()  # 14
    return result


def main():
    result = supervisor()  # 15
    print('\rAnswer:', result)


if __name__ == '__main__':
    main()
