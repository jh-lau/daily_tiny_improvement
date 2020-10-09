"""
  @Author       : liujianhan
  @Date         : 2020/10/9 15:37
  @Project      : DailyTinyImprovement
  @FileName     : +=不等于=+.py
  @Description  : +=操作相当于extend，=+操作新增一个列表对象
"""

if __name__ == '__main__':
    a = [1, 2, 3, 4]
    b = a
    a = a + [5, 6, 7, 8]
    print(a)
    print(b)

    c = [1, 2, 3, 4]
    d = c
    c += [5, 6, 7, 8]
    print(c)
    print(d)
