"""
  @Author       : liujianhan
  @Date         : 2020/10/9 11:25
  @Project      : DailyTinyImprovement
  @FileName     : 读取大文件.py
  @Description  : 一行内容超过10G的文档要怎么读取
"""
from functools import partial


def read_from_large_file(filename, block_size=1024 * 8):
    with open(filename, 'r') as fp:
        for chunk in iter(partial(fp.read, block_size), ''):
            yield chunk


if __name__ == '__main__':
    pass
