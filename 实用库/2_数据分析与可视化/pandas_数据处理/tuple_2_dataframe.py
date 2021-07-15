"""
  @Author       : liujianhan
  @Date         : 21/7/11 23:07
  @Project      : DailyTinyImprovement
  @FileName     : tuple_2_dataframe.py
  @Description  : placeholder
"""

import pandas as pd

if __name__ == '__main__':
    file_path = '../../test.csv'
    df = pd.read_csv(file_path)
    new_df = pd.DataFrame(list(df.age.apply(lambda x: (x + 1, x - 1))), columns=['age', 'old_age'])
    df = pd.concat([df, new_df], axis=1)
