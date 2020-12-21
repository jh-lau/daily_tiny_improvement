"""
  @Author       : liujianhan
  @Date         : 2020/12/21 18:05
  @Project      : DailyTinyImprovement
  @FileName     : demo1.py
  @Description  : Placeholder
"""
from sacred import Experiment

ex = Experiment()


@ex.automain
def my_main():
    print('Hello world')
