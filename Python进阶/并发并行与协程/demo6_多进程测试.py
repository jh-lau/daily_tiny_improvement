"""
  @Author       : liujianhan
  @Date         : 2020/10/14 16:20
  @Project      : DailyTinyImprovement
  @FileName     : demo6_多进程测试.py
  @Description  : Placeholder
"""
import math
from concurrent import futures
import time
from functools import wraps
import multiprocessing as mp
from dis import dis


def calc_distance(point):
    point1, point2 = point
    r = math.sqrt(sum(map(lambda x: (x[0] - x[1]) * (x[0] - x[1]), zip(point1, point2))))
    return r


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


def time_cost(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__doc__}耗时：{time.time() - t1:.2f} s")
        return result

    return wrapper


@time_cost
def gen_point_list(num):
    """距离点生成"""
    points = [(x, y) for x in range(num) for y in range(num)]
    # return [(x, y) for x in points for y in points]
    for point1 in points:
        for point2 in points:
            yield point1, point2


# @time_cost
def calc_simple(point_list):
    """直接顺序距离计算"""
    result = [calc_distance(x) for x in point_list]
    return result


@time_cost
def calc_simple_map(point_list):
    """map映射距离计算"""
    result = list(map(calc_distance, point_list))
    return result


@time_cost
def calc_mul_thread(point_list):
    """多线程距离计算"""
    max_worker = 10
    with futures.ThreadPoolExecutor(max_worker) as executor:
        result = executor.map(calc_distance, point_list)

    return result


# @time_cost
def calc_mul_proc(point_list):
    """多进程(进程池)距离计算"""
    with futures.ProcessPoolExecutor(4) as executor:
        result = executor.map(calc_distance, point_list)

    return result


@time_cost
def calc_simple_prime(num):
    """直接顺序质数计算"""
    result = [prime(num+x) for x in range(4)]
    return result


@time_cost
def calc_simple_map_prime(num):
    """map映射质数计算"""
    result = list(map(prime, [num+i for i in range(4)]))
    return result


@time_cost
def calc_mul_thread_prime(num):
    """多线程质数计算"""
    max_worker = 10
    with futures.ThreadPoolExecutor(max_worker) as executor:
        result = executor.map(prime, [num+i for i in range(4)])

    return result


@time_cost
def calc_mul_proc_prime(num):
    """多进程(进程池)质数计算"""
    with futures.ProcessPoolExecutor(4) as executor:
        result = executor.map(prime, [num+i for i in range(4)])

    return result


if __name__ == '__main__':
    # point_list = list(gen_point_list(10))
    # print(f"待计算距离数量：{len(point_list):,}")
    # dis(calc_simple)
    # dis(calc_mul_proc)
    # calc_mul_proc(point_list)
    # calc_simple(point_list)
    # calc_simple_map(point_list)
    # calc_mul_thread(point_list)

    # todo 如何获取单进程的结果
    s = gen_point_list(10)
    t3 = time.time()
    jobs = []
    for i in range(4):
        jobs.append(mp.Process(target=calc_distance, args=(next(s), )))
    for j in jobs:
        j.start()
    for j in jobs:
        j.join()
    print(f"Multi-processing process time cost: {time.time() - t3: .3f} seconds")

    num = 100_000
    # print(calc_simple_map_prime(num))
    # print(calc_simple_prime(num))
    # print(list(calc_mul_thread_prime(num)))
    # print(list(calc_mul_proc_prime(num)))
