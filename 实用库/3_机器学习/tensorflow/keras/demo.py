"""
  @Author       : liujianhan
  @Date         : 21/7/15 22:09
  @Project      : DailyTinyImprovement
  @FileName     : demo.py
  @Description  : Placeholder
"""
import tensorflow as tf

if __name__ == '__main__':
    filepath_dataset = tf.data.Dataset.list_files('data/covtype_data')
    print(filepath_dataset)
