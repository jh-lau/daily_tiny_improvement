"""
  @Author       : liujianhan
  @Date         : 2020/12/21 17:49
  @Project      : DailyTinyImprovement
  @FileName     : argparser.py
  @Description  : 另有命令行参数三方库：click：https://click-docs-zh-cn.readthedocs.io/zh/latest/
"""
import argparse
import sys

if __name__ == '__main__':
    # parser = argparse.ArgumentParser(description='Process some integers')
    # parser.add_argument('integers', metavar='N', type=int, nargs='+',
    #                     help='an integer for the accumulator')
    # parser.add_argument('--sum', dest='accumulate', action='store_const',
    #                     const=sum, default=max, help='sum the integers (default: find the max)')
    # args = parser.parse_args()
    # print(args.accumulate(args.integers))
    print(sys.argv)
