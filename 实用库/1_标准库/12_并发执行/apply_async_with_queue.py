"""
  @Author       : liujianhan
  @Date         : 2021/7/12 9:01
  @Project      : DailyTinyImprovement
  @FileName     : apply_async_with_queue.py
  @Description  : Placeholder
"""
import multiprocessing as mp


def worker(content, q):
    s = content.split(',')[10]
    q.put(s)


def listener(q):
    with open(result, 'w') as f:
        while True:
            m = q.get()
            if m == 'kill':
                break
            f.write(f"{m}\n")
            f.flush()


def main():
    manager = mp.Manager()
    q = manager.Queue()
    pool = mp.Pool(mp.cpu_count() // 2)
    pool.apply_async(listener, (q,))
    jobs = []
    with open(target, 'r', encoding='utf8') as f:
        for line in f:
            job = pool.apply_async(worker, (line, q))
            jobs.append(job)

    for job in jobs:
        job.get()

    q.put('kill')
    pool.close()
    pool.join()


if __name__ == '__main__':
    target = 'demo_file.txt'
    result = 'demo_result.txt'
    main()
