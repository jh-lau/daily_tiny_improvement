"""
  @Author       : liujianhan
  @Date         : 21/7/9 23:10
  @Project      : DailyTinyImprovement
  @FileName     : apply_async_demo.py
  @Description  : Placeholder
"""
import multiprocessing


def setcallback(x):
    with open('result.csv', 'a+') as f:
        f.writelines(f"{x}\n")


def multiplication(line):
    line = line.strip()
    return f"{line},hello"


if __name__ == '__main__':
    pool = multiprocessing.Pool(6)
    with open('test.csv') as file:
        for line in file:
            pool.apply_async(func=multiplication, args=(line,), callback=setcallback)
        pool.close()
        pool.join()
