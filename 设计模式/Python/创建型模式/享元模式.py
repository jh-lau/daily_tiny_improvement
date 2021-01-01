"""
  @Author       : liujianhan
  @Date         : 21/1/1 17:44
  @Project      : DailyTinyImprovement
  @FileName     : 享元模式.py
  @Description  : 注意和单例模式的区别：享元模式不实例化同样参数的对象，单例模式允许多实例化，只不过实例都是同一个

  享元模式通过为相似对象引入数据共享来最小化内存使用，提升性能，一个享元就是一个包含状态的独立的不可变数据的共享对象，
  依赖状态的可变数据不应是享元的一部分，因为每个对象的这种信息不相同，无法共享，如果享元需要非固有数据应该由客户端代码显示提供。
  享元模式介于单例模式和不加控制得多例模式之间。非常灵活，实用性和使用场景大于单例模式。
  例如创建一个数据库连接，不希望建立多个连接，但又要在同一解释器下操作好多台机器的数据库，当传参的机器的ip端口不同时候，
  那肯定要创建一个新的连接了，这种使用享元模式适合。
"""


class A:
    pool = dict()

    def __new__(cls, identity):
        """
        假设相同的学号只会有1个学生
        :param identity:
        :return:
        """
        obj = cls.pool.get(identity, None)
        if obj is None:
            obj = object.__new__(cls)
            print(f'实例化 学号为 {identity} 的学生')
            cls.pool[identity] = obj
        return obj

    def __init__(self, identity):
        self.identity = identity

    def eat(self):
        print(f'{self.identity} 吃饭')


if __name__ == '__main__':
    A('001').eat()
    A('001').eat()
    A('002').eat()
    print(A.pool)

    # 下面是关于这个享元模式被人说成是单例模式的反驳。如果是单例模式print(id(A('001')) == id(A('002'))) 结果会是True
    print(id(A('001')) == id(A('002')))  # False
    print(id(A('001')) == id(A('001')))  # True
