"""
  @Author       : liujianhan
  @Date         : 2020/12/21 18:05
  @Project      : DailyTinyImprovement
  @FileName     : demo3.py
  @Description  : https://sacred.readthedocs.io/en/stable/configuration.html
"""
from sacred import Experiment

ex = Experiment('hello_config')


# @ex.config
# def my_config():
#     recipient = 'world'
#     message = f"Hello {recipient}!"


@ex.main
def my_main(message, recipient, recipient2):
    print(message)
    print(recipient)
    print(recipient2)


ex.add_config({'recipient2': 'what'})

if __name__ == '__main__':
    # python demo2.py with recipient="that is coolasdfasdf" message="yes" recipient2="123"
    ex.run_commandline()
