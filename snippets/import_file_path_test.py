"""
  @Author       : liujianhan
  @Date         : 2020/1/10 下午2:03
  @Project      : DailyTinyImprovement
  @FileName     : import_file_path_test.py
  @Description  : Placeholder
"""
import sys
from os.path import dirname, abspath, basename, realpath, join
sys.path.append(abspath(dirname(__file__)))

if __name__ == '__main__':
    print(sys.path)
    print(abspath('.'))
    print('os basename:', basename(__file__))
    print('os dirname:', dirname(__file__))
    print('os abspath:', abspath(__file__))
    print('os realpath:', realpath(__file__))
    print('os dirname2:', dirname(realpath(__file__)))
    print(join(abspath(dirname(__file__)), 'src'))
    print(abspath(dirname(__file__)))