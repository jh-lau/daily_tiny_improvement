"""
  @Author       : liujianhan
  @Date         : 2021/7/21 10:30
  @Project      : DailyTinyImprovement
  @FileName     : set_options.py
  @Description  : Placeholder
"""
import pandas as pd

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_columns', None)

if __name__ == '__main__':
    df = pd.read_csv('file_path', names=['a', 'b', 'c'])
    df = df.astype({'a': int, 'b': float})
    # calculate not non value
    df.a.notna().sum()
    df.to_csv('file_path', index=False, header=False)
