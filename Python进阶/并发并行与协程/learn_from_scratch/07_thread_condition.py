"""
  @Author       : liujianhan
  @Date         : 21/1/27 22:47
  @Project      : DailyTinyImprovement
  @FileName     : 07_thread_condition.py
  @Description  : 复杂的线程同步
"""
import threading
from threading import Condition, Thread


class TianMao(Thread):
    def __init__(self, name, condition):
        super().__init__(name=name)
        self.condition = condition
        self.message = [
            '小爱同学',
            '我们来对古诗吧',
            '我住长江头',
            '日日思君不见君',
            '此水几时休',
            '只愿君心似我心'
        ]

    def run(self):
        with self.condition:
            for message in self.message:
                print(f'{self.name}: {message}')
                self.condition.notify()
                self.condition.wait()


class XiaoAi(Thread):
    def __init__(self, name, condition):
        super().__init__(name=name)
        self.condition = condition
        self.message = [
            '在呢',
            '好啊',
            '君住长江尾',
            '共饮长江水',
            '此恨何时已',
            '定不负相思意'
        ]

    def run(self) -> None:
        with self.condition:
            for message in self.message:
                self.condition.wait()
                print(f"{self.name}: {message}")
                self.condition.notify()


if __name__ == '__main__':
    cond = Condition()
    xiaoai = XiaoAi('小爱', cond)
    tianmao = TianMao('天猫精灵', cond)

    # 注意启动顺序很重要，此处tianmao先start()的话将无法正常执行下去
    # 原因是tianmao发出的notify信号xiaoai将无法收到，即其wait处无法通过notify进入

    # 调用with语句之后才能调用wait()，notify()

    # condition有两层锁，一把底层锁会在线程调用了wait方法的时候释放
    # 上面的锁会在每次调用wait的时候分配一把并放入到condition的等待队列中，等到notify方法唤醒
    xiaoai.start()
    tianmao.start()
