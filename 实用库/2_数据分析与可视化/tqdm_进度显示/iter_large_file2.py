"""
  @Author       : liujianhan
  @Date         : 2021/6/23 16:40
  @Project      : DailyTinyImprovement
  @FileName     : iter_large_file.py
  @Description  : Placeholder
"""
import mmap
import os
import time
from concurrent import futures

from tqdm import tqdm


def update(pbar):
    pbar.update(len(line.encode('utf8')))


if __name__ == '__main__':
    file_path = r'D:\Projects\basic-user-menstrual-predict\data\dataset\source\20210622_diary_menst_user_info___c8a2dd2d_6700_44ce_9655_ef76a9d2ef5b'
    with tqdm(total=os.path.getsize(file_path)) as pbar:
        with open(file_path, encoding='utf8') as file:
            for line in file:
                pbar.update(len(line.encode('utf-8')))
    #     else:
    #         with futures.ProcessPoolExecutor(max_workers=8) as executor:
    #             results = list(tqdm_进度显示(executor.map(sleep, file), total=get_num_lines(file_path)))
