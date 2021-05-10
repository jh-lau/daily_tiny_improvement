"""
  @Author       : liujianhan
  @Date         : 21/1/8 23:40
  @Project      : DailyTinyImprovement
  @FileName     : absl_demo.py
  @Description  : Placeholder
"""

from absl import flags

FLAGS = flags.FLAGS

flags.DEFINE_string('gender', None, 'Your gender.')
flags.DEFINE_integer('age', None, 'Your age')
flags.mark_flags_as_required(('gender', 'age'))

if __name__ == '__main__':
    pass
