"""
  @Author       : liujianhan
  @Date         : 21/7/29 22:01
  @Project      : DailyTinyImprovement
  @FileName     : cheat_sheet.py
  @Description  : Placeholder
"""
import pandas as pd


if __name__ == '__main__':
    file_path = 'data.csv'
    columns = ['a', 'b', 'c']
    df = pd.read_csv(file_path, names=columns, header=None)

    df.isnull.mean()
    df.isnull.sum()
    df.nunique()  # 统计不同值的数量
    label_freq = df.a.value_counts() / len(df)
    df.reset_index(drop=True, replace=True)

    # to category
    pd.get_dummies('data')
    df = df.content.astype('category').a.codes

    # 相同id下只选择某一条
    df.groupby(['id']).sample(1)

