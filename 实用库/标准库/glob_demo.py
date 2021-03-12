"""
  @Author       : liujianhan
  @Date         : 21/3/12 14:46
  @Project      : DailyTinyImprovement
  @FileName     : glob_demo.py
  @Description  : Placeholder
"""
from glob import glob

if __name__ == '__main__':
    target_file_ext = ['py', 'txt']
    t = [glob(f'*.{s}') for s in target_file_ext]
    print(t)