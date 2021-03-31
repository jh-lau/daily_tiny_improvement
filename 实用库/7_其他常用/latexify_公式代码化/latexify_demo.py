"""
  @Author       : liujianhan
  @Date         : 2020/7/30 下午1:54
  @Project      : DailyTinyImprovement
  @FileName     : latexify_test.py
  @Description  : Placeholder
"""
import math
import latexify


@latexify.with_latex
def solve(a, b, c):
    return (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)


@latexify.with_latex
def sinc(x):
    if x == 0:
        return 1
    else:
        return math.sin(x) / x


@latexify.with_latex
def fib(x):
    if x == 0:
        return 1
    elif x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)


@latexify.with_latex
def formation(x, y, z):
    return math.fsum(x)


if __name__ == '__main__':
    print(formation)
