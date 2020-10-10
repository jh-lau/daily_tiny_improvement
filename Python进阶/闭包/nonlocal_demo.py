"""
  @Author       : liujianhan
  @Date         : 2020/10/10 15:42
  @Project      : DailyTinyImprovement
  @FileName     : nonlocal_demo.py
  @Description  :
"""


def make_average_no_nonlocal():
    """
    此处不需要nonlocal关键字： 因为我们没有给 series 赋值，我们只是调
    用 series.append，并把它传给 sum 和 len。也就是说，我们利用了
    列表是可变的对象这一事实。
    :return:
    """
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return averager


def make_averager():
    """
    对数字、字符串、元组等不可变类型来说，只能读取，不能更新。
    如果尝试重新绑定，例如 count = count + 1，其实会隐式创建局部
    变量 count。这样，count 就不是自由变量了，因此不会保存在闭包
    中。
    :return:
    """
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count

    return averager


if __name__ == '__main__':
    avg = make_averager()
    avg2 = make_average_no_nonlocal()
    print(avg(10))
    print(avg(11))
    print(avg(12))
    print(avg2(10))
    print(avg2(11))
    print(avg2(12))
