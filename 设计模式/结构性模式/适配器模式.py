"""
  @Author       : liujianhan
  @Date         : 21/1/1 18:45
  @Project      : DailyTinyImprovement
  @FileName     : 适配器模式.py
  @Description  : Placeholder
"""


class Dog:
    def __init__(self, name):
        self.name = name

    def wangwang(self):
        print('my name is' + self.name + '。。。汪汪汪。。。')

    def dog_run(self):
        print(f'{self.name} is running')


class Cat:
    def __init__(self, name):
        self.name = name

    def miaomiao(self):
        print('my name is' + self.name + '。。。喵喵喵。。。')

    def cat_run(self):
        print(f'{self.name} is running')


class Sheep:
    def __init__(self, name):
        self.name = name

    def miemie(self):
        print('my name is' + self.name + '。。。咩咩。。。')

    def sheet_run(self):
        print(f'{self.name} is running')


class Adapter:
    def __init__(self, adapted_methods):
        self.__dict__.update(adapted_methods)

    def speak(self):
        pass

    def run(self):
        pass


def main():
    animals = []
    dog = Dog('旺财')
    cat = Cat('大脸猫')
    sheep = Sheep('喜洋洋')
    animals.append(Adapter({'speak': dog.wangwang, 'run': dog.dog_run}))
    animals.append(Adapter({'speak': cat.miaomiao, 'run': cat.cat_run}))
    animals.append(Adapter({'speak': sheep.miemie, 'run': sheep.sheet_run}))

    for a in animals:
        a.speak()
        a.run()


if __name__ == "__main__":
    main()
