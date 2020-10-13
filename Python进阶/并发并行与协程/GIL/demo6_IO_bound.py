"""
  @Author       : liujianhan
  @Date         : 20/10/2 23:08
  @Project      : DailyTinyImprovement
  @FileName     : demo6_IO_bound.py
  @Description  : IO密集型的任务，多线程优势比较明显
"""
import multiprocessing
import threading
import time

q = multiprocessing.Queue()


def init_queue():
    print('init q start')
    while not q.empty():
        q.get()
    for index in range(100):
        q.put(index)
    print('init q end')
    return


def task_io(task_id, q=q):
    print(f"IO task {task_id} start")
    while not q.empty():
        time.sleep(1)
        try:
            data = q.get(block=True, timeout=1)
            print(f"IO task {task_id} get data: {data}")
        except Exception as e:
            pass
            # print(f"IO task {task_id} error: {e}")
    print(f"IO task {task_id} end")
    return


if __name__ == '__main__':
    print(f"Cpu num: {multiprocessing.cpu_count()}\n")
    print(f"直接执行IO密集型任务")
    init_queue()
    time1 = time.time()
    task_io(0)
    print(f"结束后队列为空：{q.empty()}")
    print(f"结束：耗时 {time.time() - time1: .3f} 秒\n")

    print(f"多线程IO密集型任务")
    init_queue()
    time1 = time.time()
    # todo 1 注意todo1与todo2的传参区别：线程共用一个队列，因此args可以不传q
    thread_list = [threading.Thread(target=task_io, args=(i, )) for i in range(10)]
    for t in thread_list:
        t.start()
    for t in thread_list:
        if t.is_alive():
            t.join()
    print(f"结束后队列为空：{q.empty()}")
    print(f"结束耗时：{time.time() - time1:.3f} 秒\n")

    print(f"多进程IO密集型任务")
    init_queue()
    time1 = time.time()
    # todo 2 注意todo1与todo2的传参区别：多进程各自有一个队列，因此需要单独传入q
    # 可以通过任务管理器观察：多进程时会出现多个解释器运行
    process_list = [multiprocessing.Process(target=task_io, args=(i, q)) for i in range(8)]
    for p in process_list:
        p.start()
    for p in process_list:
        if p.is_alive():
            p.join()
    print(f"结束后队列为空：{q.empty()}")
    print(f"结束耗时：{time.time() - time1:.3f} 秒\n")

