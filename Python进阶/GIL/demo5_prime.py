"""
  @Author       : liujianhan
  @Date         : 20/10/2 20:35
  @Project      : DailyTinyImprovement
  @FileName     : demo5_prime.py
  @Description  : 几种运行模式的效率比较
"""
import time
import threading
import multiprocessing as mp


def is_prime(num):
    assert num > 0
    for i in range(2, int((num ** .5) + 1)):
        if num % i == 0:
            return False
    return True


def prime(num):
    result = found_num = 0
    while found_num < num:
        result += 1
        found_num += int(is_prime(result))

    return result


if __name__ == '__main__':
    # 单进程单线程
    start = 100000
    t1 = time.time()
    for i in range(4):
        print(prime(i + start))
    print(f"Single process time cost: {time.time() - t1: .3f} seconds")
    "Single process time cost:  42.275 seconds"

    # 单进程4个线程
    t2 = time.time()
    jobs = []
    for i in range(4):
        jobs.append(threading.Thread(target=prime, args=(start+i, )))
    for job in jobs:
        job.start()
    for job in jobs:
        job.join()
    print(f"Multi-threads process time cost: {time.time() - t2: .3f} seconds")
    "Multi-threads process time cost:  40.640 seconds"

    # 4个独立进程
    t3 = time.time()
    jobs = []
    for i in range(4):
        jobs.append(mp.Process(target=prime, args=(start+i, )))
    for j in jobs:
        j.start()
    for j in jobs:
        j.join()
    print(f"Multi-processing process time cost: {time.time() - t3: .3f} seconds")
    "Multi-processing process time cost:  18.997 seconds"

    # 进程池
    t4 = time.time()
    pool = mp.Pool(processes=4)
    result = pool.map(prime, range(start, start+4))
    print(f"Pool time cost: {time.time() - t4: .3f} seconds")
    "Pool time cost:  15.963 seconds"
