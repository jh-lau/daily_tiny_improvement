"""
  @Author       : liujianhan
  @Date         : 2020/7/29 下午2:05
  @Project      : DailyTinyImprovement
  @FileName     : empty_list.py
  @Description  : Placeholder
"""


def func(a, list_=[]):
    for i in range(a):
        list_.append(i)
    print(list_)


if __name__ == '__main__':
    func(3)
    func(3, [1, 2, 3])
    func(4)
