"""
  @Author       : liujianhan
  @Date         : 2021/6/23 16:40
  @Project      : DailyTinyImprovement
  @FileName     : iter_large_file.py
  @Description  : Placeholder
"""
import mmap
import time
from concurrent import futures

from tqdm import tqdm
from tqdm.contrib.concurrent import process_map


def get_num_lines(file_path):
    fp = open(file_path, "r+", encoding='utf8')
    buf = mmap.mmap(fp.fileno(), 0)
    lines = 0
    while buf.readline():
        lines += 1
    return lines


def sleep(x):
    print(x)
    pass


if __name__ == '__main__':
    file_path = r'D:\Projects\basic-user-menstrual-predict\data\dataset\source\20210622_diary_menst_user_info___c8a2dd2d_6700_44ce_9655_ef76a9d2ef5b'
    flag = 16
    # version1 no multiprocessing
    # with open(file_path, encoding='utf8') as file:
    #     if flag == 1:
    #         for line in tqdm_进度显示(file, total=get_num_lines(file_path)):
    #             pass
    # version2 no good
    # with futures.ProcessPoolExecutor(max_workers=8) as executor:
    #     with open(file_path, encoding='utf8') as file:
    #         results = list(tqdm_进度显示(executor.map(sleep, file), total=get_num_lines(file_path)))
    # version3 tqdm_进度显示 multiprocessing
    with open(file_path, encoding='utf8') as file:
        process_map(sleep, file)
