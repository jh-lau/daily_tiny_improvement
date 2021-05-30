"""
  @Author       : liujianhan
  @Date         : 21/1/8 23:40
  @Project      : DailyTinyImprovement
  @FileName     : absl_demo.py
  @Description  : Placeholder
"""
from absl import app
from absl import flags, logging

FLAGS = flags.FLAGS

flags.DEFINE_string('name', None, 'Your name.')
flags.DEFINE_integer('num_times', 111, 'Number of times to print greeting.')

flags.mark_flag_as_required('name')


class Test:
    def __init__(self):
        if FLAGS.name:
            for _ in range(FLAGS.num_times):
                logging.info(f"Test, {FLAGS.name}")


def main(argv):
    del argv
    for i in range(FLAGS.num_times):
        print(f"{i} -- Hello, {FLAGS.name}")


if __name__ == '__main__':
    app.run(main)
