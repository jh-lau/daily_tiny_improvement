"""
  @Author       : liujianhan
  @Date         : 2020/1/17 下午6:03
  @Project      : DailyTinyImprovement
  @FileName     : factorial_generator.py
  @Description  : 生成器计算阶乘
"""


def fac(n=1):
    fac_v = 1
    while True:
        fac_v *= n
        yield fac_v
        n += 1


if __name__ == '__main__':
    f = fac()
    next(f)
