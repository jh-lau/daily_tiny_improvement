"""
  @Author       : liujianhan
  @Date         : 2020/12/21 17:49
  @Project      : DailyTinyImprovement
  @FileName     : argparse_demo_命令行传参.py
  @Description  : 另有命令行参数三方库：click：https://click-docs-zh-cn.readthedocs.io/zh/latest/
"""
import argparse
import sys

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-id', dest='assume_id', type=str, required=False)
    parser.add_argument('-url', dest='ws_url', type=str, required=False)
    args = parser.parse_args()
    # assume_id = '12345678'
    # url = 'ws://10.20.20.125:9903/combat'
    print(dir(args))