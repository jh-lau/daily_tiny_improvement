"""
  @Author       : Liujianhan
  @Date         : 20/8/12 22:53
  @FileName     : sort_with_condition.py
  @ProjectName  : DailyTinyImprovement
  @Description  : Placeholder
 """

s = [(1, 'a', 131), (1, 'b', 11), (1, 'd', -1), (1, 'c', 190), (1, 'a', 2), (1, 'a', 13)]
r = [(1, {'a': 12}, 131), (1, {'a': 11}, 11), (2, {'a': 11}, -1), (-1, {'a': 15}, 190), (1, {'a': 15}, 2),
     (1, {'a': 15}, 13)]

if __name__ == '__main__':
    # s.sort(key=lambda x: x[1:])
    # print(s)
    # s.sort(key=lambda x: x[2])
    # print(s)
    # 按照第二个元素倒序，按照第三个元素升序排列
    r.sort(key=lambda x: (x[0], -list(x[1].values())[0], x[2]))
    print(r)
