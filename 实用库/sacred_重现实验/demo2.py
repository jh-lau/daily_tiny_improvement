"""
  @Author       : liujianhan
  @Date         : 2020/12/21 18:05
  @Project      : DailyTinyImprovement
  @FileName     : demo1.py
  @Description  : Placeholder
"""
from sacred import Experiment

ex = Experiment('hello_config')
ex.add_config({'recipient2': 'what'})


@ex.config
def my_config():
    recipient = 'world'
    message = f"Hello {recipient}!"

@ex.automain
def my_main(message, recipient, recipient2):
    print(message, recipient, recipient2)


