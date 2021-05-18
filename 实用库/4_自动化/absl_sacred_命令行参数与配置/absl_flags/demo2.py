"""
  @Author       : liujianhan
  @Date         : 21/1/8 23:40
  @Project      : DailyTinyImprovement
  @FileName     : absl_demo.py
  @Description  : python demo2.py --name joye --num_times 123 --gender male --age 10
"""
import sys

from demo3 import *

FLAGS = flags.FLAGS

flags.DEFINE_string('name', None, 'Your name.')
flags.DEFINE_integer('num_times', 3, 'Number of times to print greeting.')
flags.DEFINE_enum('mode', 'a', ['a', 'b', 'c', 'd'], 'list of possible value of mode')

flags.mark_flag_as_required('name')
FLAGS(sys.argv)

if __name__ == '__main__':
    print(FLAGS.name)
    print(FLAGS.num_times)
    if FLAGS.mode.startswith('a'):
        print('hello')
    print(FLAGS.mode)
    print(FLAGS.age)
    print(FLAGS.gender)
