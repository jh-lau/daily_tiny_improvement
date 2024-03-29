"""
  @Author       : liujianhan
  @Date         : 21/7/29 22:01
  @Project      : DailyTinyImprovement
  @FileName     : cheat_sheet.py
  @Description  :
"""
import pandas as pd

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_columns', None)
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

    # 列重排
    df = df[['a', 'c', 'd', 'b']]

    # 插入列
    df.insert(1, 'column_insert', '')

    # groupby之后保持索引
    df = df.groupby(['item_id', 'type']).tag_name.agg(lambda x: '-'.join(x))
    df.reset_index()

    # 排序
    df.sort_values(['a', 'b'], inplace=True)

    # 对多列进行函数调用
    f = lambda x: x - 1
    df['col_3'] = df[['col_1', 'col_2']].apply(lambda x: f(*x), axis=1)

    # from_dict
    test = {'a': [1,2, 3], 'b': [3,4, 5]}
    df = pd.DataFrame.from_dict(test, orient='index', columns=['id', 'title', 'content'])
