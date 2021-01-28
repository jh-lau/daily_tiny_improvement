"""
  @Author       : liujianhan
  @Date         : 21/1/28 23:19
  @Project      : DailyTinyImprovement
  @FileName     : 09_concurrent_futures.py
  @Description  : 线程池的场景需求
  主线程中可以获取某一个线程的状态或任务的状态及其返回值
  当一个线程完成的时候，主线程能立即知道
  futures可以让多线程和多进程的编码接口一致
"""
from concurrent import futures
import time


def get_html(times):
    time.sleep(times)
    print(f"Get page {times} successfully")
    return times


if __name__ == '__main__':
    mode = 4
    if mode == 1:
        # 1.单独写法
        executor = futures.ThreadPoolExecutor(max_workers=1)
        # 通过submit函数提交执行的函数到线程池中, submit为非阻塞，立即返回
        task1 = executor.submit(get_html, 3)
        task2 = executor.submit(get_html, 2)
        # 取消任务，成功取消返回True，否则返回False。已经启动的任务无法取消
        # 因为submit为非阻塞运行，因此要成功取消需要设定该线程还未开始执行就取消（max_workers设为1，确保任务2还没开始执行）
        print(task2.cancel())
        # done用于判定某个任务是否完成
        print(task1.done())
        # 获取task的执行结果
        print(task1.result())

    elif mode == 2:
        # 2.统一写法
        urls = [4, 2, 3]
        executor = futures.ThreadPoolExecutor(max_workers=3)
        all_task = [executor.submit(get_html, url) for url in urls]
        for future in futures.as_completed(all_task):
            data = future.result()
            # 输出无序，根据时间长短排序 2->3->4
            print(f"Get {data} page successfully.")

    elif mode == 3:
        # 3.map写法
        urls = [4, 2, 3]
        executor = futures.ThreadPoolExecutor(max_workers=3)
        for result in executor.map(get_html, urls):
            # 输出保持顺序：4->2->3
            print(f"Get {result} page successfully.")

    elif mode == 4:
        urls = [4, 2, 3]
        executor = futures.ThreadPoolExecutor(max_workers=3)
        all_task = [executor.submit(get_html, url) for url in urls]
        futures.wait(all_task, return_when=futures.FIRST_COMPLETED)
        print('Done.')
        """
        Get page 2 successfully
        Done.
        Get page 3 successfully
        Get page 4 successfully
        """
