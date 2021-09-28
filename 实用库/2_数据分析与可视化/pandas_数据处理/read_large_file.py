"""
  @Author       : liujianhan
  @Date         : 2021/6/24 8:58
  @Project      : DailyTinyImprovement
  @FileName     : read_large_file.py
  @Description  :
"""
import pandas as pd
import matplotlib.pyplot as plt
plt.show()
pd.set_option('display.max_columns', None)


def str_to_int_list(data):
    data = data.split(',')
    data = [int(s) for s in data if s.strip()]
    return data

if __name__ == '__main__':
    source = r'D:\Projects\basic-user-menstrual-predict\data\dataset\20210622_diary_menst_user_info___c8a2dd2d_6700_44ce_9655_ef76a9d2ef5b'
    target = r'D:\Projects\basic-user-menstrual-predict\data\dataset\source\20210623_diary_menst_user_info___c8a2dd2d_6700_44ce_9655_ef76a9d2ef5b'

    # with open(source, 'r', encoding='utf8') as s:
    #     with open(target, 'w', encoding='utf8') as t:
    #         for i, line in enumerate(s.readlines()):
    #             if i < 100_000:
    #                 t.writelines(f'{line}')
    # print('Done')

    df = pd.read_csv(target)
    df.columns = ['id', 'birthday', 'height', 'weight', 'province', 'city',
                  'is_marr', 'is_gest', 'ment_cycle', 'period_start_date',
                  'records', 'all_ment', 'all_dur', 'avg_ment', 'avg_dur']

    # get age
    df.birthday.fillna('1995-01-01', inplace=True)
    df.birthday = df.birthday.apply(lambda x: pd.to_datetime(x))
    df['age'] = pd.Timestamp.now() - df.birthday
    df.age = df.age.apply(lambda x: round(x.days/365))

    # set int
    df.is_marr.astype(int)
    df.is_gest.astype(int)

    print(df.head(5))
