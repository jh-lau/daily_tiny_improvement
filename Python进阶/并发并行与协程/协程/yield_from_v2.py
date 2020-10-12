"""
  @Author       : Liujianhan
  @Date         : 20/7/19 0:03
  @FileName     : yield_from_v2.py
  @ProjectName  : DailyTinyImprovement
  @Description  : Placeholder
 """
final_result = {}


# 子生成器
def sales_sum(pro_name):
    total = 0
    nums = []
    while True:
        x = yield
        print(f'{pro_name} 销量：{x}')
        if not x:
            break
        total += x
        nums.append(x)

    # 返回给委托生成器
    return total, nums


# 委托生成器
def middle(key):
    while True:
        final_result[key] = yield from sales_sum(key)
        print(key, '销量统计完成！')


def main():
    data_sets = {
        'django': [1200, 1400, 1242],
        'joey': [23, 54, 32],
        'ross': [123, 123, 213]
    }
    for key, _list in data_sets.items():
        print('start key:', key)
        m = middle(key)
        m.send(None)
        for value in _list:
            m.send(value)
        m.send(None)

    print('Final result:', final_result)


if __name__ == '__main__':
    main()
