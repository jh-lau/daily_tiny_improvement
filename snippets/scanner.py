"""
  @Author       : Liujianhan
  @Date         : 20/7/20 21:56
  @FileName     : scanner.py
  @ProjectName  : DailyTinyImprovement
  @Description  : Placeholder
 """
import asyncio
import os
import time
import multiprocessing
from concurrent import futures

target_path = 'D:\\'


# async def file_counter(file_path: str) -> int:
#     counter = 0
#     print(f'start counting in {file_path}')
#     for _, _, files in os.walk(file_path):
#         counter += len(files)
#     return counter

def file_counter(file_path: str) -> int:
    counter = 0
    print(f'start counting in {file_path}')
    for _, _, files in os.walk(file_path):
        counter += len(files)
    return counter


if __name__ == '__main__':
    path_list = ['D:\\', 'E:\\', 'C:\\']
    start = time.time()
    counter = 0
    # loop = asyncio.get_event_loop()
    # tasks = [file_counter(_) for _ in path_list]
    # loop.run_until_complete(asyncio.gather(*tasks))
    # for path in path_list:
    #     counter += file_counter(path)

    # process_list = []
    # for path in path_list:
    #     p = multiprocessing.Process(target=file_counter, args=(path,))
    #     process_list.append(p)
    #     p.start()
    #     p.join()

    with futures.ProcessPoolExecutor() as pool:
        for number in pool.map(file_counter, path_list):
            counter += number
    print(f'Time costs: {time.time() - start} --> {counter} files')
