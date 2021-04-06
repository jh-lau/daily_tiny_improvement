"""
  @Author       : liujianhan
  @Date         : 2020/11/14 14:45
  @Project      : DailyTinyImprovement
  @FileName     : 抽象工厂模式.py
  @Description  : https://github.com/faif/python-patterns/blob/master/patterns/creational/abstract_factory.py
"""
import random


class PetShop:
    def __init__(self, animal_factory=None):
        self.pet_factory = animal_factory

    def show_pet(self):
        pet = self.pet_factory()
        print(f"We have a lovely {pet}")
        print(f"It says {pet.speak()}")


class Dog:
    def speak(self):
        return 'woof'

    def __str__(self):
        return 'Dog'


class Cat:
    def speak(self):
        return 'Meow'

    def __str__(self):
        return 'Cat'


class Fox:
    def speak(self):
        return 'bilibili'

    def __str__(self):
        return 'Fox'


if __name__ == '__main__':
    cp = PetShop(Cat)
    cp.show_pet()

    shop = PetShop(random.choice([Dog, Cat, Fox]))
    shop.show_pet()
