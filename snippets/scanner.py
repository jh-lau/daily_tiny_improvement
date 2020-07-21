"""
  @Author       : Liujianhan
  @Date         : 20/7/20 21:56
  @FileName     : scanner.py
  @ProjectName  : DailyTinyImprovement
  @Description  : Placeholder
 """
import os
import time
from concurrent import futures

from colorama import Fore

target_path = 'D:\\'
target_file_ext = 'txt,md,xlsx,xls,pdf,jpg,png,jpeg,bmp,docx,doc,tmp,log'.split(',')


def file_counter(file_path: str) -> int:
    counter = 0
    print(Fore.GREEN, f'Start counting in {file_path}')
    for root, _, files in os.walk(file_path):
        match = [os.path.join(root, file) for ext in target_file_ext for file in files if file.endswith(ext)]
        counter += len(match)

    return counter


def file_checker(file: str) -> None:
    pass


if __name__ == '__main__':
    # path_list = ['D:\\', 'E:\\', 'C:\\']
    path_list = [f'/{s}' for s in os.listdir('/')]
    start = time.time()
    counter = 0
    total_pics_file = []
    total_editable_file = []

    with futures.ProcessPoolExecutor() as pool:
        for number in pool.map(file_counter, path_list):
            counter += number
    print(Fore.WHITE, f'Time costs: {time.time() - start:.3f} --> {counter} files')

    print(total_editable_file[:10])
    print(total_pics_file[:10])
