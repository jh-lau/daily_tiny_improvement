"""
  @Author       : liujianhan
  @Date         : 2020/10/15 17:26
  @Project      : DailyTinyImprovement
  @FileName     : demo8_多线程的过程可视化测试.py
  @Description  : Placeholder
"""
from time import sleep, strftime
from concurrent.futures import ThreadPoolExecutor


def display(*args):
    print(strftime('[%H:%M:%S]'), end=' ')
    print(*args)


def loiter(n):
    msg = '{}loiter({}): doing nothing for {}s...'
    display(msg.format('\t' * n, n, n))
    sleep(n)
    msg = '{}loiter({}): done.'
    display(msg.format('\t' * n, n))
    return n * 10


def main():
    display('Script starting.')
    executor = ThreadPoolExecutor(max_workers=2)
    results = executor.map(loiter, range(5))
    display(f"results: {results}")
    display('Waiting for individual results:')
    for i, result in enumerate(results):
        display(f"result {i}: {result}")


if __name__ == '__main__':
    main()
