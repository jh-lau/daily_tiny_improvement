"""
  @Author       : liujianhan
  @Date         : 21/1/1 18:36
  @Project      : DailyTinyImprovement
  @FileName     : 桥接模式.py
  @Description  : Placeholder
"""


class A:
    def run(self, name):
        print("my name is :{}".format(name))


class B:
    def run(self, name):
        print("我的名字是：{}".format(name))


class Bridge:
    def __init__(self, ager, classname):
        self.ager = ager
        self.classname = classname

    def bridge_run(self):
        self.classname.run(self.ager)


if __name__ == '__main__':
    test = Bridge('李华', A())
    test.bridge_run()
    test.ager = 'Tome'
    test.bridge_run()
    test.classname = B()
    test.bridge_run()
    test.ager = '李华'
    test.bridge_run()
