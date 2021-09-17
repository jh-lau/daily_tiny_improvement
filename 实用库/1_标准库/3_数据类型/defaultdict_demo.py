"""
  @Author       : Liujianhan
  @Date         : 20/8/10 22:23
  @FileName     : defaultdict_demo.py
  @ProjectName  : DailyTinyImprovement
  @Description  :
 """
from collections import defaultdict


def log_missing():
    print('Key added')
    return 0


if __name__ == '__main__':
    current = {'green': 12, 'blue': 3}
    increments = [
        ('red', 5),
        ('blue', 17),
        ('orange', 9)
    ]
    # defaultdict的第二个参数可以传入一个现有的字典，或者元组迭代器
    # 当查询的键不存在时，会调用log_missing对字典进行赋值
    # 如果log_missing返回的是列表，则相当于defaultdict(list)的用法
    result = defaultdict(log_missing, current)
    print(f'Before: {dict(result)}')
    for k, v in increments:
        result[k] += v
    print(f"After: {dict(result)}")
