"""
  @Author       : Liujianhan
  @Date         : 20/8/12 22:53
  @FileName     : sort_with_condition.py
  @ProjectName  : DailyTinyImprovement
  @Description  : Placeholder
 """
from pprint import pprint as print

s = [(1, 'a', 131), (1, 'b', 11), (1, 'd', -1), (1, 'c', 190), (1, 'a', 2), (1, 'a', 13)]
r = [
    ({'LX': 11}, {'LX': 15}, 131),
    ({'LX': 11}, {'LX': 15}, 130),
    ({'LX': 11}, {'LX': 11}, 115),
    ({'LX': 11}, {'LX': 11}, 112),
    ({'LX': 11}, {'LX': 11}, 132),
    ({'LX': 15}, {'LX': 21}, 213),
    ({'LX': 15}, {'LX': 21}, 212),
    ({'LX': 15}, {'LX': 21}, 211),
    ({'LX': 21}, {'LX': 15}, 191),
    ({'LX': 21}, {'LX': 11}, 190),
    ({'LX': 21}, {'LX': 11}, 198),
    ({'LX': 21}, {'LX': 12}, 170),
    ({'LX': 21}, {'LX': 13}, 100),
    ({'LX': 21}, {'LX': 15}, 20),
    ({'LX': 21}, {'LX': 15}, 139)
]


def sort_func(x):
    if x[0]['LX'] == 21:
        return x[0]['LX'], x[1]['LX'], x[2]
    return x[0]['LX'], x[1]['LX'], -x[2]


if __name__ == '__main__':
    # s.sort(key=lambda x: x[1:])
    # print(s)
    # s.sort(key=lambda x: x[2])
    # print(s)
    # 按照第二个元素倒序，按照第三个元素升序排列
    # r.sort(key=lambda x: (x[0]['LX'], x[1]['LX'], -int(x[0]['LX'] == 21) * -x[2]))
    # print(r)
    r.sort(key=sort_func)
    print(r)
