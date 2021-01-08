"""
  @Author       : liujianhan
  @Date         : 21/1/8 23:40
  @Project      : DailyTinyImprovement
  @FileName     : absl_demo.py
  @Description  : Placeholder
"""
from absl import app
from absl import flags

flag = flags.FLAGS
flags.DEFINE_string('name', None, 'Your name.')
flags.DEFINE_integer('num_times', 3, 'Number of times to print greeting.')

flags.mark_flag_as_required('name')


def main(argv):
    del argv
    for i in range(flag.num_times):
        print(f"Hello, {flag.name}")


if __name__ == '__main__':
    app.run(main)
