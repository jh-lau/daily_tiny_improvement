"""
  @Author       : liujianhan
  @Date         : 2020/12/21 18:05
  @Project      : DailyTinyImprovement
  @FileName     : client.py
  @Description  : https://sacred.readthedocs.io/en/stable/configuration.html
"""
from sacred import Experiment

ex = Experiment()


@ex.automain
def my_main():
    print('Hello world')
