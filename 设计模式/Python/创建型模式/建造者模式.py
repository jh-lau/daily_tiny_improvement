"""
  @Author       : liujianhan
  @Date         : 21/1/1 18:27
  @Project      : DailyTinyImprovement
  @FileName     : 建造者模式.py
  @Description  : Placeholder
"""
import abc


# 步骤一：创建对应的产品抽象类/产品类
class Building(object):
    def __init__(self):
        self.floor = None
        self.size = None

    def __repr__(self):
        return 'Floor: {0.floor} | size: {0.size}'.format(self)


# 步骤三：创建构建者抽象类，主要是定义构建者通用属性/方法，以及继承者必须实现的功能抽象
# Abstract builder
class AbsBuilder(object):
    def __init__(self):
        self.building = None

    def new_building(self):
        self.building = Building()

    @abc.abstractmethod
    def build_floor(self):
        pass

    @abc.abstractmethod
    def build_size(self):
        pass


# 步骤四：具体构建者类实现
class HouseBuilder(AbsBuilder):
    def build_floor(self):
        self.building.floor = 'one'

    def build_size(self):
        self.building.size = '220 squre'


class FlatBuilder(AbsBuilder):
    def build_floor(self):
        self.building.floor = 'seven'

    def build_size(self):
        self.building.size = '140 squre'


# 步骤二：创建产品的指挥者类，即最终提供给客户端的产品的实例对象，以及组装过程
class Director(object):
    def __init__(self):
        self.builder = None

    def construct_building(self):
        """
        #建造者模式下，仅在需要时客户端代码才显式地请求指挥者返回最终的对象
        """
        self.builder.new_building()
        self.builder.build_floor()
        self.builder.build_size()

    def get_building(self):
        return self.builder.building


class Client(object):
    def build(self, build_type):
        if build_type == "House":
            director = Director()
            builder = HouseBuilder()
            director.builder = builder
            director.construct_building()
            building = director.get_building()
            print(building)
        else:
            director = Director()
            builder = FlatBuilder()
            director.builder = builder
            director.construct_building()
            building = director.get_building()
            print(building)


if __name__ == "__main__":
    build_type = "Flat"
    client = Client()
    client.build(build_type)
