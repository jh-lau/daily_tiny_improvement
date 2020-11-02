"""
  @Author       : liujianhan
  @Date         : 2020/11/2 17:00
  @Project      : DailyTinyImprovement
  @FileName     : primes_py.py
  @Description  : Placeholder
"""


def primes_python(nb_primes):
    p = []
    n = 2
    while len(p) < nb_primes:
        # Is n prime?
        for i in p:
            if n % i == 0:
                break

        # If no break occurred in the loop
        else:
            p.append(n)
        n += 1
    return p
